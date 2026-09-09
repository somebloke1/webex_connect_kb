# Start Node

Source: https://help.webexconnect.io/docs/start-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:51+00:00

The _Start_ node is configured to trigger a flow using a channel, integration, webhook, or a custom event. This node allows you to configure the flow trigger in the context of the standard flow configuration. Further, the data from the trigger is available as node-level variables for use in the other flow nodes. 



![Start Node](https://files.readme.io/39e3a51-Start.jpg)




While creating a [new flow](https://help.webexconnect.io/docs/flows-introduction#section-creating-a-flow), you are prompted to configure the start node. You can choose either to configure or skip to do it later. Select a [trigger](https://help.webexconnect.io/docs/rules#section-triggers) and configure the details. Click the close icon at the upper right corner of the page to skip the trigger configuration.



![Trigger Category](https://files.readme.io/1543235-1.jpeg)




## Triggering a Flow on various Channel Events

> ❗️ 
> 
> The Instagram as a channel is deprecated.



| Channel | Possible Events |
| --- | --- |
| SMS | Mobile Originated - MO (Allows you to trigger the flow on an incoming SMS message)  <br>On Link Click  <br>  <br>Refer ['Conditional Trigger in SMS'](https://help.imiconnect.io/docs/start-node#section-conditional-trigger-in-sms) section if you want to use the 'Trigger only when there are no live sessions option'. |
| Voice | Inbound Call  <br>Missed Call  <br>  <br>**Note:** Webex Connect offers the ability to trigger the same flow for incoming calls received on more than one phone number by using a routing number option. The mapping of the routing number with the set of phone numbers for dialing is to be configured by the Ops team. Reach out to [Ops team](mailto:operations@imimobile.com) if you want to use this feature.\_  <br>  <br>Currently, the routing number feature is supported in the USA and Canada only. |
| MMS | Mobile Originated - MO (Allows you to trigger the flow on an incoming MMS message) |
| Messenger | Incoming Message  <br>On Link Click  <br>Postback |
| Instagram (Deprecated) | Incoming Message - This event occurs every time a user sends a text message with or without attachments to your Instagram account.  <br>  <br>Postback - This event is triggered when user clicks postback type button.  <br>  <br>Message Deleted - This event occurs every time a user sends a delete message to your Instagram account. |
| WhatsApp | Incoming Message - details of the sender ID and name are displayed. The whatsapp.username output variable contains the sender's user name.  <br>  <br>Postback - Postback event captures the payload received when a customer clicks on  a quick reply button within an interactive template  <br>  <br>List Message - This event occurs every time a user selects one of the List Message options  <br>Reply Buttons  Message - This event occurs every time a user selects one of the Reply Buttons  options |
| Mobile & Web App | Custom Event  <br>  <br>Incoming Message_ - \_inappmessaging.appid_ output variable captures the app ID corresponding to the incoming event  <br>  <br>On Thread Closed - this event can be used to trigger a workflow in cases where an agent has resolved a client query and marked the conversation as closed, or if a customer has abandoned a chat and the chat is marked as closed due to it being timed out. The reasonForThreadClosure captures the reason for closing the thread.  <br>  <br>OnPostback - this event is triggered when the user clicks postback type button  <br>  <br>Subscribe - this event is triggered when the user clicks re-subscribe button  <br>  <br>Unsubscribe - this event is triggered when the user clicks unsubscribe link  <br>  <br>Typing Indicator - This event is triggered when a user starts or stops typing in a Live Chat or In-App Messaging conversation. |
| Email | Incoming Message  <br>Subscribe  <br>Unsubscribe  <br>The platform will not trigger or resume a flow, nor trigger a rule or an outbound webhook notification for incoming emails where Sender Email ID is same as the Recipient Email ID. However, details of such incoming emails will be available within Export Logs. |
| Apple Messages for Business | Conversation Closed  <br>Incoming Message  <br>Interactive Message: Invitation Response  <br>Interactive Message: Classical Authentication  <br>Interactive Message: Form Response  <br>Interactive Message: iMessage App Response  <br>Interactive Message: List Picker Or Time Picker  <br>Interactive Message: New Authentication  <br>Interactive Message: Payment  <br>Interactive Message: Quick Replies (A flow is triggered when a Quick Reply message is received from a customer.)  <br>Typing Indicator |
| RCS | Incoming Attachment  <br>Incoming Message  <br>Location Response  <br>Postback  <br>Unsubscribe  <br>Subscribe |




## Flow Triggers for Integrations



| Integration | Possible Events |
| --- | --- |
| CCSP (Deprecated) | Agent Chat Initiated  <br>Chat Closed  <br>Chat Idle  <br>Chat Opened  <br>Chat Picked  <br>Chat Reopened  <br>Chat Transferred  <br>Custom Event  <br>Incoming Message |
| BOT (Deprecated) | Custom Event  <br>Handover  <br>Milestone Reached  <br>Notify  <br>Unhandled Message |
| AI Agent | Trigger from AI Agent to initiate flow |




## Triggering a Flow using Custom Event API or Inbound Webooks



| Custom Trigger | Possible Events |
| --- | --- |
| Webhook | Select an existing webhook  <br>Create a new webhook event |
| Custom event | Select an existing event  <br>Create a new event |




## Triggering a Flow on Apple Messages for Business Invitation Response

You can configure the Start node to trigger a flow when a customer responds to an Apple Messages for Business invitation message. The **Interactive Message: Invitation Response** event represents the first inbound response that converts an invitation into a standard Apple Messages for Business conversation.

To configure an invitation response trigger:

1. Double-click the **Start** node.
2. Select **Apple Messages for Business** as the trigger category.
3. Select **Interactive Message: Invitation Response** as the event.
4. Select the required Apple Messages for Business asset.
5. Optionally, add trigger conditions.
6. Click **Save**.

When the first response to an invitation is received, Webex Connect resolves the invitation context and triggers the flow with the invitation response variables.

### Trigger Conditions for Invitation Response

You can configure trigger conditions for invitation responses using invitation-specific variables. The supported operators depend on the variable type.

| Variable                 | Description                                                                | Supported Operators                                      |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| `abc.msisdn`             | Customer mobile number used for the invitation.                            | equals, notequals, contains, startswith, endswith, regex |
| `abc.invitationAccepted` | Boolean value that indicates whether the customer accepted the invitation. | equals, notequals                                        |
| `abc.requestIdentifier`  | Identifier used to correlate the invitation request and response.          | equals, notequals, contains, startswith, endswith, regex |

### Output Variables

The following output variables are available for Apple Messages for Business invitation response triggers:

| Output Variable          | Description                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| `abc.abcUserId`          | Resolved Apple Messages for Business user ID. Use this value for subsequent standard AMB messages. |
| `abc.msisdn`             | Customer mobile number used for the invitation, when available.                                    |
| `abc.invitationAccepted` | `true` if the customer selected **Yes**. `false` if the customer selected **No**.                  |
| `abc.invitationResponse` | Full invitation response payload received for the event.                                           |
| `abc.requestIdentifier`  | Request identifier associated with the invitation response.                                        |
| `abc.type`               | Event type received from Apple Messages for Business.                                              |
| `abc.timestamp`          | Timestamp when the event was received.                                                             |
| `abc.locale`             | Locale received in the invitation response, when available.                                        |
| `abc.transId`            | Webex Connect transaction ID.                                                                      |
| `service.serviceKey`     | Service key for the service in which the flow is triggered.                                        |

## Trigger Conditions in Start Node

The platform allows selective triggering of the flow only when the conditions set on the trigger event are fully met. The list of variables on which a condition can be set is dependent on the trigger event. For example, conditions can be set on the inbound message or the sender number for an MMS trigger with an inbound message.

Different conditions on variables can be set using the AND/OR operators. When AND is part of the condition, that part of the condition must be true to qualify the condition. When OR is used, the statement is executed if any one of the conditions qualifies.



![Inbound SMS with a condition on the text message set as trigger to invoke the flow](https://files.readme.io/d8259a0-1.png)




One of the several conditional operators that can be used to set conditions are listed below:

- Equals
- Not equals
- In
- Not in
- Contains
- Greater than
- Less than
- Greater than equal to
- Less than equal to
- Equals ignore-case
- Between
- Starts with
- Ends with

## Configure a Custom Event in Start Node

To configure a custom event:

1. Create a flow.
2. Select **Custom Event** as the trigger. Or, you can also double-click the _Start_ node and select the trigger as Custom Event.
3. **Select an existing event** or **Create a new event** based on your requirement. Enter a suitable name and configure the required variables. Provide a suitable name for the new event.

While configuring custom events within the Start Node:

- A pre-selected read-only checkbox is visible on the screen to highlight that it is mandatory to pass service authentication credentials when using Custom Event v1



![Custom Event Configuration](https://files.readme.io/7506a31-2.jpeg)




- The sample payload is dynamically generated for API request body based on the configured parameters. The event id i.e., `evtid` for the configured custom event is generated once you save the configuration.



![Dynamically Generated Sample Payload](https://files.readme.io/1e1cef5-json-body-in-custom-event.png)




You can start using the custom events in the flows. When you use the custom event node in a flow, the event URL is auto-populated and authentication is mandated.

## Conditional Trigger in SMS

Webex Connect allows you to conditionally trigger a flow on receiving an incoming SMS message only if the configured conditions are met. Here's how you can use this feature:

1. Double-click the Start node and select 'SMS - Mobile Originated - MO' as the flow trigger.
2. Provide the required details like SMS event, Incoming Number, and Keyword.



![Conditional Trigger](https://files.readme.io/f3afd70-Start_Node2.jpg)




When the **Trigger only when there are no live sessions checkbox** is enabled, the flow will be triggered only if no Receive node is waiting with a matching keyword and incoming number.

For example, let us suppose there are two flows Flow 1 and Flow 2:

Flow 1: The Start node in Flow 1 is selected as SMS  and the keyword configured in the Start node is 'Help'. The next node is the Receive node with a (anything) keyword.  
Flow 2: The Start node is Flow 2 is selected as SMS and the keyword configured in the Start node is (anything).

- If Flow 1 and Flow 2 are in the same service -  
  When there is an incoming message with the Help, Flow 1 is triggered. With the Help keyword, only the matching flow gets triggered (i.e., Flow 1). We have a Receive node in Flow 1, Flow 1 is waiting at the Receive node. Now, if the next message from the user is 'I need help with a laptop’ then
  - Scenario 1 - Checkbox is not enabled in Flow 2 and Flow 2 is in the same service as Flow 1.  
    The second message 'I need help with laptop' will trigger Flow 2 Start node and Flow 1 Receive node times out.
  - Scenario 2 - Checkbox is enabled in Flow 2 and  Flow 2 is in the same service as Flow 1.  
    The second message 'I need help with a laptop' will resume only the Flow 1 Receive node.
- If Flow 1 and Flow 2 are in different services -  
  When there is an incoming message with the Help keyword, Flow 1 is triggered. We have a Receive node in Flow 1, Flow 1 is waiting at the Receive node. Now, if the next message from the user is 'I need help with a laptop’ then
  - Scenario 1 - Checkbox is not enabled in Flow 2 and Flow 2 (with keyword) is in a different service from Flow 1.  
    The second message 'I need help with laptop' will trigger the Flow 2 Start node and Flow 1 Receive node, and both get resumed.
  - Scenario 2 - Checkbox is enabled in Flow 2 and if Flow 2 is in a different service as Flow 1.  
    The second message 'I need help with a laptop' will resume only the Flow 1 Receive node.

**Illustration**

Let us look at an illustration to understand this clearly.

| Service 1                                                                                                    | Service 2                                                                                                                                                                                                                        |
| :----------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flow 1 - Start node configured with Help keyword followed by a Receive node with "\*" as the keyword.        | Flow 5 – Start node configured with "\*" as the keyword followed by a Receive node with "\*"  as the keyword. You need to disable Flow 3 to enable this flow since Flow 5 is in a different service, you need to disable Flow 3. |
| Flow 2 - Start node configured with Help keyword followed by a Send SMS or any other node.                   | Flow 6 – Start node keyword configured with Balance keyword followed by a Receive node with "\*" as keyword.                                                                                                                     |
| Flow 3 - Start node configured with "\*" as the keyword followed by a Receive node with "\*" as the keyword. |                                                                                                                                                                                                                                  |
| Flow 4 - Start node configured with Loan keyword followed by a Receive node with "\*" as keyword.            |                                                                                                                                                                                                                                  |

The behavior of the flows is illustrated in the following table:



| Conditions (Trigger message and receive) | Checkbox status in different flows | Behavior |
| --- | --- | --- |
|   _ Message 1 – Help  <br>  _ Message 2 - Loan  |   _ Enabled for Flow 1  <br>  _ Disabled for Flow 2  <br>  _ Enabled for Flow 3  <br>  _ Enabled for Flow 4  <br>  _ NA for Flow 5  <br>  _ Enabled/Disabled for Flow 6  |   _ Message 1 triggers Flow 1 and Flow 2  <br>  _ Message 2 will be received by Flow 1 and Flow 2 receive node  |
| _ Message 1 – Help  <br>  _ Message 2 - Loan |   _ Enabled for Flow 1  <br>  _ Disabled for Flow 2  <br>  _ Enabled for Flow 3  <br>  _ Disabled for Flow 4  <br>  _ NA for Flow 5  <br>  _ Enabled/Disabled for Flow 6  |   _ Flow 1 and Flow 2 get triggered when Help is sent  <br>  _ Message 2 triggers only Flow 4 and does not trigger Flow 3.  |
|   _ Message 1 – Total  <br>  _ Message 2 - Loan  |   _ Enabled for Flow 1  <br>  _ Disabled for Flow 2  <br>  _ Disabled for Flow 3  <br>  _ Disabled for Flow 4  <br>  _ NA for Flow 5  <br>  _ Enabled/Disabled for Flow 6  |   _ Message 1 triggers Flow 3  <br>  _ Message 2 triggers Flow 4 as the checkbox is disabled and will be received by Flow 3 Receive node  |
|   _ Message 1 – Total  <br>  _ Message 2 - Loan  |   _ Enabled for Flow 1  <br>  _ Disabled for Flow 2  <br>  _ NA for Flow 3  <br>  _ Disabled for Flow 4  <br>  _ Enabled for Flow 5  <br>  _ Enabled/Disabled for Flow 6  |   _ Message 1 triggers Flow 5  <br>  _ Message 2 triggers Flow 4 as the checkbox is disabled and will be received by Flow 5 Receive node  |
|   _ Message 1 – Total  <br>  _ Message 2 - Balance  |   _ Enabled for Flow 1  <br>  _ Disabled for Flow 2  <br>  _ NA for Flow 3  <br>  _ Disabled for Flow 4  <br>  _ Enabled for Flow 5  <br>  _ Disabled for Flow 6  |   _ Message 1 triggers Flow 5  <br>  _ Message 2 triggers Flow 6 as the checkbox is disabled and will be received by Flow 5 Receive node  |
|   _ Message 1 – Balance  <br>  _ Message 2 - Loan  |   _ Enabled for Flow 1  <br>  _ Disabled for Flow 2  <br>  _ Disabled for Flow 3  <br>  _ Disabled for Flow 4  <br>  _ NA for Flow 5  <br>  _ Disabled for Flow 6  |   _ Message 1 triggers Flow 6  <br>  _ Message 2 triggers Flow 3 and will be received by Flow 6 Receive node  |




> 📘 Output Variables
> 
> Please refer to [Output Variables](https://help.imiconnect.io/docs/receive#output-variables) in Receive Node page to understand the details of Output Variables available for various channel events.

## Flow Trigger Behaviour in Digital Channels

> 📘 Note
> 
> This section is applicable to all the digital channels: WhatsApp, RCS, Messenger, Apple Messages for Business, Email, and Mobile and Web.
> 
> As an example WhatsApp is shown in the images.

Webex Connect allows you to trigger a flow on receiving an incoming message only if the configured conditions are met. Here is how you can use this feature:



![Screenshot of Configuring WhatsApp Event with a Incoming Message set as trigger to invoke the flow.](https://files.readme.io/353ed5f-image.png)




**Illustration**

Let us look at an illustration to understand this clearly.

**Scenario 1 - within Same Service**

| Service 1                                                                                                                           |
| :---------------------------------------------------------------------------------------------------------------------------------- |
| Flow 1 - Start node event type (Postback for channel). Receive node waiting on ‘Incoming Message’ as event type.                    |
| Flow 2 - Start node event type (Incoming message for channel). Receive node waiting on ‘Incoming Message’ as event type.            |
| Flow 3 - Start node event type (Inbound Webhook for channel). Receive node waiting on ‘Incoming Message’ as event type for channel. |

The behavior of the flows is illustrated in the following table:



| User’s Messaging Behavior | Scenario breakdown | Behavior |
| --- | --- | --- |
| User sends a Postback message followed by two Incoming messages, one after the other. | User sends a Postback message. | Flow 1 with Postback event gets triggered and the receive node is waiting.  <br>  <br>Flow 2 is not triggered.  <br>  <br>Flow 3 is not triggered. |
|  | User sends a Incoming message. | Flow 1 is not triggered and the receive node is waiting.  <br>  <br>Flow 2 is triggered and the receive node is waiting.  <br>  <br>Flow 3 is not triggered. |
|  | User sends another Incoming message. | Flow 1 is not triggered.  <br>  <br>Flow 2 is continued and ended successfully.  <br>  <br>Flow 3 is not triggered. |
|  | After maximum time-out. | Flow 1 is completed with onTimeout and is shown as End-Incomplete. |
| User sends three Incoming messages one-by-one. | User sends first Incoming message. | Flow 2 is triggered and the receive node is waiting.  <br>  <br>Flow 1 and Flow 3 are not triggered. |
|  | User sends second Incoming message. | After second Incoming Message is sent, Flow 2 is continued and completed successfully.  <br>  <br>Flow 1 and Flow 3 are not  triggered. |
|  | User sends third Incoming message. | The third Incoming Message is triggered at Flow 2 and the receive node is waiting.  <br>  <br>Flow 1 and Flow 3 are not triggered. |
| User sends a Webhook trigger followed by Postback response and Incoming message. | User sends a Postback response. | Flow 1 is triggered and the receive node is waiting.  <br>  <br>Flow 3 is waiting at receive node.  <br>  <br>Flow 2 is not triggered. |
|  | User sends a Postback response. | Flow 1 is triggered and the receive node is waiting.  <br>  <br>Flow 3 is waiting at receive node.  <br>  <br>Flow 2 is not triggered. |
|  | User sends an Incoming message. | Flow 1 is not triggered and the receive node is waiting.  <br>  <br>Flow 3 is not triggered and the receive node is waiting.  <br>  <br>Flow 2 is triggered and the receive node is waiting. |
|  | After time-out. | Flow 1 ended with onTimeout at receive node.  <br>  <br>Flow 3 ended with onTimeout at receive node.  <br>  <br>Flow 2 ended with onTimeout at receive node. |




**Scenario 2 - with Two Services**

| Service 1                                                                                                                      | Service 2                                                                                                         |
| :----------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| Flow 1 - Start node event type (Postback for channel). Receive node waiting on ‘Incoming message’ as event type.               | Flow 4 - Start node event type (Post back for channel). Receive node waiting on ‘Incoming message’ as event type. |
| Flow 2 - Start node event type (Incoming message for channel). Receive node waiting on ‘Incoming message’ as event type.       | Flow 5 - Start node event type (Incoming message for channel). No Receive node.                                   |
| Flow 3 - Start node event type (Inbound Webhook) and a Receive node waiting on ‘Incoming message’ as event type for a channel. |                                                                                                                   |

The behavior of the flows is illustrated in the following table:



| User’s Messaging Behavior | Scenario breakdown | Behavior |
| --- | --- | --- |
| User sends a Postback message followed by two Incoming messages, one after the other | User sends a Postback message. | Flow 1 in service 1 and Flow 4 in service 2 are triggered and the receive node is waiting.  <br>  <br>Flow 2 and Flow 3 in service 1 and Flow 5 service 2 are not triggered. |
|  | User sends an Incoming message. | Flow 5 in service 2 is triggered and ended successfully.  <br>  <br>Flow 2 in service 1 is triggered and the receive node is waiting.  <br>  <br>Flow 1 in service 1 is not triggered and the receive node is waiting.  <br>  <br>Flow 4 in service 2 is not triggered and the receive node is waiting.  <br>  <br>Flow 3 in service 1 is not triggered. |
|  | User sends another Incoming message. | Flow 2 is continued and ended successfully.  <br>  <br>Flow 5 in service 2 is triggered again and ended successfully.  <br>  <br>Flow 1 and 4 are waiting at receive node.  <br>  <br>Flow 3 in service 1 is not triggered. |
|  | After time-out. | Flow 1 and Flow 4 ended with onTimeout at receive node. |
| User sends three Incoming messages one-by-one. | User sends first Incoming message. | Flow 2 is triggered and the receive node is waiting.  <br>  <br>Flow 5 is triggered and ended successfully.  <br>  <br>Flow 1 and 4 are not triggered. |
|  | User sends second Incoming message. | Flow 2 is triggered with Incoming Message 1 is continued and ended successfully with Incoming Message.  <br>  <br>Flow 5 is triggered and ended successfully.  <br>  <br>Flow 1, 3 and 4 are not triggered. |
|  | User sends third Incoming message. | Flow 5 is triggered and ended successfully.  <br>  <br>Flow 2 is triggered as a new transaction and the receive node waiting.  <br>  <br>Flow 1, 3, and 4 are not triggered. |
|  | After time-out. | Flow 2 ended with onTimeout at receive node. |
| User sends a Webhook trigger followed by Postback and Incoming message. | User sends a Webhook trigger. | Flow 3 gets triggered and the receive node is waiting.  <br>  <br>Flow 1, 2, 4, and 5 are not triggered. |
|  | User sends a Postback message. | Flow 1 and Flow 4 are triggered and the receive node is waiting.  <br>  <br>Flow 2 and Flow 5 are not triggered.  <br>  <br>Flow 3 is not triggered and the receive node is waiting. |
|  | User sends a Incoming message. | Flow 2 gets triggered and the receive node is waiting.  <br>  <br>Flow 5 is triggered and ended  successfully.  <br>  <br>Flow 1, 4, and 3 are not triggered. |
|  | After time-out. | Flow 1 ended with onTimeout at receive node.  <br>  <br>Flow 3 ended with onTimeout at receive node.  <br>  <br>Flow 2 ended with onTimeout at receive node.  <br>  <br>Flow 4 ended with onTimeout at receive node. |




## Conditional Trigger in RCS

When you access the Start Node in Flow Builder and select the RCS channel, you see the ‘Trigger only when there are no live sessions’ checkbox. When you enable this option, the RCS flow triggers only if no active sessions exist with a matching event type for the same RCS App and same user. If you enable Branded Text for the tenant, the system checks for active sessions across both RCS and Branded Text–enabled SMS flows.  
This prevents multiple flows from starting simultaneously for the same user, ensuring their conversation continues in the existing session until it either completes or times out.



![Configure RCS Event](https://files.readme.io/e66506403bed718ef6c90cc4f5d1407e0f47ad598da5f976df1307c9dffec146-2025-09-15_13-26-52.png)




For example, in a tenant, let us suppose there are two RCS flows Flow 1 and Flow 2, both are configured with same event type, “Incoming Message”, in the RCS Start Node. For Flow 1, conditional trigger (CT) is disabled and for Flow 2, it is enabled. Consider Branded Text setting is not enabled for this tenant.

**Same Service:** Consider that both the RCS Flows (Flow 1 and Flow 2) are configured in the same service. The table below describes how these two RCS flows behave when an incoming message arrives, depending on their current states. Each row represents an independent scenario and it does not depend on the previous rows.

**RCS Flows (Flow 1 and Flow 2) are configured in the same service**

| Current State of Flow 1 (F1) | Current State of Flow 2 (F2) with Conditional Trigger Enabled | Outcome                                                          |
| :--------------------------- | :------------------------------------------------------------ | :--------------------------------------------------------------- |
| Is at Start Node             | Waiting on the Receive Node                                   | F1 will get triggered, and F2 doesn't trigger and keeps waiting. |
| Waiting on Receive Node      | Is at Start Node                                              | F1 will continue; F2 will not trigger.                           |
| Is at Start Node             | Is at Start Node                                              | Both flows, F1 and F2, will trigger.                             |
| Waiting on Receive Node      | Waiting on Receive Node                                       | Both flows, F1 and F2, will continue.                            |

**Different Service:** Consider that both the RCS Flows (Flow 1 and Flow 2) are configured in different services. The table below describes how these two RCS flows behave when an incoming message arrives, depending on their current states. Each row is representing an independent scenario and it does not depend on the previous rows.

**RCS Flows (Flow 1 and Flow 2) are configured in the different service**



| Current State of Flow 1 (F1),  <br>Service 1 | Current State of Flow 2 (F2), Service 2, with Conditional Trigger Enabled | Outcome |
| --- | --- | --- |
| Is at Start Node | Waiting on Receive Node | F1 will get triggered, and F2 will continue. |
| Waiting on Receive Node | Is at Start Node | F1 will continue; F2 will not trigger. |
| Is at Start Node | Is at Start Node | Both flows, F1 and F2, will trigger. |
| Waiting on Receive Node | Waiting on Receive Node | Both flows F1 and F2 will continue. |




Please refer to the [Branded Text](https://help.webexconnect.io/docs/rcs-branded-text)  page for more information.