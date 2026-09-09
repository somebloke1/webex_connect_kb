#!/usr/bin/env python3
"""Describe sanitized observed canvas models; this is not a flow import/export API."""
from __future__ import annotations
import argparse
from collections import defaultdict, Counter, deque
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REF = re.compile(r"\$\(([^()]+)\)|\$\{([^{}]+)\}")
NODE_REF = re.compile(r"^n(\d+)\.(.+)$")
SENSITIVE = re.compile(r"token|secret|password|authorization|api.?key", re.I)
JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]+")
SKIP_PARAMS = {"methodRequestParameters", "versionsList", "resourceinfo", "viewData", "_arrayResultMap", "_arrayResult", "data", "outputvariablesarray", "chOutputVars", "prevEvents", "newEvents", "headers", "authorization"}


def clean(value):
    if isinstance(value, dict):
        sensitive_name = SENSITIVE.search(str(value.get("name", "")))
        return {k: "[redacted]" if (SENSITIVE.search(k) and k.lower() not in {"isvalidatesignature", "isauthrequired"}) or (sensitive_name and k in {"value", "defaultValue", "defaultvalue"}) else clean(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean(v) for v in value]
    if isinstance(value, str):
        return JWT.sub("[redacted]", value)
    return value


def leaves(value, prefix=""):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from leaves(item, prefix + ("." if prefix else "") + str(key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from leaves(item, prefix + "[" + str(index) + "]")
    elif isinstance(value, str):
        yield prefix, value


def reference_rows(value, consumer, location):
    result = []
    for path, text in leaves(value, location):
        for match in REF.finditer(text):
            variable = match[1] or match[2]
            node = NODE_REF.match(variable)
            result.append({"consumer": consumer, "location": path, "reference": match[0], "variable": variable, "producer_node": node[1] if node else None, "producer_field": node[2] if node else None, "evidence": "literal_variable_reference"})
    return result


def strongly_connected(nodes, edges):
    graph = defaultdict(set)
    for edge in edges:
        if edge["source"] in nodes and edge["target"] in nodes:
            graph[edge["source"]].add(edge["target"])
    index = 0; stack = []; onstack = set(); indices = {}; low = {}; groups = []
    def visit(node):
        nonlocal index
        indices[node] = low[node] = index; index += 1; stack.append(node); onstack.add(node)
        for target in graph[node]:
            if target not in indices:
                visit(target); low[node] = min(low[node], low[target])
            elif target in onstack:
                low[node] = min(low[node], indices[target])
        if low[node] == indices[node]:
            component = []
            while True:
                target = stack.pop(); onstack.remove(target); component.append(target)
                if target == node: break
            if len(component) > 1 or node in graph[node]: groups.append(sorted(component, key=lambda x: (len(x), x)))
    for node in nodes:
        if node not in indices: visit(node)
    return groups


def summarize(path, root):
    raw = path.read_bytes(); document = clean(json.loads(raw)); cells = document.get("cells", [])
    by_id = {str(cell["id"]): cell for cell in cells}
    workflow = next((cell.get("value", {}).get("attributes", {}) for cell in cells if cell.get("value", {}).get("tag") == "workflowdata"), {})
    nodes = {}; terminals = []; edges = []; refs = []; assignments = []
    outcomes = {str(item.get("id")): item for item in document.get("outcomes", [])}
    for cell in cells:
        identifier = str(cell["id"]); value = cell.get("value", {}) or {}; attrs = value.get("attributes", {}) or {}
        if cell.get("edge"):
            edges.append({"id": identifier, "source": str(cell.get("source")), "target": str(cell.get("target")), "event_internal": value.get("name", value.get("value")), "event_label": value.get("label"), "representation": "explicit_edge"})
        elif cell.get("vertex") and (value.get("nodeType") == "end" or value.get("data", {}).get("type") == "end"):
            params = {p.get("name"): p.get("value") for p in value.get("params", [])}
            source = str(value.get("data", {}).get("parentNode"))
            outcome = outcomes.get(str(params.get("exitResult")), {})
            terminals.append({"id": identifier, "source": source, "target": identifier, "event_internal": params.get("nodeEvent", value.get("name")), "event_label": value.get("label"), "outcome_id": params.get("exitResult"), "outcome_name": outcome.get("tagName", outcome.get("value")), "outcome_description": outcome.get("value"), "session_retry": params.get("sessionRetry"), "async_check": params.get("asyncCheck"), "representation": "terminal_parent_node_and_nodeEvent"})
        elif cell.get("vertex") and value.get("tag"):
            params = {child.get("attributes", {}).get("name"): child.get("text") for child in value.get("children", []) if child.get("tag") == "param"}
            relevant = {k: v for k, v in params.items() if k not in SKIP_PARAMS and v not in (None, "", [], {})}
            # Receive's data is configuration; other nodes' data is often mock response content.
            if value["tag"] == "receive" and params.get("data"):
                relevant["data"] = params["data"]
            actions = [{"kind": child.get("tag"), "name": child.get("attributes", {}).get("name"), "when": child.get("attributes", {}).get("type"), "value": child.get("text")} for child in value.get("children", []) if child.get("tag") in {"session", "flow", "custom", "log", "all", "set"}]
            events = [{"event_internal": child.get("attributes", {}).get("name"), "declared_target_count": child.get("attributes", {}).get("targetcount")} for child in value.get("children", []) if child.get("tag") == "event"]
            nodes[identifier] = {"id": identifier, "label": attrs.get("label", attrs.get("name", value["tag"])), "type_internal": value["tag"], "parent_cell": str(cell.get("parent")), "events_declared": events, "configuration": relevant, "transition_actions": actions, "declared_outputs": workflow.get("dynamic_output_vars", {}).get(identifier, []), "output_mappings": params.get("outputvariablelist") or params.get("methodResponseParameters") or [{"source_path": child.get("attributes", {}).get("name"), "output_name": child.get("attributes", {}).get("type"), "is_mandatory": child.get("attributes", {}).get("ismandatory")} for child in value.get("children", []) if child.get("tag") == "data"]}
            refs += reference_rows(relevant, identifier, "configuration")
            refs += reference_rows(actions, identifier, "transition_actions")
            for action in actions:
                if action["kind"] in {"session", "flow", "custom", "set"}:
                    assignments.append({"writer_node": identifier, **action})
    custom_defaults = document.get("customVariables", [])
    refs += reference_rows(custom_defaults, "flow-custom-defaults", "customVariables")
    for outcome in document.get("outcomes", []):
        refs += reference_rows(outcome.get("notification"), "flow-settings", "outcome[" + str(outcome.get("id")) + "].notification")
    # Captured variable-use metadata supplements literal references without claiming dynamic JS analysis.
    for consumer, usage in workflow.get("copy_used_vars", {}).items():
        for kind in ("_usedVars", "_usedTransVar"):
            for ref in usage.get(kind, []):
                variable = ref.get("fullPath"); node = NODE_REF.match(variable or "")
                if variable:
                    refs.append({"consumer": str(consumer), "location": kind, "reference": "$(" + variable + ")", "variable": variable, "producer_node": node[1] if node else None, "producer_field": node[2] if node else None, "evidence": "captured_variable_use_metadata"})
    unique = {}; custom_writers = defaultdict(list)
    for assignment in assignments:
        custom_writers[str(assignment["name"])].append(assignment["writer_node"])
    for ref in refs:
        ref["observed_custom_writers"] = sorted(set(custom_writers.get(ref["variable"], []))) if not ref["producer_node"] else []
        unique[(ref["consumer"], ref["location"], ref["reference"], ref["evidence"])] = ref
    refs = list(unique.values())
    # Some shipped samples retain stale or duplicated End records. Preserve them
    # as observations, while never inventing a producer from a nearby label.
    terminal_keys = Counter((t["source"], str(t["event_internal"]), str(t["outcome_id"])) for t in terminals)
    for terminal in terminals:
        terminal["producer_captured"] = terminal["source"] in nodes
        terminal["same_binding_record_count"] = terminal_keys[(terminal["source"], str(terminal["event_internal"]), str(terminal["outcome_id"]))]
    semantic_edges = edges + [terminal for terminal in terminals if not any(e["source"] == terminal["source"] and e["target"] == terminal["target"] for e in edges)]
    starts = [n["id"] for n in nodes.values() if n["type_internal"] == "start"]
    reachable = set(starts); queue = deque(starts); graph = defaultdict(list)
    for edge in semantic_edges: graph[edge["source"]].append(edge["target"])
    while queue:
        for target in graph[queue.popleft()]:
            if target not in reachable: reachable.add(target); queue.append(target)
    declared_without_capture = []
    for node in nodes.values():
        represented = {e["event_internal"] for e in semantic_edges if e["source"] == node["id"]}
        for event in node["events_declared"]:
            if event["event_internal"] not in represented:
                declared_without_capture.append({"node": node["id"], **event})
    page_refs = []
    for node in nodes.values():
        if "page" in node["type_internal"].lower() or "workflow" in node["type_internal"].lower():
            page_refs.append({"node": node["id"], "label": node["label"], "configuration": node["configuration"]})
    return {"schema_version": 1, "sample_key": path.stem, "title": document.get("label", path.stem), "observed_at": document.get("observed_at"), "source_path": str(path.relative_to(root)), "source_sha256": hashlib.sha256(raw).hexdigest(), "evidence_type": document.get("evidence_type"), "runtime_tested": document.get("runtime_tested", False), "status": "observed_canvas_relationships_summarized", "format_warning": "Internal loaded-canvas model observations only; not a public import schema. Event internal names and visible labels are recorded separately. Dynamic script behavior and missing canvas pages are not inferred.", "counts": {"cells": len(cells), "operative_nodes": len(nodes), "explicit_edges": len(edges), "terminal_bindings": len(terminals), "variable_references": len(refs)}, "start_configuration": workflow.get("start_node_info"), "nodes": list(nodes.values()), "edges": edges, "terminal_bindings": terminals, "terminal_sources_not_captured": sorted({t["source"] for t in terminals if not t["producer_captured"]}), "duplicate_terminal_binding_groups": [{"source": key[0], "event_internal": key[1], "outcome_id": key[2], "record_count": count} for key, count in terminal_keys.items() if count > 1], "variable_handoffs": refs, "custom_variable_assignments": assignments, "custom_variables": custom_defaults, "flow_outcomes": list(outcomes.values()), "cycles": strongly_connected(nodes, edges), "cross_page_or_flow_nodes": page_refs, "capture_pages": document.get("pages"), "declared_events_without_captured_route": declared_without_capture, "nodes_not_reached_from_captured_start": sorted(set(nodes) - reachable), "edge_endpoints_not_captured": [e for e in edges if e["source"] not in by_id or e["target"] not in by_id], "node_variable_producers_not_captured": sorted(set(r["producer_node"] for r in refs if r["producer_node"] and r["producer_node"] not in nodes)), "redactions": document.get("redactions")}


def mdtext(value, limit=350):
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    text = text.replace("|", "\\|").replace("\n", " ")
    return text if len(text) <= limit else text[:limit] + "… [full value in graph summary]"


def detailed_report(summaries, notes):
    lines = ["# Observed tenant sample graphs", "", "These walkthroughs describe sanitized, read-only captures of loaded sample canvases. They establish node configuration and connections, not successful execution. Existing tenant flows were not modified by this authoring workflow. Temporary sample inspection and cleanup are recorded by the capturing agent separately.", "", "An End item may have no explicit incoming edge: `data.parentNode` plus its `nodeEvent` parameter associates the terminal with its producer and outcome. A binding whose producer is present is an observed terminal relationship, not an omitted route. Stale End parents and duplicate bindings are preserved and flagged; they do not establish an unseen producer or additional execution. The table prints the visible event label and retains differing internal names in parentheses; internal names are not public import-schema instructions.", "", "## Coverage", "", f"Captured and summarized sample files: **{len(summaries)}**. This count covers the files currently present in `sample-flows/observed/`; the parent's sample inventory determines whether all gallery/native samples have been captured. No absent sample is counted as reviewed.", "", "| Sample | Operative nodes | Explicit edges | Terminal bindings | Graph summary |", "| --- | ---: | ---: | ---: | --- |"]
    for summary in summaries:
        c = summary["counts"]
        lines.append(f"| [{mdtext(summary['title'])}](#{summary['sample_key']}) | {c['operative_nodes']} | {c['explicit_edges']} | {c['terminal_bindings']} | [JSON](sample-flows/summaries/{summary['sample_key']}.json) |")
    lines += ["", "## How an agent should use these samples", "", "Trace each business outcome from Start through a concrete transition to a terminal or the next waiting state. Read the consumer's configured variable and identify its producer; preserve the sample's exact case and node namespace. Session/custom assignments can have several observed writers, so inspect control order rather than choosing the first writer. Script-local bindings, runtime response shape and cross-page variable visibility require their own evidence.", "", "Reuse the relationship pattern and adapt bindings to the target tenant. Redacted URLs/headers, selected assets, identities, node versions, integration methods and sample response bodies are not operational defaults. Error and timeout routes are part of each walkthrough. A declared event without a captured route is reported as a capture/configuration fact; it is not automatically a product defect. No runtime action is authorized by these descriptions."]
    for summary in summaries:
        key = summary["sample_key"]; nodes = {n["id"]: n for n in summary["nodes"]}
        label = lambda i: (str(i) + ": " + nodes[i]["label"]) if i in nodes else str(i)
        lines += ["", f'<a id="{key}"></a>', "", "## " + summary["title"], "", f"Observed {summary['observed_at']}. [Captured model](../{summary['source_path']}); [complete graph summary](sample-flows/summaries/{key}.json). Runtime tested: **no**.", ""]
        note = notes.get(key, {})
        if note.get("walkthrough"):
            lines += [note["walkthrough"], ""]
        else:
            starts = [label(n["id"]) for n in summary["nodes"] if n["type_internal"] == "start"]
            lines += ["The captured journey starts at " + "; ".join(starts or ["no captured Start"]) + ". The following progression groups every observed event by its destination, including explicit End bindings. The node IDs distinguish repeated labels.", ""]
        if note.get("handoffs"):
            lines += ["Useful handoffs: " + note["handoffs"], ""]
        lines += ["### Control progression", "", "| From | Observed event → next node or outcome |", "| --- | --- |"]
        for node in summary["nodes"]:
            destinations = defaultdict(list)
            for edge in summary["edges"]:
                if edge["source"] != node["id"]: continue
                event = edge["event_label"] or edge["event_internal"] or "unlabeled"
                if edge["event_internal"] and edge["event_internal"] != event: event += " (`" + str(edge["event_internal"]) + "`)"
                destinations[label(edge["target"])].append(event)
            for end in summary["terminal_bindings"]:
                if end["source"] != node["id"]: continue
                event = end["event_label"] or end["event_internal"] or "unlabeled"
                if end["event_internal"] != event: event += " (`" + str(end["event_internal"]) + "`)"
                destination = "End " + end["id"] + " → " + str(end["outcome_name"] or end["outcome_id"])
                destinations[destination].append(event)
            rendered = "; ".join(", ".join(dict.fromkeys(events)) + " → " + target for target, events in destinations.items()) or "No outgoing route captured"
            lines.append("| " + mdtext(label(node["id"])) + " | " + mdtext(rendered, 2500) + " |")
        if summary["cycles"]:
            lines += ["", "**Loops in the captured graph:** " + "; ".join(" → ".join(label(i) for i in group) for group in summary["cycles"]) + ". These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route."]
        else:
            lines += ["", "No control loop was found among the captured operative nodes."]
        lines += ["", "### Exact producer–consumer handoffs", "", "| Producer / observed writer | Reference | Consumers |", "| --- | --- | --- |"]
        grouped = defaultdict(set); producer_info = {}
        for ref in summary["variable_handoffs"]:
            if ref["evidence"] != "literal_variable_reference": continue
            variable = ref["reference"]
            producer = label(ref["producer_node"]) if ref["producer_node"] else ("custom variable; writers " + ", ".join(label(i) for i in ref["observed_custom_writers"]) if ref["observed_custom_writers"] else "External/system/custom value; producer not established here")
            producer_info[variable] = producer
            location = ref["location"]
            if location.startswith("configuration."): location = location[len("configuration."):]
            grouped[variable].add(label(ref["consumer"]) + " / " + location)
        for variable, consumers in grouped.items():
            lines.append("| " + mdtext(producer_info[variable]) + " | `" + mdtext(variable) + "` | " + mdtext("; ".join(sorted(consumers)), 800) + " |")
        lines += ["", "### Boundaries and adaptation", ""]
        if note.get("limitations"): lines += [note["limitations"], ""]
        if summary["cross_page_or_flow_nodes"]:
            lines.append("Cross-page/flow connector nodes are captured: " + ", ".join(label(n["node"]) for n in summary["cross_page_or_flow_nodes"]) + ". Their target parameters are retained in JSON; an uncaptured target graph is not inferred.")
        else:
            lines.append("No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.")
        if summary["declared_events_without_captured_route"]:
            lines.append("Declared events without a corresponding captured edge or terminal binding: " + "; ".join(label(e["node"]) + " / `" + str(e["event_internal"]) + "` (declared target count " + str(e["declared_target_count"]) + ")" for e in summary["declared_events_without_captured_route"]) + ".")
        if summary["nodes_not_reached_from_captured_start"]:
            lines.append("Nodes not reached through captured edges from Start: " + ", ".join(label(i) for i in summary["nodes_not_reached_from_captured_start"]) + ". Inspect page/connector capture before interpreting this as a flow defect.")
        if summary["terminal_sources_not_captured"]:
            lines.append("End records reference absent producer nodes: " + ", ".join(summary["terminal_sources_not_captured"]) + ". These stale/unresolved parent references do not establish operative nodes or valid routes.")
        if summary["duplicate_terminal_binding_groups"]:
            lines.append("Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.")
        if summary["node_variable_producers_not_captured"]:
            lines.append("Literal node-qualified references name uncaptured producers: " + ", ".join("n" + i for i in summary["node_variable_producers_not_captured"]) + ". Their provenance is not guessed.")
        lines += ["The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success."]
    return "\n".join(lines) + "\n"


def report(summaries, notes, complete=False, expected=59):
    authored = sum(bool(notes.get(s["sample_key"])) for s in summaries)
    lines = ["# Observed tenant sample walkthroughs", "", "These are coherent readings of sanitized sample canvases, not runtime test results. Each narrative follows the observed trigger, working nodes, waiting/branching behavior, variable handoffs and terminal handling. [Full node-by-node relationships](tenant-sample-relationships.md) and linked JSON summaries retain the detailed evidence.", "", "## Coverage and evidence boundary", "", f"Captured samples: **{len(summaries)}**; authored walkthroughs: **{authored}**; scoped expected samples: **{expected}**. All-sample capture/authoring complete: **{str(complete).lower()}**. The parent inventory defines the bounded gallery/native/WxCC set; absent graphs are never counted as reviewed.", "", "An End pseudo-node can encode its route through `data.parentNode` and `params.nodeEvent` without an explicit edge. The summaries preserve that binding and the selected flow outcome. End records whose parent node is absent and duplicate bindings are flagged explicitly, not repaired by inference. Event names from the internal model and rendered event labels are separate fields; neither the raw model nor these summaries constitute a supported public import schema. A configured callback payload, sample response or historical `isTestExecuted` flag does not establish a new successful run.", "", "| Sample | Nodes / edges / End bindings | Walkthrough |", "| --- | --- | --- |"]
    for summary in summaries:
        c=summary["counts"];status="authored" if notes.get(summary["sample_key"]) else "pending narrative"
        lines.append(f"| [{mdtext(summary['title'])}](#{summary['sample_key']}) | {c['operative_nodes']} / {c['explicit_edges']} / {c['terminal_bindings']} | {status} |")
    lines += ["", "## Reuse discipline", "", "Begin at Start and follow the actual event→node relationships. Distinguish existing-conversation append paths from new conversations and bot-turn loops. Map each consumer to its exact node output or custom-variable writer; check custom defaults and on-enter/on-leave assignments. Preserve sample-specific case, node version and extraction paths only as observed evidence. Adapt identities, assets, authorization and system contracts for the target tenant. Redacted hosts/credentials and embedded mock responses are not usable production bindings.", "", "Read each stated limitation before reusing a pattern. Cross-page links and cycles are derived only from captured relationships; missing pages or script-generated values stay unresolved. Configuration visibility does not authorize execution, messages, external writes or publication."]
    for summary in summaries:
        key=summary["sample_key"];note=notes.get(key,{})
        lines += ["", f'<a id="{key}"></a>', "", "## "+summary["title"], "", f"Observed {summary['observed_at']}. [Sanitized model](../{summary['source_path']}) · [graph JSON](sample-flows/summaries/{key}.json) · [all relationships](tenant-sample-relationships.md#{key}).", "", note.get("walkthrough", "Graph relationships have been extracted; a coherent authored walkthrough is still pending.")]
        if note.get("handoffs"):lines += ["", "**Exact handoffs:** "+note["handoffs"]]
        if note.get("limitations"):lines += ["", "**Adaptation limits:** "+note["limitations"]]
        loop_count=len(summary["cycles"]);cross=len(summary["cross_page_or_flow_nodes"])
        lines += ["", f"Captured graph: {loop_count} cyclic node group(s), {cross} explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested."]
    return "\n".join(lines)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--capture-complete", action="store_true", help="Parent confirms the scoped capture window is complete")
    parser.add_argument("--expected-count", type=int, default=59)
    args = parser.parse_args(); root = args.root.resolve()
    input_dir = root / "evidence/sample-flows/observed"; output_dir = root / "evidence/sample-flows/summaries"; output_dir.mkdir(parents=True, exist_ok=True)
    notes = {}
    for name in ["observed-narratives.json", "native-narratives.json", "wxcc-selected-narratives.json", "wxcc-narratives.json", "wxcc-social-narratives.json"]:
        path=root / "evidence/sample-flows" / name
        if path.exists():notes.update(json.loads(path.read_text()))
    summaries = []
    for path in sorted(input_dir.glob("*.json")):
        if not isinstance(json.loads(path.read_bytes()).get("cells"), list): continue
        summary = summarize(path, root); summary["authored_walkthrough"] = notes.get(path.stem)
        summary["walkthrough_status"] = "authored" if notes.get(path.stem) else "pending"
        summaries.append(summary)
        (output_dir / path.name).write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    complete = args.capture_complete and len(summaries) == args.expected_count and all(s["authored_walkthrough"] for s in summaries)
    (root / "evidence/tenant-sample-relationships.md").write_text(detailed_report(summaries, notes))
    (root / "evidence/tenant-samples.md").write_text(report(summaries, notes, complete, args.expected_count))
    inventory = {"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "status": "complete" if complete else "captures_currently_present_summarized", "all_samples_complete": complete, "expected_count": args.expected_count, "sample_count": len(summaries), "authored_walkthrough_count": sum(s["walkthrough_status"] == "authored" for s in summaries), "samples": [{k: s[k] for k in ["sample_key", "title", "observed_at", "source_path", "source_sha256", "status", "counts", "runtime_tested", "walkthrough_status"]} for s in summaries]}
    (output_dir / "index.json").write_text(json.dumps(inventory, indent=2) + "\n")
    print(json.dumps({"samples": len(summaries), "authored": inventory["authored_walkthrough_count"], "complete": complete, "operative_nodes": sum(s["counts"]["operative_nodes"] for s in summaries), "path": "evidence/tenant-samples.md"}))


if __name__ == "__main__": main()
