# Additional public sample walkthroughs

Use [AI Agent and native sample walkthroughs](15-sample-flow-walkthroughs.md) first. This chapter covers the remaining public email/SMS examples and the Contact Center task relationships that they depend on. The [sample inventory](../evidence/sample-flows/sample-inventory.json) is the coverage ledger: its entries distinguish source occurrences, downloaded files, documented relationships, and observed canvas graphs. Similar names across gallery, tutorial and repository versions do not prove identical flows.

These are static source reviews. Arrows below describe source-stated execution order unless explicitly marked **diagram observation** or **engineering interpretation**. They are not imported native edges with verified IDs. ZIP/workflow acquisitions are recorded in the [digital-channel manifest](../evidence/sample-flows/public-wxcc-manifest.json); opaque files have not been decoded locally.

## SMS tutorials: retain the loop and the backend boundary

**Automated SMS, diagram observation:** seven labeled nodes and seven drawn connections form `event → Send Reminder → Receive Customer Response → Check Customer Response`. Confirm and Cancel lead to separate SMS acknowledgments. The visible `Invalid Resp..` branch leads to an invalid-response SMS whose `onSuccess` connection returns to Receive. The article's trigger requires `msisdn` and `appointment_time`; `cust_name` is optional. Destination is `$(msisdn)`. The screenshot has End flags on other outcomes; their truncated labels do not establish full outcome names. No appointment-system update is drawn. The machine-readable [diagram mapping](../evidence/sample-flows/automated-sms-diagram.json) preserves this distinction. [Automated SMS tutorial](https://help.webexconnect.io/docs/sending-automated-sms)

**Engineering interpretation:** the back edge is essential: a correction prompt is useful only if a subsequent response is consumed. Add a business-defined retry limit when adapting the pattern. A confirmation SMS alone is not evidence that a booking was changed. The separate six-node reminder screenshot in chapter 15 omits this retry branch; do not merge the images into one purported native graph.

**Developer appointment tutorial:** webhook `Phone/Name/Appt` → SMS → Receive (600 seconds) → Branch on `$(n11.receive.message)`, A/B → corresponding HTTP POST carrying original fields plus `Status=Confirmed/Cancelled` → SMS outcomes. The HTTP destination is a demonstration request bin, not an appointment API. [Cisco first-flow tutorial](https://developer.webex.com/blog/build-your-first-webex-connect-flow-a-step-by-step-guide)

**Engineering interpretation:** preserve the causal order when replacing the bin with a real service: validate the response before claiming the appointment changed. Node IDs in tutorial expressions belong to that sample. Select the current node's output when recreating it.

## Email attachment notification: two branches rejoin the main journey

**Documented:** `EmailAttachmentDropNotification` inserts a Parse Variables decision before Resolve Conversation. It derives `droppedAttachmentNames` from `securityNonComplianceReasonObject.attachments`, classifies the reason, and sets `droppedAttachmentNotificationMessage`. The `attachmentsDropped` outcome sends a separate email; both that Email node's success and failure paths rejoin Resolve Conversation. `noAttachmentsDropped` bypasses the notification and continues. Custom text variables include `sensitiveOrMaliciousContentFoundErrorMessage` and `errorProcessingAttachmentsMessage`. [Attachment-drop sample README][attachments]

**Engineering interpretation:** notification is a side branch of the inbound conversation, not a replacement for it. Keep both rejoin edges: otherwise an attempted warning could strand the incoming customer request. Do not pass a dropped attachment back downstream merely to complete the sample. Native IDs, all failure outcomes and the complete downstream conversation graph remain unverified from this README.

## Email priority: compute before Queue Task

**Documented:** `EmailInboundSampleFlowWithContactPriority` evaluates sender-based custom high/low-priority identifiers and supplies the result to Queue Task's Contact Priority. Priority 1 is highest, 9 lowest; empty or out-of-range values fall back to 10. This priority is set when queuing, not afterward. [Contact-priority sample README][priority]

**Engineering interpretation:** this sample teaches an ordering constraint: `inbound identity → priority decision → Queue Task`. Put the classification upstream of the external queue operation, then preserve the normal conversation lifecycle. Domain or sender-string matching is example policy, not authenticated customer entitlement. Exact downstream edges are not supplied in the README.

## Legacy bot samples: preserve state around the bot loop

**Documented legacy FBM loop:** inbound message → Search Conversation. Active/queued/on-hold conversations append the message. A missing conversation creates Conversation and Task; a closed conversation reopens and appends. The bot receives `messagetext`. Its fulfillment branch parses `taskbot.entities` and calls CRM over HTTP. Bot response → channel send → Append Conversation → Receive → update `messagetext` → append → bot. Receive timeout closes task/conversation; bot handover queues the task. The Livechat variant inserts a pre-chat Form/Receive before conversation creation. [Q&A/Task Bot walkthrough](https://help.webexconnect.io/docs/wxcc-flows-with-qnabot-nodes)

**Documented repository variants:** `SmsQABotInboundFlow` requires an SMS number and Q&A bot/imibot integration; `LiveChatQABotInboundFlow` requires the corresponding chat asset and bot. `FacebookTaskBotInboundFlow` optionally uses sheet2api for customer lookup/addition. Its documented insertion between Resolve Conversation and Task Bot is HTTP Request → Branch → Data Parser. The README does not establish every edge in the SMS or Livechat archive. [Bot-flow README][bots]

**Engineering interpretation:** this is a historical conversation/transcript pattern. Reuse its responsibilities—state resolution, transcript append, response wait, handover—but map each to the current AI Agent contract in chapter 13. Do not translate `taskbot.entities` into an invented current AI Agent variable. The misleadingly titled [AI Agent Node page](https://help.webexconnect.io/docs/configuring-flows-with-ai-agent-node) describes this same older loop; it is a separate source occurrence, not a fourth modern AI template.

## Variables across separate flows: event correlation, not a canvas wire

**Documented pair:** `LiveChatInboundSampleFlowWithSetVariable` collects `IssueDescription/IssueType` in a pre-chat form and invokes Set Variable with Set Flow Variable. The values become task context visible/editable in the desktop. `Task Routed Sample Flow For Extracting Variables` receives the later task event and uses an Evaluate extraction helper to recover context. Set Global Variable is a separate method requiring an existing global variable. [Set Variable samples README][variables]

**Engineering interpretation:** the shared task carries the relationship between these two graphs. A local variable in the inbound flow is not automatically a local variable in the routed flow. Review the setter's name/type, the event's context container, and the extractor's output together. This cross-channel technique can support email/SMS handover; the supplied inlet happens to be Livechat.

**Documented screen-pop variant:** `Task Close Flow With Screen Pop` starts on Task Closed. A transition maps `webex.variables` to `response`; Evaluate extracts `customerId`; Screen Pop builds query parameters with `customerId` and `operation=close`. Another documented approach first adds the customer variable with Set Variable in the inbound flow and extracts it later. [Screen Pop sample README][screenpop]

**Engineering interpretation:** this is an event-triggered companion, not an SMS/email sender. Replacing the demonstration URL requires an application contract for the parameter values and encoding. The close event is the causal trigger; a similarly named local variable alone cannot connect the two flows.

## Remaining current collection: surveys, queue estimates and channel variants

**Documented survey pair:** `FacebookCloseWithWxmFlow` and `LiveChatCloseWithWxmFlow` depend on the inbound Resolve Conversation setting that overrides default contact-close handling. Livechat first stores thread/user context with Set Variable; its close flow extracts that context. WXM creates a questionnaire survey token, the channel node sends its `surveyURL`, and Append Conversation records the same message/link. The Livechat sender also binds Destination to the extracted user and ThreadID to the extracted thread. [Survey samples README][surveys]

**Engineering interpretation:** the close workflow needs a preserved addressable conversation long enough to deliver the survey. Review the inbound override and the later close graph as a pair. Do not add a second close handler merely because the sample archive exists.

**Documented queue-estimate sample:** `LiveChatInboundSampleFlowWithSetVariablePIQAndEWT` uses pre-chat issue type/description, Queue Task, then PIQ and EWT with method Fetch Position in Queue. The example supplies `$(queue)` for QueueID and sends `positionInQueue`/`estimatedWaitTime`; EWT is milliseconds. A directly assigned contact can produce PIQ `-1`, for which the README suggests suppressing the display through a branch. [PIQ/EWT sample README][piq]

**Engineering interpretation:** this adds a post-queue lookup and a customer response, not an independent estimate generated before queuing. Match the task's actual queue, format the time unit for the channel, and keep an unavailable estimate separate from a promise of immediate service.

**Documented media variants:** the collection also has Facebook, WhatsApp, Apple and Livechat entry/close variants. Livechat Form → Receive maps form Name/Email into `customerName/customerEmail`. Livechat close passes Search Conversation's AliasId into Close Task. [Media-specific templates README][media]

All 33 current v3.5 archives are acquired, imported for static inspection, and individually captured, including the Apple rich-message and proactive-chat variants that have no separate folder README. Their precise topology comes from the linked observed graph summaries; an archive name alone is not a walkthrough. Older repository releases are retained as version context rather than silently substituted for the current collection.

## v3.5 SMS/email templates and their optional event companions

**Documented media contracts:** `SMS inbound` starts for incoming messages to its number; `EmailInboundFlow` starts for incoming mail to its asset. Both require queue selection and correct asset variables; Email uses `bizemailid`. Resolve Conversation's FlowID must match the imported flow. The email template accommodates absent subject/sender name and plain text. The README establishes these configuration dependencies, not a complete edge list. [Media-specific templates README][media]

**Documented v3.5 event contracts:** default participant/close handling exists from v3.0; custom event flows are optional. All three map `webex.variables → response` and `webex.RequestBody → requestBody`, then support Evaluate extraction and custom actions. Task Routed runs after acceptance; Task Modified responds to transfer/conference and branches on `webex.context` add/remove; Task Closed follows contact end. Examples use Screen Pop or HTTP. `webex.mediaChannel`/`webex.destination` conditions isolate the intended channels/assets. [Event-handling templates README][events]

**Engineering interpretation:** the media flow and event companions form a distributed journey. A queued task later causes routing/modified/closed events; these are not direct node edges. Reconcile the imported version before adding companions, because duplicate generations can repeat side effects. The older [WXCC sample page](https://help.webexconnect.io/docs/wxcc-flow-configuration-using-sample-templates) lists eight names despite saying seven; its inventory is retained separately rather than treated as the v3.5 archive schema. See chapter 6 for that generation's inbound/task lifecycle.

## CCE representative bundle: separate its event semantics

The table reviews all 15 names. Arrows are compact source-described stages, not literal native edges or exhaustive branches.

| Sample | Principal relationship |
|---|---|
| SMS Inbound Flow | resolve → choices → create task |
| Email Inbound Flow | scan → task → persist ID |
| Live Chat Inbound Flow | form → ScriptSelector → task |
| Live Chat Customer Close | active: append; queued: end task |
| Live Chat with WebCallback Flow | cancel chat → request callback |
| WebCallback CLOSED | media-switch-aware closure notification |
| Facebook Inbound Flow | choices → ScriptSelector → task |
| WhatsApp Inbound Flow | choices → ScriptSelector → task |
| AppleMessages_Inbound_Flow | name form → choices → task |
| AppleMessages_CustomerClose | active: append; queued: end task |
| CREATED Flow | request acceptance → notify |
| QUEUED Flow | available EWT → notify |
| ROUTED Flow | extract conversation → add participant |
| CLOSED Flow | disposition → closure notification |
| TRANSFERRED Flow | remove participant → recreate same taskID |

The AMB close trigger descriptions conflict: account blocking versus browser closure. Native verification remains pending. [CCE representative flows](https://help.webexconnect.io/docs/cce-flow-configurations)

**Engineering interpretation:** retain CCE as a separate integration family. Its task-creation acceptance is not the same event as agent assignment. A transfer is continuity of the existing task, so accidentally creating an unrelated ID would lose that continuity. The inventory includes all 15 bundle names; email/SMS priority is a retrieval tag, not an exclusion. Public HTTP acquisition returned 403. A browser follow-up loaded the release listing, but Download displayed a Cisco.com login and service-contract requirement. The bundle's native IDs and edges remain unavailable. This is a documented partial review, not an imported graph review; the [acquisition record](../evidence/sample-flows/cce-acquisition-status.json) preserves the limitation.

## Reading coverage correctly

The inventory's scope is the observed tenant gallery, complete current linked sample collections, and samples in the captured official help/Studio corpus, not every Cisco flow example ever published. Other-channel entries remain included; message templates are distinguished from executable flow samples. Public repository occurrences are version-specific; neither matching names nor an acquired ZIP proves equivalence to the tenant gallery. Treat `documented_partial_contract` as useful evidence with a named gap, not as a completed native graph review.

For a future adaptation, read the relevant sample's graph summary and these source contracts together. Track trigger payload → parsed or assigned variable → node input → external operation → returned or sent result. Enumerate actual loops, rejoin edges and terminal outcomes; configuration evidence cannot establish runtime success.

[attachments]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Attachment%20Drop%20Notification%20to%20Customer/README.md
[priority]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Usage%20of%20Contact%20Priority%20In%20Flows/README.md
[bots]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Bot%20Flows/README.md
[variables]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Usage%20of%20Set%20Variable%20In%20Flows/README.md
[screenpop]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Usage%20of%20Screen%20Pop%20in%20Flows/README.md
[media]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Template/Media%20Specific%20Workflows/README.md
[events]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Template/Event%20Handling%20Workflows/README.md
[surveys]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Usage%20Of%20Surveys%20in%20Flows/README.md
[piq]: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/ef668084a137c251f81ae3aa38d1f4e06b4e5573/Webex%20Connect%20Flows/v3.5/Sample/Usage%20of%20PIQ%20And%20EWT%20In%20Flows/README.md
