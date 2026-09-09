# Observed tenant sample walkthroughs

These are coherent readings of sanitized sample canvases, not runtime test results. Each narrative follows the observed trigger, working nodes, waiting/branching behavior, variable handoffs and terminal handling. [Full node-by-node relationships](tenant-sample-relationships.md) and linked JSON summaries retain the detailed evidence.

## Coverage and evidence boundary

Captured samples: **59**; authored walkthroughs: **59**; scoped expected samples: **59**. All-sample capture/authoring complete: **true**. The parent inventory defines the bounded gallery/native/WxCC set; absent graphs are never counted as reviewed.

An End pseudo-node can encode its route through `data.parentNode` and `params.nodeEvent` without an explicit edge. The summaries preserve that binding and the selected flow outcome. End records whose parent node is absent and duplicate bindings are flagged explicitly, not repaired by inference. Event names from the internal model and rendered event labels are separate fields; neither the raw model nor these summaries constitute a supported public import schema. A configured callback payload, sample response or historical `isTestExecuted` flag does not establish a new successful run.

| Sample | Nodes / edges / End bindings | Walkthrough |
| --- | --- | --- |
| [AI Agent Scripted Doctor Appointment](#gallery-ai-doctor) | 43 / 160 / 31 | authored |
| [AI Agent Livechat Generic](#gallery-ai-livechat) | 27 / 109 / 26 | authored |
| [AppointmentReminder](#gallery-appointment-reminder) | 11 / 10 / 19 | authored |
| [Autoresponder](#gallery-autoresponder) | 2 / 1 / 3 | authored |
| [Chatbot](#gallery-chatbot) | 10 / 9 / 15 | authored |
| [LogisticsParcelNotifications](#gallery-logistics) | 16 / 16 / 26 | authored |
| [SMSSurvey](#gallery-sms-survey) | 6 / 6 / 9 | authored |
| [AI Agent Fulfilment - Track Package](#gallery-track-package) | 2 / 1 / 3 | authored |
| [WebhooktoSMSalerts](#gallery-webhook-sms) | 2 / 1 / 0 | authored |
| [Block card and order replacement.workflow](#native-block-card-and-order-replacement) | 2 / 1 / 1 | authored |
| [cancel_appointment.workflow](#native-cancel-appointment) | 2 / 1 / 0 | authored |
| [cancel_booking.workflow](#native-cancel-booking) | 2 / 1 / 2 | authored |
| [cancel_checkin.workflow](#native-cancel-checkin) | 2 / 1 / 3 | authored |
| [check_availability.workflow](#native-check-availability) | 2 / 1 / 0 | authored |
| [checkin.workflow](#native-checkin) | 2 / 1 / 3 | authored |
| [create_appointment.workflow](#native-create-appointment) | 2 / 1 / 0 | authored |
| [Fetch account balance.workflow](#native-fetch-account-balance) | 5 / 4 / 0 | authored |
| [Fetch Recent Transactions.workflow](#native-fetch-recent-transactions) | 5 / 4 / 0 | authored |
| [get_flight_info.workflow](#native-get-flight-info) | 2 / 1 / 2 | authored |
| [lookup_appointment.workflow](#native-lookup-appointment) | 2 / 1 / 0 | authored |
| [lookup_flights.workflow](#native-lookup-flights) | 2 / 1 / 3 | authored |
| [Register Transaction Dispute.workflow](#native-register-transaction-dispute) | 2 / 1 / 1 | authored |
| [Request priority shipping.workflow](#native-request-priority-shipping) | 2 / 1 / 1 | authored |
| [reschedule_flight.workflow](#native-reschedule-flight) | 2 / 1 / 2 | authored |
| [sendSMS.workflow](#native-sendsms) | 2 / 1 / 0 | authored |
| [Verify user.workflow](#native-verify-user) | 2 / 1 / 3 | authored |
| [AMB Simplified Flow.workflow](#wxcc-amb-simplified-flow) | 13 / 36 / 28 | authored |
| [Apple Basic Inbound Flow.workflow](#wxcc-apple-basic-inbound-flow) | 13 / 49 / 14 | authored |
| [Apple Form Response Flow.workflow](#wxcc-apple-form-response-flow) | 4 / 9 / 13 | authored |
| [Apple iMessage App Flow.workflow](#wxcc-apple-imessage-app-flow) | 5 / 13 / 12 | authored |
| [Apple Inbound Flow with Form.workflow](#wxcc-apple-inbound-flow-with-form) | 17 / 77 / 14 | authored |
| [Apple Inbound Flow with IntentId GroupId based Routing.workflow](#wxcc-apple-inbound-flow-with-intentid-groupid-based-routing) | 14 / 58 / 14 | authored |
| [Apple List Picker Flow.workflow](#wxcc-apple-list-picker-flow) | 18 / 86 / 14 | authored |
| [Apple Time Picker and List Picker Response Flow.workflow](#wxcc-apple-time-picker-and-list-picker-response-flow) | 6 / 18 / 17 | authored |
| [Apple Time Picker Flow.workflow](#wxcc-apple-time-picker-flow) | 14 / 57 / 14 | authored |
| [Apple Unsubscribe Flow.workflow](#wxcc-apple-unsubscribe-flow) | 3 / 5 / 13 | authored |
| [EmailAttachmentDropNotification.workflow](#wxcc-emailattachmentdropnotification) | 11 / 39 / 14 | authored |
| [EmailInboundFlow.workflow](#wxcc-emailinboundflow) | 10 / 35 / 14 | authored |
| [EmailInboundSampleFlowWithContactPriority.workflow](#wxcc-emailinboundsampleflowwithcontactpriority) | 11 / 38 / 14 | authored |
| [FacebookAttachmentDropNotification.workflow](#wxcc-facebookattachmentdropnotification) | 11 / 39 / 14 | authored |
| [FacebookCloseWithWxmFlow.workflow](#wxcc-facebookclosewithwxmflow) | 12 / 36 / 27 | authored |
| [FacebookInboundFlow.workflow](#wxcc-facebookinboundflow) | 10 / 35 / 14 | authored |
| [FacebookTaskBotInboundFlow.workflow](#wxcc-facebooktaskbotinboundflow) | 31 / 98 / 35 | authored |
| [Live Chat Close Flow.workflow](#wxcc-live-chat-close-flow) | 4 / 5 / 19 | authored |
| [Livechat Inbound flow with proactive chat changes.workflow](#wxcc-livechat-inbound-flow-with-proactive-chat-changes) | 15 / 67 / 14 | authored |
| [LiveChatCloseWithWxmFlow.workflow](#wxcc-livechatclosewithwxmflow) | 12 / 36 / 27 | authored |
| [LivechatInbound flow.workflow](#wxcc-livechatinbound-flow) | 13 / 55 / 14 | authored |
| [LivechatInboundFlowWithoutForm.workflow](#wxcc-livechatinboundflowwithoutform) | 9 / 32 / 14 | authored |
| [LiveChatInboundSampleFlowWithSetVariable.workflow](#wxcc-livechatinboundsampleflowwithsetvariable) | 14 / 66 / 14 | authored |
| [LiveChatInboundSampleFlowWithSetVariablePIQAndEWT.workflow](#wxcc-livechatinboundsampleflowwithsetvariablepiqandewt) | 17 / 69 / 25 | authored |
| [LiveChatQABotInboundFlow.workflow](#wxcc-livechatqabotinboundflow) | 29 / 114 / 24 | authored |
| [SMS inbound.workflow](#wxcc-sms-inbound) | 10 / 32 / 17 | authored |
| [SmsQABotInboundFlow.workflow](#wxcc-smsqabotinboundflow) | 23 / 84 / 27 | authored |
| [Task Close Flow With Screen Pop.workflow](#wxcc-task-close-flow-with-screen-pop) | 3 / 2 / 9 | authored |
| [Task Close Flow.workflow](#wxcc-task-close-flow) | 3 / 2 / 9 | authored |
| [Task Modified Flow.workflow](#wxcc-task-modified-flow) | 4 / 3 / 12 | authored |
| [Task Routed Flow.workflow](#wxcc-task-routed-flow) | 3 / 2 / 9 | authored |
| [Task Routed Sample Flow For Extracting Variables.workflow](#wxcc-task-routed-sample-flow-for-extracting-variables) | 3 / 2 / 9 | authored |
| [Whatsapp inbound.workflow](#wxcc-whatsapp-inbound) | 10 / 35 / 14 | authored |

## Reuse discipline

Begin at Start and follow the actual event→node relationships. Distinguish existing-conversation append paths from new conversations and bot-turn loops. Map each consumer to its exact node output or custom-variable writer; check custom defaults and on-enter/on-leave assignments. Preserve sample-specific case, node version and extraction paths only as observed evidence. Adapt identities, assets, authorization and system contracts for the target tenant. Redacted hosts/credentials and embedded mock responses are not usable production bindings.

Read each stated limitation before reusing a pattern. Cross-page links and cycles are derived only from captured relationships; missing pages or script-generated values stay unresolved. Configuration visibility does not authorize execution, messages, external writes or publication.

<a id="gallery-ai-doctor"></a>

## AI Agent Scripted Doctor Appointment

Observed 2026-09-08T23:56:36.255Z. [Sanitized model](../evidence/sample-flows/observed/gallery-ai-doctor.json) · [graph JSON](sample-flows/summaries/gallery-ai-doctor.json) · [all relationships](tenant-sample-relationships.md#gallery-ai-doctor).

This extends the generic Live Chat lifecycle with appointment fulfillment. Search/Resolve Conversation, pre-chat, bot replies, append operations and Receive 756 form the same outer conversation. After an agent reply is sent/appended, parser 1745 reads SessionMetadata and parser 1725 reads messageMetadata. Branch 1727 selects availability, create, lookup or cancel using responseKey. Each branch extracts relevant entities, calls its HTTP node, and joins Evaluate 1731 to construct fulfilmentResp. The response is sent and appended before returning to Receive. A fulfillment failure can use the error-handover path. On agent handover, previous-intent classification chooses an appointment-specific queue or the general queue. Receive failure closes the task and the agent session.

**Exact handoffs:** AI `MessageMetadata` is copied to `messageMetadata`; parser 1725 extracts `$.templateKey` as `responseKey`. `SessionMetadata` supplies `$.previous_intent_model_state.intent.name` as PreviousIntent and `$.model_state.entities.<entity>.value` for date/period/name/birth-date/reason. HTTP availability maps `$.nearest_available_slots[0]` to `n1726.nearest_available_slot`; create maps appointment_number/status; lookup maps date/time. `fulfilmentStatusCode` and those outputs feed `fulfilmentResp`, then Send 1735 and Append 1738.

**Adaptation limits:** These nested metadata paths are sample/version-specific observations, not universal AI Agent output guarantees. The node exposes MessageMetadata/SessionMetadata rather than legacy Task Bot Intent/Entities outputs. It uses integration version 52902 and case-sensitive DataStore mapping. Close Session timeout ends Incomplete here. Embedded API examples, queue IDs, selected agents and entity names require adaptation; the captured n9 debug reference has no captured producer. Material error-path mismatch: Evaluate 1731 assigns agentTextResponse on backend failure, but its onleave assignment persists agentTextResp. Its result 1 (error handover) leads to Send 768, which consumes $(agentTextResp), previously populated from n1695.TextResponse. The intended system-error text is therefore not established by this captured assignment; stale agent text may be reused. In an authorized adaptation, align the script variable, transition assignment and Send consumer, initialize the failure message explicitly, and verify the failed-fulfillment path. This is a documentation finding; the native sample was not edited or executed.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-ai-livechat"></a>

## AI Agent Livechat Generic

Observed 2026-09-08T23:56:08.143Z. [Sanitized model](../evidence/sample-flows/observed/gallery-ai-livechat.json) · [graph JSON](sample-flows/summaries/gallery-ai-livechat.json) · [all relationships](tenant-sample-relationships.md#gallery-ai-livechat).

An incoming app message reaches Search Conversation 1621. New or closed conversations receive a pre-chat form and wait at Receive 38; active, queued or on-hold conversations go directly through payload preparation 1610 to Resolve Conversation 1590. Created/reopened outcomes append the form and invoke AI Agent 1695; appended and accepted outcomes terminate through their own End bindings, avoiding a second bot turn on that path. The bot success path sends TextResponse, appends that outgoing message, and waits at Receive 756. A customer reply is normalized/checked, appended inbound, and sent back to AI Agent: this is the captured conversational loop. Handover sends a notice, appends it, queues the task and acknowledges queuing. Receive errors/timeouts close the task, notify the customer and invoke the separate AI Agent Close Session method.

**Exact handoffs:** `n2.inappmessaging.userId` and `threadId` anchor sends, search and receives. Start/Receive transition actions write `questionForBot`; the Process Message request consumes `$(questionForBot)`. `$(n1695.TextResponse)` feeds Send Bot response and Append Conversation. Close Session consumes `$(n1695.SessionId)`. Resolve Conversation exposes `conversationOperation`, whose timeout branch distinguishes created/reopened from appended.

**Adaptation limits:** The captured AI integration version ID is 52902 with Process Message method 58694 and Close Session 58695. Its mapping spells `DataStore`, whereas the compact current documentation uses `Datastore`; preserve the observed version/case instead of generalizing. The Close Session timeout End is configured as Success here, unlike the doctor sample. A log references uncaptured n9.evaluate.output; this is stale/uncaptured debug provenance, not evidence of a working producer.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-appointment-reminder"></a>

## AppointmentReminder

Observed 2026-09-08T23:58:37.146Z. [Sanitized model](../evidence/sample-flows/observed/gallery-appointment-reminder.json) · [graph JSON](sample-flows/summaries/gallery-appointment-reminder.json) · [all relationships](tenant-sample-relationships.md#gallery-appointment-reminder).

Webhook Start 2 sends an appointment reminder through SMS 225, then Receive 11 waits 600 seconds. Branch 19 maps A to HTTP 25 (`/appointconfirm`) and B to HTTP 29 (`/appointmentcancel`). HTTP success sends the relevant confirmation/cancellation message, while HTTP error sends an unable-to-process response. Unrecognized customer input receives a clarification message and does not loop back in the captured graph.

**Exact handoffs:** The reminder uses custom values `$(name)` and `$(dateTime)` and sends to `$(msisdn)`. Branch 19 reads `$(n11.receive.message)`. Confirmation/cancellation are represented by separate HTTP paths and separate success/failure SMS nodes.

**Adaptation limits:** The timestamp appears in message text; no Delay/Scheduler node is captured, so this graph alone does not schedule reminders. The sample models the business actions with GET and does not prove safe mutation semantics or an appointment-ID contract. Several final-send error declarations lack captured routes. Do not infer that the acknowledgement updates a real appointment.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-autoresponder"></a>

## Autoresponder

Observed 2026-09-08T23:58:25.886Z. [Sanitized model](../evidence/sample-flows/observed/gallery-autoresponder.json) · [graph JSON](sample-flows/summaries/gallery-autoresponder.json) · [all relationships](tenant-sample-relationships.md#gallery-autoresponder).

SMS Start 2 immediately routes to Send SMS 33. The reply acknowledges the incoming message, and the send's End bindings map the observed outcomes. There is no Receive node because this flow handles one inbound event per invocation, rather than maintaining an in-flow conversation.

**Exact handoffs:** The reply text interpolates `$(n2.sms.message)` and its recipient is the inbound sender `$(n2.sms.sender_number)`. Reusing the source identity prevents accidentally addressing the business number, but actual sender/asset configuration still needs tenant binding.

**Adaptation limits:** This sample contains no explicit keyword classifier, rate limiter, duplicate-event guard or bot invocation. It demonstrates acknowledgement only; configured End outcomes are not proof a handset received the response.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-chatbot"></a>

## Chatbot

Observed 2026-09-08T23:58:00.130Z. [Sanitized model](../evidence/sample-flows/observed/gallery-chatbot.json) · [graph JSON](sample-flows/summaries/gallery-chatbot.json) · [all relationships](tenant-sample-relationships.md#gallery-chatbot).

An inbound SMS starts a deterministic pizza menu. Send 157 presents A/B/C choices; Receive 11 waits 600 seconds; Branch 19 routes choices to one of three HTTP GET nodes. Each HTTP success path sends an order-confirmation SMS. This is a menu-and-branch example, with no observed AI Agent node and no customer-response loop after the order branch.

**Exact handoffs:** Every outgoing SMS addresses `$(n2.sms.sender_number)`. Branch 19 consumes `$(n11.receive.message)`; A selects Cajun, the nominal B branch selects Beef, and C selects Branch3. The HTTP nodes each use the same captured `/api/cajunpziza` path, so distinct menu outcomes do not establish distinct business-system requests.

**Adaptation limits:** The Beef comparison is captured as `B$(n11.receive.message)` rather than plain B. Correct that expression and each API binding before treating the menu as operational. Several HTTP/send error declarations have no captured route. The sample label Chatbot must not be mistaken for evidence of Studio intents, an LLM or autonomous reasoning.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-logistics"></a>

## LogisticsParcelNotifications

Observed 2026-09-08T23:56:52.097Z. [Sanitized model](../evidence/sample-flows/observed/gallery-logistics.json) · [graph JSON](sample-flows/summaries/gallery-logistics.json) · [all relationships](tenant-sample-relationships.md#gallery-logistics).

A webhook triggers the delivery SMS, then Receive 4 waits up to 86400 seconds. Branch 5 recognizes CANCEL or CHANGE case-insensitively. CANCEL calls HTTP 15, then sends cancellation confirmation on success or a technical-error message on error. CHANGE asks for an address, waits at Receive 31, echoes that address for confirmation, and waits at Receive 36. YES calls HTTP 41 and sends update confirmation/error; RETRY returns to the address question, making an explicit loop. Other initial answers receive an invalid-response message. Thus the two API actions occur after distinct customer confirmations, rather than merely after sending the first alert.

**Exact handoffs:** The initial message uses `n2.inboundWebhook.customerName`, `parcelID`, `delievryTime` and `deliveryDate`; recipients use `phoneNumber`. Branches consume `$(n4.receive.message)` and `$(n36.receive.message)`. The proposed address is `$(n31.receive.message)` and is echoed by Send 33 before the YES branch.

**Adaptation limits:** The initial webhook parse schema and business URLs are not operationally populated in this capture. Preserve the misspelled observed `delievryTime` only when matching the actual trigger schema. Several Receive failure/timeout declarations have no captured destination, and the RETRY cycle has no explicit attempt counter. Confirm API body bindings and recovery policy before reuse; customer-facing success text is not delivery/API execution evidence.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-sms-survey"></a>

## SMSSurvey

Observed 2026-09-08T23:57:36.392Z. [Sanitized model](../evidence/sample-flows/observed/gallery-sms-survey.json) · [graph JSON](sample-flows/summaries/gallery-sms-survey.json) · [all relationships](tenant-sample-relationships.md#gallery-sms-survey).

Webhook Start 2 sends the survey through SMS 122, then Receive 11 waits 600 seconds for an SMS reply. Branch 22 accepts values 1 through 5 and sends the thank-you message. Any other answer goes through correction SMS 143 and back to Receive 11, creating the observed retry loop. There is no captured persistence/API node to store the rating and no explicit attempt counter in the loop.

**Exact handoffs:** The prompt uses `$(name)` and all SMS destinations use `$(number)`. Branch 22 evaluates `$(n11.receive.message)` against numeric choices 1–5. The custom-variable defaults are preserved, but a source for number is not established by the captured Start configuration.

**Adaptation limits:** The correction message asks for 1–10 while the initial question and branch accept only 1–5. Reconcile this concrete inconsistency before adapting the sample. Some send-error declarations lack captured routes. A thank-you send proves neither storage nor a measured response rate, and no messages were sent during inspection.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-track-package"></a>

## AI Agent Fulfilment - Track Package

Observed 2026-09-09T00:09:50.634Z. [Sanitized model](../evidence/sample-flows/observed/gallery-track-package.json) · [graph JSON](sample-flows/summaries/gallery-track-package.json) · [all relationships](tenant-sample-relationships.md#gallery-track-package).

The AI Agent event enters Start 2, then its onBegin edge invokes HTTP Request 3. The HTTP node performs GET against the sample tracking path and extracts the complete JSON body under fullResp. Its End bindings associate internal oncomplete (rendered onSuccess) with Success, onerror with Error, and ontimeout with Incomplete. The flow-settings Last Execution Status entry contains an agent-facing response object. This is a fulfillment adapter: the agent supplies a package identifier, Connect calls the business API, and flow outcome configuration returns data; there is no Send or Receive node in this graph.

**Exact handoffs:** Start output `$(n2.aiAgent.packageNum)` becomes `/track/$(n2.aiAgent.packageNum)` in the HTTP URL. HTTP JSON path `$` maps to `n3.fullResp`; `$(n3.fullResp)` is used by the on-leave log and notification custompayload.response. The custom response also carries `$(transid)`.

**Adaptation limits:** The configured example marks packageNum nonmandatory and includes embedded historical response data. Those examples are not a successful current API response. URL hosts/header values are redacted. The same response variable is referenced by the all-status outcome configuration, so validate what is available on failure before adapting the return contract. No loop or retry is captured.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="gallery-webhook-sms"></a>

## WebhooktoSMSalerts

Observed 2026-09-08T23:57:29.390Z. [Sanitized model](../evidence/sample-flows/observed/gallery-webhook-sms.json) · [graph JSON](sample-flows/summaries/gallery-webhook-sms.json) · [all relationships](tenant-sample-relationships.md#gallery-webhook-sms).

This is the smallest event-to-message adapter: Webhook Start 2 connects directly to SMS 3 through onBegin. The send's terminal behavior and flow outcome settings remain in the complete graph summary. There is no conversation loop, business API call, data parser, schedule or reply wait.

**Exact handoffs:** SMS destination is `$(n2.inboundWebhook.phone)` and message is `$(n2.inboundWebhook.alertdesc)`. Both depend on the webhook's eventual payload/schema binding; there is no intermediate custom-variable transformation.

**Adaptation limits:** The captured Webhook configuration has empty parseOutput/jsonData and no configured URL. It illustrates the intended field contract but does not establish an installed webhook. SMS onerror declares a target but no corresponding captured edge/End binding is present. Provision sender/assets and define failure behavior before using the pattern.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-block-card-and-order-replacement"></a>

## Block card and order replacement.workflow

Observed 2026-09-09T00:00:54.162Z. [Sanitized model](../evidence/sample-flows/observed/native-block-card-and-order-replacement.json) · [graph JSON](sample-flows/summaries/native-block-card-and-order-replacement.json) · [all relationships](tenant-sample-relationships.md#native-block-card-and-order-replacement).

AI Agent Start 2 receives optional string `customer_id` and `order_replacement`, then `onbegin`/rendered `onBegin` enters HTTP Request 6. It posts to `/block_card`. End pseudo-node 15 belongs to node 6 through `data.parentNode=6` and `params.nodeEvent=oncomplete`, rendered `onSuccess`; that terminal association exists without a separate edge record. There is one backend operation, not separate block and replacement-order nodes.

**Exact handoffs:** The HTTP body renames `$(n2.aiAgent.customer_id)` to `user_id` and passes `$(n2.aiAgent.order_replacement)` as `order_replacement`. Connection/request timeout fields both contain 10000. Response paths `$.replacement_card` and `$.status` become `n6.replacement_card` and `n6.status`. The all-status Last Execution Status outcome stores custom return fields `status=$(n6.status)` and `replacement_card=$(n6.replacement_card)`; it does not return the HTTP status code.

**Adaptation limits:** No explicit HTTP error edge, retry, reconciliation lookup, or conditional second operation appears. The saved response example describes a card block without a replacement, but is not a current execution result. Any meaning of order_replacement values and backend write safety requires the actual endpoint contract. Hosts and headers are redacted. The internal model is not a public import schema and runtime testing is explicitly false; no card or replacement order was changed.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-cancel-appointment"></a>

## cancel_appointment.workflow

Observed 2026-09-08T23:59:56.277Z. [Sanitized model](../evidence/sample-flows/observed/native-cancel-appointment.json) · [graph JSON](sample-flows/summaries/native-cancel-appointment.json) · [all relationships](tenant-sample-relationships.md#native-cancel-appointment).

Start 2 receives an AI Agent event whose parsed input is optional string `appointment_number`. Its `onbegin` event, rendered `onBegin`, enters HTTP Request 3, which posts to the sanitized `/cancel_appointment` endpoint. That is the complete connected operational sequence in the capture. HTTP declares `oncomplete` and `onerror`, but neither has an explicit outgoing graph edge to another processing node.

**Exact handoffs:** HTTP body `$(n2.aiAgent.payload)` forwards the whole incoming action payload. The Last Execution Status outcome is configured to notify for all status codes, returning transaction, flow, and service identifiers plus `httpStatus=$(n3.http.statusCode)` and `httpResponse=$(n3.http.responseBody)`. The payload therefore preserves the backend's status and body rather than manufacturing a cancellation confirmation. No appointment-number rewrite or cancellation-status extraction is visible.

**Adaptation limits:** A cancellation request is configured; successful cancellation was not executed or established. There is no visible confirmation branch, duplicate-write protection, retry loop, reconciliation lookup, or customer notification step. The declared input type is string although its embedded example value is numeric; consumers should preserve that observed discrepancy when adapting the contract. Hosts and headers are redacted. The internal model is not an importable public schema, and its `runtime_tested=false` limits this account to configuration evidence.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-cancel-booking"></a>

## cancel_booking.workflow

Observed 2026-09-09T00:01:47.372Z. [Sanitized model](../evidence/sample-flows/observed/native-cancel-booking.json) · [graph JSON](sample-flows/summaries/native-cancel-booking.json) · [all relationships](tenant-sample-relationships.md#native-cancel-booking).

AI Agent Start 2 exposes optional strings `booking_id`, `reason`, and `flight_id`. Its internal `onbegin`, rendered `onBegin`, enters HTTP 3 POST `/cancel_flight`. Two End pseudo-nodes refer back to HTTP 3: node 9 binds `oncomplete`/rendered `onSuccess` with exitResult 2, and node 10 binds `onerror`/`onError` with exitResult 3. These terminal relationships are stored through parentNode and nodeEvent rather than ordinary edge records.

**Exact handoffs:** The HTTP body maps each input explicitly: `booking_id=$(n2.aiAgent.booking_id)`, `flight_id=$(n2.aiAgent.flight_id)`, and `reason=$(n2.aiAgent.reason)`. Both timeout fields contain 10000. Response extraction maps `$.booking.booking_id` to `n3.booking_id`, `$.message` to `n3.message`, and `$.error` to `n3.error`. The all-status Last Execution Status notification uses payloadType 1 and stores those three outputs with `transactionID=$(transid)`.

**Adaptation limits:** No refund calculation, confirmation step, retry loop, or follow-up booking lookup is visible. The two identifiers are incoming dependencies; this graph does not call the flight-info sample to obtain them. Error termination is configured but no error-specific replacement payload is shown if extraction fails. Hosts/headers are redacted, sample response data is not current cancellation evidence, and this internal model is not a public import schema. Runtime testing is false; no booking was cancelled.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-cancel-checkin"></a>

## cancel_checkin.workflow

Observed 2026-09-09T00:01:50.901Z. [Sanitized model](../evidence/sample-flows/observed/native-cancel-checkin.json) · [graph JSON](sample-flows/summaries/native-cancel-checkin.json) · [all relationships](tenant-sample-relationships.md#native-cancel-checkin).

AI Agent Start 2 declares optional string `booking_id`, `notes`, and `last_name`. Its `onbegin`/rendered `onBegin` reaches HTTP 3 POST `/cancel_check_in`. End pseudo-nodes 9, 10, and 13 belong to HTTP 3: `oncomplete`/`onSuccess` has exitResult 2, while `onerror`/`onError` and `ontimeout`/`onTimeout` both have exitResult 3. The timeout terminal is present even though the HTTP children list only completion and error events.

**Exact handoffs:** The request preserves `booking_id=$(n2.aiAgent.booking_id)` and `last_name=$(n2.aiAgent.last_name)`, but renames `$(n2.aiAgent.notes)` to body field `reason`. Connection/request timeouts are 10000. Response `$.booking.check_in_notes` is named `n3.reason`, with `$.message` and `$.error` extracted separately. The all-status Last Execution Status payload, with payloadType 1, returns transactionID, `$(n3.message)`, `$(n3.reason)`, and `$(n3.error)`.

**Adaptation limits:** This is check-in cancellation, not cancellation of the flight booking itself. No loop, confirmation lookup, channel notification, or direct connection to another sample exists. Incoming notes and returned reason have different source paths despite their related meaning. Stored names and booking examples are fixtures. Headers and hosts are redacted; the internal model is not an importable public schema. Runtime testing is false, so neither the write nor timeout response behavior was exercised.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-check-availability"></a>

## check_availability.workflow

Observed 2026-09-08T23:59:30.439Z. [Sanitized model](../evidence/sample-flows/observed/native-check-availability.json) · [graph JSON](sample-flows/summaries/native-check-availability.json) · [all relationships](tenant-sample-relationships.md#native-check-availability).

Start 2 is an AI Agent event with optional string inputs `preferred_period` and `preferred_date`. Its internal `onbegin` event, rendered `onBegin`, leads directly to HTTP Request 3. The request posts to the sanitized `/check_availability` path. There is no parser, availability-selection branch, or second operation between the incoming action and the backend call. HTTP declares `oncomplete` and `onerror`; the captured model has no explicit outgoing edges from that node.

**Exact handoffs:** The request body is the whole `$(n2.aiAgent.payload)`, not a newly constructed object using the individual parsed fields. The notifying Last Execution Status outcome applies to all status codes and maps `httpStatus` from `$(n3.http.statusCode)` and `httpResponse` from `$(n3.http.responseBody)`, alongside transaction, flow, and service identifiers. This makes the observed sample a backend response pass-through; no normalization of dates, periods, or available-slot results is configured.

**Adaptation limits:** The configured example date/period are fixtures, not available appointments. No retry loop, explicit request timeout, business-result check, SMS/email send, or cross-flow call appears. The backend host and header values are redacted. This internal canvas model is evidence rather than a public import schema; `runtime_tested` is false, so neither backend availability nor an agent's interpretation of the returned result was verified.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-checkin"></a>

## checkin.workflow

Observed 2026-09-09T00:01:54.153Z. [Sanitized model](../evidence/sample-flows/observed/native-checkin.json) · [graph JSON](sample-flows/summaries/native-checkin.json) · [all relationships](tenant-sample-relationships.md#native-checkin).

AI Agent Start 2 exposes optional string `booking_id`, `notes`, and `last_name`, then `onbegin`/rendered `onBegin` enters HTTP 3 POST `/check_in`. End pseudo-nodes associate with HTTP 3 through parentNode and nodeEvent: node 9 terminates `oncomplete`/`onSuccess` with exitResult 2, node 10 terminates `onerror`/`onError` with 3, and node 13 terminates `ontimeout`/`onTimeout` with 4. The graph has no retry return edge.

**Exact handoffs:** HTTP body uses `booking_id=$(n2.aiAgent.booking_id)`, `last_name=$(n2.aiAgent.last_name)`, and `notes=$(n2.aiAgent.notes)`. Both timeout fields contain 10000. JSONPath `$.booking.check_in_notes` becomes output `n3.notes`; `$.message` and `$.error` become their corresponding n3 outputs. The all-status Last Execution Status notification stores payloadType 1 and returns transactionID, message, error, and notes through those outputs. It does not create a boarding-pass response or independently retrieve flight details.

**Adaptation limits:** The check-in action and its error/timeout terminal configuration were inspected without execution. Embedded booking/name/notes examples are fixtures, and a stored success message does not prove a completed check-in. No explicit business-status branch, duplicate-write safeguard, reconciliation operation, or SMS/email send appears. Hosts and header values are redacted. This internal canvas representation is evidence rather than a public import schema; `runtime_tested=false` applies to all paths.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-create-appointment"></a>

## create_appointment.workflow

Observed 2026-09-09T00:00:34.955Z. [Sanitized model](../evidence/sample-flows/observed/native-create-appointment.json) · [graph JSON](sample-flows/summaries/native-create-appointment.json) · [all relationships](tenant-sample-relationships.md#native-create-appointment).

AI Agent Start 2 declares optional string inputs `reason`, `date_of_birth`, `patient_name`, and `time_slot`. Its internal `onbegin`, rendered `onBegin`, connects to HTTP Request 3. The request posts to the sanitized `/create_appointment` path. There is no intervening slot lookup, user-confirmation node, or second write: the sample delegates booking behavior to that endpoint.

**Exact handoffs:** HTTP body `$(n2.aiAgent.payload)` forwards the complete incoming action payload. It does not reconstruct the body from the four separately exposed variables. The notifying Last Execution Status outcome covers all status codes and stores a custom payload with transaction, flow, and service identifiers, `httpStatus=$(n3.http.statusCode)`, and `httpResponse=$(n3.http.responseBody)`. No response-field extraction or appointment-ID assignment appears; any booking identifier must remain inside the returned HTTP body.

**Adaptation limits:** The observed model has only the Start-to-HTTP edge, no retry loop, explicit request timeout, idempotency key, or compensating cancellation. Example names, dates, and reasons are sample fixtures. No SMS/email confirmation is sent by this graph. Header values and hosts are redacted. The internal canvas representation is not a public import schema, and `runtime_tested=false` means neither creation nor the returned booking contract was verified by execution.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-fetch-account-balance"></a>

## Fetch account balance.workflow

Observed 2026-09-09T00:01:01.220Z. [Sanitized model](../evidence/sample-flows/observed/native-fetch-account-balance.json) · [graph JSON](sample-flows/summaries/native-fetch-account-balance.json) · [all relationships](tenant-sample-relationships.md#native-fetch-account-balance).

AI Agent Start 2 takes optional string `customer_id` and enters HTTP 3 through `onbegin`/`onBegin`. HTTP GET `/get_balance/$(n2.aiAgent.customer_id)` uses connection/request timeout values 10000. Its internal `oncomplete`, rendered `onSuccess`, leads to Branch 5. Status code 200 chooses `user found` and Evaluate 7; the fallback `user not found` goes to Evaluate 8.

**Exact handoffs:** HTTP extracts `$.account_balance` and `$.status`. Evaluate 7 has constant expression 1, but its on-enter session actions perform the useful transformation: set `status=success`, `balance=$(n3.account_balance)`, and a success message. Evaluate 8 assigns `status=failure` and a not-found message. Last Execution Status uses `payloadType=1` and stores `payload` fields transactionID, `$(status)`, `$(balance)`, and `$(message)`. Its separate custompayload instead mentions transactions; that alternate stored object should not be silently treated as the balance contract.

**Adaptation limits:** The HTTP onerror port has no explicit recovery edge, so it does not necessarily pass through the not-found assignment. The branch classifies all non-200 completed responses as not found; it does not inspect body semantics. No retry, channel send, or other flow call appears. Embedded `isTestExecuted=true` and response examples belong to the template, not this inspection. Hosts/headers are redacted, the model is internal rather than an import schema, and `runtime_tested=false`.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-fetch-recent-transactions"></a>

## Fetch Recent Transactions.workflow

Observed 2026-09-09T00:00:57.584Z. [Sanitized model](../evidence/sample-flows/observed/native-fetch-recent-transactions.json) · [graph JSON](sample-flows/summaries/native-fetch-recent-transactions.json) · [all relationships](tenant-sample-relationships.md#native-fetch-recent-transactions).

AI Agent Start 2 supplies `customer_id` to HTTP 3 GET `/get_transactions/$(n2.aiAgent.customer_id)`. Start `onbegin` renders as `onBegin`; HTTP `oncomplete` renders as `onSuccess` and connects to Branch 5. HTTP status 200 selects `user found` → Evaluate 7; every other completed status selects `user not found` → Evaluate 8. No pagination or per-transaction loop is present.

**Exact handoffs:** HTTP extraction names `last_transactions` from JSONPath `$`, the whole response, rather than `$.last_transactions`; it also extracts `$.status`. Evaluate 7 on-enter actions assign `status=success`, `transactions=$(n3.last_transactions)`, and a success message. Evaluate 8 assigns failure status/message. The outcome has `payloadType=1`: its payload returns `status=$(n3.status)` and `transactions=$(n3.last_transactions)` directly, plus transactionID and `$(message)`. A distinct custompayload references session `$(status)` and unquoted `$(transactions)`. Thus the stored payload bypasses two session assignments and preserves the response wrapper.

**Adaptation limits:** HTTP errors have no explicit recovery edge; the non-200 branch is not a general transport-failure handler. No retry, dispute-registration call, or customer message is configured. Embedded transaction examples and Evaluate test flags are historical template data, not observed account activity or a current test. Hosts and headers are redacted. This internal model is not an import schema; `runtime_tested=false` leaves response serialization and agent interpretation unverified.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-get-flight-info"></a>

## get_flight_info.workflow

Observed 2026-09-09T00:02:04.734Z. [Sanitized model](../evidence/sample-flows/observed/native-get-flight-info.json) · [graph JSON](sample-flows/summaries/native-get-flight-info.json) · [all relationships](tenant-sample-relationships.md#native-get-flight-info).

AI Agent Start 2 takes optional string `booking_id` and `last_name`. Its `onbegin`/rendered `onBegin` enters HTTP 3 GET `/get_booking_info?booking_id=$(n2.aiAgent.booking_id)&last_name=$(n2.aiAgent.last_name)`. Connection/request timeout values are 10000. End pseudo-node 12 binds HTTP `oncomplete`/`onSuccess` with exitResult 2; node 13 binds `onerror`/`onError` with 3. No downstream booking modification occurs.

**Exact handoffs:** HTTP extracts fields from `$.booking`: arrival/departure times, flight number, origin/destination, booking status, flight_id, booking_id, flight status, and check_in_status. It renames `$.booking.user_name` to `n3.passenger_name` and extracts top-level `$.error`. The all-status Last Execution Status outcome has payloadType 2 and stores a custompayload with transactionID plus these named n3 outputs. The returned booking_id and flight_id are useful inputs for later actions, but no native edge or Call Workflow invokes those actions here.

**Adaptation limits:** There is no explicit URL-encoding transformation, no-result branch, retry, or separate timeout pseudo-node. The graph maps configured response paths without proving their presence on every response. Sample booking details are not live travel records, and the lookup does not establish an identity-assurance policy. The host is redacted; the internal model is not a public import schema. Runtime testing is false, so no lookup or response serialization was exercised.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-lookup-appointment"></a>

## lookup_appointment.workflow

Observed 2026-09-09T00:00:38.393Z. [Sanitized model](../evidence/sample-flows/observed/native-lookup-appointment.json) · [graph JSON](sample-flows/summaries/native-lookup-appointment.json) · [all relationships](tenant-sample-relationships.md#native-lookup-appointment).

AI Agent Start 2 declares optional string inputs `date_of_birth` and `patient_name`. Its `onbegin` event, rendered `onBegin`, enters HTTP Request 3, which posts to the sanitized `/lookup_appointment` endpoint. The graph contains no additional branch for no appointment, multiple appointments, or a later cancellation; those are not recoverable from the filename or the two-node sequence.

**Exact handoffs:** The whole `$(n2.aiAgent.payload)` is the HTTP body. No name normalization, date conversion, or field-by-field request mapping is configured. The Last Execution Status outcome notifies for all status codes and stores transaction, flow, and service identifiers together with `httpStatus=$(n3.http.statusCode)` and `httpResponse=$(n3.http.responseBody)`. The backend body is preserved instead of being reduced to a selected appointment, making its result schema a separate integration dependency.

**Adaptation limits:** The HTTP node has no explicit outgoing edge to another operational node, no visible retry loop, and no filled timeout values. A matched record would not by itself establish verified customer identity, and this capture does not demonstrate a match at all. Sample personal fields are fixtures and are omitted here. Hosts and headers are redacted; the model is internal evidence, not a public import schema. No runtime test, customer communication, or cross-flow invocation occurred.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-lookup-flights"></a>

## lookup_flights.workflow

Observed 2026-09-09T00:02:08.072Z. [Sanitized model](../evidence/sample-flows/observed/native-lookup-flights.json) · [graph JSON](sample-flows/summaries/native-lookup-flights.json) · [all relationships](tenant-sample-relationships.md#native-lookup-flights).

AI Agent Start 2 declares optional strings `booking_id`, `last_name`, and `new_date`. Its internal `onbegin`, rendered `onBegin`, leads to HTTP 3 GET `/lookup_flights?booking_id=$(n2.aiAgent.booking_id)&last_name=$(n2.aiAgent.last_name)&new_date=$(n2.aiAgent.new_date)`. Both timeout fields contain 10000. End pseudo-nodes 7, 8, and 11 link back to HTTP 3: `oncomplete`/`onSuccess` exits with 2, while `onerror`/`onError` and `ontimeout`/`onTimeout` exit with 3.

**Exact handoffs:** HTTP extracts `$.available_flights` as `n3.available_flights` and `$.error` as `n3.error`. The Last Execution Status notification covers all status codes, uses payloadType 1, and stores transactionID, `available_flights=$(n3.available_flights)`, and `error=$(n3.error)`. It returns a candidate collection; there is no selection transformation, loop over flights, or mapping from a chosen flight to the reschedule action inside this graph.

**Adaptation limits:** No booking write or customer notification is configured. The model does not demonstrate date normalization, query-value encoding, an empty-list branch, or retry behavior. Returning candidates cannot establish that one remains available when a later action executes. Error/timeout terminals do not provide a distinct fallback list. Hosts are redacted and fixtures are not current availability. The internal model is not an importable public schema; `runtime_tested=false` means none of these paths was executed.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-register-transaction-dispute"></a>

## Register Transaction Dispute.workflow

Observed 2026-09-09T00:01:22.827Z. [Sanitized model](../evidence/sample-flows/observed/native-register-transaction-dispute.json) · [graph JSON](sample-flows/summaries/native-register-transaction-dispute.json) · [all relationships](tenant-sample-relationships.md#native-register-transaction-dispute).

AI Agent Start 2 declares optional strings `transaction_id`, `dispute_reason`, and `customer_id`. Its internal `onbegin`, rendered `onBegin`, enters HTTP Request 3 POST `/raise_dispute`. End pseudo-node 7 belongs to HTTP 3 and binds `oncomplete`, rendered `onSuccess`, with exitResult 2. No ordinary edge to that terminal is required in the observed internal representation.

**Exact handoffs:** The body translates `$(n2.aiAgent.customer_id)` to `user_id`, preserves `transaction_id=$(n2.aiAgent.transaction_id)`, and translates `$(n2.aiAgent.dispute_reason)` to `reason`. Connection/request timeout fields both contain 10000. HTTP response path `$.status` becomes `n3.dispute_status`. The Last Execution Status outcome notifies for all status codes with payloadType 2 and custompayload `transactionID=$(transid)` plus `status=$(n3.dispute_status)`. The graph expects a transaction identifier as input; it does not invoke Fetch Recent Transactions to select one.

**Adaptation limits:** No explicit HTTP error terminal/edge, retry loop, dispute-ID return, duplicate-dispute check, or customer notification appears. The extracted backend status is not inspected by a separate business-success branch. Historical sample responses do not prove a current dispute was registered. The backend host and headers are redacted. This internal model is evidence rather than a public import schema, and runtime testing is false: no financial action was performed.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-request-priority-shipping"></a>

## Request priority shipping.workflow

Observed 2026-09-09T00:01:26.431Z. [Sanitized model](../evidence/sample-flows/observed/native-request-priority-shipping.json) · [graph JSON](sample-flows/summaries/native-request-priority-shipping.json) · [all relationships](tenant-sample-relationships.md#native-request-priority-shipping).

AI Agent Start 2 advertises optional string `customer_id`, `order_id`, and `fee_in_dollars`, but its `onbegin`/rendered `onBegin` enters only HTTP Request 3 POST `/request_priority_shipping`. End pseudo-node 12 associates with HTTP 3 through parentNode and `nodeEvent=oncomplete`, rendered `onSuccess`, with exitResult 2. There is no fee-confirmation branch or separate order lookup.

**Exact handoffs:** The actual request body contains only `user_id=$(n2.aiAgent.customer_id)`. Neither `order_id` nor `fee_in_dollars` is sent or consumed elsewhere in the captured graph. HTTP timeout fields both contain 10000, and response path `$.status` is extracted as node output `status`. However, Last Execution Status uses payloadType 1 and its payload references unqualified `$(status)`, while a custom variable also named status starts empty. No captured session assignment connects `n3.status` to that variable, so the return binding deserves explicit verification rather than silent repair.

**Adaptation limits:** The template configures a priority-shipping request but does not demonstrate order targeting, fee charging, a populated return status, retry, or error-specific recovery. There is no Call Workflow or SMS/email node. Hosts and headers are redacted; sample response data is not proof of shipment changes. The internal model is not a public import schema, and `runtime_tested=false` leaves the suspected status-binding ambiguity untested.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-reschedule-flight"></a>

## reschedule_flight.workflow

Observed 2026-09-09T00:02:11.402Z. [Sanitized model](../evidence/sample-flows/observed/native-reschedule-flight.json) · [graph JSON](sample-flows/summaries/native-reschedule-flight.json) · [all relationships](tenant-sample-relationships.md#native-reschedule-flight).

AI Agent Start 2 declares optional string `booking_id`, `last_name`, and `new_flight_id`. Its `onbegin`/rendered `onBegin` enters HTTP Request 3 POST `/reschedule_flight`. End pseudo-node 13 binds HTTP `oncomplete`/`onSuccess` with exitResult 2; node 14 binds `onerror`/`onError` with exitResult 3. The sample calls one reschedule endpoint; it does not visibly create a new booking and then cancel an old one.

**Exact handoffs:** HTTP body preserves `booking_id=$(n2.aiAgent.booking_id)`, `last_name=$(n2.aiAgent.last_name)`, and `new_flight_id=$(n2.aiAgent.new_flight_id)`. Timeout values are 10000. Fields beneath `$.updated_booking` become outputs prefixed `updated_`: arrival_time, departure_time, flight_number, origin, destination, booking_id, and flight_id. Top-level message/error are extracted too. The all-status Last Execution Status payloadType 1 payload returns transactionID and these n3 outputs. Selection of new_flight_id must precede invocation elsewhere; no Lookup Flights call is configured here.

**Adaptation limits:** No explicit timeout pseudo-node, retry loop, rollback, price-difference calculation, or notification is present. A single HTTP endpoint does not establish atomicity or safe repetition of its backend operation. Embedded updated-booking data is a template fixture, not a rescheduled trip. Hosts and headers are redacted. This internal model is not an importable public schema; runtime testing is false, including response mapping and all mutation outcomes.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-sendsms"></a>

## sendSMS.workflow

Observed 2026-09-09T00:00:41.982Z. [Sanitized model](../evidence/sample-flows/observed/native-sendsms.json) · [graph JSON](sample-flows/summaries/native-sendsms.json) · [all relationships](tenant-sample-relationships.md#native-sendsms).

AI Agent Start 2 exposes optional string `msisdn` and `messageContent`. Its `onbegin`, rendered `onBegin`, connects directly to SMS 3. The node selects SMS delivery and an `msisdn` destination. There is no Receive, conversation loop, or HTTP operation, so this is an agent action for a single outbound message rather than a complete two-way SMS assistant.

**Exact handoffs:** SMS destination is `$(n2.aiAgent.msisdn)` and message is `$(n2.aiAgent.messageContent)`. The main `senderid` parameter is blank, while `resourceinfo` and `viewmodeData` retain a sender resource; those differing representations require tenant rebinding rather than copying the resource blindly. Last Execution Status is configured for all status codes with `payloadType=1`; its `payload` contains `serviceName=$(serviceName)` and literal `status=success`. A separate stored `custompayload` carries transaction metadata and statuscode 1000.

**Adaptation limits:** A literal success string is not delivery evidence. The captured model supplies no explicit delivery-event edge, receipt-processing node, failure-specific return object, or customer-reply handling; `successoutcome=1` alone is not enough to infer receipt behavior. An extra `CustomerIDType` appears only in conditionData, not the AI Agent parseOutput contract. This internal canvas model is not a public import schema. `runtime_tested=false`: no message was invoked, sent, received, or delivery-verified.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="native-verify-user"></a>

## Verify user.workflow

Observed 2026-09-09T00:01:29.840Z. [Sanitized model](../evidence/sample-flows/observed/native-verify-user.json) · [graph JSON](sample-flows/summaries/native-verify-user.json) · [all relationships](tenant-sample-relationships.md#native-verify-user).

AI Agent Start 2 accepts optional string `zipcode` and `date_of_birth`. Its `onbegin`/rendered `onBegin` enters HTTP 3, labeled Fetch user details, posting to `/verify_user`. End pseudo-nodes 34, 35, and 36 associate with node 3: `oncomplete`/`onSuccess` has exitResult 2, `onerror`/`onError` has 3, and `ontimeout`/`onTimeout` has 4. There is no verification-result Branch or conversational retry.

**Exact handoffs:** The request deliberately changes case and names: `DOB=$(n2.aiAgent.date_of_birth)` and `ZIP_code=$(n2.aiAgent.zipcode)`. Connection/request timeouts both contain 10000. JSONPath `$` becomes whole-response output `n3.user_details`, while `$.status` becomes `n3.status`. Last Execution Status covers all status codes and uses payloadType 1, storing transactionID, `user_details=$(n3.user_details)`, and `status=$(n3.status)`. A distinct custompayload stores transactionID and response only. HTTP on-leave log actions reference `$(n3.fullResp)` and `$(n3.status)`; fullResp is not a configured extraction output.

**Adaptation limits:** The title does not establish robust authentication or a validated identity policy. No direct call to later banking actions or explicit customer_id extraction is shown; any reuse of user_details belongs to external orchestration. Existing log configuration was only observed, never changed. Hosts and headers are redacted. This internal model is not a public import schema, and `runtime_tested=false` means backend verification, logging, and return serialization were not tested.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-amb-simplified-flow"></a>

## AMB Simplified Flow.workflow

Observed 2026-09-09T00:07:06.551Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-amb-simplified-flow.json) · [graph JSON](sample-flows/summaries/wxcc-amb-simplified-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-amb-simplified-flow).

Incoming Apple Start 2 feeds Evaluate 13, which builds details for Resolve Conversation 15. Created/reopened routes send status 5 then Queue Task 59. Queued sends acknowledgement 60, whose success calls PIQ and EWT 74. A successful estimate sends message 80 with both values; InsufficientData sends 76 with position only. PIQ errors/timeouts end Error. Queue failure closes task 23 and sends error 27. Resolve appended/accepted finish Success; its timeout branches on conversationOperation, closing created/reopened work and succeeding for appended. Unlike the Basic Inbound sample, this has no pre-queue Receive.

**Exact handoffs:** Evaluate 13 serializes messageDetails and pciDetails as `detailsJson`; Resolve consumes it with `$(transId)`. PIQ/EWT uses `$(queue)` and `$(taskId)` plus lookback minutes 5. Messages consume `$(n74.positionInQueue)` and, on Success, `$(n74.estimatedWaitTime)`. Queue itself contains a fixed sample queue ID, while PIQ references a custom queue variable.

**Adaptation limits:** Bind queue consistently across Queue Task and PIQ/EWT; the graph does not prove their values match. Estimate units are not established by the message text and there is no periodic refresh loop. Send 76 has no captured terminal bindings and declares an unrouted error; repeated End records under Send 80 cannot be reassigned to it. Its older details shape includes isAppleMessage and PCI data but not the newer Basic sample’s malware/security sections.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-basic-inbound-flow"></a>

## Apple Basic Inbound Flow.workflow

Observed 2026-09-09T00:07:13.174Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-basic-inbound-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-basic-inbound-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-basic-inbound-flow).

Start 2 copies the incoming Apple event into custom variables; Evaluate 13 builds message and scan details; Resolve Conversation 15 creates, reopens, or appends the conversation. Created/reopened routes greet the customer through Send 5 and wait at Receive 189 for up to 600 seconds. A reply reaches attachment transformation 192, then Append Conversation 191, then Queue Task 59. Receive/send/attachment/append failures also continue to queueing through their captured fallback edges. Queued sends acknowledgement 60; queue failure closes the task through 23 before error message 27. Appended/accepted terminate Success without repeating the greeting. Resolve timeout branches on conversationOperation: created/reopened closes the task, appended succeeds, and unknown/error terminates Error.

**Exact handoffs:** `$(n2.abc.abcUserId)` addresses sends; Start copies `n2.abc.message` to `resolveConversationmessagetext`. Evaluate 13 produces `detailsJson` for Resolve. Receive copies `$(n189.abc.attachments)` and security scan failure details; Evaluate 192 builds `parseDataAttachment`, consumed by Append 191 alongside `$(n189.receive.message)`. Queue/Close consume `$(taskId)` and `$(conversationId)`.

**Adaptation limits:** This waits once before queueing; no captured conversational loop or AI node exists. Start contains the whitespace-bearing reference `$(n2. abc.attachmentCount)`. The attachment script marks dropped files and clears their URLs; it does not itself perform a security scan. Sample identities, queue selection, and error-send handling need adaptation; Send 22 has an unrouted declared error.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-form-response-flow"></a>

## Apple Form Response Flow.workflow

Observed 2026-09-09T00:06:00.411Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-form-response-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-form-response-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-form-response-flow).

This is a separate event handler for Interactive Message: Form Response, not the form-presentation flow. Start 2 searches conversation 226. Only conversationActive reaches Append Conversation 242, which records the incoming form response; its append-success binding ends Success. Search results noConversationFound, closed, in-queue and on-hold end Error, as do search failures/timeouts. Append failure or timeout sends error message 22 to the originating Apple user; that message’s success binding selects Success, even though the append operation failed. There is no Resolve, queue, Receive or customer-response loop in this graph.

**Exact handoffs:** Search uses `$(n2.abc.abcUserId)` as customeraddress and the sample business address. Append 242 uses `$(n226.conversationId)` as its conversation path, `$(n2.abc.interactivePayload)` as ambFormResponse, `$(n2.abc.timestamp)` as timestamp, and `$(n2.abc.capabilityList)` as extras. The message type is `amb-form-response` with inbound direction.

**Adaptation limits:** Request fields and stored nodeInput show different business-address values; neither is a target-tenant default. End entries naming parent node 27 remain in the model although that operative node is absent; these cannot be assigned to Send 22 by guess. Send 22 declares an error with no captured matching route. A Success outcome here can mean error notification succeeded, not form ingestion succeeded.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-imessage-app-flow"></a>

## Apple iMessage App Flow.workflow

Observed 2026-09-09T00:06:09.966Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-imessage-app-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-imessage-app-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-imessage-app-flow).

The iMessage App Response event at Start 2 invokes Search Conversation 226. Active or in-queue results append through 242; no conversation, closed or on-hold results send restart notice 382 asking for a plain-text message. Search failures and timeout terminate Error. Append success terminates Success, while its failure/timeout routes to error Send 22. Restart notice 382 has Success and Error terminal bindings, with duplicate records preserved. There is no task creation, queue operation, iMessage application launch, Receive wait or conversational loop.

**Exact handoffs:** Search customeraddress is `$(n2.abc.abcUserId)`. Append 242 uses `$(n226.conversationId)` and maps `$(n2.abc.url)` into text with message type `text-with-attachments`, inbound direction, `$(n2.abc.timestamp)` and capabilityList. Both messages address the incoming Apple user.

**Adaptation limits:** The sample app response is represented by its URL text; the graph does not parse an app-specific result schema or attach a file merely because the message type says text-with-attachments. Search request_body and stored nodeInput business addresses disagree. Send 22 lacks captured terminal handling for its declared error; its success is also not represented by a binding in this capture. Duplicate restart-notice End items do not imply multiple sends. Reconcile active bindings before adaptation.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-inbound-flow-with-form"></a>

## Apple Inbound Flow with Form.workflow

Observed 2026-09-09T00:07:37.231Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-inbound-flow-with-form.json) · [graph JSON](sample-flows/summaries/wxcc-apple-inbound-flow-with-form.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-inbound-flow-with-form).

Start 2 goes to capability Evaluate 247. FORM-capable devices reach Search Conversation 241: new/closed conversations receive form 239 and wait 300 seconds at Receive 263; active/queued/on-hold conversations go directly to preparation 13. Unsupported or failed capability checks also go to 13. Evaluate 13 parses form selections, builds details, then calls Resolve 15. Created/reopened outcomes reach Branch 260: if a form was presented, Append 245 records its response before message 5; otherwise message 5 is immediate. Set Variable 190 then attempts to expose customerEmail on the task, and all its captured outcomes proceed to Queue 59. Queued sends acknowledgement 60; queue failure closes task 23 and sends error 27. Appended/accepted Resolve outcomes end Success.

**Exact handoffs:** Receive writes `formResponse = $(n263.abc.selections)`. Evaluate 13 reads pageIdentifier values `name`, `emailAddress`, and `defectiveProduct`; it assigns customerName/customerEmail/defectiveProduct. Send 239 sets `formsSupported` true on entry; Branch 260 tests it. Append 245 consumes `$(n263.receive.payload)`. Set Variable publishes `$(customerEmail)` as String, agent-viewable/editable, nonglobal and nonreportable.

**Adaptation limits:** The stored send type is spelled `form_mesage`; this is internal model evidence, not an import instruction. A Set Variable failure still queues the task, so queueing does not prove customerEmail reached the desktop. Form timeout/error sends error 22. There is no response-validation/retry loop; selected form definitions, default values, and identifiers need tenant-specific binding.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-inbound-flow-with-intentid-groupid-based-routing"></a>

## Apple Inbound Flow with IntentId GroupId based Routing.workflow

Observed 2026-09-09T00:05:17.004Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-inbound-flow-with-intentid-groupid-based-routing.json) · [graph JSON](sample-flows/summaries/wxcc-apple-inbound-flow-with-intentid-groupid-based-routing.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-inbound-flow-with-intentid-groupid-based-routing).

Incoming Apple Start 2 feeds payload preparation 13 and Resolve Conversation 15. Only created/reopened outcomes reach routing Branch 191. The accounts condition requires intentId=support AND groupId=account; it sends notice 193 then Queue Task 192. The sales condition requires intentId=courses AND groupId=sales; notice 194 precedes Queue Task 196. Unmatched/branch-error paths use default Queue Task 59. Each notice continues to its queue on success, policy failure or error. Every Queued outcome sends acknowledgement 60; queue failures converge on Close Task 23 then error message 27. Resolve appended/accepted terminate Success. Its timeout branch 172 closes created/reopened work, succeeds for appended, and errors for other states.

**Exact handoffs:** Start writes `intentId = $(n2.abc.intentId)` and `groupId = $(n2.abc.groupId)`; these are Apple event fields used directly by Branch 191. It also writes `abcUserId`; notices 193/194 consume `$(abcUserId)`. Evaluate 13 serializes `detailsJson` for Resolve; queue nodes consume `$(taskId)` and `$(conversationId)`.

**Adaptation limits:** The word intent here is an Apple event routing identifier; this graph contains no Studio intent classifier or AI invocation. Queue choices are sample bindings, not a universal accounts/sales mapping. There is no Receive, loop, or business-system lookup. Resolve errors use customer error Send 22, whose declared send-error destination is not captured.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-list-picker-flow"></a>

## Apple List Picker Flow.workflow

Observed 2026-09-09T00:05:25.341Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-list-picker-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-list-picker-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-list-picker-flow).

Start 2 and Evaluate 13 reach Resolve Conversation 15. Created/reopened outcomes send country list picker 193, then Receive 206 waits 300 seconds. A list-picker response appends the outbound picker through 197, then inbound response through 198, and sends status message 5. Branch 199 examines the received choices: USA routes Queue 201, India Queue 203, UK Queue 200; unmatched/error routes default Queue 59. Picker/send/receive/append fallback paths also reach this branch. Queued sends acknowledgement 60; queue failures close task 23 then send error 27. Appended/accepted Resolve outcomes terminate Success, while Resolve timeout uses operation-sensitive Branch 172.

**Exact handoffs:** Picker 193 offers India, USA and UK with requestIdentifier `system`. Append 197 consumes `$(n193.send.listPicker)` and `$(n193.send.sentDateTime)`. Append 198 request fields consume `$(n206.receive.payload)` and `$(n206.abc.timestamp)`; Branch 199 tests `$(n206.abc.listPickerItems)` using contains. All queue nodes use the shared task/conversation identifiers.

**Adaptation limits:** Stored nodeInput in Append 198 still references uncaptured n194, while its request_body references n206. Queue request fields select the same queue ID across country-specific nodes, while stored UI queue selections differ; distinct branches do not establish distinct operational queues. Rebind through the supported UI and verify the active contract. A response timeout can reach the branch without a valid selected country; no selection retry loop is captured.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-time-picker-and-list-picker-response-flow"></a>

## Apple Time Picker and List Picker Response Flow.workflow

Observed 2026-09-09T00:06:05.466Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-time-picker-and-list-picker-response-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-time-picker-and-list-picker-response-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-time-picker-and-list-picker-response-flow).

Start 2 handles the Apple List Picker or Time Picker interactive-response event and searches conversation 226. Only an active conversation reaches Evaluate 336, which classifies messageType by substring. Result 1 selects list-response Append 242; result 2 selects time-response Append 348; unsupported type/result 3 and Evaluate failures terminate Error. Search no-conversation, closed, queued, on-hold and failure states also terminate Error. Either append’s failure/timeout routes to customer error Send 22. The model records successful append terminal bindings under node 348; the detailed graph preserves their actual parent references instead of assuming symmetric wiring.

**Exact handoffs:** Start writes `messageType = $(n2.abc.type)`. Evaluate checks `list_picker_response` and `time_picker_response`. Both append nodes use `$(n226.conversationId)`, `$(n2.abc.interactivePayload)`, `$(n2.abc.timestamp)` and capabilityList, while selecting `amb-list-picker-response` or `amb-time-picker-response` respectively.

**Adaptation limits:** Two success End records name parent 348; no corresponding parent-242 success binding is present. Additional error End records name absent parent 27, and Send 22 has an unrouted error declaration. Preserve these observed inconsistencies rather than inventing a successful list branch. Search request_body and stored UI business addresses differ. This records an existing interaction; it sends no picker and has no queue/Receive loop.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-time-picker-flow"></a>

## Apple Time Picker Flow.workflow

Observed 2026-09-09T00:05:32.254Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-time-picker-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-time-picker-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-time-picker-flow).

Start 2 prepares details at Evaluate 13 and invokes Resolve Conversation 15. Created/reopened routes send time picker 193 and wait up to 300 seconds at Receive 206. Its interactive time-picker event appends the outbound picker through 197, then the inbound response through 198, then status message 5 and Queue Task 59. Picker, Receive and append failures converge on the same status/queue path. Queued sends acknowledgement 60; queue failure closes task 23 then sends error 27. Existing appended/accepted Resolve outcomes finish Success without presenting the picker. Resolve timeout uses Branch 172 to distinguish created/reopened cleanup from appended completion.

**Exact handoffs:** Append 197 records `$(n193.send.timePicker)` and `$(n193.send.sentDateTime)` as `amb-time-picker`. Append 198 records `$(n206.receive.payload)` and `$(n206.abc.timestamp)` as `amb-time-picker-response`, plus capability metadata. Sends address `$(n2.abc.abcUserId)`; append/queue nodes consume shared `conversationId`/`taskId`.

**Adaptation limits:** Picker slots are fixed to 2024-04-01 at 09:00 and 10:00, with duration 1800 and timezoneOffset `Asia/Calcutta`; they are historical examples, not available appointments. The graph records a selection then queues work: no booking API, availability lookup, selected-slot branch or retry loop exists. Queueing can occur after a picker timeout. Several repeated End bindings and Send 22’s unrouted error are retained as captured.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-apple-unsubscribe-flow"></a>

## Apple Unsubscribe Flow.workflow

Observed 2026-09-09T00:07:41.477Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-apple-unsubscribe-flow.json) · [graph JSON](sample-flows/summaries/wxcc-apple-unsubscribe-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-apple-unsubscribe-flow).

Apple Conversation closed triggers Start 2 and Search Conversation 3. Search results conversationClosed, conversationOnHold, conversationInQueue and conversationActive all route to Close Task 4. Close Task Success terminates Success; its Error, authorization, invalid-data/choice, general-error and timeout events terminate Error. Search noConversationFound terminates Success without a close attempt, while search failures/timeouts end Error. This is an event-to-cleanup flow with no outgoing customer message, Receive or loop.

**Exact handoffs:** Search identifies the conversation using the incoming Apple identity. Its output `$(n3.aliasId)` becomes both Close Task’s Task Id request value and ID path parameter. `$(n3.conversationId)` becomes Conversation ID, with Media Type social. These are separate identifiers; the alias/task ID is not replaced by the conversation ID.

**Adaptation limits:** The sample name Unsubscribe describes Apple conversation-close handling. The graph does not show an SMS opt-out list, consent database, subscription API or cross-channel contact-policy update. It also deliberately attempts Close Task for the conversationClosed search result; do not silently remove that path from the observed design. No retries are present, and imported authorization/tenant bindings are examples. Terminal configuration is not proof a real task was closed.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-emailattachmentdropnotification"></a>

## EmailAttachmentDropNotification.workflow

Observed 2026-09-09T00:02:36.379Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-emailattachmentdropnotification.json) · [graph JSON](sample-flows/summaries/wxcc-emailattachmentdropnotification.json) · [all relationships](tenant-sample-relationships.md#wxcc-emailattachmentdropnotification).

Email Start 2 enters Parse Variables 9. Its attachmentsDropped result sends notification Email 1980 before Resolve Conversation 1894; noAttachmentsDropped goes directly to Resolve. All three notification outcomes—onsuccess, onerror, and onpolicyfail—continue to Resolve. Created/reopened conversations send acknowledgment 1898, then Queue Task 1851; Queued sends Email 39. Resolve appended/accepted outcomes terminate rather than enqueue the same conversation again. Queue failures enter Close Task 1854 and then error Email 322; Resolve timeout Branch 1910 closes only its Create/Reopen Path.

**Exact handoffs:** Start preserves `$(n2.email.emailId)`, `$(n2.email.inReplyTo)`, subject, message variants, attachments, and scan metadata. Evaluate builds detailsJson for Resolve and collects attachment names from security failure data. It selects attachmentsDropped when the reason contains PCI: Failed:, Malware: Failed:, or System Alert; the notification body is `$(droppedAttachmentNotificationMessage)`. Resolve supplies taskId/conversationOperation; Queue and Close consume `$(taskId)` and the stored `$(conversationId)`. Outbound email destinations are `$(n2.email.emailId)` with `$(subject)`.

**Adaptation limits:** The model constructs notices from scan results; it does not itself scan attachments. Notification failure does not block routing. Emails use createnew, so carrying inReplyTo inside Resolve details does not prove outbound threading. No conversation wait/retry loop exists. Some End records overlap explicit acknowledgment routes or reference absent parent 1878; they are retained as model residue, not silently resolved. The conversationId is a placeholder, and resource bindings need adaptation. Nothing was sent or executed; this internal model is not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-emailinboundflow"></a>

## EmailInboundFlow.workflow

Observed 2026-09-09T00:04:52.983Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-emailinboundflow.json) · [graph JSON](sample-flows/summaries/wxcc-emailinboundflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-emailinboundflow).

Email Start 2 copies inbound context and enters Parse Variables 9. Numeric outcome 1/success connects to Resolve Conversation 1894. Created/reopened outcomes send Email 1898, then Queue Task 1851 on send success, error, or policy failure. Queue event Queued sends acknowledgment Email 39. Resolve appended and accepted outcomes terminate via End associations; they do not repeat queuing. Queue errors/timeouts attempt Close Task 1854, whose outcomes send error Email 322. Resolve timeout Branch 1910 distinguishes create/reopen cleanup from an append path that terminates.

**Exact handoffs:** The event provides `$(n2.email.emailId)`, `$(n2.email.inReplyTo)`, recipients, subject, body variants, attachments, and scan metadata. Evaluate normalizes attachment names/URLs and dropped flags, supplies defaults for missing sender/subject, and assembles detailsJson containing messageDetails plus PCI, malware, and security results. Resolve consumes `$(transId)` and `$(detailsJson)` and exposes taskId/conversationOperation. Queue/Close use `$(taskId)` and `$(conversationId)`. Customer emails use destination `$(n2.email.emailId)`, subject `$(subject)`, and createnew.

**Adaptation limits:** This processes one inbound email event; no Receive loop or AI Agent node appears. A resolved acknowledgment precedes queuing and does not prove a business issue was resolved. The retained conversationId is a placeholder, while selected queue/flow values are sample bindings. Some End records overlap explicit acknowledgment routes or name absent parent 1878. Outbound threading and attachment edge cases remain untested. No message or task operation was invoked; the internal model is not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-emailinboundsampleflowwithcontactpriority"></a>

## EmailInboundSampleFlowWithContactPriority.workflow

Observed 2026-09-09T00:03:49.819Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-emailinboundsampleflowwithcontactpriority.json) · [graph JSON](sample-flows/summaries/wxcc-emailinboundsampleflowwithcontactpriority.json) · [all relationships](tenant-sample-relationships.md#wxcc-emailinboundsampleflowwithcontactpriority).

Email Start 2 → Parse Variables 9 → Resolve Conversation 1894 establishes the inbound email/task context. Created/reopened outcomes send acknowledgment Email 1898 and continue to Determine Contact Priority 1980 whether sending succeeds, errors, or fails policy. The Evaluate result and both error outcomes all continue to Queue Task 1851. Queued sends Email 39. Queue failure closes task 1854 and sends error Email 322; Resolve appended/accepted outcomes terminate. Resolve timeout enters Branch 1910, whose Create/Reopen Path attempts Close Task.

**Exact handoffs:** Inbound sender, thread references, text/HTML, attachments, and scan metadata become detailsJson for Resolve using `$(transId)`. Priority Evaluate initializes contactPriority to string 10, sets 1 when customerEmailId equals priorityOneCustomer, and 5 when it equals priorityFiveCustomer. Queue request_body maps contactPriority to `$(contactPriority)`, alongside `$(taskId)`, `$(conversationId)`, and email media type. Queue nodeInput separately retains a blank contactPriority. All outbound emails address `$(n2.email.emailId)` and retain `$(subject)`.

**Adaptation limits:** The priority list is two stored example addresses, not customer classification logic or an entitlement policy. The blank-versus-dynamic priority representations require verification when adapting. Queuing continues even if priority evaluation fails, so a valid assigned priority is not established on every path. End residue overlaps acknowledgment edges and includes absent parent 1878. Resolve nodeInput contains an explicit flow-ID placeholder; conversationId is also a placeholder. No flow, queue action, or email was executed. This internal capture is evidence, not an importable public schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-facebookattachmentdropnotification"></a>

## FacebookAttachmentDropNotification.workflow

Observed 2026-09-09T00:06:28.189Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-facebookattachmentdropnotification.json) · [graph JSON](sample-flows/summaries/wxcc-facebookattachmentdropnotification.json) · [all relationships](tenant-sample-relationships.md#wxcc-facebookattachmentdropnotification).

Messenger Start 2 copies message, identity, attachment and scan fields into custom variables before Evaluate 9 constructs `detailsJson` and chooses an attachment-notification result. `attachmentsDropped` sends Messenger 1969; all its captured outcomes continue to Resolve Conversation 1897. `noAttachmentsDropped` enters 1897 directly. Created/reopened conversations send acknowledgment 1899, then Queue Task 1701 regardless of acknowledgment delivery outcome; `Queued` sends confirmation 1912. Appended and accepted events terminate Success. Resolve timeout branches at 1939: created/reopened attempts Close Task 1703, appended terminates Success, and other/error results terminate Error. Queue failures also close the task; every captured close outcome sends error notice 1651. Other parse/resolve errors use notice 1662.

**Exact handoffs:** Start supplies `$(n2.messenger.psId)` to each send. Evaluate 9 reads scan-reason custom variables, selecting sensitive-content, malware or processing-error text into `droppedAttachmentNotificationMessage`, then passes `$(detailsJson)` to 1897. Queue/close use `$(taskId)` and `$(conversationId)`; Resolve declares `taskId` and `conversationOperation` outputs, while the timeout branch consumes the unqualified operation variable. These custom bindings must be reconciled with the actual integration callback contract.

**Adaptation limits:** No Receive node or retry loop is captured. Evaluate uses `appId` while the captured Start assignment/default is `appid`, and Start assigns timestamp from `$(n2.messenger.ts)` although its output list names `messenger.timestamp`; preserve these discrepancies for adaptation. Some terminal bindings name uncaptured producers 1980/1825, and notice-node error routes are absent. Placeholder identities and conversation defaults are not deployable bindings. Runtime remains untested.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-facebookclosewithwxmflow"></a>

## FacebookCloseWithWxmFlow.workflow

Observed 2026-09-09T00:06:34.924Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-facebookclosewithwxmflow.json) · [graph JSON](sample-flows/summaries/wxcc-facebookclosewithwxmflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-facebookclosewithwxmflow).

Task Closed Start 2 enters Branch 1406. Only a request-body match for string-valued `overrideDefaultClose` true together with `mediaChannel` facebook continues; the unmatched branch ends Success. Evaluate 57 parses the task variables and request body, then WXM 1487 creates a survey link. Success sends Messenger 896; successful delivery appends the outbound survey at 902. Survey-generation failure, send failure and every captured append outcome converge on Close Conversation 629. Successful closure, or failure code 4547 recognized by Branch 114, reaches Close Task 653. Its Success enters owner Branch 246: an owner triggers Screen Pop 720, otherwise the flow ends Success. Other close failures use Close Task 671 with failure context.

**Exact handoffs:** Start stores `$(n2.webex.variables)` as `response` and `$(n2.webex.RequestBody)` as `requestBody`; Evaluate persists parsed `mediaResourceId` and customer/agent fields on leave. Both Messenger 896 and Append 902 consume `$(n1487.surveyURL)`; the send targets `$(n2.webex.origin)`, and append/close use `$(mediaResourceId)`. Task closure and Screen Pop consume `$(n2.webex.taskId)` and owner; the screen pop includes parsed `$(CustomerId)`.

**Adaptation limits:** There is no survey-response wait or retry loop. WXM questionnaire/prefill IDs and the generic screen-pop URL are sample configuration. The override check is a regex over serialized input, not a typed Boolean field test. Evaluate errors and several Close Task events lack captured routes; detached terminal bindings reference uncaptured 683/305. Screen-pop success/error terminals exist, but no operation was executed.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-facebookinboundflow"></a>

## FacebookInboundFlow.workflow

Observed 2026-09-09T00:07:46.595Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-facebookinboundflow.json) · [graph JSON](sample-flows/summaries/wxcc-facebookinboundflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-facebookinboundflow).

Messenger Incoming Message 2 enters Evaluate 9, then Resolve Conversation 1897. Evaluate assembles incoming message, attachment and scan details. Resolve `created` or `reopened` sends acknowledgment 1899, whose success, policy-failure and error edges all continue to Queue Task 1701. `Queued` sends notification 1912. Resolve `appended` ends successfully; `accepted` has a Success terminal with asynchronous checking. Resolve timeout enters Branch 1939: a created/reopened operation closes Task 1703, appended ends successfully, and unmatched/error ends with Error. Queue failures also close Task 1703; its configured outcomes converge on error notification 1651. Evaluate/other Resolve failures use notification 1662.

**Exact handoffs:** Start on-leave assignments copy `$(n2.messenger.message)`, attachments, sender `psId` and scan metadata into custom variables. Evaluate builds `detailsJson`, consumed by Resolve's Details JSON; Resolve declares `transId`, `taskId` and `conversationOperation` outputs. Queue and Close use unqualified `$(taskId)` and `$(conversationId)`. Every Messenger send targets `$(n2.messenger.psId)`. This is an incoming-message routing transaction; no Receive node, conversation loop or AI Agent node appears.

**Adaptation limits:** The capture retains both terminal bindings and outgoing edges for acknowledgment 1899, plus terminal metadata with absent producer nodes; execution precedence is unverified. Start assigns timestamp from `n2.messenger.ts` although its output list names `messenger.timestamp`; Evaluate uses `appId` while Start assigns `appid`. Preserve those differences when adapting. Selected resources and stored fixtures are not defaults. Internal canvas evidence is not an import schema; runtime testing is false.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-facebooktaskbotinboundflow"></a>

## FacebookTaskBotInboundFlow.workflow

Observed 2026-09-09T00:03:05.707Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-facebooktaskbotinboundflow.json) · [graph JSON](sample-flows/summaries/wxcc-facebooktaskbotinboundflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-facebooktaskbotinboundflow).

Messenger Start 2 → Evaluate 9 → Resolve Conversation 1740 sends created/reopened to HTTP lookup 1574. Branch 1575 sends empty body or HTTP 400/404/429 directly to Task bot 1777; other responses pass through account parser 1576. Bot onSuccess enters Branch 1585: TemplateKey linkAcc parses Entities at 1586 and Datastore at 1590, posts account data at 1584, then sends reply 1404. Other template keys send directly. Outbound Append 1273 checks Goodbye Intent at Branch 1794; otherwise Receive 756 waits 120 seconds. fbm.mo → normalization 1413 → inbound Append 1332 → bot is the turn loop. onAgentHandover sends/appends the reply then Queue Task 1388.

**Exact handoffs:** Bot consumer.facebook_id and Send destination use `$(n2.messenger.psId)`; msg uses `$(questionForBot)` and correlation uses `$(transid)`. Receive filters that original sender. Account lookup uses a literal ID, not the inbound psId. Parser 1576 reads the first record Account number/Balance into session accNum/balance. The linkAcc path extracts `$.accNum.value` from `$(n1777.Entities)` and `$.bal` from `$(n1777.Datastore)`; POST writes these with the inbound psId/name. Receive refreshes message/attachments; normalization prepares `messageFromCustomer` and `parseDataAttachment` for Append.

**Adaptation limits:** This is a legacy Task Bot demonstration with a sample account store, not a current AI Agent or verified banking workflow. Goodbye/Receive timeout sends closure notice 1426 then Close Task 1796; many failures use separate close/error paths. Resolve appended/accepted ends through parent/event bindings. The literal lookup ID and stale log reference to absent n1405 remain explicit. No retry/idempotency guard surrounds the account POST. No runtime actions occurred; headers/hosts are sanitized, resource IDs need adaptation, and this internal model is not a public import schema.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-live-chat-close-flow"></a>

## Live Chat Close Flow.workflow

Observed 2026-09-09T00:08:02.557Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-live-chat-close-flow.json) · [graph JSON](sample-flows/summaries/wxcc-live-chat-close-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-live-chat-close-flow).

The Mobile & Web App `On Thread Closed` event starts node 2 and Search Conversation 108. Its `conversationActive` route appends the closure reason as an announcement at 208, ending Success on append success. The closed, in-queue and on-hold routes instead invoke Close Task 124. No conversation found terminates Success. Search, append and close errors/timeouts have explicit Error terminal bindings; Close Task Success terminates Success. The active route does not continue from Append 208 into Close Task 124 in the captured graph.

**Exact handoffs:** Search 108 identifies the conversation from `$(n2.inappmessaging.userId)`, `$(n2.inappmessaging.appId)` and `$(n2.inappmessaging.threadId)`; the user ID is also the browser fingerprint. It extracts `aliasId` from `$.value.aliasId` and `conversationId` from `$.value.conversationId`. Close Task 124 uses `$(n108.aliasId)` as Task Id and `$(n108.conversationId)` as Conversation ID with media type `chat`. Append 208 uses the same conversation ID, `$(n2.inappmessaging.reasonForThreadClosure)` as announcement text, and `$(n2.inappmessaging.ts)` as timestamp.

**Adaptation limits:** This is a channel thread-close handler, distinct from a WxCC Task Closed survey flow. It neither sends a customer message nor waits for another turn, and contains no control loop. Preserve the distinct active-versus-queued closure behavior when adapting; tenant bindings, closure semantics and successful execution were not tested.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechat-inbound-flow-with-proactive-chat-changes"></a>

## Livechat Inbound flow with proactive chat changes.workflow

Observed 2026-09-09T00:08:09.451Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechat-inbound-flow-with-proactive-chat-changes.json) · [graph JSON](sample-flows/summaries/wxcc-livechat-inbound-flow-with-proactive-chat-changes.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechat-inbound-flow-with-proactive-chat-changes).

APP Start 2 searches Conversation 2433. No conversation or a closed conversation sends pre-chat form 2436, then Receive 2438 waits 300 seconds for `app.onformresponse`; active, queued or held conversations go directly to Evaluate 2465. Evaluate feeds Resolve Conversation 2588. Created/reopened conversations append the form response through 2424, then Branch 2620 selects Queue 2621 for proactive chat or Queue 2259 otherwise; branch error also selects 2259. Both `Queued` events send acknowledgment 1727. Resolve appended/accepted events end successfully, accepted with asynchronous checking. Resolve timeout reaches Branch 2517: create/reopen closes Task 2261, append succeeds, other/error fails. Append/queue failures also close Task 2261 and send error 2227; earlier failures use 2234.

**Exact handoffs:** Start copies `$(n2.inappmessaging.message.extras)` into `messageExtras`. Evaluate parses it, compares `proactive_id !== 0`, sets `isProactiveChat`, and extracts `proactive_queue_id` as `proactiveQueueId`; Queue 2621 consumes that dynamic queue ID. Receive assigns customerName/customerEmail from formFields.Name/Email; Append consumes `$(n2438.inappmessaging.formResponse)`. Evaluate includes proactiveRuleId in `detailsJson` for Resolve. Queue/Close use taskId/conversationId; notifications retain the original userId and threadId.

**Adaptation limits:** The script expects parseable extras with suitable proactive fields; missing or malformed values are not demonstrated. Queue 2259 retains different fixed queue IDs in nodeInput and request_body. Close Task selects media type social although Resolve/Queue select chat. No retry loop or AI Agent node appears, and several notification errors lack captured routes. Resource/template bindings require adaptation. This internal canvas is configuration evidence, not a public schema or successful execution; runtime testing is false.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechatclosewithwxmflow"></a>

## LiveChatCloseWithWxmFlow.workflow

Observed 2026-09-09T00:06:41.662Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechatclosewithwxmflow.json) · [graph JSON](sample-flows/summaries/wxcc-livechatclosewithwxmflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechatclosewithwxmflow).

Task Closed Start 2 enters Branch 1406, which requires the serialized override-default-close string and media channel `web`; no match ends Success. Evaluate 57 parses task variables and customer data, then WXM 1510 creates a survey link. Success sends Live Chat 993, whose successful send appends the survey message at 1511. Survey-generation failures, send failures and all captured append results proceed to Close Conversation 629. Closure success leads to Close Task 653; close failure first checks code 4547 at Branch 114 and otherwise uses failure-context Close Task 671. Successful task closure checks owner at Branch 246, invoking Screen Pop 720 when present or terminating Success without an owner.

**Exact handoffs:** Evaluate reads the arrays saved from `$(n2.webex.variables)` and `$(n2.webex.RequestBody)`, extracts variable names `threadID` and `userID` into `thread` and `user`, and persists `mediaResourceId` plus customer fields. Sender 993 uses `$(user)`, `$(thread)` and `$(n1510.surveyURL)`. Append 1511 targets `$(mediaResourceId)` but its text references `$(n1477.surveyURL)`: no node 1477 is captured. This differs from the correctly linked send and must be repaired when adapting.

**Adaptation limits:** The regex gate expects a string representation of true. Survey/questionnaire and screen-pop settings require replacement. No survey-response wait or retry loop exists. Several Evaluate/Close Task failure routes are absent, while detached terminal bindings refer to uncaptured 683/305. Screen Pop has Success/Error terminals; configuration visibility does not prove survey delivery, conversation closure or runtime variable scope.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechatinbound-flow"></a>

## LivechatInbound flow.workflow

Observed 2026-09-09T00:08:15.873Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechatinbound-flow.json) · [graph JSON](sample-flows/summaries/wxcc-livechatinbound-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechatinbound-flow).

APP Start 2 enters Search Conversation 2433. `noConversationFound` and `conversationClosed` send pre-chat form 2436; Receive 2438 waits 300 seconds for `app.onformresponse`, then Evaluate 2465 prepares Resolve Conversation 2588. Active/in-queue/on-hold search results skip the form and enter Evaluate directly. Resolve created/reopened results append the received form through 2424, whose `onAppendMessageSuccess` queues Task 2259. `Queued` sends notification 1727. Resolve appended and accepted end successfully, accepted with asynchronous checking. Resolve timeout reaches Branch 2517: created/reopened closes Task 2261, appended succeeds, unmatched/error fails. Append/queue failures also close Task 2261 and send notification 2227; search/form/receive/Evaluate/other Resolve failures use 2234.

**Exact handoffs:** Search and every chat send retain `$(n2.inappmessaging.userId)` and threadId. Receive's on-leave actions assign customerName and customerEmail from `n2438.inappmessaging.formFields.Name` and `.Email`; Append uses its formResponse and timestamp. Evaluate defaults missing name/email to userId and constructs `detailsJson` with message, identity, attachment and scan details. Resolve consumes that object; Queue and Close consume unqualified taskId/conversationId. Branch 2517 checks unqualified `$(conversationOperation)`.

**Adaptation limits:** Form/template, business address and fixed queue values are sample bindings. Close Task's media type is social, while Resolve and Queue use chat; retain this mismatch for adaptation. Some final notification failures have no captured route. There is no Receive retry, proactive-queue branch or AI Agent node. Internal canvas evidence is not a public import schema, and runtime testing is false.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechatinboundflowwithoutform"></a>

## LivechatInboundFlowWithoutForm.workflow

Observed 2026-09-09T00:08:44.986Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechatinboundflowwithoutform.json) · [graph JSON](sample-flows/summaries/wxcc-livechatinboundflowwithoutform.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechatinboundflowwithoutform).

APP Start 2 enters Evaluate 2465 and Resolve Conversation 2307 directly: there is no Search Conversation, form send, Receive wait or form-append operation. Resolve created/reopened events queue Task 2259, and `Queued` sends acknowledgment 1727. Resolve appended ends with Success; accepted also ends with Success and asynchronous checking. A Resolve timeout enters Branch 2481, whose created/reopened path closes Task 2261, appended path succeeds and unmatched/error paths fail. Queue timeout and other configured failures also close Task 2261; its outcomes all send error notification 2227. Evaluate errors and the other Resolve failure events instead send notification 2234.

**Exact handoffs:** Start supplies the in-app message, user/thread identities, attachments and scan values. Evaluate substitutes userId when customerName/customerEmail are empty, assembles message/PCI/malware/security details, and serializes `detailsJson` for Resolve. Branch 2481 explicitly tests `$(n2307.conversationOperation)`. Queue/Close take `$(taskId)` and `$(conversationId)`; all chat sends target `$(n2.inappmessaging.userId)` on `$(n2.inappmessaging.threadId)`. No autonomous customer-answering or business-action node is present.

**Adaptation limits:** The flow has no explicit cycle or retry. Close Task specifies media type social while Resolve/Queue specify chat. Extra terminal metadata references absent producer nodes, and final message failures lack captured recovery routes. Fixed queue and integration bindings need tenant-specific replacement; no resource availability is established. This internal model records configuration rather than a public import schema, and runtime testing is false.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechatinboundsampleflowwithsetvariable"></a>

## LiveChatInboundSampleFlowWithSetVariable.workflow

Observed 2026-09-09T00:04:00.804Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechatinboundsampleflowwithsetvariable.json) · [graph JSON](sample-flows/summaries/wxcc-livechatinboundsampleflowwithsetvariable.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechatinboundsampleflowwithsetvariable).

App Start 2 enters Search Conversation 2433 using customer, app, and thread identity. No/closed conversation sends pre-chat form 2436 and waits up to 300 seconds in Receive 2635; app.onformresponse enters Evaluate 2465. Active/in-queue/on-hold search outcomes bypass the form and enter that Evaluate directly. Its numeric 1 outcome, rendered success, reaches Resolve Conversation 2588. Created/reopened goes through Append Conversation 2424 to Queue Task 2259; Queued runs Set Variable 2634, then sends queued notification 1727. Resolve appended/accepted terminates through End bindings.

**Exact handoffs:** Receive matches `$(n2.inappmessaging.userId)` and `$(n2.inappmessaging.threadId)`, extracting form Name/Email into customerName/customerEmail. Evaluate builds detailsJson from message, attachment, and scan context. Append records `$(n2635.inappmessaging.formResponse)` with its timestamp. Set Variable uses `$(taskId)` and maps `$(n2635.inappmessaging.formFields.IssueDescription)` and `$(n2635.inappmessaging.formFields.IssueType)` into same-named String task variables, both agent-viewable/editable, non-global, and non-reportable. Those names support the separate Task Routed extraction example.

**Adaptation limits:** All listed Set Variable outcomes, including Task Failed and errors, still send the queued notification; it is not proof that variables were stored. Form-field consumers depend on the pre-chat path. Queue uses chat media type while Close Task 2261 stores social, a captured mismatch. Resolve timeout closes only create/reopen; several End records refer to absent parents. App/form/queue values and conversationId need binding. No runtime test or desktop-variable propagation occurred. This internal model is not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechatinboundsampleflowwithsetvariablepiqandewt"></a>

## LiveChatInboundSampleFlowWithSetVariablePIQAndEWT.workflow

Observed 2026-09-09T00:07:00.851Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechatinboundsampleflowwithsetvariablepiqandewt.json) · [graph JSON](sample-flows/summaries/wxcc-livechatinboundsampleflowwithsetvariablepiqandewt.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechatinboundsampleflowwithsetvariablepiqandewt).

Incoming-message Start 2 searches at 2433. Missing/closed conversations send pre-chat form 2436 and Receive 2635 waits 300 seconds; active/in-queue/on-hold conversations bypass the form. Both paths normalize message and scan data in Evaluate 2465, then Resolve Conversation 2588. Created/reopened results append the form at 2424, queue the task at 2259, set task variables at 2634, and send queued notice 1727. Every captured Set Variable outcome continues to that notice; only its successful-send route fetches PIQ/EWT at 2475. PIQ success sends both values at 2476, while `InsufficientData` sends position alone at 2477. Both sends end Success/Error. Resolve appended/accepted terminates Success; resolve timeout branches at 2517. Queue/append failures attempt Close Task 2261 then send error notice 2227; form/search/parse failures use 2234.

**Exact handoffs:** Receive saves Name/Email into customer variables. Append consumes `$(n2635.inappmessaging.formResponse)` and timestamp; Set Variable copies `formFields.IssueDescription` and `formFields.IssueType` from that same Receive into agent-viewable, editable task fields. Resolve consumes `$(detailsJson)`; queue/set/PIQ consume custom `$(taskId)`. PIQ uses `$(queue)` with lookback minutes 5, extracting `positionInQueue` from `$.piq` and `estimatedWaitTime` from `$.ewt` for the two notices.

**Adaptation limits:** This retrieves queue status once; no polling or conversational loop is captured. Task-variable update failure is intentionally not a gate before the queued notice. Close Task is configured with media type `social` although Queue Task uses `chat`; the custom queue binding also needs reconciliation with the selected queue. Some notification failure routes and detached terminal producers are unresolved. Form template, tenant bindings and all runtime behavior remain untested.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-livechatqabotinboundflow"></a>

## LiveChatQABotInboundFlow.workflow

Observed 2026-09-09T00:03:14.397Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-livechatqabotinboundflow.json) · [graph JSON](sample-flows/summaries/wxcc-livechatqabotinboundflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-livechatqabotinboundflow).

App Start 2 searches conversation 1621. No/closed conversation sends form 36 and waits 300 seconds in Receive 38; active/in-queue/on-hold goes straight to Evaluate 1610. Resolve Conversation 1590 then sends created/reopened through Append form response 1254 into QnA bot 1661. onSuccess sends reply 745, timestamps it, and appends outbound 1273. Branch 1668 closes on Article containing Goodbye; otherwise Receive 756 waits 120 seconds. app.mo → Evaluate 1559 → filtering Branches 1108/1121 → inbound Append 1332 → bot forms the reply loop. onAgentHandover sends/appends a handoff message and queues task 1388.

**Exact handoffs:** Search and both Receives use the original app/user/thread identity. Form response provides customerName/customerEmail, while subsequent Receive refreshes `questionForBot` and message from `$(n756.receive.message)` plus attachments/scan state. Bot inputs use `consumer.uid=$(n2.inappmessaging.userId)`, correlation_id `$(transid)`, platform web, and `$(questionForBot)`. `$(n1661.TextResponse)` feeds channel Send and outbound Append; inbound Append uses `$(message)`, `$(n756.inappmessaging.timestamp)`, and `$(parseDataAttachment)`. Task operations consume taskId/conversationId; appended/accepted Resolve outcomes terminate.

**Adaptation limits:** Legacy QnA Bot semantics must not be substituted for the AI Agent node. typing_indicator and closechat are filtered back to Receive rather than closing; Goodbye uses Close Task 1669, whose stored media type social differs from chat elsewhere. Timeout/error notifications lead to Close Task 1357; terminal outcomes are attached via parent/event records. A log still references absent n9.evaluate.output. No total-loop bound appears. Form/app/queue bindings and placeholder conversationId require adaptation. Runtime testing is false: no bot turn, task, or message was executed. This internal model is not a public import schema.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-sms-inbound"></a>

## SMS inbound.workflow

Observed 2026-09-09T00:04:57.868Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-sms-inbound.json) · [graph JSON](sample-flows/summaries/wxcc-sms-inbound.json) · [all relationships](tenant-sample-relationships.md#wxcc-sms-inbound).

SMS Start 2 enters Evaluate 9 and then Resolve Conversation 1097 through numeric outcome 1/success. Resolve created/reopened sends SMS 1186, whose onsuccess enters Queue Task 736; Queued sends SMS 1153. Resolve appended/accepted terminates through End bindings, avoiding a second queue action for an already handled conversation. Queue errors/timeouts attempt Close Task 775. Close failures reach error SMS 984, while its Success terminates. Resolve timeout Branch 1362 closes its Create/Reopen Path and ends its Append Path.

**Exact handoffs:** Start copies senderNumber, serviceNumber, message, timestamp, transId, and scan metadata from the inbound event. Evaluate constructs a JSON object with messageDetails and scan details, then serializes detailsJson. Resolve consumes `$(transId)` and `$(detailsJson)` with media type social and channel sms; Queue/Close use `$(taskId)` and `$(conversationId)`. Notifications address `$(n2.sms.senderNumber)`. The acknowledgment text distinguishes message resolution from the later queued notification.

**Adaptation limits:** This is the basic event-driven inbound task flow: there is no QnA/AI Agent node or customer-reply Receive loop. SMS 1186 failure/policy outcomes terminate rather than queue, unlike the email sample. conversationId remains a placeholder, and sender/queue bindings are sample-specific. Duplicate End records for notification parents are internal residue. Configured cleanup and acknowledgment messages do not prove execution, routing, delivery, or resolution. Runtime testing is false; the internal canvas model is not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-smsqabotinboundflow"></a>

## SmsQABotInboundFlow.workflow

Observed 2026-09-09T00:03:21.623Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-smsqabotinboundflow.json) · [graph JSON](sample-flows/summaries/wxcc-smsqabotinboundflow.json) · [all relationships](tenant-sample-relationships.md#wxcc-smsqabotinboundflow).

SMS Start 2 → Evaluate 9 → Resolve Conversation 1097 creates the message/task context. Created/reopened sends SMS 1186, then QnA bot 1344. onSuccess sends TextResponse via SMS 1260, obtains a timestamp, and appends the outbound turn at 1266. Branch 1446 closes task 1447 when Article contains Goodbye; otherwise Receive 1268 waits 120 seconds. sms.mo enters Branches 1271/1273: closechat messages return to Receive, while other messages append inbound at 1272 and re-enter the bot. onAgentHandover sends/appends a handoff message, then Queue Task 736; Queued sends notification 1153.

**Exact handoffs:** The bot request uses `consumer.phone=$(n2.sms.senderNumber)`, correlation_id `$(transid)`, platform sms, and `msg=$(questionForBot)`. Receive filters the original sender, a stored service code, and wildcard keyword; on leave it refreshes questionForBot/message from `$(n1268.receive.message)`. Bot TextResponse comes from `$.generated_msg[0].text`; Article comes from `$.messageStore.top_match_section.first_question`. Queue and Close use taskId/conversationId. Inbound Append uses `$(message)` and `$(timern)`, the timestamp generated after the preceding bot send, despite Receive separately storing its own timestamp.

**Adaptation limits:** This is legacy QnA Bot, not the current AI Agent node contract. The closechat filter does not close the task; Goodbye or failure/timeout paths do. No total-turn cap is configured. Resolve appended/accepted and Close Task 1447 outcomes terminate through End parent/event bindings. Errors generally attempt Close Task 775; numeric/Boolean scan inputs versus string replace calls remain untested. Resource values and conversationId are sample bindings. No SMS, bot session, or task operation ran; this internal model is not a public import schema.

Captured graph: 1 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-task-close-flow-with-screen-pop"></a>

## Task Close Flow With Screen Pop.workflow

Observed 2026-09-09T00:03:53.840Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-task-close-flow-with-screen-pop.json) · [graph JSON](sample-flows/summaries/wxcc-task-close-flow-with-screen-pop.json) · [all relationships](tenant-sample-relationships.md#wxcc-task-close-flow-with-screen-pop).

WxCC Task v2 Start 2 listens for Task Closed and filters webex.destination to a stored integration value. Its onbegin event, rendered onBegin, leads to Evaluate 836; numeric outcome 1, rendered Success, leads to Screen Pop 720. This responds to closure already reported by WxCC; it does not perform Close Task. Screen Pop success terminates through End 916, bound to parentNode 720 and nodeEvent onScreenPopSuccess; failure/timeout bindings terminate with exitResult 3.

**Exact handoffs:** Start on-leave actions store `response=$(n2.webex.variables)` and `requestBody=$(n2.webex.RequestBody)`. Evaluate parses both JSON values, reads IssueDescription/IssueType by name from the variable array, reads customerId from requestObj.data.customerId, and obtains customerName from parsed callAssociatedDetails. Screen Pop uses `transid=$(n2.webex.taskId)`, `agentId=$(n2.webex.owner)`, target newBrowserTab, and a demonstration URL. Its nodeInput query carries `customerId=$(CustomerId)`, `customerName=$(CustomerName)`, and operation closed.

**Adaptation limits:** Stored request_body instead references lowercase `$(customerId)` and omits customerName. Evaluate uses lowercase customerId/customerName while custom variables are capitalized, with no explicit case-bridging session assignment in this capture. Preserve these differences when adapting. No retry, message send, or runtime task event was exercised; embedded isTestExecuted is template data. Destination and screen URL need appropriate bindings. The internal canvas model is evidence, not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-task-close-flow"></a>

## Task Close Flow.workflow

Observed 2026-09-09T00:04:28.883Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-task-close-flow.json) · [graph JSON](sample-flows/summaries/wxcc-task-close-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-task-close-flow).

Task Closed triggers WxCC Task v2 Start 2 after its webex.destination condition matches. Start onbegin/onBegin reaches Evaluate 836; numeric outcome 1, rendered Success, reaches Screen Pop 720. Despite the simple filename, this sample does contain Screen Pop. It does not close a task: the close event is its entry condition. End 928 binds Screen Pop onScreenPopSuccess with exitResult 2; failure, unavailable-service, and timeout terminals bind back to node 720 and use 3.

**Exact handoffs:** Start stores `$(n2.webex.variables)` in response and `$(n2.webex.RequestBody)` in requestBody. Evaluate parses the variable array and request envelope, extracts customerId from data.customerId, and traverses contact, queue, agent, team, and callAssociatedDetails fields. Screen Pop passes `$(n2.webex.taskId)` as transid and `$(n2.webex.owner)` as agentId, with newBrowserTab and operation closed. Its nodeInput query uses `$(CustomerId)`; stored request_body uses `$(customerId)`.

**Adaptation limits:** The capitalization mismatch matters because the script creates lowercase customerId and the declared custom variable is CustomerId; no explicit assignment bridges them here. The demonstration URL and destination filter are sample bindings, not production configuration. This graph has no retry or customer-message stage. No task closure or browser screen pop was executed, regardless of embedded test flags. The internal observed model is not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-task-modified-flow"></a>

## Task Modified Flow.workflow

Observed 2026-09-09T00:04:32.908Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-task-modified-flow.json) · [graph JSON](sample-flows/summaries/wxcc-task-modified-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-task-modified-flow).

WxCC Task v2 Start 2 receives Task Modified and filters webex.destination. It enters Evaluate 1630, then Branch 1547 through numeric outcome 1/Success. The branch sends only `$(n2.webex.context)` equal to add or remove through Add/Remove agent to Screen Pop 1326. None of the above terminates at End 1629 with exitResult 2, avoiding a screen pop for other modifications. Screen Pop onScreenPopSuccess terminates at End 1642.

**Exact handoffs:** Start copies `$(n2.webex.variables)` and `$(n2.webex.RequestBody)` into response/requestBody. Evaluate parses them, extracts IssueDescription/IssueType and standard contact/agent fields, and reads customerId from the event body. Screen Pop consumes `$(n2.webex.ID)` as transid and `$(n2.webex.agentId)` as agentId, targets sameBrowserTab, and marks operation modified. Its nodeInput uses `$(CustomerId)` while request_body uses `$(customerId)`.

**Adaptation limits:** The script-to-custom-variable capitalization discrepancy is retained; a populated CustomerId is not proven. Most error/timeout pseudo-nodes carry exitResult 3, but the onScreenPopFailure pseudo-node has a blank exitResult and no nodeEvent parameter; its association comes from parentNode/name. There is no retry, task mutation, or notification stage. The integration destination and URL are sample-specific. Runtime testing is false, and this internal canvas model is evidence rather than a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-task-routed-flow"></a>

## Task Routed Flow.workflow

Observed 2026-09-09T00:04:46.978Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-task-routed-flow.json) · [graph JSON](sample-flows/summaries/wxcc-task-routed-flow.json) · [all relationships](tenant-sample-relationships.md#wxcc-task-routed-flow).

WxCC Task v2 Start 2 accepts Task Routed for a configured webex.destination. Start onbegin/onBegin enters Evaluate 1520; its numeric result 1, rendered Success, reaches Screen Pop 1326. Screen Pop onScreenPopSuccess binds to End 1608 with exitResult 2. Evaluate failures and most Screen Pop errors/timeouts terminate with 3 through pseudo-node parent/event associations. This reacts to task assignment; it does not queue or route the task itself.

**Exact handoffs:** Start stores `response=$(n2.webex.variables)` and `requestBody=$(n2.webex.RequestBody)`. Evaluate parses the variable array and envelope, obtains customerId from data.customerId, and derives customerName from callAssociatedDetails, alongside contact/queue/agent fields. Screen Pop sends `transid=$(n2.webex.ID)` and `agentId=$(n2.webex.agentId)` to a demonstration URL in sameBrowserTab. The nodeInput query uses `CustomerName=$(customerName)` with operation routed; stored request_body instead carries `CustomerId=$(customerId)`.

**Adaptation limits:** Those two persisted query configurations are different contracts and were not reconciled by execution. The onScreenPopFailure End has blank exitResult, although its parent/name associates it with node 1326. No retry, customer reply, or downstream workflow exists. Stored integration values and script test flags do not prove a current task event or successful screen pop. Runtime testing is false; the internal model is not a public import schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-task-routed-sample-flow-for-extracting-variables"></a>

## Task Routed Sample Flow For Extracting Variables.workflow

Observed 2026-09-09T00:04:25.187Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-task-routed-sample-flow-for-extracting-variables.json) · [graph JSON](sample-flows/summaries/wxcc-task-routed-sample-flow-for-extracting-variables.json) · [all relationships](tenant-sample-relationships.md#wxcc-task-routed-sample-flow-for-extracting-variables).

Task Routed reaches WxCC Task v2 Start 2 under its webex.destination filter, then Evaluate 1520. Numeric outcome 1, rendered Success, connects to Screen Pop 1326. The central example is extracting task variables established by an inbound flow and carrying them into a desktop action. Screen Pop success terminates at End 1574 through parentNode 1326 and nodeEvent onScreenPopSuccess; most error/timeouts have corresponding End bindings.

**Exact handoffs:** Start copies `$(n2.webex.variables)` into response and `$(n2.webex.RequestBody)` into requestBody. Evaluate parses response as an array and uses extractVariable(name) to find IssueDescription and IssueType; it also reads customerId from requestObj.data.customerId and assigns custom CustomerId on leave. Screen Pop uses `transid=$(n2.webex.ID)`, `agentId=$(n2.webex.agentId)`, target sameBrowserTab, and query fields `issue=$(IssueDescription)` and `type=$(IssueType)`. The names match the separate LiveChat Set Variable example, but no direct Call Workflow edge joins the samples.

**Adaptation limits:** Task variables arrive through WxCC events, not shared local memory between independent flow invocations. The onScreenPopFailure pseudo-node has blank exitResult; preserve that incomplete configuration. The destination filter, URL, and desktop behavior need binding in an adapted design. Existing logs and embedded test flags are observations only. No event or screen pop was executed; the internal model is not an importable public schema.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.

<a id="wxcc-whatsapp-inbound"></a>

## Whatsapp inbound.workflow

Observed 2026-09-09T00:08:50.405Z. [Sanitized model](../evidence/sample-flows/observed/wxcc-whatsapp-inbound.json) · [graph JSON](sample-flows/summaries/wxcc-whatsapp-inbound.json) · [all relationships](tenant-sample-relationships.md#wxcc-whatsapp-inbound).

WhatsApp Incoming Message 2 enters Evaluate 9, then Resolve Conversation 2016. Resolve created/reopened events send acknowledgment 2018; its success, policy-failure and error edges all continue to Queue Task 1598. `Queued` sends notification 2039. Resolve appended ends successfully; accepted uses a Success terminal with asynchronous checking. Resolve timeout enters Branch 2126: created/reopened operations close Task 1599, appended ends successfully, unmatched/error ends with Error. Queue failures also close Task 1599; its configured outcomes converge on error notification 1938. Evaluate and other Resolve failures use notification 1923.

**Exact handoffs:** Start copies `$(n2.whatsapp.waId)`, username, message, attachments, caption, timestamp, transId and scan metadata into custom variables. Evaluate strips the transaction suffix, converts the incoming timestamp from seconds to ISO format, and creates `detailsJson` for Resolve's social/whatsapp operation. Queue/Close use unqualified taskId/conversationId; Branch uses `$(conversationOperation)`. Every WhatsApp message targets `$(n2.whatsapp.waId)` and uses a text body. The graph has no Receive wait, reply loop, AI Agent call or fulfillment operation.

**Adaptation limits:** The script uses appId while Start assigns appid, so case-sensitive binding must be checked when adapting. The initial error sender declares an error event without a captured recovery route. Queue, business-number and authorization bindings are sample-specific; acknowledgments and Success terminals do not establish agent acceptance or message delivery. Internal canvas evidence is not a public import schema. Runtime testing is false: no message, task or conversation was changed.

Captured graph: 0 cyclic node group(s), 0 explicit cross-page/flow connector(s). These counts describe captured wiring; runtime remains untested.
