# Independent forward test: inbound SMS order status

Design-only build packet, prepared 2026-09-08 by the integration QA agent from the installed skill and local KB. Request: “Design an inbound SMS order-status flow with verified identity, an HTTP dependency, bounded invalid replies, duplicate-event handling and human escalation. Return a build packet, not a tenant configuration.” No tenant controls, external messages, or external APIs were exercised. All execution tests below are `not_run`.

## Proposed business contract

An inbound `STATUS` message starts one conversation on a designated SMS number. Collect one order identifier, establish that the sender matches the order's registered customer, verify possession through a short-lived OTP, then retrieve and disclose only that customer's minimal order status. `AGENT` during a waiting turn, exhausted invalid replies, or a recoverable business-system failure routes to human assistance. `STOP` follows the existing consent/opt-out policy and ends automation; it does not create an agent task automatically.

This is a proposed identity policy, requiring business-owner acceptance: the authoritative customer record must associate this order with the inbound number, then OTP verifies current possession of that registered number. An arbitrary order ID and a code sent to an arbitrary self-supplied number do not establish identity. Higher assurance, account recovery, changed registered numbers and disputed ownership route to the approved human process without disclosing order data.

Chosen engineering limits, not platform defaults: ten-minute total self-service lifetime; up to three invalid inputs per collection stage (initial attempt plus two clarifications); OTP valid for five minutes, with no resend in this initial design; one active self-service interaction per tenant/business-number/customer-number tuple. Order-input waits are at most 120 seconds, OTP waits at most 120 seconds and remaining OTP lifetime, further-help wait at most 60 seconds, always clipped to the remaining total lifetime. The business-state service supplies remaining time where necessary, avoiding an assumed Evaluate date API.

## Dependencies that must be bound before a build

| Required binding | Status and rule |
|---|---|
| Tenant/service/test SMS number, role, sender format | Unknown. Use the intended existing client-level service if WxCC requires it; do not create or rebind one for this packet. Inspect competing rules/Start nodes before implementation. |
| Business-state/identity/order API | Proposed contract below, not a built-in Connect API or an asserted existing endpoint. Obtain actual URLs, credentials, schemas, limits and idempotency semantics from its owner. |
| Customer identity policy and transactional-message eligibility | Unknown business policy; cannot be inferred from a phone number or this documentation. |
| Stable inbound delivery identifier | `sms.transId` is documented as a transaction ID, but redelivery stability must be verified. Use the provider's stable original-message ID where exposed; do not claim exactly-once behavior from a new execution ID. |
| Agent platform/queue/business hours | Select existing approved handoff implementation. The detailed candidate below is WxCC plus Engage; verify installed versions/entitlement. Do not mix CCE or standalone Engage field contracts. |
| Existing SMS opt-out/help handler | Confirm it and its trigger precedence. This design adds no competing tenant rule. |
| Exact node IDs and outcomes | Logical labels below are not IDs to paste into a flow. Select actual references from the picker. Exact SMS-send event labels and version-specific integration outcomes remain binding tasks. |

## Data dictionary

All custom names are alphanumeric and use `$(Name)` references. No custom variable uses a reserved name such as `message`, `msisdn`, or `transid`.

| Custom variable | Origin/type | Lifetime and handling |
|---|---|---|
| BusinessNumber | Start's `sms.serviceNumber`, string | Snapshot on entry; no numeric conversion. Used for receive and task destination. |
| CustomerNumber | Start's `sms.senderNumber`, string | Snapshot on entry; country code preserved. Verify required destination format. Sensitive. |
| EventId | Current Start/Receive `sms.transId` or verified stable provider ID, string | Replace on every inbound turn; ledger owns duplicate disposition. |
| LatestText / LatestKeyword | Current producer's `sms.message` / `sms.keyword`, strings | Replace before every branch. A keyword-only message can have empty message text; test both values for commands. No blanket variable logging. |
| InteractionId / Stage / Deadline | Durable state API response | Opaque interaction ID and finite state; one owner. Stage version prevents concurrent progression. |
| OrderId / CustomerKey | Validated reply / association API | Strings, initialized empty. CustomerKey is never trusted from user input. Bound together. |
| ChallengeId / VerificationState | State service / successful Validate OTP | Initialized `UNVERIFIED`; change to verified only on the documented success edge. Bound to order/customer/purpose. |
| InvalidOrderCount / InvalidOtpCount / InvalidHelpCount | State record | Separate integer counters; duplicate delivery never increments them. |
| RequestAttempt | Set on entering each logical dependency operation | Initialize 0, increment immediately before each actual attempt; maximum 3 includes initial request. |
| HttpStatus / HttpBody / BusinessStatus | Configured HTTP output picker, parsed response | Documented outputs use `https.statusCode` and `https.responseBody`, but cached examples conflict. Copy actual namespace/case. |
| ConversationId / TaskId / Owner | Existing handoff/state contract | Separate IDs; Owner moves from BOT to HANDOFF_PENDING to AGENT only on appropriate evidence. |

## Topology and concrete node configuration

Main path: **Start → claim event/session → prompt/Receive order → validate order → verify customer/order association → Generate OTP → SMS/Receive code → Validate OTP → order-status HTTP → parse and authorize result → SMS status → Receive further help → end or handoff**.

Duplicate and stale events pass through the state gate before processing. Every material error, invalid-input, timeout and terminal outcome has a destination. Separate classification/increment/wait nodes make loops nonadjacent, respecting the documented prohibition on connecting directly back to the preceding node.

| Logical step / palette node | Fields and binding | Outcomes / next action |
|---|---|---|
| S / Start | `SMS - Mobile Originated - MO`; Incoming Number = approved business number; Keyword = `STATUS`; enable “Trigger only when there are no live sessions” after collision review | Configured SMS success event → E. Snapshot sender, business number, message, keyword and event identity. Guard is not durable deduplication. |
| E / HTTP Request then Branch | Atomic claim-or-read at actual state endpoint; body carries business/customer tuple, EventId, stage version; timeout contract below | HTTP `onSuccess` → inspect status/body; NEW → stage action, DUPLICATE/STALE → no repeated work, EXISTING_AGENT → existing append handler, unavailable → controlled technical end. |
| P / SMS | Destination Type = `msisdn`; Destination = `$(CustomerNumber)`; From Number = approved asset; Message Type = Text; prompt asks for order ID or `AGENT`/`STOP`; Wait For = Gateway Submit | Configured submission-success event → R; submission/error/expiry routes to message-failure disposition. Submission is not delivery. No blind send retry after ambiguous outcome. |
| R / Receive | Channel SMS; Number = business number; From Number = customer number; Keyword = UI's any-keyword selection; Max Timeout = chosen stage time clipped to remaining lifetime | `sms.mo` → snapshot NEW current reply → E for current-stage claim; `onTimeout` → NO_RESPONSE; `onError` → technical failure. |
| O / Branch | Ordered command tests first, then order format `^[A-Za-z0-9-]{6,32}$` as this example business format | Named AGENT → H; STOP → existing preference policy/end; valid → A; `None of the above` → increment InvalidOrderCount and prompt if <3, else H; `onError` → technical end. Actual format must match business IDs. |
| A / HTTP Request + Data Parser + Branch | Read association, supplying order and sender; response must assert matching registered customer and current eligibility. Select JSON paths for match/result/customer ID only | Valid matching association → G. Missing/multiple/unauthorized result → generic verification-unavailable response and offer H; never disclose which account exists. Malformed/failed response → H or technical end. |
| G / Generate OTP | OTP Format Numeric; OTP Length 6 explicitly; OTP Validity 5 minutes; Transaction Reference = ChallengeId; Extra Parameters bind CustomerKey, OrderId and purpose `orderstatus` | `onSuccess` → OTP send, using output `generateOTP.OTP` from actual node; `onError` → verification unavailable. No code logging. |
| C / SMS, then Receive | Same verified registered number/sender; text code only with purpose and expiry; submission-success → OTP Receive. Receive binds the same SMS asset/customer with remaining timeout | `sms.mo` → E → command/shape branch → V; timeout → expired/no-response; error → technical end. Never send to a number entered in the conversation. |
| V / Validate OTP | OTP = newly captured candidate; Transaction Reference and Extra Parameters exactly match G; no resend command enabled | `onSuccess` → mark verification for this interaction/order → L; `onFail` → increment InvalidOtpCount, <3 reprompt, otherwise H; `onError` → verification unavailable. Expired challenge never returns to Generate automatically. |
| L / HTTP Request | GET actual order-status resource with OrderId and verified CustomerKey through supported auth; ask for minimal status and allowed fields | `onSuccess` → classify HTTP/business result → Data Parser; `onTimeout`/`onError` → dependency retry policy. Authorization failure has no retry. |
| B / Data Parser + Branch | Source = actual HTTP response-body output; JSON sample; parse orderId, customerKey, status, asOf; reject missing/wrong types | Require returned customer/order equal verified bindings; allow only approved status enum. Success → M. Any mismatch/invalid schema → no disclosure; H with safe reason. |
| M / SMS | Same addressing fields; text such as “Your order is dispatched. Reply AGENT for help or DONE to finish.” Render only approved factual status, no address/payment details | Submission-success → F; failure → delivery/technical disposition. Record STATUS_SUBMITTED distinctly from confirmed delivery and from final completion. |
| F / Receive then Branch | Same SMS correlation; Max Timeout ≤60 seconds and deadline | `sms.mo` → E → AGENT H, DONE terminal COMPLETED; other input ≤2 clarifications, third terminal; timeout ends without inventing a delivery confirmation; error technical end. |

All unspecified optional Notify URL, callback authorization and template settings use the reviewed service's explicit contract, not guessed values. Obtain the SMS node's rendered outcome inventory because its cached page documents wait behavior without a complete stable event table. Each displayed event must be connected or deliberately terminated at build time.

## HTTP, duplicate and failure contract

The state API must perform atomic claim and compare/update, with durable replay retention sufficient for the actual upstream redelivery window. A lookup followed by an unrelated write is not an atomic claim. It supplies InteractionId, current stage/version, owner, deadline, counters and any existing handoff IDs. Logical operations below require owner-supplied schemas/endpoints; their names are not Webex API field claims.

1. `claimInbound`: deduplicate original message identity within tenant/business asset; return the prior disposition for repeats. Claim the customer tuple before sending a new prompt. If an already-consumed duplicate resumes a Receive, route through a short state check back to the same stage's Receive, with unchanged attempts and reduced remaining time.
2. `advanceStage`: compare expected stage/version and record completion; duplicates cannot consume another attempt or repeat OTP generation. A later legitimate repeated text has its own message ID and is processed normally. No text-only deduplication.
3. `claimSend`/`claimHandoff`: keep the operation's state/ID durably. Do not interpret claiming as successful sending. An unknown send/task result goes to reconciliation; it is not released for blind duplicate execution.
4. Late events after terminal state cannot reuse verification. A fresh STATUS journey starts unverified. Repeated old events return prior disposition. New events while AGENT owns the interaction append to the existing conversation, suppressing bot replies.

HTTP Request settings: Connection Timeout = 2,000 ms, Request Timeout = 5,000 ms, both below the documented 20,000 ms maxima; actual dependency contract may require adjustment. Query values are automatically encoded; do not pre-encode them. HTTP `onSuccess` still requires response/status/schema/business checks.

Retry only approved read or genuinely idempotent operations on transport failure, 429, or explicitly transient 502/503/504. At most three total calls, delays 1 then 2 seconds, within a 20-second dependency-operation budget and overall interaction deadline. Before every attempt increment RequestAttempt; after each failure test both remaining count and whether the next timeout can fit within the deadline. Honor a larger Retry-After only if budget permits. Authentication, authorization, invalid input, not-found, business rejection and schema errors do not retry identically. Any write timeout is UNKNOWN; query status by operation key before repeating. Ledger unavailable means stop safely; ordinary flow custom variables cannot replace it.

## Human escalation candidate: existing WxCC/Engage explicit lifecycle

Use one existing compatible explicit search/create/append architecture. Do not add Resolve Conversation side effects on top of it. If the tenant already uses the simplified resolver, adapt to that supported template instead of duplicating task creation.

- H reads Owner and existing ConversationId/TaskId under the handoff claim. Search by SMS business/customer addresses; append to existing active conversation or create according to the installed template. Carry reason, verification result/time, masked customer/order references and nonsecret transcript. A code is never transferred.
- Create Task candidate SMS fields: TASK ID = stable valid task ID from the approved template/state contract; CONVERSATION ID = returned Engage ID; DESTINATION = BusinessNumber; MEDIA TYPE = Social; MEDIA CHANNEL = SMS; CUSTOMER NAME and CUSTOMER ID = CustomerNumber per SMS source; Mobile Number (ORIGIN) = CustomerNumber. `created` → queue; `onTimeout` → reconcile; `onInvalidData`, `onError`, `onInvalidChoice`, `onauthorizationfail`, `Error`, `Task failed` → corresponding failed/needs-review state. Check exact installed spelling/version.
- Queue Task: TASK ID, CONVERSATION ID, MEDIA TYPE Social, MEDIA CHANNEL SMS, static QUEUE NAME = approved order-support queue; priority = 5 as a proposed selectable 1–9 value; no invented priority 10 or dynamic-queue entitlement. `Queued` means queued, not agent connected. `onTimeout` → reconcile; `onInvalidData`, `onError`, `onInvalidChoice`, `onauthorizatonfail`, `Error`, `taskFailed` → controlled failure. Source spelling differs from Create Task, so use actual UI.
- Existing Task Routed handler adds the routed agent as participant and acknowledges routing after the result. Existing modified/close handlers retain both IDs and close only the actual intended lifecycle. AGENT ownership begins when that handler confirms participation. HANDOFF_PENDING already suppresses conflicting bot service logic.
- Outside working hours or if routing fails, say assistance is unavailable and provide the business-approved contact route. Do not claim “connected” or “callback booked” without corresponding evidence. A queued task with ambiguous status is reconciled; never create a replacement just because a timeout occurred.

## Design acceptance fixtures

Every row is `not_run`; these are expected tests for a future explicitly authorized test environment.

| Case | Expected evidence/result |
|---|---|
| Happy path, order `000123`, matching registered sender, valid OTP | Correct order/customer pair; one OTP send; one status send; leading zeroes intact; selected HTTP and SMS events recorded. |
| Someone else's order; unknown or multiple match | No order data/code sent to an arbitrary supplied address; generic failure; approved human route. |
| Wrong OTP three times; expired OTP; changed order after challenge | Exactly two clarifications, then stop verification; no lookup/disclosure; changed binding cannot inherit verified state. |
| Three malformed order IDs, second reply valid after first invalid | Bounded loop; second reply actually replaces LatestText; counts separated from OTP/dependency retries. |
| Missing/null status or returned customer/order mismatch | No empty/guessed status disclosure; controlled failure. |
| GET 503 twice then success; 401; Retry-After exceeds budget | Exactly 3 calls in first case; 1 call for permanent auth failure; no overdue retry; Delay `onTimeout` used as normal continuation. |
| Same incoming event delivered twice, including after original ends | One claim/progression/send; repeat does not spend OTP attempt or revive verification. |
| Two first messages race; two different business numbers share sender | One active owner per correct tuple; no false collision across assets. |
| Duplicate reply consumed by Receive; late reply after deadline | Same-stage bounded rewait for duplicate; old verification not reused; remaining lifetime decreases. |
| Keyword-only AGENT/STOP/DONE | Recognized even if sms.message is empty and command is in sms.keyword. |
| Handoff create timeout after task committed | Existing task discovered/reused; no duplicate task; no false “connected” SMS. |
| Queued then routed, agent close, duplicate close | Correct task/conversation IDs and transcript; automation suppressed; both systems converge to intended terminal state. |
| SMS submission succeeds but delivery is unknown | Status remains submitted/unknown delivery; no claim of actual receipt or blind fallback send. |

Release state: designed only; configured = no; saved = no; tested against tenant = no; published = no; end-to-end verified = no. This packet authorizes no external action.

## Local evidence used and sufficiency judgment

Read the installed [skill](../../skills/webex-connect-flows/SKILL.md), [knowledge map](../../knowledge/00-map.md), [design](../../knowledge/01-platform-and-design.md), [lifecycle](../../knowledge/02-flow-lifecycle.md), [variables](../../knowledge/03-variables-and-expressions.md), [nodes](../../knowledge/04-node-reference.md), [channels](../../knowledge/05-channels.md), [integrations](../../knowledge/06-integrations-and-contact-center.md), [recipes](../../knowledge/08-recipes.md), [mastery path](../../knowledge/11-mastery-path.md), and [build-brief template](../../templates/flow-build-brief.md). Local search led to the exact cached [Start](../../sources/cache/help/start-node.md), [Receive](../../sources/cache/help/receive-node.md), [SMS](../../sources/cache/help/sms-node.md), [Create Task](../../sources/cache/help/wxcc-create-task.md), and [Queue Task](../../sources/cache/help/wxcc-queue-task.md) pages; source metadata records the 6.20.0 reference snapshot separately from release announcements.

The library suffices to design this packet without broad research. It correctly exposes tenant/business bindings and actual picker/runtime checks as remaining implementation facts. It does not remove the need to obtain the user's business API or identity policy. One material inconsistency in the node chapter's retry counter was reported separately; this packet uses the explicit three-total-attempt contract.
