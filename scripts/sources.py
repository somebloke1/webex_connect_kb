#!/usr/bin/env python3
"""Fetch official public documentation into a provenance-bearing local cache.

Uses only Python's standard library. No credentials, browser cookies, or proxy bypass.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HELP = "https://help.webexconnect.io/docs/introduction"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; WebexConnectLocalResearch/1.0)", "Accept": "text/html"}


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=45) as response:
        raw = response.read().decode("utf-8", errors="replace")
        return raw, response.geturl(), response.status


def parse_ssr(raw):
    match = re.search(r'<script\b[^>]*\bid=["\']ssr-props["\'][^>]*>(.*?)</script>', raw, re.S)
    if not match:
        raise ValueError("No ReadMe public SSR document found; no fallback to navigation-only text")
    result = json.loads(match.group(1))
    if result.get("is404"):
        raise ValueError("ReadMe reports is404")
    return result


class BodyText(HTMLParser):
    """Readable source body, including table cells, code and image descriptions."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
        self.headings = []
        self.heading = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style", "svg", "nav", "aside"}:
            self.skip += 1
        if self.skip:
            return
        if tag in {"p", "div", "section", "tr", "pre", "blockquote", "ul", "ol"}:
            self.parts.append("\n")
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n" + "#" * int(tag[1]) + " ")
            self.heading = []
        if tag == "li":
            self.parts.append("\n- ")
        if tag in {"td", "th"}:
            self.parts.append(" | ")
        if tag == "br":
            self.parts.append("\n")
        if tag == "img" and attrs.get("alt"):
            self.parts.append(" [Image: " + attrs["alt"] + "] ")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "svg", "nav", "aside"}:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self.heading is not None:
            self.headings.append("".join(self.heading).strip())
            self.heading = None
        if tag in {"p", "div", "section", "tr", "pre", "blockquote", "li", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)
            if self.heading is not None:
                self.heading.append(data)

    def text(self):
        return re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", "".join(self.parts)).strip() + "\n"


def readme_markdown(body, base, variables, links=None):
    """Convert ReadMe blocks to readable Markdown; retain unknown blocks verbatim."""
    for item in variables:
        body = body.replace("<<" + item["name"] + ">>", str(item.get("default", "")))
    body = re.sub(r"\]\(doc:([^ )#]+)([^ )]*)\)", lambda m: "](" + links[m[1]] + m[2] + ")" if links and m[1] in links else m[0], body)

    def block(match):
        kind, raw = match[1], match[2]
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return match[0]
        if kind == "code":
            return "\n\n" + "\n\n".join("```" + c.get("language", "") + "\n" + c.get("code", "") + "\n```" for c in data.get("codes", [])) + "\n\n"
        if kind == "image":
            return "\n\n" + "\n\n".join("![" + (i.get("caption") or i.get("image", ["", "", ""])[-1] or "Source screenshot") + "](" + i["image"][0] + ")" for i in data.get("images", []) if i.get("image")) + "\n\n"
        if kind == "callout":
            text = "**" + data.get("title", data.get("type", "Note")) + "**\n\n" + data.get("body", "")
            return "\n\n> " + text.replace("\n", "\n> ") + "\n\n"
        if kind == "parameters":
            cells, cols, rows = data.get("data", {}), data.get("cols", 0), data.get("rows", 0)
            def cell(key):
                return str(cells.get(key, "")).replace("|", "\\|").replace("\n", "<br>")
            if cols:
                lines = ["| " + " | ".join(cell("h-" + str(c)) for c in range(cols)) + " |", "| " + " | ".join("---" for _ in range(cols)) + " |"]
                lines += ["| " + " | ".join(cell(str(r) + "-" + str(c)) for c in range(cols)) + " |" for r in range(rows)]
                return "\n\n" + "\n".join(lines) + "\n\n"
        if kind == "html":
            return "\n\n" + data.get("html", "") + "\n\n"
        return match[0]
    return re.sub(r"\[block:([\w-]+)\]\s*(.*?)\s*\[/block\]", block, body, flags=re.S)


def nav_pages(pages):
    for page in pages:
        yield page
        yield from nav_pages(page.get("children", []))


def document_links(ssr, base):
    links = {}
    for section, categories in ssr.get("sidebars", {}).items():
        prefix = "reference" if section == "refs" else "docs"
        for category in categories:
            for page in nav_pages(category.get("pages", [])):
                for slug in [page.get("slug"), page.get("previousSlug")]:
                    if slug:
                        links[slug] = base + "/" + prefix + "/" + page["slug"]
    return links


def discover_help(output):
    raw, resolved, _ = fetch(DEFAULT_HELP)
    ssr = parse_ssr(raw)
    version = ssr.get("version", {}).get("version")
    seeds = []
    for category in ssr.get("sidebars", {}).get("docs", []):
        for page in nav_pages(category.get("pages", [])):
            if page.get("hidden") or page.get("link_external"):
                continue
            seeds.append({"url": "https://help.webexconnect.io/docs/" + page["slug"], "title": page.get("title"), "source_family": "help", "category": category.get("title"), "doc_version": version, "deprecated": bool(page.get("deprecated")), "discovered_from": resolved})
    # Preserve every visible help topic: even asset provisioning/compliance affects implementability.
    result = {"retrieved_at": utc_now(), "source": resolved, "default_version": version, "scope": "All visible platform-help navigation pages; API navigation is selected separately to exclude SDK internals.", "seeds": seeds}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    return result


def api_material(doc, ssr):
    """Include reference parameters/examples and OpenAPI operations outside doc.body."""
    api = doc.get("api", {})
    if not (doc.get("isApi") or doc.get("isReference")):
        return "", None, None
    oas = ssr.get("oasDefinition")
    public = {"api": api, "swagger": doc.get("swagger"), "oas_public_id": ssr.get("oasPublicUrl")}
    chunks = ["## API reference metadata", "", "These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.", "", "```json", json.dumps(api, indent=2, ensure_ascii=False), "```", ""]
    if isinstance(oas, dict):
        route = (doc.get("swagger") or {}).get("path") or api.get("url")
        method = api.get("method", "get").lower()
        routes = oas.get("paths", {})
        # Retain the actual route and selected operation; full schema is cached by hash.
        item = routes.get(route, {})
        operation = item.get(method, {})
        # ReadMe's swagger.path can be stale even when its current api.url or
        # operationId identifies the real public OpenAPI operation.
        if not operation and api.get("url") in routes:
            route = api["url"]
            item = routes[route]
            operation = item.get(method, {})
        if not operation:
            for candidate_route, candidate_item in routes.items():
                for candidate_method, candidate in candidate_item.items():
                    if isinstance(candidate, dict) and candidate.get("operationId") == doc.get("slug"):
                        route, method, item, operation = candidate_route, candidate_method, candidate_item, candidate
                        break
                if operation:
                    break
        selected = {"openapi": oas.get("openapi"), "info": {k: v for k, v in oas.get("info", {}).items() if k != "x-logo"}, "servers": oas.get("servers"), "security": oas.get("security"), "path": route, "method": method, "path_parameters": item.get("parameters", []), "operation": operation, "components": oas.get("components", {})}
        selected["operation_status"] = "selected" if operation else "not_present_in_supplied_openapi"
        public["selected_openapi"] = selected
        chunks += ["## OpenAPI operation and component schemas", "", "Operation extraction: " + selected["operation_status"] + ". Missing operation definitions must not be inferred from this cache.", "", "```json", json.dumps(selected, indent=2, ensure_ascii=False), "```", ""]
    return "\n".join(chunks), public, oas


class ArticleHTML(HTMLParser):
    """Capture one explicitly identified article element; fail if its markup changes."""
    def __init__(self, selector):
        super().__init__(convert_charrefs=False)
        self.selector, self.parts, self.stack = selector, [], []
        self.started = False
        self.complete = False

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        match = tag == self.selector.get("tag") and all(attr.get(k) == v for k, v in self.selector.items() if k != "tag")
        if not self.started and match:
            self.started = True
        if self.started and not self.complete:
            self.parts.append(self.get_starttag_text())
            if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
                self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.started and not self.complete:
            self.parts.append("</" + tag + ">")
            if tag in self.stack:
                while self.stack:
                    if self.stack.pop() == tag:
                        break
            if not self.stack:
                self.complete = True

    def handle_data(self, data):
        if self.started and not self.complete:
            self.parts.append(data)

    def handle_entityref(self, name):
        self.handle_data("&" + name + ";")

    def handle_charref(self, name):
        self.handle_data("&#" + name + ";")


def discover_changelog(output, pages=1):
    seeds = []
    for page in range(1, pages + 1):
        url = "https://help.webexconnect.io/changelog" + ("?page=" + str(page) if page > 1 else "")
        raw, resolved, status = fetch(url)
        ssr = parse_ssr(raw)
        for item in ssr.get("changelogs", []):
            seeds.append({"url": "https://help.webexconnect.io/changelog/" + item["slug"], "title": item["title"], "source_family": "changelog", "category": "Product and policy updates", "source_published_at": item.get("createdAt"), "discovered_from": resolved})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(seeds, indent=2, ensure_ascii=False) + "\n")
    return {"pages": pages, "sources": len(seeds), "path": str(output)}


def verify_cache(root):
    records = read_inventory(root / "sources/inventory.jsonl")
    errors, checked = [], 0
    for record in records.values():
        if record.get("status") != "ok":
            errors.append({"url": record["url"], "error": record.get("error", "Source not cached")})
            continue
        fields = dict(record.get("file_sha256", {}))
        for field, hash_field in [("api_metadata_path", "sha256_api_metadata"), ("openapi_path", "sha256_openapi")]:
            if record.get(field):
                fields[field] = record[hash_field]
        for field, expected in fields.items():
            path = root / record[field]
            checked += 1
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                errors.append({"url": record["url"], "path": str(path), "error": "Missing file or SHA256 mismatch"})
    return {"records": len(records), "checked_files": checked, "errors": errors, "verified_at": utc_now()}


class HTMLTree(HTMLParser):
    """Small article-only HTML tree used to preserve lists, links and table rows."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = {"tag": "root", "attrs": {}, "children": []}
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "children": []}
        self.stack[-1]["children"].append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1]["children"].append(data)


def article_markdown(body, url):
    tree = HTMLTree()
    tree.feed(body)
    def descendants(node, tag):
        for child in node["children"]:
            if isinstance(child, dict):
                if child["tag"] == tag:
                    yield child
                else:
                    yield from descendants(child, tag)
    def render(node):
        if isinstance(node, str):
            return re.sub(r"\s+", " ", node)
        tag, attrs = node["tag"], node["attrs"]
        if tag in {"nav", "script", "style", "svg", "aside"}:
            return ""
        content = "".join(render(child) for child in node["children"])
        anchor = ('\n<a id="' + html.escape(attrs["id"], quote=True) + '"></a>\n') if attrs.get("id") else ""
        if tag == "table":
            # Preserve original merged-cell tables as HTML rather than flattening their relationships.
            if any(descendants(node, "table")) or any(c["attrs"].get("rowspan") or c["attrs"].get("colspan") for c in list(descendants(node, "td")) + list(descendants(node, "th"))):
                return anchor + "\n\n" + serialize(node) + "\n\n"
            rows = []
            for row in descendants(node, "tr"):
                cells = [c for c in row["children"] if isinstance(c, dict) and c["tag"] in {"td", "th"}]
                if cells:
                    rows.append([re.sub(r"\n+", "<br>", render(c).strip()).replace("|", "\\|") for c in cells])
            if not rows:
                return ""
            width = max(map(len, rows))
            rows = [row + [""] * (width - len(row)) for row in rows]
            first_has_header = any(True for _ in descendants(node, "th"))
            if not first_has_header:
                rows.insert(0, [""] * width)
            lines = ["| " + " | ".join(row) + " |" for row in rows]
            lines.insert(1, "| " + " | ".join("---" for _ in range(width)) + " |")
            captions = [render(c).strip() for c in descendants(node, "caption")]
            return anchor + "\n\n" + "\n".join(captions + lines) + "\n\n"
        if tag == "a":
            href = attrs.get("href")
            return anchor + ("[" + content.strip() + "](" + urllib.parse.urljoin(url, href) + ")" if href and content.strip() else content)
        if tag == "img":
            src = attrs.get("src")
            return "![" + attrs.get("alt", "Source figure") + "](" + urllib.parse.urljoin(url, src) + ")" if src else ""
        if re.fullmatch(r"h[1-6]", tag):
            return anchor + "\n\n" + "#" * int(tag[1]) + " " + content.strip() + "\n\n"
        if tag == "br":
            return "\n"
        if tag in {"strong", "b"}:
            return "**" + content.strip() + "**" if content.strip() else ""
        if tag in {"code", "tt"}:
            return "`" + content.strip() + "`"
        if tag == "pre":
            parser = BodyText(); parser.feed(serialize(node))
            return "\n\n```text\n" + parser.text().strip() + "\n```\n\n"
        if tag == "li":
            return "\n- " + content.strip().replace("\n", "\n  ") + "\n"
        if tag in {"p", "div", "section", "article", "main", "ul", "ol", "blockquote"}:
            return anchor + "\n\n" + content.strip() + "\n\n"
        return anchor + content
    def serialize(node):
        if isinstance(node, str):
            return html.escape(node)
        if node["tag"] in {"nav", "script", "style", "svg", "aside"}:
            return ""
        attrs = "".join(" " + k + '="' + html.escape(v or "", quote=True) + '"' for k, v in node["attrs"].items())
        return "<" + node["tag"] + attrs + ">" + "".join(serialize(c) for c in node["children"]) + "</" + node["tag"] + ">"
    return re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", render(tree.root)).strip() + "\n"


def webex_help_article(raw):
    match = re.search(r'<script\b[^>]*\bid=["\']__NEXT_DATA__["\'][^>]*>(.*?)</script>', raw, re.S)
    if not match:
        raise ValueError("No Webex Help public Next.js article data")
    props = json.loads(match.group(1)).get("props", {}).get("pageProps", {})
    if props.get("finalError"):
        raise ValueError("Webex Help article reports an error")
    data = props.get("data") or {}
    chapters = props.get("chapters") or []
    body = "\n".join(chapter["divHtml"] for chapter in chapters) if chapters else props.get("UIData", "")
    parser = BodyText(); parser.feed(body)
    if len(parser.text().split()) < 30:
        raise ValueError("Webex Help article body missing or too short; blank book wrapper rejected")
    metadata = {k: data.get(k) for k in ["id", "externalId", "language", "status", "isBook", "creationTime", "lastModifiedTime", "lastSyncTime"]}
    metadata.update({"chapter_titles": [c["title"] for c in chapters], "table_count": len(re.findall(r"<table\b", body)), "products": data.get("metadata", {}).get("product"), "version_note": "No product documentation version supplied; use publisher lastModifiedTime and retrieval date."})
    metadata["title_raw"] = data.get("title")
    title = html.unescape(re.sub(r"<[^>]+>", "", data.get("title") or "")).strip()
    return {"doc": {"body": body, "title": title, "updatedAt": data.get("lastModifiedTime"), "_id": data.get("externalId")}, "rdmd": {"dehydrated": {"body": body}}, "publisher_metadata": metadata}


def source_id(seed):
    path = urllib.parse.urlsplit(seed["url"]).path.strip("/").replace("/", "--") or "index"
    path = re.sub(r"[^\w.-]+", "-", path)
    # keep conventional /docs/slug easy for authoring agents
    path = re.sub(r"^(docs|reference)--", "", path)
    return seed.get("source_family", "web") + "/" + path


def ingest_one(seed, root):
    record = dict(seed)
    record.update({"retrieved_at": utc_now(), "status": "pending", "source_kind": "official_documentation"})
    try:
        raw, resolved, status = fetch(seed["url"])
        if seed.get("extractor") == "webex_help_article":
            ssr = webex_help_article(raw)
        elif seed.get("extractor") == "html_element":
            article = ArticleHTML(seed["selector"])
            article.feed(raw)
            if not article.complete:
                raise ValueError("Selected article element not found or incomplete")
            body = "".join(article.parts)
            ssr = {"doc": {"body": body, "title": seed["title"]}, "rdmd": {"dehydrated": {"body": body}}}
        else:
            ssr = parse_ssr(raw)
        doc = ssr.get("doc") or ssr.get("changelog") or {}
        original = doc.get("body", "")
        rendered = ssr.get("rdmd", {}).get("dehydrated", {}).get("body", "")
        api_markdown, api_data, oas = api_material(doc, ssr)
        if not original and not rendered and not api_markdown:
            raise ValueError("Document body missing; navigation is not an acceptable source body")
        parser = BodyText()
        parser.feed(rendered)
        body_text = parser.text() if rendered else original
        base = urllib.parse.urlunsplit((*urllib.parse.urlsplit(resolved)[:2], "", "", ""))
        variables = ssr.get("context", {}).get("variables", {}).get("defaults", [])
        links = document_links(ssr, base)
        markdown = article_markdown(original, resolved) if seed.get("extractor") == "webex_help_article" else readme_markdown(original, base, variables, links)
        body_text = readme_markdown(body_text, base, variables, links)
        if not parser.headings:
            parser.headings = re.findall(r"^#{1,6} (.+)$", markdown, flags=re.M)
        if api_markdown:
            markdown += "\n\n" + api_markdown
            body_text += "\n\n" + api_markdown
        record.update({"status": "ok", "http_status": status, "resolved_url": resolved, "title": doc.get("title") or ssr.get("meta", {}).get("title") or seed.get("title"), "doc_version": ssr.get("version", {}).get("version"), "source_updated_at": doc.get("updatedAt"), "doc_id": doc.get("_id"), "headings": parser.headings, "word_count": len(body_text.split()), "sha256_source_body": sha(original), "sha256_html_response": sha(raw), "extraction": "ReadMe SSR doc.body + rdmd.dehydrated.body + reference API/OpenAPI metadata when present; navigation excluded", "deprecated": bool(doc.get("deprecated") or seed.get("deprecated"))})
        if seed.get("extractor") == "html_element":
            record["extraction"] = "Explicit article HTML element; document navigation excluded"
            record["source_kind"] = "official_article"
        if seed.get("extractor") == "webex_help_article":
            record["extraction"] = "Webex Help public Next.js pageProps.chapters[*].divHtml for books or UIData for articles; navigation excluded; headings, table cells and original links preserved"
            record["source_body_format"] = "html"
            record["publisher_metadata"] = ssr["publisher_metadata"]
        path = root / "sources/cache" / source_id(seed)
        path.parent.mkdir(parents=True, exist_ok=True)
        if ssr.get("changelog"):
            record["source_kind"] = "official_changelog"
            release = re.search(r"v(\d+\.\d+\.\d+)", record["title"])
            record["release_version"] = release.group(1) if release else None
        if api_data:
            schema_file = path.with_suffix(".api.json")
            schema_body = json.dumps(api_data, indent=2, ensure_ascii=False) + "\n"
            schema_file.write_text(schema_body)
            record["api_metadata_path"] = str(schema_file.relative_to(root))
            record["sha256_api_metadata"] = sha(schema_body)
        if isinstance(oas, dict):
            schema_body = json.dumps(oas, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
            schema_file = root / "sources/cache/openapi" / (sha(schema_body) + ".json")
            schema_file.parent.mkdir(parents=True, exist_ok=True)
            schema_file.write_text(schema_body)
            record["openapi_path"] = str(schema_file.relative_to(root))
            record["sha256_openapi"] = sha(schema_body)
        # Keep the exact author-source separately from normalized readable Markdown.
        files = {"source_path": (path.with_suffix(".source.md"), original), "markdown_path": (path.with_suffix(".md"), "# " + record["title"] + "\n\nSource: " + resolved + "\nDocumentation version: " + (record["doc_version"] or "not specified by publisher") + ("\nSource last modified: " + record["source_updated_at"] if record.get("source_updated_at") else "") + "\nRetrieved: " + record["retrieved_at"] + "\n\n" + markdown), "text_path": (path.with_suffix(".txt"), body_text)}
        hashes = {}
        for key, (file, content) in files.items():
            file.write_text(content, encoding="utf-8")
            record[key] = str(file.relative_to(root))
            hashes[key] = sha(content)
        record["file_sha256"] = hashes
        record["metadata_path"] = str(path.with_suffix(".metadata.json").relative_to(root))
        (path.with_suffix(".metadata.json")).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    except (urllib.error.URLError, ValueError, KeyError, TypeError, OSError) as exc:
        record.update({"status": "error", "error": str(exc), "http_status": getattr(exc, "code", None)})
    return record


def load_seeds(paths):
    seeds = {}
    for path in paths:
        data = json.loads(path.read_text())
        if isinstance(data, dict):
            data = data["seeds"]
        for seed in data:
            seeds[seed["url"]] = seed
    return list(seeds.values())


def read_inventory(path):
    if not path.exists():
        return {}
    return {r["url"]: r for line in path.read_text().splitlines() if line.strip() for r in [json.loads(line)]}


def write_inventory(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in sorted(records.values(), key=lambda r: r["url"])))
    temporary.replace(path)


def build_coverage(root, records):
    from collections import Counter
    counts = Counter(r["source_family"] for r in records)
    statuses = Counter(r["status"] for r in records)
    versions = Counter(str(r.get("doc_version") or "unspecified") for r in records)
    latest_release = max((r for r in records if r.get("release_version")), key=lambda r: tuple(int(x) for x in r["release_version"].split(".")), default=None)
    navigation = json.loads((root / "sources/api-navigation.json").read_text()) if (root / "sources/api-navigation.json").exists() else {}
    coverage = {
        "generated_at": utc_now(),
        "declared_scope": "All visible official platform-help navigation pages; all public developer API references plus app asset/profile prerequisites; current-page release and policy notices; selected Cisco tutorial; AI Agent Studio administration guide and directly linked essential articles.",
        "total_sources": len(records), "status_counts": dict(statuses), "source_family_counts": dict(counts),
        "documentation_version_counts": dict(versions), "rendered_word_count": sum(r.get("word_count", 0) for r in records),
        "categories": [{"source_family": family, "category": category, "total": sum(r["source_family"] == family and r.get("category") == category for r in records), "cached": sum(r["source_family"] == family and r.get("category") == category and r["status"] == "ok" for r in records)} for family, category in sorted(set((r["source_family"], r.get("category", "Uncategorized")) for r in records))],
        "developer_navigation_selection": navigation.get("counts", {}),
        "latest_observed_release_notice": {k: latest_release.get(k) for k in ["title", "url", "release_version", "source_published_at"]} if latest_release else None,
        "version_note": "Default help/developer documentation versions and release-notice versions can differ. Neither proves a tenant deployment version.",
        "api_metadata_documents": sum(bool(r.get("api_metadata_path")) for r in records),
        "openapi_documents": sum(bool(r.get("openapi_path")) for r in records),
        "unique_openapi_snapshots": len(set(r["openapi_path"] for r in records if r.get("openapi_path"))),
        "studio_source_count": sum(r.get("source_family") == "studio" for r in records),
        "studio_table_count": sum(r.get("publisher_metadata", {}).get("table_count", 0) for r in records if r.get("source_family") == "studio"),
        "limitations": ["SDK implementation navigation excluded; its app asset/profile prerequisites are included.", "Images are linked to official originals; prose and schemas are local. Visual-only labels still require the source image or tenant UI.", "Four SMS narrative reference pages supply no OpenAPI operation; cached API parameters/examples and narrative remain available.", "Optional Cisco support article 222936 direct retrieval returned HTTP 403; its reviewed citation is retained in authored knowledge but it is outside this cached manifest.", "No tenant configuration or messaging action performed by this source workflow."]
    }
    (root / "sources/coverage.json").write_text(json.dumps(coverage, indent=2, ensure_ascii=False) + "\n")
    return coverage


def build_studio_index(root, records):
    studio = [r for r in records if r.get("source_family") == "studio" and r.get("status") == "ok"]
    if not studio:
        return
    lines = ["# AI Agent Studio source index", "", "Local full-text references for AI Agent Studio design and configuration. Source modification dates are publisher metadata; these articles do not supply a product documentation version. Keep Connect AI Agent node contracts separate from Studio configuration and from Contact Center voice Flow Designer.", "", "| Reference | Local full text | Publisher modified | Tables |", "| --- | --- | --- | ---: |"]
    for record in sorted(studio, key=lambda r: r["title"]):
        path = Path(record["markdown_path"])
        lines.append("| [" + record["title"] + "](" + record["url"] + ") | [local](" + str(path.relative_to("sources")) + ") | " + str(record.get("source_updated_at")) + " | " + str(record.get("publisher_metadata", {}).get("table_count", 0)) + " |")
    guide = next((r for r in studio if r["url"].endswith("/ncs9r37")), None)
    if guide:
        lines += ["", "## Administration guide section jumps", "", "The cached guide contains all seven original chapters. These jumps retain the publisher's exact section IDs; full field tables and screenshots are available in the local guide and its original source links.", ""]
        content = (root / guide["markdown_path"]).read_text()
        seen = set()
        for anchor, level, title in re.findall(r'<a id="([^"<>]+)"></a>\s*\n(#{1,6}) ([^\n]+)', content):
            if title in seen or len(level) > 4:
                continue
            seen.add(title)
            lines.append("- [" + title.replace("**", "") + "](cache/studio/article--ncs9r37.md#" + anchor + ")")
    lines += ["", "Acquisition and hashes: [inventory](inventory.jsonl). Measured scope: [coverage](coverage.json). Refresh these sources using the `supplemental-seeds.json` manifest and `scripts/sources.py`.", ""]
    (root / "sources/studio-index.md").write_text("\n".join(lines))


def build_catalog(root):
    inventory = read_inventory(root / "sources/inventory.jsonl")
    records = list(inventory.values())
    build_coverage(root, records)
    build_studio_index(root, records)
    by_category = {}
    for r in records:
        by_category.setdefault((r.get("source_family", "web"), r.get("category", "Uncategorized")), []).append(r)
    lines = ["# Official source catalog", "", "Generated from `sources/inventory.jsonl`. Local cache is research material and is excluded from version control; source rights remain with their owners.", "", f"Catalog generated: {utc_now()}", "", f"Sources: {len(records)}; successfully cached: {sum(r['status'] == 'ok' for r in records)}; unavailable: {sum(r['status'] != 'ok' for r in records)}.", "", "The recorded documentation version describes the retrieved documentation, not any tenant's deployed product version.", ""]
    for (family, category), group in sorted(by_category.items()):
        lines += [f"## {family}: {category}", "", "| Source | Version | Local Markdown | Words | Status |", "| --- | --- | --- | ---: | --- |"]
        for r in sorted(group, key=lambda r: r.get("title") or r["url"]):
            title = (r.get("title") or r["url"]).replace("|", "\\|")
            local = "[cache](../" + r["markdown_path"] + ")" if r.get("markdown_path") else "—"
            lines.append(f"| [{title}]({r['url']}) | {r.get('doc_version') or 'unspecified'} | {local} | {r.get('word_count', 0)} | {r['status']} |")
        lines.append("")
    (root / "sources/catalog.md").write_text("\n".join(lines))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    discover = sub.add_parser("discover", help="Discover current official platform-help navigation")
    discover.add_argument("--output", type=Path, default=ROOT / "sources/help-seeds.json")
    ingest = sub.add_parser("ingest", help="Fetch selected official sources; resumes completed records")
    ingest.add_argument("--seeds", type=Path, nargs="+", required=True)
    ingest.add_argument("--workers", type=int, default=4)
    ingest.add_argument("--refresh", action="store_true")
    ingest.add_argument("--limit", type=int)
    ingest.add_argument("--match", default="", help="Only URLs containing this string")
    sub.add_parser("catalog")
    sub.add_parser("verify", help="Verify all cache file SHA256 values and report unavailable sources")
    changes = sub.add_parser("discover-changelog", help="Discover current release/policy notices")
    changes.add_argument("--output", type=Path, default=ROOT / "sources/changelog-seeds.json")
    changes.add_argument("--pages", type=int, default=1)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.command == "discover":
        result = discover_help(args.output)
        print(json.dumps({"sources": len(result["seeds"]), "default_version": result["default_version"], "path": str(args.output)}))
    elif args.command == "verify":
        result = verify_cache(root)
        print(json.dumps(result, indent=2))
        return int(bool(result["errors"]))
    elif args.command == "discover-changelog":
        print(json.dumps(discover_changelog(args.output, args.pages)))
    elif args.command == "catalog":
        build_catalog(root)
    elif args.command == "ingest":
        inventory_path = root / "sources/inventory.jsonl"
        records = read_inventory(inventory_path)
        seeds = load_seeds(args.seeds)
        seeds = [s for s in seeds if args.match in s["url"] and (args.refresh or records.get(s["url"], {}).get("status") != "ok" or not (root / records[s["url"]].get("markdown_path", "missing")).is_file())]
        if args.limit:
            seeds = seeds[:args.limit]
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, min(args.workers, 8))) as pool:
            for future in concurrent.futures.as_completed([pool.submit(ingest_one, seed, root) for seed in seeds]):
                record = future.result()
                previous = records.get(record["url"], {})
                if previous.get("sha256_source_body") and record.get("sha256_source_body"):
                    record["previous_retrieved_at"] = previous.get("retrieved_at")
                    record["previous_sha256_source_body"] = previous.get("sha256_source_body")
                    record["source_body_changed"] = previous["sha256_source_body"] != record["sha256_source_body"]
                records[record["url"]] = record
                if record.get("status") == "ok" and record.get("metadata_path"):
                    (root / record["metadata_path"]).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
                write_inventory(inventory_path, records)
                print(record["status"], record["url"], record.get("word_count", record.get("error")), flush=True)
        build_catalog(root)
        failures = sum(records[s["url"]]["status"] != "ok" for s in seeds)
        print(json.dumps({"attempted": len(seeds), "failed": failures, "inventory": str(inventory_path)}))
        return int(bool(failures))
    return 0


if __name__ == "__main__":
    sys.exit(main())
