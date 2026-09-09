# AI Agent recipes with SMS and email

Reviewed 2026-09-08. These are **proposed implementation blueprints**, not live flows or importable Webex JSON. They combine the documented [AI Agent contracts](13-ai-agent-flows.md), [channel nodes](05-channels.md), [core nodes](04-node-reference.md) and [contact-center lifecycle](06-integrations-and-contact-center.md). No customer messages, tenant writes or backend actions were executed to produce them.

The central architecture is a shared business operation with two channel adapters. The agent interprets a request and explains an established result; the fulfillment flow validates and performs an allowed operation; SMS/email format and deliver its customer-facing representation. Neither an agent's generated sentence nor a green send edge is evidence that the business operation completed.

## Common build contract

The names below are **application-defined variables**. They do not describe a Cisco event envelope or promise a storage service built into Connect. Use an existing case/CRM store or an explicitly implemented persistence service when state must survive a flow run.

| Application variable | Purpose and proposed rule |
|---|---|
| `channel` | `sms` or `email`; trusted adapter assigns it |
| `businessAsset` | Business number or mailbox/app association from the trigger/configuration |
| `channelCustomer` | Original customer channel identifier, preserved as text |
| `customerRecordId` | Verified CRM/account link, if established; never inferred from similar names |
| `conversationKey` | Business-defined context key including channel and business asset; email also needs thread/case context |
| `inboundEventId` | Stable incoming identifier selected from the actual event contract for duplicate processing checks |
| `messageText` | Current customer request after normalization; not the whole accumulated transcript |
| `replyContext` | Original channel-specific reply data, kept outside a free-form model-generated object |
| `businessContext` | Minimal relevant, authorized case facts and verified results |
| `owner` | Proposed `automation`, `human`, or `closed` state in the application/conversation system |
| `operationId` | One business action intent; distinct from a delivery attempt and reused on reconciliation |
| `sendIntentId` | One intended outbound message to one channel/address; separate receipt history |
| `aiSessionId` | Observed agent session handle used only through supported node operations |

**Identity rule.** Link an SMS number and email address through an established profile/account verification process. Until then they are different identities. Unified business context does not mean the platform automatically shares an AI session across channels, nor that two email threads from one sender have isolated AI memory. Use the [session boundary guidance](13-ai-agent-flows.md) before choosing reset, reuse or concurrency behavior.

**Routing rule.** Apply opt-out, invalid-address, duplicate-event and current-human-owner checks before invoking the agent. Keep tenant/provider settings and static asset bindings out of model control. Customer text and attachment content are data; they cannot choose a backend authorization, invent a tool permission, or redirect a response to an arbitrary address.

### Exact source fields to bind once

Select node variables using the installed node's picker and add its actual `n<ID>` prefix. The following **documented field names** are a lookup aid; the left-side grouping is this blueprint's adapter design.

| Adapter input | Candidate documented variables |
|---|---|
| SMS identity/content | `sms.senderNumber`, `sms.serviceNumber`, `sms.keyword`, `sms.message` |
| SMS event reference | `sms.transId`, `sms.timestamp` |
| Email sender/content | `email.emailId`, `email.subject`, `email.message`, `email.htmlMessage`, `email.strippedText` |
| Email reply context | `email.messageId`, `email.inReplyTo`, `email.headers`, `email.toAddresses` |
| Email attachments/asset | `email.attachments`, `email.appId`, `email.assetType`, `email.transId` |

Source: [Receive event catalog](../sources/cache/help/receive-node.md). Its CC/BCC spellings differ from contact-center examples; do not silently replace `ccRecipents`/`bccRecipents` with other spellings. Use the producing node's actual picker. Detailed keyword and correlation behavior remains in [core nodes](04-node-reference.md#receive-correlate-a-response-to-a-waiting-execution).

### Shared agent invocation and formatter

Bind the agent using the [Process Message field table](13-ai-agent-flows.md). Choose the actual incoming channel and identifier. Pass the current request as the message; pass verified case context as turn-scoped input. Use profile-scoped parameters only for facts deliberately meant to persist beyond this exchange.

**Proposed formatter contract:** `formatResponse(validatedBusinessResult, normalizedAgentMessages, channelPolicy)`. Implement this with supported nodes or an owned formatting service; it is not a built-in function. The formatter should:

1. Chapter 13 establishes that `FullResponse` is an array, but does not supply its complete element schema. Bind the formatter to the actual configured agent response shape from a documented or authorized captured sample, with an explicit policy for multiple text items and unsupported rich elements. Never stringify a raw response array into an SMS or email.
2. Keep identifiers, dates, amounts, next steps and action status consistent with the verified tool result. If the tool failed or is unresolved, the text must say so.
3. For SMS, produce a concise answer and at most one necessary follow-up question. Apply a tested segment/encoding budget after variable expansion. Offer an email continuation only to a verified eligible address and according to the requested communication purpose.
4. For email, produce a subject, plain-text body and optionally approved-template HTML. Escape inserted text and links. Use paragraphs/details appropriate to the case; do not copy SMS truncation into email.
5. Keep the recipient, sender, reply-chain headers and attachment URLs under deterministic mapping. The agent may suggest content; an established workflow decides where it is sent.

### Map logical steps to actual nodes

The topology labels below are not extra palette nodes. Use **Branch** for deterministic routing, **Evaluate/Data Parser** for supported field transformations, **HTTP Request or an enabled Custom/Prebuilt integration** for the owned case/authorization/formatting service, **AI Agent** for model invocation, and the appropriate **SMS/Email/Receive** nodes for channel work. External MIME parsing, attachment extraction, durable records and recipient verification require an actual service contract; they are not assumed capabilities of Evaluate. Resolve/Append/Queue/Close steps apply only where the corresponding contact-center integration exists. Exact utility fields and runtime limits are in [chapter 04](04-node-reference.md).

## Recipe 1: SMS support agent with bounded conversation turns

**Example acceptance:** a customer texts a support question, receives a grounded answer or ticket status, can supply one missing detail, and reaches a human when required. Duplicate inbound events do not create another ticket or repeat a completed answer.

**Proposed topology:**

```text
SMS Start
  → normalize + eligibility + duplicate/owner gate
  → load authorized case context
  → AI Agent: Process Message
      success → validate/format response → SMS Send → record result
                  → bounded Receive → normalize new turn → agent again
      handover → human-routing procedure → record ownership → end automation
      error/timeout → bounded recovery or clear fallback → end/route
```

This is the **outer channel flow**. The agent's tool invocation uses recipe 3, not this Receive loop.

| Step | Configuration to place in the build packet |
|---|---|
| Start | SMS mobile-originated event, exact business number and keyword policy; use the documented no-live-session guard when a matching Receive owns subsequent replies |
| Normalize | Map the SMS fields above; handle keyword-only commands before missing-message validation; preserve phone strings |
| Context | Lookup only cases linked to the verified customer; route `owner=human` inbound text to the existing conversation |
| Agent | Configured support agent; current customer request; correct channel/customer identity; current ticket/context as turn data |
| Send | Destination Type=`msisdn`; Destination=`channelCustomer`; From Number=bound business number; Message=formatted SMS; Correlation ID=`sendIntentId` |
| Receive | Bind the same customer/business number and intended keyword; set a finite timeout and route timeout/error explicitly |
| Next turn | Replace current message, increment an application turn counter, preserve operation/case identifiers, and return through the gate |
| Exit | Write disposition; close the AI session only according to the defined session ownership policy; do not equate this with closing a contact-center task |

The Start/Receive bindings and Send fields implement the contracts already summarized in [core nodes](04-node-reference.md) and [SMS](05-channels.md#sms-and-mms-implementation-notes). Node IDs and exact field case are tenant bindings, not values to copy from this table.

**Two continuity choices.** For short conversations, use the finite Receive loop and the documented entry guard. The guard concerns a waiting flow; it is not an AI-memory toggle. For delayed SMS conversations, finish each run and reload durable context on the next inbound event. Choose one ownership strategy for a given asset/use case and document late-message behavior. Do not allow a wildcard Start and an active Receive to race accidentally.

**Example proposed exchange:** customer asks “Status of T-204?”; the lookup tool returns an authorized case with status `waiting_for_customer` and a specific missing item; the agent asks for that item, rather than declaring the case resolved. A subsequent confirmation can initiate a separately authorized update action. A bare `HELP` command must not be sent as an empty agent message merely because keyword parsing removed the command from the message body.

**Failure dispositions.** Invalid customer/message → repair deterministic input. Agent timeout → no inferred answer; offer retry/human route under the bounded policy. Send timeout → reconcile receipts before resend. Customer silence → end this wait without treating the issue as resolved. Human handover → use the real WxCC/CCE/Engage procedure in chapter 06; where no human integration is configured, return a truthful support channel/case reference rather than pretending queue allocation occurred.

**Acceptance cases:** first text; command-only text; second turn; late reply after timeout; another sender during the wait; duplicate event; new question after handoff; ticket lookup denied; tool mutation with ambiguous result; long/Unicode answer after final formatting.

## Recipe 2: email triage and reply agent

**Example acceptance:** an incoming support email is associated with the correct case, its relevant text and safe attachment context are considered, and the customer receives an accurate threaded response or a human-review disposition. Another unrelated email from the same person does not inherit an earlier case's authorization or facts.

**Recommended topology:**

```text
Email Incoming Message
  → eligibility / auto-reply / duplicate gate
  → extract current text + preserve MIME/reply metadata
  → resolve conversation/case + ownership
  → prepare validated attachment context
  → AI Agent: Process Message → optional bounded fulfillment action
  → verify business result → draft/render email
  → configured automatic-send or review policy
  → send/record delivery evidence → persist case context → end run
```

A later email starts another run. This design avoids occupying a Receive while a person may take hours to reply; it does not claim that the Email channel cannot use Receive.

### Entry and normalization

1. Verify the app's actual route. SMTP inbound requires forwarding into Connect. The asset page says SMTP lacks delivery tracking/failure notifications, while the node page says tracking is available for SES or SMTP. Preserve that conflict: verify the selected route's actual receipt capability and use `delivery_unknown` when it is unavailable or unresolved. Cisco documents a 25 MB SMTP inbound attachment limit; SES size/region and legacy-asset limits differ. [Email asset](https://help.webexconnect.io/docs/email), [Email node](https://help.webexconnect.io/docs/email-node)
2. Preserve sender, business mailbox, original subject, Message-ID, In-Reply-To, recipient lists, raw headers and attachment metadata. Keep the original event available for diagnostics under the retention policy.
3. Prefer the current readable request as the agent message. If stripped text is absent, apply an explicit HTML-to-text/quoted-history extraction step. This is application processing; no automatic attachment OCR or quoted-reply removal is assumed in the AI Agent node.
4. Flag auto-generated mail, delivery-status notifications, mailing-list/bulk messages and repeated self-responses according to parsed headers and local policy. These are deterministic routing decisions. Preserve a review route for uncertain classification; do not let generated content recursively trigger automated replies without a stop rule.

### Thread and case continuity

Use the [documented Resolve Conversation strategy](06-integrations-and-contact-center.md#simplified-resolve-conversation-path) when implementing WxCC-linked conversation resolution. With an external ticket system, use its actual thread/case rules. An application may carry the resolved case ID as context, but must verify that the sender is entitled to that case on every request.

Do not replace email thread identity with `email.emailId` alone. Keep subject changes, missing reply headers, forward chains, CC changes and two simultaneous cases as distinct acceptance cases. If using the AI node with the same customer identifier across concurrent cases, the documented UI does not prove per-thread session isolation. Pass case-specific facts per turn and use a verified session-isolation/reset strategy from chapter 13; if unresolved, route sensitive/ambiguous cases to review rather than reuse unknown memory.

### Attachments

**Proposed attachment pipeline:** retain each attachment's original name, MIME type, source reference and scan disposition; reject unsupported or blocked content; extract text only through a configured approved parser; pass a bounded extracted-text summary plus provenance to the agent. A URL is not proof that the agent read the file. For attachment-only mail, either process the approved attachment or ask for usable information/handoff; do not fabricate a document summary.

In a contact-center path, preserve the existing security-scan and append schema from [chapter 06](06-integrations-and-contact-center.md). Show the agent/human which attachments were unavailable. Do not restore a dropped attachment from raw payload data to bypass that disposition.

For sending, the documented dynamic attachment keys are `mimeType`, `name`, `attachmentType`, `mediaUrl`; type `2` refers to a media URL. The node documents up to five attachments with 10 MB combined. The following is a **syntactically corrected illustrative payload**, using an owned placeholder URL rather than Cisco's malformed example URLs:

```json
[
  {
    "mimeType": "application/pdf",
    "name": "case-summary.pdf",
    "attachmentType": 2,
    "mediaUrl": "https://media.example.org/case-summary.pdf"
  }
]
```

Validate actual media access, allowed MIME, size and authorization before delivery. [Email attachment fields](https://help.webexconnect.io/docs/email-node)

### Outbound field plan

| Email-node field | Proposed assignment |
|---|---|
| Destination Type / Destination ID | Email Id / verified reply recipient |
| From Email / From Name | Bound asset / approved support identity |
| ReplyTo Email | The mailbox that will re-enter this workflow |
| Subject | Controlled reply subject with stable case reference |
| Email type / Fallback Text | Text or approved HTML/template / equivalent plain text |
| CC/BCC | Explicit recipient policy; never mirror unknown lists blindly |
| SMTP `In-Reply-To` | Validated inbound Message-ID for this reply, where this route exposes the field |
| Correlation ID | This email's `sendIntentId` |

See [email contract](05-channels.md#email); do not invent a universal Headers field for a tenant whose node does not expose it. Preserve the inbound `In-Reply-To` for lookup, and distinguish it from the inbound `Message-ID` that identifies the message being answered. Correct visual threading still needs a real client/route check when deployment is authorized.

**Example response policy:** a status-only read can send automatically under an approved support policy; a refund, changed account address or other consequential action requires the existing business authorization/confirmation process. A draft requiring review is not a sent message. Keep workflow statuses such as `draft_ready`, `awaiting_review`, `send_submitted` and `delivery_unknown` explicit and application-defined.

**Acceptance cases:** plain/HTML email; attachment-only mail; blocked/oversized attachment; changed subject; missing reply header; two threads from one sender; forwarded email; CC change; auto-response loop; SMTP receipt-availability conflict and no-receipt fallback; duplicate inbound email; denied tool lookup; human-owned conversation.

## Recipe 3: one fulfillment action for ticket lookup or creation

**Example acceptance:** the AI Agent can request a defined ticket operation and receives a machine-readable business result that its response can accurately explain. It cannot create a ticket merely by mentioning one in generated text.

This uses **AI Agent → Connect fulfillment**, configured exactly as [chapter 13](13-ai-agent-flows.md) describes. The short fulfillment runtime and prohibited waiting-node rules apply. Studio's action entities and the parsed Start sample must agree; the JSON below is an **application contract proposal**, not Cisco's built-in request envelope.

```json
{
  "operation": "lookup",
  "operation_id": "op-204-lookup-1",
  "customer_record_id": "customer-verified-42",
  "ticket_id": "T-204",
  "request_summary": "",
  "authorization_ref": "verified-session-reference"
}
```

**Proposed node sequence:** AI Agent Start → normalize input → validate operation/customer authorization → retrieve existing result by operation ID → call the one allowed backend operation → classify response → set result variables → finish with the configured AI outcome payload. Use the actual backend's endpoint, authentication and schema; this chapter does not invent a CRM API.

| Branch | Required behavior |
|---|---|
| `lookup` | Validate ticket ownership/permission; return a minimal factual result or not-found/denied without leaking another customer's data |
| `create` | Require the business's eligible confirmed request and complete required fields; use backend-supported idempotency/deduplication |
| Missing clarification/approval | Return `needs_input` or `approval_required`, then end this tool call; the agent asks outside it |
| Duplicate completed operation | Return the established result rather than create again |
| Backend rejects request | Map actual validation/business rejection to an explicit result |
| Timeout after a possible mutation | Return/record an unresolved status; reconcile by the operation key before retry |
| Unexpected operation | Reject; do not pass through a model-selected URL/method |

Illustrative successful result, suitable for mapping into the configured notification payload:

```json
{
  "operation_id": "op-204-lookup-1",
  "result": "found",
  "ticket": {
    "id": "T-204",
    "status": "waiting_for_customer",
    "next_step": "Provide the device serial number."
  },
  "action_performed": false,
  "customer_message_facts": ["Ticket T-204 exists", "A serial number is needed"]
}
```

Use actual verified data in production. Proposed result vocabulary: `found`, `created`, `not_found`, `denied`, `needs_input`, `approval_required`, `business_rejected`, `unavailable`, `outcome_unknown`. Keep transport details separate from business results. The result must distinguish “ticket created” from “creation request accepted” if the backend is asynchronous.

**Long-running work.** If the backend offers a genuine durable job API, a short action may return that accepted job reference with truthful pending status. A separate approved event/job mechanism can later continue the work. Do not fake a synchronous completion, insert a long Receive, or use Call Workflow as an assumed function return inside fulfillment. If no durable job mechanism exists, return an unsupported/unavailable result and use the defined human path.

**Default side-effect policy.** Lookup is read-only. Create/update is available only where the business has authorized that tool and the current request satisfies its rules. A string such as `authorization_ref` is a lookup reference, not evidence by itself; the backend must validate it. User-provided message text cannot set an `approved=true` shortcut. Human/customer confirmation, if needed, is collected before another action invocation.

**Acceptance cases:** allowed lookup; wrong customer; missing ticket; malicious operation value; repeated create with the same operation ID; different intent with a different ID; timeout after commit; missing notification result; returned pending job; safe error without credentials or raw internal diagnostics.

## Recipe 4: agent-controlled status updates across SMS and email

**Example acceptance:** during an SMS conversation the customer asks for a concise status by text and detailed instructions by email. Both messages reflect the same verified case state, reach verified eligible addresses, and retain independent delivery/reply histories.

**Proposed topology:**

```text
Customer request → AI Agent → verified status lookup
  → communication eligibility / recipient verification / policy gate
  → durable notification intents for requested channels
  → SMS adapter → receipt processing
  → Email adapter → receipt processing where available
  → customer replies re-enter their own channel adapter
```

Choose either immediate bounded orchestration or an existing durable dispatcher appropriate to the response-time constraints. The AI action must return the truthful state—such as intent recorded or messages submitted—rather than wait for recipients to read/respond. This blueprint does not assume Connect supplies a generic transactional outbox or background job queue.

**Shared business result example:** case T-204 requires a serial number. SMS says “T-204 needs your device serial number. Details sent to your verified email.” The last sentence is permitted only if the email submission state supports it; otherwise say that email delivery is pending or omit the claim. Email includes the same case status plus instructions and an approved attachment/link. Neither formatter is allowed to invent a completion date.

**Independent records.** Keep one business operation and separate send intents: `operationId + channel + recipient + contentVersion`. That key is an application proposal, not a provider key format. Retrying email must not resend an already completed SMS; retrying SMS must not create another ticket. A late delivery callback updates only its own send record. A read/open event does not authorize further business mutations.

**Replies and switching channels.** An email reply preserves email thread context; an SMS reply enters its SMS case-resolution path. Reconnect them through the verified customer/case record. If the sender supplies a new email address, perform the defined verification before transferring case information. Cross-channel identity association alone does not establish consent for every purpose.

**Human fallback.** A customer may switch to a person while a notification is pending. Read the current ownership/policy at dispatch time and define whether the promised transactional update still sends. The AI handover branch must use the actual task/conversation process, and the dispatcher must not start a competing conversational bot turn.

**Acceptance cases:** SMS only; email only; both; new unverified email; SMS delivered/email failed; email submitted/SMS unknown; duplicate status request; late callback; changed case status before dispatch; human takeover; reply arrives on the other channel; unavailable or unverified receipt support on the SMTP route.

## Implementation handoff and evidence

For each selected recipe, produce a concrete [build brief](../templates/flow-build-brief.md) containing:

- Actual service/assets, AI Agent type/name/language, installed node versions, and verified channel identity mapping.
- Exact agent action/Start input sample, backend request/result schemas, and outcome notification mappings.
- Node IDs, variable dictionary, named edges and the application's ownership/session policy.
- SMS encoding/segment budget; email reply/attachment/recipient rules; content templates and delivery evidence available for each route.
- Permission, confirmation, idempotency and reconciliation rules for each business side effect.
- Applicable acceptance cases with expected business state, agent statement, sent content and receipt disposition.

This chapter supplies the design packet structure and reusable logic. Completing a design is different from configuring, publishing or executing it. During this documentation mission, all recipes remain proposals; live verification requires the separate authorization described in the project scope.
