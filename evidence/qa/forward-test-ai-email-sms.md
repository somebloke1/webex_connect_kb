# Independent forward test: AI Agent with email and SMS

Prepared 2026-09-09 UTC from the local KB only. This is a **design packet**, not a tenant configuration, native flow export, or execution record. The machine-readable companion is [forward-test-ai-email-sms.yaml](forward-test-ai-email-sms.yaml).

## Request and selected pattern

Design a support AI Agent that answers stable support-policy questions from reviewed knowledge and performs one authenticated ticket-status lookup. Use SMS for short conversational turns and email for detailed threaded replies. Preserve identity, thread, session, ownership and duplicate boundaries. Route unverifiable requests, unsupported attachments and explicit human requests to the business's existing review/handoff process.

Selected manifest routes: `agent_design`, `autonomous_fulfillment`, `studio_knowledge_tools`, `email_adapter`, `sms_adapter`, `graph_and_variables`, `human_handoff`, `external_api`, `troubleshoot_or_review`. Followed their priority and exact-contract routing. Sample units 15/16 were deliberately outside this review assignment, so no claims rely on their evolving contents.

Use a **current autonomous AI Agent** plus a separate **AI Agent-triggered fulfillment flow**. Scripted fulfillment is not selected: that alternative parses documented `SessionMetadata` response/intent paths and runs the API operation in the outer flow. `taskbot.entities`, `bot.text_response`, legacy `TemplateKey`, and Contact Center voice `Virtual Agent V2` custom-event loops do not belong in this design.

## Agent configuration contract

Proposed agent name: `Support Ticket Guide`; engine candidate: general-purpose **Webex AI Pro 2.0**, subject to actual availability. Language: English from the configured agent's actual supported options. Agent type: Autonomous. No Studio create, edit, preview, test or publication is authorized by this packet.

Goal/instruction proposal: answer support-policy questions using the approved policy source; ask for a missing ticket reference; use `lookupTicket` for private ticket status; never claim a lookup, change or handoff succeeded without the relevant result; do not infer account authorization from a matching name, email address, telephone number or customer-supplied approval flag; request human help on denial, uncertainty or explicit request. Keep SMS concise and email readable. Preserve all meaningful response items. The agent cannot choose sender assets, recipients, endpoints, credentials or recipient-verification rules.

Knowledge bindings are **unresolved** because this KB contains product-building knowledge, not the user's customer-support policies. Supply reviewed policy files/articles with owner, effective date, product/region applicability, revision and answer fixtures. Keep live ticket records behind the lookup action. Studio upload, review, binding and publication are distinct later steps; local file existence establishes none of them.

Studio action proposal: one Fulfillment action named `lookupTicket` (within documented 64 characters), described as returning the status of a ticket accessible under an already verified request context. Its entity schema declares an object with string properties `ticketReference` and `requestContextRef`, both required. `ticketReference` is customer-supplied; `requestContextRef` must originate from the approved application identity process and be independently validated by the backend. Do not ask a customer to manufacture the latter.

The **mechanism for transporting trusted request context from the channel adapter into the action invocation is a blocking binding**. The public sources document optional Message Parameters and action input entities, but do not establish a universal authenticated action envelope, automatic mapping of those parameters into action input, or a safe customer-identity field to assume in Start. Inspect an approved representative configured action payload and establish its trust contract before implementation. A model copying an opaque reference is not validation. If this transport cannot be established, retain general policy Q&A and route private lookups to review, or select an explicitly designed outer-flow authorization/lookup pattern. Do not silently pretend it works.

Illustrative business sample, not a Cisco envelope:

```json
{"ticketReference":"T-204","requestContextRef":"opaque-verified-context-example"}
```

Studio's JSON entity editor documents type validation only. Backend validation must enforce required values, allowed reference format, current authorization, expiry and record ownership even if the schema includes `required`, `pattern` or `enum`.

## Three flow units and the return boundary

```text
SMS Start -> prepare/claim -> eligibility/owner gate -> AI Agent Process Message
  onSuccess -> validate/format all response items -> SMS -> bounded Receive
  Receive sms.mo -> replace current fields -> prepare/claim -> next agent turn
  onAgentHandover / failed turn -> existing human-review handler

Email Start -> prepare/claim/thread resolution -> eligibility/owner gate
  -> AI Agent Process Message -> validate/format -> Email -> persist/end
  A later email starts a new run; no hours-long Receive is assumed.

Autonomous action invocation --separate platform invocation--> AI Agent Start
  -> authorized lookup HTTP -> classify -> parse/map result -> terminal outcome
  --Flow Outcomes / Last Execution Status / Notify AI Agent--> invoking agent
```

There is no drawn canvas edge from Process Message to the fulfillment Start and no invented Return Response node. In a future authorized build, configure the fulfillment Start category **AI Agent**, event **Trigger from AI Agent to initiate flow**, parse the real sample JSON, and retain its documented Webex CI-secured endpoint. Under **Flow Settings → Flow Outcomes → Last Execution Status**, keep **Notify AI Agent** enabled and map every terminal result. Select that client-workspace service/flow in the Studio action's **Webex Connect Flow Builder Fulfillment**. All these are configuration instructions, not performed actions.

Fulfillment has a documented **30-second execution maximum** and prohibits the listed waiting nodes: Delay, Social Hour, Receive and Call Workflow. Choose one HTTP lookup, connection timeout 2,000 ms, request timeout 5,000 ms, with no in-flow retry in this initial design. The parent AI node's documented approximately 15-second timeout is a separate contract; 5-second HTTP plus 30-second fulfillment is **not** a promised response-time calculation. Verify the whole action/inference boundary later. On timeout, return `unavailable` if the flow can terminate and notify; an absent notification remains unknown, never `found`.

## Concrete fields, producers and edges

Logical IDs in the companion packet are authored labels. All `native_node_id` values remain null. Exact picker prefixes must be captured when a tenant node exists.

| Node / fields | Producer → assignment → consumer | Outcome contract |
|---|---|---|
| SMS Start: SMS MO event, Incoming Number, keyword policy, no-live-session guard | Documented `sms.senderNumber`, `sms.serviceNumber`, `sms.transId`, `sms.timestamp`, `sms.keyword`, `sms.message` → snapshot current variables → gate | Actual Start success event remains a picker binding; no guard is treated as durable deduplication. |
| Email Start: selected email app/incoming event | `email.emailId`, `email.appId`, `email.transId`, `email.messageId`, `email.inReplyTo`, `email.headers`, `email.toAddresses`, `email.subject`, content and attachment fields → normalization + case resolution | Exact trigger event label is unresolved; never guess a receive-event spelling as Start's edge. |
| Preparation: HTTP Request + Branch | Actual owned case/identity service returns owner, dedup disposition, verified context reference, current text, thread/case reference and remaining budget → gate | HTTP `onSuccess` still checks status/schema; named gate branches `Automate`, `HumanOwned`, `Duplicate`, `Review`; `None of the above`/`onError` → controlled review/failure. |
| AI Agent / Process Message, separately for SMS and email | Agent type Autonomous; reviewed Agent; Message = current normalized text; Channel = corresponding channel; channel-specific identifier = original sender; Language = supported choice; Message Parameters = intended turn context | Documented `onSuccess` → format; `onAgentHandover` → handoff; `onError`, `onInvalidCustomerID`, `onInvalidMessage`, `onTimeOut` → safe fallback. Observed b1.4 set differs; do not merge it blindly. |
| Formatter: owned HTTP service or proven supported transformation | AI `FullResponse` + recorded verified tool result + deterministic channel policy → approved content | FullResponse is documented as an array; element structure, node prefix and success-only availability require an actual representative sample. No `[0].text` or `aiagent.FullResponse` shape is invented. Unknown/malformed shape → review. |
| SMS Send | Destination Type `msisdn`; Destination = captured verified target; From Number = approved business asset; Message Type Text/Unicode as actual content requires; Message = formatted answer; Correlation ID = send intent | Choose Gateway Submit continuation in the configured node. Exact send events are unresolved; acceptance/submission, delivery and customer reply remain separate. |
| SMS Receive | SMS; Number = same business number; From Number = customer number; any-keyword policy; Max Timeout = min(120 seconds, remaining lifetime) | `sms.mo` copies **new** message/keyword/event fields before gate; `onTimeout` → inactivity disposition; `onError` → controlled technical end. |
| Email Send | Destination type Email Id; Destination ID = verified reply target; From Email = asset-controlled; From Name = approved support identity; ReplyTo Email = chosen reentry mailbox; Subject = controlled case subject; Email type Text or approved HTML/template with Fallback Text; CC/BCC by policy | SMTP `In-Reply-To` = the current inbound **Message-ID**, where available. No universal Headers field. Configured send outcomes/receipts are unresolved until route inspection. |
| Fulfillment HTTP Request | Parsed proposed action fields → actual endpoint/auth reference → response body/status from actual picker | `onSuccess` → status/business classification; `onError`/`onTimeout` → unavailable result. No blind retry or waiting node. |
| Fulfillment Branch / Data Parser | Validate backend `result`, ticket ID, status and authorized current context → initialize/set all custom result variables | `found` → parsed safe fields; `not_found`/`denied`/`invalid`/`unavailable` → explicit empty-ticket body; parser failure → unavailable. Terminal events notify with latest values. |

For AI nodes, the official outcome set above is documented evidence. A separate observed unconfigured b1.4 set includes `onInvalidData`, `onInvalidChoice`, `onTimeout`, `onFailure` instead. The actual configured version's complete field/outcome set is a blocker; `outcome_coverage_complete` remains false. Distinguish `TextResponse` (first text only and not suitable for every rich response) from `FullResponse` (all response items).

## Identity, thread, duplicate and session policies

- Preserve channel customer, business asset, mail thread/case, inbound event, Connect transaction, AI ConsumerId/SessionId/TransactionId and business-operation references separately. No AI session is presumed to be an email thread. Cross-channel association requires verified customer records.
- Gate duplicates using the actual stable source-message key plus business asset, with atomic state owned by a real service. Verify whether `sms.transId`/`email.transId` stays stable across redelivery. Flow variables and the SMS live-session guard are insufficient for cross-run deduplication. Human-owned events append to the existing human conversation rather than invoking the AI again.
- SMS default: at most five processed customer turns and ten minutes total; duplicates spend no turn, and each valid new turn replaces input. The deadline is checked before the next Receive and before any next side effect. Timeout ends the wait without declaring the ticket resolved. A late new request reloads case state and identity eligibility.
- Email default: one processed message per Connect run. Preserve inbound Message-ID and In-Reply-To separately, use actual case/thread rules, and exclude quoted history/auto-responses through an approved parser. A forward or changed CC list does not automatically change the reply recipient or authorization.
- The documented Process Message contract does not accept a Session ID input or prove concurrent thread isolation. Serialize related agent/customer work while establishing the real session contract. Merely serializing turns does not clear old case memory. Sensitive unrelated email threads stay in review until owned-session closure/new-session behavior or another supported isolation policy is verified. Do not invent an identifier containing thread/transaction IDs to force isolation.
- Close Session accepts Agent plus the **Session ID returned by Process Message**. Its owner must establish no pending SMS turn, action, other email case or human workflow relies on that session. Closing a Connect run or a Contact Center task is not closing the AI session. The design has no unconditional per-email close action.

## Business result and response safety

Suggested custom notification body:

```json
{"result":"found","ticketReference":"T-204","status":"waiting_for_customer","nextStep":"Provide the device serial number.","actionPerformed":false}
```

The keys are application-defined. Use `not_found`, `denied`, `invalid` or `unavailable` with empty ticket/status details on those branches. Initialize a safe unavailable result before the HTTP call so failures cannot reuse an earlier branch's `found` value. Validate that the returned ticket/customer binding equals the authorized request, not merely that the HTTP status is 200. Keep this compact body well below the documented 16,000-character limit. No private credentials or raw exception text reach the agent.

The one selected operation reads status only. It cannot create a ticket, refund, change an address or register an email recipient. It may record a request disposition in the authorized owning service; that is a separately scoped future write. Repeated lookup invocations do not become claims that updates occurred.

SMS output contains a short supported status and one next question. Email may include fuller instructions, plain text and approved escaped HTML. Preserve all intended answer items; unsupported rich content goes through an explicit fallback. Email attachment extraction requires an actual parser/scan contract. A URL does not establish that an AI node has read an attachment. Attachment-only or blocked material routes to review or requests usable text.

SMTP delivery tracking is **unresolved in the source snapshot**: the asset page says no tracking/failure notifications, while the Email node page says tracking is available for SES or SMTP. The safe design records submission evidence actually obtained and leaves delivery unknown unless the configured route produces verified receipts. It neither promises a receipt nor discards one that does arrive. Plain-text email read receipts are not documented as available.

Human requests use the existing case/contact-center handoff integration and carry nonsecret current case, verification and transcript context. The parent of that integration must bind its exact nodes/queue/lifecycle. Request accepted, task queued and human joined are separate states. On timeout, discover whether an existing request/task exists before creating another. A support-review fallback says what actually happened; it never announces an agent connection without participation evidence.

## Expected cases — all not_run

| Fixture | Expected path/result |
|---|---|
| SMS policy question with no ticket context | One current AI turn; knowledge-supported answer; no lookup call. |
| Missing ticket reference | Clarification outside fulfillment; no guessed reference. |
| Verified T-204 lookup | Single backend lookup; found result returned via Notify AI Agent; safe SMS/email content agrees with it. |
| Expired/unbound authorization context, someone else's ticket | Denied/review; no private result even if the model supplies plausible fields. |
| HTTP 200 with denied payload, null status, malformed JSON | Business failure/schema fallback; never found. |
| Fulfillment timeout or missing notification | Unavailable/unknown turn; no invented completion. |
| Two response items, unsupported rich item | All meaningful text retained in order or explicit review; no first-item truncation. |
| Keyword-only HELP; second SMS corrects reference | Latest keyword/message handled; no stale first-turn text; separate current operation. |
| Sixth SMS turn, expired lifetime, late reply | Bounded exit/reentry according to session policy. |
| Duplicate inbound source event, simultaneous first messages | One owner/progression; no duplicate answer or handoff. |
| Two unrelated emails from the same sender | Distinct case authorization; no reuse of unknown AI memory; review until isolation is established. |
| HTML/quoted email, attachment-only email, changed CC | Correct extraction/reply policy; no invented attachment understanding or arbitrary recipient. |
| SMTP submission with no receipt | Submission recorded; delivery_unknown; no unconditional failure resend. |
| Explicit human request; duplicate handoff; handoff timeout | Existing lifecycle reused; automated replies stop; no false connected claim. |

## Evidence and readiness

Primary local contracts: [AI Agent node](../../sources/cache/help/ai-agent-node.md), [fulfillment procedure](../../sources/cache/help/configure-fulfilment-flows-for-ai-agent-actions.md), [Studio actions/slots](../../sources/cache/studio/article--ncs9r37.md#concept-template_5ea99e1f-a679-4cf9-8e33-7a4f83d9f66a), [JSON entity validation](../../sources/cache/studio/article--ncs9r37.md#concept-template_7d93102d-6315-44a3-a257-9c211827de36), [scripted digital fulfillment](../../sources/cache/studio/article--mzpuseb.md#digital-channels), [Receive fields](../../sources/cache/help/receive-node.md), [Email node](../../sources/cache/help/email-node.md), [Email asset](../../sources/cache/help/email.md), [SMS node](../../sources/cache/help/sms-node.md), [HTTP node](../../sources/cache/help/http-request-node.md).

The local library sufficed to build this reviewable design and locate exact field tables without external research. It does not remove the need for real business-policy/identity APIs, trusted context transport, response-element samples, tenant/node bindings, and session-isolation evidence. Those are unresolved implementation inputs, not gaps to fill with invented platform behavior.

Status: **design reviewable; implementation blocked on listed bindings; no configuration, execution, messages, publication or business API action performed**. The scope remains documentation only.
