# Independent QA: completed sample material unit

Reviewed 2026-09-09 UTC. One reasoned, critical, constructive, non-perfectionistic pass of chapters 15/16, sample inventory/manifests, all 59 observed graphs and summaries, both generated walkthrough reports, `summarize_sample_graphs.py`, and `search_kb.py --scope samples`. The acceptance criterion was complete collection coverage and usable, evidence-scoped graph/data/terminal explanations. No Webex, Studio, Control Hub, message, flow-execution or network action was performed. Earlier KB, AI authoring and transcription units were not reviewed again.

## Result

The native inspection unit is complete for **59 samples: 9 gallery + 17 AI fulfillment + 33 current WxCC v3.5 archives**. Every sample has an observed model, derived summary, coherent narrative and both report anchors. One material omission in a critical sample limitation was reported and the parent reports it integrated; the parent owns final verification of that change. No other material defect emerged from this bounded pass.

The inventory's 95 entries preserve overlapping source occurrences, tutorials and versions; they are not 95 unique native flows. **All 15 CCE bundle entries remain source-only.** Their acquisition record and chapter 16 retain the HTTP 403 and later browser login/service-contract gate. They were not counted as native graphs or execution evidence.

## Full-collection mechanical evidence

Fresh independent local checks are recorded in [sample-mechanical-checks.json](sample-mechanical-checks.json); the reproducer is [sample-mechanical-checks.py](sample-mechanical-checks.py). These compare raw observed records directly to summaries rather than invoking the summarizer again.

| Check | Result |
| --- | --- |
| Expected inventory cohort keys ↔ observed files ↔ summaries ↔ summary index | Exactly 59; identical sets, excluding `index.json` as a sample |
| Source hashes and runtime claims | All 59 source SHA-256 values match; observed and summary `runtime_tested` are false |
| Cell/node/edge/End records | Unique cell IDs; exact ID sets and counts agree for every graph |
| Explicit edge contract | Every source, target, internal event and visible label matches the observed model |
| End contract | Every parent, event, exitResult, named outcome and producer-present flag agrees; duplicate groups agree |
| Cycles | Independent mutual-reachability calculation matches each captured strongly connected group |
| Variable relationships | Counts agree; recorded writers exist; missing node-producer flags agree; literal references and captured variable-use metadata stay distinguished |
| Narrative/report coverage | All 59 narrative objects have walkthrough, handoffs and limitations, equal authoritative narrative inputs, and appear in both reports |
| Acquisition manifests | All 17 native AI and all 43 WxCC records (33 archives + 10 READMEs) exist and match recorded hashes/byte lengths |

Confirmed totals: **2,958 cells, 534 operative nodes, 1,670 explicit edges, 695 End records and 4,382 variable uses**. **15 graphs** have stale End parents; every such graph is flagged. Duplicate End bindings and unresolved producers are retained as observed inconsistencies, not normalized into invented execution paths. These are static consistency checks, not a proof of runtime reachability, variable availability on every branch, or business success.

## Semantic comparisons and practical coverage

I followed the critical narratives through the captured node parameters, assignments, edges and End settings, including Generic AI Live Chat, scripted Doctor, Track Package, native lookup appointment, native sendSMS, inbound email, inbound SMS and dropped-email-attachment notification. A bounded second set covered contact priority, task-variable extraction/screen pop, Set Variable with PIQ/EWT, Apple picker responses and native check-in. [sample-semantic-checks.json](sample-semantic-checks.json) records 26 direct parameter comparisons across these 13 graphs and the Doctor mismatch witness.

The explanations correctly distinguish current AI outputs from legacy bot outputs; an outer conversation loop from a short action fulfillment; HTTP completion from business result; SMS/email submission from delivery; and Close Task from AI-session closure. Specific useful limitations are preserved: native sendSMS's literal success return is not delivery evidence; email acknowledgment failure can still lead to Queue while the SMS variant differs; queued/task-variable failures and PIQ insufficient-data branches remain visible; the task-variable pair exchanges data via events rather than a fabricated cross-flow edge; the Apple list branch lacks the symmetric success End that its time branch has; and native check-in contains no duplicate-write safeguard or independent boarding-pass operation.

Chapters 15/16 distinguish published sequences, opaque downloaded files, later supported UI captures, version-specific paths and engineering adaptations. Sample-only nested metadata paths are not promoted to universal AI schemas. The review did not attempt to correct every vendor example or validate every possible source-code input.

## Material finding and practical fix

**S1 — Doctor failure handoff text uses mismatched variable names.** In [the observed Doctor model](../sample-flows/observed/gallery-ai-doctor.json), node `1731`'s failure expression assigns `agentTextResponse` (line 25190), while its on-leave action names and reads `agentTextResp` (lines 25229/25234). Internal outcome `1` explicitly leads to Send `768`; that node's message reads `$(agentTextResp)` (line 6136). The earlier AI node writes its TextResponse into the latter variable. Consequently, the intended system-error notice is not established by the captured assignment and could reuse prior AI text. This is a static inconsistency, not an observed failed execution.

The original Doctor narrative described the error-handover route without this caveat. Practical documentation fix: add the mismatch to its authoritative limitations and instruct an adapting builder to align Evaluate's output, transition assignment and Send input before treating the notice as reliable. Preserve the original evidence. The parent reports adding this to `observed-narratives.json` and regenerating all summaries/reports; no tenant or raw capture was changed. No second independent review of the fix was performed.

## Retrieval and forward use

Fresh `samples` scope returns exactly 59 documents, all from `evidence/sample-flows/summaries/`, all carrying `kind=sample`, static evidence type and `runtime_tested=false`. A temporary local fixture with a sanitized summary plus sentinel-bearing raw and observed JSON proved raw/observed paths are excluded. Source-parameter checks include the observed redacted-input boundary; no credential or raw import is required for sample retrieval. Scope does not index the summary index itself.

Queries for AI Agent Livechat, MessageMetadata, Email Inbound, lookup_appointment and sendSMS returned scoped summary evidence. A CLI forward query for AI Agent Fulfilment Track Package returned the exact gallery summary with provenance fields. [The sample adaptation forward test](forward-test-sample-adaptation.md) follows manifest routes, reuses its real Start → HTTP → terminal/notification contract, and leaves actual identity, endpoint, agent, channel and session bindings unresolved. It required no external research and makes no native-import or execution claim.

Tenant cleanup verification and the separately reviewed transcription/skill checks remain the parent's responsibility; they were intentionally not repeated in this unit.
