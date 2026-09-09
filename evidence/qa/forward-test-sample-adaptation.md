# Sample-based forward test: add a fulfillment reference to the AI/email/SMS packet

Prepared 2026-09-09 UTC using local KB files only. This supplements [the existing design packet](forward-test-ai-email-sms.md); it does not configure, import, invoke or publish a flow. All proposed cases remain `not_run`.

## Request and retrieval

Request: “Use a reviewed sample to make the ticket-status fulfillment segment concrete. Explain exactly what to reuse and what the SMS/email adapters must still own.”

Selected manifest routes: `autonomous_fulfillment` (20), `email_adapter` (30), `sms_adapter` (31), and `graph_and_variables` (40). The existing packet already supplies `agent_design`. Follow the routes' authored guidance and exact contracts; use the sample index for graph evidence.

Executed locally:

```bash
python scripts/search_kb.py 'AI Agent Fulfilment Track Package' --scope samples --all --json --limit 1
```

First result: [gallery-track-package.json](../sample-flows/summaries/gallery-track-package.json), `kind=sample`, `evidence_type=read_only_inspection_of_loaded_sample_canvas_model`, `runtime_tested=false`, `walkthrough_status=authored`. Its [observed source](../sample-flows/observed/gallery-track-package.json) is the source of the IDs and edges below. The exact public return contract is cached at [Configure Fulfillment Flows](../../sources/cache/help/configure-fulfilment-flows-for-ai-agent-actions.md).

## What the reviewed sample establishes

| Observed segment | Evidence and meaning | Adaptation for the existing ticket-status design |
| --- | --- | --- |
| Start `2` → HTTP `3` | AI Agent Start exposes `packageNum`; internal `onbegin`, displayed `onBegin`, enters HTTP. | Keep the separate AI Agent invocation boundary. Parse the actual action payload; proposed ticket fields replace this sample slot only after the binding is established. |
| HTTP `3` request | GET uses the sample tracking path and `$(n2.aiAgent.packageNum)`. | The actual owned ticket lookup endpoint, authorization reference and verified-context transport remain unresolved. The sample contains no identity-verification proof. |
| HTTP output | Whole-body JSONPath `$` maps to `fullResp`, referenced as `$(n3.fullResp)`. | Do not forward the whole backend body. Classify HTTP and business results, then populate the existing compact `result`, `ticketReference`, `status` and `nextStep` return proposal. |
| HTTP terminal bindings | `oncomplete` / displayed `onSuccess` → Success; `onerror` → Error; `ontimeout` → Incomplete. These are End parent/event associations, not missing explicit edges. | Preserve every outcome in the logical graph. A transport-success result must pass authorization and schema/business checks before becoming `found`. |
| Flow outcome return | Last Execution Status has notification enabled for all statuses; custom payload includes `transactionID=$(transid)` and `response=$(n3.fullResp)`. | Configure an explicit initialized result for every exit. On error/timeout, `n3.fullResp` may be absent, so the sample's success-shaped return must not be copied unchanged. |

The sample has no Send, Receive or retry loop. Its fulfillment result returns to the invoking agent; it does not directly contact the customer. The public contract uses **AI Agent** Start and **Flow Settings → Flow Outcomes → Last Execution Status → Notify AI Agent**, with the selected client-workspace flow bound in Studio's **Webex Connect Flow Builder Fulfillment**. No Return Response node or direct canvas edge from the outer Process Message node is implied. [Cisco fulfillment contract](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions)

## Narrow logical amendment

```text
actual AI Agent action event
  -> validate required ticket reference and trusted request context
  -> initialize unavailable return
  -> HTTP lookup (one attempt)
       success -> classify authorization/status/schema
                    found -> map allowed fields -> terminal + notify
                    denied/not_found/invalid -> safe result -> terminal + notify
       error/timeout -> unavailable -> terminal + notify
```

The identifiers above are proposed logical labels; target native IDs and picker expressions remain null. Keep the original packet's 2,000 ms connection and 5,000 ms request budget proposal. The documented 30-second fulfillment limit and restrictions on Delay, Social Hour, Receive and Call Workflow apply; they do not prove the total agent response time. A missing return notification is unknown completion, never `found`.

SMS still owns its sender asset, current message replacement, duplicate claim, bounded Receive and later customer turn. Email still owns reply target, case/thread correlation and reentry on a later message. Both adapters own human handoff and presentation of the returned answer; neither receives an identity guarantee from the Track Package sample. The existing blockers for trusted context transport, configured AI version, FullResponse shape, thread/session isolation and actual channel bindings remain.

## Acceptance cases for a later authorized build

- Authorized matching ticket and valid response: return only allowed status fields; outer adapter formats the answer once.
- HTTP success with a denied/mismatched ticket or malformed body: return a safe denial/unavailable result, never the whole response.
- HTTP error/timeout before `fullResp` exists: initialized unavailable return has no stale ticket data.
- Duplicate action/customer event: apply the existing packet's ownership/deduplication contract; this sample supplies no durable deduplication mechanism.
- Customer reply after fulfillment: resume the channel/agent conversation; do not hold the fulfillment invocation open waiting for it.

Result: local sources suffice to reuse the sample's invocation, HTTP-output and terminal-return structure. The unresolved items are concrete business/tenant bindings already represented in the design packet, not a need for broad strategy research.
