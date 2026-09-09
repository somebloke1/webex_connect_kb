#!/usr/bin/env python3
"""Refresh the sample coverage ledger from local acquisition and canvas evidence.

No network or tenant actions. Documentation status is curated below; a capture
never implies runtime execution. Re-run after adding sanitized observations or
their derived summaries. Paths in the JSON are workspace-relative.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "evidence/sample-flows"
CH15 = "knowledge/15-sample-flow-walkthroughs.md"
CH16 = "knowledge/16-additional-sample-walkthroughs.md"


def read(path):
    return json.loads((ROOT / path).read_text())


def key(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    records = []

    def add(cohort, name, sources, *, relevant=True, reason="AI Agent, email/SMS, or required task-event companion", doc="not_reviewed", walkthrough=None, **extra):
        row = {
            "id": f"{cohort}:{key(name)}", "cohort": cohort, "name": name,
            "in_collection_scope": True, "in_priority_scope": relevant, "scope_reason": reason,
            "source_urls": sources, "documentation_review": doc,
            "documentation_walkthrough": walkthrough,
            "artifact_status": "not_acquired", "ui_graph_capture": "not_observed",
            "ui_graph_summary": "not_available", "ui_walkthrough_status": "not_available", "runtime_tested": False,
        }
        row.update(extra)
        records.append(row)
        return row

    gallery = [
        "AI Agent Scripted Doctor Appointment", "AI Agent Livechat Generic",
        "AI Agent Fulfilment - Track Package", "LogisticsParcelNotifications",
        "WebhooktoSMSalerts", "SMSSurvey", "Chatbot", "Autoresponder",
        "AppointmentReminder",
    ]
    for name in gallery:
        ai = name.startswith("AI Agent")
        add("tenant_gallery", name,
            ["https://help.webexconnect.io/docs/using-ai-agent-flow-templates"] if ai else [],
            reason="All nine entries in the authenticated tenant sample gallery",
            doc="documented_topology" if ai else "no_separate_public_walkthrough",
            walkthrough=CH15 if ai else None, artifact_status="tenant_gallery_template",
            identity_evidence="Exact labels in observed/*.json; Start from Scratch is not a sample")

    for item in read("evidence/sample-flows/public-native-manifest.json"):
        add("ai_fulfilment_repository", item["file"], [item["source_url"]],
            doc="artifact_acquisition_only", walkthrough=CH15,
            artifact_status="downloaded_opaque_workflow",
            artifact_path=f"evidence/sample-flows/raw/{item['file']}",
            acquisition_manifest="evidence/sample-flows/public-native-manifest.json",
            sha256=item["sha256"],
            limitation="Acquisition-stage JSON/hex checks did not yield nodes or edges; consult later UI evidence separately")

    for slug in ["patient-match-epic-ehr-flow-template", "get-future-appointments-flow-template", "confirm-appointment-flow-template", "cancel-appointment-flow-template", "epic-reschedule-appointment-flow-template"]:
        text = (ROOT / f"sources/cache/help/{slug}.md").read_text()
        add("epic_documented_template", text.splitlines()[0].removeprefix("# "),
            [f"https://help.webexconnect.io/docs/{slug}"], doc="documented_topology",
            walkthrough=CH15, source_cache=f"sources/cache/help/{slug}.md")

    for slug, chapter, diagram in [
        ("sending-automated-sms", CH16, "evidence/sample-flows/automated-sms-diagram.json"),
        ("setup-appointment-reminder-webexconnect", CH15, "evidence/sample-flows/appointment-reminder-diagram.json"),
    ]:
        add("sms_tutorial", slug, [f"https://help.webexconnect.io/docs/{slug}"],
            doc="documented_and_diagram_topology", walkthrough=chapter,
            diagram_evidence=diagram, source_cache=f"sources/cache/help/{slug}.md")
    add("sms_tutorial", "Developer appointment webhook tutorial",
        ["https://developer.webex.com/blog/build-your-first-webex-connect-flow-a-step-by-step-guide"],
        doc="documented_topology", walkthrough=CH16,
        source_cache="sources/cache/cisco/blog--build-your-first-webex-connect-flow-a-step-by-step-guide.txt")
    add("studio_tutorial", "Scripted Track Package fulfillment",
        ["https://help.webex.com/article/mzpuseb"],
        doc="documented_topology", walkthrough="knowledge/13-ai-agent-flows.md",
        source_cache="sources/cache/studio/article--mzpuseb.md",
        identity_note="Separate public Studio walkthrough; not asserted identical to the tenant gallery Track Package")

    downloads = {r["repository_path"]: r for r in read("evidence/sample-flows/public-wxcc-manifest.json")}
    tree = read("evidence/sample-flows/raw/webexcc-digital-channels-tree.json")
    for entry in tree["tree"]:
        path = entry["path"]
        if not path.startswith("Webex Connect Flows/v3.5/") or not path.endswith(".zip"):
            continue
        acquired = downloads.get(path)
        # Priority is a retrieval tag only: every current v3.5 archive is included.
        relevant = any(s in path for s in ["/Bot Flows/", "/Usage of Contact Priority", "/Usage of Set Variable", "/Usage of Screen Pop", "/Event Handling Workflows/", "EmailAttachment", "EmailInboundFlow", "SMS inbound"])
        src = f"https://github.com/CiscoDevNet/webexcc-digital-channels/blob/{tree['sha']}/{quote(path)}"
        row = add("wxcc_repository_v3_5", Path(path).name, [src], relevant=relevant,
            reason="AI/SMS/email sample or task-context companion" if relevant else "Additional channel sample included to cover the whole current collection",
            doc="artifact_only_no_separate_readme",
            walkthrough=None,
            repository_path=path, repository_commit=tree["sha"], repository_blob_sha=entry["sha"])
        if acquired:
            readme = downloads.get(str(Path(path).parent / "README.md"))
            row.update(artifact_status="downloaded_zip_with_opaque_workflow",
                artifact_path=acquired["local_path"], sha256=acquired["sha256"],
                acquisition_manifest="evidence/sample-flows/public-wxcc-manifest.json")
            if readme:
                row["source_urls"].append(readme["source_url"])
                row["readme_path"] = readme["local_path"]
                row["documentation_review"] = "documented_partial_contract"
                row["documentation_walkthrough"] = CH16
            row["capture_labels"] = [Path(m["name"]).name for m in acquired.get("zip_members", [])
                if m["name"].endswith(".workflow") and not m["name"].startswith("__MACOSX/")]

    def table_names(slug):
        lines = (ROOT / f"sources/cache/help/{slug}.md").read_text().splitlines()
        names = []
        started = False
        for line in lines:
            if line.startswith("| Flow Name"):
                started = True
                continue
            if started and line.startswith("|"):
                name = line.split("|")[1].strip()
                if name and not name.startswith(":") and not name.startswith("-"):
                    names.append(name)
            elif started and names:
                break
        return names

    old = "wxcc-flow-configuration-using-sample-templates"
    for name in table_names(old):
        relevant = name in {"Email Inbound", "SMS Inbound Message", "Task Routed", "Task Modified", "Close Task"}
        add("wxcc_legacy_help_listing", name, [f"https://help.webexconnect.io/docs/{old}"],
            relevant=relevant, reason="SMS/email or shared event companion" if relevant else "Additional channel entry retained from the complete legacy table",
            doc="documented_partial_contract" if relevant else "listed_and_scope_reviewed",
            walkthrough="knowledge/06-integrations-and-contact-center.md" if relevant else None,
            source_cache=f"sources/cache/help/{old}.md",
            identity_note="Legacy help generation; table contains eight entries despite prose saying seven; not equated to v3.5 files")

    cce = "cce-flow-configurations"
    for name in table_names(cce):
        relevant = name in {"SMS Inbound Flow", "Email Inbound Flow", "CREATED Flow", "QUEUED Flow", "ROUTED Flow", "CLOSED Flow", "TRANSFERRED Flow"}
        add("cce_documented_bundle", name, [f"https://help.webexconnect.io/docs/{cce}"],
            relevant=relevant, reason="SMS/email or CCE event companion" if relevant else "Additional channel/web-callback entry included from the whole CCE bundle",
            doc="documented_partial_contract",
            walkthrough=CH16, source_cache=f"sources/cache/help/{cce}.md",
            artifact_status="vendor_release_page_http_403_no_bundle_acquired",
            acquisition_evidence="evidence/sample-flows/cce-acquisition-status.json")

    for slug in ["wxcc-flows-with-qnabot-nodes", "configuring-flows-with-ai-agent-node"]:
        for name in ["FBM inbound bot callback/CRM example", "Livechat inbound bot/pre-chat variant"]:
            add("legacy_bot_documentation", name + " - " + slug,
                [f"https://help.webexconnect.io/docs/{slug}"],
                doc="documented_topology", walkthrough=CH16,
                source_cache=f"sources/cache/help/{slug}.md",
                identity_note="Two help pages describe the same legacy Q&A/Task Bot patterns; not four unique modern AI templates")

    captures = {}
    for path in sorted((BASE / "observed").glob("*.json")):
        try:
            item = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue  # A concurrent evidence writer may be finishing its file.
        if item.get("label"):
            captures.setdefault(item["label"], []).append((path, item))

    # Preserve unsuccessful static decoding as history and append the later,
    # supported UI inspection as a separate evidence layer.
    for manifest_name in ["public-native-manifest.json", "public-wxcc-manifest.json"]:
        manifest_path = BASE / manifest_name
        manifest = json.loads(manifest_path.read_text())
        for item in manifest:
            labels = [item["file"]] if "file" in item else [Path(m["name"]).name
                for m in item.get("zip_members", [])
                if m["name"].endswith(".workflow") and not m["name"].startswith("__MACOSX/")]
            matches = [(path, capture) for label in labels for path, capture in captures.get(label, [])]
            if matches:
                item["inspection_scope"] = "Original acquisition/static parse checks, before later supported UI inspection"
                item["supported_ui_inspection"] = {
                    "status": "imported_for_read_only_static_graph_inspection",
                    "observations": [{"path": str(path.relative_to(ROOT)),
                        "observed_at": capture.get("observed_at"),
                        "evidence_type": capture.get("evidence_type")}
                        for path, capture in matches],
                    "runtime_tested": False,
                    "note": "Temporary sample inspection is separate from executing or validating a live integration",
                }
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    summary_index_path = BASE / "summaries/index.json"
    try:
        summary_index = json.loads(summary_index_path.read_text()) if summary_index_path.exists() else {}
    except json.JSONDecodeError:
        summary_index = {}
    narrative_status = {item["source_path"]: item for item in summary_index.get("samples", [])}
    for row in records:
        if row["cohort"] not in {"tenant_gallery", "ai_fulfilment_repository", "wxcc_repository_v3_5"}:
            continue
        matches = []
        for label in row.get("capture_labels", [row["name"]]):
            matches.extend(captures.get(label, []))
        if matches:
            row["ui_graph_capture"] = "observed_static_canvas"
            row["observed_paths"] = [str(path.relative_to(ROOT)) for path, _ in matches]
            row["ui_evidence_types"] = sorted({item.get("evidence_type", "unspecified") for _, item in matches})
            present, stale = [], []
            for source_path, _ in matches:
                summary_path = BASE / "summaries" / source_path.name
                if not summary_path.exists():
                    continue
                try:
                    summary = json.loads(summary_path.read_text())
                except json.JSONDecodeError:
                    continue
                if summary.get("source_sha256") == hashlib.sha256(source_path.read_bytes()).hexdigest():
                    present.append(summary_path)
                else:
                    stale.append(summary_path)
            if stale:
                row["stale_summary_paths"] = [str(p.relative_to(ROOT)) for p in stale]
            if present:
                row["ui_graph_summary"] = "derived_summary_available"
                row["summary_paths"] = [str(p.relative_to(ROOT)) for p in present]
                for source_path, _ in matches:
                    narrative = narrative_status.get(str(source_path.relative_to(ROOT)), {})
                    current_sha = hashlib.sha256(source_path.read_bytes()).hexdigest()
                    if narrative.get("walkthrough_status") == "authored" and narrative.get("source_sha256") == current_sha:
                        row["ui_walkthrough_status"] = "authored_from_current_capture"
                        row["ui_walkthrough"] = "evidence/tenant-samples.md#" + narrative["sample_key"]

    assert len({r["id"] for r in records}) == len(records), "duplicate inventory IDs"
    counts = Counter(r["cohort"] for r in records)
    output = {
        "schema_version": 1, "refreshed_at": datetime.now(timezone.utc).isoformat(),
        "scope": "All nine observed tenant gallery templates; all 17 official AI fulfillment native files; all 33 current v3.5 digital-channel repository archives; all entries in the cached CCE/WXCC template tables; captured AI/email/SMS public tutorials. Priority tags do not exclude other channels within these collections. This is bounded corpus coverage, not every Cisco sample globally.",
        "count_unit": "Inventory entries by evidence cohort, not deduplicated unique flows; tutorials, legacy generations and equivalent source occurrences remain separate.",
        "counts": {"entries": len(records), "in_priority_scope": sum(r["in_priority_scope"] for r in records),
            "additional_channel_entries_included": sum(not r["in_priority_scope"] for r in records),
            "by_cohort": dict(counts), "downloaded_native_or_zip": sum(r["artifact_status"].startswith("downloaded_") for r in records),
            "observed_static_canvas": sum(r["ui_graph_capture"] == "observed_static_canvas" for r in records),
            "derived_graph_summaries": sum(r["ui_graph_summary"] == "derived_summary_available" for r in records),
            "authored_ui_walkthroughs": sum(r["ui_walkthrough_status"] == "authored_from_current_capture" for r in records),
            "runtime_tested": 0},
        "status_semantics": {
            "documented_topology": "Source states the major connected execution path; not an exact native edge extraction.",
            "documented_partial_contract": "Source explains useful dependencies or branches, but does not establish every native node/edge.",
            "observed_static_canvas": "Sanitized configured sample graph was captured; no flow execution was performed.",
            "derived_summary_available": "A separate summary JSON matches the current capture SHA256; this is not an independent QA or runtime claim.",
            "authored_from_current_capture": "The summary index records an authored walkthrough for the same current capture hash.",
        },
        "source_exclusions": [
            {"source": "sources/cache/help/templates*.md", "reason": "Message-content templates, not executable flow samples"},
            {"source": "sources/cache/help/sending-and-receiving-sms-using-sandbox.md", "reason": "Sandbox messaging/API exercise without its own connected sample flow"},
            {"source": "sources/cache/help/webex-ai-agent-in-sandbox.md", "reason": "Studio access guide, not a sample flow"},
            {"source": "Older version directories in webexcc-digital-channels", "reason": "Historical releases are version duplicates; current v3.5 collection is inventoried in full, with the older help listing retained for version-conflict context"},
            {"source": "sources/cache/help/branch-node-to-build-flow-with-conditional-branch.md", "reason": "Individual-node illustration, covered by node reference rather than a standalone AI/email/SMS sample"},
            {"source": "sources/cache/help/calling-a-flow-from-another-flow.md", "reason": "Call Workflow mechanism illustration, covered by node/lifecycle references"},
        ],
        "refresh_command": "python scripts/update_sample_inventory.py",
        "samples": records,
    }
    (BASE / "sample-inventory.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output["counts"], indent=2))


if __name__ == "__main__":
    main()
