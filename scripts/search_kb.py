#!/usr/bin/env python3
"""Search guidance, exact official sources, observed sample graphs, and transcripts.

Standard-library BM25 retrieval, with title/path boosts and source-aware snippets.
No remote service, embedding model, API key, persistent index, or network needed.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"[A-Za-z0-9_]+")


def tokens(value):
    return [x.casefold() for x in TOKEN.findall(value)]


def documents(root, scope, family=None, version=None):
    found = []
    if scope in ("all", "sources"):
        inventory = root / "sources/inventory.jsonl"
        if inventory.exists():
            for line in inventory.read_text().splitlines():
                if not line.strip():
                    continue
                record = json.loads(line)
                if record.get("status") != "ok" or (family and record.get("source_family") != family) or (version and record.get("doc_version") != version):
                    continue
                name = record.get("text_path") or record.get("markdown_path")
                path = root / name if name else None
                if not path or not path.is_file():
                    continue
                found.append({"path": name, "markdown_path": record.get("markdown_path"), "kind": "source", "title": record.get("title", path.stem), "url": record.get("resolved_url", record["url"]), "version": record.get("doc_version"), "retrieved_at": record.get("retrieved_at"), "category": record.get("category"), "text": path.read_text()})
    if scope in ("all", "knowledge") and not family and not version:
        paths = set()
        for folder in ("knowledge", "docs", "patterns", "templates", "examples", "skills"):
            paths.update((root / folder).rglob("*.md"))
        paths.update(p for p in [root / "README.md", root / "AGENTS.md"] if p.is_file())
        for path in sorted(paths):
            content = path.read_text()
            title = next((line.lstrip("# ") for line in content.splitlines() if line.startswith("# ")), path.stem)
            found.append({"path": str(path.relative_to(root)), "kind": "knowledge", "title": title, "url": None, "text": content})
    if scope in ("all", "samples") and not family and not version:
        # One sanitized, attributed relationship record per reviewed sample.
        # Do not index raw imports, tenant payloads, or duplicate canvas captures.
        for path in sorted((root / "evidence/sample-flows/summaries").glob("*.json")):
            if path.name == "index.json":
                continue
            content = path.read_text()
            record = json.loads(content)
            if not record.get("sample_key"):
                continue
            found.append({"path": str(path.relative_to(root)), "kind": "sample",
                          "title": record.get("title", path.stem), "url": None,
                          "evidence_type": record.get("evidence_type"),
                          "runtime_tested": record.get("runtime_tested", False),
                          "walkthrough_status": record.get("walkthrough_status"),
                          "observed_at": record.get("observed_at"), "text": content})
    if scope in ("all", "transcripts") and not family and not version:
        # Only normalized transcript artifacts: no duplicate VTT/raw JSON/review files.
        for path in sorted((root / "transcripts").rglob("transcript.srt")):
            # Synthetic ASR fixtures are validation evidence, never tutorial knowledge.
            if any(part in {"fixtures", "local-asr-validation"} for part in path.relative_to(root / "transcripts").parts):
                continue
            metadata_path = path.with_name("metadata.json")
            if not metadata_path.is_file():
                continue
            metadata = json.loads(metadata_path.read_text())
            if metadata.get("evidence_type") == "synthetic_fixture":
                continue
            found.append({"path": str(path.relative_to(root)), "kind": "transcript", "title": metadata.get("title") or path.parent.name, "url": metadata.get("source"), "method": metadata.get("method"), "caption_kind": metadata.get("caption_kind"), "human_reviewed": metadata.get("human_reviewed", False), "retrieved_at": metadata.get("created_at"), "text": path.read_text()})
    return found


def best_snippets(content, query, maximum=3):
    candidates = []
    lines = content.splitlines()
    for index, line in enumerate(lines):
        line_terms = set(tokens(line))
        count = sum(term in line_terms for term in query)
        if count:
            # For field tables, preserve the matched row's exact local line.
            clean = re.sub(r"\s+", " ", line).strip()
            if len(clean) > 500:
                first = min((clean.casefold().find(t) for t in query if t in clean.casefold()), default=0)
                offset = max(0, first - 100)
                clean = ("…" if offset else "") + clean[offset:offset + 500] + "…"
            candidates.append((count, index + 1, clean))
    chosen = sorted(candidates, key=lambda x: (-x[0], x[1]))[:maximum]
    results = []
    for _, line, text in sorted(chosen, key=lambda x: x[1]):
        snippet = {"line": line, "text": text}
        for preceding in reversed(lines[max(0, line - 4):line - 1]):
            if re.match(r"\d\d:\d\d:\d\d,\d{3} -->", preceding):
                snippet["timestamp"] = preceding
                break
        results.append(snippet)
    return results


def search(root, query, limit=8, scope="all", family=None, version=None, require_all=False, phrase=False):
    terms = list(dict.fromkeys(tokens(query)))
    if not terms:
        return []
    corpus = documents(root, scope, family, version)
    term_counts = [Counter(tokens(d["text"])) for d in corpus]
    sizes = [sum(c.values()) for c in term_counts]
    avg_size = sum(sizes) / max(1, len(sizes))
    frequency = {t: sum(t in c for c in term_counts) for t in terms}
    ranked = []
    for doc, counts, size in zip(corpus, term_counts, sizes):
        matched = [t for t in terms if t in counts]
        if not matched or (require_all and len(matched) != len(terms)) or (phrase and query.casefold() not in doc["text"].casefold()):
            continue
        score = 0.0
        title_tokens = set(tokens(doc["title"] + " " + doc["path"]))
        for term in matched:
            idf = math.log(1 + (len(corpus) - frequency[term] + 0.5) / (frequency[term] + 0.5))
            tf = counts[term]
            score += idf * ((tf * 2.2) / (tf + 1.2 * (0.25 + 0.75 * size / max(1, avg_size))))
            if term in title_tokens:
                score += idf * 1.8
        # Favor matching the complete query without hiding partial useful results.
        score *= 0.5 + 0.5 * len(matched) / len(terms)
        result = {k: v for k, v in doc.items() if k != "text"}
        result.update({"score": round(score, 3), "matched_terms": matched, "snippets": best_snippets(doc["text"], terms)})
        ranked.append(result)
    return sorted(ranked, key=lambda d: (-d["score"], d["path"]))[:limit]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="Words, an exact field, or a quoted phrase")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--scope", choices=("all", "knowledge", "sources", "samples", "transcripts"), default="all")
    parser.add_argument("--family", help="Limit official sources, e.g. help or developer")
    parser.add_argument("--version", help="Limit to recorded documentation version (not a tenant version)")
    parser.add_argument("--all", action="store_true", dest="require_all", help="Require every query term")
    parser.add_argument("--phrase", action="store_true", help="Require literal case-insensitive phrase")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    query = " ".join(args.query)
    results = search(args.root.resolve(), query, args.limit, args.scope, args.family, args.version, args.require_all, args.phrase)
    if args.json:
        print(json.dumps({"query": query, "results": results}, indent=2, ensure_ascii=False))
    else:
        for index, r in enumerate(results, 1):
            print(f"{index}. {r['title']} [{r['kind']}; score {r['score']}]")
            print("   " + r["path"] + (" | docs " + str(r["version"]) if r.get("version") else ""))
            if r.get("url"):
                print("   " + r["url"])
            for snippet in r["snippets"]:
                print(f"   L{snippet['line']}" + (" [" + snippet["timestamp"] + "]" if snippet.get("timestamp") else "") + ": " + snippet["text"])
            print()
        if not results:
            print("No local matches. Try fewer terms, another scope, or ingest the missing source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
