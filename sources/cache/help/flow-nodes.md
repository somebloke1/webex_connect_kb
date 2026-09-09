# Node Palette

Source: https://help.webexconnect.io/docs/flow-nodes
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:42+00:00

A _node_ is a building block for constructing flows. Node is a discrete function that executes within a flow. Nodes encapsulate an action or a decision to form the basis of a flow. Each node performs a specific function, in some cases depending on the outcome, and can decide between two or more possible paths to continue the execution.<br>

You can drag-and-drop the nodes to place them on the flow canvas. When you drag-and-drop a node, the node snaps to the canvas-grid. You can move the node to any empty space on the canvas grid, however, you cannot superimpose one node on another.<br>

You must connect all the nodes, in a logical sequence, using the connectors to form a meaningful flow. Each node has a set of configurable properties and events. Double-click any node to open the configuration window where you can configure the properties and events. Every node accepts input and provides output. Based on your requirements, you also need to configure the events that the node needs to execute.<br>

> 📘 
> 
> Please note that all flow variables are case-sensitive.

Except for the _Start_ node, all nodes have pre-defined edges. You can configure the **End Flow** settings and use a node edge to end the flow.

The nodes are classified into the following categories based on their configurable properties:



| Utilities | Channels | Pre-built Integrations |
| --- | --- | --- |
| [Evaluate](https://help.webexconnect.io/docs/evaluate-node) | [Send SMS](https://help.webexconnect.io/docs/sms-node) | [IMIcampaign Profile Node](https://help.webexconnect.io/docs/campaign-profile-node)  <br>  <br>**Note**: You can see this node only if it has been enabled by the Admin. |
| [Branch](https://help.webexconnect.io/docs/branch-node) | RCS  <br>> _ [RCS Capability Node](https://help.webexconnect.io/docs/rcs-capability-node)  <br>> _ [RCS Message Node](https://help.webexconnect.io/docs/rcs-message-node) | [Create Chat](https://help.webexconnect.io/docs/create-chat-node) |
| [HTTP Request](https://help.webexconnect.io/docs/http-request-node) | [Push](https://help.webexconnect.io/docs/push) | Cisco Webex Contact Center Nodes  <br>  <br>  _ [Create Task](https://help.webexconnect.io/docs/wxcc-create-task)  <br>  _ [Queue Task](https://help.webexconnect.io/docs/wxcc-queue-task)  <br>  _ [Screen Pop](https://help.webexconnect.io/docs/wxcc-screen-pop)  <br>  _ [Routed Notification](https://help.webexconnect.io/docs/wxcc-routed-notification)  <br>  _ [Modify Notification](https://help.webexconnect.io/docs/wxcc-modify-notification)  <br>  _ [Close Task](https://help.webexconnect.io/docs/wxcc-close-task)  <br>  _ [Search Conversation](https://help.webexconnect.io/docs/wxcc-engage-search-conversation)  <br>  _ [Append Conversation](https://help.webexconnect.io/docs/wxcc-engage-append-conversation)  <br>  _ [Create Conversation](https://help.webexconnect.io/docs/wxcc-engage-create-conversation)  <br>  _ [Add Participant](https://help.webexconnect.io/docs/wxcc-engage-add-participant)  <br>  _ [Remove Participant](https://help.webexconnect.io/docs/wxcc-engage-remove-participant)  <br>  _ [Close Conversation](https://help.webexconnect.io/docs/wxcc-engage-close-conversation)  <br>  \* [Update Conversation](https://help.webexconnect.io/docs/wxcc-engage-update-conversation) |
| [Delay](https://help.webexconnect.io/docs/delay-node) | [Live Chat / In-app Messaging](https://help.webexconnect.io/docs/in-app-messaging) | Cisco Contact Center Nodes  <br>  <br>  _ [ECE Login](doc:ece-login)  <br>  _ [Search Customer](doc:search-customer)  <br>  _ [Edit Customer](doc:edit-customer)  <br>  _ [Entrypoint Configuration](doc:entrypoint-configuration)  <br>  _ [Agent Availability](doc:agent-availability)  <br>  _ [Start Conversation](doc:start-conversation)  <br>  _ [Send Message](doc:send-message)  <br>  _ [Process ECE Events](doc:process-ece-events)  <br>  \* [Get File Info](doc:get-file-info)  |
| [Data Parser](https://help.webexconnect.io/docs/data-parser-node) | [Email](https://help.imiconnect.io/docs/email-node) |  |
| [Data Transform](https://help.webexconnect.io/docs/data-transform-node) | [Apple Messages for Business](https://help.imiconnect.io/docs/apple-messages-for-business) |  |
| [Call Workflow](https://help.webexconnect.io/docs/call-workflow-node) | [Messenger](https://help.webexconnect.io/docs/messenger) |  |
| [Page Connector](https://help.webexconnect.io/docs/page-connector-node) | [WhatsApp](https://help.imiconnect.io/docs/whatsapp) |  |
| [Profile](https://help.webexconnect.io/docs/profile-node) |  |  |
| [Generate OTP](https://help.webexconnect.io/docs/generate-otp-node) | [Receive](https://help.webexconnect.io/docs/receive-node) |  |
| [Validate OTP](https://help.webexconnect.io/docs/validate-otp-node) | [Send Voice](https://help.webexconnect.io/docs/send-voice-node) |  |
| [Social Hour](https://help.webexconnect.io/docs/social-hour-check-node) | [Voice Node Group](https://help.webexconnect.io/docs/voice-node-group) |  |
| [Cryptographic Hash](https://help.webexconnect.io/docs/cryptographic-hash-node-configuration) | [Play Node](https://help.webexconnect.io/docs/play-node) |  |
| [Decryption](https://help.webexconnect.io/docs/decryption-node) | [Call User Node](https://help.webexconnect.io/docs/call-user-node) |  |
| [Encryption](https://help.webexconnect.io/docs/encryption-node) | [Record Node](https://help.webexconnect.io/docs/record-node) |  |
|  | [Collect Input Node](https://help.webexconnect.io/docs/collect-input-node) |  |
|  | [IVR Menu Node](https://help.webexconnect.io/docs/ivr-menu-node) |  |
|  | [Call Patch Node](https://help.webexconnect.io/docs/call-patch-node) |  |




> 📘 Note:
> 
> You can now delete authorizations of a pre-built integration from integration as well as from the integration node configuration window. In case, any live flow uses the authorization, you will be alerted about the flows which will get affected.