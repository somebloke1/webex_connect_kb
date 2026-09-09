# Independent AI Agent integration QA

Completed as one bounded pass of the new AI-focused authored unit. The review is constructive and proportionate: it checks material correctness and whether another agent can produce a useful build packet without broad research. It does not assess speculative completeness or repeat earlier units' QA.

## Result and forward test

The local library supports a concrete, reviewable AI Agent design with separate SMS/email adapters and an autonomous ticket-lookup fulfillment flow. The new material correctly distinguishes current AI Agent nodes, legacy Task/QnA Bot contracts, scripted digital fulfillment and Contact Center voice activities. It does not pretend that generic product documentation supplies tenant resources or the user's business API.

- [Readable independent forward-test packet](forward-test-ai-email-sms.md)
- [JSON-compatible YAML build packet](forward-test-ai-email-sms.yaml): 18 logical nodes, 58 proposed/documented edge records, 8 explicit unresolved implementation bindings and 13 expected cases, all `not_run`.
- [Route/interface check evidence](ai-route-checks.json)

The packet is designed from the local KB, using the supplied structured template. No intended solution was requested from authors. No native node IDs, undocumented response-element paths, working API endpoints or executed results were invented. Exact configured outcome coverage remains false rather than falsely claiming a deployable graph.

## Material findings and practical fixes

| Finding at the reviewed snapshot | Supporting evidence | Practical correction / disposition |
|---|---|---|
| Chapter 14's email normalization step asserted that SMTP lacks delivery tracking/failure notifications without retaining a conflicting current source claim | `sources/cache/help/email.md:299` says SMTP lacks support; `sources/cache/help/email-node.md:157` says delivery status tracking is available for SES or SMTP. Both are captured 6.20.0 references. The blanket claim could misdirect receipt/failure wiring for this priority channel. | Preserve both claims and mark actual route/tenant receipt support unresolved. Record submission and leave delivery unknown until evidence exists; do not promise receipts or discard valid ones. Parent reports this correction and related acceptance-case wording applied. |
| Chapter 14's formatter instructed readers to use the “actual response-array schema described in chapter 13,” but neither that chapter nor its source supplies a complete element schema | `sources/cache/help/ai-agent-node.md:65` describes FullResponse as an array with multiple/rich items. It gives no universal item discriminator/text/rich-element paths or qualified picker prefix. A builder could invent a shape while believing it came from the KB. | State that only the array-level contract is documented; bind a representative selected-agent/node-version response sample before parsing elements, preserve multiple items and route unknown shapes to review. Parent reports the correction applied. |

Both were reported during this same pass. The parent owns final readback of the fixes; no additional independent QA pass is requested. No other material defect was found in the reviewed scope.

## Evidence checked

Read chapters 13/14, updated mastery chapter 11 and skill, `docs/agent-ingestion.md`, the route manifest, and the structured packet template. Checked task-relevant exact cached contracts including:

- Current **AI Agent / Process Message / Close Session** fields, outputs and documented outcomes; parameter persistence/turn scope; first-text versus full response; documented timeout and tenant rate limit.
- **Autonomous fulfillment**: AI Agent Start direction, actual event wording, Webex CI endpoint, client-workspace selection, 30-second limit, listed restricted waiting nodes, `Last Execution Status` and `Notify AI Agent`, 16,000-character return limit and final-value behavior.
- **Studio action/slot/JSON tables**: action name/description limits, slot fields and lengths, required/type handling, client-workspace fulfillment selection, action limits and MCP configuration scope. The source explicitly states type-only schema validation; the guidance does not promote schema hints into backend authorization.
- **Scripted digital fulfillment**: outer-flow responsibility, holding response, generatedDf sample, `$.model_state.template_key`, `$.previous_intent_model_state.intent.name`, API/result/send/append/Receive sequence. These are not applied to autonomous response metadata.
- **Engine reference**: current autonomous 2.0 choices versus announced 1.0 deprecation, region/language limits, scripted Swiftmatch utterance/description requirements.
- **SMS/email fields**: original sender/business identifiers, SMS keyword-only handling, incoming email message/reply IDs, spelling differences, SMTP threading and attachment limits, and deterministic send mapping.

The review retained distinct evidence classes: official contract, proposed design, observed but unconfigured tenant node, and future execution. The documented AI outcome spelling does not overwrite the separately observed b1.4 inventory. The read-only mission is carried through the skill and the design packet.

## Executed interface checks

The manifest and JSON-compatible YAML template parsed successfully. All 12 route IDs are unique; every route's required packet section exists in the template; all authored/exact-contract paths resolve. Relevant authored Markdown links and exact Studio section anchors resolve. The generated forward-test packet parsed, all logical edge endpoints refer to defined nodes, and every expected case remains `not_run`.

Local exact-field search retrieved the AI Agent contract for FullResponse alongside the separately identified legacy contracts. The route manifest provides deterministic disambiguation, avoiding reliance on the broad search rank alone.

No transcription tests, source-crawler implementation review, earlier general-content QA, or sample-unit 15/16 review was repeated. Sample-related route paths were checked for existence only; their content and expanding observed graphs remain outside this unit.

## What remains an implementation binding

The forward test exposes concrete inputs a KB cannot safely invent: the reviewed business-policy corpus; actual identity/lookup/handoff service contracts; trusted identity-context transport into an autonomous action; configured AI node/version/output/edge bindings; FullResponse element samples; concurrent email-session isolation/closure; and route-specific email receipts. The packet explains the effect and evidence needed for each. Their presence is honest scope handling, not a reason to perform broad research or unauthorized tenant tests.

This pass used local files only. No browser, Webex Connect or Studio configuration, Control Hub action, external API, outbound message, publication or flow execution was performed. No economical agent was used. The result validates a documentation/design workflow, not a production journey.
