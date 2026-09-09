# Integrations and contact-center lifecycles

Reviewed 2026-09-08. Select the integration family and installed node version before using field names or templates. WxCC task nodes, CCE task nodes, Engage conversation nodes and standalone Engage routing are different contracts. This chapter concerns **Webex Connect orchestration and digital channels**, not instructions for Webex Contact Center's native voice Flow Designer.

## Choose the integration surface

| Requirement | Starting choice | Verify before implementation |
|---|---|---|
| One external HTTP call | HTTP Request; see [core nodes](04-node-reference.md) | Authentication, status/body contract, timeout, idempotency |
| Reusable REST/SOAP interface or advanced authentication | Custom Node | Tenant entitlement, method/UI schema, response mapping, authorization, certificates |
| Supported packaged system | Prebuilt integration | Enabled integration, node/event version, runtime authorization and inbound-event authorization |
| WxCC digital-agent handoff | WxCC task + Engage conversation lifecycle, or supported Resolve Conversation template | Asset mapping, task/conversation linkage, queue, routed/modified/close event handling |
| Cisco Contact Center Enterprise | CCE task + CCE-compatible Engage flows | Domain, routing script selector, asset-specific event filters |
| Standalone Webex Engage | Standalone conversation/routing nodes | Channel/business identity, team/skill queue and working hours |

The table is a design selection aid. Product-specific behavior follows.

**Custom nodes.** Reusable REST/SOAP integrations are entitlement dependent. REST methods define URL, headers, body, timeouts, static/dynamic fields, response paths and outcomes; SOAP starts from WSDL. Supported authentication includes Basic, Digest, AWS Signature and OAuth 2.0 authorization-code/client-credentials flows. Configure required fields and validation in the node UI. New configurations support TLS 1.2/1.3; certificate application can distinguish API requests from OAuth authorization requests. Throttle settings apply across flows using the integration. The source conflicts on volume-limit code (430 in prose, 431 in its response-code list): confirm actual response before branching on it. [Custom Node Integration](https://help.webexconnect.io/docs/custom-nodes-integration)

**Prebuilt integrations.** Availability requires tenant enablement. Inspect Assets → Integrations for the actual nodes, inbound events, versions and authorization mechanisms. Node and event authorization are separate surfaces. A newer node may use a different authentication scheme while an older scheme still displays pending status. Prefer the installed recommended version after checking its change log and mappings; do not replace a node solely because its name matches. [Prebuilt introduction](https://help.webexconnect.io/docs/pre-built-integrations-introduction)

**Design recommendation: contract worksheet.** For each external operation, record method/endpoint, auth reference, request schema, allowed response statuses, response schema, missing/null behavior, side effects, duplicate key, timeout budget and recovery. Branch on business response content as well as transport status. Never embed an access token in an exported flow example. A timeout on a mutating call is an unknown outcome until reconciled with the receiving system.

## WxCC digital integration: separate the identities

| Identity | Meaning and recommended handling |
|---|---|
| Business asset | The number, mailbox, app, Page or business account the customer contacted; preserve it in lookup/event filters |
| Customer channel identity | Sender address within the channel/business scope; separate it from display name and CRM identity |
| Conversation ID | Engage conversation/transcript handle; persist it across relevant messages |
| Task ID | Contact-center routing/work handle; a reopened conversation can have a new task |
| Flow transaction ID | Execution trace for a particular flow run; do not assume it equals every downstream ID |
| Message/provider ID | Individual send/receive artifact for receipt and duplicate correlation |

This is a design model; select field values from the specific node/event contract below rather than deriving them from these names.

**Authorization.** WxCC task nodes require runtime authorization. Cisco documents a Contact Center license plus Control Hub Full Admin or Contact Center Admin for the authorizing user. Credential/account changes can invalidate integration access. Use a managed dedicated authorization and verify refresh/re-authorization operationally; “Authorized” in configuration is not a successful runtime probe. The task-node family includes create, variable-setting, queue, PIQ/EWT, routed/modified notifications, screen pop and close. [WxCC task integration](https://help.webexconnect.io/docs/wxcc-task-integration-nodes-and-node-authorizations)

**Deployment topology.** Cisco's representative bundle separates channel inbound flows from organization-wide Task Routed, Task Modified and Close Task handlers, with separate Live Chat close-thread handling. An inbound handler searches, appends, creates or reopens as appropriate; new work creates/queues a task. Save immediately after importing a template to preserve Evaluate formatting. Enable attachment support and retain the template's security-scan handling; `securityscaninfo` combines PCI/malware information where enabled. WhatsApp location cannot be appended directly in this documented route; convert coordinates to safe text/map-link form. Do not turn template-internal SDK metadata into a business contract. [WxCC sample-flow configuration](https://help.webexconnect.io/docs/wxcc-flow-configuration-using-sample-templates)

## Select one conversation-resolution architecture

### Simplified Resolve Conversation path

Resolve Conversation consolidates matching, append/create/reopen and task linkage. Its `created`/`reopened` outcomes can proceed to self-service or queueing; `appended` normally finishes that inbound processing; `accepted` awaits asynchronous completion. Live Chat matching uses customer/business/thread context and creates a new conversation after closure; the documented route does not reopen Live Chat. Email prefers reply-header matching, then sender/mailbox/subject; social channels match customer and business addresses. Build the channel-specific Details JSON from the matching template, not a generic message object. The page contains inconsistent field spellings and a misleading “ending” description: its detailed behavior is resolution, not a close command. [Resolve Conversation](https://help.webexconnect.io/docs/wxcc-resolve-conversation)

**Design recommendation.** Choose the currently supported template for your channel and node version. Retain its message/security structures, then add business logic around its explicit outcomes. Do not run an additional manual Create Task or Append Message after the middleware already performed that operation. Test fresh, active, queued and closed conversations independently, including the late reply after closure.

### Explicit search/create/append path

Use this when maintaining a compatible existing template or deliberately owning each step. Do not mix its side effects indiscriminately with the simplified path.

| Operation | Fields/results that matter | Primary reference |
|---|---|---|
| Search Conversation | Channel/business and customer addresses; email also carries subject, recipients and reply context. Results include existence, status, conversation ID; later versions add alias/team/user/API details. | [Search](https://help.webexconnect.io/docs/wxcc-engage-search-conversation) |
| Create Conversation | Channel/customer/message information; asynchronous creation outcomes; preserve the returned conversation linkage from the actual version. | [Create](https://help.webexconnect.io/docs/wxcc-engage-create-conversation) |
| Create Task | Task ID, conversation ID, destination asset, media type/channel, customer identity; email-specific subject/recipients/attachment fields. | [Create Task](https://help.webexconnect.io/docs/wxcc-create-task) |
| Append Conversation | Existing conversation ID, direction, channel-specific message type, content, timestamp and attachment object. | [Append](https://help.webexconnect.io/docs/wxcc-engage-append-conversation) |
| Queue Task | Task/conversation/media context, static queue or dynamic queue ID, routing skills, priority and optional relaxation. | [Queue Task](https://help.webexconnect.io/docs/wxcc-queue-task) |

**Search/create caveat.** The Create Task documentation has conflicting Live Chat customer-ID examples and unusual WhatsApp destination/source-number guidance. These must not be generalized into a universal field map. Use the current official flow template and installed node's description, then verify values in a controlled transaction. Origin/customer address and destination/business address are separate concepts even where a particular UI labels them unexpectedly. [Create Task](https://help.webexconnect.io/docs/wxcc-create-task)

**Queueing.** Static queues expose longest-available-agent or skill routing; dynamic selection takes a Queue ID. Configure skill, condition and value, with optional relaxation. The page documents priorities 1–9 with 1 highest, while describing 10 as the default; do not assume 10 is an explicit selectable priority. Queue-node version 1.3 is recommended there for skill-relaxation fixes. Queue submission is not proof that an agent joined. [Queue Task](https://help.webexconnect.io/docs/wxcc-queue-task)

**Appending.** Agent transcript rendering needs the right schema: email carries addresses, headers, plain/HTML/stripped bodies and attachments; Live Chat distinguishes inbound replies from outbound cards/quick replies and announcements. WhatsApp button/list append cannot use `send.response_interactive` according to the current reference; construct the documented interactive JSON and inbound title/identifier representation instead. Inspect the local [full Append reference](../sources/cache/help/wxcc-engage-append-conversation.md) for exact payload structure. [Append Conversation](https://help.webexconnect.io/docs/wxcc-engage-append-conversation)

**Design recommendation.** A race between two inbound messages can create competing work if lookup/create is treated as an atomic transaction without evidence. Retain stable identifiers, reconcile ambiguous creates, and test simultaneous first messages. Store outbound bot messages in the transcript where required; a successful channel send alone does not prove the agent sees the same history.

## Finish the routed, modified and close paths

| Event/step | Required action and evidence |
|---|---|
| Task routed → Add Participant | Use conversation/media-resource ID and routed-event agent ID. Follow participant success/failure, not merely API request initiation. [Add Participant](https://help.webexconnect.io/docs/wxcc-engage-add-participant) |
| Participant addition result → Routed Notification | Report accepted or rejected routing with task/agent/queue/media context and failure reason/code as applicable. [Routed Notification](https://help.webexconnect.io/docs/wxcc-routed-notification) |
| Task modified | Add/remove the intended participant for transfer/conference, then report the actual result. Modified notification carries task, agent, queue, media-resource ID/type and rejection reason/code. [Modify Notification](https://help.webexconnect.io/docs/wxcc-modify-notification) |
| Conversation closure | Close Conversation targets the conversation/media-resource ID and has distinct completion/failure/timeout outcomes. [Close Conversation](https://help.webexconnect.io/docs/wxcc-engage-close-conversation) |
| Close result → task acknowledgement | Select Close Task Accept, Close Task Reject or direct Close Task on WxCC according to the initiating event and template. Carry task ID, conversation ID, queue/media context, and failure details. [Close Task](https://help.webexconnect.io/docs/wxcc-close-task) |

**Design recommendation.** Ownership changes and closure are state transitions, not a message to the customer. Do not send a successful handoff message before routing/participation evidence supports it. On a partial failure, record which system changed, retain both IDs, and retry/reconcile only the incomplete operation. Define behavior for customer abandonment, agent rejection, transfer failure and closure arriving twice. Avoid infinite close-event loops by distinguishing requested closure from its acknowledgement.

**Operational guardrails.** Cisco documents no implicit retry in prebuilt/HTTP integration calls; implement appropriate bounded logic explicitly. Use client-level services for WxCC integration, reuse authorization configurations, lock stable services and preserve their service keys. Long waits and endless loops can exhaust concurrency. These are specific integration constraints; general release and diagnostic procedures are in [operations](07-testing-and-operations.md). [WxCC best practices](https://help.webexconnect.io/docs/wxcc-best-practices-guidelines)

## Cisco Contact Center Enterprise is a separate route

CCE exposes its own Create Task, Get Task Details and End Task nodes and authorizations. A WxCC Queue Task configuration is not a substitute for CCE's task/routing contract. [CCE node family](https://help.webexconnect.io/docs/cce-integration-nodes-and-node-authorizations)

| CCE create field | Purpose |
|---|---|
| Tracking ID / task ID | Track the request and resulting task using the template's ID construction |
| Domain | Configured reachable Finesse domain |
| Conversation ID | Engage conversation linkage |
| Destination / origin | Business asset contacted versus customer channel identifier; verify channel template |
| Media type/channel | CCE routing media classification |
| Preferred Owner | Preferred agent's CCE Skill Target ID |
| Script Selector | Select the routing script |
| Call/user/extension variables | Explicit routing context; call-variable values have a documented 40-byte limit |

Create Task exposes `location` and `responsePayload`, success/error statuses and a task-already-exists outcome. The page's destination prose and examples conflict; asset-specific examples/template need verification before enactment. [CCE Create Task](https://help.webexconnect.io/docs/cce-create-task)

CCE's representative flow bundle uses Engage as conversation/transcript/attachment storage and has separate inbound, routed, transfer and close handlers. With multiple assets, filter CCE webhook-triggered flows on their asset destination to avoid one event triggering multiple handlers. Preserve the specific channel's business asset association rather than duplicating a broad webhook trigger. [CCE flow configuration](https://help.webexconnect.io/docs/cce-flow-configurations)

End Task carries domain/tracking/task information and applicable call/user/extension variables; use the installed method's outputs/outcomes. **Design recommendation:** follow CCE's actual task state when reconciling an uncertain close and retain a failed close for operational recovery rather than inventing a replacement task. [CCE End Task](https://help.webexconnect.io/docs/cce-end-task)

## Webex Engage standalone

Standalone Engage has a separate palette: conversation search/create/append/update/hold/close/reopen, team working hours, transfer and transcript fetch. Customer and business channel identities are inputs to conversation lookup; Alias ID is an external reference. These nodes route conversations directly in Engage rather than requiring WxCC task APIs. [Standalone palette](https://help.webexconnect.io/docs/node-palette)

Transfer Conversation takes an Engage conversation ID and routes to a team or skill queue. Its success outcome differs between the documented team and skill variants; check the installed variant. Reuse the configured default authorization where supported so a re-authorization does not require editing every flow. [Standalone transfer](https://help.webexconnect.io/docs/transfer-conversation)

**Streaming scope matters.** The standalone streaming page limits support to AMB typing indicators and explicitly does not deliver ordinary incoming messages through that route. [Standalone Engage streams](https://help.webexconnect.io/docs/data-streams-webex-engage) The WxCC-linked Engage page describes a pre-authorized incoming-event stream with channel/asset selection. Do not transplant the standalone restriction or its settings into a linked tenant without checking which integration is installed. [WxCC Engage palette and streams](https://help.webexconnect.io/docs/wxcc-engage-node-palette)

## Acceptance scenarios for an agent handoff

The following is a **design test matrix**, not a claim of tests executed against a tenant:

1. New inbound text creates exactly the intended conversation/task and routes to the expected queue.
2. Second message in active/queued state appends to the existing conversation; it does not create duplicate work.
3. Closed conversation reply follows the channel/version's reopen-or-create behavior.
4. Attachment, attachment-only message and blocked attachment preserve useful agent-visible context without exposing rejected content.
5. Agent addition fails: routing is rejected accurately and the customer receives the defined recovery.
6. Transfer/conference adds/removes the correct participant and acknowledges the actual result.
7. Agent close and customer thread close reconcile both task and conversation; repeated close events are harmless.
8. Token failure, timeout and unknown create result retain identifiers and lead to bounded recovery.
9. Two assets using the same customer identity and simultaneous first messages remain correctly separated.
10. Human agent receives the gathered intent, validated customer context and transcript; automated responders stop according to the intended ownership state.

For an actual build, record run IDs, node versions, outputs and downstream state for each applicable case. A local documentation review cannot establish that an external tenant integration works.
