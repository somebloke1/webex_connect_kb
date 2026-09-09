# Agent ingestion and build guidance

Start with [agent-index.json](../knowledge/agent-index.json), then populate [agent-flow-build-packet.yaml](../templates/agent-flow-build-packet.yaml). The packet is **logical pseudodesign**, encoded as JSON-compatible YAML. Its keys are this library's planning vocabulary; it is **not an importable Cisco format**. No template value authorizes a tenant action.

## Retrieve deterministically

1. Select manifest route IDs from the explicit task. Include `agent_design` for a new agent flow; add `email_adapter` and/or `sms_adapter`, then the relevant fulfillment, graph, handoff, or review routes. The manifest's `when` values describe intent facets, not mandatory keyword matching.
2. Sort selected routes by ascending priority. Read `authored` paths, then `exact_contracts`; deduplicate in first-occurrence order. Paths in the JSON/YAML artifacts are relative to the repository root.
3. Use the [Studio section index](../sources/studio-index.md) to open a specific field table instead of loading the whole manual. Read [connected sample walkthroughs](../knowledge/15-sample-flow-walkthroughs.md) and [every observed sample](../evidence/tenant-samples.md) for relationships between nodes. The [sample inventory](../evidence/sample-flows/sample-inventory.json) records complete collection coverage and any source-only gap; use `--scope samples` for exact field/node retrieval across sanitized graph summaries.
4. For an omitted contract, search its exact node/method/field locally: `python scripts/search_kb.py 'SessionMetadata' --scope sources --all --json --limit 5`. Read the returned source around the field, not only the snippet. Broad external research is a fallback for missing or changed evidence.

## Preserve evidence scope

Use official, version-scoped documentation for product semantics and target-tenant observations for visible configured fields. Neither proves execution. An executed case proves only its recorded scenario and boundaries. Release announcements do not establish a tenant's deployed version. Recommendations describe proposed designs; video transcripts need their date, transcription method, and timestamps.

When evidence conflicts, keep both claims and their scope. Record the unresolved binding and what evidence would resolve it. Do not silently normalize outcome spelling or borrow a Task Bot output for an AI Agent node. A downloaded native artifact is not a parsed graph; a documented sequence is not a complete set of native edge records.

## Produce a connected contract

Separate **channel → agent → reply/continuation/handoff** from **agent action → backend fulfillment → result returned to agent**. Scripted digital fulfillment belongs within the outer conversation path. Select applicable packet flow units; mark the others not applicable with a reason.

For each node, record its logical purpose separately from the native ID, exact palette type/version/method, field labels, literals/resource references, and picker expressions. Trace every consumed value through **producer → transformation/transition assignment → consumer**. State its type, requiredness, scope, lifetime, and behavior when absent. Do not replace an unknown namespace with a plausible one.

For each edge, record the exact source outcome, condition, destination or terminal disposition, and assignments. Account for all displayed outcomes. For each loop, specify the value updated, exit condition, and deadline. For each backend operation, separate API acceptance from business completion and define the returned result on failure as well as success. For each channel, separate sending, delivery, transcript append, session closure, and human ownership.

Use null for an unresolved value, with an entry under `unresolved`; null never means a safe default. Record credentials by existing reference, not secret value. Keep schema, sample payload, and native export as separate artifacts. Proposed custom names must be labeled as proposed.

## Separate readiness from authorization

Fill `authorization` from actual user instructions and retain their evidence. For this KB mission, local documentation/tooling edits are authorized; Webex Connect inspection is read-only except any specifically authorized disposable sample scope recorded by the coordinator. **Control Hub is strictly read-only with no experimentation exception.** Do not transfer Connect's narrow exception to Control Hub. The parent coordinates browser work.

A future build request may authorize a different scope; apply its explicit instructions rather than treating this template as a permanent approval barrier. Record create/edit, execute/send, publish, Control Hub mutation, and business writes independently. Design completion is not publication permission, and publication is not execution evidence.

Before implementation, resolve the required tenant/resource/node bindings and material source conflicts. Review graph completeness, variable availability, meaningful terminal results, and the task's material failure cases. Keep results `not_run` until executed. Deliver a reviewable packet with remaining gaps even when those gaps require tenant evidence; do not claim an unresolved design is deployable.
