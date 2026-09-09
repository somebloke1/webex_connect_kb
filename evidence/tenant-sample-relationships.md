# Observed tenant sample graphs

These walkthroughs describe sanitized, read-only captures of loaded sample canvases. They establish node configuration and connections, not successful execution. Existing tenant flows were not modified by this authoring workflow. Temporary sample inspection and cleanup are recorded by the capturing agent separately.

An End item may have no explicit incoming edge: `data.parentNode` plus its `nodeEvent` parameter associates the terminal with its producer and outcome. A binding whose producer is present is an observed terminal relationship, not an omitted route. Stale End parents and duplicate bindings are preserved and flagged; they do not establish an unseen producer or additional execution. The table prints the visible event label and retains differing internal names in parentheses; internal names are not public import-schema instructions.

## Coverage

Captured and summarized sample files: **59**. This count covers the files currently present in `sample-flows/observed/`; the parent's sample inventory determines whether all gallery/native samples have been captured. No absent sample is counted as reviewed.

| Sample | Operative nodes | Explicit edges | Terminal bindings | Graph summary |
| --- | ---: | ---: | ---: | --- |
| [AI Agent Scripted Doctor Appointment](#gallery-ai-doctor) | 43 | 160 | 31 | [JSON](sample-flows/summaries/gallery-ai-doctor.json) |
| [AI Agent Livechat Generic](#gallery-ai-livechat) | 27 | 109 | 26 | [JSON](sample-flows/summaries/gallery-ai-livechat.json) |
| [AppointmentReminder](#gallery-appointment-reminder) | 11 | 10 | 19 | [JSON](sample-flows/summaries/gallery-appointment-reminder.json) |
| [Autoresponder](#gallery-autoresponder) | 2 | 1 | 3 | [JSON](sample-flows/summaries/gallery-autoresponder.json) |
| [Chatbot](#gallery-chatbot) | 10 | 9 | 15 | [JSON](sample-flows/summaries/gallery-chatbot.json) |
| [LogisticsParcelNotifications](#gallery-logistics) | 16 | 16 | 26 | [JSON](sample-flows/summaries/gallery-logistics.json) |
| [SMSSurvey](#gallery-sms-survey) | 6 | 6 | 9 | [JSON](sample-flows/summaries/gallery-sms-survey.json) |
| [AI Agent Fulfilment - Track Package](#gallery-track-package) | 2 | 1 | 3 | [JSON](sample-flows/summaries/gallery-track-package.json) |
| [WebhooktoSMSalerts](#gallery-webhook-sms) | 2 | 1 | 0 | [JSON](sample-flows/summaries/gallery-webhook-sms.json) |
| [Block card and order replacement.workflow](#native-block-card-and-order-replacement) | 2 | 1 | 1 | [JSON](sample-flows/summaries/native-block-card-and-order-replacement.json) |
| [cancel_appointment.workflow](#native-cancel-appointment) | 2 | 1 | 0 | [JSON](sample-flows/summaries/native-cancel-appointment.json) |
| [cancel_booking.workflow](#native-cancel-booking) | 2 | 1 | 2 | [JSON](sample-flows/summaries/native-cancel-booking.json) |
| [cancel_checkin.workflow](#native-cancel-checkin) | 2 | 1 | 3 | [JSON](sample-flows/summaries/native-cancel-checkin.json) |
| [check_availability.workflow](#native-check-availability) | 2 | 1 | 0 | [JSON](sample-flows/summaries/native-check-availability.json) |
| [checkin.workflow](#native-checkin) | 2 | 1 | 3 | [JSON](sample-flows/summaries/native-checkin.json) |
| [create_appointment.workflow](#native-create-appointment) | 2 | 1 | 0 | [JSON](sample-flows/summaries/native-create-appointment.json) |
| [Fetch account balance.workflow](#native-fetch-account-balance) | 5 | 4 | 0 | [JSON](sample-flows/summaries/native-fetch-account-balance.json) |
| [Fetch Recent Transactions.workflow](#native-fetch-recent-transactions) | 5 | 4 | 0 | [JSON](sample-flows/summaries/native-fetch-recent-transactions.json) |
| [get_flight_info.workflow](#native-get-flight-info) | 2 | 1 | 2 | [JSON](sample-flows/summaries/native-get-flight-info.json) |
| [lookup_appointment.workflow](#native-lookup-appointment) | 2 | 1 | 0 | [JSON](sample-flows/summaries/native-lookup-appointment.json) |
| [lookup_flights.workflow](#native-lookup-flights) | 2 | 1 | 3 | [JSON](sample-flows/summaries/native-lookup-flights.json) |
| [Register Transaction Dispute.workflow](#native-register-transaction-dispute) | 2 | 1 | 1 | [JSON](sample-flows/summaries/native-register-transaction-dispute.json) |
| [Request priority shipping.workflow](#native-request-priority-shipping) | 2 | 1 | 1 | [JSON](sample-flows/summaries/native-request-priority-shipping.json) |
| [reschedule_flight.workflow](#native-reschedule-flight) | 2 | 1 | 2 | [JSON](sample-flows/summaries/native-reschedule-flight.json) |
| [sendSMS.workflow](#native-sendsms) | 2 | 1 | 0 | [JSON](sample-flows/summaries/native-sendsms.json) |
| [Verify user.workflow](#native-verify-user) | 2 | 1 | 3 | [JSON](sample-flows/summaries/native-verify-user.json) |
| [AMB Simplified Flow.workflow](#wxcc-amb-simplified-flow) | 13 | 36 | 28 | [JSON](sample-flows/summaries/wxcc-amb-simplified-flow.json) |
| [Apple Basic Inbound Flow.workflow](#wxcc-apple-basic-inbound-flow) | 13 | 49 | 14 | [JSON](sample-flows/summaries/wxcc-apple-basic-inbound-flow.json) |
| [Apple Form Response Flow.workflow](#wxcc-apple-form-response-flow) | 4 | 9 | 13 | [JSON](sample-flows/summaries/wxcc-apple-form-response-flow.json) |
| [Apple iMessage App Flow.workflow](#wxcc-apple-imessage-app-flow) | 5 | 13 | 12 | [JSON](sample-flows/summaries/wxcc-apple-imessage-app-flow.json) |
| [Apple Inbound Flow with Form.workflow](#wxcc-apple-inbound-flow-with-form) | 17 | 77 | 14 | [JSON](sample-flows/summaries/wxcc-apple-inbound-flow-with-form.json) |
| [Apple Inbound Flow with IntentId GroupId based Routing.workflow](#wxcc-apple-inbound-flow-with-intentid-groupid-based-routing) | 14 | 58 | 14 | [JSON](sample-flows/summaries/wxcc-apple-inbound-flow-with-intentid-groupid-based-routing.json) |
| [Apple List Picker Flow.workflow](#wxcc-apple-list-picker-flow) | 18 | 86 | 14 | [JSON](sample-flows/summaries/wxcc-apple-list-picker-flow.json) |
| [Apple Time Picker and List Picker Response Flow.workflow](#wxcc-apple-time-picker-and-list-picker-response-flow) | 6 | 18 | 17 | [JSON](sample-flows/summaries/wxcc-apple-time-picker-and-list-picker-response-flow.json) |
| [Apple Time Picker Flow.workflow](#wxcc-apple-time-picker-flow) | 14 | 57 | 14 | [JSON](sample-flows/summaries/wxcc-apple-time-picker-flow.json) |
| [Apple Unsubscribe Flow.workflow](#wxcc-apple-unsubscribe-flow) | 3 | 5 | 13 | [JSON](sample-flows/summaries/wxcc-apple-unsubscribe-flow.json) |
| [EmailAttachmentDropNotification.workflow](#wxcc-emailattachmentdropnotification) | 11 | 39 | 14 | [JSON](sample-flows/summaries/wxcc-emailattachmentdropnotification.json) |
| [EmailInboundFlow.workflow](#wxcc-emailinboundflow) | 10 | 35 | 14 | [JSON](sample-flows/summaries/wxcc-emailinboundflow.json) |
| [EmailInboundSampleFlowWithContactPriority.workflow](#wxcc-emailinboundsampleflowwithcontactpriority) | 11 | 38 | 14 | [JSON](sample-flows/summaries/wxcc-emailinboundsampleflowwithcontactpriority.json) |
| [FacebookAttachmentDropNotification.workflow](#wxcc-facebookattachmentdropnotification) | 11 | 39 | 14 | [JSON](sample-flows/summaries/wxcc-facebookattachmentdropnotification.json) |
| [FacebookCloseWithWxmFlow.workflow](#wxcc-facebookclosewithwxmflow) | 12 | 36 | 27 | [JSON](sample-flows/summaries/wxcc-facebookclosewithwxmflow.json) |
| [FacebookInboundFlow.workflow](#wxcc-facebookinboundflow) | 10 | 35 | 14 | [JSON](sample-flows/summaries/wxcc-facebookinboundflow.json) |
| [FacebookTaskBotInboundFlow.workflow](#wxcc-facebooktaskbotinboundflow) | 31 | 98 | 35 | [JSON](sample-flows/summaries/wxcc-facebooktaskbotinboundflow.json) |
| [Live Chat Close Flow.workflow](#wxcc-live-chat-close-flow) | 4 | 5 | 19 | [JSON](sample-flows/summaries/wxcc-live-chat-close-flow.json) |
| [Livechat Inbound flow with proactive chat changes.workflow](#wxcc-livechat-inbound-flow-with-proactive-chat-changes) | 15 | 67 | 14 | [JSON](sample-flows/summaries/wxcc-livechat-inbound-flow-with-proactive-chat-changes.json) |
| [LiveChatCloseWithWxmFlow.workflow](#wxcc-livechatclosewithwxmflow) | 12 | 36 | 27 | [JSON](sample-flows/summaries/wxcc-livechatclosewithwxmflow.json) |
| [LivechatInbound flow.workflow](#wxcc-livechatinbound-flow) | 13 | 55 | 14 | [JSON](sample-flows/summaries/wxcc-livechatinbound-flow.json) |
| [LivechatInboundFlowWithoutForm.workflow](#wxcc-livechatinboundflowwithoutform) | 9 | 32 | 14 | [JSON](sample-flows/summaries/wxcc-livechatinboundflowwithoutform.json) |
| [LiveChatInboundSampleFlowWithSetVariable.workflow](#wxcc-livechatinboundsampleflowwithsetvariable) | 14 | 66 | 14 | [JSON](sample-flows/summaries/wxcc-livechatinboundsampleflowwithsetvariable.json) |
| [LiveChatInboundSampleFlowWithSetVariablePIQAndEWT.workflow](#wxcc-livechatinboundsampleflowwithsetvariablepiqandewt) | 17 | 69 | 25 | [JSON](sample-flows/summaries/wxcc-livechatinboundsampleflowwithsetvariablepiqandewt.json) |
| [LiveChatQABotInboundFlow.workflow](#wxcc-livechatqabotinboundflow) | 29 | 114 | 24 | [JSON](sample-flows/summaries/wxcc-livechatqabotinboundflow.json) |
| [SMS inbound.workflow](#wxcc-sms-inbound) | 10 | 32 | 17 | [JSON](sample-flows/summaries/wxcc-sms-inbound.json) |
| [SmsQABotInboundFlow.workflow](#wxcc-smsqabotinboundflow) | 23 | 84 | 27 | [JSON](sample-flows/summaries/wxcc-smsqabotinboundflow.json) |
| [Task Close Flow With Screen Pop.workflow](#wxcc-task-close-flow-with-screen-pop) | 3 | 2 | 9 | [JSON](sample-flows/summaries/wxcc-task-close-flow-with-screen-pop.json) |
| [Task Close Flow.workflow](#wxcc-task-close-flow) | 3 | 2 | 9 | [JSON](sample-flows/summaries/wxcc-task-close-flow.json) |
| [Task Modified Flow.workflow](#wxcc-task-modified-flow) | 4 | 3 | 12 | [JSON](sample-flows/summaries/wxcc-task-modified-flow.json) |
| [Task Routed Flow.workflow](#wxcc-task-routed-flow) | 3 | 2 | 9 | [JSON](sample-flows/summaries/wxcc-task-routed-flow.json) |
| [Task Routed Sample Flow For Extracting Variables.workflow](#wxcc-task-routed-sample-flow-for-extracting-variables) | 3 | 2 | 9 | [JSON](sample-flows/summaries/wxcc-task-routed-sample-flow-for-extracting-variables.json) |
| [Whatsapp inbound.workflow](#wxcc-whatsapp-inbound) | 10 | 35 | 14 | [JSON](sample-flows/summaries/wxcc-whatsapp-inbound.json) |

## How an agent should use these samples

Trace each business outcome from Start through a concrete transition to a terminal or the next waiting state. Read the consumer's configured variable and identify its producer; preserve the sample's exact case and node namespace. Session/custom assignments can have several observed writers, so inspect control order rather than choosing the first writer. Script-local bindings, runtime response shape and cross-page variable visibility require their own evidence.

Reuse the relationship pattern and adapt bindings to the target tenant. Redacted URLs/headers, selected assets, identities, node versions, integration methods and sample response bodies are not operational defaults. Error and timeout routes are part of each walkthrough. A declared event without a captured route is reported as a capture/configuration fact; it is not automatically a product defect. No runtime action is authorized by these descriptions.

<a id="gallery-ai-doctor"></a>

## AI Agent Scripted Doctor Appointment

Observed 2026-09-08T23:56:36.255Z. [Captured model](../evidence/sample-flows/observed/gallery-ai-doctor.json); [complete graph summary](sample-flows/summaries/gallery-ai-doctor.json). Runtime tested: **no**.

This extends the generic Live Chat lifecycle with appointment fulfillment. Search/Resolve Conversation, pre-chat, bot replies, append operations and Receive 756 form the same outer conversation. After an agent reply is sent/appended, parser 1745 reads SessionMetadata and parser 1725 reads messageMetadata. Branch 1727 selects availability, create, lookup or cancel using responseKey. Each branch extracts relevant entities, calls its HTTP node, and joins Evaluate 1731 to construct fulfilmentResp. The response is sent and appended before returning to Receive. A fulfillment failure can use the error-handover path. On agent handover, previous-intent classification chooses an appointment-specific queue or the general queue. Receive failure closes the task and the agent session.

Useful handoffs: AI `MessageMetadata` is copied to `messageMetadata`; parser 1725 extracts `$.templateKey` as `responseKey`. `SessionMetadata` supplies `$.previous_intent_model_state.intent.name` as PreviousIntent and `$.model_state.entities.<entity>.value` for date/period/name/birth-date/reason. HTTP availability maps `$.nearest_available_slots[0]` to `n1726.nearest_available_slot`; create maps appointment_number/status; lookup maps date/time. `fulfilmentStatusCode` and those outputs feed `fulfilmentResp`, then Send 1735 and Append 1738.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Mobile & Web App Event | onBegin (`onbegin`) → 1621: Search Conversation |
| 36: Pre-chat form | onSuccess (`onsuccess`) → 38: Receive; onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1487: Error notif |
| 38: Receive | app.onformresponse → 1610: Evaluate; onError (`onerror`), onTimeout (`ontimeout`) → 372: Close conversation notify |
| 372: Close conversation notify | onError (`onerror`), onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`) → 1357: Close Task |
| 745: Send Bot response | onSuccess (`onsuccess`) → 1273: Append Conversation |
| 756: Receive | onTimeout (`ontimeout`), onError (`onerror`) → 1519: Close chat notification; app.mo → 1559: Parse attachments and PCI check |
| 768: Connecting to agent notification | onSuccess (`onsuccess`) → 1465: Append Conversation; onError (`onerror`) → End 1757 → Error; onPolicyFail (`onpolicyfail`) → End 1758 → Error |
| 1108: Invalid message check | invalid msgs → 1121: Invalid message check; None of the above → 1332: Append Conversation; onError (`onerror`) → 1357: Close Task |
| 1121: Invalid message check | invalid msgs → 756: Receive; None of the above → 1332: Append Conversation; onError (`onerror`) → 1357: Close Task |
| 1254: Append Conversation | onInvalidData (`oninvaliddata`), onTimeout (`ontimeout`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1695: AI Agent |
| 1273: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onTimeout (`ontimeout`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1745: Parse agent sessionmetadata |
| 1332: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1695: AI Agent |
| 1357: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error → 1513: Error notif |
| 1388: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1357: Close Task; Queued → 1613: Queued |
| 1465: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1746: Branch |
| 1487: Error notif | onSuccess (`onsuccess`) → End 1641 → Success |
| 1513: Error notif | onError (`onerror`) → End 1639 → Error; onPolicyFail (`onpolicyfail`) → End 1640 → Error; onError (`onerror`) → End 1649 → Error; onPolicyFail (`onpolicyfail`) → End 1650 → Error; onSuccess (`onsuccess`) → End 1651 → Success |
| 1519: Close chat notification | onSuccess (`onsuccess`), onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1702: Close Task |
| 1559: Parse attachments and PCI check | success (`1`) → 1108: Invalid message check; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1357: Close Task |
| 1590: Resolve Conversation | created, reopened → 1254: Append Conversation; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 1487: Error notif; onTimeout (`ontimeout`) → 1632: Branch; onauthorizationfail → 372: Close conversation notify; appended → End 1791 → Success; accepted → End 1792 → Success |
| 1610: Evaluate | success (`1`) → 1590: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1487: Error notif |
| 1613: Queued | onSuccess (`onsuccess`) → End 1614 → Success; onError (`onerror`) → End 1616 → Error; onPolicyFail (`onpolicyfail`) → End 1619 → Error |
| 1621: Search Conversation | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`) → 1487: Error notif; noConversationFound, conversationClosed → 36: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 1610: Evaluate |
| 1632: Branch | Create/Reopen Path → 1357: Close Task; onError (`onerror`) → End 1644 → Error; Append Path → End 1645 → Success; None of the above → End 1646 → Error |
| 1695: AI Agent | onAgentHandover → 768: Connecting to agent notification; onTimeout (`ontimeout`) → 1519: Close chat notification; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onFailure → 1357: Close Task; onSuccess → 745: Send Bot response |
| 1702: Close Task | Success → 1761: AI Agent; onTimeout (`ontimeout`) → End 1703 → Incomplete; onError (`onerror`) → End 1708 → Error; onInvalidData (`oninvaliddata`) → End 1712 → Error; onInvalidChoice (`oninvalidchoice`) → End 1717 → Error; Error → End 1723 → Error |
| 1725: Parse agent messagemetadata | onSuccess (`oncomplete`) → 1727: check response name; onError (`onerror`) → 1357: Close Task |
| 1726: check_availability | onSuccess (`oncomplete`) → 1731: Process fulfilment data; onError (`onerror`), onTimeout (`ontimeout`) → 1357: Close Task |
| 1727: check response name | None of the above → 756: Receive; onError (`onerror`) → 1357: Close Task; check_availability → 1748: extract entities; create_appointment → 1749: extract entities; lookup_appointment → 1753: extract entities; cancel_appointment → 1754: extract entities |
| 1731: Process fulfilment data | fulfilment → 1735: Send fulfilment response; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1357: Close Task; error handover (`1`) → 768: Connecting to agent notification |
| 1735: Send fulfilment response | onSuccess (`onsuccess`) → 1738: Append Conversation; onError (`onerror`) → End 1733 → Error; onPolicyFail (`onpolicyfail`) → End 1734 → Error; onError (`onerror`) → End 1743 → Error; onPolicyFail (`onpolicyfail`) → End 1744 → Error |
| 1738: Append Conversation | onAppendMessageSuccess → 756: Receive; onInvalidData (`oninvaliddata`), onTimeout (`ontimeout`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure → 1357: Close Task |
| 1745: Parse agent sessionmetadata | onSuccess (`oncomplete`) → 1725: Parse agent messagemetadata; onError (`onerror`) → 1357: Close Task |
| 1746: Branch | None of the above → 1388: Queue Task; appointmentCases → 1747: Queue Task; onError (`onerror`) → 1357: Close Task |
| 1747: Queue Task | Queued → 1613: Queued; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 1357: Close Task |
| 1748: extract entities | onSuccess (`oncomplete`) → 1726: check_availability; onError (`onerror`) → 1357: Close Task |
| 1749: extract entities | onSuccess (`oncomplete`) → 1752: create_appointment; onError (`onerror`) → 1357: Close Task |
| 1752: create_appointment | onSuccess (`oncomplete`) → 1731: Process fulfilment data; onError (`onerror`), onTimeout (`ontimeout`) → 1357: Close Task |
| 1753: extract entities | onSuccess (`oncomplete`) → 1755: lookup_appointment; onError (`onerror`) → 1357: Close Task |
| 1754: extract entities | onSuccess (`oncomplete`) → 1756: cancel_appointment; onError (`onerror`) → 1357: Close Task |
| 1755: lookup_appointment | onSuccess (`oncomplete`) → 1731: Process fulfilment data; onError (`onerror`), onTimeout (`ontimeout`) → 1357: Close Task |
| 1756: cancel_appointment | onSuccess (`oncomplete`) → 1731: Process fulfilment data; onError (`onerror`), onTimeout (`ontimeout`) → 1357: Close Task |
| 1761: AI Agent | onInvalidData (`oninvaliddata`) → End 1793 → Error; onError (`onerror`) → End 1794 → Error; onInvalidChoice (`oninvalidchoice`) → End 1795 → Error; onFailure → End 1796 → Error; onTimeout (`ontimeout`) → End 1797 → Incomplete; onSuccess → End 1798 → Success |

**Loops in the captured graph:** 745: Send Bot response → 756: Receive → 1108: Invalid message check → 1121: Invalid message check → 1273: Append Conversation → 1332: Append Conversation → 1559: Parse attachments and PCI check → 1695: AI Agent → 1725: Parse agent messagemetadata → 1726: check_availability → 1727: check response name → 1731: Process fulfilment data → 1735: Send fulfilment response → 1738: Append Conversation → 1745: Parse agent sessionmetadata → 1748: extract entities → 1749: extract entities → 1752: create_appointment → 1753: extract entities → 1754: extract entities → 1755: lookup_appointment → 1756: cancel_appointment. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.message)` | 2: Configure Mobile & Web App Event / transition_actions[0].value; 2: Configure Mobile & Web App Event / transition_actions[19].value; 2: Configure Mobile & Web App Event / transition_actions[32].value; 2: Configure Mobile & Web App Event / transition_actions[3].value; flow-custom-defaults / customVariables[6].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.attachment)` | 2: Configure Mobile & Web App Event / transition_actions[12].value; 2: Configure Mobile & Web App Event / transition_actions[1].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure Mobile & Web App Event / transition_actions[20].value; 2: Configure Mobile & Web App Event / transition_actions[2].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.appId)` | 1621: Search Conversation / extraParamsData.bizaddress; 1621: Search Conversation / nodeInput.bizaddress; 1621: Search Conversation / request_body[2].value; 2: Configure Mobile & Web App Event / transition_actions[4].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[21].value; 2: Configure Mobile & Web App Event / transition_actions[5].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.extras)` | 2: Configure Mobile & Web App Event / transition_actions[6].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadId)` | 1487: Error notif / thread_id; 1513: Error notif / thread_id; 1519: Close chat notification / thread_id; 1613: Queued / thread_id; 1621: Search Conversation / extraParamsData.threadid; 1621: Search Conversation / nodeInput.threadid; 1621: Search Conversation / request_body[4].value; 1735: Send fulfilment response / thread_id; 2: Configure Mobile & Web App Event / transition_actions[7].value; 36: Pre-chat form / thread_id; 372: Close conversation notify / thread_id; 38: Receive / data[0].threadid; 745: Send Bot response / thread_id; 756: Receive / data[0].threadid; 768: Connecting to agent notification / thread_id |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure Mobile & Web App Event / transition_actions[8].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure Mobile & Web App Event / transition_actions[9].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.userId)` | 1487: Error notif / destination; 1513: Error notif / destination; 1519: Close chat notification / destination; 1613: Queued / destination; 1621: Search Conversation / extraParamsData.browserfingerprint; 1621: Search Conversation / extraParamsData.customeraddress; 1621: Search Conversation / nodeInput.browserfingerprint; 1621: Search Conversation / nodeInput.customeraddress; 1621: Search Conversation / request_body[1].value; 1621: Search Conversation / request_body[5].value; 1695: AI Agent / extraParamsData.consumer.uid; 1695: AI Agent / extraParamsData.request_body.consumer.uid; 1695: AI Agent / extraParamsData.uid; 1695: AI Agent / nodeInput.consumer.uid; 1695: AI Agent / nodeInput.request_body.consumer.uid; 1695: AI Agent / nodeInput.uid; 1695: AI Agent / request_body[0].value.consumer.u… [full value in graph summary] |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[11].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.version)` | 2: Configure Mobile & Web App Event / transition_actions[13].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.timestamp)` | 2: Configure Mobile & Web App Event / transition_actions[14].value |
| 2: Configure Mobile & Web App Event | `$(n2.service.serviceKey)` | 2: Configure Mobile & Web App Event / transition_actions[15].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure Mobile & Web App Event / transition_actions[16].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[17].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure Mobile & Web App Event / transition_actions[18].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.tid)` | 2: Configure Mobile & Web App Event / transition_actions[22].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[23].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure Mobile & Web App Event / transition_actions[24].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[25].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure Mobile & Web App Event / transition_actions[26].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[27].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure Mobile & Web App Event / transition_actions[28].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure Mobile & Web App Event / transition_actions[29].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[30].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(appId)` | 2: Configure Mobile & Web App Event / transition_actions[31].value |
| 38: Receive | `$(n38.inappmessaging.timestamp)` | 1254: Append Conversation / extraParamsData.timestamp; 1254: Append Conversation / request_body[6].value; 38: Receive / transition_actions[0].value |
| 38: Receive | `$(n38.inappmessaging.formFields.Name)` | 38: Receive / transition_actions[1].value |
| 38: Receive | `$(n38.inappmessaging.formFields.Email)` | 38: Receive / transition_actions[2].value |
| custom variable; writers 1695: AI Agent, 1731: Process fulfilment data, 1761: AI Agent | `$(agentTextResp)` | 1273: Append Conversation / extraParamsData.text; 1273: Append Conversation / extraParamsData.textOrResponse; 1273: Append Conversation / nodeInput.text; 1273: Append Conversation / nodeInput.textOrResponse; 1273: Append Conversation / request_body[5].value; 1465: Append Conversation / extraParamsData.text; 1465: Append Conversation / extraParamsData.textOrResponse; 1465: Append Conversation / nodeInput.text; 1465: Append Conversation / nodeInput.textOrResponse; 1465: Append Conversation / request_body[5].value; 1731: Process fulfilment data / transition_actions[1].value; 745: Send Bot response / message; 768: Connecting to agent notification / message |
| 756: Receive | `$(n756.receive.message)` | 1108: Invalid message check / expression; 1108: Invalid message check / outcomes[0].conditions[0].varaible; 1108: Invalid message check / outcomes[0].conditions[1].varaible; 1121: Invalid message check / expression; 1121: Invalid message check / outcomes[0].conditions[0].varaible; 1121: Invalid message check / outcomes[0].conditions[1].varaible; 756: Receive / transition_actions[0].value; 756: Receive / transition_actions[2].value; 756: Receive / transition_actions[8].value |
| 756: Receive | `$(n756.inappmessaging.timestamp)` | 1332: Append Conversation / extraParamsData.timestamp; 1332: Append Conversation / request_body[6].value; 756: Receive / transition_actions[10].value; 756: Receive / transition_actions[1].value |
| 756: Receive | `$(n756.inappmessaging.attachment)` | 756: Receive / transition_actions[12].value; 756: Receive / transition_actions[3].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 756: Receive / transition_actions[4].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.securityFailedReason)` | 756: Receive / transition_actions[5].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.isSecurityCompliance)` | 756: Receive / transition_actions[6].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 756: Receive / transition_actions[7].value |
| 756: Receive | `$(n756.inappmessaging.message)` | 756: Receive / transition_actions[9].value |
| 756: Receive | `$(n756.receive.attachment)` | 756: Receive / transition_actions[11].value |
| 756: Receive | `$(n756.receive.payload)` | 756: Receive / transition_actions[13].value |
| 38: Receive | `$(n38.inappmessaging.formResponse)` | 1254: Append Conversation / extraParamsData.livechatformresponse; 1254: Append Conversation / extraParamsData.textOrResponse; 1254: Append Conversation / request_body[4].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1254: Append Conversation / extraParamsData.conversationid; 1254: Append Conversation / path_parameters[1].value; 1273: Append Conversation / extraParamsData.conversationid; 1273: Append Conversation / nodeInput.conversationid; 1273: Append Conversation / path_parameters[1].value; 1332: Append Conversation / extraParamsData.conversationid; 1332: Append Conversation / path_parameters[1].value; 1357: Close Task / nodeInput.Conversation ID; 1357: Close Task / request_body[2].value; 1388: Queue Task / extraParamsData.conversationid; 1388: Queue Task / nodeInput.conversationid; 1388: Queue Task / request_body[3].value; 1388: Queue Task / transition_actions[1].value; 1465: Append Conversation / extraParamsData.conversationid; 1465: Append Conversation / nodeInput.conversationid; 1465: Append Con… [full value in graph summary] |
| 745: Send Bot response | `$(n745.send.sentDateTime)` | 1273: Append Conversation / extraParamsData.timestamp; 1273: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(timern)` | 1273: Append Conversation / nodeInput.timestamp; 1465: Append Conversation / nodeInput.timestamp; 1738: Append Conversation / nodeInput.timestamp |
| custom variable; writers 2: Configure Mobile & Web App Event, 756: Receive | `$(message)` | 1332: Append Conversation / extraParamsData.text; 1332: Append Conversation / extraParamsData.textOrResponse; 1332: Append Conversation / request_body[5].value; 1559: Parse attachments and PCI check / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(parseDataAttachment)` | 1332: Append Conversation / extraParamsData.attachments; 1332: Append Conversation / request_body[7].value; 1332: Append Conversation / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1357: Close Task / nodeInput.ID; 1357: Close Task / nodeInput.Task Id; 1357: Close Task / path_parameters[1].value; 1357: Close Task / request_body[0].value; 1357: Close Task / transition_actions[0].value; 1388: Queue Task / extraParamsData.id; 1388: Queue Task / nodeInput.id; 1388: Queue Task / path_parameters[1].value; 1388: Queue Task / request_body[0].value; 1388: Queue Task / transition_actions[0].value; 1590: Resolve Conversation / transition_actions[0].value; 1702: Close Task / nodeInput.ID; 1702: Close Task / nodeInput.Task Id; 1702: Close Task / path_parameters[1].value; 1702: Close Task / request_body[0].value; 1702: Close Task / transition_actions[0].value; 1747: Queue Task / extraParamsData.id; 1747: Queue Task / nodeInput.id; 1747: Queue Task / path_parameters[1].value; 1747: … [full value in graph summary] |
| 768: Connecting to agent notification | `$(n768.send.sentDateTime)` | 1465: Append Conversation / extraParamsData.timestamp; 1465: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1487: Error notif / message; 1513: Error notif / message |
| custom variable; writers 2: Configure Mobile & Web App Event, 756: Receive | `$(inappPayloadObject)` | 1559: Parse attachments and PCI check / transition_actions[1].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(nonPCIComplianceReasonObject)` | 1559: Parse attachments and PCI check / transition_actions[2].value |
| External/system/custom value; producer not established here | `$(tid)` | 1559: Parse attachments and PCI check / transition_actions[3].value |
| External/system/custom value; producer not established here | `$(flid)` | 1559: Parse attachments and PCI check / transition_actions[4].value |
| 9 | `$(n9.evaluate.output)` | 1559: Parse attachments and PCI check / transition_actions[5].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(transId)` | 1590: Resolve Conversation / extraParamsData.trackingId; 1590: Resolve Conversation / extraParamsData.transId; 1590: Resolve Conversation / nodeInput.trackingId; 1590: Resolve Conversation / nodeInput.transId; 1590: Resolve Conversation / request_body[0].value; 1590: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1590: Resolve Conversation / extraParamsData.details; 1590: Resolve Conversation / nodeInput.details; 1590: Resolve Conversation / request_body[6].value; 1610: Evaluate / transition_actions[0].value |
| custom variable; writers 38: Receive | `$(customerName)` | 1590: Resolve Conversation / transition_actions[3].value |
| custom variable; writers 38: Receive | `$(customerEmail)` | 1590: Resolve Conversation / transition_actions[4].value |
| 1590: Resolve Conversation | `$(n1590.conversationOperation)` | 1632: Branch / expression; 1632: Branch / outcomes[0].conditions[0].varaible; 1632: Branch / outcomes[0].conditions[1].varaible; 1632: Branch / outcomes[1].conditions[0].varaible; 1632: Branch / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(transid)` | 1695: AI Agent / extraParamsData.request_body.correlation_id; 1695: AI Agent / extraParamsData.transid; 1695: AI Agent / nodeInput.request_body.correlation_id; 1695: AI Agent / nodeInput.transid; 1695: AI Agent / request_body[0].value.correlation_id; 1761: AI Agent / extraParamsData.request_body.correlation_id; 1761: AI Agent / extraParamsData.transid; 1761: AI Agent / nodeInput.request_body.correlation_id; 1761: AI Agent / nodeInput.transid |
| custom variable; writers 1559: Parse attachments and PCI check, 2: Configure Mobile & Web App Event, 756: Receive | `$(questionForBot)` | 1695: AI Agent / extraParamsData.msg; 1695: AI Agent / extraParamsData.request_body.msg; 1695: AI Agent / nodeInput.msg; 1695: AI Agent / nodeInput.request_body.msg; 1695: AI Agent / request_body[0].value.msg; 1761: AI Agent / extraParamsData.msg; 1761: AI Agent / extraParamsData.request_body.msg; 1761: AI Agent / nodeInput.msg; 1761: AI Agent / nodeInput.request_body.msg |
| 1695: AI Agent | `$(n1695.TextResponse)` | 1695: AI Agent / transition_actions[0].value; 1761: AI Agent / transition_actions[0].value |
| 1695: AI Agent | `$(n1695.FullResponse)` | 1695: AI Agent / transition_actions[1].value; 1761: AI Agent / transition_actions[1].value |
| 1695: AI Agent | `$(n1695.MessageMetadata)` | 1695: AI Agent / transition_actions[2].value; 1695: AI Agent / transition_actions[4].value; 1761: AI Agent / transition_actions[2].value; 1761: AI Agent / transition_actions[4].value |
| 1695: AI Agent | `$(n1695.SessionMetadata)` | 1695: AI Agent / transition_actions[3].value; 1695: AI Agent / transition_actions[5].value; 1745: Parse agent sessionmetadata / input; 1748: extract entities / input; 1749: extract entities / input; 1753: extract entities / input; 1754: extract entities / input; 1761: AI Agent / transition_actions[3].value; 1761: AI Agent / transition_actions[5].value |
| custom variable; writers 1695: AI Agent, 1761: AI Agent | `$(messageMetadata)` | 1725: Parse agent messagemetadata / input |
| 1725: Parse agent messagemetadata | `$(n1725.responseKey)` | 1725: Parse agent messagemetadata / transition_actions[0].value; 1748: extract entities / transition_actions[0].value; 1749: extract entities / transition_actions[0].value; 1753: extract entities / transition_actions[0].value; 1754: extract entities / transition_actions[0].value |
| 1748: extract entities | `$(n1748.preferred_period)` | 1726: check_availability / body.preferred_period |
| 1748: extract entities | `$(n1748.preferred_date)` | 1726: check_availability / body.preferred_date |
| 1726: check_availability | `$(n1726.http.statusCode)` | 1726: check_availability / transition_actions[0].value; 1726: check_availability / transition_actions[1].value |
| custom variable; writers 1726: check_availability, 1752: create_appointment, 1755: lookup_appointment, 1756: cancel_appointment | `$(fulfilmentStatusCode)` | 1726: check_availability / transition_actions[2].value; 1731: Process fulfilment data / exp; 1731: Process fulfilment data / expression; 1731: Process fulfilment data / transition_actions[2].value |
| custom variable; writers 1725: Parse agent messagemetadata, 1748: extract entities, 1749: extract entities, 1753: extract entities, 1754: extract entities | `$(responseKey)` | 1727: check response name / expression; 1727: check response name / outcomes[0].conditions[0].varaible; 1727: check response name / outcomes[1].conditions[0].varaible; 1727: check response name / outcomes[2].conditions[0].varaible; 1727: check response name / outcomes[3].conditions[0].varaible; 1731: Process fulfilment data / exp; 1731: Process fulfilment data / expression |
| 1726: check_availability | `$(n1726.nearest_available_slot)` | 1731: Process fulfilment data / exp; 1731: Process fulfilment data / expression; 1752: create_appointment / body.time_slot |
| 1755: lookup_appointment | `$(n1755.date)` | 1731: Process fulfilment data / exp; 1731: Process fulfilment data / expression |
| 1755: lookup_appointment | `$(n1755.time)` | 1731: Process fulfilment data / exp; 1731: Process fulfilment data / expression |
| custom variable; writers 1731: Process fulfilment data | `$(fulfilmentResp)` | 1731: Process fulfilment data / transition_actions[0].value; 1735: Send fulfilment response / message; 1738: Append Conversation / extraParamsData.text; 1738: Append Conversation / extraParamsData.textOrResponse; 1738: Append Conversation / nodeInput.text; 1738: Append Conversation / nodeInput.textOrResponse; 1738: Append Conversation / request_body[5].value |
| 1735: Send fulfilment response | `$(n1735.send.sentDateTime)` | 1738: Append Conversation / extraParamsData.timestamp; 1738: Append Conversation / request_body[6].value |
| 1745: Parse agent sessionmetadata | `$(n1745.PreviousIntent)` | 1746: Branch / expression; 1746: Branch / outcomes[0].conditions[0].varaible; 1746: Branch / outcomes[0].conditions[1].varaible; 1746: Branch / outcomes[0].conditions[2].varaible; 1746: Branch / outcomes[0].conditions[3].varaible |
| 1749: extract entities | `$(n1749.date_of_birth)` | 1752: create_appointment / body.date_of_birth |
| 1749: extract entities | `$(n1749.patient_name)` | 1752: create_appointment / body.patient_name |
| 1749: extract entities | `$(n1749.reason)` | 1752: create_appointment / body.reason |
| 1752: create_appointment | `$(n1752.http.statusCode)` | 1752: create_appointment / transition_actions[0].value |
| 1753: extract entities | `$(n1753.date_of_birth)` | 1755: lookup_appointment / body.date_of_birth |
| 1753: extract entities | `$(n1753.patient_name)` | 1755: lookup_appointment / body.patient_name |
| 1755: lookup_appointment | `$(n1755.http.statusCode)` | 1755: lookup_appointment / transition_actions[0].value |
| 1755: lookup_appointment | `$(n1755.appointment_number)` | 1756: cancel_appointment / body.appointment_number |
| 1756: cancel_appointment | `$(n1756.http.statusCode)` | 1756: cancel_appointment / transition_actions[0].value |
| 1695: AI Agent | `$(n1695.SessionId)` | 1761: AI Agent / extraParamsData.session_id; 1761: AI Agent / nodeInput.session_id; 1761: AI Agent / request_body[0].value |

### Boundaries and adaptation

These nested metadata paths are sample/version-specific observations, not universal AI Agent output guarantees. The node exposes MessageMetadata/SessionMetadata rather than legacy Task Bot Intent/Entities outputs. It uses integration version 52902 and case-sensitive DataStore mapping. Close Session timeout ends Incomplete here. Embedded API examples, queue IDs, selected agents and entity names require adaptation; the captured n9 debug reference has no captured producer. Material error-path mismatch: Evaluate 1731 assigns agentTextResponse on backend failure, but its onleave assignment persists agentTextResp. Its result 1 (error handover) leads to Send 768, which consumes $(agentTextResp), previously populated from n1695.TextResponse. The intended system-error text is therefore not established by this captured assignment; stale agent text may be reused. In an authorized adaptation, align the script variable, transition assignment and Send consumer, initialize the failure message explicitly, and verify the failed-fulfillment path. This is a documentation finding; the native sample was not edited or executed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 745: Send Bot response / `onerror` (declared target count 1); 1487: Error notif / `onerror` (declared target count 1); 1725: Parse agent messagemetadata / `oninvaliddata` (declared target count None); 1745: Parse agent sessionmetadata / `oninvaliddata` (declared target count None); 1748: extract entities / `oninvaliddata` (declared target count None); 1749: extract entities / `oninvaliddata` (declared target count None); 1753: extract entities / `oninvaliddata` (declared target count None); 1754: extract entities / `oninvaliddata` (declared target count None).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
Literal node-qualified references name uncaptured producers: n9. Their provenance is not guessed.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-ai-livechat"></a>

## AI Agent Livechat Generic

Observed 2026-09-08T23:56:08.143Z. [Captured model](../evidence/sample-flows/observed/gallery-ai-livechat.json); [complete graph summary](sample-flows/summaries/gallery-ai-livechat.json). Runtime tested: **no**.

An incoming app message reaches Search Conversation 1621. New or closed conversations receive a pre-chat form and wait at Receive 38; active, queued or on-hold conversations go directly through payload preparation 1610 to Resolve Conversation 1590. Created/reopened outcomes append the form and invoke AI Agent 1695; appended and accepted outcomes terminate through their own End bindings, avoiding a second bot turn on that path. The bot success path sends TextResponse, appends that outgoing message, and waits at Receive 756. A customer reply is normalized/checked, appended inbound, and sent back to AI Agent: this is the captured conversational loop. Handover sends a notice, appends it, queues the task and acknowledges queuing. Receive errors/timeouts close the task, notify the customer and invoke the separate AI Agent Close Session method.

Useful handoffs: `n2.inappmessaging.userId` and `threadId` anchor sends, search and receives. Start/Receive transition actions write `questionForBot`; the Process Message request consumes `$(questionForBot)`. `$(n1695.TextResponse)` feeds Send Bot response and Append Conversation. Close Session consumes `$(n1695.SessionId)`. Resolve Conversation exposes `conversationOperation`, whose timeout branch distinguishes created/reopened from appended.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Mobile & Web App Event | onBegin (`onbegin`) → 1621: Search Conversation |
| 36: Pre-chat form | onSuccess (`onsuccess`) → 38: Receive; onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1487: Error notif |
| 38: Receive | app.onformresponse → 1610: Evaluate; onError (`onerror`), onTimeout (`ontimeout`) → 372: Close conversation notify |
| 372: Close conversation notify | onError (`onerror`), onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`) → 1357: Close Task |
| 745: Send Bot response | onSuccess (`onsuccess`) → 1273: Append Conversation; onError (`onerror`) → End 1738 → Error; onPolicyFail (`onpolicyfail`) → End 1739 → Error |
| 756: Receive | app.mo → 1559: Parse attachments and PCI check; onTimeout (`ontimeout`), onError (`onerror`) → 1700: Close Task |
| 768: Connecting to agent notification | onSuccess (`onsuccess`) → 1465: Append Conversation; onError (`onerror`) → End 1707 → Error; onPolicyFail (`onpolicyfail`) → End 1708 → Error |
| 1108: Invalid message check | invalid msgs → 1121: Invalid message check; None of the above → 1332: Append Conversation; onError (`onerror`) → 1357: Close Task |
| 1121: Invalid message check | invalid msgs → 756: Receive; None of the above → 1332: Append Conversation; onError (`onerror`) → 1357: Close Task |
| 1254: Append Conversation | onInvalidData (`oninvaliddata`), onTimeout (`ontimeout`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1695: AI Agent |
| 1273: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onTimeout (`ontimeout`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 756: Receive |
| 1332: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1695: AI Agent |
| 1357: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error → 1513: Error notif |
| 1388: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1357: Close Task; Queued → 1613: Queued |
| 1465: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1388: Queue Task |
| 1487: Error notif | onSuccess (`onsuccess`) → End 1641 → Success |
| 1513: Error notif | onError (`onerror`) → End 1639 → Error; onPolicyFail (`onpolicyfail`) → End 1640 → Error; onError (`onerror`) → End 1649 → Error; onPolicyFail (`onpolicyfail`) → End 1650 → Error; onSuccess (`onsuccess`) → End 1651 → Success |
| 1519: Close chat notification | onSuccess (`onsuccess`) → 1711: AI Agent; onError (`onerror`) → End 1703 → Error; onPolicyFail (`onpolicyfail`) → End 1706 → Error |
| 1559: Parse attachments and PCI check | success (`1`) → 1108: Invalid message check; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1357: Close Task |
| 1590: Resolve Conversation | created, reopened → 1254: Append Conversation; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 1487: Error notif; onTimeout (`ontimeout`) → 1632: Branch; onauthorizationfail → 372: Close conversation notify; appended → End 1742 → Success; accepted → End 1743 → Success |
| 1610: Evaluate | success (`1`) → 1590: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1487: Error notif |
| 1613: Queued | onSuccess (`onsuccess`) → End 1614 → Success; onError (`onerror`) → End 1616 → Error; onPolicyFail (`onpolicyfail`) → End 1619 → Error |
| 1621: Search Conversation | noConversationFound, conversationClosed → 36: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 1610: Evaluate; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`) → 1487: Error notif |
| 1632: Branch | Create/Reopen Path → 1357: Close Task; onError (`onerror`) → End 1644 → Error; Append Path → End 1645 → Success; None of the above → End 1646 → Error |
| 1695: AI Agent | onSuccess → 745: Send Bot response; onAgentHandover → 768: Connecting to agent notification; onTimeout (`ontimeout`) → 1519: Close chat notification; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onFailure → 1357: Close Task |
| 1700: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error → 1519: Close chat notification |
| 1711: AI Agent | onInvalidData (`oninvaliddata`) → End 1744 → Error; onError (`onerror`) → End 1745 → Error; onInvalidChoice (`oninvalidchoice`) → End 1746 → Error; onFailure → End 1747 → Error; onTimeout (`ontimeout`) → End 1748 → Success; onSuccess → End 1749 → Success |

**Loops in the captured graph:** 745: Send Bot response → 756: Receive → 1108: Invalid message check → 1121: Invalid message check → 1273: Append Conversation → 1332: Append Conversation → 1559: Parse attachments and PCI check → 1695: AI Agent. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.message)` | 2: Configure Mobile & Web App Event / transition_actions[0].value; 2: Configure Mobile & Web App Event / transition_actions[19].value; 2: Configure Mobile & Web App Event / transition_actions[32].value; 2: Configure Mobile & Web App Event / transition_actions[3].value; flow-custom-defaults / customVariables[6].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.attachment)` | 2: Configure Mobile & Web App Event / transition_actions[12].value; 2: Configure Mobile & Web App Event / transition_actions[1].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure Mobile & Web App Event / transition_actions[20].value; 2: Configure Mobile & Web App Event / transition_actions[2].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.appId)` | 1621: Search Conversation / extraParamsData.bizaddress; 1621: Search Conversation / nodeInput.bizaddress; 1621: Search Conversation / request_body[2].value; 2: Configure Mobile & Web App Event / transition_actions[4].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[21].value; 2: Configure Mobile & Web App Event / transition_actions[5].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.extras)` | 2: Configure Mobile & Web App Event / transition_actions[6].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadId)` | 1487: Error notif / thread_id; 1513: Error notif / thread_id; 1519: Close chat notification / thread_id; 1613: Queued / thread_id; 1621: Search Conversation / extraParamsData.threadid; 1621: Search Conversation / nodeInput.threadid; 1621: Search Conversation / request_body[4].value; 2: Configure Mobile & Web App Event / transition_actions[7].value; 36: Pre-chat form / thread_id; 372: Close conversation notify / thread_id; 38: Receive / data[0].threadid; 745: Send Bot response / thread_id; 756: Receive / data[0].threadid; 768: Connecting to agent notification / thread_id |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure Mobile & Web App Event / transition_actions[8].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure Mobile & Web App Event / transition_actions[9].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.userId)` | 1487: Error notif / destination; 1513: Error notif / destination; 1519: Close chat notification / destination; 1613: Queued / destination; 1621: Search Conversation / extraParamsData.browserfingerprint; 1621: Search Conversation / extraParamsData.customeraddress; 1621: Search Conversation / nodeInput.browserfingerprint; 1621: Search Conversation / nodeInput.customeraddress; 1621: Search Conversation / request_body[1].value; 1621: Search Conversation / request_body[5].value; 1695: AI Agent / extraParamsData.consumer.uid; 1695: AI Agent / extraParamsData.request_body.consumer.uid; 1695: AI Agent / extraParamsData.uid; 1695: AI Agent / nodeInput.consumer.uid; 1695: AI Agent / nodeInput.request_body.consumer.uid; 1695: AI Agent / nodeInput.uid; 1695: AI Agent / request_body[0].value.consumer.u… [full value in graph summary] |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[11].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.version)` | 2: Configure Mobile & Web App Event / transition_actions[13].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.timestamp)` | 2: Configure Mobile & Web App Event / transition_actions[14].value |
| 2: Configure Mobile & Web App Event | `$(n2.service.serviceKey)` | 2: Configure Mobile & Web App Event / transition_actions[15].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure Mobile & Web App Event / transition_actions[16].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[17].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure Mobile & Web App Event / transition_actions[18].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.tid)` | 2: Configure Mobile & Web App Event / transition_actions[22].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[23].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure Mobile & Web App Event / transition_actions[24].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[25].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure Mobile & Web App Event / transition_actions[26].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[27].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure Mobile & Web App Event / transition_actions[28].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure Mobile & Web App Event / transition_actions[29].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[30].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(appId)` | 2: Configure Mobile & Web App Event / transition_actions[31].value |
| 38: Receive | `$(n38.inappmessaging.timestamp)` | 1254: Append Conversation / extraParamsData.timestamp; 1254: Append Conversation / request_body[6].value; 38: Receive / transition_actions[0].value |
| 38: Receive | `$(n38.inappmessaging.formFields.Name)` | 38: Receive / transition_actions[1].value |
| 38: Receive | `$(n38.inappmessaging.formFields.Email)` | 38: Receive / transition_actions[2].value |
| 1695: AI Agent | `$(n1695.TextResponse)` | 1273: Append Conversation / extraParamsData.text; 1273: Append Conversation / extraParamsData.textOrResponse; 1273: Append Conversation / nodeInput.text; 1273: Append Conversation / nodeInput.textOrResponse; 1273: Append Conversation / request_body[5].value; 1465: Append Conversation / extraParamsData.text; 1465: Append Conversation / extraParamsData.textOrResponse; 1465: Append Conversation / nodeInput.text; 1465: Append Conversation / nodeInput.textOrResponse; 1465: Append Conversation / request_body[5].value; 745: Send Bot response / message; 768: Connecting to agent notification / message |
| 756: Receive | `$(n756.receive.message)` | 1108: Invalid message check / expression; 1108: Invalid message check / outcomes[0].conditions[0].varaible; 1108: Invalid message check / outcomes[0].conditions[1].varaible; 1121: Invalid message check / expression; 1121: Invalid message check / outcomes[0].conditions[0].varaible; 1121: Invalid message check / outcomes[0].conditions[1].varaible; 756: Receive / transition_actions[0].value; 756: Receive / transition_actions[2].value; 756: Receive / transition_actions[8].value |
| 756: Receive | `$(n756.inappmessaging.timestamp)` | 1332: Append Conversation / extraParamsData.timestamp; 1332: Append Conversation / request_body[6].value; 756: Receive / transition_actions[10].value; 756: Receive / transition_actions[1].value |
| 756: Receive | `$(n756.inappmessaging.attachment)` | 756: Receive / transition_actions[12].value; 756: Receive / transition_actions[3].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 756: Receive / transition_actions[4].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.securityFailedReason)` | 756: Receive / transition_actions[5].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.isSecurityCompliance)` | 756: Receive / transition_actions[6].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 756: Receive / transition_actions[7].value |
| 756: Receive | `$(n756.inappmessaging.message)` | 756: Receive / transition_actions[9].value |
| 756: Receive | `$(n756.receive.attachment)` | 756: Receive / transition_actions[11].value |
| 756: Receive | `$(n756.receive.payload)` | 756: Receive / transition_actions[13].value |
| 38: Receive | `$(n38.inappmessaging.formResponse)` | 1254: Append Conversation / extraParamsData.livechatformresponse; 1254: Append Conversation / extraParamsData.textOrResponse; 1254: Append Conversation / request_body[4].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1254: Append Conversation / extraParamsData.conversationid; 1254: Append Conversation / path_parameters[1].value; 1273: Append Conversation / extraParamsData.conversationid; 1273: Append Conversation / nodeInput.conversationid; 1273: Append Conversation / path_parameters[1].value; 1332: Append Conversation / extraParamsData.conversationid; 1332: Append Conversation / path_parameters[1].value; 1357: Close Task / nodeInput.Conversation ID; 1357: Close Task / request_body[2].value; 1388: Queue Task / extraParamsData.conversationid; 1388: Queue Task / nodeInput.conversationid; 1388: Queue Task / request_body[3].value; 1388: Queue Task / transition_actions[1].value; 1465: Append Conversation / extraParamsData.conversationid; 1465: Append Conversation / nodeInput.conversationid; 1465: Append Con… [full value in graph summary] |
| 745: Send Bot response | `$(n745.send.sentDateTime)` | 1273: Append Conversation / extraParamsData.timestamp; 1273: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(timern)` | 1273: Append Conversation / nodeInput.timestamp; 1465: Append Conversation / nodeInput.timestamp |
| custom variable; writers 2: Configure Mobile & Web App Event, 756: Receive | `$(message)` | 1332: Append Conversation / extraParamsData.text; 1332: Append Conversation / extraParamsData.textOrResponse; 1332: Append Conversation / request_body[5].value; 1559: Parse attachments and PCI check / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(parseDataAttachment)` | 1332: Append Conversation / extraParamsData.attachments; 1332: Append Conversation / request_body[7].value; 1332: Append Conversation / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1357: Close Task / nodeInput.ID; 1357: Close Task / nodeInput.Task Id; 1357: Close Task / path_parameters[1].value; 1357: Close Task / request_body[0].value; 1357: Close Task / transition_actions[0].value; 1388: Queue Task / extraParamsData.id; 1388: Queue Task / nodeInput.id; 1388: Queue Task / path_parameters[1].value; 1388: Queue Task / request_body[0].value; 1388: Queue Task / transition_actions[0].value; 1590: Resolve Conversation / transition_actions[0].value; 1700: Close Task / nodeInput.ID; 1700: Close Task / nodeInput.Task Id; 1700: Close Task / path_parameters[1].value; 1700: Close Task / request_body[0].value; 1700: Close Task / transition_actions[0].value |
| 768: Connecting to agent notification | `$(n768.send.sentDateTime)` | 1465: Append Conversation / extraParamsData.timestamp; 1465: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1487: Error notif / message; 1513: Error notif / message |
| custom variable; writers 2: Configure Mobile & Web App Event, 756: Receive | `$(inappPayloadObject)` | 1559: Parse attachments and PCI check / transition_actions[1].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(nonPCIComplianceReasonObject)` | 1559: Parse attachments and PCI check / transition_actions[2].value |
| External/system/custom value; producer not established here | `$(tid)` | 1559: Parse attachments and PCI check / transition_actions[3].value |
| External/system/custom value; producer not established here | `$(flid)` | 1559: Parse attachments and PCI check / transition_actions[4].value |
| 9 | `$(n9.evaluate.output)` | 1559: Parse attachments and PCI check / transition_actions[5].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(transId)` | 1590: Resolve Conversation / extraParamsData.trackingId; 1590: Resolve Conversation / extraParamsData.transId; 1590: Resolve Conversation / nodeInput.trackingId; 1590: Resolve Conversation / nodeInput.transId; 1590: Resolve Conversation / request_body[0].value; 1590: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1590: Resolve Conversation / extraParamsData.details; 1590: Resolve Conversation / nodeInput.details; 1590: Resolve Conversation / request_body[6].value; 1610: Evaluate / transition_actions[0].value |
| custom variable; writers 38: Receive | `$(customerName)` | 1590: Resolve Conversation / transition_actions[3].value |
| custom variable; writers 38: Receive | `$(customerEmail)` | 1590: Resolve Conversation / transition_actions[4].value |
| 1590: Resolve Conversation | `$(n1590.conversationOperation)` | 1632: Branch / expression; 1632: Branch / outcomes[0].conditions[0].varaible; 1632: Branch / outcomes[0].conditions[1].varaible; 1632: Branch / outcomes[1].conditions[0].varaible; 1632: Branch / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(transid)` | 1695: AI Agent / extraParamsData.request_body.correlation_id; 1695: AI Agent / extraParamsData.transid; 1695: AI Agent / nodeInput.request_body.correlation_id; 1695: AI Agent / nodeInput.transid; 1695: AI Agent / request_body[0].value.correlation_id; 1711: AI Agent / extraParamsData.request_body.correlation_id; 1711: AI Agent / extraParamsData.transid; 1711: AI Agent / nodeInput.request_body.correlation_id; 1711: AI Agent / nodeInput.transid |
| custom variable; writers 1559: Parse attachments and PCI check, 2: Configure Mobile & Web App Event, 756: Receive | `$(questionForBot)` | 1695: AI Agent / extraParamsData.msg; 1695: AI Agent / extraParamsData.request_body.msg; 1695: AI Agent / nodeInput.msg; 1695: AI Agent / nodeInput.request_body.msg; 1695: AI Agent / request_body[0].value.msg; 1711: AI Agent / extraParamsData.msg; 1711: AI Agent / extraParamsData.request_body.msg; 1711: AI Agent / nodeInput.msg; 1711: AI Agent / nodeInput.request_body.msg |
| 1695: AI Agent | `$(n1695.MessageMetadata)` | 1695: AI Agent / transition_actions[0].value |
| 1695: AI Agent | `$(n1695.SessionMetadata)` | 1695: AI Agent / transition_actions[1].value |
| 1695: AI Agent | `$(n1695.SessionId)` | 1711: AI Agent / extraParamsData.session_id; 1711: AI Agent / nodeInput.session_id; 1711: AI Agent / request_body[0].value |

### Boundaries and adaptation

The captured AI integration version ID is 52902 with Process Message method 58694 and Close Session 58695. Its mapping spells `DataStore`, whereas the compact current documentation uses `Datastore`; preserve the observed version/case instead of generalizing. The Close Session timeout End is configured as Success here, unlike the doctor sample. A log references uncaptured n9.evaluate.output; this is stale/uncaptured debug provenance, not evidence of a working producer.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1487: Error notif / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
Literal node-qualified references name uncaptured producers: n9. Their provenance is not guessed.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-appointment-reminder"></a>

## AppointmentReminder

Observed 2026-09-08T23:58:37.146Z. [Captured model](../evidence/sample-flows/observed/gallery-appointment-reminder.json); [complete graph summary](sample-flows/summaries/gallery-appointment-reminder.json). Runtime tested: **no**.

Webhook Start 2 sends an appointment reminder through SMS 225, then Receive 11 waits 600 seconds. Branch 19 maps A to HTTP 25 (`/appointconfirm`) and B to HTTP 29 (`/appointmentcancel`). HTTP success sends the relevant confirmation/cancellation message, while HTTP error sends an unable-to-process response. Unrecognized customer input receives a clarification message and does not loop back in the captured graph.

Useful handoffs: The reminder uses custom values `$(name)` and `$(dateTime)` and sends to `$(msisdn)`. Branch 19 reads `$(n11.receive.message)`. Confirmation/cancellation are represented by separate HTTP paths and separate success/failure SMS nodes.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Webhook | onbegin → 225: Send SMS |
| 11: Receive | sms.mo → 19: Check User Response; onerror → End 104 → ; ontimeout → End 112 →  |
| 19: Check User Response | Confirm → 25: API Update; Cancel → 29: HTTP request; None of the above → 238: Send SMS; onerror → End 118 →  |
| 25: API Update | oncomplete → 290: Send SMS; onerror → 298: Send SMS |
| 29: HTTP request | onerror → 328: Send SMS; oncomplete → 320: Send SMS |
| 225: Send SMS | onsuccess → 11: Receive; onerror → End 237 → Error |
| 238: Send SMS | onsuccess → End 249 → Success; onerror → End 256 → Error; onpolicyfail → End 288 → Error; onerror → End 307 → Error; onpolicyfail → End 308 → Error; onsuccess → End 311 → Success; onerror → End 313 → Error; onpolicyfail → End 314 → Error; onsuccess → End 317 → Success; onerror → End 337 → Error; onpolicyfail → End 338 → Error; onsuccess → End 341 → Success; onerror → End 343 → Error; onpolicyfail → End 344 → Error; onsuccess → End 347 → Success |
| 290: Send SMS | No outgoing route captured |
| 298: Send SMS | No outgoing route captured |
| 320: Send SMS | No outgoing route captured |
| 328: Send SMS | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 11: Receive | `$(n11.receive.message)` | 19: Check User Response / expression; 19: Check User Response / outcomes[0].conditions[0].varaible; 19: Check User Response / outcomes[1].conditions[0].varaible |
| External/system/custom value; producer not established here | `$(name)` | 225: Send SMS / message; flow-custom-defaults / customVariables[26].value |
| External/system/custom value; producer not established here | `$(dateTime)` | 225: Send SMS / message |
| External/system/custom value; producer not established here | `$(msisdn)` | 225: Send SMS / destination; 238: Send SMS / destination; 290: Send SMS / destination; 298: Send SMS / destination; 320: Send SMS / destination; 328: Send SMS / destination; flow-custom-defaults / customVariables[5].value |
| External/system/custom value; producer not established here | `$(facebook.psid)` | flow-custom-defaults / customVariables[0].value |
| External/system/custom value; producer not established here | `$(wechat.wechat_user_id)` | flow-custom-defaults / customVariables[1].value |
| External/system/custom value; producer not established here | `$(app.deviceId)` | flow-custom-defaults / customVariables[2].value |
| External/system/custom value; producer not established here | `$(app.pushId)` | flow-custom-defaults / customVariables[3].value |
| External/system/custom value; producer not established here | `$(twitter.twitterid)` | flow-custom-defaults / customVariables[4].value |
| External/system/custom value; producer not established here | `$(email)` | flow-custom-defaults / customVariables[6].value |
| External/system/custom value; producer not established here | `$(customerId)` | flow-custom-defaults / customVariables[7].value |
| External/system/custom value; producer not established here | `$(app.imei)` | flow-custom-defaults / customVariables[8].value |
| External/system/custom value; producer not established here | `$(app.os)` | flow-custom-defaults / customVariables[9].value |
| External/system/custom value; producer not established here | `$(app.model)` | flow-custom-defaults / customVariables[10].value |
| External/system/custom value; producer not established here | `$(app.telecom)` | flow-custom-defaults / customVariables[11].value |
| External/system/custom value; producer not established here | `$(app.imsi)` | flow-custom-defaults / customVariables[12].value |
| External/system/custom value; producer not established here | `$(app.location)` | flow-custom-defaults / customVariables[13].value |
| External/system/custom value; producer not established here | `$(app.language)` | flow-custom-defaults / customVariables[14].value |
| External/system/custom value; producer not established here | `$(facebook.birthday)` | flow-custom-defaults / customVariables[15].value |
| External/system/custom value; producer not established here | `$(facebook.email)` | flow-custom-defaults / customVariables[16].value |
| External/system/custom value; producer not established here | `$(facebook.first_name)` | flow-custom-defaults / customVariables[17].value |
| External/system/custom value; producer not established here | `$(facebook.gender)` | flow-custom-defaults / customVariables[18].value |
| External/system/custom value; producer not established here | `$(facebook.last_name)` | flow-custom-defaults / customVariables[19].value |
| External/system/custom value; producer not established here | `$(facebook.location)` | flow-custom-defaults / customVariables[20].value |
| External/system/custom value; producer not established here | `$(facebook.middle_name)` | flow-custom-defaults / customVariables[21].value |
| External/system/custom value; producer not established here | `$(facebook.name)` | flow-custom-defaults / customVariables[22].value |
| External/system/custom value; producer not established here | `$(facebook.timezone)` | flow-custom-defaults / customVariables[23].value |
| External/system/custom value; producer not established here | `$(twitter.username)` | flow-custom-defaults / customVariables[24].value |
| External/system/custom value; producer not established here | `$(app.rtmId)` | flow-custom-defaults / customVariables[25].value |
| External/system/custom value; producer not established here | `$(app.oldlocation)` | flow-custom-defaults / customVariables[27].value |
| External/system/custom value; producer not established here | `$(app.mcc)` | flow-custom-defaults / customVariables[28].value |
| External/system/custom value; producer not established here | `$(app.mnc)` | flow-custom-defaults / customVariables[29].value |
| External/system/custom value; producer not established here | `$(message)` | flow-custom-defaults / customVariables[30].value |
| External/system/custom value; producer not established here | `$(time)` | flow-custom-defaults / customVariables[31].value |
| External/system/custom value; producer not established here | `$(app.message)` | flow-custom-defaults / customVariables[32].value |
| External/system/custom value; producer not established here | `$(sms.message)` | flow-custom-defaults / customVariables[33].value |
| External/system/custom value; producer not established here | `$(twitter.message)` | flow-custom-defaults / customVariables[34].value |
| External/system/custom value; producer not established here | `$(facebook.message)` | flow-custom-defaults / customVariables[35].value |
| External/system/custom value; producer not established here | `$(wechat.message)` | flow-custom-defaults / customVariables[36].value |
| External/system/custom value; producer not established here | `$(app.thread_id)` | flow-custom-defaults / customVariables[37].value |
| External/system/custom value; producer not established here | `$(abc.attachmentCount)` | flow-custom-defaults / customVariables[38].value |
| External/system/custom value; producer not established here | `$(abc.message)` | flow-custom-defaults / customVariables[39].value |
| External/system/custom value; producer not established here | `$(abc.requestIdentifier)` | flow-custom-defaults / customVariables[40].value |
| External/system/custom value; producer not established here | `$(abc.interactive_type)` | flow-custom-defaults / customVariables[41].value |
| External/system/custom value; producer not established here | `$(abc.hasattachment)` | flow-custom-defaults / customVariables[42].value |
| External/system/custom value; producer not established here | `$(abc.abcUserId)` | flow-custom-defaults / customVariables[43].value |

### Boundaries and adaptation

The timestamp appears in message text; no Delay/Scheduler node is captured, so this graph alone does not schedule reminders. The sample models the business actions with GET and does not prove safe mutation semantics or an appointment-ID contract. Several final-send error declarations lack captured routes. Do not infer that the acknowledgement updates a real appointment.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 290: Send SMS / `onerror` (declared target count 1); 298: Send SMS / `onerror` (declared target count 1); 320: Send SMS / `onerror` (declared target count 1); 328: Send SMS / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-autoresponder"></a>

## Autoresponder

Observed 2026-09-08T23:58:25.886Z. [Captured model](../evidence/sample-flows/observed/gallery-autoresponder.json); [complete graph summary](sample-flows/summaries/gallery-autoresponder.json). Runtime tested: **no**.

SMS Start 2 immediately routes to Send SMS 33. The reply acknowledges the incoming message, and the send's End bindings map the observed outcomes. There is no Receive node because this flow handles one inbound event per invocation, rather than maintaining an in-flow conversation.

Useful handoffs: The reply text interpolates `$(n2.sms.message)` and its recipient is the inbound sender `$(n2.sms.sender_number)`. Reusing the source identity prevents accidentally addressing the business number, but actual sender/asset configuration still needs tenant binding.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure SMS Event | onbegin → 33: Send SMS |
| 33: Send SMS | onsuccess → End 44 → Success; onerror → End 51 → ; onpolicyfail → End 59 → Incomplete |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure SMS Event | `$(n2.sms.message)` | 33: Send SMS / message |
| 2: Configure SMS Event | `$(n2.sms.sender_number)` | 33: Send SMS / destination |
| External/system/custom value; producer not established here | `$(facebook.psid)` | flow-custom-defaults / customVariables[0].value |
| External/system/custom value; producer not established here | `$(wechat.wechat_user_id)` | flow-custom-defaults / customVariables[1].value |
| External/system/custom value; producer not established here | `$(app.deviceId)` | flow-custom-defaults / customVariables[2].value |
| External/system/custom value; producer not established here | `$(app.pushId)` | flow-custom-defaults / customVariables[3].value |
| External/system/custom value; producer not established here | `$(twitter.twitterid)` | flow-custom-defaults / customVariables[4].value |
| External/system/custom value; producer not established here | `$(msisdn)` | flow-custom-defaults / customVariables[5].value |
| External/system/custom value; producer not established here | `$(email)` | flow-custom-defaults / customVariables[6].value |
| External/system/custom value; producer not established here | `$(customerId)` | flow-custom-defaults / customVariables[7].value |
| External/system/custom value; producer not established here | `$(app.imei)` | flow-custom-defaults / customVariables[8].value |
| External/system/custom value; producer not established here | `$(app.os)` | flow-custom-defaults / customVariables[9].value |
| External/system/custom value; producer not established here | `$(app.model)` | flow-custom-defaults / customVariables[10].value |
| External/system/custom value; producer not established here | `$(app.telecom)` | flow-custom-defaults / customVariables[11].value |
| External/system/custom value; producer not established here | `$(app.imsi)` | flow-custom-defaults / customVariables[12].value |
| External/system/custom value; producer not established here | `$(app.location)` | flow-custom-defaults / customVariables[13].value |
| External/system/custom value; producer not established here | `$(app.language)` | flow-custom-defaults / customVariables[14].value |
| External/system/custom value; producer not established here | `$(facebook.birthday)` | flow-custom-defaults / customVariables[15].value |
| External/system/custom value; producer not established here | `$(facebook.email)` | flow-custom-defaults / customVariables[16].value |
| External/system/custom value; producer not established here | `$(facebook.first_name)` | flow-custom-defaults / customVariables[17].value |
| External/system/custom value; producer not established here | `$(facebook.gender)` | flow-custom-defaults / customVariables[18].value |
| External/system/custom value; producer not established here | `$(facebook.last_name)` | flow-custom-defaults / customVariables[19].value |
| External/system/custom value; producer not established here | `$(facebook.location)` | flow-custom-defaults / customVariables[20].value |
| External/system/custom value; producer not established here | `$(facebook.middle_name)` | flow-custom-defaults / customVariables[21].value |
| External/system/custom value; producer not established here | `$(facebook.name)` | flow-custom-defaults / customVariables[22].value |
| External/system/custom value; producer not established here | `$(facebook.timezone)` | flow-custom-defaults / customVariables[23].value |
| External/system/custom value; producer not established here | `$(twitter.username)` | flow-custom-defaults / customVariables[24].value |
| External/system/custom value; producer not established here | `$(app.rtmId)` | flow-custom-defaults / customVariables[25].value |
| External/system/custom value; producer not established here | `$(name)` | flow-custom-defaults / customVariables[26].value |
| External/system/custom value; producer not established here | `$(app.oldlocation)` | flow-custom-defaults / customVariables[27].value |
| External/system/custom value; producer not established here | `$(app.mcc)` | flow-custom-defaults / customVariables[28].value |
| External/system/custom value; producer not established here | `$(app.mnc)` | flow-custom-defaults / customVariables[29].value |
| External/system/custom value; producer not established here | `$(message)` | flow-custom-defaults / customVariables[30].value |
| External/system/custom value; producer not established here | `$(time)` | flow-custom-defaults / customVariables[31].value |
| External/system/custom value; producer not established here | `$(app.message)` | flow-custom-defaults / customVariables[32].value |
| External/system/custom value; producer not established here | `$(sms.message)` | flow-custom-defaults / customVariables[33].value |
| External/system/custom value; producer not established here | `$(twitter.message)` | flow-custom-defaults / customVariables[34].value |
| External/system/custom value; producer not established here | `$(facebook.message)` | flow-custom-defaults / customVariables[35].value |
| External/system/custom value; producer not established here | `$(wechat.message)` | flow-custom-defaults / customVariables[36].value |
| External/system/custom value; producer not established here | `$(app.thread_id)` | flow-custom-defaults / customVariables[37].value |
| External/system/custom value; producer not established here | `$(abc.attachmentCount)` | flow-custom-defaults / customVariables[38].value |
| External/system/custom value; producer not established here | `$(abc.message)` | flow-custom-defaults / customVariables[39].value |
| External/system/custom value; producer not established here | `$(abc.requestIdentifier)` | flow-custom-defaults / customVariables[40].value |
| External/system/custom value; producer not established here | `$(abc.interactive_type)` | flow-custom-defaults / customVariables[41].value |
| External/system/custom value; producer not established here | `$(abc.hasattachment)` | flow-custom-defaults / customVariables[42].value |
| External/system/custom value; producer not established here | `$(abc.abcUserId)` | flow-custom-defaults / customVariables[43].value |

### Boundaries and adaptation

This sample contains no explicit keyword classifier, rate limiter, duplicate-event guard or bot invocation. It demonstrates acknowledgement only; configured End outcomes are not proof a handset received the response.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-chatbot"></a>

## Chatbot

Observed 2026-09-08T23:58:00.130Z. [Captured model](../evidence/sample-flows/observed/gallery-chatbot.json); [complete graph summary](sample-flows/summaries/gallery-chatbot.json). Runtime tested: **no**.

An inbound SMS starts a deterministic pizza menu. Send 157 presents A/B/C choices; Receive 11 waits 600 seconds; Branch 19 routes choices to one of three HTTP GET nodes. Each HTTP success path sends an order-confirmation SMS. This is a menu-and-branch example, with no observed AI Agent node and no customer-response loop after the order branch.

Useful handoffs: Every outgoing SMS addresses `$(n2.sms.sender_number)`. Branch 19 consumes `$(n11.receive.message)`; A selects Cajun, the nominal B branch selects Beef, and C selects Branch3. The HTTP nodes each use the same captured `/api/cajunpziza` path, so distinct menu outcomes do not establish distinct business-system requests.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure SMS Event | onbegin → 157: Send SMS |
| 11: Receive | sms.mo → 19: Branch; onerror → End 134 → ; ontimeout → End 142 →  |
| 19: Branch | Cajun → 33: HTTP request; Beef → 84: HTTP request; Branch3 → 71: HTTP request; onerror → End 127 →  |
| 33: HTTP request | oncomplete → 185: Send SMS; onerror → End 42 → ; onerror → End 74 → ; onerror → End 87 →  |
| 71: HTTP request | oncomplete → 192: Send SMS |
| 84: HTTP request | oncomplete → 178: Send SMS |
| 157: Send SMS | onsuccess → 11: Receive; onerror → End 169 → Error; onpolicyfail → End 176 → Incomplete; onerror → End 200 → Error; onpolicyfail → End 201 → Incomplete; onerror → End 205 → Error; onpolicyfail → End 206 → Incomplete; onerror → End 210 → Error; onpolicyfail → End 211 → Incomplete |
| 178: Send SMS | No outgoing route captured |
| 185: Send SMS | onsuccess → End 222 → Success |
| 192: Send SMS | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 11: Receive | `$(n11.receive.message)` | 19: Branch / expression; 19: Branch / outcomes[0].conditions[0].varaible; 19: Branch / outcomes[1].conditions[0].value; 19: Branch / outcomes[1].conditions[0].varaible; 19: Branch / outcomes[2].conditions[0].varaible |
| 2: Configure SMS Event | `$(n2.sms.sender_number)` | 157: Send SMS / destination; 178: Send SMS / destination; 185: Send SMS / destination; 192: Send SMS / destination |
| External/system/custom value; producer not established here | `$(facebook.psid)` | flow-custom-defaults / customVariables[0].value |
| External/system/custom value; producer not established here | `$(wechat.wechat_user_id)` | flow-custom-defaults / customVariables[1].value |
| External/system/custom value; producer not established here | `$(app.deviceId)` | flow-custom-defaults / customVariables[2].value |
| External/system/custom value; producer not established here | `$(app.pushId)` | flow-custom-defaults / customVariables[3].value |
| External/system/custom value; producer not established here | `$(twitter.twitterid)` | flow-custom-defaults / customVariables[4].value |
| External/system/custom value; producer not established here | `$(msisdn)` | flow-custom-defaults / customVariables[5].value |
| External/system/custom value; producer not established here | `$(email)` | flow-custom-defaults / customVariables[6].value |
| External/system/custom value; producer not established here | `$(customerId)` | flow-custom-defaults / customVariables[7].value |
| External/system/custom value; producer not established here | `$(app.imei)` | flow-custom-defaults / customVariables[8].value |
| External/system/custom value; producer not established here | `$(app.os)` | flow-custom-defaults / customVariables[9].value |
| External/system/custom value; producer not established here | `$(app.model)` | flow-custom-defaults / customVariables[10].value |
| External/system/custom value; producer not established here | `$(app.telecom)` | flow-custom-defaults / customVariables[11].value |
| External/system/custom value; producer not established here | `$(app.imsi)` | flow-custom-defaults / customVariables[12].value |
| External/system/custom value; producer not established here | `$(app.location)` | flow-custom-defaults / customVariables[13].value |
| External/system/custom value; producer not established here | `$(app.language)` | flow-custom-defaults / customVariables[14].value |
| External/system/custom value; producer not established here | `$(facebook.birthday)` | flow-custom-defaults / customVariables[15].value |
| External/system/custom value; producer not established here | `$(facebook.email)` | flow-custom-defaults / customVariables[16].value |
| External/system/custom value; producer not established here | `$(facebook.first_name)` | flow-custom-defaults / customVariables[17].value |
| External/system/custom value; producer not established here | `$(facebook.gender)` | flow-custom-defaults / customVariables[18].value |
| External/system/custom value; producer not established here | `$(facebook.last_name)` | flow-custom-defaults / customVariables[19].value |
| External/system/custom value; producer not established here | `$(facebook.location)` | flow-custom-defaults / customVariables[20].value |
| External/system/custom value; producer not established here | `$(facebook.middle_name)` | flow-custom-defaults / customVariables[21].value |
| External/system/custom value; producer not established here | `$(facebook.name)` | flow-custom-defaults / customVariables[22].value |
| External/system/custom value; producer not established here | `$(facebook.timezone)` | flow-custom-defaults / customVariables[23].value |
| External/system/custom value; producer not established here | `$(twitter.username)` | flow-custom-defaults / customVariables[24].value |
| External/system/custom value; producer not established here | `$(app.rtmId)` | flow-custom-defaults / customVariables[25].value |
| External/system/custom value; producer not established here | `$(name)` | flow-custom-defaults / customVariables[26].value |
| External/system/custom value; producer not established here | `$(app.oldlocation)` | flow-custom-defaults / customVariables[27].value |
| External/system/custom value; producer not established here | `$(app.mcc)` | flow-custom-defaults / customVariables[28].value |
| External/system/custom value; producer not established here | `$(app.mnc)` | flow-custom-defaults / customVariables[29].value |
| External/system/custom value; producer not established here | `$(message)` | flow-custom-defaults / customVariables[30].value |
| External/system/custom value; producer not established here | `$(time)` | flow-custom-defaults / customVariables[31].value |
| External/system/custom value; producer not established here | `$(app.message)` | flow-custom-defaults / customVariables[32].value |
| External/system/custom value; producer not established here | `$(sms.message)` | flow-custom-defaults / customVariables[33].value |
| External/system/custom value; producer not established here | `$(twitter.message)` | flow-custom-defaults / customVariables[34].value |
| External/system/custom value; producer not established here | `$(facebook.message)` | flow-custom-defaults / customVariables[35].value |
| External/system/custom value; producer not established here | `$(wechat.message)` | flow-custom-defaults / customVariables[36].value |
| External/system/custom value; producer not established here | `$(app.thread_id)` | flow-custom-defaults / customVariables[37].value |
| External/system/custom value; producer not established here | `$(abc.attachmentCount)` | flow-custom-defaults / customVariables[38].value |
| External/system/custom value; producer not established here | `$(abc.message)` | flow-custom-defaults / customVariables[39].value |
| External/system/custom value; producer not established here | `$(abc.requestIdentifier)` | flow-custom-defaults / customVariables[40].value |
| External/system/custom value; producer not established here | `$(abc.interactive_type)` | flow-custom-defaults / customVariables[41].value |
| External/system/custom value; producer not established here | `$(abc.hasattachment)` | flow-custom-defaults / customVariables[42].value |
| External/system/custom value; producer not established here | `$(abc.abcUserId)` | flow-custom-defaults / customVariables[43].value |

### Boundaries and adaptation

The Beef comparison is captured as `B$(n11.receive.message)` rather than plain B. Correct that expression and each API binding before treating the menu as operational. Several HTTP/send error declarations have no captured route. The sample label Chatbot must not be mistaken for evidence of Studio intents, an LLM or autonomous reasoning.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 71: HTTP request / `onerror` (declared target count 1); 84: HTTP request / `onerror` (declared target count 1); 178: Send SMS / `onerror` (declared target count 1); 185: Send SMS / `onerror` (declared target count 1); 192: Send SMS / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-logistics"></a>

## LogisticsParcelNotifications

Observed 2026-09-08T23:56:52.097Z. [Captured model](../evidence/sample-flows/observed/gallery-logistics.json); [complete graph summary](sample-flows/summaries/gallery-logistics.json). Runtime tested: **no**.

A webhook triggers the delivery SMS, then Receive 4 waits up to 86400 seconds. Branch 5 recognizes CANCEL or CHANGE case-insensitively. CANCEL calls HTTP 15, then sends cancellation confirmation on success or a technical-error message on error. CHANGE asks for an address, waits at Receive 31, echoes that address for confirmation, and waits at Receive 36. YES calls HTTP 41 and sends update confirmation/error; RETRY returns to the address question, making an explicit loop. Other initial answers receive an invalid-response message. Thus the two API actions occur after distinct customer confirmations, rather than merely after sending the first alert.

Useful handoffs: The initial message uses `n2.inboundWebhook.customerName`, `parcelID`, `delievryTime` and `deliveryDate`; recipients use `phoneNumber`. Branches consume `$(n4.receive.message)` and `$(n36.receive.message)`. The proposed address is `$(n31.receive.message)` and is echoed by Send 33 before the YES branch.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Invoke Parcel Notification Flow | onBegin (`onbegin`) → 3: Send Upcoming Delivery Alert |
| 3: Send Upcoming Delivery Alert | onSuccess (`onsuccess`) → 4: Wait for customer response; onError (`onerror`) → End 10 → Error; onPolicyFail (`onpolicyfail`) → End 13 → Error |
| 4: Wait for customer response | sms.mo → 5: Branch as per customer response |
| 5: Branch as per customer response | None of the above → 7: Invalid Customer Response; CHANGE → 9: Ask new delivery address; CANCEL → 15: Call API to Cancel Delivery; onError (`onerror`) → End 80 → Error |
| 6: Send SMS | onSuccess (`onsuccess`) → End 56 → Success |
| 7: Invalid Customer Response | onSuccess (`onsuccess`) → End 73 → Success; onError (`onerror`) → End 75 → Error; onPolicyFail (`onpolicyfail`) → End 78 → Error |
| 9: Ask new delivery address | onSuccess (`onsuccess`) → 31: Wait for updated address; onPolicyFail (`onpolicyfail`) → End 85 → Error; onError (`onerror`) → End 87 → Error |
| 15: Call API to Cancel Delivery | onSuccess (`oncomplete`) → 6: Send SMS; onError (`onerror`) → 59: Error message |
| 31: Wait for updated address | sms.mo → 33: Confirm delivery address |
| 33: Confirm delivery address | onSuccess (`onsuccess`) → 36: Wait for updated address; onPolicyFail (`onpolicyfail`) → End 82 → Error; onError (`onerror`) → End 84 → Error |
| 36: Wait for updated address | sms.mo → 38: Branch as per customer response; onError (`onerror`) → End 11 → Error; onError (`onerror`) → End 32 → Error; onError (`onerror`) → End 37 → Error |
| 38: Branch as per customer response | RETRY → 9: Ask new delivery address; YES → 41: Call API to Change Address; onError (`onerror`) → End 81 → Error |
| 41: Call API to Change Address | onSuccess (`oncomplete`) → 46: Send SMS; onError (`onerror`) → 66: Error message |
| 46: Send SMS | onError (`onerror`) → End 17 → Error; onPolicyFail (`onpolicyfail`) → End 19 → Error; onError (`onerror`) → End 49 → Error; onPolicyFail (`onpolicyfail`) → End 50 → Error; onSuccess (`onsuccess`) → End 53 → Success |
| 59: Error message | No outgoing route captured |
| 66: Error message | onSuccess (`onsuccess`) → End 60 → Success; onError (`onerror`) → End 62 → Error; onPolicyFail (`onpolicyfail`) → End 65 → Error; onError (`onerror`) → End 70 → Error; onPolicyFail (`onpolicyfail`) → End 71 → Error; onSuccess (`onsuccess`) → End 72 → Success |

**Loops in the captured graph:** 9: Ask new delivery address → 31: Wait for updated address → 33: Confirm delivery address → 36: Wait for updated address → 38: Branch as per customer response. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Invoke Parcel Notification Flow | `$(n2.inboundWebhook.customerName)` | 3: Send Upcoming Delivery Alert / message |
| 2: Invoke Parcel Notification Flow | `$(n2.inboundWebhook.parcelID)` | 15: Call API to Cancel Delivery / body.parcelID; 3: Send Upcoming Delivery Alert / message; 41: Call API to Change Address / body.parcelID; 6: Send SMS / message |
| 2: Invoke Parcel Notification Flow | `$(n2.inboundWebhook.delievryTime)` | 3: Send Upcoming Delivery Alert / message |
| 2: Invoke Parcel Notification Flow | `$(n2.inboundWebhook.deliveryDate)` | 3: Send Upcoming Delivery Alert / message |
| 2: Invoke Parcel Notification Flow | `$(n2.inboundWebhook.phoneNumber)` | 33: Confirm delivery address / destination; 3: Send Upcoming Delivery Alert / destination; 46: Send SMS / destination; 59: Error message / destination; 66: Error message / destination; 6: Send SMS / destination; 7: Invalid Customer Response / destination; 9: Ask new delivery address / destination |
| 4: Wait for customer response | `$(n4.receive.message)` | 5: Branch as per customer response / expression; 5: Branch as per customer response / outcomes[0].conditions[0].varaible; 5: Branch as per customer response / outcomes[1].conditions[0].varaible |
| 31: Wait for updated address | `$(n31.receive.message)` | 33: Confirm delivery address / message |
| 36: Wait for updated address | `$(n36.receive.message)` | 38: Branch as per customer response / expression; 38: Branch as per customer response / outcomes[0].conditions[0].varaible; 38: Branch as per customer response / outcomes[1].conditions[0].varaible; 41: Call API to Change Address / body.newAddress |

### Boundaries and adaptation

The initial webhook parse schema and business URLs are not operationally populated in this capture. Preserve the misspelled observed `delievryTime` only when matching the actual trigger schema. Several Receive failure/timeout declarations have no captured destination, and the RETRY cycle has no explicit attempt counter. Confirm API body bindings and recovery policy before reuse; customer-facing success text is not delivery/API execution evidence.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 4: Wait for customer response / `ontimeout` (declared target count 1); 4: Wait for customer response / `onerror` (declared target count 1); 6: Send SMS / `onerror` (declared target count 1); 31: Wait for updated address / `ontimeout` (declared target count 1); 31: Wait for updated address / `onerror` (declared target count 1); 36: Wait for updated address / `ontimeout` (declared target count 1); 59: Error message / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-sms-survey"></a>

## SMSSurvey

Observed 2026-09-08T23:57:36.392Z. [Captured model](../evidence/sample-flows/observed/gallery-sms-survey.json); [complete graph summary](sample-flows/summaries/gallery-sms-survey.json). Runtime tested: **no**.

Webhook Start 2 sends the survey through SMS 122, then Receive 11 waits 600 seconds for an SMS reply. Branch 22 accepts values 1 through 5 and sends the thank-you message. Any other answer goes through correction SMS 143 and back to Receive 11, creating the observed retry loop. There is no captured persistence/API node to store the rating and no explicit attempt counter in the loop.

Useful handoffs: The prompt uses `$(name)` and all SMS destinations use `$(number)`. Branch 22 evaluates `$(n11.receive.message)` against numeric choices 1–5. The custom-variable defaults are preserved, but a source for number is not established by the captured Start configuration.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Webhook | onbegin → 122: Send SMS |
| 11: Receive | sms.mo → 22: Branch; onerror → End 57 → ; ontimeout → End 65 →  |
| 22: Branch | Valid Response → 150: Send SMS; None of the above → 143: Send SMS; onerror → End 71 →  |
| 122: Send SMS | onsuccess → 11: Receive; onerror → End 134 → Error; onpolicyfail → End 141 → Incomplete; onerror → End 158 → Error; onpolicyfail → End 159 → Incomplete; onerror → End 166 → Error; onpolicyfail → End 167 → Incomplete |
| 143: Send SMS | onsuccess → 11: Receive |
| 150: Send SMS | No outgoing route captured |

**Loops in the captured graph:** 11: Receive → 22: Branch → 143: Send SMS. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 11: Receive | `$(n11.receive.message)` | 22: Branch / expression; 22: Branch / outcomes[0].conditions[0].varaible; 22: Branch / outcomes[0].conditions[1].varaible; 22: Branch / outcomes[0].conditions[2].varaible; 22: Branch / outcomes[0].conditions[3].varaible; 22: Branch / outcomes[0].conditions[4].varaible |
| External/system/custom value; producer not established here | `$(name)` | 122: Send SMS / message; flow-custom-defaults / customVariables[26].value |
| External/system/custom value; producer not established here | `$(number)` | 122: Send SMS / destination; 143: Send SMS / destination; 150: Send SMS / destination |
| External/system/custom value; producer not established here | `$(facebook.psid)` | flow-custom-defaults / customVariables[0].value |
| External/system/custom value; producer not established here | `$(wechat.wechat_user_id)` | flow-custom-defaults / customVariables[1].value |
| External/system/custom value; producer not established here | `$(app.deviceId)` | flow-custom-defaults / customVariables[2].value |
| External/system/custom value; producer not established here | `$(app.pushId)` | flow-custom-defaults / customVariables[3].value |
| External/system/custom value; producer not established here | `$(twitter.twitterid)` | flow-custom-defaults / customVariables[4].value |
| External/system/custom value; producer not established here | `$(msisdn)` | flow-custom-defaults / customVariables[5].value |
| External/system/custom value; producer not established here | `$(email)` | flow-custom-defaults / customVariables[6].value |
| External/system/custom value; producer not established here | `$(customerId)` | flow-custom-defaults / customVariables[7].value |
| External/system/custom value; producer not established here | `$(app.imei)` | flow-custom-defaults / customVariables[8].value |
| External/system/custom value; producer not established here | `$(app.os)` | flow-custom-defaults / customVariables[9].value |
| External/system/custom value; producer not established here | `$(app.model)` | flow-custom-defaults / customVariables[10].value |
| External/system/custom value; producer not established here | `$(app.telecom)` | flow-custom-defaults / customVariables[11].value |
| External/system/custom value; producer not established here | `$(app.imsi)` | flow-custom-defaults / customVariables[12].value |
| External/system/custom value; producer not established here | `$(app.location)` | flow-custom-defaults / customVariables[13].value |
| External/system/custom value; producer not established here | `$(app.language)` | flow-custom-defaults / customVariables[14].value |
| External/system/custom value; producer not established here | `$(facebook.birthday)` | flow-custom-defaults / customVariables[15].value |
| External/system/custom value; producer not established here | `$(facebook.email)` | flow-custom-defaults / customVariables[16].value |
| External/system/custom value; producer not established here | `$(facebook.first_name)` | flow-custom-defaults / customVariables[17].value |
| External/system/custom value; producer not established here | `$(facebook.gender)` | flow-custom-defaults / customVariables[18].value |
| External/system/custom value; producer not established here | `$(facebook.last_name)` | flow-custom-defaults / customVariables[19].value |
| External/system/custom value; producer not established here | `$(facebook.location)` | flow-custom-defaults / customVariables[20].value |
| External/system/custom value; producer not established here | `$(facebook.middle_name)` | flow-custom-defaults / customVariables[21].value |
| External/system/custom value; producer not established here | `$(facebook.name)` | flow-custom-defaults / customVariables[22].value |
| External/system/custom value; producer not established here | `$(facebook.timezone)` | flow-custom-defaults / customVariables[23].value |
| External/system/custom value; producer not established here | `$(twitter.username)` | flow-custom-defaults / customVariables[24].value |
| External/system/custom value; producer not established here | `$(app.rtmId)` | flow-custom-defaults / customVariables[25].value |
| External/system/custom value; producer not established here | `$(app.oldlocation)` | flow-custom-defaults / customVariables[27].value |
| External/system/custom value; producer not established here | `$(app.mcc)` | flow-custom-defaults / customVariables[28].value |
| External/system/custom value; producer not established here | `$(app.mnc)` | flow-custom-defaults / customVariables[29].value |
| External/system/custom value; producer not established here | `$(message)` | flow-custom-defaults / customVariables[30].value |
| External/system/custom value; producer not established here | `$(time)` | flow-custom-defaults / customVariables[31].value |
| External/system/custom value; producer not established here | `$(app.message)` | flow-custom-defaults / customVariables[32].value |
| External/system/custom value; producer not established here | `$(sms.message)` | flow-custom-defaults / customVariables[33].value |
| External/system/custom value; producer not established here | `$(twitter.message)` | flow-custom-defaults / customVariables[34].value |
| External/system/custom value; producer not established here | `$(facebook.message)` | flow-custom-defaults / customVariables[35].value |
| External/system/custom value; producer not established here | `$(wechat.message)` | flow-custom-defaults / customVariables[36].value |
| External/system/custom value; producer not established here | `$(app.thread_id)` | flow-custom-defaults / customVariables[37].value |
| External/system/custom value; producer not established here | `$(abc.attachmentCount)` | flow-custom-defaults / customVariables[38].value |
| External/system/custom value; producer not established here | `$(abc.message)` | flow-custom-defaults / customVariables[39].value |
| External/system/custom value; producer not established here | `$(abc.requestIdentifier)` | flow-custom-defaults / customVariables[40].value |
| External/system/custom value; producer not established here | `$(abc.interactive_type)` | flow-custom-defaults / customVariables[41].value |
| External/system/custom value; producer not established here | `$(abc.hasattachment)` | flow-custom-defaults / customVariables[42].value |
| External/system/custom value; producer not established here | `$(abc.abcUserId)` | flow-custom-defaults / customVariables[43].value |

### Boundaries and adaptation

The correction message asks for 1–10 while the initial question and branch accept only 1–5. Reconcile this concrete inconsistency before adapting the sample. Some send-error declarations lack captured routes. A thank-you send proves neither storage nor a measured response rate, and no messages were sent during inspection.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 143: Send SMS / `onerror` (declared target count 1); 150: Send SMS / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-track-package"></a>

## AI Agent Fulfilment - Track Package

Observed 2026-09-09T00:09:50.634Z. [Captured model](../evidence/sample-flows/observed/gallery-track-package.json); [complete graph summary](sample-flows/summaries/gallery-track-package.json). Runtime tested: **no**.

The AI Agent event enters Start 2, then its onBegin edge invokes HTTP Request 3. The HTTP node performs GET against the sample tracking path and extracts the complete JSON body under fullResp. Its End bindings associate internal oncomplete (rendered onSuccess) with Success, onerror with Error, and ontimeout with Incomplete. The flow-settings Last Execution Status entry contains an agent-facing response object. This is a fulfillment adapter: the agent supplies a package identifier, Connect calls the business API, and flow outcome configuration returns data; there is no Send or Receive node in this graph.

Useful handoffs: Start output `$(n2.aiAgent.packageNum)` becomes `/track/$(n2.aiAgent.packageNum)` in the HTTP URL. HTTP JSON path `$` maps to `n3.fullResp`; `$(n3.fullResp)` is used by the on-leave log and notification custompayload.response. The custom response also carries `$(transid)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 4 → Success; onError (`onerror`) → End 6 → Error; onTimeout (`ontimeout`) → End 9 → Incomplete |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.packageNum)` | 3: HTTP Request / url |
| 3: HTTP Request | `$(n3.fullResp)` | 3: HTTP Request / transition_actions[0].value; flow-settings / outcome[1].notification.custompayload.response |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.payload.serviceName |

### Boundaries and adaptation

The configured example marks packageNum nonmandatory and includes embedded historical response data. Those examples are not a successful current API response. URL hosts/header values are redacted. The same response variable is referenced by the all-status outcome configuration, so validate what is available on failure before adapting the return contract. No loop or retry is captured.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="gallery-webhook-sms"></a>

## WebhooktoSMSalerts

Observed 2026-09-08T23:57:29.390Z. [Captured model](../evidence/sample-flows/observed/gallery-webhook-sms.json); [complete graph summary](sample-flows/summaries/gallery-webhook-sms.json). Runtime tested: **no**.

This is the smallest event-to-message adapter: Webhook Start 2 connects directly to SMS 3 through onBegin. The send's terminal behavior and flow outcome settings remain in the complete graph summary. There is no conversation loop, business API call, data parser, schedule or reply wait.

Useful handoffs: SMS destination is `$(n2.inboundWebhook.phone)` and message is `$(n2.inboundWebhook.alertdesc)`. Both depend on the webhook's eventual payload/schema binding; there is no intermediate custom-variable transformation.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Webhook | onBegin (`onbegin`) → 3: SMS |
| 3: SMS | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Webhook | `$(n2.inboundWebhook.alertdesc)` | 3: SMS / message |
| 2: Configure Webhook | `$(n2.inboundWebhook.phone)` | 3: SMS / destination |

### Boundaries and adaptation

The captured Webhook configuration has empty parseOutput/jsonData and no configured URL. It illustrates the intended field contract but does not establish an installed webhook. SMS onerror declares a target but no corresponding captured edge/End binding is present. Provision sender/assets and define failure behavior before using the pattern.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: SMS / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-block-card-and-order-replacement"></a>

## Block card and order replacement.workflow

Observed 2026-09-09T00:00:54.162Z. [Captured model](../evidence/sample-flows/observed/native-block-card-and-order-replacement.json); [complete graph summary](sample-flows/summaries/native-block-card-and-order-replacement.json). Runtime tested: **no**.

AI Agent Start 2 receives optional string `customer_id` and `order_replacement`, then `onbegin`/rendered `onBegin` enters HTTP Request 6. It posts to `/block_card`. End pseudo-node 15 belongs to node 6 through `data.parentNode=6` and `params.nodeEvent=oncomplete`, rendered `onSuccess`; that terminal association exists without a separate edge record. There is one backend operation, not separate block and replacement-order nodes.

Useful handoffs: The HTTP body renames `$(n2.aiAgent.customer_id)` to `user_id` and passes `$(n2.aiAgent.order_replacement)` as `order_replacement`. Connection/request timeout fields both contain 10000. Response paths `$.replacement_card` and `$.status` become `n6.replacement_card` and `n6.status`. The all-status Last Execution Status outcome stores custom return fields `status=$(n6.status)` and `replacement_card=$(n6.replacement_card)`; it does not return the HTTP status code.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 6: HTTP Request |
| 6: HTTP Request | onSuccess (`oncomplete`) → End 15 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.customer_id)` | 6: HTTP Request / body.user_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.order_replacement)` | 6: HTTP Request / body.order_replacement |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.payload.serviceName |
| 6: HTTP Request | `$(n6.status)` | flow-settings / outcome[1].notification.custompayload.status |
| 6: HTTP Request | `$(n6.replacement_card)` | flow-settings / outcome[1].notification.custompayload.replacement_card |

### Boundaries and adaptation

No explicit HTTP error edge, retry, reconciliation lookup, or conditional second operation appears. The saved response example describes a card block without a replacement, but is not a current execution result. Any meaning of order_replacement values and backend write safety requires the actual endpoint contract. Hosts and headers are redacted. The internal model is not a public import schema and runtime testing is explicitly false; no card or replacement order was changed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 6: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-cancel-appointment"></a>

## cancel_appointment.workflow

Observed 2026-09-08T23:59:56.277Z. [Captured model](../evidence/sample-flows/observed/native-cancel-appointment.json); [complete graph summary](sample-flows/summaries/native-cancel-appointment.json). Runtime tested: **no**.

Start 2 receives an AI Agent event whose parsed input is optional string `appointment_number`. Its `onbegin` event, rendered `onBegin`, enters HTTP Request 3, which posts to the sanitized `/cancel_appointment` endpoint. That is the complete connected operational sequence in the capture. HTTP declares `oncomplete` and `onerror`, but neither has an explicit outgoing graph edge to another processing node.

Useful handoffs: HTTP body `$(n2.aiAgent.payload)` forwards the whole incoming action payload. The Last Execution Status outcome is configured to notify for all status codes, returning transaction, flow, and service identifiers plus `httpStatus=$(n3.http.statusCode)` and `httpResponse=$(n3.http.responseBody)`. The payload therefore preserves the backend's status and body rather than manufacturing a cancellation confirmation. No appointment-number rewrite or cancellation-status extraction is visible.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.payload)` | 3: HTTP Request / body |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname; flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName; flow-settings / outcome[1].notification.payload.serviceName |
| 3: HTTP Request | `$(n3.http.statusCode)` | flow-settings / outcome[1].notification.custompayload.httpStatus |
| 3: HTTP Request | `$(n3.http.responseBody)` | flow-settings / outcome[1].notification.custompayload.httpResponse |

### Boundaries and adaptation

A cancellation request is configured; successful cancellation was not executed or established. There is no visible confirmation branch, duplicate-write protection, retry loop, reconciliation lookup, or customer notification step. The declared input type is string although its embedded example value is numeric; consumers should preserve that observed discrepancy when adapting the contract. Hosts and headers are redacted. The internal model is not an importable public schema, and its `runtime_tested=false` limits this account to configuration evidence.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `oncomplete` (declared target count 1); 3: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-cancel-booking"></a>

## cancel_booking.workflow

Observed 2026-09-09T00:01:47.372Z. [Captured model](../evidence/sample-flows/observed/native-cancel-booking.json); [complete graph summary](sample-flows/summaries/native-cancel-booking.json). Runtime tested: **no**.

AI Agent Start 2 exposes optional strings `booking_id`, `reason`, and `flight_id`. Its internal `onbegin`, rendered `onBegin`, enters HTTP 3 POST `/cancel_flight`. Two End pseudo-nodes refer back to HTTP 3: node 9 binds `oncomplete`/rendered `onSuccess` with exitResult 2, and node 10 binds `onerror`/`onError` with exitResult 3. These terminal relationships are stored through parentNode and nodeEvent rather than ordinary edge records.

Useful handoffs: The HTTP body maps each input explicitly: `booking_id=$(n2.aiAgent.booking_id)`, `flight_id=$(n2.aiAgent.flight_id)`, and `reason=$(n2.aiAgent.reason)`. Both timeout fields contain 10000. Response extraction maps `$.booking.booking_id` to `n3.booking_id`, `$.message` to `n3.message`, and `$.error` to `n3.error`. The all-status Last Execution Status notification uses payloadType 1 and stores those three outputs with `transactionID=$(transid)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 9 → Success; onError (`onerror`) → End 10 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.booking_id)` | 3: HTTP Request / body.booking_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.flight_id)` | 3: HTTP Request / body.flight_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.reason)` | 3: HTTP Request / body.reason |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| 3: HTTP Request | `$(n3.message)` | flow-settings / outcome[1].notification.payload.message |
| 3: HTTP Request | `$(n3.booking_id)` | flow-settings / outcome[1].notification.payload.booking_id |
| 3: HTTP Request | `$(n3.error)` | flow-settings / outcome[1].notification.payload.error |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName |

### Boundaries and adaptation

No refund calculation, confirmation step, retry loop, or follow-up booking lookup is visible. The two identifiers are incoming dependencies; this graph does not call the flight-info sample to obtain them. Error termination is configured but no error-specific replacement payload is shown if extraction fails. Hosts/headers are redacted, sample response data is not current cancellation evidence, and this internal model is not a public import schema. Runtime testing is false; no booking was cancelled.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-cancel-checkin"></a>

## cancel_checkin.workflow

Observed 2026-09-09T00:01:50.901Z. [Captured model](../evidence/sample-flows/observed/native-cancel-checkin.json); [complete graph summary](sample-flows/summaries/native-cancel-checkin.json). Runtime tested: **no**.

AI Agent Start 2 declares optional string `booking_id`, `notes`, and `last_name`. Its `onbegin`/rendered `onBegin` reaches HTTP 3 POST `/cancel_check_in`. End pseudo-nodes 9, 10, and 13 belong to HTTP 3: `oncomplete`/`onSuccess` has exitResult 2, while `onerror`/`onError` and `ontimeout`/`onTimeout` both have exitResult 3. The timeout terminal is present even though the HTTP children list only completion and error events.

Useful handoffs: The request preserves `booking_id=$(n2.aiAgent.booking_id)` and `last_name=$(n2.aiAgent.last_name)`, but renames `$(n2.aiAgent.notes)` to body field `reason`. Connection/request timeouts are 10000. Response `$.booking.check_in_notes` is named `n3.reason`, with `$.message` and `$.error` extracted separately. The all-status Last Execution Status payload, with payloadType 1, returns transactionID, `$(n3.message)`, `$(n3.reason)`, and `$(n3.error)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 9 → Success; onError (`onerror`) → End 10 → Error; onTimeout (`ontimeout`) → End 13 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.booking_id)` | 3: HTTP Request / body.booking_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.last_name)` | 3: HTTP Request / body.last_name |
| 2: Configure AI Agent Event | `$(n2.aiAgent.notes)` | 3: HTTP Request / body.reason |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| 3: HTTP Request | `$(n3.message)` | flow-settings / outcome[1].notification.payload.message |
| 3: HTTP Request | `$(n3.reason)` | flow-settings / outcome[1].notification.payload.reason |
| 3: HTTP Request | `$(n3.error)` | flow-settings / outcome[1].notification.payload.error |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName |

### Boundaries and adaptation

This is check-in cancellation, not cancellation of the flight booking itself. No loop, confirmation lookup, channel notification, or direct connection to another sample exists. Incoming notes and returned reason have different source paths despite their related meaning. Stored names and booking examples are fixtures. Headers and hosts are redacted; the internal model is not an importable public schema. Runtime testing is false, so neither the write nor timeout response behavior was exercised.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-check-availability"></a>

## check_availability.workflow

Observed 2026-09-08T23:59:30.439Z. [Captured model](../evidence/sample-flows/observed/native-check-availability.json); [complete graph summary](sample-flows/summaries/native-check-availability.json). Runtime tested: **no**.

Start 2 is an AI Agent event with optional string inputs `preferred_period` and `preferred_date`. Its internal `onbegin` event, rendered `onBegin`, leads directly to HTTP Request 3. The request posts to the sanitized `/check_availability` path. There is no parser, availability-selection branch, or second operation between the incoming action and the backend call. HTTP declares `oncomplete` and `onerror`; the captured model has no explicit outgoing edges from that node.

Useful handoffs: The request body is the whole `$(n2.aiAgent.payload)`, not a newly constructed object using the individual parsed fields. The notifying Last Execution Status outcome applies to all status codes and maps `httpStatus` from `$(n3.http.statusCode)` and `httpResponse` from `$(n3.http.responseBody)`, alongside transaction, flow, and service identifiers. This makes the observed sample a backend response pass-through; no normalization of dates, periods, or available-slot results is configured.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.payload)` | 3: HTTP Request / body |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname; flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName; flow-settings / outcome[1].notification.payload.serviceName |
| 3: HTTP Request | `$(n3.http.statusCode)` | flow-settings / outcome[1].notification.custompayload.httpStatus |
| 3: HTTP Request | `$(n3.http.responseBody)` | flow-settings / outcome[1].notification.custompayload.httpResponse |

### Boundaries and adaptation

The configured example date/period are fixtures, not available appointments. No retry loop, explicit request timeout, business-result check, SMS/email send, or cross-flow call appears. The backend host and header values are redacted. This internal canvas model is evidence rather than a public import schema; `runtime_tested` is false, so neither backend availability nor an agent's interpretation of the returned result was verified.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `oncomplete` (declared target count 1); 3: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-checkin"></a>

## checkin.workflow

Observed 2026-09-09T00:01:54.153Z. [Captured model](../evidence/sample-flows/observed/native-checkin.json); [complete graph summary](sample-flows/summaries/native-checkin.json). Runtime tested: **no**.

AI Agent Start 2 exposes optional string `booking_id`, `notes`, and `last_name`, then `onbegin`/rendered `onBegin` enters HTTP 3 POST `/check_in`. End pseudo-nodes associate with HTTP 3 through parentNode and nodeEvent: node 9 terminates `oncomplete`/`onSuccess` with exitResult 2, node 10 terminates `onerror`/`onError` with 3, and node 13 terminates `ontimeout`/`onTimeout` with 4. The graph has no retry return edge.

Useful handoffs: HTTP body uses `booking_id=$(n2.aiAgent.booking_id)`, `last_name=$(n2.aiAgent.last_name)`, and `notes=$(n2.aiAgent.notes)`. Both timeout fields contain 10000. JSONPath `$.booking.check_in_notes` becomes output `n3.notes`; `$.message` and `$.error` become their corresponding n3 outputs. The all-status Last Execution Status notification stores payloadType 1 and returns transactionID, message, error, and notes through those outputs. It does not create a boarding-pass response or independently retrieve flight details.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 9 → Success; onError (`onerror`) → End 10 → Error; onTimeout (`ontimeout`) → End 13 → Incomplete |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.booking_id)` | 3: HTTP Request / body.booking_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.last_name)` | 3: HTTP Request / body.last_name |
| 2: Configure AI Agent Event | `$(n2.aiAgent.notes)` | 3: HTTP Request / body.notes |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| 3: HTTP Request | `$(n3.message)` | flow-settings / outcome[1].notification.payload.message |
| 3: HTTP Request | `$(n3.error)` | flow-settings / outcome[1].notification.payload.error |
| 3: HTTP Request | `$(n3.notes)` | flow-settings / outcome[1].notification.payload.notes |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName |

### Boundaries and adaptation

The check-in action and its error/timeout terminal configuration were inspected without execution. Embedded booking/name/notes examples are fixtures, and a stored success message does not prove a completed check-in. No explicit business-status branch, duplicate-write safeguard, reconciliation operation, or SMS/email send appears. Hosts and header values are redacted. This internal canvas representation is evidence rather than a public import schema; `runtime_tested=false` applies to all paths.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-create-appointment"></a>

## create_appointment.workflow

Observed 2026-09-09T00:00:34.955Z. [Captured model](../evidence/sample-flows/observed/native-create-appointment.json); [complete graph summary](sample-flows/summaries/native-create-appointment.json). Runtime tested: **no**.

AI Agent Start 2 declares optional string inputs `reason`, `date_of_birth`, `patient_name`, and `time_slot`. Its internal `onbegin`, rendered `onBegin`, connects to HTTP Request 3. The request posts to the sanitized `/create_appointment` path. There is no intervening slot lookup, user-confirmation node, or second write: the sample delegates booking behavior to that endpoint.

Useful handoffs: HTTP body `$(n2.aiAgent.payload)` forwards the complete incoming action payload. It does not reconstruct the body from the four separately exposed variables. The notifying Last Execution Status outcome covers all status codes and stores a custom payload with transaction, flow, and service identifiers, `httpStatus=$(n3.http.statusCode)`, and `httpResponse=$(n3.http.responseBody)`. No response-field extraction or appointment-ID assignment appears; any booking identifier must remain inside the returned HTTP body.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.payload)` | 3: HTTP Request / body |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname; flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName; flow-settings / outcome[1].notification.payload.serviceName |
| 3: HTTP Request | `$(n3.http.statusCode)` | flow-settings / outcome[1].notification.custompayload.httpStatus |
| 3: HTTP Request | `$(n3.http.responseBody)` | flow-settings / outcome[1].notification.custompayload.httpResponse |

### Boundaries and adaptation

The observed model has only the Start-to-HTTP edge, no retry loop, explicit request timeout, idempotency key, or compensating cancellation. Example names, dates, and reasons are sample fixtures. No SMS/email confirmation is sent by this graph. Header values and hosts are redacted. The internal canvas representation is not a public import schema, and `runtime_tested=false` means neither creation nor the returned booking contract was verified by execution.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `oncomplete` (declared target count 1); 3: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-fetch-account-balance"></a>

## Fetch account balance.workflow

Observed 2026-09-09T00:01:01.220Z. [Captured model](../evidence/sample-flows/observed/native-fetch-account-balance.json); [complete graph summary](sample-flows/summaries/native-fetch-account-balance.json). Runtime tested: **no**.

AI Agent Start 2 takes optional string `customer_id` and enters HTTP 3 through `onbegin`/`onBegin`. HTTP GET `/get_balance/$(n2.aiAgent.customer_id)` uses connection/request timeout values 10000. Its internal `oncomplete`, rendered `onSuccess`, leads to Branch 5. Status code 200 chooses `user found` and Evaluate 7; the fallback `user not found` goes to Evaluate 8.

Useful handoffs: HTTP extracts `$.account_balance` and `$.status`. Evaluate 7 has constant expression 1, but its on-enter session actions perform the useful transformation: set `status=success`, `balance=$(n3.account_balance)`, and a success message. Evaluate 8 assigns `status=failure` and a not-found message. Last Execution Status uses `payloadType=1` and stores `payload` fields transactionID, `$(status)`, `$(balance)`, and `$(message)`. Its separate custompayload instead mentions transactions; that alternate stored object should not be silently treated as the balance contract.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → 5: Branch |
| 5: Branch | user found → 7: Evaluate; user not found → 8: Evaluate |
| 7: Evaluate | No outgoing route captured |
| 8: Evaluate | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.customer_id)` | 3: HTTP Request / url |
| 3: HTTP Request | `$(n3.http.statusCode)` | 5: Branch / expression; 5: Branch / outcomes[0].conditions[0].varaible |
| 3: HTTP Request | `$(n3.account_balance)` | 7: Evaluate / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload; flow-settings / outcome[1].notification.payload.transactionID |
| custom variable; writers 7: Evaluate, 8: Evaluate | `$(status)` | flow-settings / outcome[1].notification.custompayload; flow-settings / outcome[1].notification.payload.status |
| custom variable; writers 7: Evaluate | `$(balance)` | flow-settings / outcome[1].notification.payload.balance |
| custom variable; writers 7: Evaluate, 8: Evaluate | `$(message)` | flow-settings / outcome[1].notification.custompayload; flow-settings / outcome[1].notification.payload.message |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload |
| External/system/custom value; producer not established here | `$(transactions)` | flow-settings / outcome[1].notification.custompayload |

### Boundaries and adaptation

The HTTP onerror port has no explicit recovery edge, so it does not necessarily pass through the not-found assignment. The branch classifies all non-200 completed responses as not found; it does not inspect body semantics. No retry, channel send, or other flow call appears. Embedded `isTestExecuted=true` and response examples belong to the template, not this inspection. Hosts/headers are redacted, the model is internal rather than an import schema, and `runtime_tested=false`.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `onerror` (declared target count 1); 5: Branch / `onerror` (declared target count None); 7: Evaluate / `oninvalidchoice` (declared target count 1); 7: Evaluate / `onerror` (declared target count 1); 8: Evaluate / `oninvalidchoice` (declared target count 1); 8: Evaluate / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-fetch-recent-transactions"></a>

## Fetch Recent Transactions.workflow

Observed 2026-09-09T00:00:57.584Z. [Captured model](../evidence/sample-flows/observed/native-fetch-recent-transactions.json); [complete graph summary](sample-flows/summaries/native-fetch-recent-transactions.json). Runtime tested: **no**.

AI Agent Start 2 supplies `customer_id` to HTTP 3 GET `/get_transactions/$(n2.aiAgent.customer_id)`. Start `onbegin` renders as `onBegin`; HTTP `oncomplete` renders as `onSuccess` and connects to Branch 5. HTTP status 200 selects `user found` → Evaluate 7; every other completed status selects `user not found` → Evaluate 8. No pagination or per-transaction loop is present.

Useful handoffs: HTTP extraction names `last_transactions` from JSONPath `$`, the whole response, rather than `$.last_transactions`; it also extracts `$.status`. Evaluate 7 on-enter actions assign `status=success`, `transactions=$(n3.last_transactions)`, and a success message. Evaluate 8 assigns failure status/message. The outcome has `payloadType=1`: its payload returns `status=$(n3.status)` and `transactions=$(n3.last_transactions)` directly, plus transactionID and `$(message)`. A distinct custompayload references session `$(status)` and unquoted `$(transactions)`. Thus the stored payload bypasses two session assignments and preserves the response wrapper.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → 5: Branch |
| 5: Branch | user found → 7: Evaluate; user not found → 8: Evaluate |
| 7: Evaluate | No outgoing route captured |
| 8: Evaluate | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.customer_id)` | 3: HTTP Request / url |
| 3: HTTP Request | `$(n3.http.statusCode)` | 5: Branch / expression; 5: Branch / outcomes[0].conditions[0].varaible |
| 3: HTTP Request | `$(n3.last_transactions)` | 7: Evaluate / transition_actions[1].value; flow-settings / outcome[1].notification.payload.transactions |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload; flow-settings / outcome[1].notification.payload.transactionID |
| 3: HTTP Request | `$(n3.status)` | flow-settings / outcome[1].notification.payload.status |
| custom variable; writers 7: Evaluate, 8: Evaluate | `$(message)` | flow-settings / outcome[1].notification.custompayload; flow-settings / outcome[1].notification.payload.message |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload |
| custom variable; writers 7: Evaluate, 8: Evaluate | `$(status)` | flow-settings / outcome[1].notification.custompayload |
| custom variable; writers 7: Evaluate | `$(transactions)` | flow-settings / outcome[1].notification.custompayload |

### Boundaries and adaptation

HTTP errors have no explicit recovery edge; the non-200 branch is not a general transport-failure handler. No retry, dispute-registration call, or customer message is configured. Embedded transaction examples and Evaluate test flags are historical template data, not observed account activity or a current test. Hosts and headers are redacted. This internal model is not an import schema; `runtime_tested=false` leaves response serialization and agent interpretation unverified.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `onerror` (declared target count 1); 5: Branch / `onerror` (declared target count None); 7: Evaluate / `oninvalidchoice` (declared target count 1); 7: Evaluate / `onerror` (declared target count 1); 8: Evaluate / `oninvalidchoice` (declared target count 1); 8: Evaluate / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-get-flight-info"></a>

## get_flight_info.workflow

Observed 2026-09-09T00:02:04.734Z. [Captured model](../evidence/sample-flows/observed/native-get-flight-info.json); [complete graph summary](sample-flows/summaries/native-get-flight-info.json). Runtime tested: **no**.

AI Agent Start 2 takes optional string `booking_id` and `last_name`. Its `onbegin`/rendered `onBegin` enters HTTP 3 GET `/get_booking_info?booking_id=$(n2.aiAgent.booking_id)&last_name=$(n2.aiAgent.last_name)`. Connection/request timeout values are 10000. End pseudo-node 12 binds HTTP `oncomplete`/`onSuccess` with exitResult 2; node 13 binds `onerror`/`onError` with 3. No downstream booking modification occurs.

Useful handoffs: HTTP extracts fields from `$.booking`: arrival/departure times, flight number, origin/destination, booking status, flight_id, booking_id, flight status, and check_in_status. It renames `$.booking.user_name` to `n3.passenger_name` and extracts top-level `$.error`. The all-status Last Execution Status outcome has payloadType 2 and stores a custompayload with transactionID plus these named n3 outputs. The returned booking_id and flight_id are useful inputs for later actions, but no native edge or Call Workflow invokes those actions here.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 12 → Success; onError (`onerror`) → End 13 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.booking_id)` | 3: HTTP Request / url |
| 2: Configure AI Agent Event | `$(n2.aiAgent.last_name)` | 3: HTTP Request / url |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.payload.serviceName |
| 3: HTTP Request | `$(n3.passenger_name)` | flow-settings / outcome[1].notification.custompayload.passenger_name |
| 3: HTTP Request | `$(n3.arrival_time)` | flow-settings / outcome[1].notification.custompayload.arrival_time |
| 3: HTTP Request | `$(n3.flight_number)` | flow-settings / outcome[1].notification.custompayload.flight_number |
| 3: HTTP Request | `$(n3.origin)` | flow-settings / outcome[1].notification.custompayload.origin |
| 3: HTTP Request | `$(n3.destination)` | flow-settings / outcome[1].notification.custompayload.destination |
| 3: HTTP Request | `$(n3.booking_status)` | flow-settings / outcome[1].notification.custompayload.booking_status |
| 3: HTTP Request | `$(n3.flight_id)` | flow-settings / outcome[1].notification.custompayload.flight_id |
| 3: HTTP Request | `$(n3.booking_id)` | flow-settings / outcome[1].notification.custompayload.booking_id |
| 3: HTTP Request | `$(n3.flight_status)` | flow-settings / outcome[1].notification.custompayload.flight_status |
| 3: HTTP Request | `$(n3.check_in_status)` | flow-settings / outcome[1].notification.custompayload.check_in_status |
| 3: HTTP Request | `$(n3.departure_time)` | flow-settings / outcome[1].notification.custompayload.departure_time |
| 3: HTTP Request | `$(n3.error)` | flow-settings / outcome[1].notification.custompayload.error |

### Boundaries and adaptation

There is no explicit URL-encoding transformation, no-result branch, retry, or separate timeout pseudo-node. The graph maps configured response paths without proving their presence on every response. Sample booking details are not live travel records, and the lookup does not establish an identity-assurance policy. The host is redacted; the internal model is not a public import schema. Runtime testing is false, so no lookup or response serialization was exercised.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-lookup-appointment"></a>

## lookup_appointment.workflow

Observed 2026-09-09T00:00:38.393Z. [Captured model](../evidence/sample-flows/observed/native-lookup-appointment.json); [complete graph summary](sample-flows/summaries/native-lookup-appointment.json). Runtime tested: **no**.

AI Agent Start 2 declares optional string inputs `date_of_birth` and `patient_name`. Its `onbegin` event, rendered `onBegin`, enters HTTP Request 3, which posts to the sanitized `/lookup_appointment` endpoint. The graph contains no additional branch for no appointment, multiple appointments, or a later cancellation; those are not recoverable from the filename or the two-node sequence.

Useful handoffs: The whole `$(n2.aiAgent.payload)` is the HTTP body. No name normalization, date conversion, or field-by-field request mapping is configured. The Last Execution Status outcome notifies for all status codes and stores transaction, flow, and service identifiers together with `httpStatus=$(n3.http.statusCode)` and `httpResponse=$(n3.http.responseBody)`. The backend body is preserved instead of being reduced to a selected appointment, making its result schema a separate integration dependency.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.payload)` | 3: HTTP Request / body |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname; flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName; flow-settings / outcome[1].notification.payload.serviceName |
| 3: HTTP Request | `$(n3.http.statusCode)` | flow-settings / outcome[1].notification.custompayload.httpStatus |
| 3: HTTP Request | `$(n3.http.responseBody)` | flow-settings / outcome[1].notification.custompayload.httpResponse |

### Boundaries and adaptation

The HTTP node has no explicit outgoing edge to another operational node, no visible retry loop, and no filled timeout values. A matched record would not by itself establish verified customer identity, and this capture does not demonstrate a match at all. Sample personal fields are fixtures and are omitted here. Hosts and headers are redacted; the model is internal evidence, not a public import schema. No runtime test, customer communication, or cross-flow invocation occurred.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `oncomplete` (declared target count 1); 3: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-lookup-flights"></a>

## lookup_flights.workflow

Observed 2026-09-09T00:02:08.072Z. [Captured model](../evidence/sample-flows/observed/native-lookup-flights.json); [complete graph summary](sample-flows/summaries/native-lookup-flights.json). Runtime tested: **no**.

AI Agent Start 2 declares optional strings `booking_id`, `last_name`, and `new_date`. Its internal `onbegin`, rendered `onBegin`, leads to HTTP 3 GET `/lookup_flights?booking_id=$(n2.aiAgent.booking_id)&last_name=$(n2.aiAgent.last_name)&new_date=$(n2.aiAgent.new_date)`. Both timeout fields contain 10000. End pseudo-nodes 7, 8, and 11 link back to HTTP 3: `oncomplete`/`onSuccess` exits with 2, while `onerror`/`onError` and `ontimeout`/`onTimeout` exit with 3.

Useful handoffs: HTTP extracts `$.available_flights` as `n3.available_flights` and `$.error` as `n3.error`. The Last Execution Status notification covers all status codes, uses payloadType 1, and stores transactionID, `available_flights=$(n3.available_flights)`, and `error=$(n3.error)`. It returns a candidate collection; there is no selection transformation, loop over flights, or mapping from a chosen flight to the reschedule action inside this graph.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 7 → Success; onError (`onerror`) → End 8 → Error; onTimeout (`ontimeout`) → End 11 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.booking_id)` | 3: HTTP Request / url |
| 2: Configure AI Agent Event | `$(n2.aiAgent.last_name)` | 3: HTTP Request / url |
| 2: Configure AI Agent Event | `$(n2.aiAgent.new_date)` | 3: HTTP Request / url |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| 3: HTTP Request | `$(n3.available_flights)` | flow-settings / outcome[1].notification.payload.available_flights |
| 3: HTTP Request | `$(n3.error)` | flow-settings / outcome[1].notification.payload.error |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName |

### Boundaries and adaptation

No booking write or customer notification is configured. The model does not demonstrate date normalization, query-value encoding, an empty-list branch, or retry behavior. Returning candidates cannot establish that one remains available when a later action executes. Error/timeout terminals do not provide a distinct fallback list. Hosts are redacted and fixtures are not current availability. The internal model is not an importable public schema; `runtime_tested=false` means none of these paths was executed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-register-transaction-dispute"></a>

## Register Transaction Dispute.workflow

Observed 2026-09-09T00:01:22.827Z. [Captured model](../evidence/sample-flows/observed/native-register-transaction-dispute.json); [complete graph summary](sample-flows/summaries/native-register-transaction-dispute.json). Runtime tested: **no**.

AI Agent Start 2 declares optional strings `transaction_id`, `dispute_reason`, and `customer_id`. Its internal `onbegin`, rendered `onBegin`, enters HTTP Request 3 POST `/raise_dispute`. End pseudo-node 7 belongs to HTTP 3 and binds `oncomplete`, rendered `onSuccess`, with exitResult 2. No ordinary edge to that terminal is required in the observed internal representation.

Useful handoffs: The body translates `$(n2.aiAgent.customer_id)` to `user_id`, preserves `transaction_id=$(n2.aiAgent.transaction_id)`, and translates `$(n2.aiAgent.dispute_reason)` to `reason`. Connection/request timeout fields both contain 10000. HTTP response path `$.status` becomes `n3.dispute_status`. The Last Execution Status outcome notifies for all status codes with payloadType 2 and custompayload `transactionID=$(transid)` plus `status=$(n3.dispute_status)`. The graph expects a transaction identifier as input; it does not invoke Fetch Recent Transactions to select one.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 7 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.customer_id)` | 3: HTTP Request / body.user_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.transaction_id)` | 3: HTTP Request / body.transaction_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.dispute_reason)` | 3: HTTP Request / body.reason |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.payload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.payload.serviceName |
| 3: HTTP Request | `$(n3.dispute_status)` | flow-settings / outcome[1].notification.custompayload.status |

### Boundaries and adaptation

No explicit HTTP error terminal/edge, retry loop, dispute-ID return, duplicate-dispute check, or customer notification appears. The extracted backend status is not inspected by a separate business-success branch. Historical sample responses do not prove a current dispute was registered. The backend host and headers are redacted. This internal model is evidence rather than a public import schema, and runtime testing is false: no financial action was performed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-request-priority-shipping"></a>

## Request priority shipping.workflow

Observed 2026-09-09T00:01:26.431Z. [Captured model](../evidence/sample-flows/observed/native-request-priority-shipping.json); [complete graph summary](sample-flows/summaries/native-request-priority-shipping.json). Runtime tested: **no**.

AI Agent Start 2 advertises optional string `customer_id`, `order_id`, and `fee_in_dollars`, but its `onbegin`/rendered `onBegin` enters only HTTP Request 3 POST `/request_priority_shipping`. End pseudo-node 12 associates with HTTP 3 through parentNode and `nodeEvent=oncomplete`, rendered `onSuccess`, with exitResult 2. There is no fee-confirmation branch or separate order lookup.

Useful handoffs: The actual request body contains only `user_id=$(n2.aiAgent.customer_id)`. Neither `order_id` nor `fee_in_dollars` is sent or consumed elsewhere in the captured graph. HTTP timeout fields both contain 10000, and response path `$.status` is extracted as node output `status`. However, Last Execution Status uses payloadType 1 and its payload references unqualified `$(status)`, while a custom variable also named status starts empty. No captured session assignment connects `n3.status` to that variable, so the return binding deserves explicit verification rather than silent repair.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 12 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.customer_id)` | 3: HTTP Request / body.user_id |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| External/system/custom value; producer not established here | `$(status)` | flow-settings / outcome[1].notification.payload.status |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName |

### Boundaries and adaptation

The template configures a priority-shipping request but does not demonstrate order targeting, fee charging, a populated return status, retry, or error-specific recovery. There is no Call Workflow or SMS/email node. Hosts and headers are redacted; sample response data is not proof of shipment changes. The internal model is not a public import schema, and `runtime_tested=false` leaves the suspected status-binding ambiguity untested.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: HTTP Request / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-reschedule-flight"></a>

## reschedule_flight.workflow

Observed 2026-09-09T00:02:11.402Z. [Captured model](../evidence/sample-flows/observed/native-reschedule-flight.json); [complete graph summary](sample-flows/summaries/native-reschedule-flight.json). Runtime tested: **no**.

AI Agent Start 2 declares optional string `booking_id`, `last_name`, and `new_flight_id`. Its `onbegin`/rendered `onBegin` enters HTTP Request 3 POST `/reschedule_flight`. End pseudo-node 13 binds HTTP `oncomplete`/`onSuccess` with exitResult 2; node 14 binds `onerror`/`onError` with exitResult 3. The sample calls one reschedule endpoint; it does not visibly create a new booking and then cancel an old one.

Useful handoffs: HTTP body preserves `booking_id=$(n2.aiAgent.booking_id)`, `last_name=$(n2.aiAgent.last_name)`, and `new_flight_id=$(n2.aiAgent.new_flight_id)`. Timeout values are 10000. Fields beneath `$.updated_booking` become outputs prefixed `updated_`: arrival_time, departure_time, flight_number, origin, destination, booking_id, and flight_id. Top-level message/error are extracted too. The all-status Last Execution Status payloadType 1 payload returns transactionID and these n3 outputs. Selection of new_flight_id must precede invocation elsewhere; no Lookup Flights call is configured here.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: HTTP Request |
| 3: HTTP Request | onSuccess (`oncomplete`) → End 13 → Success; onError (`onerror`) → End 14 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.booking_id)` | 3: HTTP Request / body.booking_id |
| 2: Configure AI Agent Event | `$(n2.aiAgent.last_name)` | 3: HTTP Request / body.last_name |
| 2: Configure AI Agent Event | `$(n2.aiAgent.new_flight_id)` | 3: HTTP Request / body.new_flight_id |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| 3: HTTP Request | `$(n3.updated_arrival_time)` | flow-settings / outcome[1].notification.payload.updated_arrival_time |
| 3: HTTP Request | `$(n3.updated_flight_number)` | flow-settings / outcome[1].notification.payload.updated_flight_number |
| 3: HTTP Request | `$(n3.updated_origin)` | flow-settings / outcome[1].notification.payload.updated_origin |
| 3: HTTP Request | `$(n3.updated_destination)` | flow-settings / outcome[1].notification.payload.updated_destination |
| 3: HTTP Request | `$(n3.updated_booking_id)` | flow-settings / outcome[1].notification.payload.updated_booking_id |
| 3: HTTP Request | `$(n3.updated_departure_time)` | flow-settings / outcome[1].notification.payload.updated_departure_time |
| 3: HTTP Request | `$(n3.message)` | flow-settings / outcome[1].notification.payload.message |
| 3: HTTP Request | `$(n3.error)` | flow-settings / outcome[1].notification.payload.error |
| 3: HTTP Request | `$(n3.updated_flight_id)` | flow-settings / outcome[1].notification.payload.updated_flight_id |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName |

### Boundaries and adaptation

No explicit timeout pseudo-node, retry loop, rollback, price-difference calculation, or notification is present. A single HTTP endpoint does not establish atomicity or safe repetition of its backend operation. Embedded updated-booking data is a template fixture, not a rescheduled trip. Hosts and headers are redacted. This internal model is not an importable public schema; runtime testing is false, including response mapping and all mutation outcomes.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-sendsms"></a>

## sendSMS.workflow

Observed 2026-09-09T00:00:41.982Z. [Captured model](../evidence/sample-flows/observed/native-sendsms.json); [complete graph summary](sample-flows/summaries/native-sendsms.json). Runtime tested: **no**.

AI Agent Start 2 exposes optional string `msisdn` and `messageContent`. Its `onbegin`, rendered `onBegin`, connects directly to SMS 3. The node selects SMS delivery and an `msisdn` destination. There is no Receive, conversation loop, or HTTP operation, so this is an agent action for a single outbound message rather than a complete two-way SMS assistant.

Useful handoffs: SMS destination is `$(n2.aiAgent.msisdn)` and message is `$(n2.aiAgent.messageContent)`. The main `senderid` parameter is blank, while `resourceinfo` and `viewmodeData` retain a sender resource; those differing representations require tenant rebinding rather than copying the resource blindly. Last Execution Status is configured for all status codes with `payloadType=1`; its `payload` contains `serviceName=$(serviceName)` and literal `status=success`. A separate stored `custompayload` carries transaction metadata and statuscode 1000.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: SMS |
| 3: SMS | No outgoing route captured |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.messageContent)` | 3: SMS / message |
| 2: Configure AI Agent Event | `$(n2.aiAgent.msisdn)` | 3: SMS / destination |
| External/system/custom value; producer not established here | `$(serviceName)` | flow-settings / outcome[1].notification.custompayload.serviceName; flow-settings / outcome[1].notification.payload.serviceName |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID |
| External/system/custom value; producer not established here | `$(flowname)` | flow-settings / outcome[1].notification.custompayload.flowname |

### Boundaries and adaptation

A literal success string is not delivery evidence. The captured model supplies no explicit delivery-event edge, receipt-processing node, failure-specific return object, or customer-reply handling; `successoutcome=1` alone is not enough to infer receipt behavior. An extra `CustomerIDType` appears only in conditionData, not the AI Agent parseOutput contract. This internal canvas model is not a public import schema. `runtime_tested=false`: no message was invoked, sent, received, or delivery-verified.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 3: SMS / `onerror` (declared target count 1).
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="native-verify-user"></a>

## Verify user.workflow

Observed 2026-09-09T00:01:29.840Z. [Captured model](../evidence/sample-flows/observed/native-verify-user.json); [complete graph summary](sample-flows/summaries/native-verify-user.json). Runtime tested: **no**.

AI Agent Start 2 accepts optional string `zipcode` and `date_of_birth`. Its `onbegin`/rendered `onBegin` enters HTTP 3, labeled Fetch user details, posting to `/verify_user`. End pseudo-nodes 34, 35, and 36 associate with node 3: `oncomplete`/`onSuccess` has exitResult 2, `onerror`/`onError` has 3, and `ontimeout`/`onTimeout` has 4. There is no verification-result Branch or conversational retry.

Useful handoffs: The request deliberately changes case and names: `DOB=$(n2.aiAgent.date_of_birth)` and `ZIP_code=$(n2.aiAgent.zipcode)`. Connection/request timeouts both contain 10000. JSONPath `$` becomes whole-response output `n3.user_details`, while `$.status` becomes `n3.status`. Last Execution Status covers all status codes and uses payloadType 1, storing transactionID, `user_details=$(n3.user_details)`, and `status=$(n3.status)`. A distinct custompayload stores transactionID and response only. HTTP on-leave log actions reference `$(n3.fullResp)` and `$(n3.status)`; fullResp is not a configured extraction output.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure AI Agent Event | onBegin (`onbegin`) → 3: Fetch user details |
| 3: Fetch user details | onSuccess (`oncomplete`) → End 34 → Success; onError (`onerror`) → End 35 → Error; onTimeout (`ontimeout`) → End 36 → Incomplete |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure AI Agent Event | `$(n2.aiAgent.date_of_birth)` | 3: Fetch user details / body.DOB |
| 2: Configure AI Agent Event | `$(n2.aiAgent.zipcode)` | 3: Fetch user details / body.ZIP_code |
| 3: Fetch user details | `$(n3.fullResp)` | 3: Fetch user details / transition_actions[0].value |
| 3: Fetch user details | `$(n3.status)` | 3: Fetch user details / transition_actions[1].value; flow-settings / outcome[1].notification.payload.status |
| External/system/custom value; producer not established here | `$(transid)` | flow-settings / outcome[1].notification.custompayload.transactionID; flow-settings / outcome[1].notification.payload.transactionID |
| 3: Fetch user details | `$(n3.user_details)` | flow-settings / outcome[1].notification.custompayload.response; flow-settings / outcome[1].notification.payload.user_details |

### Boundaries and adaptation

The title does not establish robust authentication or a validated identity policy. No direct call to later banking actions or explicit customer_id extraction is shown; any reuse of user_details belongs to external orchestration. Existing log configuration was only observed, never changed. Hosts and headers are redacted. This internal model is not a public import schema, and `runtime_tested=false` means backend verification, logging, and return serialization were not tested.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-amb-simplified-flow"></a>

## AMB Simplified Flow.workflow

Observed 2026-09-09T00:07:06.551Z. [Captured model](../evidence/sample-flows/observed/wxcc-amb-simplified-flow.json); [complete graph summary](sample-flows/summaries/wxcc-amb-simplified-flow.json). Runtime tested: **no**.

Incoming Apple Start 2 feeds Evaluate 13, which builds details for Resolve Conversation 15. Created/reopened routes send status 5 then Queue Task 59. Queued sends acknowledgement 60, whose success calls PIQ and EWT 74. A successful estimate sends message 80 with both values; InsufficientData sends 76 with position only. PIQ errors/timeouts end Error. Queue failure closes task 23 and sends error 27. Resolve appended/accepted finish Success; its timeout branches on conversationOperation, closing created/reopened work and succeeding for appended. Unlike the Basic Inbound sample, this has no pre-queue Receive.

Useful handoffs: Evaluate 13 serializes messageDetails and pciDetails as `detailsJson`; Resolve consumes it with `$(transId)`. PIQ/EWT uses `$(queue)` and `$(taskId)` plus lookback minutes 5. Messages consume `$(n74.positionInQueue)` and, on Success, `$(n74.estimatedWaitTime)`. Queue itself contains a fixed sample queue ID, while PIQ references a custom queue variable.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 13: Evaluate |
| 5: Apple Messages for Business | onSuccess (`onsuccess`) → 59: Queue Task; onPolicyFail (`onpolicyfail`) → End 215 → Error; onError (`onerror`) → End 216 → Error |
| 13: Evaluate | success (`1`) → 15: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 22: Apple Messages for Business |
| 15: Resolve Conversation | created, reopened → 5: Apple Messages for Business; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 22: Apple Messages for Business; onTimeout (`ontimeout`) → 172: Branch; appended → End 213 → Success; accepted → End 214 → Success |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 129 → Success |
| 23: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error → 27: Apple Messages for Business |
| 27: Apple Messages for Business | onSuccess (`onsuccess`) → End 52 → Success; onPolicyFail (`onpolicyfail`) → End 72 → Error; onError (`onerror`) → End 73 → Error |
| 59: Queue Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task; Queued → 60: Apple Messages for Business |
| 60: Apple Messages for Business | onSuccess (`onsuccess`) → 74: PIQ and EWT; onPolicyFail (`onpolicyfail`) → End 34 → Error; onError (`onerror`) → End 35 → Error; onPolicyFail (`onpolicyfail`) → End 217 → Error; onError (`onerror`) → End 218 → Error |
| 74: PIQ and EWT | Success → 80: Apple Messages for Business; InsufficientData → 76: Apple Messages for Business; onError (`onerror`) → End 219 → Error; onInvalidData (`oninvaliddata`) → End 220 → Error; onInvalidChoice (`oninvalidchoice`) → End 221 → Error; onauthorizationfail → End 222 → Error; serviceUnavailable → End 223 → Error; Error → End 224 → Error; onTimeout (`ontimeout`) → End 225 → Error |
| 76: Apple Messages for Business | No outgoing route captured |
| 80: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 89 → Error; onError (`onerror`) → End 90 → Error; onSuccess (`onsuccess`) → End 91 → Success; onPolicyFail (`onpolicyfail`) → End 92 → Error; onError (`onerror`) → End 93 → Error; onSuccess (`onsuccess`) → End 94 → Success |
| 172: Branch | Create/Reopen Path → 23: Close Task; onError (`onerror`) → End 226 → Error; Append Path → End 227 → Success; None of the above → End 228 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 22: Apple Messages for Business / destination; 27: Apple Messages for Business / destination; 2: Configure Apple Messages for Business Event / transition_actions[0].value; 5: Apple Messages for Business / destination; 60: Apple Messages for Business / destination; 76: Apple Messages for Business / destination; 80: Apple Messages for Business / destination |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachments)` | 2: Configure Apple Messages for Business Event / transition_actions[1].value |
| 2: Configure Apple Messages for Business Event | `$(n2. abc.attachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[2].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachmentUrl)` | 2: Configure Apple Messages for Business Event / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.accountId)` | 2: Configure Apple Messages for Business Event / transition_actions[4].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.appId)` | 2: Configure Apple Messages for Business Event / transition_actions[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 2: Configure Apple Messages for Business Event / transition_actions[16].value; 2: Configure Apple Messages for Business Event / transition_actions[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.transId)` | 2: Configure Apple Messages for Business Event / transition_actions[7].value |
| 2: Configure Apple Messages for Business Event | `$(n2.service.serviceKey)` | 2: Configure Apple Messages for Business Event / transition_actions[8].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.message)` | 2: Configure Apple Messages for Business Event / transition_actions[9].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCIValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[10].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.nonPCIComplianceReason)` | 2: Configure Apple Messages for Business Event / transition_actions[11].value; 2: Configure Apple Messages for Business Event / transition_actions[15].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isAttachmentEnabled)` | 2: Configure Apple Messages for Business Event / transition_actions[12].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[13].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCICompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 13: Evaluate / transition_actions[0].value; 15: Resolve Conversation / extraParamsData.details; 15: Resolve Conversation / nodeInput.details; 15: Resolve Conversation / request_body[6].value |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(transId)` | 15: Resolve Conversation / extraParamsData.trackingId; 15: Resolve Conversation / extraParamsData.transId; 15: Resolve Conversation / nodeInput.trackingId; 15: Resolve Conversation / nodeInput.transId; 15: Resolve Conversation / request_body[0].value; 15: Resolve Conversation / transition_actions[0].value |
| 15: Resolve Conversation | `$(n15.transId)` | 15: Resolve Conversation / transition_actions[1].value |
| 15: Resolve Conversation | `$(n15.taskId)` | 15: Resolve Conversation / transition_actions[2].value |
| 15: Resolve Conversation | `$(n15.conversationOperation)` | 15: Resolve Conversation / transition_actions[3].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 22: Apple Messages for Business / body; 27: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(taskId)` | 23: Close Task / nodeInput.ID; 23: Close Task / nodeInput.Task Id; 23: Close Task / path_parameters[1].value; 23: Close Task / request_body[0].value; 59: Queue Task / extraParamsData.id; 59: Queue Task / path_parameters[1].value; 59: Queue Task / request_body[0].value; 74: PIQ and EWT / extraParamsData.taskid; 74: PIQ and EWT / nodeInput.taskid; 74: PIQ and EWT / path_parameters[2].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 23: Close Task / nodeInput.Conversation ID; 23: Close Task / request_body[2].value; 59: Queue Task / extraParamsData.conversationid; 59: Queue Task / request_body[3].value |
| External/system/custom value; producer not established here | `$(queue)` | 74: PIQ and EWT / extraParamsData.queueid; 74: PIQ and EWT / nodeInput.queueid; 74: PIQ and EWT / path_parameters[1].value |
| 74: PIQ and EWT | `$(n74.positionInQueue)` | 76: Apple Messages for Business / body; 80: Apple Messages for Business / body |
| 74: PIQ and EWT | `$(n74.estimatedWaitTime)` | 80: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 172: Branch / expression; 172: Branch / outcomes[0].conditions[0].varaible; 172: Branch / outcomes[0].conditions[1].varaible; 172: Branch / outcomes[1].conditions[0].varaible |

### Boundaries and adaptation

Bind queue consistently across Queue Task and PIQ/EWT; the graph does not prove their values match. Estimate units are not established by the message text and there is no periodic refresh loop. Send 76 has no captured terminal bindings and declares an unrouted error; repeated End records under Send 80 cannot be reassigned to it. Its older details shape includes isAppleMessage and PCI data but not the newer Basic sample’s malware/security sections.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1); 76: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-basic-inbound-flow"></a>

## Apple Basic Inbound Flow.workflow

Observed 2026-09-09T00:07:13.174Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-basic-inbound-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-basic-inbound-flow.json). Runtime tested: **no**.

Start 2 copies the incoming Apple event into custom variables; Evaluate 13 builds message and scan details; Resolve Conversation 15 creates, reopens, or appends the conversation. Created/reopened routes greet the customer through Send 5 and wait at Receive 189 for up to 600 seconds. A reply reaches attachment transformation 192, then Append Conversation 191, then Queue Task 59. Receive/send/attachment/append failures also continue to queueing through their captured fallback edges. Queued sends acknowledgement 60; queue failure closes the task through 23 before error message 27. Appended/accepted terminate Success without repeating the greeting. Resolve timeout branches on conversationOperation: created/reopened closes the task, appended succeeds, and unknown/error terminates Error.

Useful handoffs: `$(n2.abc.abcUserId)` addresses sends; Start copies `n2.abc.message` to `resolveConversationmessagetext`. Evaluate 13 produces `detailsJson` for Resolve. Receive copies `$(n189.abc.attachments)` and security scan failure details; Evaluate 192 builds `parseDataAttachment`, consumed by Append 191 alongside `$(n189.receive.message)`. Queue/Close consume `$(taskId)` and `$(conversationId)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 13: Evaluate |
| 5: Apple Messages for Business | onSuccess (`onsuccess`) → 189: Receive; onPolicyFail (`onpolicyfail`), onError (`onerror`) → 59: Queue Task |
| 13: Evaluate | success (`1`) → 15: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 22: Apple Messages for Business |
| 15: Resolve Conversation | created, reopened → 5: Apple Messages for Business; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 22: Apple Messages for Business; onTimeout (`ontimeout`) → 172: Branch; appended → End 195 → Success; accepted → End 196 → Success |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 129 → Success |
| 23: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error → 27: Apple Messages for Business |
| 27: Apple Messages for Business | onSuccess (`onsuccess`) → End 52 → Success; onPolicyFail (`onpolicyfail`) → End 72 → Error; onError (`onerror`) → End 73 → Error |
| 59: Queue Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task; Queued → 60: Apple Messages for Business |
| 60: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 34 → Error; onError (`onerror`) → End 35 → Error; onSuccess (`onsuccess`) → End 181 → Success; onPolicyFail (`onpolicyfail`) → End 183 → Error; onError (`onerror`) → End 186 → Error |
| 172: Branch | Create/Reopen Path → 23: Close Task; Append Path → End 173 → Success; None of the above → End 175 → Error; onError (`onerror`) → End 178 → Error |
| 189: Receive | abc.mo → 192: Evaluate; onError (`onerror`), onTimeout (`ontimeout`) → 59: Queue Task |
| 191: Append Conversation | onAppendMessageSuccess, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 59: Queue Task |
| 192: Evaluate | success (`1`) → 191: Append Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 59: Queue Task |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 22: Apple Messages for Business / destination; 27: Apple Messages for Business / destination; 2: Configure Apple Messages for Business Event / transition_actions[0].value; 5: Apple Messages for Business / destination; 60: Apple Messages for Business / destination |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachments)` | 2: Configure Apple Messages for Business Event / transition_actions[1].value |
| 2: Configure Apple Messages for Business Event | `$(n2. abc.attachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[2].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachmentUrl)` | 2: Configure Apple Messages for Business Event / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.accountId)` | 2: Configure Apple Messages for Business Event / transition_actions[4].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.appId)` | 2: Configure Apple Messages for Business Event / transition_actions[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 2: Configure Apple Messages for Business Event / transition_actions[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.transId)` | 2: Configure Apple Messages for Business Event / transition_actions[7].value |
| 2: Configure Apple Messages for Business Event | `$(n2.service.serviceKey)` | 2: Configure Apple Messages for Business Event / transition_actions[8].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.message)` | 2: Configure Apple Messages for Business Event / transition_actions[9].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCIValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[10].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.nonPCIComplianceReason)` | 2: Configure Apple Messages for Business Event / transition_actions[11].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isAttachmentEnabled)` | 2: Configure Apple Messages for Business Event / transition_actions[12].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[13].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCICompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(defaultCustomerName)` | 2: Configure Apple Messages for Business Event / transition_actions[15].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[16].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.securityFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[17].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[18].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[19].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[20].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[21].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.malwareFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[22].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[23].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 2: Configure Apple Messages for Business Event / transition_actions[24].value |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(transId)` | 15: Resolve Conversation / extraParamsData.trackingId; 15: Resolve Conversation / extraParamsData.transId; 15: Resolve Conversation / nodeInput.trackingId; 15: Resolve Conversation / nodeInput.transId; 15: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 15: Resolve Conversation / extraParamsData.details; 15: Resolve Conversation / nodeInput.details; 15: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 22: Apple Messages for Business / body; 27: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(taskId)` | 23: Close Task / path_parameters[1].value; 23: Close Task / request_body[0].value; 59: Queue Task / extraParamsData.id; 59: Queue Task / nodeInput.id; 59: Queue Task / path_parameters[1].value; 59: Queue Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 191: Append Conversation / extraParamsData.conversationid; 191: Append Conversation / path_parameters[1].value; 23: Close Task / request_body[2].value; 59: Queue Task / extraParamsData.conversationid; 59: Queue Task / nodeInput.conversationid; 59: Queue Task / request_body[3].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 172: Branch / expression; 172: Branch / outcomes[0].conditions[0].varaible; 172: Branch / outcomes[0].conditions[1].varaible; 172: Branch / outcomes[1].conditions[0].varaible |
| 189: Receive | `$(n189.abc.attachments)` | 189: Receive / transition_actions[0].value |
| 189: Receive | `$(n189.abc.securityscaninfo.securityFailedReason)` | 189: Receive / transition_actions[1].value |
| 189: Receive | `$(n189.receive.message)` | 191: Append Conversation / extraParamsData.text; 191: Append Conversation / extraParamsData.textOrResponse; 191: Append Conversation / request_body[5].value |
| 189: Receive | `$(n189.abc.timestamp)` | 191: Append Conversation / extraParamsData.timestamp; 191: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(parseDataAttachment)` | 191: Append Conversation / extraParamsData.attachments; 191: Append Conversation / request_body[7].value |
| 189: Receive | `$(n189.abc.capabilityList)` | 191: Append Conversation / extraParamsData.extras; 191: Append Conversation / request_body[32].value |

### Boundaries and adaptation

This waits once before queueing; no captured conversational loop or AI node exists. Start contains the whitespace-bearing reference `$(n2. abc.attachmentCount)`. The attachment script marks dropped files and clears their URLs; it does not itself perform a security scan. Sample identities, queue selection, and error-send handling need adaptation; Send 22 has an unrouted declared error.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-form-response-flow"></a>

## Apple Form Response Flow.workflow

Observed 2026-09-09T00:06:00.411Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-form-response-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-form-response-flow.json). Runtime tested: **no**.

This is a separate event handler for Interactive Message: Form Response, not the form-presentation flow. Start 2 searches conversation 226. Only conversationActive reaches Append Conversation 242, which records the incoming form response; its append-success binding ends Success. Search results noConversationFound, closed, in-queue and on-hold end Error, as do search failures/timeouts. Append failure or timeout sends error message 22 to the originating Apple user; that message’s success binding selects Success, even though the append operation failed. There is no Resolve, queue, Receive or customer-response loop in this graph.

Useful handoffs: Search uses `$(n2.abc.abcUserId)` as customeraddress and the sample business address. Append 242 uses `$(n226.conversationId)` as its conversation path, `$(n2.abc.interactivePayload)` as ambFormResponse, `$(n2.abc.timestamp)` as timestamp, and `$(n2.abc.capabilityList)` as extras. The message type is `amb-form-response` with inbound direction.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 226: Search Conversation |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 345 → Success |
| 226: Search Conversation | conversationActive → 242: Append Conversation; onInvalidData (`oninvaliddata`) → End 378 → Error; onError (`onerror`) → End 379 → Error; onInvalidChoice (`oninvalidchoice`) → End 380 → Error; onauthorizationfail → End 381 → Error; onTimeout (`ontimeout`) → End 382 → Error; noConversationFound → End 383 → Error; conversationClosed → End 384 → Error; conversationInQueue → End 385 → Error; conversationOnHold → End 386 → Error |
| 242: Append Conversation | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure → 22: Apple Messages for Business; onAppendMessageSuccess → End 387 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.requestIdentifier)` | 2: Configure Apple Messages for Business Event / transition_actions[0].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 226: Search Conversation / extraParamsData.customeraddress; 226: Search Conversation / nodeInput.customeraddress; 226: Search Conversation / request_body[1].value; 22: Apple Messages for Business / destination |
| External/system/custom value; producer not established here | `$(errorMsg)` | 22: Apple Messages for Business / body |
| 226: Search Conversation | `$(n226.conversationId)` | 226: Search Conversation / transition_actions[0].value; 242: Append Conversation / extraParamsData.conversationid; 242: Append Conversation / path_parameters[1].value |
| 226: Search Conversation | `$(n226.aliasId)` | 226: Search Conversation / transition_actions[1].value |
| 226: Search Conversation | `$(n226.status)` | 226: Search Conversation / transition_actions[2].value |
| 226: Search Conversation | `$(n226.responsePayload)` | 226: Search Conversation / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 242: Append Conversation / extraParamsData.timestamp; 242: Append Conversation / request_body[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.interactivePayload)` | 242: Append Conversation / extraParamsData.ambFormResponse; 242: Append Conversation / extraParamsData.textOrResponse; 242: Append Conversation / request_body[21].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 242: Append Conversation / extraParamsData.extras; 242: Append Conversation / request_body[32].value |

### Boundaries and adaptation

Request fields and stored nodeInput show different business-address values; neither is a target-tenant default. End entries naming parent node 27 remain in the model although that operative node is absent; these cannot be assigned to Send 22 by guess. Send 22 declares an error with no captured matching route. A Success outcome here can mean error notification succeeded, not form ingestion succeeded.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
End records reference absent producer nodes: 27. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-imessage-app-flow"></a>

## Apple iMessage App Flow.workflow

Observed 2026-09-09T00:06:09.966Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-imessage-app-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-imessage-app-flow.json). Runtime tested: **no**.

The iMessage App Response event at Start 2 invokes Search Conversation 226. Active or in-queue results append through 242; no conversation, closed or on-hold results send restart notice 382 asking for a plain-text message. Search failures and timeout terminate Error. Append success terminates Success, while its failure/timeout routes to error Send 22. Restart notice 382 has Success and Error terminal bindings, with duplicate records preserved. There is no task creation, queue operation, iMessage application launch, Receive wait or conversational loop.

Useful handoffs: Search customeraddress is `$(n2.abc.abcUserId)`. Append 242 uses `$(n226.conversationId)` and maps `$(n2.abc.url)` into text with message type `text-with-attachments`, inbound direction, `$(n2.abc.timestamp)` and capabilityList. Both messages address the incoming Apple user.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 226: Search Conversation |
| 22: Apple Messages for Business | No outgoing route captured |
| 226: Search Conversation | conversationActive, conversationInQueue → 242: Append Conversation; noConversationFound, conversationClosed, conversationOnHold → 382: Apple Messages for Business; onInvalidData (`oninvaliddata`) → End 394 → Error; onError (`onerror`) → End 395 → Error; onInvalidChoice (`oninvalidchoice`) → End 396 → Error; onauthorizationfail → End 397 → Error; onTimeout (`ontimeout`) → End 398 → Error |
| 242: Append Conversation | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure → 22: Apple Messages for Business; onAppendMessageSuccess → End 399 → Success |
| 382: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 360 → Error; onError (`onerror`) → End 361 → Error; onSuccess (`onsuccess`) → End 362 → Success; onPolicyFail (`onpolicyfail`) → End 386 → Error; onError (`onerror`) → End 387 → Error; onSuccess (`onsuccess`) → End 388 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 226: Search Conversation / extraParamsData.customeraddress; 226: Search Conversation / nodeInput.customeraddress; 226: Search Conversation / request_body[1].value; 22: Apple Messages for Business / destination; 382: Apple Messages for Business / destination |
| External/system/custom value; producer not established here | `$(errorMsg)` | 22: Apple Messages for Business / body |
| 226: Search Conversation | `$(n226.conversationId)` | 226: Search Conversation / transition_actions[0].value; 242: Append Conversation / extraParamsData.conversationid; 242: Append Conversation / path_parameters[1].value |
| 226: Search Conversation | `$(n226.aliasId)` | 226: Search Conversation / transition_actions[1].value |
| 226: Search Conversation | `$(n226.status)` | 226: Search Conversation / transition_actions[2].value |
| 226: Search Conversation | `$(n226.responsePayload)` | 226: Search Conversation / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.url)` | 242: Append Conversation / extraParamsData.text; 242: Append Conversation / extraParamsData.textOrResponse; 242: Append Conversation / request_body[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 242: Append Conversation / extraParamsData.timestamp; 242: Append Conversation / request_body[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 242: Append Conversation / extraParamsData.extras; 242: Append Conversation / request_body[32].value |

### Boundaries and adaptation

The sample app response is represented by its URL text; the graph does not parse an app-specific result schema or attach a file merely because the message type says text-with-attachments. Search request_body and stored nodeInput business addresses disagree. Send 22 lacks captured terminal handling for its declared error; its success is also not represented by a binding in this capture. Duplicate restart-notice End items do not imply multiple sends. Reconcile active bindings before adaptation.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-inbound-flow-with-form"></a>

## Apple Inbound Flow with Form.workflow

Observed 2026-09-09T00:07:37.231Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-inbound-flow-with-form.json); [complete graph summary](sample-flows/summaries/wxcc-apple-inbound-flow-with-form.json). Runtime tested: **no**.

Start 2 goes to capability Evaluate 247. FORM-capable devices reach Search Conversation 241: new/closed conversations receive form 239 and wait 300 seconds at Receive 263; active/queued/on-hold conversations go directly to preparation 13. Unsupported or failed capability checks also go to 13. Evaluate 13 parses form selections, builds details, then calls Resolve 15. Created/reopened outcomes reach Branch 260: if a form was presented, Append 245 records its response before message 5; otherwise message 5 is immediate. Set Variable 190 then attempts to expose customerEmail on the task, and all its captured outcomes proceed to Queue 59. Queued sends acknowledgement 60; queue failure closes task 23 and sends error 27. Appended/accepted Resolve outcomes end Success.

Useful handoffs: Receive writes `formResponse = $(n263.abc.selections)`. Evaluate 13 reads pageIdentifier values `name`, `emailAddress`, and `defectiveProduct`; it assigns customerName/customerEmail/defectiveProduct. Send 239 sets `formsSupported` true on entry; Branch 260 tests it. Append 245 consumes `$(n263.receive.payload)`. Set Variable publishes `$(customerEmail)` as String, agent-viewable/editable, nonglobal and nonreportable.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 247: Evaluate |
| 5: Apple Messages for Business | onPolicyFail (`onpolicyfail`), onError (`onerror`), onSuccess (`onsuccess`) → 190: Set Variable |
| 13: Evaluate | success (`1`) → 15: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 22: Apple Messages for Business |
| 15: Resolve Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 22: Apple Messages for Business; onTimeout (`ontimeout`) → 172: Branch; created, reopened → 260: Branch; appended → End 264 → Success; accepted → End 265 → Success |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 129 → Success |
| 23: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error → 27: Apple Messages for Business |
| 27: Apple Messages for Business | onSuccess (`onsuccess`) → End 52 → Success; onPolicyFail (`onpolicyfail`) → End 72 → Error; onError (`onerror`) → End 73 → Error |
| 59: Queue Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task; Queued → 60: Apple Messages for Business |
| 60: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 34 → Error; onError (`onerror`) → End 35 → Error; onSuccess (`onsuccess`) → End 233 → Success; onPolicyFail (`onpolicyfail`) → End 235 → Error; onError (`onerror`) → End 238 → Error |
| 172: Branch | Create/Reopen Path → 23: Close Task; Append Path → End 173 → Success; None of the above → End 175 → Error; onError (`onerror`) → End 178 → Error |
| 190: Set Variable | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Task Updated, onauthorizationfail, Invalid Token, Bad Request, Not Found, serviceUnavailable, Task Failed → 59: Queue Task |
| 239: Apple Messages for Business | onPolicyFail (`onpolicyfail`), onError (`onerror`) → 22: Apple Messages for Business; onSuccess (`onsuccess`) → 263: Receive |
| 241: Search Conversation | noConversationFound, conversationClosed → 239: Apple Messages for Business; conversationActive, conversationInQueue, conversationOnHold → 13: Evaluate; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, onTimeout (`ontimeout`) → 22: Apple Messages for Business |
| 245: Append Conversation | onAppendMessageSuccess, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 5: Apple Messages for Business |
| 247: Evaluate | formsSupported → 241: Search Conversation; formsNotSupported (`1`), onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 13: Evaluate |
| 260: Branch | Form presented → 245: Append Conversation; None of the above, onError (`onerror`) → 5: Apple Messages for Business |
| 263: Receive | abc.oninteractiveformmessage → 13: Evaluate; onTimeout (`ontimeout`), onError (`onerror`) → 22: Apple Messages for Business |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 22: Apple Messages for Business / destination; 239: Apple Messages for Business / destination; 241: Search Conversation / extraParamsData.customeraddress; 241: Search Conversation / nodeInput.customeraddress; 241: Search Conversation / request_body[1].value; 27: Apple Messages for Business / destination; 2: Configure Apple Messages for Business Event / transition_actions[0].value; 5: Apple Messages for Business / destination; 60: Apple Messages for Business / destination |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachments)` | 2: Configure Apple Messages for Business Event / transition_actions[1].value |
| 2: Configure Apple Messages for Business Event | `$(n2. abc.attachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[2].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachmentUrl)` | 2: Configure Apple Messages for Business Event / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.accountId)` | 2: Configure Apple Messages for Business Event / transition_actions[4].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.appId)` | 2: Configure Apple Messages for Business Event / transition_actions[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 2: Configure Apple Messages for Business Event / transition_actions[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.transId)` | 2: Configure Apple Messages for Business Event / transition_actions[7].value |
| 2: Configure Apple Messages for Business Event | `$(n2.service.serviceKey)` | 2: Configure Apple Messages for Business Event / transition_actions[8].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.message)` | 2: Configure Apple Messages for Business Event / transition_actions[9].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCIValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[10].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.nonPCIComplianceReason)` | 2: Configure Apple Messages for Business Event / transition_actions[11].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isAttachmentEnabled)` | 2: Configure Apple Messages for Business Event / transition_actions[12].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[13].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCICompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(defaultCustomerName)` | 2: Configure Apple Messages for Business Event / transition_actions[15].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[16].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.securityFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[17].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[18].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[19].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[20].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[21].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.malwareFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[22].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[23].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 2: Configure Apple Messages for Business Event / transition_actions[24].value |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(transId)` | 15: Resolve Conversation / extraParamsData.trackingId; 15: Resolve Conversation / extraParamsData.transId; 15: Resolve Conversation / nodeInput.trackingId; 15: Resolve Conversation / nodeInput.transId; 15: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 15: Resolve Conversation / extraParamsData.details; 15: Resolve Conversation / nodeInput.details; 15: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 22: Apple Messages for Business / body; 27: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(taskId)` | 190: Set Variable / extraParamsData.id; 190: Set Variable / nodeInput.id; 190: Set Variable / path_parameters[1].value; 190: Set Variable / request_body[0].value; 23: Close Task / path_parameters[1].value; 23: Close Task / request_body[0].value; 59: Queue Task / extraParamsData.id; 59: Queue Task / nodeInput.id; 59: Queue Task / path_parameters[1].value; 59: Queue Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 190: Set Variable / extraParamsData.flowVariables[6].value; 190: Set Variable / nodeInput.flowVariables[6].value; 23: Close Task / request_body[2].value; 245: Append Conversation / extraParamsData.conversationid; 245: Append Conversation / path_parameters[1].value; 59: Queue Task / extraParamsData.conversationid; 59: Queue Task / nodeInput.conversationid; 59: Queue Task / request_body[3].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 172: Branch / expression; 172: Branch / outcomes[0].conditions[0].varaible; 172: Branch / outcomes[0].conditions[1].varaible; 172: Branch / outcomes[1].conditions[0].varaible |
| External/system/custom value; producer not established here | `$(customerEmail)` | 190: Set Variable / extraParamsData.fv[0].value; 190: Set Variable / extraParamsData.vrbls[0].value; 190: Set Variable / nodeInput.fv[1].value; 190: Set Variable / nodeInput.vrbls[1].value; 190: Set Variable / request_body[2].value[0].value |
| External/system/custom value; producer not established here | `$(gender)` | 190: Set Variable / extraParamsData.value; 190: Set Variable / nodeInput.fv[0].value; 190: Set Variable / nodeInput.value; 190: Set Variable / nodeInput.vrbls[0].value |
| custom variable; writers 263: Receive | `$(formResponse)` | 241: Search Conversation / transition_actions[0].value; 263: Receive / transition_actions[1].value |
| 263: Receive | `$(n263.abc.timestamp)` | 245: Append Conversation / extraParamsData.timestamp; 245: Append Conversation / request_body[6].value |
| 263: Receive | `$(n263.receive.payload)` | 245: Append Conversation / extraParamsData.ambFormResponse; 245: Append Conversation / extraParamsData.textOrResponse; 245: Append Conversation / request_body[21].value |
| 263: Receive | `$(n263.abc.capabilityList)` | 245: Append Conversation / extraParamsData.extras; 245: Append Conversation / request_body[32].value |
| custom variable; writers 239: Apple Messages for Business | `$(formsSupported)` | 260: Branch / expression; 260: Branch / outcomes[0].conditions[0].varaible |
| 263: Receive | `$(n263.abc.selections)` | 263: Receive / transition_actions[0].value; 263: Receive / transition_actions[2].value |
| 263: Receive | `$(n263.receive.message)` | 263: Receive / transition_actions[3].value |

### Boundaries and adaptation

The stored send type is spelled `form_mesage`; this is internal model evidence, not an import instruction. A Set Variable failure still queues the task, so queueing does not prove customerEmail reached the desktop. Form timeout/error sends error 22. There is no response-validation/retry loop; selected form definitions, default values, and identifiers need tenant-specific binding.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-inbound-flow-with-intentid-groupid-based-routing"></a>

## Apple Inbound Flow with IntentId GroupId based Routing.workflow

Observed 2026-09-09T00:05:17.004Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-inbound-flow-with-intentid-groupid-based-routing.json); [complete graph summary](sample-flows/summaries/wxcc-apple-inbound-flow-with-intentid-groupid-based-routing.json). Runtime tested: **no**.

Incoming Apple Start 2 feeds payload preparation 13 and Resolve Conversation 15. Only created/reopened outcomes reach routing Branch 191. The accounts condition requires intentId=support AND groupId=account; it sends notice 193 then Queue Task 192. The sales condition requires intentId=courses AND groupId=sales; notice 194 precedes Queue Task 196. Unmatched/branch-error paths use default Queue Task 59. Each notice continues to its queue on success, policy failure or error. Every Queued outcome sends acknowledgement 60; queue failures converge on Close Task 23 then error message 27. Resolve appended/accepted terminate Success. Its timeout branch 172 closes created/reopened work, succeeds for appended, and errors for other states.

Useful handoffs: Start writes `intentId = $(n2.abc.intentId)` and `groupId = $(n2.abc.groupId)`; these are Apple event fields used directly by Branch 191. It also writes `abcUserId`; notices 193/194 consume `$(abcUserId)`. Evaluate 13 serializes `detailsJson` for Resolve; queue nodes consume `$(taskId)` and `$(conversationId)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 13: Evaluate |
| 13: Evaluate | success (`1`) → 15: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 22: Apple Messages for Business |
| 15: Resolve Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 22: Apple Messages for Business; onTimeout (`ontimeout`) → 172: Branch; reopened, created → 191: Branch; appended → End 207 → Success; accepted → End 208 → Success |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 129 → Success |
| 23: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error → 27: Apple Messages for Business |
| 27: Apple Messages for Business | onSuccess (`onsuccess`) → End 52 → Success; onPolicyFail (`onpolicyfail`) → End 72 → Error; onError (`onerror`) → End 73 → Error |
| 59: Queue Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task; Queued → 60: Apple Messages for Business |
| 60: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 34 → Error; onError (`onerror`) → End 35 → Error; onPolicyFail (`onpolicyfail`) → End 200 → Error; onError (`onerror`) → End 201 → Error; onSuccess (`onsuccess`) → End 202 → Success |
| 172: Branch | Create/Reopen Path → 23: Close Task; Append Path → End 173 → Success; None of the above → End 175 → Error; onError (`onerror`) → End 178 → Error |
| 191: Branch | None of the above, onError (`onerror`) → 59: Queue Task; accounts intent → 193: Apple Messages for Business; sales → 194: Apple Messages for Business |
| 192: Queue Task | Queued → 60: Apple Messages for Business; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed → 23: Close Task |
| 193: Apple Messages for Business | onError (`onerror`), onPolicyFail (`onpolicyfail`), onSuccess (`onsuccess`) → 192: Queue Task |
| 194: Apple Messages for Business | onSuccess (`onsuccess`), onError (`onerror`), onPolicyFail (`onpolicyfail`) → 196: Queue Task |
| 196: Queue Task | Queued → 60: Apple Messages for Business; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed → 23: Close Task |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 22: Apple Messages for Business / destination; 27: Apple Messages for Business / destination; 2: Configure Apple Messages for Business Event / transition_actions[0].value; 60: Apple Messages for Business / destination |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachments)` | 2: Configure Apple Messages for Business Event / transition_actions[1].value |
| 2: Configure Apple Messages for Business Event | `$(n2. abc.attachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[2].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachmentUrl)` | 2: Configure Apple Messages for Business Event / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.accountId)` | 2: Configure Apple Messages for Business Event / transition_actions[4].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.appId)` | 2: Configure Apple Messages for Business Event / transition_actions[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 2: Configure Apple Messages for Business Event / transition_actions[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.transId)` | 2: Configure Apple Messages for Business Event / transition_actions[7].value |
| 2: Configure Apple Messages for Business Event | `$(n2.service.serviceKey)` | 2: Configure Apple Messages for Business Event / transition_actions[8].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.message)` | 2: Configure Apple Messages for Business Event / transition_actions[9].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCIValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[10].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.nonPCIComplianceReason)` | 2: Configure Apple Messages for Business Event / transition_actions[11].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isAttachmentEnabled)` | 2: Configure Apple Messages for Business Event / transition_actions[12].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[13].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCICompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[14].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[16].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.securityFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[17].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[18].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[19].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[20].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[21].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.malwareFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[22].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[23].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.intentId)` | 2: Configure Apple Messages for Business Event / transition_actions[24].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.groupId)` | 2: Configure Apple Messages for Business Event / transition_actions[25].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 2: Configure Apple Messages for Business Event / transition_actions[26].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 13: Evaluate / transition_actions[0].value; 15: Resolve Conversation / extraParamsData.details; 15: Resolve Conversation / nodeInput.details; 15: Resolve Conversation / request_body[6].value |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(transId)` | 15: Resolve Conversation / extraParamsData.trackingId; 15: Resolve Conversation / extraParamsData.transId; 15: Resolve Conversation / nodeInput.trackingId; 15: Resolve Conversation / nodeInput.transId; 15: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 22: Apple Messages for Business / body; 27: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(taskId)` | 192: Queue Task / extraParamsData.id; 192: Queue Task / nodeInput.id; 192: Queue Task / path_parameters[1].value; 192: Queue Task / request_body[0].value; 196: Queue Task / extraParamsData.id; 196: Queue Task / nodeInput.id; 196: Queue Task / path_parameters[1].value; 196: Queue Task / request_body[0].value; 23: Close Task / path_parameters[1].value; 23: Close Task / request_body[0].value; 59: Queue Task / extraParamsData.id; 59: Queue Task / nodeInput.id; 59: Queue Task / path_parameters[1].value; 59: Queue Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 192: Queue Task / extraParamsData.conversationid; 192: Queue Task / nodeInput.conversationid; 192: Queue Task / request_body[3].value; 196: Queue Task / extraParamsData.conversationid; 196: Queue Task / nodeInput.conversationid; 196: Queue Task / request_body[3].value; 23: Close Task / request_body[2].value; 59: Queue Task / extraParamsData.conversationid; 59: Queue Task / nodeInput.conversationid; 59: Queue Task / request_body[3].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 172: Branch / expression; 172: Branch / outcomes[0].conditions[0].varaible; 172: Branch / outcomes[0].conditions[1].varaible; 172: Branch / outcomes[1].conditions[0].varaible |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(intentId)` | 191: Branch / expression; 191: Branch / outcomes[0].conditions[0].varaible; 191: Branch / outcomes[1].conditions[0].varaible |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(groupId)` | 191: Branch / expression; 191: Branch / outcomes[0].conditions[1].varaible; 191: Branch / outcomes[1].conditions[1].varaible |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(abcUserId)` | 193: Apple Messages for Business / destination; 194: Apple Messages for Business / destination |

### Boundaries and adaptation

The word intent here is an Apple event routing identifier; this graph contains no Studio intent classifier or AI invocation. Queue choices are sample bindings, not a universal accounts/sales mapping. There is no Receive, loop, or business-system lookup. Resolve errors use customer error Send 22, whose declared send-error destination is not captured.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-list-picker-flow"></a>

## Apple List Picker Flow.workflow

Observed 2026-09-09T00:05:25.341Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-list-picker-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-list-picker-flow.json). Runtime tested: **no**.

Start 2 and Evaluate 13 reach Resolve Conversation 15. Created/reopened outcomes send country list picker 193, then Receive 206 waits 300 seconds. A list-picker response appends the outbound picker through 197, then inbound response through 198, and sends status message 5. Branch 199 examines the received choices: USA routes Queue 201, India Queue 203, UK Queue 200; unmatched/error routes default Queue 59. Picker/send/receive/append fallback paths also reach this branch. Queued sends acknowledgement 60; queue failures close task 23 then send error 27. Appended/accepted Resolve outcomes terminate Success, while Resolve timeout uses operation-sensitive Branch 172.

Useful handoffs: Picker 193 offers India, USA and UK with requestIdentifier `system`. Append 197 consumes `$(n193.send.listPicker)` and `$(n193.send.sentDateTime)`. Append 198 request fields consume `$(n206.receive.payload)` and `$(n206.abc.timestamp)`; Branch 199 tests `$(n206.abc.listPickerItems)` using contains. All queue nodes use the shared task/conversation identifiers.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 13: Evaluate |
| 5: Apple Messages for Business | onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`), onError (`onerror`) → 199: Branch |
| 13: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 22: Apple Messages for Business; success (`1`) → 15: Resolve Conversation |
| 15: Resolve Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 22: Apple Messages for Business; onTimeout (`ontimeout`) → 172: Branch; created, reopened → 193: Apple Messages for Business; appended → End 210 → Success; accepted → End 211 → Success |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 129 → Success |
| 23: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error → 27: Apple Messages for Business |
| 27: Apple Messages for Business | onSuccess (`onsuccess`) → End 52 → Success; onPolicyFail (`onpolicyfail`) → End 72 → Error; onError (`onerror`) → End 73 → Error |
| 59: Queue Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task; Queued → 60: Apple Messages for Business |
| 60: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 34 → Error; onError (`onerror`) → End 35 → Error; onSuccess (`onsuccess`) → End 181 → Success; onPolicyFail (`onpolicyfail`) → End 183 → Error; onError (`onerror`) → End 186 → Error |
| 172: Branch | Create/Reopen Path → 23: Close Task; Append Path → End 173 → Success; None of the above → End 175 → Error; onError (`onerror`) → End 178 → Error |
| 193: Apple Messages for Business | onPolicyFail (`onpolicyfail`), onError (`onerror`) → 5: Apple Messages for Business; onSuccess (`onsuccess`) → 206: Receive |
| 197: Append Conversation | onAppendMessageSuccess → 198: Append Conversation; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 5: Apple Messages for Business |
| 198: Append Conversation | onAppendMessageSuccess, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 5: Apple Messages for Business |
| 199: Branch | USA → 201: Queue Task; India → 203: Queue Task; UK → 200: Queue Task; None of the above, onError (`onerror`) → 59: Queue Task |
| 200: Queue Task | Queued → 60: Apple Messages for Business; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed → 23: Close Task |
| 201: Queue Task | Queued → 60: Apple Messages for Business; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task |
| 203: Queue Task | Queued → 60: Apple Messages for Business; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task |
| 206: Receive | abc.oninteractivelistpicker → 197: Append Conversation; onTimeout (`ontimeout`), onError (`onerror`) → 5: Apple Messages for Business |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 193: Apple Messages for Business / destination; 22: Apple Messages for Business / destination; 27: Apple Messages for Business / destination; 2: Configure Apple Messages for Business Event / transition_actions[0].value; 5: Apple Messages for Business / destination; 60: Apple Messages for Business / destination |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachments)` | 2: Configure Apple Messages for Business Event / transition_actions[1].value |
| 2: Configure Apple Messages for Business Event | `$(n2. abc.attachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[2].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachmentUrl)` | 2: Configure Apple Messages for Business Event / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.accountId)` | 2: Configure Apple Messages for Business Event / transition_actions[4].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.appId)` | 2: Configure Apple Messages for Business Event / transition_actions[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 2: Configure Apple Messages for Business Event / transition_actions[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.transId)` | 2: Configure Apple Messages for Business Event / transition_actions[7].value |
| 2: Configure Apple Messages for Business Event | `$(n2.service.serviceKey)` | 2: Configure Apple Messages for Business Event / transition_actions[8].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.message)` | 2: Configure Apple Messages for Business Event / transition_actions[9].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCIValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[10].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.nonPCIComplianceReason)` | 2: Configure Apple Messages for Business Event / transition_actions[11].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isAttachmentEnabled)` | 2: Configure Apple Messages for Business Event / transition_actions[12].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[13].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCICompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(defaultCustomerName)` | 2: Configure Apple Messages for Business Event / transition_actions[15].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[16].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.securityFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[17].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[18].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[19].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[20].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[21].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.malwareFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[22].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[23].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 2: Configure Apple Messages for Business Event / transition_actions[24].value |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(transId)` | 15: Resolve Conversation / extraParamsData.trackingId; 15: Resolve Conversation / extraParamsData.transId; 15: Resolve Conversation / nodeInput.trackingId; 15: Resolve Conversation / nodeInput.transId; 15: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 15: Resolve Conversation / extraParamsData.details; 15: Resolve Conversation / nodeInput.details; 15: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 22: Apple Messages for Business / body; 27: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(taskId)` | 200: Queue Task / extraParamsData.id; 200: Queue Task / nodeInput.id; 200: Queue Task / path_parameters[1].value; 200: Queue Task / request_body[0].value; 201: Queue Task / extraParamsData.id; 201: Queue Task / nodeInput.id; 201: Queue Task / path_parameters[1].value; 201: Queue Task / request_body[0].value; 203: Queue Task / extraParamsData.id; 203: Queue Task / nodeInput.id; 203: Queue Task / path_parameters[1].value; 203: Queue Task / request_body[0].value; 23: Close Task / path_parameters[1].value; 23: Close Task / request_body[0].value; 59: Queue Task / extraParamsData.id; 59: Queue Task / nodeInput.id; 59: Queue Task / path_parameters[1].value; 59: Queue Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 197: Append Conversation / extraParamsData.conversationid; 197: Append Conversation / path_parameters[1].value; 198: Append Conversation / extraParamsData.conversationid; 198: Append Conversation / nodeInput.conversationid; 198: Append Conversation / path_parameters[1].value; 200: Queue Task / extraParamsData.conversationid; 200: Queue Task / nodeInput.conversationid; 200: Queue Task / request_body[3].value; 201: Queue Task / extraParamsData.conversationid; 201: Queue Task / nodeInput.conversationid; 201: Queue Task / request_body[3].value; 203: Queue Task / extraParamsData.conversationid; 203: Queue Task / nodeInput.conversationid; 203: Queue Task / request_body[3].value; 23: Close Task / request_body[2].value; 59: Queue Task / extraParamsData.conversationid; 59: Queue Task / nodeInput.co… [full value in graph summary] |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 172: Branch / expression; 172: Branch / outcomes[0].conditions[0].varaible; 172: Branch / outcomes[0].conditions[1].varaible; 172: Branch / outcomes[1].conditions[0].varaible |
| 193: Apple Messages for Business | `$(n193.send.sentDateTime)` | 197: Append Conversation / extraParamsData.timestamp; 197: Append Conversation / request_body[6].value |
| 193: Apple Messages for Business | `$(n193.send.listPicker)` | 197: Append Conversation / extraParamsData.ambListPicker; 197: Append Conversation / extraParamsData.textOrResponse; 197: Append Conversation / request_body[22].value |
| 206: Receive | `$(n206.abc.timestamp)` | 198: Append Conversation / extraParamsData.timestamp; 198: Append Conversation / request_body[6].value |
| 206: Receive | `$(n206.receive.payload)` | 198: Append Conversation / extraParamsData.ambListPickerResponse; 198: Append Conversation / extraParamsData.textOrResponse; 198: Append Conversation / request_body[23].value; 206: Receive / transition_actions[0].value |
| 206: Receive | `$(n206.abc.capabilityList)` | 198: Append Conversation / extraParamsData.extras; 198: Append Conversation / request_body[32].value |
| 194 | `$(n194.receive.payload)` | 198: Append Conversation / nodeInput.ambListPickerResponse; 198: Append Conversation / nodeInput.textOrResponse |
| 194 | `$(n194.abc.timestamp)` | 198: Append Conversation / nodeInput.timestamp |
| 194 | `$(n194.abc.capabilityList)` | 198: Append Conversation / nodeInput.extras |
| 206: Receive | `$(n206.abc.listPickerItems)` | 199: Branch / expression; 199: Branch / outcomes[0].conditions[0].varaible; 199: Branch / outcomes[1].conditions[0].varaible; 199: Branch / outcomes[2].conditions[0].varaible |

### Boundaries and adaptation

Stored nodeInput in Append 198 still references uncaptured n194, while its request_body references n206. Queue request fields select the same queue ID across country-specific nodes, while stored UI queue selections differ; distinct branches do not establish distinct operational queues. Rebind through the supported UI and verify the active contract. A response timeout can reach the branch without a valid selected country; no selection retry loop is captured.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
Literal node-qualified references name uncaptured producers: n194. Their provenance is not guessed.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-time-picker-and-list-picker-response-flow"></a>

## Apple Time Picker and List Picker Response Flow.workflow

Observed 2026-09-09T00:06:05.466Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-time-picker-and-list-picker-response-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-time-picker-and-list-picker-response-flow.json). Runtime tested: **no**.

Start 2 handles the Apple List Picker or Time Picker interactive-response event and searches conversation 226. Only an active conversation reaches Evaluate 336, which classifies messageType by substring. Result 1 selects list-response Append 242; result 2 selects time-response Append 348; unsupported type/result 3 and Evaluate failures terminate Error. Search no-conversation, closed, queued, on-hold and failure states also terminate Error. Either append’s failure/timeout routes to customer error Send 22. The model records successful append terminal bindings under node 348; the detailed graph preserves their actual parent references instead of assuming symmetric wiring.

Useful handoffs: Start writes `messageType = $(n2.abc.type)`. Evaluate checks `list_picker_response` and `time_picker_response`. Both append nodes use `$(n226.conversationId)`, `$(n2.abc.interactivePayload)`, `$(n2.abc.timestamp)` and capabilityList, while selecting `amb-list-picker-response` or `amb-time-picker-response` respectively.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 226: Search Conversation |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 360 → Success |
| 226: Search Conversation | conversationActive → 336: Evaluate; onInvalidData (`oninvaliddata`) → End 390 → Error; onError (`onerror`) → End 391 → Error; onInvalidChoice (`oninvalidchoice`) → End 392 → Error; onauthorizationfail → End 393 → Error; onTimeout (`ontimeout`) → End 394 → Error; noConversationFound → End 395 → Error; conversationClosed → End 396 → Error; conversationInQueue → End 397 → Error; conversationOnHold → End 398 → Error |
| 242: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 22: Apple Messages for Business |
| 336: Evaluate | listPickerResponse (`1`) → 242: Append Conversation; timePickerResponse (`2`) → 348: Append Conversation; onInvalidChoice (`oninvalidchoice`) → End 352 → Error; onError (`onerror`) → End 354 → Error; None of the above (`3`) → End 357 → Error |
| 348: Append Conversation | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure → 22: Apple Messages for Business; onAppendMessageSuccess → End 399 → Success; onAppendMessageSuccess → End 400 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.type)` | 2: Configure Apple Messages for Business Event / transition_actions[0].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 226: Search Conversation / extraParamsData.customeraddress; 226: Search Conversation / nodeInput.customeraddress; 226: Search Conversation / request_body[1].value; 22: Apple Messages for Business / destination |
| External/system/custom value; producer not established here | `$(errorMsg)` | 22: Apple Messages for Business / body |
| 226: Search Conversation | `$(n226.conversationId)` | 226: Search Conversation / transition_actions[0].value; 242: Append Conversation / extraParamsData.conversationid; 242: Append Conversation / path_parameters[1].value; 348: Append Conversation / extraParamsData.conversationid; 348: Append Conversation / path_parameters[1].value |
| 226: Search Conversation | `$(n226.aliasId)` | 226: Search Conversation / transition_actions[1].value |
| 226: Search Conversation | `$(n226.status)` | 226: Search Conversation / transition_actions[2].value |
| 226: Search Conversation | `$(n226.responsePayload)` | 226: Search Conversation / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 242: Append Conversation / extraParamsData.timestamp; 242: Append Conversation / request_body[6].value; 348: Append Conversation / extraParamsData.timestamp; 348: Append Conversation / request_body[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.interactivePayload)` | 242: Append Conversation / extraParamsData.ambListPickerResponse; 242: Append Conversation / extraParamsData.textOrResponse; 242: Append Conversation / request_body[23].value; 348: Append Conversation / extraParamsData.ambTimePickerResponse; 348: Append Conversation / extraParamsData.textOrResponse; 348: Append Conversation / request_body[27].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 242: Append Conversation / extraParamsData.extras; 242: Append Conversation / request_body[32].value; 348: Append Conversation / extraParamsData.extras; 348: Append Conversation / request_body[32].value |

### Boundaries and adaptation

Two success End records name parent 348; no corresponding parent-242 success binding is present. Additional error End records name absent parent 27, and Send 22 has an unrouted error declaration. Preserve these observed inconsistencies rather than inventing a successful list branch. Search request_body and stored UI business addresses differ. This records an existing interaction; it sends no picker and has no queue/Receive loop.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
End records reference absent producer nodes: 27. These stale/unresolved parent references do not establish operative nodes or valid routes.
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-time-picker-flow"></a>

## Apple Time Picker Flow.workflow

Observed 2026-09-09T00:05:32.254Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-time-picker-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-time-picker-flow.json). Runtime tested: **no**.

Start 2 prepares details at Evaluate 13 and invokes Resolve Conversation 15. Created/reopened routes send time picker 193 and wait up to 300 seconds at Receive 206. Its interactive time-picker event appends the outbound picker through 197, then the inbound response through 198, then status message 5 and Queue Task 59. Picker, Receive and append failures converge on the same status/queue path. Queued sends acknowledgement 60; queue failure closes task 23 then sends error 27. Existing appended/accepted Resolve outcomes finish Success without presenting the picker. Resolve timeout uses Branch 172 to distinguish created/reopened cleanup from appended completion.

Useful handoffs: Append 197 records `$(n193.send.timePicker)` and `$(n193.send.sentDateTime)` as `amb-time-picker`. Append 198 records `$(n206.receive.payload)` and `$(n206.abc.timestamp)` as `amb-time-picker-response`, plus capability metadata. Sends address `$(n2.abc.abcUserId)`; append/queue nodes consume shared `conversationId`/`taskId`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 13: Evaluate |
| 5: Apple Messages for Business | onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`), onError (`onerror`) → 59: Queue Task |
| 13: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 22: Apple Messages for Business; success (`1`) → 15: Resolve Conversation |
| 15: Resolve Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 22: Apple Messages for Business; onTimeout (`ontimeout`) → 172: Branch; created, reopened → 193: Apple Messages for Business; appended → End 207 → Success; accepted → End 208 → Success |
| 22: Apple Messages for Business | onSuccess (`onsuccess`) → End 129 → Success |
| 23: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error → 27: Apple Messages for Business |
| 27: Apple Messages for Business | onSuccess (`onsuccess`) → End 52 → Success; onPolicyFail (`onpolicyfail`) → End 72 → Error; onError (`onerror`) → End 73 → Error |
| 59: Queue Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 23: Close Task; Queued → 60: Apple Messages for Business |
| 60: Apple Messages for Business | onPolicyFail (`onpolicyfail`) → End 34 → Error; onError (`onerror`) → End 35 → Error; onSuccess (`onsuccess`) → End 181 → Success; onPolicyFail (`onpolicyfail`) → End 183 → Error; onError (`onerror`) → End 186 → Error |
| 172: Branch | Create/Reopen Path → 23: Close Task; Append Path → End 173 → Success; None of the above → End 175 → Error; onError (`onerror`) → End 178 → Error |
| 193: Apple Messages for Business | onPolicyFail (`onpolicyfail`), onError (`onerror`) → 5: Apple Messages for Business; onSuccess (`onsuccess`) → 206: Receive |
| 197: Append Conversation | onAppendMessageSuccess → 198: Append Conversation; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 5: Apple Messages for Business |
| 198: Append Conversation | onAppendMessageSuccess, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 5: Apple Messages for Business |
| 206: Receive | onTimeout (`ontimeout`), onError (`onerror`) → 5: Apple Messages for Business; abc.oninteractivetimepicker → 197: Append Conversation |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 193: Apple Messages for Business / destination; 22: Apple Messages for Business / destination; 27: Apple Messages for Business / destination; 2: Configure Apple Messages for Business Event / transition_actions[0].value; 5: Apple Messages for Business / destination; 60: Apple Messages for Business / destination |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachments)` | 2: Configure Apple Messages for Business Event / transition_actions[1].value |
| 2: Configure Apple Messages for Business Event | `$(n2. abc.attachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[2].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.attachmentUrl)` | 2: Configure Apple Messages for Business Event / transition_actions[3].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.accountId)` | 2: Configure Apple Messages for Business Event / transition_actions[4].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.appId)` | 2: Configure Apple Messages for Business Event / transition_actions[5].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.timestamp)` | 2: Configure Apple Messages for Business Event / transition_actions[6].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.transId)` | 2: Configure Apple Messages for Business Event / transition_actions[7].value |
| 2: Configure Apple Messages for Business Event | `$(n2.service.serviceKey)` | 2: Configure Apple Messages for Business Event / transition_actions[8].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.message)` | 2: Configure Apple Messages for Business Event / transition_actions[9].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCIValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[10].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.nonPCIComplianceReason)` | 2: Configure Apple Messages for Business Event / transition_actions[11].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isAttachmentEnabled)` | 2: Configure Apple Messages for Business Event / transition_actions[12].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[13].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.pciInfo.isPCICompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(defaultCustomerName)` | 2: Configure Apple Messages for Business Event / transition_actions[15].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[16].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.securityFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[17].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[18].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.securityscaninfo.isSecurityCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[19].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareValidationDone)` | 2: Configure Apple Messages for Business Event / transition_actions[20].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.isMalwareCompliance)` | 2: Configure Apple Messages for Business Event / transition_actions[21].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.malwareFailedReason)` | 2: Configure Apple Messages for Business Event / transition_actions[22].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.malwareinfo.droppedAttachmentCount)` | 2: Configure Apple Messages for Business Event / transition_actions[23].value |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.capabilityList)` | 2: Configure Apple Messages for Business Event / transition_actions[24].value |
| custom variable; writers 2: Configure Apple Messages for Business Event | `$(transId)` | 15: Resolve Conversation / extraParamsData.trackingId; 15: Resolve Conversation / extraParamsData.transId; 15: Resolve Conversation / nodeInput.trackingId; 15: Resolve Conversation / nodeInput.transId; 15: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 15: Resolve Conversation / extraParamsData.details; 15: Resolve Conversation / nodeInput.details; 15: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 22: Apple Messages for Business / body; 27: Apple Messages for Business / body |
| External/system/custom value; producer not established here | `$(taskId)` | 23: Close Task / path_parameters[1].value; 23: Close Task / request_body[0].value; 59: Queue Task / extraParamsData.id; 59: Queue Task / nodeInput.id; 59: Queue Task / path_parameters[1].value; 59: Queue Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 197: Append Conversation / extraParamsData.conversationid; 197: Append Conversation / path_parameters[1].value; 198: Append Conversation / extraParamsData.conversationid; 198: Append Conversation / path_parameters[1].value; 23: Close Task / request_body[2].value; 59: Queue Task / extraParamsData.conversationid; 59: Queue Task / nodeInput.conversationid; 59: Queue Task / request_body[3].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 172: Branch / expression; 172: Branch / outcomes[0].conditions[0].varaible; 172: Branch / outcomes[0].conditions[1].varaible; 172: Branch / outcomes[1].conditions[0].varaible |
| 193: Apple Messages for Business | `$(n193.send.sentDateTime)` | 197: Append Conversation / extraParamsData.timestamp; 197: Append Conversation / request_body[6].value |
| 193: Apple Messages for Business | `$(n193.send.timePicker)` | 197: Append Conversation / extraParamsData.ambTimePicker; 197: Append Conversation / extraParamsData.textOrResponse; 197: Append Conversation / request_body[26].value |
| 206: Receive | `$(n206.abc.timestamp)` | 198: Append Conversation / extraParamsData.timestamp; 198: Append Conversation / request_body[6].value |
| 206: Receive | `$(n206.receive.payload)` | 198: Append Conversation / extraParamsData.ambTimePickerResponse; 198: Append Conversation / extraParamsData.textOrResponse; 198: Append Conversation / request_body[27].value; 206: Receive / transition_actions[0].value |
| 206: Receive | `$(n206.abc.capabilityList)` | 198: Append Conversation / extraParamsData.extras; 198: Append Conversation / request_body[32].value |

### Boundaries and adaptation

Picker slots are fixed to 2024-04-01 at 09:00 and 10:00, with duration 1800 and timezoneOffset `Asia/Calcutta`; they are historical examples, not available appointments. The graph records a selection then queues work: no booking API, availability lookup, selected-slot branch or retry loop exists. Queueing can occur after a picker timeout. Several repeated End bindings and Send 22’s unrouted error are retained as captured.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 22: Apple Messages for Business / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-apple-unsubscribe-flow"></a>

## Apple Unsubscribe Flow.workflow

Observed 2026-09-09T00:07:41.477Z. [Captured model](../evidence/sample-flows/observed/wxcc-apple-unsubscribe-flow.json); [complete graph summary](sample-flows/summaries/wxcc-apple-unsubscribe-flow.json). Runtime tested: **no**.

Apple Conversation closed triggers Start 2 and Search Conversation 3. Search results conversationClosed, conversationOnHold, conversationInQueue and conversationActive all route to Close Task 4. Close Task Success terminates Success; its Error, authorization, invalid-data/choice, general-error and timeout events terminate Error. Search noConversationFound terminates Success without a close attempt, while search failures/timeouts end Error. This is an event-to-cleanup flow with no outgoing customer message, Receive or loop.

Useful handoffs: Search identifies the conversation using the incoming Apple identity. Its output `$(n3.aliasId)` becomes both Close Task’s Task Id request value and ID path parameter. `$(n3.conversationId)` becomes Conversation ID, with Media Type social. These are separate identifiers; the alias/task ID is not replaced by the conversation ID.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Apple Messages for Business Event | onBegin (`onbegin`) → 3: Search Conversation |
| 3: Search Conversation | conversationClosed, conversationOnHold, conversationInQueue, conversationActive → 4: Close Task; onInvalidData (`oninvaliddata`) → End 165 → Error; onError (`onerror`) → End 166 → Error; onInvalidChoice (`oninvalidchoice`) → End 167 → Error; onauthorizationfail → End 168 → Error; onTimeout (`ontimeout`) → End 169 → Error; noConversationFound → End 170 → Success |
| 4: Close Task | onInvalidData (`oninvaliddata`) → End 64 → Error; onError (`onerror`) → End 65 → Error; onInvalidChoice (`oninvalidchoice`) → End 66 → Error; onauthorizationfail → End 67 → Error; Error → End 68 → Error; onTimeout (`ontimeout`) → End 69 → Error; Success → End 152 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Apple Messages for Business Event | `$(n2.abc.abcUserId)` | 3: Search Conversation / extraParamsData.customeraddress; 3: Search Conversation / nodeInput.customeraddress; 3: Search Conversation / request_body[1].value |
| 3: Search Conversation | `$(n3.aliasId)` | 4: Close Task / nodeInput.ID; 4: Close Task / nodeInput.Task Id; 4: Close Task / path_parameters[1].value; 4: Close Task / request_body[0].value |
| 3: Search Conversation | `$(n3.conversationId)` | 4: Close Task / nodeInput.Conversation ID; 4: Close Task / request_body[2].value |

### Boundaries and adaptation

The sample name Unsubscribe describes Apple conversation-close handling. The graph does not show an SMS opt-out list, consent database, subscription API or cross-channel contact-policy update. It also deliberately attempts Close Task for the conversationClosed search result; do not silently remove that path from the observed design. No retries are present, and imported authorization/tenant bindings are examples. Terminal configuration is not proof a real task was closed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-emailattachmentdropnotification"></a>

## EmailAttachmentDropNotification.workflow

Observed 2026-09-09T00:02:36.379Z. [Captured model](../evidence/sample-flows/observed/wxcc-emailattachmentdropnotification.json); [complete graph summary](sample-flows/summaries/wxcc-emailattachmentdropnotification.json). Runtime tested: **no**.

Email Start 2 enters Parse Variables 9. Its attachmentsDropped result sends notification Email 1980 before Resolve Conversation 1894; noAttachmentsDropped goes directly to Resolve. All three notification outcomes—onsuccess, onerror, and onpolicyfail—continue to Resolve. Created/reopened conversations send acknowledgment 1898, then Queue Task 1851; Queued sends Email 39. Resolve appended/accepted outcomes terminate rather than enqueue the same conversation again. Queue failures enter Close Task 1854 and then error Email 322; Resolve timeout Branch 1910 closes only its Create/Reopen Path.

Useful handoffs: Start preserves `$(n2.email.emailId)`, `$(n2.email.inReplyTo)`, subject, message variants, attachments, and scan metadata. Evaluate builds detailsJson for Resolve and collects attachment names from security failure data. It selects attachmentsDropped when the reason contains PCI: Failed:, Malware: Failed:, or System Alert; the notification body is `$(droppedAttachmentNotificationMessage)`. Resolve supplies taskId/conversationOperation; Queue and Close consume `$(taskId)` and the stored `$(conversationId)`. Outbound email destinations are `$(n2.email.emailId)` with `$(subject)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Email Event | onBegin (`onbegin`) → 9: Parse Variables |
| 9: Parse Variables | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1832: Email; noAttachmentsDropped → 1894: Resolve Conversation; attachmentsDropped → 1980: Email |
| 39: Email | No outgoing route captured |
| 322: Email | No outgoing route captured |
| 1832: Email | onError (`onerror`) → End 2004 → Error; onPolicyFail (`onpolicyfail`) → End 2005 → Error; onSuccess (`onsuccess`) → End 2006 → Success |
| 1851: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1854: Close Task; Queued → 39: Email |
| 1854: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 322: Email |
| 1894: Resolve Conversation | created, reopened → 1898: Email; onTimeout (`ontimeout`) → 1910: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1832: Email; appended → End 1993 → Success; accepted → End 1994 → Success |
| 1898: Email | onSuccess (`onsuccess`), onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1851: Queue Task; onPolicyFail (`onpolicyfail`) → End 2007 → Error; onError (`onerror`) → End 2008 → Error; onSuccess (`onsuccess`) → End 2009 → Success |
| 1910: Branch | Create/Reopen Path → 1854: Close Task; onError (`onerror`) → End 1931 → Error; Append Path → End 1932 → Success; None of the above → End 1933 → Error |
| 1980: Email | onError (`onerror`), onPolicyFail (`onpolicyfail`), onSuccess (`onsuccess`) → 1894: Resolve Conversation |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Email Event | `$(n2.email.pciInfo.nonPCIComplianceReason)` | 2: Configure Email Event / transition_actions[0].value; 2: Configure Email Event / transition_actions[28].value; 2: Configure Email Event / transition_actions[31].value |
| 2: Configure Email Event | `$(n2.email.attachments)` | 2: Configure Email Event / transition_actions[1].value; 2: Configure Email Event / transition_actions[22].value |
| 2: Configure Email Event | `$(n2.email.message)` | 2: Configure Email Event / transition_actions[18].value; 2: Configure Email Event / transition_actions[2].value |
| 2: Configure Email Event | `$(n2.email.htmlMessage)` | 2: Configure Email Event / transition_actions[19].value; 2: Configure Email Event / transition_actions[3].value |
| 2: Configure Email Event | `$(n2.email.strippedText)` | 2: Configure Email Event / transition_actions[20].value; 2: Configure Email Event / transition_actions[4].value |
| 2: Configure Email Event | `$(n2.email.strippedHTML)` | 2: Configure Email Event / transition_actions[21].value; 2: Configure Email Event / transition_actions[5].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isPCIValidationDone)` | 2: Configure Email Event / transition_actions[30].value; 2: Configure Email Event / transition_actions[6].value |
| 2: Configure Email Event | `$(n2.email.recipient)` | 2: Configure Email Event / transition_actions[7].value |
| 2: Configure Email Event | `$(n2.email.appId)` | 2: Configure Email Event / transition_actions[8].value |
| 2: Configure Email Event | `$(n2.email.assetType)` | 2: Configure Email Event / transition_actions[9].value |
| 2: Configure Email Event | `$(n2.email.senderName)` | 2: Configure Email Event / transition_actions[10].value |
| 2: Configure Email Event | `$(n2.email.emailId)` | 1832: Email / destination; 1898: Email / destination; 1980: Email / destination; 2: Configure Email Event / transition_actions[11].value; 322: Email / destination; 39: Email / destination |
| 2: Configure Email Event | `$(n2.email.toAddresses)` | 2: Configure Email Event / transition_actions[12].value |
| 2: Configure Email Event | `$(n2.email.ccRecipients)` | 2: Configure Email Event / transition_actions[13].value |
| 2: Configure Email Event | `$(n2.email.bccRecipients)` | 2: Configure Email Event / transition_actions[14].value |
| 2: Configure Email Event | `$(n2.email.subject)` | 2: Configure Email Event / transition_actions[15].value |
| 2: Configure Email Event | `$(n2.email.inReplyTo)` | 2: Configure Email Event / transition_actions[16].value |
| 2: Configure Email Event | `$(n2.service.serviceKey)` | 2: Configure Email Event / transition_actions[23].value |
| 2: Configure Email Event | `$(n2.email.timestamp)` | 2: Configure Email Event / transition_actions[24].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isAttachmentEnabled)` | 2: Configure Email Event / transition_actions[25].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[26].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isPCICompliance)` | 2: Configure Email Event / transition_actions[27].value |
| 2: Configure Email Event | `$(n2.email.transId)` | 2: Configure Email Event / transition_actions[29].value; 2: Configure Email Event / transition_actions[32].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.isSecurityCompliance)` | 2: Configure Email Event / transition_actions[33].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[34].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.isSecurityValidationDone)` | 2: Configure Email Event / transition_actions[35].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.securityFailedReason)` | 2: Configure Email Event / transition_actions[36].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.isMalwareValidationDone)` | 2: Configure Email Event / transition_actions[37].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.isMalwareCompliance)` | 2: Configure Email Event / transition_actions[38].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.malwareFailedReason)` | 2: Configure Email Event / transition_actions[39].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[40].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1894: Resolve Conversation / extraParamsData.details; 1894: Resolve Conversation / request_body[6].value; 9: Parse Variables / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(droppedAttachmentNotificationMessage)` | 1980: Email / body; 9: Parse Variables / transition_actions[1].value |
| custom variable; writers 2: Configure Email Event | `$(bizemailid)` | 1832: Email / fromname; 1898: Email / fromname; 1980: Email / fromname; 322: Email / fromname; 39: Email / fromname |
| custom variable; writers 2: Configure Email Event | `$(subject)` | 1832: Email / subject; 1898: Email / subject; 1980: Email / subject; 322: Email / subject; 39: Email / subject |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1832: Email / body; 322: Email / body |
| External/system/custom value; producer not established here | `$(taskId)` | 1851: Queue Task / extraParamsData.id; 1851: Queue Task / path_parameters[1].value; 1851: Queue Task / request_body[0].value; 1854: Close Task / nodeInput.ID; 1854: Close Task / nodeInput.Task Id; 1854: Close Task / path_parameters[1].value; 1854: Close Task / request_body[0].value; 1894: Resolve Conversation / transition_actions[0].value; 1910: Branch / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1851: Queue Task / extraParamsData.conversationid; 1851: Queue Task / request_body[3].value; 1854: Close Task / nodeInput.Conversation ID; 1854: Close Task / request_body[2].value |
| custom variable; writers 2: Configure Email Event | `$(transId)` | 1894: Resolve Conversation / extraParamsData.trackingId; 1894: Resolve Conversation / extraParamsData.transId; 1894: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 1894: Resolve Conversation / transition_actions[1].value; 1910: Branch / expression; 1910: Branch / outcomes[0].conditions[0].varaible; 1910: Branch / outcomes[0].conditions[1].varaible; 1910: Branch / outcomes[1].conditions[0].varaible; 1910: Branch / transition_actions[1].value |

### Boundaries and adaptation

The model constructs notices from scan results; it does not itself scan attachments. Notification failure does not block routing. Emails use createnew, so carrying inReplyTo inside Resolve details does not prove outbound threading. No conversation wait/retry loop exists. Some End records overlap explicit acknowledgment routes or reference absent parent 1878; they are retained as model residue, not silently resolved. The conversationId is a placeholder, and resource bindings need adaptation. Nothing was sent or executed; this internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 39: Email / `onerror` (declared target count 1); 322: Email / `onerror` (declared target count 1).
End records reference absent producer nodes: 1878. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-emailinboundflow"></a>

## EmailInboundFlow.workflow

Observed 2026-09-09T00:04:52.983Z. [Captured model](../evidence/sample-flows/observed/wxcc-emailinboundflow.json); [complete graph summary](sample-flows/summaries/wxcc-emailinboundflow.json). Runtime tested: **no**.

Email Start 2 copies inbound context and enters Parse Variables 9. Numeric outcome 1/success connects to Resolve Conversation 1894. Created/reopened outcomes send Email 1898, then Queue Task 1851 on send success, error, or policy failure. Queue event Queued sends acknowledgment Email 39. Resolve appended and accepted outcomes terminate via End associations; they do not repeat queuing. Queue errors/timeouts attempt Close Task 1854, whose outcomes send error Email 322. Resolve timeout Branch 1910 distinguishes create/reopen cleanup from an append path that terminates.

Useful handoffs: The event provides `$(n2.email.emailId)`, `$(n2.email.inReplyTo)`, recipients, subject, body variants, attachments, and scan metadata. Evaluate normalizes attachment names/URLs and dropped flags, supplies defaults for missing sender/subject, and assembles detailsJson containing messageDetails plus PCI, malware, and security results. Resolve consumes `$(transId)` and `$(detailsJson)` and exposes taskId/conversationOperation. Queue/Close use `$(taskId)` and `$(conversationId)`. Customer emails use destination `$(n2.email.emailId)`, subject `$(subject)`, and createnew.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Email Event | onBegin (`onbegin`) → 9: Parse Variables |
| 9: Parse Variables | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1832: Email; success  (`1`) → 1894: Resolve Conversation |
| 39: Email | No outgoing route captured |
| 322: Email | No outgoing route captured |
| 1832: Email | onError (`onerror`) → End 2000 → Error; onPolicyFail (`onpolicyfail`) → End 2001 → Error; onSuccess (`onsuccess`) → End 2002 → Success |
| 1851: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1854: Close Task; Queued → 39: Email |
| 1854: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 322: Email |
| 1894: Resolve Conversation | created, reopened → 1898: Email; onTimeout (`ontimeout`) → 1910: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1832: Email; appended → End 2013 → Success; accepted → End 2014 → Success |
| 1898: Email | onSuccess (`onsuccess`), onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1851: Queue Task; onPolicyFail (`onpolicyfail`) → End 2003 → Error; onError (`onerror`) → End 2004 → Error; onSuccess (`onsuccess`) → End 2005 → Success |
| 1910: Branch | Create/Reopen Path → 1854: Close Task; onError (`onerror`) → End 1931 → Error; Append Path → End 1932 → Success; None of the above → End 1933 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Email Event | `$(n2.email.pciInfo.nonPCIComplianceReason)` | 2: Configure Email Event / transition_actions[0].value; 2: Configure Email Event / transition_actions[28].value; 2: Configure Email Event / transition_actions[31].value |
| 2: Configure Email Event | `$(n2.email.attachments)` | 2: Configure Email Event / transition_actions[1].value; 2: Configure Email Event / transition_actions[22].value |
| 2: Configure Email Event | `$(n2.email.message)` | 2: Configure Email Event / transition_actions[18].value; 2: Configure Email Event / transition_actions[2].value |
| 2: Configure Email Event | `$(n2.email.htmlMessage)` | 2: Configure Email Event / transition_actions[19].value; 2: Configure Email Event / transition_actions[3].value |
| 2: Configure Email Event | `$(n2.email.strippedText)` | 2: Configure Email Event / transition_actions[20].value; 2: Configure Email Event / transition_actions[4].value |
| 2: Configure Email Event | `$(n2.email.strippedHTML)` | 2: Configure Email Event / transition_actions[21].value; 2: Configure Email Event / transition_actions[5].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isPCIValidationDone)` | 2: Configure Email Event / transition_actions[30].value; 2: Configure Email Event / transition_actions[6].value |
| 2: Configure Email Event | `$(n2.email.recipient)` | 2: Configure Email Event / transition_actions[7].value |
| 2: Configure Email Event | `$(n2.email.appId)` | 2: Configure Email Event / transition_actions[8].value |
| 2: Configure Email Event | `$(n2.email.assetType)` | 2: Configure Email Event / transition_actions[9].value |
| 2: Configure Email Event | `$(n2.email.senderName)` | 2: Configure Email Event / transition_actions[10].value |
| 2: Configure Email Event | `$(n2.email.emailId)` | 1832: Email / destination; 1898: Email / destination; 2: Configure Email Event / transition_actions[11].value; 322: Email / destination; 39: Email / destination |
| 2: Configure Email Event | `$(n2.email.toAddresses)` | 2: Configure Email Event / transition_actions[12].value |
| 2: Configure Email Event | `$(n2.email.ccRecipients)` | 2: Configure Email Event / transition_actions[13].value |
| 2: Configure Email Event | `$(n2.email.bccRecipients)` | 2: Configure Email Event / transition_actions[14].value |
| 2: Configure Email Event | `$(n2.email.subject)` | 2: Configure Email Event / transition_actions[15].value |
| 2: Configure Email Event | `$(n2.email.inReplyTo)` | 2: Configure Email Event / transition_actions[16].value |
| 2: Configure Email Event | `$(n2.service.serviceKey)` | 2: Configure Email Event / transition_actions[23].value |
| 2: Configure Email Event | `$(n2.email.timestamp)` | 2: Configure Email Event / transition_actions[24].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isAttachmentEnabled)` | 2: Configure Email Event / transition_actions[25].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[26].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isPCICompliance)` | 2: Configure Email Event / transition_actions[27].value |
| 2: Configure Email Event | `$(n2.email.transId)` | 2: Configure Email Event / transition_actions[29].value; 2: Configure Email Event / transition_actions[32].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.isSecurityCompliance)` | 2: Configure Email Event / transition_actions[33].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[34].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.isSecurityValidationDone)` | 2: Configure Email Event / transition_actions[35].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.securityFailedReason)` | 2: Configure Email Event / transition_actions[36].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.isMalwareValidationDone)` | 2: Configure Email Event / transition_actions[37].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.isMalwareCompliance)` | 2: Configure Email Event / transition_actions[38].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.malwareFailedReason)` | 2: Configure Email Event / transition_actions[39].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[40].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1894: Resolve Conversation / extraParamsData.details; 1894: Resolve Conversation / nodeInput.details; 1894: Resolve Conversation / request_body[6].value; 9: Parse Variables / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(int)` | 9: Parse Variables / transition_actions[1].value |
| custom variable; writers 2: Configure Email Event | `$(bizemailid)` | 1832: Email / fromname; 1898: Email / fromname; 322: Email / fromname; 39: Email / fromname |
| custom variable; writers 2: Configure Email Event | `$(subject)` | 1832: Email / subject; 1898: Email / subject; 322: Email / subject; 39: Email / subject |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1832: Email / body; 322: Email / body |
| External/system/custom value; producer not established here | `$(taskId)` | 1851: Queue Task / extraParamsData.id; 1851: Queue Task / nodeInput.id; 1851: Queue Task / path_parameters[1].value; 1851: Queue Task / request_body[0].value; 1854: Close Task / nodeInput.ID; 1854: Close Task / nodeInput.Task Id; 1854: Close Task / path_parameters[1].value; 1854: Close Task / request_body[0].value; 1894: Resolve Conversation / transition_actions[0].value; 1910: Branch / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1851: Queue Task / extraParamsData.conversationid; 1851: Queue Task / nodeInput.conversationid; 1851: Queue Task / request_body[3].value; 1854: Close Task / nodeInput.Conversation ID; 1854: Close Task / request_body[2].value |
| custom variable; writers 2: Configure Email Event | `$(transId)` | 1894: Resolve Conversation / extraParamsData.trackingId; 1894: Resolve Conversation / extraParamsData.transId; 1894: Resolve Conversation / nodeInput.trackingId; 1894: Resolve Conversation / nodeInput.transId; 1894: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 1894: Resolve Conversation / transition_actions[1].value; 1910: Branch / expression; 1910: Branch / outcomes[0].conditions[0].varaible; 1910: Branch / outcomes[0].conditions[1].varaible; 1910: Branch / outcomes[1].conditions[0].varaible; 1910: Branch / transition_actions[1].value |

### Boundaries and adaptation

This processes one inbound email event; no Receive loop or AI Agent node appears. A resolved acknowledgment precedes queuing and does not prove a business issue was resolved. The retained conversationId is a placeholder, while selected queue/flow values are sample bindings. Some End records overlap explicit acknowledgment routes or name absent parent 1878. Outbound threading and attachment edge cases remain untested. No message or task operation was invoked; the internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 39: Email / `onerror` (declared target count 1); 322: Email / `onerror` (declared target count 1).
End records reference absent producer nodes: 1878. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-emailinboundsampleflowwithcontactpriority"></a>

## EmailInboundSampleFlowWithContactPriority.workflow

Observed 2026-09-09T00:03:49.819Z. [Captured model](../evidence/sample-flows/observed/wxcc-emailinboundsampleflowwithcontactpriority.json); [complete graph summary](sample-flows/summaries/wxcc-emailinboundsampleflowwithcontactpriority.json). Runtime tested: **no**.

Email Start 2 → Parse Variables 9 → Resolve Conversation 1894 establishes the inbound email/task context. Created/reopened outcomes send acknowledgment Email 1898 and continue to Determine Contact Priority 1980 whether sending succeeds, errors, or fails policy. The Evaluate result and both error outcomes all continue to Queue Task 1851. Queued sends Email 39. Queue failure closes task 1854 and sends error Email 322; Resolve appended/accepted outcomes terminate. Resolve timeout enters Branch 1910, whose Create/Reopen Path attempts Close Task.

Useful handoffs: Inbound sender, thread references, text/HTML, attachments, and scan metadata become detailsJson for Resolve using `$(transId)`. Priority Evaluate initializes contactPriority to string 10, sets 1 when customerEmailId equals priorityOneCustomer, and 5 when it equals priorityFiveCustomer. Queue request_body maps contactPriority to `$(contactPriority)`, alongside `$(taskId)`, `$(conversationId)`, and email media type. Queue nodeInput separately retains a blank contactPriority. All outbound emails address `$(n2.email.emailId)` and retain `$(subject)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Email Event | onBegin (`onbegin`) → 9: Parse Variables |
| 9: Parse Variables | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1832: Email; success  (`1`) → 1894: Resolve Conversation |
| 39: Email | No outgoing route captured |
| 322: Email | No outgoing route captured |
| 1832: Email | onError (`onerror`) → End 1993 → Error; onPolicyFail (`onpolicyfail`) → End 1994 → Error; onSuccess (`onsuccess`) → End 1995 → Success |
| 1851: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1854: Close Task; Queued → 39: Email |
| 1854: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 322: Email |
| 1894: Resolve Conversation | created, reopened → 1898: Email; onTimeout (`ontimeout`) → 1910: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1832: Email; appended → End 2002 → Success; accepted → End 2003 → Success |
| 1898: Email | onSuccess (`onsuccess`), onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1980: Determine Contact Priority; onPolicyFail (`onpolicyfail`) → End 1996 → Error; onError (`onerror`) → End 1997 → Error; onSuccess (`onsuccess`) → End 1998 → Success |
| 1910: Branch | Create/Reopen Path → 1854: Close Task; onError (`onerror`) → End 1931 → Error; Append Path → End 1932 → Success; None of the above → End 1933 → Error |
| 1980: Determine Contact Priority | success (`1`), onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1851: Queue Task |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Email Event | `$(n2.email.pciInfo.nonPCIComplianceReason)` | 2: Configure Email Event / transition_actions[0].value; 2: Configure Email Event / transition_actions[28].value; 2: Configure Email Event / transition_actions[31].value |
| 2: Configure Email Event | `$(n2.email.attachments)` | 2: Configure Email Event / transition_actions[1].value; 2: Configure Email Event / transition_actions[22].value |
| 2: Configure Email Event | `$(n2.email.message)` | 2: Configure Email Event / transition_actions[18].value; 2: Configure Email Event / transition_actions[2].value |
| 2: Configure Email Event | `$(n2.email.htmlMessage)` | 2: Configure Email Event / transition_actions[19].value; 2: Configure Email Event / transition_actions[3].value |
| 2: Configure Email Event | `$(n2.email.strippedText)` | 2: Configure Email Event / transition_actions[20].value; 2: Configure Email Event / transition_actions[4].value |
| 2: Configure Email Event | `$(n2.email.strippedHTML)` | 2: Configure Email Event / transition_actions[21].value; 2: Configure Email Event / transition_actions[5].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isPCIValidationDone)` | 2: Configure Email Event / transition_actions[30].value; 2: Configure Email Event / transition_actions[6].value |
| 2: Configure Email Event | `$(n2.email.recipient)` | 2: Configure Email Event / transition_actions[7].value |
| 2: Configure Email Event | `$(n2.email.appId)` | 2: Configure Email Event / transition_actions[8].value |
| 2: Configure Email Event | `$(n2.email.assetType)` | 2: Configure Email Event / transition_actions[9].value |
| 2: Configure Email Event | `$(n2.email.senderName)` | 2: Configure Email Event / transition_actions[10].value |
| 2: Configure Email Event | `$(n2.email.emailId)` | 1832: Email / destination; 1898: Email / destination; 2: Configure Email Event / transition_actions[11].value; 322: Email / destination; 39: Email / destination |
| 2: Configure Email Event | `$(n2.email.toAddresses)` | 2: Configure Email Event / transition_actions[12].value |
| 2: Configure Email Event | `$(n2.email.ccRecipients)` | 2: Configure Email Event / transition_actions[13].value |
| 2: Configure Email Event | `$(n2.email.bccRecipients)` | 2: Configure Email Event / transition_actions[14].value |
| 2: Configure Email Event | `$(n2.email.subject)` | 2: Configure Email Event / transition_actions[15].value |
| 2: Configure Email Event | `$(n2.email.inReplyTo)` | 2: Configure Email Event / transition_actions[16].value |
| 2: Configure Email Event | `$(n2.service.serviceKey)` | 2: Configure Email Event / transition_actions[23].value |
| 2: Configure Email Event | `$(n2.email.timestamp)` | 2: Configure Email Event / transition_actions[24].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isAttachmentEnabled)` | 2: Configure Email Event / transition_actions[25].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[26].value |
| 2: Configure Email Event | `$(n2.email.pciInfo.isPCICompliance)` | 2: Configure Email Event / transition_actions[27].value |
| 2: Configure Email Event | `$(n2.email.transId)` | 2: Configure Email Event / transition_actions[29].value; 2: Configure Email Event / transition_actions[32].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.isSecurityCompliance)` | 2: Configure Email Event / transition_actions[33].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[34].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.isSecurityValidationDone)` | 2: Configure Email Event / transition_actions[35].value |
| 2: Configure Email Event | `$(n2.email.securityscaninfo.securityFailedReason)` | 2: Configure Email Event / transition_actions[36].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.isMalwareValidationDone)` | 2: Configure Email Event / transition_actions[37].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.isMalwareCompliance)` | 2: Configure Email Event / transition_actions[38].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.malwareFailedReason)` | 2: Configure Email Event / transition_actions[39].value |
| 2: Configure Email Event | `$(n2.email.malwareinfo.droppedAttachmentCount)` | 2: Configure Email Event / transition_actions[40].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1894: Resolve Conversation / extraParamsData.details; 1894: Resolve Conversation / nodeInput.details; 1894: Resolve Conversation / request_body[6].value; 9: Parse Variables / transition_actions[0].value |
| custom variable; writers 2: Configure Email Event | `$(bizemailid)` | 1832: Email / fromname; 1898: Email / fromname; 322: Email / fromname; 39: Email / fromname |
| custom variable; writers 2: Configure Email Event | `$(subject)` | 1832: Email / subject; 1898: Email / subject; 322: Email / subject; 39: Email / subject |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1832: Email / body; 322: Email / body |
| External/system/custom value; producer not established here | `$(taskId)` | 1851: Queue Task / extraParamsData.id; 1851: Queue Task / nodeInput.id; 1851: Queue Task / path_parameters[1].value; 1851: Queue Task / request_body[0].value; 1854: Close Task / nodeInput.ID; 1854: Close Task / nodeInput.Task Id; 1854: Close Task / path_parameters[1].value; 1854: Close Task / request_body[0].value; 1894: Resolve Conversation / transition_actions[0].value; 1910: Branch / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1851: Queue Task / extraParamsData.conversationid; 1851: Queue Task / nodeInput.conversationid; 1851: Queue Task / request_body[3].value; 1854: Close Task / nodeInput.Conversation ID; 1854: Close Task / request_body[2].value |
| External/system/custom value; producer not established here | `$(contactPriority)` | 1851: Queue Task / extraParamsData.contactPriority; 1851: Queue Task / request_body[6].value; 1980: Determine Contact Priority / transition_actions[0].value |
| custom variable; writers 2: Configure Email Event | `$(transId)` | 1894: Resolve Conversation / extraParamsData.trackingId; 1894: Resolve Conversation / extraParamsData.transId; 1894: Resolve Conversation / nodeInput.trackingId; 1894: Resolve Conversation / nodeInput.transId; 1894: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 1894: Resolve Conversation / transition_actions[1].value; 1910: Branch / expression; 1910: Branch / outcomes[0].conditions[0].varaible; 1910: Branch / outcomes[0].conditions[1].varaible; 1910: Branch / outcomes[1].conditions[0].varaible; 1910: Branch / transition_actions[1].value |

### Boundaries and adaptation

The priority list is two stored example addresses, not customer classification logic or an entitlement policy. The blank-versus-dynamic priority representations require verification when adapting. Queuing continues even if priority evaluation fails, so a valid assigned priority is not established on every path. End residue overlaps acknowledgment edges and includes absent parent 1878. Resolve nodeInput contains an explicit flow-ID placeholder; conversationId is also a placeholder. No flow, queue action, or email was executed. This internal capture is evidence, not an importable public schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 39: Email / `onerror` (declared target count 1); 322: Email / `onerror` (declared target count 1).
End records reference absent producer nodes: 1878. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-facebookattachmentdropnotification"></a>

## FacebookAttachmentDropNotification.workflow

Observed 2026-09-09T00:06:28.189Z. [Captured model](../evidence/sample-flows/observed/wxcc-facebookattachmentdropnotification.json); [complete graph summary](sample-flows/summaries/wxcc-facebookattachmentdropnotification.json). Runtime tested: **no**.

Messenger Start 2 copies message, identity, attachment and scan fields into custom variables before Evaluate 9 constructs `detailsJson` and chooses an attachment-notification result. `attachmentsDropped` sends Messenger 1969; all its captured outcomes continue to Resolve Conversation 1897. `noAttachmentsDropped` enters 1897 directly. Created/reopened conversations send acknowledgment 1899, then Queue Task 1701 regardless of acknowledgment delivery outcome; `Queued` sends confirmation 1912. Appended and accepted events terminate Success. Resolve timeout branches at 1939: created/reopened attempts Close Task 1703, appended terminates Success, and other/error results terminate Error. Queue failures also close the task; every captured close outcome sends error notice 1651. Other parse/resolve errors use notice 1662.

Useful handoffs: Start supplies `$(n2.messenger.psId)` to each send. Evaluate 9 reads scan-reason custom variables, selecting sensitive-content, malware or processing-error text into `droppedAttachmentNotificationMessage`, then passes `$(detailsJson)` to 1897. Queue/close use `$(taskId)` and `$(conversationId)`; Resolve declares `taskId` and `conversationOperation` outputs, while the timeout branch consumes the unqualified operation variable. These custom bindings must be reconciled with the actual integration callback contract.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Incoming Message | onBegin (`onbegin`) → 9: Parse Variables |
| 9: Parse Variables | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1662: Messenger; noAttachmentsDropped → 1897: Resolve Conversation; attachmentsDropped → 1969: Messenger |
| 1651: Messenger | No outgoing route captured |
| 1662: Messenger | No outgoing route captured |
| 1701: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1703: Close Task; Queued → 1912: Queued |
| 1703: Close Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Success, Error, onauthorizationfail → 1651: Messenger |
| 1897: Resolve Conversation | created, reopened → 1899: Messenger; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1662: Messenger; onTimeout (`ontimeout`) → 1939: Branch; appended → End 1995 → Success; accepted → End 1996 → Success |
| 1899: Messenger | onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`), onError (`onerror`) → 1701: Queue Task |
| 1912: Queued | onError (`onerror`) → End 1922 → Error; onPolicyFail (`onpolicyfail`) → End 1923 → Error; onSuccess (`onsuccess`) → End 1924 → Success |
| 1939: Branch | Create/Reopen Path → 1703: Close Task; onError (`onerror`) → End 1952 → Error; Append Path → End 1953 → Success; None of the above → End 1954 → Error |
| 1969: Messenger | onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`), onError (`onerror`) → 1897: Resolve Conversation |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Incoming Message | `$(n2.messenger.attachments)` | 2: Incoming Message / transition_actions[0].value; 2: Incoming Message / transition_actions[15].value |
| 2: Incoming Message | `$(n2.messenger.message)` | 2: Incoming Message / transition_actions[14].value; 2: Incoming Message / transition_actions[1].value |
| 2: Incoming Message | `$(n2.messenger.attachmentUrl)` | 2: Incoming Message / transition_actions[2].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.nonPCIComplianceReason)` | 2: Incoming Message / transition_actions[17].value; 2: Incoming Message / transition_actions[3].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.isPCIValidationDone)` | 2: Incoming Message / transition_actions[16].value; 2: Incoming Message / transition_actions[4].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.isPCICompliance)` | 2: Incoming Message / transition_actions[5].value |
| 2: Incoming Message | `$(n2.messenger.name)` | 2: Incoming Message / transition_actions[6].value |
| 2: Incoming Message | `$(n2.messenger.appId)` | 2: Incoming Message / transition_actions[7].value |
| 2: Incoming Message | `$(n2.messenger.psId)` | 1651: Messenger / destination; 1662: Messenger / destination; 1899: Messenger / destination; 1912: Queued / destination; 1969: Messenger / destination; 2: Incoming Message / transition_actions[8].value |
| 2: Incoming Message | `$(n2.messenger.ts)` | 2: Incoming Message / transition_actions[9].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.isAttachmentEnabled)` | 2: Incoming Message / transition_actions[10].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.droppedAttachmentCount)` | 2: Incoming Message / transition_actions[11].value |
| 2: Incoming Message | `$(n2.service.serviceKey)` | 2: Incoming Message / transition_actions[12].value |
| 2: Incoming Message | `$(n2.messenger.transId)` | 2: Incoming Message / transition_actions[13].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.isSecurityValidationDone)` | 2: Incoming Message / transition_actions[18].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.securityFailedReason)` | 2: Incoming Message / transition_actions[19].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.droppedAttachmentCount)` | 2: Incoming Message / transition_actions[20].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.isSecurityCompliance)` | 2: Incoming Message / transition_actions[21].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.isMalwareValidationDone)` | 2: Incoming Message / transition_actions[22].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.isMalwareCompliance)` | 2: Incoming Message / transition_actions[23].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.malwareFailedReason)` | 2: Incoming Message / transition_actions[24].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.droppedAttachmentCount)` | 2: Incoming Message / transition_actions[25].value |
| External/system/custom value; producer not established here | `$(droppedAttachmentNotificationMessage)` | 1969: Messenger / fb_text; 9: Parse Variables / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1651: Messenger / fb_text; 1662: Messenger / fb_text |
| External/system/custom value; producer not established here | `$(taskId)` | 1701: Queue Task / extraParamsData.id; 1701: Queue Task / path_parameters[1].value; 1701: Queue Task / request_body[0].value; 1703: Close Task / nodeInput.ID; 1703: Close Task / nodeInput.Task Id; 1703: Close Task / path_parameters[1].value; 1703: Close Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1701: Queue Task / extraParamsData.conversationid; 1701: Queue Task / request_body[3].value; 1703: Close Task / nodeInput.Conversation ID; 1703: Close Task / request_body[2].value |
| custom variable; writers 2: Incoming Message | `$(transId)` | 1897: Resolve Conversation / extraParamsData.trackingId; 1897: Resolve Conversation / extraParamsData.transId; 1897: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1897: Resolve Conversation / extraParamsData.details; 1897: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 1939: Branch / expression; 1939: Branch / outcomes[0].conditions[0].varaible; 1939: Branch / outcomes[0].conditions[1].varaible; 1939: Branch / outcomes[1].conditions[0].varaible |

### Boundaries and adaptation

No Receive node or retry loop is captured. Evaluate uses `appId` while the captured Start assignment/default is `appid`, and Start assigns timestamp from `$(n2.messenger.ts)` although its output list names `messenger.timestamp`; preserve these discrepancies for adaptation. Some terminal bindings name uncaptured producers 1980/1825, and notice-node error routes are absent. Placeholder identities and conversation defaults are not deployable bindings. Runtime remains untested.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1651: Messenger / `onerror` (declared target count 1); 1662: Messenger / `onerror` (declared target count 1).
End records reference absent producer nodes: 1825, 1980. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-facebookclosewithwxmflow"></a>

## FacebookCloseWithWxmFlow.workflow

Observed 2026-09-09T00:06:34.924Z. [Captured model](../evidence/sample-flows/observed/wxcc-facebookclosewithwxmflow.json); [complete graph summary](sample-flows/summaries/wxcc-facebookclosewithwxmflow.json). Runtime tested: **no**.

Task Closed Start 2 enters Branch 1406. Only a request-body match for string-valued `overrideDefaultClose` true together with `mediaChannel` facebook continues; the unmatched branch ends Success. Evaluate 57 parses the task variables and request body, then WXM 1487 creates a survey link. Success sends Messenger 896; successful delivery appends the outbound survey at 902. Survey-generation failure, send failure and every captured append outcome converge on Close Conversation 629. Successful closure, or failure code 4547 recognized by Branch 114, reaches Close Task 653. Its Success enters owner Branch 246: an owner triggers Screen Pop 720, otherwise the flow ends Success. Other close failures use Close Task 671 with failure context.

Useful handoffs: Start stores `$(n2.webex.variables)` as `response` and `$(n2.webex.RequestBody)` as `requestBody`; Evaluate persists parsed `mediaResourceId` and customer/agent fields on leave. Both Messenger 896 and Append 902 consume `$(n1487.surveyURL)`; the send targets `$(n2.webex.origin)`, and append/close use `$(mediaResourceId)`. Task closure and Screen Pop consume `$(n2.webex.taskId)` and owner; the screen pop includes parsed `$(CustomerId)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: WxCC Task v2 | onBegin (`onbegin`) → 1406: Branch |
| 57: Evaluate | Success (`1`) → 1487: WXM |
| 114: Branch | Conversation already closed → 653: Close Task; onError (`onerror`), None of the above → 671: Close Task |
| 246: Branch | Owner present → 720: Screen Pop; onError (`onerror`) → End 413 → Error; None of the above → End 414 → Success |
| 629: Close Conversation | onConversationClosed → 653: Close Task; onCloseConversationFailure, onFailure → 114: Branch; onError (`onerror`), onInvalidData (`oninvaliddata`), onauthorizationfail, onTimeout (`ontimeout`), onInvalidChoice (`oninvalidchoice`) → 671: Close Task |
| 653: Close Task | Success → 246: Branch; onauthorizationfail → End 871 → Error |
| 671: Close Task | onauthorizationfail → End 878 → Error |
| 720: Screen Pop | onInvalidData (`oninvaliddata`) → End 852 → Error; onError (`onerror`) → End 853 → Error; onInvalidChoice (`oninvalidchoice`) → End 854 → Error; onScreenPopFailure → End 855 → Error; serviceUnavailable → End 856 → Error; onTimeout (`ontimeout`) → End 857 → Error; onScreenPopSuccess → End 858 → Success; onauthorizationfail → End 893 → Error |
| 896: Messenger | onSuccess (`onsuccess`) → 902: Append Conversation; onPolicyFail (`onpolicyfail`), onError (`onerror`) → 629: Close Conversation |
| 902: Append Conversation | onAppendMessageSuccess, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure, onTimeout (`ontimeout`) → 629: Close Conversation |
| 1406: Branch | OverrideDefaultCloseChecked → 57: Evaluate; onError (`onerror`) → End 1485 → Error; None of the above → End 1486 → Success |
| 1487: WXM | createTokenForTheQuestionnaireOnSuccess → 896: Messenger; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, failedToAddSurveyToken, UserRoleNotAllowedAccessThisResource, APIRequestLimitExceeded, onTimeout (`ontimeout`) → 629: Close Conversation |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: WxCC Task v2 | `$(n2.webex.variables)` | 2: WxCC Task v2 / transition_actions[0].value |
| 2: WxCC Task v2 | `$(n2.webex.RequestBody)` | 1406: Branch / expression; 1406: Branch / outcomes[0].conditions[0].varaible; 2: WxCC Task v2 / transition_actions[1].value |
| custom variable; writers 57: Evaluate | `$(mediaResourceId)` | 57: Evaluate / transition_actions[0].value; 629: Close Conversation / nodeInput.conversation id; 629: Close Conversation / path_parameters[1].value; 653: Close Task / nodeInput.Conversation Id; 653: Close Task / request_body[4].value; 671: Close Task / nodeInput.media resource id; 671: Close Task / request_body[3].value; 902: Append Conversation / extraParamsData.conversationid; 902: Append Conversation / nodeInput.conversationid; 902: Append Conversation / path_parameters[1].value |
| External/system/custom value; producer not established here | `$(agentName)` | 57: Evaluate / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(agentDn)` | 57: Evaluate / transition_actions[2].value |
| External/system/custom value; producer not established here | `$(agentId)` | 57: Evaluate / transition_actions[3].value |
| External/system/custom value; producer not established here | `$(agentSessionId)` | 57: Evaluate / transition_actions[4].value |
| External/system/custom value; producer not established here | `$(teamName)` | 57: Evaluate / transition_actions[5].value |
| External/system/custom value; producer not established here | `$(teamId)` | 57: Evaluate / transition_actions[6].value |
| External/system/custom value; producer not established here | `$(contactId)` | 57: Evaluate / transition_actions[7].value |
| custom variable; writers 57: Evaluate | `$(ani)` | 57: Evaluate / transition_actions[8].value |
| External/system/custom value; producer not established here | `$(dn)` | 57: Evaluate / transition_actions[9].value |
| External/system/custom value; producer not established here | `$(orgId)` | 57: Evaluate / transition_actions[10].value |
| External/system/custom value; producer not established here | `$(queueId)` | 57: Evaluate / transition_actions[11].value |
| External/system/custom value; producer not established here | `$(queueName)` | 57: Evaluate / transition_actions[12].value |
| External/system/custom value; producer not established here | `$(siteId)` | 57: Evaluate / transition_actions[13].value |
| External/system/custom value; producer not established here | `$(customerName)` | 57: Evaluate / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(contactDirection)` | 57: Evaluate / transition_actions[15].value |
| External/system/custom value; producer not established here | `$(mediaType)` | 57: Evaluate / transition_actions[16].value |
| External/system/custom value; producer not established here | `$(mediaChannel)` | 57: Evaluate / transition_actions[17].value |
| External/system/custom value; producer not established here | `$(customerId)` | 57: Evaluate / transition_actions[18].value |
| External/system/custom value; producer not established here | `$(thread)` | 57: Evaluate / transition_actions[19].value |
| External/system/custom value; producer not established here | `$(code)` | 114: Branch / expression; 114: Branch / outcomes[0].conditions[0].varaible; 671: Close Task / nodeInput.reason code; 671: Close Task / request_body[6].value |
| 2: WxCC Task v2 | `$(n2.webex.owner)` | 246: Branch / expression; 246: Branch / outcomes[0].conditions[0].varaible; 671: Close Task / nodeInput.agent ID; 671: Close Task / request_body[2].value; 720: Screen Pop / extraParamsData.agentId; 720: Screen Pop / nodeInput.agentId; 720: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(emptystring)` | 246: Branch / expression; 246: Branch / outcomes[0].conditions[0].value |
| 2: WxCC Task v2 | `$(n2.webex.taskId)` | 653: Close Task / nodeInput.ID; 653: Close Task / nodeInput.Task Id; 653: Close Task / path_parameters[1].value; 653: Close Task / request_body[0].value; 671: Close Task / nodeInput.ID; 671: Close Task / nodeInput.Task ID; 671: Close Task / path_parameters[1].value; 671: Close Task / request_body[0].value; 720: Screen Pop / extraParamsData.transid; 720: Screen Pop / nodeInput.transid; 720: Screen Pop / request_body[0].value |
| 2: WxCC Task v2 | `$(n2.webex.queue)` | 653: Close Task / nodeInput.Queue Id; 653: Close Task / request_body[3].value |
| 2: WxCC Task v2 | `$(n2.webex.mediaType)` | 653: Close Task / nodeInput.Media Type; 653: Close Task / request_body[5].value; 671: Close Task / nodeInput.Media type; 671: Close Task / request_body[4].value |
| External/system/custom value; producer not established here | `$(description)` | 671: Close Task / nodeInput.reason; 671: Close Task / request_body[5].value |
| custom variable; writers 57: Evaluate | `$(CustomerId)` | 720: Screen Pop / extraParamsData.queryParameters.customerId; 720: Screen Pop / nodeInput.queryParameters.customerId; 720: Screen Pop / request_body[4].value.customerId |
| 2: WxCC Task v2 | `$(n2.webex.origin)` | 896: Messenger / destination |
| 1487: WXM | `$(n1487.surveyURL)` | 896: Messenger / fb_text; 902: Append Conversation / extraParamsData.text; 902: Append Conversation / extraParamsData.textOrResponse; 902: Append Conversation / nodeInput.text; 902: Append Conversation / nodeInput.textOrResponse; 902: Append Conversation / request_body[5].value |
| External/system/custom value; producer not established here | `$(utctime)` | 902: Append Conversation / extraParamsData.timestamp; 902: Append Conversation / nodeInput.timestamp; 902: Append Conversation / request_body[6].value |
| 2: WxCC Task v2 | `$(n2.webex.mediaChannel)` | 1406: Branch / expression; 1406: Branch / outcomes[0].conditions[1].varaible |

### Boundaries and adaptation

There is no survey-response wait or retry loop. WXM questionnaire/prefill IDs and the generic screen-pop URL are sample configuration. The override check is a regex over serialized input, not a typed Boolean field test. Evaluate errors and several Close Task events lack captured routes; detached terminal bindings reference uncaptured 683/305. Screen-pop success/error terminals exist, but no operation was executed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 57: Evaluate / `oninvalidchoice` (declared target count 1); 57: Evaluate / `onerror` (declared target count 1); 653: Close Task / `oninvaliddata` (declared target count None); 653: Close Task / `onerror` (declared target count None); 653: Close Task / `oninvalidchoice` (declared target count None); 653: Close Task / `ontimeout` (declared target count None); 671: Close Task / `oninvaliddata` (declared target count None); 671: Close Task / `onerror` (declared target count None); 671: Close Task / `oninvalidchoice` (declared target count None); 671: Close Task / `ontimeout` (declared target count None).
End records reference absent producer nodes: 305, 683. These stale/unresolved parent references do not establish operative nodes or valid routes.
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-facebookinboundflow"></a>

## FacebookInboundFlow.workflow

Observed 2026-09-09T00:07:46.595Z. [Captured model](../evidence/sample-flows/observed/wxcc-facebookinboundflow.json); [complete graph summary](sample-flows/summaries/wxcc-facebookinboundflow.json). Runtime tested: **no**.

Messenger Incoming Message 2 enters Evaluate 9, then Resolve Conversation 1897. Evaluate assembles incoming message, attachment and scan details. Resolve `created` or `reopened` sends acknowledgment 1899, whose success, policy-failure and error edges all continue to Queue Task 1701. `Queued` sends notification 1912. Resolve `appended` ends successfully; `accepted` has a Success terminal with asynchronous checking. Resolve timeout enters Branch 1939: a created/reopened operation closes Task 1703, appended ends successfully, and unmatched/error ends with Error. Queue failures also close Task 1703; its configured outcomes converge on error notification 1651. Evaluate/other Resolve failures use notification 1662.

Useful handoffs: Start on-leave assignments copy `$(n2.messenger.message)`, attachments, sender `psId` and scan metadata into custom variables. Evaluate builds `detailsJson`, consumed by Resolve's Details JSON; Resolve declares `transId`, `taskId` and `conversationOperation` outputs. Queue and Close use unqualified `$(taskId)` and `$(conversationId)`. Every Messenger send targets `$(n2.messenger.psId)`. This is an incoming-message routing transaction; no Receive node, conversation loop or AI Agent node appears.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Incoming Message | onBegin (`onbegin`) → 9: Evaluate |
| 9: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1662: Messenger; success (`1`) → 1897: Resolve Conversation |
| 1651: Messenger | No outgoing route captured |
| 1662: Messenger | No outgoing route captured |
| 1701: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1703: Close Task; Queued → 1912: Queued |
| 1703: Close Task | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Success, Error, onauthorizationfail → 1651: Messenger |
| 1897: Resolve Conversation | created, reopened → 1899: Messenger; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1662: Messenger; onTimeout (`ontimeout`) → 1939: Branch; appended → End 1975 → Success; accepted → End 1976 → Success |
| 1899: Messenger | onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`), onError (`onerror`) → 1701: Queue Task; onError (`onerror`) → End 1720 → Error; onPolicyFail (`onpolicyfail`) → End 1721 → Error; onSuccess (`onsuccess`) → End 1722 → Success |
| 1912: Queued | onError (`onerror`) → End 1922 → Error; onPolicyFail (`onpolicyfail`) → End 1923 → Error; onSuccess (`onsuccess`) → End 1924 → Success |
| 1939: Branch | Create/Reopen Path → 1703: Close Task; onError (`onerror`) → End 1952 → Error; Append Path → End 1953 → Success; None of the above → End 1954 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Incoming Message | `$(n2.messenger.attachments)` | 2: Incoming Message / transition_actions[0].value; 2: Incoming Message / transition_actions[15].value |
| 2: Incoming Message | `$(n2.messenger.message)` | 2: Incoming Message / transition_actions[14].value; 2: Incoming Message / transition_actions[1].value |
| 2: Incoming Message | `$(n2.messenger.attachmentUrl)` | 2: Incoming Message / transition_actions[2].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.nonPCIComplianceReason)` | 2: Incoming Message / transition_actions[17].value; 2: Incoming Message / transition_actions[3].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.isPCIValidationDone)` | 2: Incoming Message / transition_actions[16].value; 2: Incoming Message / transition_actions[4].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.isPCICompliance)` | 2: Incoming Message / transition_actions[5].value |
| 2: Incoming Message | `$(n2.messenger.name)` | 2: Incoming Message / transition_actions[6].value |
| 2: Incoming Message | `$(n2.messenger.appId)` | 2: Incoming Message / transition_actions[7].value |
| 2: Incoming Message | `$(n2.messenger.psId)` | 1651: Messenger / destination; 1662: Messenger / destination; 1899: Messenger / destination; 1912: Queued / destination; 2: Incoming Message / transition_actions[8].value |
| 2: Incoming Message | `$(n2.messenger.ts)` | 2: Incoming Message / transition_actions[9].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.isAttachmentEnabled)` | 2: Incoming Message / transition_actions[10].value |
| 2: Incoming Message | `$(n2.messenger.pciInfo.droppedAttachmentCount)` | 2: Incoming Message / transition_actions[11].value |
| 2: Incoming Message | `$(n2.service.serviceKey)` | 2: Incoming Message / transition_actions[12].value |
| 2: Incoming Message | `$(n2.messenger.transId)` | 2: Incoming Message / transition_actions[13].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.isSecurityValidationDone)` | 2: Incoming Message / transition_actions[18].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.securityFailedReason)` | 2: Incoming Message / transition_actions[19].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.droppedAttachmentCount)` | 2: Incoming Message / transition_actions[20].value |
| 2: Incoming Message | `$(n2.messenger.securityscaninfo.isSecurityCompliance)` | 2: Incoming Message / transition_actions[21].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.isMalwareValidationDone)` | 2: Incoming Message / transition_actions[22].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.isMalwareCompliance)` | 2: Incoming Message / transition_actions[23].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.malwareFailedReason)` | 2: Incoming Message / transition_actions[24].value |
| 2: Incoming Message | `$(n2.messenger.malwareinfo.droppedAttachmentCount)` | 2: Incoming Message / transition_actions[25].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1897: Resolve Conversation / extraParamsData.details; 1897: Resolve Conversation / nodeInput.details; 1897: Resolve Conversation / request_body[6].value; 9: Evaluate / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1651: Messenger / fb_text; 1662: Messenger / fb_text |
| External/system/custom value; producer not established here | `$(taskId)` | 1701: Queue Task / extraParamsData.id; 1701: Queue Task / nodeInput.id; 1701: Queue Task / path_parameters[1].value; 1701: Queue Task / request_body[0].value; 1703: Close Task / nodeInput.ID; 1703: Close Task / nodeInput.Task Id; 1703: Close Task / path_parameters[1].value; 1703: Close Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1701: Queue Task / extraParamsData.conversationid; 1701: Queue Task / nodeInput.conversationid; 1701: Queue Task / request_body[3].value; 1703: Close Task / nodeInput.Conversation ID; 1703: Close Task / request_body[2].value |
| custom variable; writers 2: Incoming Message | `$(transId)` | 1897: Resolve Conversation / extraParamsData.trackingId; 1897: Resolve Conversation / extraParamsData.transId; 1897: Resolve Conversation / nodeInput.trackingId; 1897: Resolve Conversation / nodeInput.transId; 1897: Resolve Conversation / request_body[0].value; 1897: Resolve Conversation / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 1939: Branch / expression; 1939: Branch / outcomes[0].conditions[0].varaible; 1939: Branch / outcomes[0].conditions[1].varaible; 1939: Branch / outcomes[1].conditions[0].varaible |

### Boundaries and adaptation

The capture retains both terminal bindings and outgoing edges for acknowledgment 1899, plus terminal metadata with absent producer nodes; execution precedence is unverified. Start assigns timestamp from `n2.messenger.ts` although its output list names `messenger.timestamp`; Evaluate uses `appId` while Start assigns `appid`. Preserve those differences when adapting. Selected resources and stored fixtures are not defaults. Internal canvas evidence is not an import schema; runtime testing is false.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1651: Messenger / `onerror` (declared target count 1); 1662: Messenger / `onerror` (declared target count 1).
End records reference absent producer nodes: 1825. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-facebooktaskbotinboundflow"></a>

## FacebookTaskBotInboundFlow.workflow

Observed 2026-09-09T00:03:05.707Z. [Captured model](../evidence/sample-flows/observed/wxcc-facebooktaskbotinboundflow.json); [complete graph summary](sample-flows/summaries/wxcc-facebooktaskbotinboundflow.json). Runtime tested: **no**.

Messenger Start 2 → Evaluate 9 → Resolve Conversation 1740 sends created/reopened to HTTP lookup 1574. Branch 1575 sends empty body or HTTP 400/404/429 directly to Task bot 1777; other responses pass through account parser 1576. Bot onSuccess enters Branch 1585: TemplateKey linkAcc parses Entities at 1586 and Datastore at 1590, posts account data at 1584, then sends reply 1404. Other template keys send directly. Outbound Append 1273 checks Goodbye Intent at Branch 1794; otherwise Receive 756 waits 120 seconds. fbm.mo → normalization 1413 → inbound Append 1332 → bot is the turn loop. onAgentHandover sends/appends the reply then Queue Task 1388.

Useful handoffs: Bot consumer.facebook_id and Send destination use `$(n2.messenger.psId)`; msg uses `$(questionForBot)` and correlation uses `$(transid)`. Receive filters that original sender. Account lookup uses a literal ID, not the inbound psId. Parser 1576 reads the first record Account number/Balance into session accNum/balance. The linkAcc path extracts `$.accNum.value` from `$(n1777.Entities)` and `$.bal` from `$(n1777.Datastore)`; POST writes these with the inbound psId/name. Receive refreshes message/attachments; normalization prepares `messageFromCustomer` and `parseDataAttachment` for Append.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Messenger Event | onBegin (`onbegin`) → 9: Evaluate |
| 9: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1616: Messenger; success (`1`) → 1740: Resolve Conversation |
| 756: Receive | fbm.mo → 1413: Receive timestamp; onTimeout (`ontimeout`) → 1426: Messenger; onError (`onerror`) → 1645: Messenger |
| 1273: Append Conversation | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1645: Messenger; onAppendMessageSuccess → 1794: Branch |
| 1332: Append Conversation | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1645: Messenger; onAppendMessageSuccess → 1777: Task bot |
| 1357: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, Success → 1653: Messenger |
| 1388: Queue Task | onInvalidData (`oninvaliddata`), onTimeout (`ontimeout`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1357: Close Task; Queued → 1749: Messenger |
| 1404: Messenger | onSuccess (`onsuccess`) → 1273: Append Conversation |
| 1413: Receive timestamp | timern (`1`) → 1332: Append Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1649: Messenger |
| 1426: Messenger | onSuccess (`onsuccess`) → 1796: Close Task |
| 1434: Messenger | onSuccess (`onsuccess`) → 1552: Append Conversation; onError (`onerror`) → End 1780 → Error; onPolicyFail (`onpolicyfail`) → End 1781 → Error; onError (`onerror`) → End 1818 → Error; onPolicyFail (`onpolicyfail`) → End 1819 → Error |
| 1552: Append Conversation | onAppendMessageSuccess → 1388: Queue Task; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1649: Messenger |
| 1574: HTTP Request | onSuccess (`oncomplete`) → 1575: Branch; onError (`onerror`) → 1624: Messenger; onTimeout (`ontimeout`) → 1762: Close Task |
| 1575: Branch | None of the above → 1576: Data Parser; onError (`onerror`) → 1624: Messenger; Not found → 1777: Task bot |
| 1576: Data Parser | onError (`onerror`) → 1624: Messenger; onSuccess (`oncomplete`) → 1777: Task bot |
| 1584: HTTP Request | onSuccess (`oncomplete`) → 1404: Messenger; onTimeout (`ontimeout`), onError (`onerror`) → 1796: Close Task |
| 1585: Branch | None of the above → 1404: Messenger; Link account → 1586: Data Parser; onError (`onerror`) → 1624: Messenger |
| 1586: Data Parser | onSuccess (`oncomplete`) → 1590: Data Parser; onError (`onerror`) → 1645: Messenger |
| 1590: Data Parser | onSuccess (`oncomplete`) → 1584: HTTP Request; onError (`onerror`) → 1645: Messenger |
| 1616: Messenger | onSuccess (`onsuccess`) → End 1786 → Success |
| 1624: Messenger | onError (`onerror`) → End 1784 → Error; onPolicyFail (`onpolicyfail`) → End 1785 → Error |
| 1645: Messenger | No outgoing route captured |
| 1649: Messenger | No outgoing route captured |
| 1653: Messenger | No outgoing route captured |
| 1740: Resolve Conversation | created, reopened → 1574: HTTP Request; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1616: Messenger; onTimeout (`ontimeout`) → 1761: Branch; appended → End 1822 → Success; accepted → End 1823 → Success |
| 1749: Messenger | onError (`onerror`) → End 1752 → Error; onPolicyFail (`onpolicyfail`) → End 1753 → Error; onSuccess (`onsuccess`) → End 1756 → Success; onError (`onerror`) → End 1787 → Error; onPolicyFail (`onpolicyfail`) → End 1788 → Error |
| 1761: Branch | Create/Reopen Path → 1762: Close Task; onError (`onerror`) → End 1766 → Error; Append Path → End 1768 → Success; None of the above → End 1771 → Error |
| 1762: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error → 1624: Messenger |
| 1777: Task bot | onSuccess → 1585: Branch; onAgentHandover → 1434: Messenger; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onFailure → 1762: Close Task |
| 1794: Branch | None of the above → 756: Receive; onError (`onerror`), Conversation Closed → 1426: Messenger |
| 1796: Close Task | onTimeout (`ontimeout`) → End 1797 → Error; Success → End 1799 → Success; onInvalidData (`oninvaliddata`) → End 1802 → Error; onError (`onerror`) → End 1806 → Error; onInvalidChoice (`oninvalidchoice`) → End 1811 → Error; Error → End 1817 → Error |

**Loops in the captured graph:** 756: Receive → 1273: Append Conversation → 1332: Append Conversation → 1404: Messenger → 1413: Receive timestamp → 1584: HTTP Request → 1585: Branch → 1586: Data Parser → 1590: Data Parser → 1777: Task bot → 1794: Branch. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Messenger Event | `$(n2.messenger.attachments)` | 2: Configure Messenger Event / transition_actions[0].value; 2: Configure Messenger Event / transition_actions[15].value |
| 2: Configure Messenger Event | `$(n2.messenger.message)` | 2: Configure Messenger Event / transition_actions[14].value; 2: Configure Messenger Event / transition_actions[1].value |
| 2: Configure Messenger Event | `$(n2.messenger.attachmentUrl)` | 2: Configure Messenger Event / transition_actions[2].value |
| 2: Configure Messenger Event | `$(n2.messenger.pciInfo.nonPCIComplianceReason)` | 2: Configure Messenger Event / transition_actions[17].value; 2: Configure Messenger Event / transition_actions[3].value |
| 2: Configure Messenger Event | `$(n2.messenger.pciInfo.isPCIValidationDone)` | 2: Configure Messenger Event / transition_actions[16].value; 2: Configure Messenger Event / transition_actions[4].value |
| 2: Configure Messenger Event | `$(n2.messenger.pciInfo.isPCICompliance)` | 2: Configure Messenger Event / transition_actions[5].value |
| 2: Configure Messenger Event | `$(n2.messenger.name)` | 1584: HTTP Request / body.Name; 2: Configure Messenger Event / transition_actions[6].value |
| 2: Configure Messenger Event | `$(n2.messenger.appId)` | 2: Configure Messenger Event / transition_actions[7].value |
| 2: Configure Messenger Event | `$(n2.messenger.psId)` | 1404: Messenger / destination; 1426: Messenger / destination; 1434: Messenger / destination; 1584: HTTP Request / body.ID; 1616: Messenger / destination; 1624: Messenger / destination; 1645: Messenger / destination; 1649: Messenger / destination; 1653: Messenger / destination; 1749: Messenger / destination; 1777: Task bot / extraParamsData.consumer.facebook_id; 1777: Task bot / extraParamsData.uid; 1777: Task bot / nodeInput.consumer.facebook_id; 1777: Task bot / nodeInput.uid; 1777: Task bot / request_body[0].value.facebook_id; 2: Configure Messenger Event / transition_actions[8].value |
| 2: Configure Messenger Event | `$(n2.messenger.ts)` | 2: Configure Messenger Event / transition_actions[9].value |
| 2: Configure Messenger Event | `$(n2.messenger.pciInfo.isAttachmentEnabled)` | 2: Configure Messenger Event / transition_actions[10].value |
| 2: Configure Messenger Event | `$(n2.messenger.pciInfo.droppedAttachmentCount)` | 2: Configure Messenger Event / transition_actions[11].value |
| 2: Configure Messenger Event | `$(n2.service.serviceKey)` | 2: Configure Messenger Event / transition_actions[12].value |
| 2: Configure Messenger Event | `$(n2.messenger.transId)` | 2: Configure Messenger Event / transition_actions[13].value |
| 2: Configure Messenger Event | `$(n2.messenger.securityscaninfo.isSecurityValidationDone)` | 2: Configure Messenger Event / transition_actions[18].value |
| 2: Configure Messenger Event | `$(n2.messenger.securityscaninfo.securityFailedReason)` | 2: Configure Messenger Event / transition_actions[19].value |
| 2: Configure Messenger Event | `$(n2.messenger.securityscaninfo.droppedAttachmentCount)` | 2: Configure Messenger Event / transition_actions[20].value |
| 2: Configure Messenger Event | `$(n2.messenger.securityscaninfo.isSecurityCompliance)` | 2: Configure Messenger Event / transition_actions[21].value |
| 2: Configure Messenger Event | `$(n2.messenger.malwareinfo.isMalwareValidationDone)` | 2: Configure Messenger Event / transition_actions[22].value |
| 2: Configure Messenger Event | `$(n2.messenger.malwareinfo.isMalwareCompliance)` | 2: Configure Messenger Event / transition_actions[23].value |
| 2: Configure Messenger Event | `$(n2.messenger.malwareinfo.malwareFailedReason)` | 2: Configure Messenger Event / transition_actions[24].value |
| 2: Configure Messenger Event | `$(n2.messenger.malwareinfo.droppedAttachmentCount)` | 2: Configure Messenger Event / transition_actions[25].value |
| External/system/custom value; producer not established here | `$(messageFromCustomer)` | 1332: Append Conversation / extraParamsData.text; 1332: Append Conversation / extraParamsData.textOrResponse; 1332: Append Conversation / request_body[5].value; 1413: Receive timestamp / transition_actions[0].value; 1413: Receive timestamp / transition_actions[1].value; 1413: Receive timestamp / transition_actions[3].value; 9: Evaluate / transition_actions[0].value; 9: Evaluate / transition_actions[4].value |
| External/system/custom value; producer not established here | `$(tid)` | 9: Evaluate / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(flid)` | 9: Evaluate / transition_actions[2].value |
| 9: Evaluate | `$(n9.evaluate.output)` | 9: Evaluate / transition_actions[3].value |
| custom variable; writers 1413: Receive timestamp, 756: Receive, 9: Evaluate | `$(questionForBot)` | 1413: Receive timestamp / transition_actions[2].value; 1413: Receive timestamp / transition_actions[4].value; 1777: Task bot / extraParamsData.msg; 1777: Task bot / nodeInput.msg; 1777: Task bot / request_body[3].value; 1777: Task bot / transition_actions[0].value; 9: Evaluate / transition_actions[5].value |
| 756: Receive | `$(n756.receive.message)` | 756: Receive / transition_actions[0].value; 756: Receive / transition_actions[3].value; 756: Receive / transition_actions[9].value |
| 756: Receive | `$(n756.inappmessaging.timestamp)` | 756: Receive / transition_actions[1].value |
| 756: Receive | `$(n756.receive.attachment)` | 756: Receive / transition_actions[15].value; 756: Receive / transition_actions[2].value |
| 756: Receive | `$(n756.messenger.securityscaninfo.securityFailedReason)` | 756: Receive / transition_actions[4].value |
| 756: Receive | `$(n756.messenger.securityscaninfo.isSecurityValidationDone)` | 756: Receive / transition_actions[5].value |
| 756: Receive | `$(n756.messenger.securityscaninfo.isSecurityCompliance)` | 756: Receive / transition_actions[6].value |
| 756: Receive | `$(n756.messenger.attachmentUrl)` | 756: Receive / transition_actions[12].value; 756: Receive / transition_actions[7].value |
| 756: Receive | `$(n756.messenger.attachments)` | 756: Receive / transition_actions[10].value |
| 756: Receive | `$(n756.messenger.pciInfo.nonPCIComplianceReason)` | 756: Receive / transition_actions[11].value |
| 756: Receive | `$(n756.messenger.pciInfo.isPCIValidationDone)` | 756: Receive / transition_actions[13].value |
| 756: Receive | `$(n756.messenger.pciInfo.isPCICompliance)` | 756: Receive / transition_actions[14].value |
| 1777: Task bot | `$(n1777.TextResponse)` | 1273: Append Conversation / extraParamsData.text; 1273: Append Conversation / extraParamsData.textOrResponse; 1273: Append Conversation / request_body[5].value; 1404: Messenger / fb_text; 1434: Messenger / fb_text; 1552: Append Conversation / extraParamsData.text; 1552: Append Conversation / extraParamsData.textOrResponse; 1552: Append Conversation / request_body[5].value |
| 1404: Messenger | `$(n1404.send.sentDateTime)` | 1273: Append Conversation / extraParamsData.timestamp; 1273: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1273: Append Conversation / extraParamsData.conversationid; 1273: Append Conversation / path_parameters[1].value; 1273: Append Conversation / transition_actions[0].value; 1332: Append Conversation / extraParamsData.conversationid; 1332: Append Conversation / path_parameters[1].value; 1357: Close Task / nodeInput.Conversation ID; 1357: Close Task / request_body[2].value; 1388: Queue Task / extraParamsData.conversationid; 1388: Queue Task / request_body[3].value; 1552: Append Conversation / extraParamsData.conversationid; 1552: Append Conversation / path_parameters[1].value; 1740: Resolve Conversation / transition_actions[0].value; 1762: Close Task / nodeInput.Conversation ID; 1762: Close Task / request_body[2].value; 1762: Close Task / transition_actions[1].value; 1796: Close Task / request… [full value in graph summary] |
| External/system/custom value; producer not established here | `$(timern)` | 1332: Append Conversation / extraParamsData.timestamp; 1332: Append Conversation / request_body[6].value; 1332: Append Conversation / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(parseDataAttachment)` | 1332: Append Conversation / extraParamsData.attachments; 1332: Append Conversation / request_body[7].value; 1332: Append Conversation / transition_actions[2].value |
| 756: Receive | `$(n756.messenger.timestamp)` | 1332: Append Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1357: Close Task / nodeInput.ID; 1357: Close Task / nodeInput.Task Id; 1357: Close Task / path_parameters[1].value; 1357: Close Task / request_body[0].value; 1388: Queue Task / extraParamsData.id; 1388: Queue Task / path_parameters[1].value; 1388: Queue Task / request_body[0].value; 1762: Close Task / nodeInput.ID; 1762: Close Task / nodeInput.Task Id; 1762: Close Task / path_parameters[1].value; 1762: Close Task / request_body[0].value; 1762: Close Task / transition_actions[0].value; 1796: Close Task / path_parameters[1].value; 1796: Close Task / request_body[0].value |
| custom variable; writers 1794: Branch, 756: Receive | `$(BotCloseMessage)` | 1426: Messenger / fb_text |
| 1434: Messenger | `$(n1434.send.sentDateTime)` | 1552: Append Conversation / extraParamsData.timestamp; 1552: Append Conversation / request_body[6].value |
| 1574: HTTP Request | `$(n1574.http.responseBody)` | 1575: Branch / expression; 1575: Branch / outcomes[0].conditions[0].varaible; 1576: Data Parser / input |
| 1574: HTTP Request | `$(n1574.http.statusCode)` | 1575: Branch / expression; 1575: Branch / outcomes[0].conditions[1].varaible; 1575: Branch / outcomes[0].conditions[2].varaible; 1575: Branch / outcomes[0].conditions[3].varaible |
| 1576: Data Parser | `$(n1576.AccNum)` | 1576: Data Parser / transition_actions[0].value |
| 1576: Data Parser | `$(n1576.Balance)` | 1576: Data Parser / transition_actions[1].value |
| 1586: Data Parser | `$(n1586.accNum)` | 1584: HTTP Request / body.Account number; 1584: HTTP Request / transition_actions[0].value |
| 1590: Data Parser | `$(n1590.balance)` | 1584: HTTP Request / body.Balance; 1584: HTTP Request / transition_actions[1].value |
| 1777: Task bot | `$(n1777.TemplateKey)` | 1585: Branch / expression; 1585: Branch / outcomes[0].conditions[0].varaible |
| 1777: Task bot | `$(n1777.Entities)` | 1586: Data Parser / input |
| 1777: Task bot | `$(n1777.Datastore)` | 1590: Data Parser / input |
| 1405 | `$(n1405.taskbot.data_store)` | 1590: Data Parser / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1616: Messenger / fb_text |
| External/system/custom value; producer not established here | `$(errorMsg2)` | 1624: Messenger / fb_text; 1645: Messenger / fb_text; 1649: Messenger / fb_text; 1653: Messenger / fb_text |
| custom variable; writers 2: Configure Messenger Event | `$(transId)` | 1740: Resolve Conversation / extraParamsData.trackingId; 1740: Resolve Conversation / extraParamsData.transId; 1740: Resolve Conversation / request_body[0].value; 1740: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1740: Resolve Conversation / extraParamsData.details; 1740: Resolve Conversation / request_body[6].value |
| 1740: Resolve Conversation | `$(n1740.conversationOperation)` | 1761: Branch / expression; 1761: Branch / outcomes[0].conditions[0].varaible; 1761: Branch / outcomes[0].conditions[1].varaible; 1761: Branch / outcomes[1].conditions[0].varaible |
| External/system/custom value; producer not established here | `$(transid)` | 1777: Task bot / extraParamsData.transid; 1777: Task bot / nodeInput.transid; 1777: Task bot / request_body[1].value |
| 1777: Task bot | `$(n1777.Intent)` | 1794: Branch / expression; 1794: Branch / outcomes[0].conditions[0].varaible |

### Boundaries and adaptation

This is a legacy Task Bot demonstration with a sample account store, not a current AI Agent or verified banking workflow. Goodbye/Receive timeout sends closure notice 1426 then Close Task 1796; many failures use separate close/error paths. Resolve appended/accepted ends through parent/event bindings. The literal lookup ID and stale log reference to absent n1405 remain explicit. No retry/idempotency guard surrounds the account POST. No runtime actions occurred; headers/hosts are sanitized, resource IDs need adaptation, and this internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1404: Messenger / `onerror` (declared target count 1); 1426: Messenger / `onerror` (declared target count 1); 1576: Data Parser / `oninvaliddata` (declared target count None); 1586: Data Parser / `oninvaliddata` (declared target count None); 1590: Data Parser / `oninvaliddata` (declared target count None); 1616: Messenger / `onerror` (declared target count 1); 1645: Messenger / `onerror` (declared target count 1); 1649: Messenger / `onerror` (declared target count 1); 1653: Messenger / `onerror` (declared target count 1).
End records reference absent producer nodes: 1681, 1730. These stale/unresolved parent references do not establish operative nodes or valid routes.
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
Literal node-qualified references name uncaptured producers: n1405. Their provenance is not guessed.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-live-chat-close-flow"></a>

## Live Chat Close Flow.workflow

Observed 2026-09-09T00:08:02.557Z. [Captured model](../evidence/sample-flows/observed/wxcc-live-chat-close-flow.json); [complete graph summary](sample-flows/summaries/wxcc-live-chat-close-flow.json). Runtime tested: **no**.

The Mobile & Web App `On Thread Closed` event starts node 2 and Search Conversation 108. Its `conversationActive` route appends the closure reason as an announcement at 208, ending Success on append success. The closed, in-queue and on-hold routes instead invoke Close Task 124. No conversation found terminates Success. Search, append and close errors/timeouts have explicit Error terminal bindings; Close Task Success terminates Success. The active route does not continue from Append 208 into Close Task 124 in the captured graph.

Useful handoffs: Search 108 identifies the conversation from `$(n2.inappmessaging.userId)`, `$(n2.inappmessaging.appId)` and `$(n2.inappmessaging.threadId)`; the user ID is also the browser fingerprint. It extracts `aliasId` from `$.value.aliasId` and `conversationId` from `$.value.conversationId`. Close Task 124 uses `$(n108.aliasId)` as Task Id and `$(n108.conversationId)` as Conversation ID with media type `chat`. Append 208 uses the same conversation ID, `$(n2.inappmessaging.reasonForThreadClosure)` as announcement text, and `$(n2.inappmessaging.ts)` as timestamp.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Mobile & Web App Event | onBegin (`onbegin`) → 108: Search Conversation |
| 108: Search Conversation | conversationActive → 208: Append Conversation; conversationClosed, conversationInQueue, conversationOnHold → 124: Close Task; onInvalidData (`oninvaliddata`) → End 313 → Error; onError (`onerror`) → End 314 → Error; onInvalidChoice (`oninvalidchoice`) → End 315 → Error; onTimeout (`ontimeout`) → End 316 → Error; noConversationFound → End 317 → Success |
| 124: Close Task | onInvalidData (`oninvaliddata`) → End 318 → Error; onError (`onerror`) → End 319 → Error; onInvalidChoice (`oninvalidchoice`) → End 320 → Error; Error → End 321 → Error; onTimeout (`ontimeout`) → End 322 → Error; Success → End 323 → Success |
| 208: Append Conversation | onInvalidData (`oninvaliddata`) → End 331 → Error; onError (`onerror`) → End 332 → Error; onInvalidChoice (`oninvalidchoice`) → End 333 → Error; Failure → End 334 → Error; onAppendMessageFailure → End 335 → Error; onTimeout (`ontimeout`) → End 336 → Error; onAppendMessageSuccess → End 337 → Success; onauthorizationfail → End 345 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.userId)` | 108: Search Conversation / extraParamsData.browserfingerprint; 108: Search Conversation / extraParamsData.customeraddress; 108: Search Conversation / nodeInput.browserfingerprint; 108: Search Conversation / nodeInput.customeraddress; 108: Search Conversation / request_body[1].value; 108: Search Conversation / request_body[5].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.appId)` | 108: Search Conversation / extraParamsData.bizaddress; 108: Search Conversation / nodeInput.bizaddress; 108: Search Conversation / request_body[2].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadId)` | 108: Search Conversation / extraParamsData.threadid; 108: Search Conversation / nodeInput.threadid; 108: Search Conversation / request_body[4].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.ts)` | 108: Search Conversation / transition_actions[0].value; 208: Append Conversation / extraParamsData.timestamp; 208: Append Conversation / request_body[6].value |
| 108: Search Conversation | `$(n108.aliasId)` | 108: Search Conversation / transition_actions[1].value; 124: Close Task / nodeInput.ID; 124: Close Task / nodeInput.Task Id; 124: Close Task / path_parameters[1].value; 124: Close Task / request_body[0].value |
| 108: Search Conversation | `$(n108.conversationId)` | 124: Close Task / nodeInput.Conversation ID; 124: Close Task / request_body[2].value; 208: Append Conversation / extraParamsData.conversationid; 208: Append Conversation / path_parameters[1].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.reasonForThreadClosure)` | 208: Append Conversation / extraParamsData.text; 208: Append Conversation / extraParamsData.textOrResponse; 208: Append Conversation / request_body[5].value |

### Boundaries and adaptation

This is a channel thread-close handler, distinct from a WxCC Task Closed survey flow. It neither sends a customer message nor waits for another turn, and contains no control loop. Preserve the distinct active-versus-queued closure behavior when adapting; tenant bindings, closure semantics and successful execution were not tested.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechat-inbound-flow-with-proactive-chat-changes"></a>

## Livechat Inbound flow with proactive chat changes.workflow

Observed 2026-09-09T00:08:09.451Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechat-inbound-flow-with-proactive-chat-changes.json); [complete graph summary](sample-flows/summaries/wxcc-livechat-inbound-flow-with-proactive-chat-changes.json). Runtime tested: **no**.

APP Start 2 searches Conversation 2433. No conversation or a closed conversation sends pre-chat form 2436, then Receive 2438 waits 300 seconds for `app.onformresponse`; active, queued or held conversations go directly to Evaluate 2465. Evaluate feeds Resolve Conversation 2588. Created/reopened conversations append the form response through 2424, then Branch 2620 selects Queue 2621 for proactive chat or Queue 2259 otherwise; branch error also selects 2259. Both `Queued` events send acknowledgment 1727. Resolve appended/accepted events end successfully, accepted with asynchronous checking. Resolve timeout reaches Branch 2517: create/reopen closes Task 2261, append succeeds, other/error fails. Append/queue failures also close Task 2261 and send error 2227; earlier failures use 2234.

Useful handoffs: Start copies `$(n2.inappmessaging.message.extras)` into `messageExtras`. Evaluate parses it, compares `proactive_id !== 0`, sets `isProactiveChat`, and extracts `proactive_queue_id` as `proactiveQueueId`; Queue 2621 consumes that dynamic queue ID. Receive assigns customerName/customerEmail from formFields.Name/Email; Append consumes `$(n2438.inappmessaging.formResponse)`. Evaluate includes proactiveRuleId in `detailsJson` for Resolve. Queue/Close use taskId/conversationId; notifications retain the original userId and threadId.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure APP Event | onBegin (`onbegin`) → 2433: Search Conversation |
| 1727: Queued | onSuccess (`onsuccess`) → End 2632 → Success |
| 2227: Error Notif | No outgoing route captured |
| 2234: Error Notif | No outgoing route captured |
| 2259: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 2261: Close Task; Queued → 1727: Queued |
| 2261: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 2227: Error Notif |
| 2424: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 2261: Close Task; onAppendMessageSuccess → 2620: Branch |
| 2433: Search Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), onauthorizationfail → 2234: Error Notif; noConversationFound, conversationClosed → 2436: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 2465: Evaluate |
| 2436: Pre-chat form | onSuccess (`onsuccess`) → 2438: Receive; onPolicyFail (`onpolicyfail`), onError (`onerror`) → 2234: Error Notif |
| 2438: Receive | onError (`onerror`), onTimeout (`ontimeout`) → 2234: Error Notif; app.onformresponse → 2465: Evaluate |
| 2465: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 2234: Error Notif; success (`1`) → 2588: Resolve Conversation |
| 2517: Branch | Create / Reopen Path → 2261: Close Task; onError (`onerror`) → End 2633 → Error; None of the above → End 2634 → Error; Append Path → End 2635 → Success |
| 2588: Resolve Conversation | created, reopened → 2424: Append Conversation; onTimeout (`ontimeout`) → 2517: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 2234: Error Notif; accepted → End 2625 → Success; appended → End 2626 → Success |
| 2620: Branch | None of the above, onError (`onerror`) → 2259: Queue Task; Proactive Branch → 2621: Queue Task |
| 2621: Queue Task | Queued → 1727: Queued; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Error, taskFailed, onTimeout (`ontimeout`) → 2261: Close Task |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure APP Event | `$(n2.inappmessaging.message)` | 2: Configure APP Event / transition_actions[0].value; 2: Configure APP Event / transition_actions[19].value; flow-custom-defaults / customVariables[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachment)` | 2: Configure APP Event / transition_actions[11].value; 2: Configure APP Event / transition_actions[1].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure APP Event / transition_actions[2].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure APP Event / transition_actions[21].value; 2: Configure APP Event / transition_actions[3].value |
| 2: Configure APP Event | `$(n2.inappmessaging.extras)` | 2: Configure APP Event / transition_actions[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.appId)` | 2: Configure APP Event / transition_actions[5].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadId)` | 1727: Queued / thread_id; 2227: Error Notif / thread_id; 2234: Error Notif / thread_id; 2433: Search Conversation / extraParamsData.threadid; 2433: Search Conversation / nodeInput.threadid; 2433: Search Conversation / request_body[4].value; 2436: Pre-chat form / thread_id; 2: Configure APP Event / transition_actions[6].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure APP Event / transition_actions[7].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure APP Event / transition_actions[8].value |
| 2: Configure APP Event | `$(n2.inappmessaging.userId)` | 1727: Queued / destination; 2227: Error Notif / destination; 2234: Error Notif / destination; 2433: Search Conversation / extraParamsData.browserfingerprint; 2433: Search Conversation / extraParamsData.customeraddress; 2433: Search Conversation / nodeInput.browserfingerprint; 2433: Search Conversation / nodeInput.customeraddress; 2433: Search Conversation / request_body[1].value; 2433: Search Conversation / request_body[5].value; 2436: Pre-chat form / destination; 2: Configure APP Event / transition_actions[9].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure APP Event / transition_actions[10].value |
| 2: Configure APP Event | `$(n2.inappmessaging.version)` | 2: Configure APP Event / transition_actions[12].value |
| 2: Configure APP Event | `$(n2.inappmessaging.timestamp)` | 2: Configure APP Event / transition_actions[13].value |
| 2: Configure APP Event | `$(n2.inappmessaging.tid)` | 2: Configure APP Event / transition_actions[14].value; 2: Configure APP Event / transition_actions[22].value |
| 2: Configure APP Event | `$(n2.service.serviceKey)` | 2: Configure APP Event / transition_actions[15].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure APP Event / transition_actions[16].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[17].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure APP Event / transition_actions[18].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReasonObject)` | 2: Configure APP Event / transition_actions[20].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure APP Event / transition_actions[23].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure APP Event / transition_actions[24].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[25].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure APP Event / transition_actions[26].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure APP Event / transition_actions[27].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure APP Event / transition_actions[28].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure APP Event / transition_actions[29].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[30].value |
| 2: Configure APP Event | `$(n2.inappmessaging.message.extras)` | 2: Configure APP Event / transition_actions[31].value; flow-custom-defaults / customVariables[48].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 2227: Error Notif / message; 2234: Error Notif / message |
| External/system/custom value; producer not established here | `$(taskId)` | 2259: Queue Task / extraParamsData.id; 2259: Queue Task / nodeInput.id; 2259: Queue Task / path_parameters[1].value; 2259: Queue Task / request_body[0].value; 2259: Queue Task / transition_actions[0].value; 2261: Close Task / nodeInput.ID; 2261: Close Task / nodeInput.Task Id; 2261: Close Task / path_parameters[1].value; 2261: Close Task / request_body[0].value; 2261: Close Task / transition_actions[0].value; 2621: Queue Task / extraParamsData.id; 2621: Queue Task / nodeInput.id; 2621: Queue Task / path_parameters[1].value; 2621: Queue Task / request_body[0].value; 2621: Queue Task / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 2259: Queue Task / extraParamsData.conversationid; 2259: Queue Task / nodeInput.conversationid; 2259: Queue Task / request_body[3].value; 2259: Queue Task / transition_actions[1].value; 2261: Close Task / nodeInput.Conversation ID; 2261: Close Task / request_body[2].value; 2424: Append Conversation / extraParamsData.conversationid; 2424: Append Conversation / path_parameters[1].value; 2424: Append Conversation / transition_actions[0].value; 2588: Resolve Conversation / transition_actions[0].value; 2621: Queue Task / extraParamsData.conversationid; 2621: Queue Task / nodeInput.conversationid; 2621: Queue Task / request_body[3].value; 2621: Queue Task / transition_actions[1].value |
| 2438: Receive | `$(n2438.inappmessaging.formResponse)` | 2424: Append Conversation / extraParamsData.livechatformresponse; 2424: Append Conversation / extraParamsData.textOrResponse; 2424: Append Conversation / request_body[4].value |
| 2438: Receive | `$(n2438.inappmessaging.timestamp)` | 2424: Append Conversation / extraParamsData.timestamp; 2424: Append Conversation / request_body[6].value |
| 2433: Search Conversation | `$(n2433.aliasId)` | 2424: Append Conversation / extraParamsData.messageAliasId |
| 2438: Receive | `$(n2438.inappmessaging.formFields.Name)` | 2438: Receive / transition_actions[0].value |
| 2438: Receive | `$(n2438.inappmessaging.formFields.Email)` | 2438: Receive / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 2517: Branch / expression; 2517: Branch / outcomes[0].conditions[0].varaible; 2517: Branch / outcomes[0].conditions[1].varaible; 2517: Branch / outcomes[1].conditions[0].varaible |
| custom variable; writers 2: Configure APP Event | `$(transId)` | 2588: Resolve Conversation / extraParamsData.trackingId; 2588: Resolve Conversation / extraParamsData.transId; 2588: Resolve Conversation / nodeInput.trackingId; 2588: Resolve Conversation / nodeInput.transId; 2588: Resolve Conversation / request_body[0].value; 2588: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 2588: Resolve Conversation / extraParamsData.details; 2588: Resolve Conversation / nodeInput.details; 2588: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(isProactiveChat)` | 2620: Branch / expression; 2620: Branch / outcomes[0].conditions[0].varaible |
| External/system/custom value; producer not established here | `$(proactiveQueueId)` | 2621: Queue Task / extraParamsData.queueid; 2621: Queue Task / nodeInput.queueid; 2621: Queue Task / request_body[2].value |

### Boundaries and adaptation

The script expects parseable extras with suitable proactive fields; missing or malformed values are not demonstrated. Queue 2259 retains different fixed queue IDs in nodeInput and request_body. Close Task selects media type social although Resolve/Queue select chat. No retry loop or AI Agent node appears, and several notification errors lack captured routes. Resource/template bindings require adaptation. This internal canvas is configuration evidence, not a public schema or successful execution; runtime testing is false.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1727: Queued / `onerror` (declared target count 1); 2227: Error Notif / `onerror` (declared target count 1); 2234: Error Notif / `onerror` (declared target count 1).
End records reference absent producer nodes: 2238, 2291, 2577. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechatclosewithwxmflow"></a>

## LiveChatCloseWithWxmFlow.workflow

Observed 2026-09-09T00:06:41.662Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechatclosewithwxmflow.json); [complete graph summary](sample-flows/summaries/wxcc-livechatclosewithwxmflow.json). Runtime tested: **no**.

Task Closed Start 2 enters Branch 1406, which requires the serialized override-default-close string and media channel `web`; no match ends Success. Evaluate 57 parses task variables and customer data, then WXM 1510 creates a survey link. Success sends Live Chat 993, whose successful send appends the survey message at 1511. Survey-generation failures, send failures and all captured append results proceed to Close Conversation 629. Closure success leads to Close Task 653; close failure first checks code 4547 at Branch 114 and otherwise uses failure-context Close Task 671. Successful task closure checks owner at Branch 246, invoking Screen Pop 720 when present or terminating Success without an owner.

Useful handoffs: Evaluate reads the arrays saved from `$(n2.webex.variables)` and `$(n2.webex.RequestBody)`, extracts variable names `threadID` and `userID` into `thread` and `user`, and persists `mediaResourceId` plus customer fields. Sender 993 uses `$(user)`, `$(thread)` and `$(n1510.surveyURL)`. Append 1511 targets `$(mediaResourceId)` but its text references `$(n1477.surveyURL)`: no node 1477 is captured. This differs from the correctly linked send and must be repaired when adapting.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Webex CC Task | onBegin (`onbegin`) → 1406: Branch |
| 57: Evaluate | Success (`1`) → 1510: WXM |
| 114: Branch | Conversation already closed → 653: Close Task; onError (`onerror`), None of the above → 671: Close Task |
| 246: Branch | Owner present → 720: Screen Pop; onError (`onerror`) → End 413 → Error; None of the above → End 414 → Success |
| 629: Close Conversation | onConversationClosed → 653: Close Task; onCloseConversationFailure, onFailure → 114: Branch; onError (`onerror`), onInvalidData (`oninvaliddata`), onauthorizationfail, onTimeout (`ontimeout`), onInvalidChoice (`oninvalidchoice`) → 671: Close Task |
| 653: Close Task | Success → 246: Branch; onauthorizationfail → End 871 → Error |
| 671: Close Task | onauthorizationfail → End 878 → Error |
| 720: Screen Pop | onInvalidData (`oninvaliddata`) → End 852 → Error; onError (`onerror`) → End 853 → Error; onInvalidChoice (`oninvalidchoice`) → End 854 → Error; onScreenPopFailure → End 855 → Error; serviceUnavailable → End 856 → Error; onTimeout (`ontimeout`) → End 857 → Error; onScreenPopSuccess → End 858 → Success; onauthorizationfail → End 893 → Error |
| 993: Live Chat / In-App Messaging | onPolicyFail (`onpolicyfail`), onError (`onerror`) → 629: Close Conversation; onSuccess (`onsuccess`) → 1511: Append Conversation |
| 1406: Branch | OverrideDefaultCloseChecked → 57: Evaluate; onError (`onerror`) → End 1475 → Error; None of the above → End 1476 → Success |
| 1510: WXM | createTokenForTheQuestionnaireOnSuccess → 993: Live Chat / In-App Messaging; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, failedToAddSurveyToken, UserRoleNotAllowedAccessThisResource, APIRequestLimitExceeded, onTimeout (`ontimeout`) → 629: Close Conversation |
| 1511: Append Conversation | onAppendMessageSuccess, onInvalidData (`oninvaliddata`), onError (`onerror`), onTimeout (`ontimeout`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Failure, onAppendMessageFailure → 629: Close Conversation |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Webex CC Task | `$(n2.webex.variables)` | 2: Webex CC Task / transition_actions[0].value |
| 2: Webex CC Task | `$(n2.webex.RequestBody)` | 1406: Branch / expression; 1406: Branch / outcomes[0].conditions[0].varaible; 2: Webex CC Task / transition_actions[1].value |
| custom variable; writers 57: Evaluate | `$(mediaResourceId)` | 1511: Append Conversation / extraParamsData.conversationid; 1511: Append Conversation / path_parameters[1].value; 57: Evaluate / transition_actions[0].value; 629: Close Conversation / nodeInput.conversation id; 629: Close Conversation / path_parameters[1].value; 653: Close Task / nodeInput.Conversation Id; 653: Close Task / request_body[4].value; 671: Close Task / nodeInput.media resource id; 671: Close Task / request_body[3].value |
| External/system/custom value; producer not established here | `$(agentName)` | 57: Evaluate / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(agentDn)` | 57: Evaluate / transition_actions[2].value |
| External/system/custom value; producer not established here | `$(agentId)` | 57: Evaluate / transition_actions[3].value |
| External/system/custom value; producer not established here | `$(agentSessionId)` | 57: Evaluate / transition_actions[4].value |
| External/system/custom value; producer not established here | `$(teamName)` | 57: Evaluate / transition_actions[5].value |
| External/system/custom value; producer not established here | `$(teamId)` | 57: Evaluate / transition_actions[6].value |
| External/system/custom value; producer not established here | `$(contactId)` | 57: Evaluate / transition_actions[7].value |
| External/system/custom value; producer not established here | `$(dn)` | 57: Evaluate / transition_actions[8].value |
| External/system/custom value; producer not established here | `$(orgId)` | 57: Evaluate / transition_actions[9].value |
| External/system/custom value; producer not established here | `$(queueId)` | 57: Evaluate / transition_actions[10].value |
| External/system/custom value; producer not established here | `$(queueName)` | 57: Evaluate / transition_actions[11].value |
| External/system/custom value; producer not established here | `$(siteId)` | 57: Evaluate / transition_actions[12].value |
| External/system/custom value; producer not established here | `$(customerName)` | 57: Evaluate / transition_actions[13].value |
| External/system/custom value; producer not established here | `$(contactDirection)` | 57: Evaluate / transition_actions[14].value |
| External/system/custom value; producer not established here | `$(mediaType)` | 57: Evaluate / transition_actions[15].value |
| External/system/custom value; producer not established here | `$(mediaChannel)` | 57: Evaluate / transition_actions[16].value |
| External/system/custom value; producer not established here | `$(customerId)` | 57: Evaluate / transition_actions[17].value |
| External/system/custom value; producer not established here | `$(thread)` | 57: Evaluate / transition_actions[18].value; 993: Live Chat / In-App Messaging / thread_id |
| External/system/custom value; producer not established here | `$(code)` | 114: Branch / expression; 114: Branch / outcomes[0].conditions[0].varaible; 671: Close Task / nodeInput.reason code; 671: Close Task / request_body[6].value |
| 2: Webex CC Task | `$(n2.webex.owner)` | 246: Branch / expression; 246: Branch / outcomes[0].conditions[0].varaible; 671: Close Task / nodeInput.agent ID; 671: Close Task / request_body[2].value; 720: Screen Pop / extraParamsData.agentId; 720: Screen Pop / nodeInput.agentId; 720: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(emptystring)` | 246: Branch / expression; 246: Branch / outcomes[0].conditions[0].value |
| 2: Webex CC Task | `$(n2.webex.taskId)` | 653: Close Task / nodeInput.ID; 653: Close Task / nodeInput.Task Id; 653: Close Task / path_parameters[1].value; 653: Close Task / request_body[0].value; 671: Close Task / nodeInput.ID; 671: Close Task / nodeInput.Task ID; 671: Close Task / path_parameters[1].value; 671: Close Task / request_body[0].value; 720: Screen Pop / extraParamsData.transid; 720: Screen Pop / nodeInput.transid; 720: Screen Pop / request_body[0].value |
| 2: Webex CC Task | `$(n2.webex.queue)` | 653: Close Task / nodeInput.Queue Id; 653: Close Task / request_body[3].value |
| 2: Webex CC Task | `$(n2.webex.mediaType)` | 653: Close Task / nodeInput.Media Type; 653: Close Task / request_body[5].value; 671: Close Task / nodeInput.Media type; 671: Close Task / request_body[4].value |
| External/system/custom value; producer not established here | `$(description)` | 671: Close Task / nodeInput.reason; 671: Close Task / request_body[5].value |
| custom variable; writers 57: Evaluate | `$(CustomerId)` | 720: Screen Pop / extraParamsData.queryParameters.customerId; 720: Screen Pop / nodeInput.queryParameters.customerId; 720: Screen Pop / request_body[4].value.customerId |
| External/system/custom value; producer not established here | `$(user)` | 993: Live Chat / In-App Messaging / destination |
| 1510: WXM | `$(n1510.surveyURL)` | 993: Live Chat / In-App Messaging / message |
| 2: Webex CC Task | `$(n2.webex.mediaChannel)` | 1406: Branch / expression; 1406: Branch / outcomes[0].conditions[1].varaible |
| 1477 | `$(n1477.surveyURL)` | 1511: Append Conversation / extraParamsData.text; 1511: Append Conversation / extraParamsData.textOrResponse; 1511: Append Conversation / request_body[5].value |
| External/system/custom value; producer not established here | `$(utctime)` | 1511: Append Conversation / extraParamsData.timestamp; 1511: Append Conversation / request_body[6].value |

### Boundaries and adaptation

The regex gate expects a string representation of true. Survey/questionnaire and screen-pop settings require replacement. No survey-response wait or retry loop exists. Several Evaluate/Close Task failure routes are absent, while detached terminal bindings refer to uncaptured 683/305. Screen Pop has Success/Error terminals; configuration visibility does not prove survey delivery, conversation closure or runtime variable scope.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 57: Evaluate / `oninvalidchoice` (declared target count 1); 57: Evaluate / `onerror` (declared target count 1); 653: Close Task / `oninvaliddata` (declared target count None); 653: Close Task / `onerror` (declared target count None); 653: Close Task / `oninvalidchoice` (declared target count None); 653: Close Task / `ontimeout` (declared target count None); 671: Close Task / `oninvaliddata` (declared target count None); 671: Close Task / `onerror` (declared target count None); 671: Close Task / `oninvalidchoice` (declared target count None); 671: Close Task / `ontimeout` (declared target count None).
End records reference absent producer nodes: 305, 683. These stale/unresolved parent references do not establish operative nodes or valid routes.
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
Literal node-qualified references name uncaptured producers: n1477. Their provenance is not guessed.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechatinbound-flow"></a>

## LivechatInbound flow.workflow

Observed 2026-09-09T00:08:15.873Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechatinbound-flow.json); [complete graph summary](sample-flows/summaries/wxcc-livechatinbound-flow.json). Runtime tested: **no**.

APP Start 2 enters Search Conversation 2433. `noConversationFound` and `conversationClosed` send pre-chat form 2436; Receive 2438 waits 300 seconds for `app.onformresponse`, then Evaluate 2465 prepares Resolve Conversation 2588. Active/in-queue/on-hold search results skip the form and enter Evaluate directly. Resolve created/reopened results append the received form through 2424, whose `onAppendMessageSuccess` queues Task 2259. `Queued` sends notification 1727. Resolve appended and accepted end successfully, accepted with asynchronous checking. Resolve timeout reaches Branch 2517: created/reopened closes Task 2261, appended succeeds, unmatched/error fails. Append/queue failures also close Task 2261 and send notification 2227; search/form/receive/Evaluate/other Resolve failures use 2234.

Useful handoffs: Search and every chat send retain `$(n2.inappmessaging.userId)` and threadId. Receive's on-leave actions assign customerName and customerEmail from `n2438.inappmessaging.formFields.Name` and `.Email`; Append uses its formResponse and timestamp. Evaluate defaults missing name/email to userId and constructs `detailsJson` with message, identity, attachment and scan details. Resolve consumes that object; Queue and Close consume unqualified taskId/conversationId. Branch 2517 checks unqualified `$(conversationOperation)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure APP Event | onBegin (`onbegin`) → 2433: Search Conversation |
| 1727: Queued | onSuccess (`onsuccess`) → End 2626 → Success |
| 2227: Error Notif | No outgoing route captured |
| 2234: Error Notif | No outgoing route captured |
| 2259: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 2261: Close Task; Queued → 1727: Queued |
| 2261: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 2227: Error Notif |
| 2424: Append Conversation | onAppendMessageSuccess → 2259: Queue Task; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 2261: Close Task |
| 2433: Search Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`) → 2234: Error Notif; noConversationFound, conversationClosed → 2436: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 2465: Evaluate |
| 2436: Pre-chat form | onSuccess (`onsuccess`) → 2438: Receive; onPolicyFail (`onpolicyfail`), onError (`onerror`) → 2234: Error Notif |
| 2438: Receive | onError (`onerror`), onTimeout (`ontimeout`) → 2234: Error Notif; app.onformresponse → 2465: Evaluate |
| 2465: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 2234: Error Notif; success (`1`) → 2588: Resolve Conversation |
| 2517: Branch | Create / Reopen Path → 2261: Close Task; onError (`onerror`) → End 2603 → Error; None of the above → End 2604 → Error; Append Path → End 2605 → Success |
| 2588: Resolve Conversation | created, reopened → 2424: Append Conversation; onTimeout (`ontimeout`) → 2517: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 2234: Error Notif; accepted → End 2622 → Success; appended → End 2623 → Success |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure APP Event | `$(n2.inappmessaging.message)` | 2: Configure APP Event / transition_actions[0].value; 2: Configure APP Event / transition_actions[19].value; flow-custom-defaults / customVariables[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachment)` | 2: Configure APP Event / transition_actions[11].value; 2: Configure APP Event / transition_actions[1].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure APP Event / transition_actions[2].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure APP Event / transition_actions[21].value; 2: Configure APP Event / transition_actions[3].value |
| 2: Configure APP Event | `$(n2.inappmessaging.extras)` | 2: Configure APP Event / transition_actions[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.appId)` | 2: Configure APP Event / transition_actions[5].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadId)` | 1727: Queued / thread_id; 2227: Error Notif / thread_id; 2234: Error Notif / thread_id; 2433: Search Conversation / extraParamsData.threadid; 2433: Search Conversation / request_body[4].value; 2436: Pre-chat form / thread_id; 2: Configure APP Event / transition_actions[6].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure APP Event / transition_actions[7].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure APP Event / transition_actions[8].value |
| 2: Configure APP Event | `$(n2.inappmessaging.userId)` | 1727: Queued / destination; 2227: Error Notif / destination; 2234: Error Notif / destination; 2433: Search Conversation / extraParamsData.browserfingerprint; 2433: Search Conversation / extraParamsData.customeraddress; 2433: Search Conversation / request_body[1].value; 2433: Search Conversation / request_body[5].value; 2436: Pre-chat form / destination; 2: Configure APP Event / transition_actions[9].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure APP Event / transition_actions[10].value |
| 2: Configure APP Event | `$(n2.inappmessaging.version)` | 2: Configure APP Event / transition_actions[12].value |
| 2: Configure APP Event | `$(n2.inappmessaging.timestamp)` | 2: Configure APP Event / transition_actions[13].value |
| 2: Configure APP Event | `$(n2.inappmessaging.tid)` | 2: Configure APP Event / transition_actions[14].value; 2: Configure APP Event / transition_actions[22].value |
| 2: Configure APP Event | `$(n2.service.serviceKey)` | 2: Configure APP Event / transition_actions[15].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure APP Event / transition_actions[16].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[17].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure APP Event / transition_actions[18].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReasonObject)` | 2: Configure APP Event / transition_actions[20].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure APP Event / transition_actions[23].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure APP Event / transition_actions[24].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[25].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure APP Event / transition_actions[26].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure APP Event / transition_actions[27].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure APP Event / transition_actions[28].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure APP Event / transition_actions[29].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[30].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 2227: Error Notif / message; 2234: Error Notif / message |
| External/system/custom value; producer not established here | `$(taskId)` | 2259: Queue Task / extraParamsData.id; 2259: Queue Task / nodeInput.id; 2259: Queue Task / path_parameters[1].value; 2259: Queue Task / request_body[0].value; 2259: Queue Task / transition_actions[0].value; 2261: Close Task / nodeInput.ID; 2261: Close Task / nodeInput.Task Id; 2261: Close Task / path_parameters[1].value; 2261: Close Task / request_body[0].value; 2261: Close Task / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 2259: Queue Task / extraParamsData.conversationid; 2259: Queue Task / nodeInput.conversationid; 2259: Queue Task / request_body[3].value; 2259: Queue Task / transition_actions[1].value; 2261: Close Task / nodeInput.Conversation ID; 2261: Close Task / request_body[2].value; 2424: Append Conversation / extraParamsData.conversationid; 2424: Append Conversation / path_parameters[1].value; 2424: Append Conversation / transition_actions[0].value; 2588: Resolve Conversation / transition_actions[0].value |
| 2438: Receive | `$(n2438.inappmessaging.formResponse)` | 2424: Append Conversation / extraParamsData.livechatformresponse; 2424: Append Conversation / extraParamsData.textOrResponse; 2424: Append Conversation / request_body[4].value |
| 2438: Receive | `$(n2438.inappmessaging.timestamp)` | 2424: Append Conversation / extraParamsData.timestamp; 2424: Append Conversation / request_body[6].value |
| 2433: Search Conversation | `$(n2433.aliasId)` | 2424: Append Conversation / extraParamsData.messageAliasId |
| 2438: Receive | `$(n2438.inappmessaging.formFields.Name)` | 2438: Receive / transition_actions[0].value |
| 2438: Receive | `$(n2438.inappmessaging.formFields.Email)` | 2438: Receive / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 2517: Branch / expression; 2517: Branch / outcomes[0].conditions[0].varaible; 2517: Branch / outcomes[0].conditions[1].varaible; 2517: Branch / outcomes[1].conditions[0].varaible |
| custom variable; writers 2: Configure APP Event | `$(transId)` | 2588: Resolve Conversation / extraParamsData.trackingId; 2588: Resolve Conversation / extraParamsData.transId; 2588: Resolve Conversation / nodeInput.trackingId; 2588: Resolve Conversation / nodeInput.transId; 2588: Resolve Conversation / request_body[0].value; 2588: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 2588: Resolve Conversation / extraParamsData.details; 2588: Resolve Conversation / nodeInput.details; 2588: Resolve Conversation / request_body[6].value |

### Boundaries and adaptation

Form/template, business address and fixed queue values are sample bindings. Close Task's media type is social, while Resolve and Queue use chat; retain this mismatch for adaptation. Some final notification failures have no captured route. There is no Receive retry, proactive-queue branch or AI Agent node. Internal canvas evidence is not a public import schema, and runtime testing is false.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1727: Queued / `onerror` (declared target count 1); 2227: Error Notif / `onerror` (declared target count 1); 2234: Error Notif / `onerror` (declared target count 1).
End records reference absent producer nodes: 2238, 2291, 2577. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechatinboundflowwithoutform"></a>

## LivechatInboundFlowWithoutForm.workflow

Observed 2026-09-09T00:08:44.986Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechatinboundflowwithoutform.json); [complete graph summary](sample-flows/summaries/wxcc-livechatinboundflowwithoutform.json). Runtime tested: **no**.

APP Start 2 enters Evaluate 2465 and Resolve Conversation 2307 directly: there is no Search Conversation, form send, Receive wait or form-append operation. Resolve created/reopened events queue Task 2259, and `Queued` sends acknowledgment 1727. Resolve appended ends with Success; accepted also ends with Success and asynchronous checking. A Resolve timeout enters Branch 2481, whose created/reopened path closes Task 2261, appended path succeeds and unmatched/error paths fail. Queue timeout and other configured failures also close Task 2261; its outcomes all send error notification 2227. Evaluate errors and the other Resolve failure events instead send notification 2234.

Useful handoffs: Start supplies the in-app message, user/thread identities, attachments and scan values. Evaluate substitutes userId when customerName/customerEmail are empty, assembles message/PCI/malware/security details, and serializes `detailsJson` for Resolve. Branch 2481 explicitly tests `$(n2307.conversationOperation)`. Queue/Close take `$(taskId)` and `$(conversationId)`; all chat sends target `$(n2.inappmessaging.userId)` on `$(n2.inappmessaging.threadId)`. No autonomous customer-answering or business-action node is present.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure APP Event | onBegin (`onbegin`) → 2465: Evaluate |
| 1727: Queued | No outgoing route captured |
| 2227: Error Notif | No outgoing route captured |
| 2234: Error Notif | No outgoing route captured |
| 2259: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 2261: Close Task; Queued → 1727: Queued |
| 2261: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 2227: Error Notif |
| 2307: Resolve Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 2234: Error Notif; onTimeout (`ontimeout`) → 2481: Branch; created, reopened → 2259: Queue Task; appended → End 2508 → Success; accepted → End 2509 → Success |
| 2465: Evaluate | success (`1`) → 2307: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 2234: Error Notif |
| 2481: Branch | Create/Reopen Path → 2261: Close Task; Append Path → End 2482 → Success; None of the above → End 2484 → Error; onError (`onerror`) → End 2487 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure APP Event | `$(n2.inappmessaging.message)` | 2: Configure APP Event / transition_actions[0].value; 2: Configure APP Event / transition_actions[19].value; flow-custom-defaults / customVariables[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachment)` | 2: Configure APP Event / transition_actions[11].value; 2: Configure APP Event / transition_actions[1].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure APP Event / transition_actions[2].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure APP Event / transition_actions[21].value; 2: Configure APP Event / transition_actions[3].value |
| 2: Configure APP Event | `$(n2.inappmessaging.extras)` | 2: Configure APP Event / transition_actions[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.appId)` | 2: Configure APP Event / transition_actions[5].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadId)` | 1727: Queued / thread_id; 2227: Error Notif / thread_id; 2234: Error Notif / thread_id; 2: Configure APP Event / transition_actions[6].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure APP Event / transition_actions[7].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure APP Event / transition_actions[8].value |
| 2: Configure APP Event | `$(n2.inappmessaging.userId)` | 1727: Queued / destination; 2227: Error Notif / destination; 2234: Error Notif / destination; 2: Configure APP Event / transition_actions[9].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure APP Event / transition_actions[10].value |
| 2: Configure APP Event | `$(n2.inappmessaging.version)` | 2: Configure APP Event / transition_actions[12].value |
| 2: Configure APP Event | `$(n2.inappmessaging.timestamp)` | 2: Configure APP Event / transition_actions[13].value |
| 2: Configure APP Event | `$(n2.inappmessaging.tid)` | 2: Configure APP Event / transition_actions[14].value; 2: Configure APP Event / transition_actions[22].value; 2: Configure APP Event / transition_actions[23].value |
| 2: Configure APP Event | `$(n2.service.serviceKey)` | 2: Configure APP Event / transition_actions[15].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure APP Event / transition_actions[16].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[17].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure APP Event / transition_actions[18].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReasonObject)` | 2: Configure APP Event / transition_actions[20].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[24].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure APP Event / transition_actions[25].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure APP Event / transition_actions[26].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure APP Event / transition_actions[27].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure APP Event / transition_actions[28].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure APP Event / transition_actions[29].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure APP Event / transition_actions[30].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[31].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 2227: Error Notif / message; 2234: Error Notif / message |
| External/system/custom value; producer not established here | `$(taskId)` | 2259: Queue Task / extraParamsData.id; 2259: Queue Task / nodeInput.id; 2259: Queue Task / path_parameters[1].value; 2259: Queue Task / request_body[0].value; 2261: Close Task / nodeInput.ID; 2261: Close Task / nodeInput.Task Id; 2261: Close Task / path_parameters[1].value; 2261: Close Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 2259: Queue Task / extraParamsData.conversationid; 2259: Queue Task / nodeInput.conversationid; 2259: Queue Task / request_body[3].value; 2261: Close Task / nodeInput.Conversation ID; 2261: Close Task / request_body[2].value |
| custom variable; writers 2: Configure APP Event | `$(transId)` | 2307: Resolve Conversation / extraParamsData.trackingId; 2307: Resolve Conversation / extraParamsData.transId; 2307: Resolve Conversation / nodeInput.trackingId; 2307: Resolve Conversation / nodeInput.transId; 2307: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 2307: Resolve Conversation / extraParamsData.details; 2307: Resolve Conversation / nodeInput.details; 2307: Resolve Conversation / request_body[6].value |
| 2307: Resolve Conversation | `$(n2307.conversationOperation)` | 2481: Branch / expression; 2481: Branch / outcomes[0].conditions[0].varaible; 2481: Branch / outcomes[0].conditions[1].varaible; 2481: Branch / outcomes[1].conditions[0].varaible |

### Boundaries and adaptation

The flow has no explicit cycle or retry. Close Task specifies media type social while Resolve/Queue specify chat. Extra terminal metadata references absent producer nodes, and final message failures lack captured recovery routes. Fixed queue and integration bindings need tenant-specific replacement; no resource availability is established. This internal model records configuration rather than a public import schema, and runtime testing is false.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1727: Queued / `onerror` (declared target count 1); 2227: Error Notif / `onerror` (declared target count 1); 2234: Error Notif / `onerror` (declared target count 1).
End records reference absent producer nodes: 2238, 2291. These stale/unresolved parent references do not establish operative nodes or valid routes.
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechatinboundsampleflowwithsetvariable"></a>

## LiveChatInboundSampleFlowWithSetVariable.workflow

Observed 2026-09-09T00:04:00.804Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechatinboundsampleflowwithsetvariable.json); [complete graph summary](sample-flows/summaries/wxcc-livechatinboundsampleflowwithsetvariable.json). Runtime tested: **no**.

App Start 2 enters Search Conversation 2433 using customer, app, and thread identity. No/closed conversation sends pre-chat form 2436 and waits up to 300 seconds in Receive 2635; app.onformresponse enters Evaluate 2465. Active/in-queue/on-hold search outcomes bypass the form and enter that Evaluate directly. Its numeric 1 outcome, rendered success, reaches Resolve Conversation 2588. Created/reopened goes through Append Conversation 2424 to Queue Task 2259; Queued runs Set Variable 2634, then sends queued notification 1727. Resolve appended/accepted terminates through End bindings.

Useful handoffs: Receive matches `$(n2.inappmessaging.userId)` and `$(n2.inappmessaging.threadId)`, extracting form Name/Email into customerName/customerEmail. Evaluate builds detailsJson from message, attachment, and scan context. Append records `$(n2635.inappmessaging.formResponse)` with its timestamp. Set Variable uses `$(taskId)` and maps `$(n2635.inappmessaging.formFields.IssueDescription)` and `$(n2635.inappmessaging.formFields.IssueType)` into same-named String task variables, both agent-viewable/editable, non-global, and non-reportable. Those names support the separate Task Routed extraction example.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure APP Event | onBegin (`onbegin`) → 2433: Search Conversation |
| 1727: Queued | onSuccess (`onsuccess`) → End 2648 → Success |
| 2227: Error Notif | No outgoing route captured |
| 2234: Error Notif | No outgoing route captured |
| 2259: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 2261: Close Task; Queued → 2634: Set Variable |
| 2261: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 2227: Error Notif |
| 2424: Append Conversation | onAppendMessageSuccess → 2259: Queue Task; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 2261: Close Task |
| 2433: Search Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`) → 2234: Error Notif; noConversationFound, conversationClosed → 2436: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 2465: Evaluate |
| 2436: Pre-chat form | onPolicyFail (`onpolicyfail`), onError (`onerror`) → 2234: Error Notif; onSuccess (`onsuccess`) → 2635: Receive |
| 2465: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 2234: Error Notif; success (`1`) → 2588: Resolve Conversation |
| 2517: Branch | Create / Reopen Path → 2261: Close Task; onError (`onerror`) → End 2603 → Error; None of the above → End 2604 → Error; Append Path → End 2605 → Success |
| 2588: Resolve Conversation | created, reopened → 2424: Append Conversation; onTimeout (`ontimeout`) → 2517: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 2234: Error Notif; accepted → End 2653 → Success; appended → End 2654 → Success |
| 2634: Set Variable | onTimeout (`ontimeout`), Task Updated, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Invalid Token, Bad Request, Not Found, serviceUnavailable, Task Failed → 1727: Queued |
| 2635: Receive | app.onformresponse → 2465: Evaluate; onTimeout (`ontimeout`), onError (`onerror`) → 2234: Error Notif |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure APP Event | `$(n2.inappmessaging.message)` | 2: Configure APP Event / transition_actions[0].value; 2: Configure APP Event / transition_actions[19].value; flow-custom-defaults / customVariables[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachment)` | 2: Configure APP Event / transition_actions[11].value; 2: Configure APP Event / transition_actions[1].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure APP Event / transition_actions[20].value; 2: Configure APP Event / transition_actions[2].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure APP Event / transition_actions[21].value; 2: Configure APP Event / transition_actions[3].value |
| 2: Configure APP Event | `$(n2.inappmessaging.extras)` | 2: Configure APP Event / transition_actions[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.appId)` | 2433: Search Conversation / extraParamsData.bizaddress; 2433: Search Conversation / nodeInput.bizaddress; 2433: Search Conversation / request_body[2].value; 2: Configure APP Event / transition_actions[5].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadId)` | 1727: Queued / thread_id; 2227: Error Notif / thread_id; 2234: Error Notif / thread_id; 2433: Search Conversation / extraParamsData.threadid; 2433: Search Conversation / nodeInput.threadid; 2433: Search Conversation / request_body[4].value; 2436: Pre-chat form / thread_id; 2: Configure APP Event / transition_actions[6].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure APP Event / transition_actions[7].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure APP Event / transition_actions[8].value |
| 2: Configure APP Event | `$(n2.inappmessaging.userId)` | 1727: Queued / destination; 2227: Error Notif / destination; 2234: Error Notif / destination; 2433: Search Conversation / extraParamsData.browserfingerprint; 2433: Search Conversation / extraParamsData.customeraddress; 2433: Search Conversation / nodeInput.browserfingerprint; 2433: Search Conversation / nodeInput.customeraddress; 2433: Search Conversation / request_body[1].value; 2433: Search Conversation / request_body[5].value; 2436: Pre-chat form / destination; 2: Configure APP Event / transition_actions[9].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure APP Event / transition_actions[10].value |
| 2: Configure APP Event | `$(n2.inappmessaging.version)` | 2: Configure APP Event / transition_actions[12].value |
| 2: Configure APP Event | `$(n2.inappmessaging.timestamp)` | 2: Configure APP Event / transition_actions[13].value |
| 2: Configure APP Event | `$(n2.inappmessaging.tid)` | 2: Configure APP Event / transition_actions[14].value; 2: Configure APP Event / transition_actions[22].value |
| 2: Configure APP Event | `$(n2.service.serviceKey)` | 2: Configure APP Event / transition_actions[15].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure APP Event / transition_actions[16].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[17].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure APP Event / transition_actions[18].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure APP Event / transition_actions[23].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure APP Event / transition_actions[24].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[25].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure APP Event / transition_actions[26].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure APP Event / transition_actions[27].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure APP Event / transition_actions[28].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure APP Event / transition_actions[29].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[30].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 2227: Error Notif / message; 2234: Error Notif / message |
| External/system/custom value; producer not established here | `$(taskId)` | 2259: Queue Task / extraParamsData.id; 2259: Queue Task / path_parameters[1].value; 2259: Queue Task / request_body[0].value; 2259: Queue Task / transition_actions[0].value; 2261: Close Task / nodeInput.ID; 2261: Close Task / nodeInput.Task Id; 2261: Close Task / path_parameters[1].value; 2261: Close Task / request_body[0].value; 2261: Close Task / transition_actions[0].value; 2634: Set Variable / extraParamsData.id; 2634: Set Variable / nodeInput.id; 2634: Set Variable / path_parameters[1].value; 2634: Set Variable / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 2259: Queue Task / extraParamsData.conversationid; 2259: Queue Task / request_body[3].value; 2259: Queue Task / transition_actions[1].value; 2261: Close Task / nodeInput.Conversation ID; 2261: Close Task / request_body[2].value; 2424: Append Conversation / extraParamsData.conversationid; 2424: Append Conversation / path_parameters[1].value; 2424: Append Conversation / transition_actions[0].value; 2588: Resolve Conversation / transition_actions[0].value |
| 2635: Receive | `$(n2635.inappmessaging.formResponse)` | 2424: Append Conversation / extraParamsData.livechatformresponse; 2424: Append Conversation / extraParamsData.textOrResponse; 2424: Append Conversation / request_body[4].value |
| 2635: Receive | `$(n2635.inappmessaging.timestamp)` | 2424: Append Conversation / extraParamsData.timestamp; 2424: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 2517: Branch / expression; 2517: Branch / outcomes[0].conditions[0].varaible; 2517: Branch / outcomes[0].conditions[1].varaible; 2517: Branch / outcomes[1].conditions[0].varaible |
| custom variable; writers 2: Configure APP Event | `$(transId)` | 2588: Resolve Conversation / extraParamsData.trackingId; 2588: Resolve Conversation / extraParamsData.transId; 2588: Resolve Conversation / request_body[0].value; 2588: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 2588: Resolve Conversation / extraParamsData.details; 2588: Resolve Conversation / request_body[6].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.IssueDescription)` | 2634: Set Variable / extraParamsData.fv[0].value; 2634: Set Variable / extraParamsData.value; 2634: Set Variable / extraParamsData.vrbls[0].value; 2634: Set Variable / nodeInput.fv[0].value; 2634: Set Variable / nodeInput.value; 2634: Set Variable / nodeInput.vrbls[0].value; 2634: Set Variable / request_body[2].value[0].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.IssueType)` | 2634: Set Variable / extraParamsData.fv[1].value; 2634: Set Variable / extraParamsData.vrbls[1].value; 2634: Set Variable / nodeInput.fv[1].value; 2634: Set Variable / nodeInput.vrbls[1].value; 2634: Set Variable / request_body[2].value[1].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.Name)` | 2635: Receive / transition_actions[0].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.Email)` | 2635: Receive / transition_actions[1].value |

### Boundaries and adaptation

All listed Set Variable outcomes, including Task Failed and errors, still send the queued notification; it is not proof that variables were stored. Form-field consumers depend on the pre-chat path. Queue uses chat media type while Close Task 2261 stores social, a captured mismatch. Resolve timeout closes only create/reopen; several End records refer to absent parents. App/form/queue values and conversationId need binding. No runtime test or desktop-variable propagation occurred. This internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1727: Queued / `onerror` (declared target count 1); 2227: Error Notif / `onerror` (declared target count 1); 2234: Error Notif / `onerror` (declared target count 1).
End records reference absent producer nodes: 2238, 2291, 2577. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechatinboundsampleflowwithsetvariablepiqandewt"></a>

## LiveChatInboundSampleFlowWithSetVariablePIQAndEWT.workflow

Observed 2026-09-09T00:07:00.851Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechatinboundsampleflowwithsetvariablepiqandewt.json); [complete graph summary](sample-flows/summaries/wxcc-livechatinboundsampleflowwithsetvariablepiqandewt.json). Runtime tested: **no**.

Incoming-message Start 2 searches at 2433. Missing/closed conversations send pre-chat form 2436 and Receive 2635 waits 300 seconds; active/in-queue/on-hold conversations bypass the form. Both paths normalize message and scan data in Evaluate 2465, then Resolve Conversation 2588. Created/reopened results append the form at 2424, queue the task at 2259, set task variables at 2634, and send queued notice 1727. Every captured Set Variable outcome continues to that notice; only its successful-send route fetches PIQ/EWT at 2475. PIQ success sends both values at 2476, while `InsufficientData` sends position alone at 2477. Both sends end Success/Error. Resolve appended/accepted terminates Success; resolve timeout branches at 2517. Queue/append failures attempt Close Task 2261 then send error notice 2227; form/search/parse failures use 2234.

Useful handoffs: Receive saves Name/Email into customer variables. Append consumes `$(n2635.inappmessaging.formResponse)` and timestamp; Set Variable copies `formFields.IssueDescription` and `formFields.IssueType` from that same Receive into agent-viewable, editable task fields. Resolve consumes `$(detailsJson)`; queue/set/PIQ consume custom `$(taskId)`. PIQ uses `$(queue)` with lookback minutes 5, extracting `positionInQueue` from `$.piq` and `estimatedWaitTime` from `$.ewt` for the two notices.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure APP Event | onBegin (`onbegin`) → 2433: Search Conversation |
| 1727: Queued | onSuccess (`onsuccess`) → 2475: PIQ and EWT |
| 2227: Error Notif | No outgoing route captured |
| 2234: Error Notif | No outgoing route captured |
| 2259: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 2261: Close Task; Queued → 2634: Set Variable |
| 2261: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Success, Error, onauthorizationfail → 2227: Error Notif |
| 2424: Append Conversation | onAppendMessageSuccess → 2259: Queue Task; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 2261: Close Task |
| 2433: Search Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`) → 2234: Error Notif; noConversationFound, conversationClosed → 2436: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 2465: Evaluate |
| 2436: Pre-chat form | onPolicyFail (`onpolicyfail`), onError (`onerror`) → 2234: Error Notif; onSuccess (`onsuccess`) → 2635: Receive |
| 2465: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 2234: Error Notif; success (`1`) → 2588: Resolve Conversation |
| 2475: PIQ and EWT | InsufficientData → 2477: Live Chat / In-App Messaging; Success → 2476: Live Chat / In-App Messaging; onInvalidData (`oninvaliddata`) → End 2656 → Error; onError (`onerror`) → End 2657 → Error; onInvalidChoice (`oninvalidchoice`) → End 2658 → Error; serviceUnavailable → End 2659 → Error; Error → End 2660 → Error; onTimeout (`ontimeout`) → End 2661 → Error |
| 2476: Live Chat / In-App Messaging | onSuccess (`onsuccess`) → End 2502 → Success; onError (`onerror`) → End 2504 → Error; onPolicyFail (`onpolicyfail`) → End 2507 → Error |
| 2477: Live Chat / In-App Messaging | onSuccess (`onsuccess`) → End 2508 → Success; onError (`onerror`) → End 2510 → Error; onPolicyFail (`onpolicyfail`) → End 2513 → Error |
| 2517: Branch | Create / Reopen Path → 2261: Close Task; onError (`onerror`) → End 2603 → Error; None of the above → End 2604 → Error; Append Path → End 2605 → Success |
| 2588: Resolve Conversation | created, reopened → 2424: Append Conversation; onTimeout (`ontimeout`) → 2517: Branch; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 2234: Error Notif; accepted → End 2664 → Success; appended → End 2665 → Success |
| 2634: Set Variable | onTimeout (`ontimeout`), Task Updated, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onauthorizationfail, Invalid Token, Bad Request, Not Found, serviceUnavailable, Task Failed → 1727: Queued |
| 2635: Receive | app.onformresponse → 2465: Evaluate; onTimeout (`ontimeout`), onError (`onerror`) → 2234: Error Notif |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure APP Event | `$(n2.inappmessaging.message)` | 2: Configure APP Event / transition_actions[0].value; 2: Configure APP Event / transition_actions[19].value; flow-custom-defaults / customVariables[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachment)` | 2: Configure APP Event / transition_actions[11].value; 2: Configure APP Event / transition_actions[1].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure APP Event / transition_actions[20].value; 2: Configure APP Event / transition_actions[2].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure APP Event / transition_actions[21].value; 2: Configure APP Event / transition_actions[3].value |
| 2: Configure APP Event | `$(n2.inappmessaging.extras)` | 2: Configure APP Event / transition_actions[4].value |
| 2: Configure APP Event | `$(n2.inappmessaging.appId)` | 2433: Search Conversation / extraParamsData.bizaddress; 2433: Search Conversation / nodeInput.bizaddress; 2433: Search Conversation / request_body[2].value; 2: Configure APP Event / transition_actions[5].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadId)` | 1727: Queued / thread_id; 2227: Error Notif / thread_id; 2234: Error Notif / thread_id; 2433: Search Conversation / extraParamsData.threadid; 2433: Search Conversation / nodeInput.threadid; 2433: Search Conversation / request_body[4].value; 2436: Pre-chat form / thread_id; 2476: Live Chat / In-App Messaging / thread_id; 2477: Live Chat / In-App Messaging / thread_id; 2: Configure APP Event / transition_actions[6].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure APP Event / transition_actions[7].value |
| 2: Configure APP Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure APP Event / transition_actions[8].value |
| 2: Configure APP Event | `$(n2.inappmessaging.userId)` | 1727: Queued / destination; 2227: Error Notif / destination; 2234: Error Notif / destination; 2433: Search Conversation / extraParamsData.browserfingerprint; 2433: Search Conversation / extraParamsData.customeraddress; 2433: Search Conversation / nodeInput.browserfingerprint; 2433: Search Conversation / nodeInput.customeraddress; 2433: Search Conversation / request_body[1].value; 2433: Search Conversation / request_body[5].value; 2436: Pre-chat form / destination; 2476: Live Chat / In-App Messaging / destination; 2477: Live Chat / In-App Messaging / destination; 2: Configure APP Event / transition_actions[9].value |
| 2: Configure APP Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure APP Event / transition_actions[10].value |
| 2: Configure APP Event | `$(n2.inappmessaging.version)` | 2: Configure APP Event / transition_actions[12].value |
| 2: Configure APP Event | `$(n2.inappmessaging.timestamp)` | 2: Configure APP Event / transition_actions[13].value |
| 2: Configure APP Event | `$(n2.inappmessaging.tid)` | 2: Configure APP Event / transition_actions[14].value; 2: Configure APP Event / transition_actions[22].value |
| 2: Configure APP Event | `$(n2.service.serviceKey)` | 2: Configure APP Event / transition_actions[15].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure APP Event / transition_actions[16].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[17].value |
| 2: Configure APP Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure APP Event / transition_actions[18].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure APP Event / transition_actions[23].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure APP Event / transition_actions[24].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[25].value |
| 2: Configure APP Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure APP Event / transition_actions[26].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure APP Event / transition_actions[27].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure APP Event / transition_actions[28].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure APP Event / transition_actions[29].value |
| 2: Configure APP Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure APP Event / transition_actions[30].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 2227: Error Notif / message; 2234: Error Notif / message |
| External/system/custom value; producer not established here | `$(taskId)` | 2259: Queue Task / extraParamsData.id; 2259: Queue Task / path_parameters[1].value; 2259: Queue Task / request_body[0].value; 2259: Queue Task / transition_actions[0].value; 2261: Close Task / nodeInput.ID; 2261: Close Task / nodeInput.Task Id; 2261: Close Task / path_parameters[1].value; 2261: Close Task / request_body[0].value; 2261: Close Task / transition_actions[0].value; 2475: PIQ and EWT / extraParamsData.taskid; 2475: PIQ and EWT / nodeInput.taskid; 2475: PIQ and EWT / path_parameters[2].value; 2475: PIQ and EWT / transition_actions[0].value; 2634: Set Variable / extraParamsData.id; 2634: Set Variable / nodeInput.id; 2634: Set Variable / path_parameters[1].value; 2634: Set Variable / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 2259: Queue Task / extraParamsData.conversationid; 2259: Queue Task / request_body[3].value; 2259: Queue Task / transition_actions[1].value; 2261: Close Task / nodeInput.Conversation ID; 2261: Close Task / request_body[2].value; 2424: Append Conversation / extraParamsData.conversationid; 2424: Append Conversation / path_parameters[1].value; 2424: Append Conversation / transition_actions[0].value; 2475: PIQ and EWT / transition_actions[1].value; 2588: Resolve Conversation / transition_actions[0].value |
| 2635: Receive | `$(n2635.inappmessaging.formResponse)` | 2424: Append Conversation / extraParamsData.livechatformresponse; 2424: Append Conversation / extraParamsData.textOrResponse; 2424: Append Conversation / request_body[4].value |
| 2635: Receive | `$(n2635.inappmessaging.timestamp)` | 2424: Append Conversation / extraParamsData.timestamp; 2424: Append Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(queue)` | 2475: PIQ and EWT / extraParamsData.queueid; 2475: PIQ and EWT / nodeInput.queueid; 2475: PIQ and EWT / path_parameters[1].value |
| 2475: PIQ and EWT | `$(n2475.positionInQueue)` | 2476: Live Chat / In-App Messaging / message; 2477: Live Chat / In-App Messaging / message |
| 2475: PIQ and EWT | `$(n2475.estimatedWaitTime)` | 2476: Live Chat / In-App Messaging / message |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 2517: Branch / expression; 2517: Branch / outcomes[0].conditions[0].varaible; 2517: Branch / outcomes[0].conditions[1].varaible; 2517: Branch / outcomes[1].conditions[0].varaible |
| custom variable; writers 2: Configure APP Event | `$(transId)` | 2588: Resolve Conversation / extraParamsData.trackingId; 2588: Resolve Conversation / extraParamsData.transId; 2588: Resolve Conversation / nodeInput.trackingId; 2588: Resolve Conversation / nodeInput.transId; 2588: Resolve Conversation / request_body[0].value; 2588: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 2588: Resolve Conversation / extraParamsData.details; 2588: Resolve Conversation / nodeInput.details; 2588: Resolve Conversation / request_body[6].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.IssueDescription)` | 2634: Set Variable / extraParamsData.fv[0].value; 2634: Set Variable / extraParamsData.value; 2634: Set Variable / extraParamsData.vrbls[0].value; 2634: Set Variable / nodeInput.fv[0].value; 2634: Set Variable / nodeInput.value; 2634: Set Variable / nodeInput.vrbls[0].value; 2634: Set Variable / request_body[2].value[0].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.IssueType)` | 2634: Set Variable / extraParamsData.fv[1].value; 2634: Set Variable / extraParamsData.vrbls[1].value; 2634: Set Variable / nodeInput.fv[1].value; 2634: Set Variable / nodeInput.vrbls[1].value; 2634: Set Variable / request_body[2].value[1].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.Name)` | 2635: Receive / transition_actions[0].value |
| 2635: Receive | `$(n2635.inappmessaging.formFields.Email)` | 2635: Receive / transition_actions[1].value |

### Boundaries and adaptation

This retrieves queue status once; no polling or conversational loop is captured. Task-variable update failure is intentionally not a gate before the queued notice. Close Task is configured with media type `social` although Queue Task uses `chat`; the custom queue binding also needs reconciliation with the selected queue. Some notification failure routes and detached terminal producers are unresolved. Form template, tenant bindings and all runtime behavior remain untested.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1727: Queued / `onerror` (declared target count 1); 2227: Error Notif / `onerror` (declared target count 1); 2234: Error Notif / `onerror` (declared target count 1).
End records reference absent producer nodes: 2238, 2291, 2577. These stale/unresolved parent references do not establish operative nodes or valid routes.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-livechatqabotinboundflow"></a>

## LiveChatQABotInboundFlow.workflow

Observed 2026-09-09T00:03:14.397Z. [Captured model](../evidence/sample-flows/observed/wxcc-livechatqabotinboundflow.json); [complete graph summary](sample-flows/summaries/wxcc-livechatqabotinboundflow.json). Runtime tested: **no**.

App Start 2 searches conversation 1621. No/closed conversation sends form 36 and waits 300 seconds in Receive 38; active/in-queue/on-hold goes straight to Evaluate 1610. Resolve Conversation 1590 then sends created/reopened through Append form response 1254 into QnA bot 1661. onSuccess sends reply 745, timestamps it, and appends outbound 1273. Branch 1668 closes on Article containing Goodbye; otherwise Receive 756 waits 120 seconds. app.mo → Evaluate 1559 → filtering Branches 1108/1121 → inbound Append 1332 → bot forms the reply loop. onAgentHandover sends/appends a handoff message and queues task 1388.

Useful handoffs: Search and both Receives use the original app/user/thread identity. Form response provides customerName/customerEmail, while subsequent Receive refreshes `questionForBot` and message from `$(n756.receive.message)` plus attachments/scan state. Bot inputs use `consumer.uid=$(n2.inappmessaging.userId)`, correlation_id `$(transid)`, platform web, and `$(questionForBot)`. `$(n1661.TextResponse)` feeds channel Send and outbound Append; inbound Append uses `$(message)`, `$(n756.inappmessaging.timestamp)`, and `$(parseDataAttachment)`. Task operations consume taskId/conversationId; appended/accepted Resolve outcomes terminate.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure Mobile & Web App Event | onBegin (`onbegin`) → 1621: Search Conversation |
| 36: Pre-chat form | onSuccess (`onsuccess`) → 38: Receive; onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1487: Error notif |
| 38: Receive | app.onformresponse → 1610: Evaluate; onError (`onerror`), onTimeout (`ontimeout`) → 372: Close conversation notify |
| 372: Close conversation notify | onError (`onerror`), onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`) → 1357: Close Task |
| 745: Send Bot resposne | onSuccess (`onsuccess`) → 1160: Get current time; onError (`onerror`) → End 1662 → Error; onPolicyFail (`onpolicyfail`) → End 1663 → Error |
| 756: Receive | onTimeout (`ontimeout`), onError (`onerror`) → 1519: Close chat notification; app.mo → 1559: Evaluate |
| 768: Connecting to agent notification | onSuccess (`onsuccess`) → 1472: Get current time; onError (`onerror`) → End 1664 → Error; onPolicyFail (`onpolicyfail`) → End 1665 → Error |
| 1108: Branch | invalid msgs → 1121: Branch; None of the above → 1332: Append Conversation; onError (`onerror`) → 1357: Close Task |
| 1121: Branch | invalid msgs → 756: Receive; None of the above → 1332: Append Conversation; onError (`onerror`) → 1357: Close Task |
| 1160: Get current time | timern (`1`) → 1273: Append Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1357: Close Task |
| 1254: Append Conversation | onInvalidData (`oninvaliddata`), onTimeout (`ontimeout`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1661: QnA bot |
| 1273: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onTimeout (`ontimeout`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1668: Branch |
| 1332: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task; onAppendMessageSuccess → 1661: QnA bot |
| 1357: Close Task | Success, onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error → 1513: Error notif |
| 1388: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1357: Close Task; Queued → 1613: Queued |
| 1465: Append Conversation | onAppendMessageSuccess → 1388: Queue Task; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onTimeout (`ontimeout`), Failure, onAppendMessageFailure, onauthorizationfail → 1357: Close Task |
| 1472: Get current time | timern (`1`) → 1465: Append Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1357: Close Task |
| 1487: Error notif | onSuccess (`onsuccess`) → End 1641 → Success |
| 1513: Error notif | onError (`onerror`) → End 1639 → Error; onPolicyFail (`onpolicyfail`) → End 1640 → Error; onError (`onerror`) → End 1649 → Error; onPolicyFail (`onpolicyfail`) → End 1650 → Error; onSuccess (`onsuccess`) → End 1651 → Success |
| 1519: Close chat notification | onSuccess (`onsuccess`), onError (`onerror`), onPolicyFail (`onpolicyfail`) → 1357: Close Task |
| 1559: Evaluate | success (`1`) → 1108: Branch; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1357: Close Task |
| 1590: Resolve Conversation | created, reopened → 1254: Append Conversation; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed → 1487: Error notif; onTimeout (`ontimeout`) → 1632: Branch; onauthorizationfail → 372: Close conversation notify; appended → End 1693 → Success; accepted → End 1694 → Success |
| 1610: Evaluate | success (`1`) → 1590: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1487: Error notif |
| 1613: Queued | onSuccess (`onsuccess`) → End 1614 → Success; onError (`onerror`) → End 1616 → Error; onPolicyFail (`onpolicyfail`) → End 1619 → Error |
| 1621: Search Conversation | noConversationFound, conversationClosed → 36: Pre-chat form; conversationActive, conversationInQueue, conversationOnHold → 1610: Evaluate; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`) → 1487: Error notif |
| 1632: Branch | Create/Reopen Path → 1357: Close Task; onError (`onerror`) → End 1644 → Error; Append Path → End 1645 → Success; None of the above → End 1646 → Error |
| 1661: QnA bot | onSuccess → 745: Send Bot resposne; onAgentHandover → 768: Connecting to agent notification; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onFailure → 1357: Close Task |
| 1668: Branch | None of the above → 756: Receive; Close Bot Conversation, onError (`onerror`) → 1669: Close Task |
| 1669: Close Task | onTimeout (`ontimeout`) → End 1670 → Error; Success → End 1672 → Success; onInvalidData (`oninvaliddata`) → End 1675 → Error; onError (`onerror`) → End 1679 → Error; onInvalidChoice (`oninvalidchoice`) → End 1684 → Error; Error → End 1690 → Error |

**Loops in the captured graph:** 745: Send Bot resposne → 756: Receive → 1108: Branch → 1121: Branch → 1160: Get current time → 1273: Append Conversation → 1332: Append Conversation → 1559: Evaluate → 1661: QnA bot → 1668: Branch. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.message)` | 2: Configure Mobile & Web App Event / transition_actions[0].value; 2: Configure Mobile & Web App Event / transition_actions[19].value; 2: Configure Mobile & Web App Event / transition_actions[32].value; 2: Configure Mobile & Web App Event / transition_actions[3].value; flow-custom-defaults / customVariables[6].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.attachment)` | 2: Configure Mobile & Web App Event / transition_actions[12].value; 2: Configure Mobile & Web App Event / transition_actions[1].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.nonPCIComplianceReason)` | 2: Configure Mobile & Web App Event / transition_actions[20].value; 2: Configure Mobile & Web App Event / transition_actions[2].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.appId)` | 1621: Search Conversation / extraParamsData.bizaddress; 1621: Search Conversation / nodeInput.bizaddress; 1621: Search Conversation / request_body[2].value; 2: Configure Mobile & Web App Event / transition_actions[4].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isPCIValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[21].value; 2: Configure Mobile & Web App Event / transition_actions[5].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.extras)` | 2: Configure Mobile & Web App Event / transition_actions[6].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadId)` | 1487: Error notif / thread_id; 1513: Error notif / thread_id; 1519: Close chat notification / thread_id; 1613: Queued / thread_id; 1621: Search Conversation / extraParamsData.threadid; 1621: Search Conversation / nodeInput.threadid; 1621: Search Conversation / request_body[4].value; 2: Configure Mobile & Web App Event / transition_actions[7].value; 36: Pre-chat form / thread_id; 372: Close conversation notify / thread_id; 745: Send Bot resposne / thread_id; 768: Connecting to agent notification / thread_id |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadTitle)` | 2: Configure Mobile & Web App Event / transition_actions[8].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.threadStatus)` | 2: Configure Mobile & Web App Event / transition_actions[9].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.userId)` | 1487: Error notif / destination; 1513: Error notif / destination; 1519: Close chat notification / destination; 1613: Queued / destination; 1621: Search Conversation / extraParamsData.browserfingerprint; 1621: Search Conversation / extraParamsData.customeraddress; 1621: Search Conversation / nodeInput.browserfingerprint; 1621: Search Conversation / nodeInput.customeraddress; 1621: Search Conversation / request_body[1].value; 1621: Search Conversation / request_body[5].value; 1661: QnA bot / extraParamsData.consumer.uid; 1661: QnA bot / extraParamsData.request_body.consumer.uid; 1661: QnA bot / extraParamsData.uid; 1661: QnA bot / nodeInput.consumer.uid; 1661: QnA bot / nodeInput.request_body.consumer.uid; 1661: QnA bot / nodeInput.uid; 1661: QnA bot / request_body[0].value.consumer.uid; 2: … [full value in graph summary] |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.attachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[11].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.version)` | 2: Configure Mobile & Web App Event / transition_actions[13].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.timestamp)` | 2: Configure Mobile & Web App Event / transition_actions[14].value |
| 2: Configure Mobile & Web App Event | `$(n2.service.serviceKey)` | 2: Configure Mobile & Web App Event / transition_actions[15].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isAttachmentEnabled)` | 2: Configure Mobile & Web App Event / transition_actions[16].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[17].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.pciInfo.isPCICompliance)` | 2: Configure Mobile & Web App Event / transition_actions[18].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.tid)` | 2: Configure Mobile & Web App Event / transition_actions[22].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[23].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.securityFailedReason)` | 2: Configure Mobile & Web App Event / transition_actions[24].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[25].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.securityscaninfo.isSecurityCompliance)` | 2: Configure Mobile & Web App Event / transition_actions[26].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.isMalwareValidationDone)` | 2: Configure Mobile & Web App Event / transition_actions[27].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.isMalwareCompliance)` | 2: Configure Mobile & Web App Event / transition_actions[28].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.malwareFailedReason)` | 2: Configure Mobile & Web App Event / transition_actions[29].value |
| 2: Configure Mobile & Web App Event | `$(n2.inappmessaging.malwareinfo.droppedAttachmentCount)` | 2: Configure Mobile & Web App Event / transition_actions[30].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(appId)` | 2: Configure Mobile & Web App Event / transition_actions[31].value |
| 38: Receive | `$(n38.inappmessaging.message)` | 38: Receive / transition_actions[0].value |
| 38: Receive | `$(n38.inappmessaging.timestamp)` | 1254: Append Conversation / extraParamsData.timestamp; 1254: Append Conversation / request_body[6].value; 38: Receive / transition_actions[1].value |
| 38: Receive | `$(n38.inappmessaging.formFields.Name)` | 38: Receive / transition_actions[2].value |
| 38: Receive | `$(n38.inappmessaging.formFields.Email)` | 38: Receive / transition_actions[3].value |
| 1661: QnA bot | `$(n1661.TextResponse)` | 1273: Append Conversation / extraParamsData.text; 1273: Append Conversation / extraParamsData.textOrResponse; 1273: Append Conversation / request_body[5].value; 1465: Append Conversation / extraParamsData.text; 1465: Append Conversation / extraParamsData.textOrResponse; 1465: Append Conversation / request_body[5].value; 1661: QnA bot / transition_actions[0].value; 745: Send Bot resposne / message; 768: Connecting to agent notification / message |
| 756: Receive | `$(n756.receive.message)` | 1108: Branch / expression; 1108: Branch / outcomes[0].conditions[0].varaible; 1108: Branch / outcomes[0].conditions[1].varaible; 1121: Branch / expression; 1121: Branch / outcomes[0].conditions[0].varaible; 1121: Branch / outcomes[0].conditions[1].varaible; 756: Receive / transition_actions[0].value; 756: Receive / transition_actions[2].value; 756: Receive / transition_actions[8].value |
| 756: Receive | `$(n756.inappmessaging.timestamp)` | 1332: Append Conversation / extraParamsData.timestamp; 1332: Append Conversation / request_body[6].value; 756: Receive / transition_actions[10].value; 756: Receive / transition_actions[1].value |
| 756: Receive | `$(n756.inappmessaging.attachment)` | 756: Receive / transition_actions[12].value; 756: Receive / transition_actions[3].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.isSecurityValidationDone)` | 756: Receive / transition_actions[4].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.securityFailedReason)` | 756: Receive / transition_actions[5].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.isSecurityCompliance)` | 756: Receive / transition_actions[6].value |
| 756: Receive | `$(n756.inappmessaging.securityscaninfo.droppedAttachmentCount)` | 756: Receive / transition_actions[7].value |
| 756: Receive | `$(n756.inappmessaging.message)` | 756: Receive / transition_actions[9].value |
| 756: Receive | `$(n756.receive.attachment)` | 756: Receive / transition_actions[11].value |
| 756: Receive | `$(n756.receive.payload)` | 756: Receive / transition_actions[13].value |
| External/system/custom value; producer not established here | `$(timern)` | 1160: Get current time / transition_actions[0].value; 1273: Append Conversation / extraParamsData.timestamp; 1273: Append Conversation / request_body[6].value; 1465: Append Conversation / extraParamsData.timestamp; 1465: Append Conversation / request_body[6].value; 1472: Get current time / transition_actions[0].value |
| 1160: Get current time | `$(n1160.evaluate.output)` | 1160: Get current time / transition_actions[1].value; 1472: Get current time / transition_actions[1].value |
| 38: Receive | `$(n38.inappmessaging.formResponse)` | 1254: Append Conversation / extraParamsData.livechatformresponse; 1254: Append Conversation / extraParamsData.textOrResponse; 1254: Append Conversation / request_body[4].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1254: Append Conversation / extraParamsData.conversationid; 1254: Append Conversation / path_parameters[1].value; 1273: Append Conversation / extraParamsData.conversationid; 1273: Append Conversation / path_parameters[1].value; 1332: Append Conversation / extraParamsData.conversationid; 1332: Append Conversation / path_parameters[1].value; 1357: Close Task / nodeInput.Conversation ID; 1357: Close Task / request_body[2].value; 1388: Queue Task / extraParamsData.conversationid; 1388: Queue Task / request_body[3].value; 1388: Queue Task / transition_actions[1].value; 1465: Append Conversation / extraParamsData.conversationid; 1465: Append Conversation / path_parameters[1].value; 1590: Resolve Conversation / transition_actions[2].value; 1669: Close Task / request_body[2].value |
| custom variable; writers 2: Configure Mobile & Web App Event, 756: Receive | `$(message)` | 1332: Append Conversation / extraParamsData.text; 1332: Append Conversation / extraParamsData.textOrResponse; 1332: Append Conversation / request_body[5].value; 1559: Evaluate / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(parseDataAttachment)` | 1332: Append Conversation / extraParamsData.attachments; 1332: Append Conversation / request_body[7].value; 1332: Append Conversation / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1357: Close Task / nodeInput.ID; 1357: Close Task / nodeInput.Task Id; 1357: Close Task / path_parameters[1].value; 1357: Close Task / request_body[0].value; 1357: Close Task / transition_actions[0].value; 1388: Queue Task / extraParamsData.id; 1388: Queue Task / path_parameters[1].value; 1388: Queue Task / request_body[0].value; 1388: Queue Task / transition_actions[0].value; 1590: Resolve Conversation / transition_actions[0].value; 1669: Close Task / path_parameters[1].value; 1669: Close Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1487: Error notif / message; 1513: Error notif / message |
| custom variable; writers 2: Configure Mobile & Web App Event, 756: Receive | `$(inappPayloadObject)` | 1559: Evaluate / transition_actions[1].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(nonPCIComplianceReasonObject)` | 1559: Evaluate / transition_actions[2].value |
| External/system/custom value; producer not established here | `$(tid)` | 1559: Evaluate / transition_actions[3].value |
| External/system/custom value; producer not established here | `$(flid)` | 1559: Evaluate / transition_actions[4].value |
| 9 | `$(n9.evaluate.output)` | 1559: Evaluate / transition_actions[5].value |
| custom variable; writers 2: Configure Mobile & Web App Event | `$(transId)` | 1590: Resolve Conversation / extraParamsData.trackingId; 1590: Resolve Conversation / extraParamsData.transId; 1590: Resolve Conversation / request_body[0].value; 1590: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1590: Resolve Conversation / extraParamsData.details; 1590: Resolve Conversation / request_body[6].value; 1610: Evaluate / transition_actions[0].value |
| custom variable; writers 38: Receive | `$(customerName)` | 1590: Resolve Conversation / transition_actions[3].value |
| custom variable; writers 38: Receive | `$(customerEmail)` | 1590: Resolve Conversation / transition_actions[4].value |
| 1590: Resolve Conversation | `$(n1590.conversationOperation)` | 1632: Branch / expression; 1632: Branch / outcomes[0].conditions[0].varaible; 1632: Branch / outcomes[0].conditions[1].varaible; 1632: Branch / outcomes[1].conditions[0].varaible; 1632: Branch / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(transid)` | 1661: QnA bot / extraParamsData.request_body.correlation_id; 1661: QnA bot / extraParamsData.transid; 1661: QnA bot / nodeInput.request_body.correlation_id; 1661: QnA bot / nodeInput.transid; 1661: QnA bot / request_body[0].value.correlation_id |
| custom variable; writers 1559: Evaluate, 2: Configure Mobile & Web App Event, 38: Receive, 756: Receive | `$(questionForBot)` | 1661: QnA bot / extraParamsData.msg; 1661: QnA bot / extraParamsData.request_body.msg; 1661: QnA bot / nodeInput.msg; 1661: QnA bot / nodeInput.request_body.msg; 1661: QnA bot / request_body[0].value.msg |
| 1661: QnA bot | `$(n1661.FullResponse)` | 1661: QnA bot / transition_actions[1].value |
| 1661: QnA bot | `$(n1661.Article)` | 1661: QnA bot / transition_actions[2].value; 1668: Branch / expression; 1668: Branch / outcomes[0].conditions[0].varaible |

### Boundaries and adaptation

Legacy QnA Bot semantics must not be substituted for the AI Agent node. typing_indicator and closechat are filtered back to Receive rather than closing; Goodbye uses Close Task 1669, whose stored media type social differs from chat elsewhere. Timeout/error notifications lead to Close Task 1357; terminal outcomes are attached via parent/event records. A log still references absent n9.evaluate.output. No total-loop bound appears. Form/app/queue bindings and placeholder conversationId require adaptation. Runtime testing is false: no bot turn, task, or message was executed. This internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1487: Error notif / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
Literal node-qualified references name uncaptured producers: n9. Their provenance is not guessed.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-sms-inbound"></a>

## SMS inbound.workflow

Observed 2026-09-09T00:04:57.868Z. [Captured model](../evidence/sample-flows/observed/wxcc-sms-inbound.json); [complete graph summary](sample-flows/summaries/wxcc-sms-inbound.json). Runtime tested: **no**.

SMS Start 2 enters Evaluate 9 and then Resolve Conversation 1097 through numeric outcome 1/success. Resolve created/reopened sends SMS 1186, whose onsuccess enters Queue Task 736; Queued sends SMS 1153. Resolve appended/accepted terminates through End bindings, avoiding a second queue action for an already handled conversation. Queue errors/timeouts attempt Close Task 775. Close failures reach error SMS 984, while its Success terminates. Resolve timeout Branch 1362 closes its Create/Reopen Path and ends its Append Path.

Useful handoffs: Start copies senderNumber, serviceNumber, message, timestamp, transId, and scan metadata from the inbound event. Evaluate constructs a JSON object with messageDetails and scan details, then serializes detailsJson. Resolve consumes `$(transId)` and `$(detailsJson)` with media type social and channel sms; Queue/Close use `$(taskId)` and `$(conversationId)`. Notifications address `$(n2.sms.senderNumber)`. The acknowledgment text distinguishes message resolution from the later queued notification.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure SMS Event | onBegin (`onbegin`) → 9: Evaluate |
| 9: Evaluate | success (`1`) → 1097: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1020: SMS |
| 736: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 775: Close Task; Queued → 1153: Queued |
| 775: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, onauthorizationfail → 984: SMS; Success → End 1458 → Success |
| 984: SMS | No outgoing route captured |
| 1020: SMS | onError (`onerror`) → End 1459 → Error; onPolicyFail (`onpolicyfail`) → End 1460 → Error; onSuccess (`onsuccess`) → End 1461 → Success; onError (`onerror`) → End 1462 → Error; onPolicyFail (`onpolicyfail`) → End 1463 → Error; onSuccess (`onsuccess`) → End 1464 → Success |
| 1097: Resolve Conversation | onInvalidChoice (`oninvalidchoice`), onInvalidData (`oninvaliddata`), onError (`onerror`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1020: SMS; created, reopened → 1186: SMS; onTimeout (`ontimeout`) → 1362: Branch; appended → End 1456 → Success; accepted → End 1457 → Success |
| 1153: Queued | onError (`onerror`) → End 1467 → Error; onPolicyFail (`onpolicyfail`) → End 1468 → Error; onSuccess (`onsuccess`) → End 1469 → Success |
| 1186: SMS | onSuccess (`onsuccess`) → 736: Queue Task; onError (`onerror`) → End 1465 → Error; onPolicyFail (`onpolicyfail`) → End 1466 → Error |
| 1362: Branch | Create/Reopen Path → 775: Close Task; onError (`onerror`) → End 1386 → Error; Append Path → End 1387 → Success; None of the above → End 1388 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure SMS Event | `$(n2.sms.serviceNumber)` | 2: Configure SMS Event / transition_actions[0].value |
| 2: Configure SMS Event | `$(n2.sms.senderNumber)` | 1020: SMS / destination; 1153: Queued / destination; 1186: SMS / destination; 2: Configure SMS Event / transition_actions[1].value; 984: SMS / destination |
| 2: Configure SMS Event | `$(n2.sms.message)` | 2: Configure SMS Event / transition_actions[2].value |
| 2: Configure SMS Event | `$(n2.service.serviceKey)` | 2: Configure SMS Event / transition_actions[3].value |
| 2: Configure SMS Event | `$(n2.sms.timestamp)` | 2: Configure SMS Event / transition_actions[4].value |
| 2: Configure SMS Event | `$(n2.sms.pciInfo.isPCICompliance)` | 2: Configure SMS Event / transition_actions[5].value |
| 2: Configure SMS Event | `$(n2.sms.pciInfo.isPCIValidationDone)` | 2: Configure SMS Event / transition_actions[6].value |
| 2: Configure SMS Event | `$(n2.sms.pciInfo.nonPCIComplianceReason)` | 2: Configure SMS Event / transition_actions[7].value |
| 2: Configure SMS Event | `$(n2.sms.transId)` | 2: Configure SMS Event / transition_actions[10].value |
| 2: Configure SMS Event | `$(n2.sms.securityscaninfo.isSecurityValidationDone)` | 2: Configure SMS Event / transition_actions[11].value |
| 2: Configure SMS Event | `$(n2.sms.securityscaninfo.securityFailedReason)` | 2: Configure SMS Event / transition_actions[12].value |
| 2: Configure SMS Event | `$(n2.sms.securityscaninfo.isSecurityCompliance)` | 2: Configure SMS Event / transition_actions[13].value |
| 2: Configure SMS Event | `$(n2.sms.malwareinfo.isMalwareValidationDone)` | 2: Configure SMS Event / transition_actions[14].value |
| 2: Configure SMS Event | `$(n2.sms.malwareinfo.isMalwareCompliance)` | 2: Configure SMS Event / transition_actions[15].value |
| 2: Configure SMS Event | `$(n2.sms.malwareinfo.malwareFailedReason)` | 2: Configure SMS Event / transition_actions[16].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1097: Resolve Conversation / transition_actions[0].value; 736: Queue Task / extraParamsData.id; 736: Queue Task / nodeInput.id; 736: Queue Task / path_parameters[1].value; 736: Queue Task / request_body[0].value; 775: Close Task / nodeInput.ID; 775: Close Task / nodeInput.Task Id; 775: Close Task / path_parameters[1].value; 775: Close Task / request_body[0].value; 775: Close Task / transition_actions[2].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 736: Queue Task / extraParamsData.conversationid; 736: Queue Task / nodeInput.conversationid; 736: Queue Task / request_body[3].value; 775: Close Task / nodeInput.Conversation ID; 775: Close Task / request_body[2].value |
| 1097: Resolve Conversation | `$(n1097.taskId)` | 775: Close Task / transition_actions[0].value |
| 1097: Resolve Conversation | `$(n1097.transId)` | 1186: SMS / transition_actions[0].value; 775: Close Task / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1020: SMS / message; 984: SMS / message |
| custom variable; writers 2: Configure SMS Event | `$(transId)` | 1097: Resolve Conversation / extraParamsData.trackingId; 1097: Resolve Conversation / extraParamsData.transId; 1097: Resolve Conversation / request_body[0].value; 1097: Resolve Conversation / transition_actions[1].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1097: Resolve Conversation / extraParamsData.details; 1097: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 1362: Branch / expression; 1362: Branch / outcomes[0].conditions[0].varaible; 1362: Branch / outcomes[0].conditions[1].varaible; 1362: Branch / outcomes[1].conditions[0].varaible |

### Boundaries and adaptation

This is the basic event-driven inbound task flow: there is no QnA/AI Agent node or customer-reply Receive loop. SMS 1186 failure/policy outcomes terminate rather than queue, unlike the email sample. conversationId remains a placeholder, and sender/queue bindings are sample-specific. Duplicate End records for notification parents are internal residue. Configured cleanup and acknowledgment messages do not prove execution, routing, delivery, or resolution. Runtime testing is false; the internal canvas model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 984: SMS / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-smsqabotinboundflow"></a>

## SmsQABotInboundFlow.workflow

Observed 2026-09-09T00:03:21.623Z. [Captured model](../evidence/sample-flows/observed/wxcc-smsqabotinboundflow.json); [complete graph summary](sample-flows/summaries/wxcc-smsqabotinboundflow.json). Runtime tested: **no**.

SMS Start 2 → Evaluate 9 → Resolve Conversation 1097 creates the message/task context. Created/reopened sends SMS 1186, then QnA bot 1344. onSuccess sends TextResponse via SMS 1260, obtains a timestamp, and appends the outbound turn at 1266. Branch 1446 closes task 1447 when Article contains Goodbye; otherwise Receive 1268 waits 120 seconds. sms.mo enters Branches 1271/1273: closechat messages return to Receive, while other messages append inbound at 1272 and re-enter the bot. onAgentHandover sends/appends a handoff message, then Queue Task 736; Queued sends notification 1153.

Useful handoffs: The bot request uses `consumer.phone=$(n2.sms.senderNumber)`, correlation_id `$(transid)`, platform sms, and `msg=$(questionForBot)`. Receive filters the original sender, a stored service code, and wildcard keyword; on leave it refreshes questionForBot/message from `$(n1268.receive.message)`. Bot TextResponse comes from `$.generated_msg[0].text`; Article comes from `$.messageStore.top_match_section.first_question`. Queue and Close use taskId/conversationId. Inbound Append uses `$(message)` and `$(timern)`, the timestamp generated after the preceding bot send, despite Receive separately storing its own timestamp.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure SMS Event | onBegin (`onbegin`) → 9: Evaluate |
| 9: Evaluate | success (`1`) → 1097: Resolve Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1020: SMS |
| 736: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 775: Close Task; Queued → 1153: Queued |
| 775: Close Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, onauthorizationfail, Success → 984: SMS |
| 984: SMS | No outgoing route captured |
| 1020: SMS | onError (`onerror`) → End 1561 → Error; onPolicyFail (`onpolicyfail`) → End 1562 → Error; onSuccess (`onsuccess`) → End 1563 → Success; onError (`onerror`) → End 1569 → Error; onPolicyFail (`onpolicyfail`) → End 1570 → Error; onSuccess (`onsuccess`) → End 1571 → Success |
| 1097: Resolve Conversation | onInvalidChoice (`oninvalidchoice`), onInvalidData (`oninvaliddata`), onError (`onerror`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1020: SMS; created, reopened → 1186: SMS; onTimeout (`ontimeout`) → 1302: Branch; appended → End 1538 → Success; accepted → End 1539 → Success |
| 1153: Queued | onError (`onerror`) → End 1566 → Error; onPolicyFail (`onpolicyfail`) → End 1567 → Error; onSuccess (`onsuccess`) → End 1568 → Success |
| 1186: SMS | onSuccess (`onsuccess`) → 1344: QnA bot |
| 1260: Send Bot Response | onSuccess (`onsuccess`) → 1265: Get Current Time |
| 1265: Get Current Time | timern (`1`) → 1266: Append Conversation; onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 775: Close Task |
| 1266: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 775: Close Task; onAppendMessageSuccess → 1446: Branch |
| 1268: Receive | onError (`onerror`), onTimeout (`ontimeout`) → 775: Close Task; sms.mo → 1271: Branch |
| 1271: Branch | None of the above → 1272: Append Conversation; Invalid Messages → 1273: Branch; onError (`onerror`) → 775: Close Task |
| 1272: Append Conversation | onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 775: Close Task; onAppendMessageSuccess → 1344: QnA bot |
| 1273: Branch | None of the above → 1272: Append Conversation; Invalid Messages → 1268: Receive; onError (`onerror`) → 775: Close Task |
| 1283: Connecting to an agent | onSuccess (`onsuccess`) → 1288: Get Current Time; onError (`onerror`) → End 1557 → Error; onPolicyFail (`onpolicyfail`) → End 1558 → Error; onError (`onerror`) → End 1559 → Error; onPolicyFail (`onpolicyfail`) → End 1560 → Error; onError (`onerror`) → End 1564 → Error; onPolicyFail (`onpolicyfail`) → End 1565 → Error |
| 1288: Get Current Time | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 775: Close Task; timern (`1`) → 1289: Append Conversation |
| 1289: Append Conversation | onAppendMessageSuccess → 736: Queue Task; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Failure, onAppendMessageFailure, onTimeout (`ontimeout`), onauthorizationfail → 775: Close Task |
| 1302: Branch | Create/Reopen Path → 775: Close Task; Append Path → End 1304 → Success; None of the above → End 1306 → Error; onError (`onerror`) → End 1309 → Error |
| 1344: QnA bot | onAgentHandover → 1283: Connecting to an agent; onSuccess → 1260: Send Bot Response; onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), onFailure → 775: Close Task |
| 1446: Branch | None of the above → 1268: Receive; onError (`onerror`), Close Bot Conversation → 1447: Close Task |
| 1447: Close Task | onTimeout (`ontimeout`) → End 1448 → Error; Success → End 1450 → Success; onInvalidData (`oninvaliddata`) → End 1453 → Error; onError (`onerror`) → End 1457 → Error; onInvalidChoice (`oninvalidchoice`) → End 1462 → Error; onauthorizationfail → End 1468 → Error; Error → End 1475 → Incomplete |

**Loops in the captured graph:** 1260: Send Bot Response → 1265: Get Current Time → 1266: Append Conversation → 1268: Receive → 1271: Branch → 1272: Append Conversation → 1273: Branch → 1344: QnA bot → 1446: Branch. These are cyclic node groups, not a claimed execution ordering; use the transition table for the actual event route.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure SMS Event | `$(n2.sms.serviceNumber)` | 2: Configure SMS Event / transition_actions[0].value |
| 2: Configure SMS Event | `$(n2.sms.senderNumber)` | 1020: SMS / destination; 1153: Queued / destination; 1186: SMS / destination; 1260: Send Bot Response / destination; 1283: Connecting to an agent / destination; 1344: QnA bot / extraParamsData.consumer.phone; 1344: QnA bot / extraParamsData.request_body.consumer.phone; 1344: QnA bot / extraParamsData.uid; 1344: QnA bot / nodeInput.consumer.phone; 1344: QnA bot / nodeInput.request_body.consumer.phone; 1344: QnA bot / nodeInput.uid; 1344: QnA bot / request_body[0].value.consumer.phone; 2: Configure SMS Event / transition_actions[1].value; 984: SMS / destination |
| 2: Configure SMS Event | `$(n2.sms.message)` | 2: Configure SMS Event / transition_actions[10].value; 2: Configure SMS Event / transition_actions[2].value |
| 2: Configure SMS Event | `$(n2.service.serviceKey)` | 2: Configure SMS Event / transition_actions[3].value |
| 2: Configure SMS Event | `$(n2.sms.timestamp)` | 2: Configure SMS Event / transition_actions[4].value |
| 2: Configure SMS Event | `$(n2.sms.pciInfo.isPCICompliance)` | 2: Configure SMS Event / transition_actions[5].value |
| 2: Configure SMS Event | `$(n2.sms.pciInfo.isPCIValidationDone)` | 2: Configure SMS Event / transition_actions[6].value |
| 2: Configure SMS Event | `$(n2.sms.pciInfo.nonPCIComplianceReason)` | 2: Configure SMS Event / transition_actions[7].value |
| 2: Configure SMS Event | `$(n2.sms.transId)` | 2: Configure SMS Event / transition_actions[11].value |
| 2: Configure SMS Event | `$(n2.sms.securityscaninfo.isSecurityValidationDone)` | 2: Configure SMS Event / transition_actions[12].value |
| 2: Configure SMS Event | `$(n2.sms.securityscaninfo.securityFailedReason)` | 2: Configure SMS Event / transition_actions[13].value |
| 2: Configure SMS Event | `$(n2.sms.securityscaninfo.isSecurityCompliance)` | 2: Configure SMS Event / transition_actions[15].value |
| 2: Configure SMS Event | `$(n2.sms.malwareinfo.isMalwareValidationDone)` | 2: Configure SMS Event / transition_actions[16].value |
| 2: Configure SMS Event | `$(n2.sms.malwareinfo.isMalwareCompliance)` | 2: Configure SMS Event / transition_actions[17].value |
| 2: Configure SMS Event | `$(n2.sms.malwareinfo.malwareFailedReason)` | 2: Configure SMS Event / transition_actions[18].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1447: Close Task / path_parameters[1].value; 1447: Close Task / request_body[0].value; 736: Queue Task / extraParamsData.id; 736: Queue Task / path_parameters[1].value; 736: Queue Task / request_body[0].value; 775: Close Task / nodeInput.ID; 775: Close Task / nodeInput.Task Id; 775: Close Task / path_parameters[1].value; 775: Close Task / request_body[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1266: Append Conversation / extraParamsData.conversationid; 1266: Append Conversation / path_parameters[1].value; 1272: Append Conversation / extraParamsData.conversationid; 1272: Append Conversation / path_parameters[1].value; 1289: Append Conversation / extraParamsData.conversationid; 1289: Append Conversation / path_parameters[1].value; 1447: Close Task / request_body[2].value; 736: Queue Task / extraParamsData.conversationid; 736: Queue Task / request_body[3].value; 775: Close Task / nodeInput.Conversation ID; 775: Close Task / request_body[2].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1020: SMS / message; 984: SMS / message |
| custom variable; writers 2: Configure SMS Event | `$(transId)` | 1097: Resolve Conversation / extraParamsData.trackingId; 1097: Resolve Conversation / extraParamsData.transId; 1097: Resolve Conversation / request_body[0].value |
| External/system/custom value; producer not established here | `$(detailsJson)` | 1097: Resolve Conversation / extraParamsData.details; 1097: Resolve Conversation / request_body[6].value |
| 1097: Resolve Conversation | `$(n1097.transId)` | 1186: SMS / transition_actions[0].value; 1260: Send Bot Response / transition_actions[0].value; 1283: Connecting to an agent / transition_actions[0].value |
| 1344: QnA bot | `$(n1344.TextResponse)` | 1260: Send Bot Response / message; 1266: Append Conversation / extraParamsData.text; 1266: Append Conversation / extraParamsData.textOrResponse; 1266: Append Conversation / request_body[5].value; 1283: Connecting to an agent / message; 1289: Append Conversation / extraParamsData.text; 1289: Append Conversation / extraParamsData.textOrResponse; 1289: Append Conversation / request_body[5].value; 1344: QnA bot / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(timern)` | 1266: Append Conversation / extraParamsData.timestamp; 1266: Append Conversation / request_body[6].value; 1272: Append Conversation / extraParamsData.timestamp; 1272: Append Conversation / request_body[6].value; 1289: Append Conversation / extraParamsData.timestamp; 1289: Append Conversation / request_body[6].value |
| 1268: Receive | `$(n1268.receive.message)` | 1268: Receive / transition_actions[0].value; 1268: Receive / transition_actions[1].value; 1271: Branch / expression; 1271: Branch / outcomes[0].conditions[0].varaible; 1273: Branch / expression; 1273: Branch / outcomes[0].conditions[0].varaible |
| 1268: Receive | `$(n1268.sms.timestamp)` | 1268: Receive / transition_actions[2].value |
| custom variable; writers 1268: Receive, 2: Configure SMS Event | `$(message)` | 1272: Append Conversation / extraParamsData.text; 1272: Append Conversation / extraParamsData.textOrResponse; 1272: Append Conversation / request_body[5].value |
| 1097: Resolve Conversation | `$(n1097.conversationOperation)` | 1302: Branch / expression; 1302: Branch / outcomes[0].conditions[0].varaible; 1302: Branch / outcomes[0].conditions[1].varaible; 1302: Branch / outcomes[1].conditions[0].varaible |
| External/system/custom value; producer not established here | `$(transid)` | 1344: QnA bot / extraParamsData.request_body.correlation_id; 1344: QnA bot / extraParamsData.transid; 1344: QnA bot / nodeInput.request_body.correlation_id; 1344: QnA bot / nodeInput.transid; 1344: QnA bot / request_body[0].value.correlation_id |
| custom variable; writers 1268: Receive, 2: Configure SMS Event | `$(questionForBot)` | 1344: QnA bot / extraParamsData.msg; 1344: QnA bot / extraParamsData.request_body.msg; 1344: QnA bot / nodeInput.msg; 1344: QnA bot / nodeInput.request_body.msg; 1344: QnA bot / request_body[0].value.msg |
| 1344: QnA bot | `$(n1344.FullResponse)` | 1344: QnA bot / transition_actions[1].value |
| 1344: QnA bot | `$(n1344.Article)` | 1344: QnA bot / transition_actions[2].value; 1446: Branch / expression; 1446: Branch / outcomes[0].conditions[0].varaible |

### Boundaries and adaptation

This is legacy QnA Bot, not the current AI Agent node contract. The closechat filter does not close the task; Goodbye or failure/timeout paths do. No total-turn cap is configured. Resolve appended/accepted and Close Task 1447 outcomes terminate through End parent/event bindings. Errors generally attempt Close Task 775; numeric/Boolean scan inputs versus string replace calls remain untested. Resource values and conversationId are sample bindings. No SMS, bot session, or task operation ran; this internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 984: SMS / `onerror` (declared target count 1); 1186: SMS / `onerror` (declared target count 1); 1260: Send Bot Response / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-task-close-flow-with-screen-pop"></a>

## Task Close Flow With Screen Pop.workflow

Observed 2026-09-09T00:03:53.840Z. [Captured model](../evidence/sample-flows/observed/wxcc-task-close-flow-with-screen-pop.json); [complete graph summary](sample-flows/summaries/wxcc-task-close-flow-with-screen-pop.json). Runtime tested: **no**.

WxCC Task v2 Start 2 listens for Task Closed and filters webex.destination to a stored integration value. Its onbegin event, rendered onBegin, leads to Evaluate 836; numeric outcome 1, rendered Success, leads to Screen Pop 720. This responds to closure already reported by WxCC; it does not perform Close Task. Screen Pop success terminates through End 916, bound to parentNode 720 and nodeEvent onScreenPopSuccess; failure/timeout bindings terminate with exitResult 3.

Useful handoffs: Start on-leave actions store `response=$(n2.webex.variables)` and `requestBody=$(n2.webex.RequestBody)`. Evaluate parses both JSON values, reads IssueDescription/IssueType by name from the variable array, reads customerId from requestObj.data.customerId, and obtains customerName from parsed callAssociatedDetails. Screen Pop uses `transid=$(n2.webex.taskId)`, `agentId=$(n2.webex.owner)`, target newBrowserTab, and a demonstration URL. Its nodeInput query carries `customerId=$(CustomerId)`, `customerName=$(CustomerName)`, and operation closed.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: WxCC Task v2 | onBegin (`onbegin`) → 836: Evaluate |
| 720: Screen Pop | onInvalidData (`oninvaliddata`) → End 910 → Error; onError (`onerror`) → End 911 → Error; onInvalidChoice (`oninvalidchoice`) → End 912 → Error; onScreenPopFailure → End 913 → Error; serviceUnavailable → End 914 → Error; onTimeout (`ontimeout`) → End 915 → Error; onScreenPopSuccess → End 916 → Success |
| 836: Evaluate | Success (`1`) → 720: Screen Pop; onInvalidChoice (`oninvalidchoice`) → End 908 → Error; onError (`onerror`) → End 909 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: WxCC Task v2 | `$(n2.webex.variables)` | 2: WxCC Task v2 / transition_actions[0].value |
| 2: WxCC Task v2 | `$(n2.webex.RequestBody)` | 2: WxCC Task v2 / transition_actions[1].value |
| 2: WxCC Task v2 | `$(n2.webex.taskId)` | 720: Screen Pop / extraParamsData.transid; 720: Screen Pop / nodeInput.transid; 720: Screen Pop / request_body[0].value |
| 2: WxCC Task v2 | `$(n2.webex.owner)` | 720: Screen Pop / extraParamsData.agentId; 720: Screen Pop / nodeInput.agentId; 720: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(customerId)` | 720: Screen Pop / extraParamsData.queryParameters.customerId; 720: Screen Pop / request_body[4].value.customerId |
| External/system/custom value; producer not established here | `$(CustomerId)` | 720: Screen Pop / nodeInput.queryParameters.customerId |
| External/system/custom value; producer not established here | `$(CustomerName)` | 720: Screen Pop / nodeInput.queryParameters.customerName |

### Boundaries and adaptation

Stored request_body instead references lowercase `$(customerId)` and omits customerName. Evaluate uses lowercase customerId/customerName while custom variables are capitalized, with no explicit case-bridging session assignment in this capture. Preserve these differences when adapting. No retry, message send, or runtime task event was exercised; embedded isTestExecuted is template data. Destination and screen URL need appropriate bindings. The internal canvas model is evidence, not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-task-close-flow"></a>

## Task Close Flow.workflow

Observed 2026-09-09T00:04:28.883Z. [Captured model](../evidence/sample-flows/observed/wxcc-task-close-flow.json); [complete graph summary](sample-flows/summaries/wxcc-task-close-flow.json). Runtime tested: **no**.

Task Closed triggers WxCC Task v2 Start 2 after its webex.destination condition matches. Start onbegin/onBegin reaches Evaluate 836; numeric outcome 1, rendered Success, reaches Screen Pop 720. Despite the simple filename, this sample does contain Screen Pop. It does not close a task: the close event is its entry condition. End 928 binds Screen Pop onScreenPopSuccess with exitResult 2; failure, unavailable-service, and timeout terminals bind back to node 720 and use 3.

Useful handoffs: Start stores `$(n2.webex.variables)` in response and `$(n2.webex.RequestBody)` in requestBody. Evaluate parses the variable array and request envelope, extracts customerId from data.customerId, and traverses contact, queue, agent, team, and callAssociatedDetails fields. Screen Pop passes `$(n2.webex.taskId)` as transid and `$(n2.webex.owner)` as agentId, with newBrowserTab and operation closed. Its nodeInput query uses `$(CustomerId)`; stored request_body uses `$(customerId)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: WxCC Task v2 | onBegin (`onbegin`) → 836: Evaluate |
| 720: Screen Pop | onInvalidData (`oninvaliddata`) → End 922 → Error; onError (`onerror`) → End 923 → Error; onInvalidChoice (`oninvalidchoice`) → End 924 → Error; onScreenPopFailure → End 925 → Error; serviceUnavailable → End 926 → Error; onTimeout (`ontimeout`) → End 927 → Error; onScreenPopSuccess → End 928 → Success |
| 836: Evaluate | Success (`1`) → 720: Screen Pop; onInvalidChoice (`oninvalidchoice`) → End 931 → Error; onError (`onerror`) → End 932 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: WxCC Task v2 | `$(n2.webex.variables)` | 2: WxCC Task v2 / transition_actions[0].value |
| 2: WxCC Task v2 | `$(n2.webex.RequestBody)` | 2: WxCC Task v2 / transition_actions[1].value |
| 2: WxCC Task v2 | `$(n2.webex.taskId)` | 720: Screen Pop / extraParamsData.transid; 720: Screen Pop / nodeInput.transid; 720: Screen Pop / request_body[0].value |
| 2: WxCC Task v2 | `$(n2.webex.owner)` | 720: Screen Pop / extraParamsData.agentId; 720: Screen Pop / nodeInput.agentId; 720: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(customerId)` | 720: Screen Pop / extraParamsData.queryParameters.customerId; 720: Screen Pop / request_body[4].value.customerId |
| External/system/custom value; producer not established here | `$(CustomerId)` | 720: Screen Pop / nodeInput.queryParameters.customerId |

### Boundaries and adaptation

The capitalization mismatch matters because the script creates lowercase customerId and the declared custom variable is CustomerId; no explicit assignment bridges them here. The demonstration URL and destination filter are sample bindings, not production configuration. This graph has no retry or customer-message stage. No task closure or browser screen pop was executed, regardless of embedded test flags. The internal observed model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-task-modified-flow"></a>

## Task Modified Flow.workflow

Observed 2026-09-09T00:04:32.908Z. [Captured model](../evidence/sample-flows/observed/wxcc-task-modified-flow.json); [complete graph summary](sample-flows/summaries/wxcc-task-modified-flow.json). Runtime tested: **no**.

WxCC Task v2 Start 2 receives Task Modified and filters webex.destination. It enters Evaluate 1630, then Branch 1547 through numeric outcome 1/Success. The branch sends only `$(n2.webex.context)` equal to add or remove through Add/Remove agent to Screen Pop 1326. None of the above terminates at End 1629 with exitResult 2, avoiding a screen pop for other modifications. Screen Pop onScreenPopSuccess terminates at End 1642.

Useful handoffs: Start copies `$(n2.webex.variables)` and `$(n2.webex.RequestBody)` into response/requestBody. Evaluate parses them, extracts IssueDescription/IssueType and standard contact/agent fields, and reads customerId from the event body. Screen Pop consumes `$(n2.webex.ID)` as transid and `$(n2.webex.agentId)` as agentId, targets sameBrowserTab, and marks operation modified. Its nodeInput uses `$(CustomerId)` while request_body uses `$(customerId)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: WxCC Task v2 | onBegin (`onbegin`) → 1630: Evaluate |
| 1326: Screen Pop | onInvalidData (`oninvaliddata`) → End 1635 → Error; onError (`onerror`) → End 1636 → Error; onInvalidChoice (`oninvalidchoice`) → End 1637 → Error; onScreenPopFailure → End 1638 → ; onauthorizationfail → End 1639 → Error; serviceUnavailable → End 1640 → Error; onTimeout (`ontimeout`) → End 1641 → Error; onScreenPopSuccess → End 1642 → Success |
| 1547: Branch | Add/Remove agent → 1326: Screen Pop; onError (`onerror`) → End 1627 → Error; None of the above → End 1629 → Success |
| 1630: Evaluate | Success (`1`) → 1547: Branch; onInvalidChoice (`oninvalidchoice`) → End 1645 → Error; onError (`onerror`) → End 1646 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: WxCC Task v2 | `$(n2.webex.variables)` | 2: WxCC Task v2 / transition_actions[0].value; 2: WxCC Task v2 / transition_actions[2].value |
| 2: WxCC Task v2 | `$(n2.webex.RequestBody)` | 2: WxCC Task v2 / transition_actions[1].value |
| 2: WxCC Task v2 | `$(n2.webex.ID)` | 1326: Screen Pop / extraParamsData.transid; 1326: Screen Pop / nodeInput.transid; 1326: Screen Pop / request_body[0].value |
| 2: WxCC Task v2 | `$(n2.webex.agentId)` | 1326: Screen Pop / extraParamsData.agentId; 1326: Screen Pop / nodeInput.agentId; 1326: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(customerId)` | 1326: Screen Pop / extraParamsData.queryParameters.customerId; 1326: Screen Pop / request_body[4].value.customerId |
| External/system/custom value; producer not established here | `$(CustomerId)` | 1326: Screen Pop / nodeInput.queryParameters.customerId |
| 2: WxCC Task v2 | `$(n2.webex.context)` | 1547: Branch / expression; 1547: Branch / outcomes[0].conditions[0].varaible; 1547: Branch / outcomes[0].conditions[1].varaible |

### Boundaries and adaptation

The script-to-custom-variable capitalization discrepancy is retained; a populated CustomerId is not proven. Most error/timeout pseudo-nodes carry exitResult 3, but the onScreenPopFailure pseudo-node has a blank exitResult and no nodeEvent parameter; its association comes from parentNode/name. There is no retry, task mutation, or notification stage. The integration destination and URL are sample-specific. Runtime testing is false, and this internal canvas model is evidence rather than a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-task-routed-flow"></a>

## Task Routed Flow.workflow

Observed 2026-09-09T00:04:46.978Z. [Captured model](../evidence/sample-flows/observed/wxcc-task-routed-flow.json); [complete graph summary](sample-flows/summaries/wxcc-task-routed-flow.json). Runtime tested: **no**.

WxCC Task v2 Start 2 accepts Task Routed for a configured webex.destination. Start onbegin/onBegin enters Evaluate 1520; its numeric result 1, rendered Success, reaches Screen Pop 1326. Screen Pop onScreenPopSuccess binds to End 1608 with exitResult 2. Evaluate failures and most Screen Pop errors/timeouts terminate with 3 through pseudo-node parent/event associations. This reacts to task assignment; it does not queue or route the task itself.

Useful handoffs: Start stores `response=$(n2.webex.variables)` and `requestBody=$(n2.webex.RequestBody)`. Evaluate parses the variable array and envelope, obtains customerId from data.customerId, and derives customerName from callAssociatedDetails, alongside contact/queue/agent fields. Screen Pop sends `transid=$(n2.webex.ID)` and `agentId=$(n2.webex.agentId)` to a demonstration URL in sameBrowserTab. The nodeInput query uses `CustomerName=$(customerName)` with operation routed; stored request_body instead carries `CustomerId=$(customerId)`.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: WxCC Task v2 | onBegin (`onbegin`) → 1520: Evaluate |
| 1326: Screen Pop | onInvalidData (`oninvaliddata`) → End 1602 → Error; onError (`onerror`) → End 1603 → Error; onInvalidChoice (`oninvalidchoice`) → End 1604 → Error; onScreenPopFailure → End 1605 → ; serviceUnavailable → End 1606 → Error; onTimeout (`ontimeout`) → End 1607 → Error; onScreenPopSuccess → End 1608 → Success |
| 1520: Evaluate | Success (`1`) → 1326: Screen Pop; onInvalidChoice (`oninvalidchoice`) → End 1611 → Error; onError (`onerror`) → End 1612 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: WxCC Task v2 | `$(n2.webex.variables)` | 2: WxCC Task v2 / transition_actions[0].value; 2: WxCC Task v2 / transition_actions[2].value |
| 2: WxCC Task v2 | `$(n2.webex.RequestBody)` | 2: WxCC Task v2 / transition_actions[1].value |
| 2: WxCC Task v2 | `$(n2.webex.ID)` | 1326: Screen Pop / extraParamsData.transid; 1326: Screen Pop / nodeInput.transid; 1326: Screen Pop / request_body[0].value |
| 2: WxCC Task v2 | `$(n2.webex.agentId)` | 1326: Screen Pop / extraParamsData.agentId; 1326: Screen Pop / nodeInput.agentId; 1326: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(customerId)` | 1326: Screen Pop / extraParamsData.queryParameters.CustomerId; 1326: Screen Pop / request_body[4].value.CustomerId |
| External/system/custom value; producer not established here | `$(customerName)` | 1326: Screen Pop / nodeInput.queryParameters.CustomerName |

### Boundaries and adaptation

Those two persisted query configurations are different contracts and were not reconciled by execution. The onScreenPopFailure End has blank exitResult, although its parent/name associates it with node 1326. No retry, customer reply, or downstream workflow exists. Stored integration values and script test flags do not prove a current task event or successful screen pop. Runtime testing is false; the internal model is not a public import schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-task-routed-sample-flow-for-extracting-variables"></a>

## Task Routed Sample Flow For Extracting Variables.workflow

Observed 2026-09-09T00:04:25.187Z. [Captured model](../evidence/sample-flows/observed/wxcc-task-routed-sample-flow-for-extracting-variables.json); [complete graph summary](sample-flows/summaries/wxcc-task-routed-sample-flow-for-extracting-variables.json). Runtime tested: **no**.

Task Routed reaches WxCC Task v2 Start 2 under its webex.destination filter, then Evaluate 1520. Numeric outcome 1, rendered Success, connects to Screen Pop 1326. The central example is extracting task variables established by an inbound flow and carrying them into a desktop action. Screen Pop success terminates at End 1574 through parentNode 1326 and nodeEvent onScreenPopSuccess; most error/timeouts have corresponding End bindings.

Useful handoffs: Start copies `$(n2.webex.variables)` into response and `$(n2.webex.RequestBody)` into requestBody. Evaluate parses response as an array and uses extractVariable(name) to find IssueDescription and IssueType; it also reads customerId from requestObj.data.customerId and assigns custom CustomerId on leave. Screen Pop uses `transid=$(n2.webex.ID)`, `agentId=$(n2.webex.agentId)`, target sameBrowserTab, and query fields `issue=$(IssueDescription)` and `type=$(IssueType)`. The names match the separate LiveChat Set Variable example, but no direct Call Workflow edge joins the samples.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: WxCC Task v2 | onBegin (`onbegin`) → 1520: Evaluate |
| 1326: Screen Pop | onInvalidData (`oninvaliddata`) → End 1568 → Error; onError (`onerror`) → End 1569 → Error; onInvalidChoice (`oninvalidchoice`) → End 1570 → Error; onScreenPopFailure → End 1571 → ; serviceUnavailable → End 1572 → Error; onTimeout (`ontimeout`) → End 1573 → Error; onScreenPopSuccess → End 1574 → Success |
| 1520: Evaluate | Success (`1`) → 1326: Screen Pop; onInvalidChoice (`oninvalidchoice`) → End 1546 → Error; onError (`onerror`) → End 1547 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: WxCC Task v2 | `$(n2.webex.variables)` | 2: WxCC Task v2 / transition_actions[0].value; 2: WxCC Task v2 / transition_actions[2].value |
| 2: WxCC Task v2 | `$(n2.webex.RequestBody)` | 2: WxCC Task v2 / transition_actions[1].value |
| 2: WxCC Task v2 | `$(n2.webex.ID)` | 1326: Screen Pop / extraParamsData.transid; 1326: Screen Pop / nodeInput.transid; 1326: Screen Pop / request_body[0].value |
| 2: WxCC Task v2 | `$(n2.webex.agentId)` | 1326: Screen Pop / extraParamsData.agentId; 1326: Screen Pop / nodeInput.agentId; 1326: Screen Pop / request_body[1].value |
| External/system/custom value; producer not established here | `$(IssueDescription)` | 1326: Screen Pop / extraParamsData.queryParameters.issue; 1326: Screen Pop / nodeInput.queryParameters.issue; 1326: Screen Pop / request_body[4].value.issue |
| External/system/custom value; producer not established here | `$(IssueType)` | 1326: Screen Pop / extraParamsData.queryParameters.type; 1326: Screen Pop / nodeInput.queryParameters.type; 1326: Screen Pop / request_body[4].value.type |
| External/system/custom value; producer not established here | `$(customerId)` | 1520: Evaluate / transition_actions[0].value |

### Boundaries and adaptation

Task variables arrive through WxCC events, not shared local memory between independent flow invocations. The onScreenPopFailure pseudo-node has blank exitResult; preserve that incomplete configuration. The destination filter, URL, and desktop behavior need binding in an adapted design. Existing logs and embedded test flags are observations only. No event or screen pop was executed; the internal model is not an importable public schema.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.

<a id="wxcc-whatsapp-inbound"></a>

## Whatsapp inbound.workflow

Observed 2026-09-09T00:08:50.405Z. [Captured model](../evidence/sample-flows/observed/wxcc-whatsapp-inbound.json); [complete graph summary](sample-flows/summaries/wxcc-whatsapp-inbound.json). Runtime tested: **no**.

WhatsApp Incoming Message 2 enters Evaluate 9, then Resolve Conversation 2016. Resolve created/reopened events send acknowledgment 2018; its success, policy-failure and error edges all continue to Queue Task 1598. `Queued` sends notification 2039. Resolve appended ends successfully; accepted uses a Success terminal with asynchronous checking. Resolve timeout enters Branch 2126: created/reopened operations close Task 1599, appended ends successfully, unmatched/error ends with Error. Queue failures also close Task 1599; its configured outcomes converge on error notification 1938. Evaluate and other Resolve failures use notification 1923.

Useful handoffs: Start copies `$(n2.whatsapp.waId)`, username, message, attachments, caption, timestamp, transId and scan metadata into custom variables. Evaluate strips the transaction suffix, converts the incoming timestamp from seconds to ISO format, and creates `detailsJson` for Resolve's social/whatsapp operation. Queue/Close use unqualified taskId/conversationId; Branch uses `$(conversationOperation)`. Every WhatsApp message targets `$(n2.whatsapp.waId)` and uses a text body. The graph has no Receive wait, reply loop, AI Agent call or fulfillment operation.

### Control progression

| From | Observed event → next node or outcome |
| --- | --- |
| 2: Configure WhatsApp Event | onBegin (`onbegin`) → 9: Evaluate |
| 9: Evaluate | onInvalidChoice (`oninvalidchoice`), onError (`onerror`) → 1923: WhatsApp; success (`1`) → 2016: Resolve Conversation |
| 1598: Queue Task | onTimeout (`ontimeout`), onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, taskFailed, onauthorizationfail → 1599: Close Task; Queued → 2039: WhatsApp |
| 1599: Close Task | Success, onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), Error, onTimeout (`ontimeout`), onauthorizationfail → 1938: WhatsApp |
| 1923: WhatsApp | No outgoing route captured |
| 1938: WhatsApp | onError (`onerror`) → End 2110 → Error; onPolicyFail (`onpolicyfail`) → End 2111 → Error; onSuccess (`onsuccess`) → End 2112 → Success; onError (`onerror`) → End 2170 → Error; onPolicyFail (`onpolicyfail`) → End 2171 → Error; onSuccess (`onsuccess`) → End 2172 → Success |
| 2016: Resolve Conversation | created, reopened → 2018: WhatsApp; onInvalidData (`oninvaliddata`), onError (`onerror`), onInvalidChoice (`oninvalidchoice`), tooManyRequests, serviceUnavailable, error, taskFailed, appendFailed, onauthorizationfail → 1923: WhatsApp; onTimeout (`ontimeout`) → 2126: Branch; appended → End 2184 → Success; accepted → End 2185 → Success |
| 2018: WhatsApp | onSuccess (`onsuccess`), onPolicyFail (`onpolicyfail`), onError (`onerror`) → 1598: Queue Task |
| 2039: WhatsApp | onPolicyFail (`onpolicyfail`) → End 2161 → Error; onError (`onerror`) → End 2162 → Error; onSuccess (`onsuccess`) → End 2163 → Success |
| 2126: Branch | Create/Reopen Path → 1599: Close Task; onError (`onerror`) → End 2158 → Error; Append Path → End 2159 → Success; None of the above → End 2160 → Error |

No control loop was found among the captured operative nodes.

### Exact producer–consumer handoffs

| Producer / observed writer | Reference | Consumers |
| --- | --- | --- |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.attachments)` | 2: Configure WhatsApp Event / transition_actions[0].value; 2: Configure WhatsApp Event / transition_actions[10].value; 2: Configure WhatsApp Event / transition_actions[2].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.message)` | 2: Configure WhatsApp Event / transition_actions[1].value; 2: Configure WhatsApp Event / transition_actions[9].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.pciInfo.nonPCIComplianceReason)` | 2: Configure WhatsApp Event / transition_actions[18].value; 2: Configure WhatsApp Event / transition_actions[3].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.pciInfo.isPCIValidationDone)` | 2: Configure WhatsApp Event / transition_actions[19].value; 2: Configure WhatsApp Event / transition_actions[4].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.username)` | 2: Configure WhatsApp Event / transition_actions[5].value; 2: Configure WhatsApp Event / transition_actions[8].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.appId)` | 2: Configure WhatsApp Event / transition_actions[6].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.waId)` | 1923: WhatsApp / destination; 1938: WhatsApp / destination; 2018: WhatsApp / destination; 2039: WhatsApp / destination; 2: Configure WhatsApp Event / transition_actions[7].value |
| 2: Configure WhatsApp Event | `$(n2.service.serviceKey)` | 2: Configure WhatsApp Event / transition_actions[11].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.timestamp)` | 2: Configure WhatsApp Event / transition_actions[12].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.pciInfo.isAttachmentEnabled)` | 2: Configure WhatsApp Event / transition_actions[13].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.pciInfo.droppedAttachmentCount)` | 2: Configure WhatsApp Event / transition_actions[14].value; 2: Configure WhatsApp Event / transition_actions[20].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.transId)` | 2: Configure WhatsApp Event / transition_actions[15].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.pciInfo.isPCICompliance)` | 2: Configure WhatsApp Event / transition_actions[16].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.caption)` | 2: Configure WhatsApp Event / transition_actions[17].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.securityscaninfo.isSecurityCompliance)` | 2: Configure WhatsApp Event / transition_actions[21].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.securityscaninfo.isSecurityValidationDone)` | 2: Configure WhatsApp Event / transition_actions[22].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.securityscaninfo.securityFailedReason)` | 2: Configure WhatsApp Event / transition_actions[23].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.securityscaninfo.droppedAttachmentCount)` | 2: Configure WhatsApp Event / transition_actions[24].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.malwareinfo.isMalwareValidationDone)` | 2: Configure WhatsApp Event / transition_actions[25].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.malwareinfo.isMalwareCompliance)` | 2: Configure WhatsApp Event / transition_actions[26].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.malwareinfo.malwareFailedReason)` | 2: Configure WhatsApp Event / transition_actions[27].value |
| 2: Configure WhatsApp Event | `$(n2.whatsapp.malwareinfo.droppedAttachmentCount)` | 2: Configure WhatsApp Event / transition_actions[28].value |
| External/system/custom value; producer not established here | `$(WANumber)` | 9: Evaluate / transition_actions[0].value |
| custom variable; writers 2: Configure WhatsApp Event | `$(customerUsername)` | 9: Evaluate / transition_actions[1].value |
| custom variable; writers 2: Configure WhatsApp Event | `$(appid)` | 9: Evaluate / transition_actions[2].value |
| custom variable; writers 2: Configure WhatsApp Event | `$(customerWhatsappId)` | 9: Evaluate / transition_actions[3].value |
| custom variable; writers 2: Configure WhatsApp Event | `$(transId)` | 2016: Resolve Conversation / extraParamsData.trackingId; 2016: Resolve Conversation / extraParamsData.transId; 2016: Resolve Conversation / nodeInput.trackingId; 2016: Resolve Conversation / nodeInput.transId; 2016: Resolve Conversation / request_body[0].value; 2016: Resolve Conversation / transition_actions[1].value; 9: Evaluate / transition_actions[4].value |
| External/system/custom value; producer not established here | `$(taskId)` | 1598: Queue Task / extraParamsData.id; 1598: Queue Task / nodeInput.id; 1598: Queue Task / path_parameters[1].value; 1598: Queue Task / request_body[0].value; 1599: Close Task / nodeInput.ID; 1599: Close Task / nodeInput.Task Id; 1599: Close Task / path_parameters[1].value; 1599: Close Task / request_body[0].value; 2016: Resolve Conversation / transition_actions[0].value |
| External/system/custom value; producer not established here | `$(conversationId)` | 1598: Queue Task / extraParamsData.conversationid; 1598: Queue Task / nodeInput.conversationid; 1598: Queue Task / request_body[3].value; 1599: Close Task / nodeInput.Conversation ID; 1599: Close Task / request_body[2].value |
| External/system/custom value; producer not established here | `$(errorMsg1)` | 1923: WhatsApp / text_message.body; 1938: WhatsApp / text_message.body |
| External/system/custom value; producer not established here | `$(detailsJson)` | 2016: Resolve Conversation / extraParamsData.details; 2016: Resolve Conversation / nodeInput.details; 2016: Resolve Conversation / request_body[6].value |
| External/system/custom value; producer not established here | `$(conversationOperation)` | 2126: Branch / expression; 2126: Branch / outcomes[0].conditions[0].varaible; 2126: Branch / outcomes[0].conditions[1].varaible; 2126: Branch / outcomes[1].conditions[0].varaible |

### Boundaries and adaptation

The script uses appId while Start assigns appid, so case-sensitive binding must be checked when adapting. The initial error sender declares an error event without a captured recovery route. Queue, business-number and authorization bindings are sample-specific; acknowledgments and Success terminals do not establish agent acceptance or message delivery. Internal canvas evidence is not a public import schema. Runtime testing is false: no message, task or conversation was changed.

No explicit cross-page/flow connector node was identified in this capture. This describes the captured model, not uninspected pages or related service flows.
Declared events without a corresponding captured edge or terminal binding: 1923: WhatsApp / `onerror` (declared target count 1).
Duplicate End binding records are retained in JSON; counts represent records, not distinct executions.
The complete summary preserves node parameters, transition assignments, output mappings, terminal outcome IDs and every captured variable-use record. It does not certify authentication, target-system behavior, message delivery, retries or end-to-end success.
