The _Start_ node is configured to trigger a flow using a channel, integration, webhook, or a custom event. This node allows you to configure the flow trigger in the context of the standard flow configuration. Further, the data from the trigger is available as node-level variables for use in the other flow nodes. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39e3a51-Start.jpg",
        "Start.jpg",
        "Screenshot of Start Node"
      ],
      "align": "center",
      "caption": "Start Node"
    }
  ]
}
[/block]


While creating a [new flow](doc:flows#section-creating-a-flow), you are prompted to configure the start node. You can choose either to configure or skip to do it later. Select a [trigger](doc:rules#section-triggers) and configure the details. Click the close icon at the upper right corner of the page to skip the trigger configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1543235-1.jpeg",
        null,
        "Screenshot of Trigger Category"
      ],
      "align": "center",
      "border": true,
      "caption": "Trigger Category"
    }
  ]
}
[/block]


## Triggering a Flow on various Channel Events

> ❗️ 
> 
> The Instagram as a channel is deprecated.

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Possible Events",
    "0-0": "SMS",
    "0-1": "Mobile Originated - MO (Allows you to trigger the flow on an incoming SMS message)  \nOn Link Click  \n  \nRefer ['Conditional Trigger in SMS'](https://help.imiconnect.io/docs/start-node#section-conditional-trigger-in-sms) section if you want to use the 'Trigger only when there are no live sessions option'.",
    "1-0": "Voice",
    "1-1": "Inbound Call  \nMissed Call  \n  \n**Note:** <<prodname>> offers the ability to trigger the same flow for incoming calls received on more than one phone number by using a routing number option. The mapping of the routing number with the set of phone numbers for dialing is to be configured by the Ops team. Reach out to [Ops team](mailto:operations@imimobile.com) if you want to use this feature.\\_  \n  \nCurrently, the routing number feature is supported in the USA and Canada only.",
    "2-0": "MMS",
    "2-1": "Mobile Originated - MO (Allows you to trigger the flow on an incoming MMS message)",
    "3-0": "Messenger",
    "3-1": "Incoming Message  \nOn Link Click  \nPostback",
    "4-0": "Instagram (Deprecated)",
    "4-1": "Incoming Message - This event occurs every time a user sends a text message with or without attachments to your Instagram account.  \n  \nPostback - This event is triggered when user clicks postback type button.  \n  \nMessage Deleted - This event occurs every time a user sends a delete message to your Instagram account.",
    "5-0": "WhatsApp",
    "5-1": "Incoming Message - details of the sender ID and name are displayed. The whatsapp.username output variable contains the sender's user name.  \n  \nPostback - Postback event captures the payload received when a customer clicks on  a quick reply button within an interactive template  \n  \nList Message - This event occurs every time a user selects one of the List Message options  \nReply Buttons  Message - This event occurs every time a user selects one of the Reply Buttons  options",
    "6-0": "Mobile & Web App",
    "6-1": "Custom Event  \n  \nIncoming Message_ - \\_inappmessaging.appid_ output variable captures the app ID corresponding to the incoming event  \n  \nOn Thread Closed - this event can be used to trigger a workflow in cases where an agent has resolved a client query and marked the conversation as closed, or if a customer has abandoned a chat and the chat is marked as closed due to it being timed out. The reasonForThreadClosure captures the reason for closing the thread.  \n  \nOnPostback - this event is triggered when the user clicks postback type button  \n  \nSubscribe - this event is triggered when the user clicks re-subscribe button  \n  \nUnsubscribe - this event is triggered when the user clicks unsubscribe link  \n  \nTyping Indicator - This event is triggered when a user starts or stops typing in a Live Chat or In-App Messaging conversation.",
    "7-0": "Email",
    "7-1": "Incoming Message  \nSubscribe  \nUnsubscribe  \nThe platform will not trigger or resume a flow, nor trigger a rule or an outbound webhook notification for incoming emails where Sender Email ID is same as the Recipient Email ID. However, details of such incoming emails will be available within Export Logs.",
    "8-0": "<<AMB>>",
    "8-1": "Conversation Closed  \nIncoming Message  \nInteractive Message: Invitation Response  \nInteractive Message: Classical Authentication  \nInteractive Message: Form Response  \nInteractive Message: iMessage App Response  \nInteractive Message: List Picker Or Time Picker  \nInteractive Message: New Authentication  \nInteractive Message: Payment  \nInteractive Message: Quick Replies (A flow is triggered when a Quick Reply message is received from a customer.)  \nTyping Indicator",
    "9-0": "RCS",
    "9-1": "Incoming Attachment  \nIncoming Message  \nLocation Response  \nPostback  \nUnsubscribe  \nSubscribe"
  },
  "cols": 2,
  "rows": 10,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Flow Triggers for Integrations

[block:parameters]
{
  "data": {
    "h-0": "Integration",
    "h-1": "Possible Events",
    "0-0": "CCSP (Deprecated)",
    "0-1": "Agent Chat Initiated  \nChat Closed  \nChat Idle  \nChat Opened  \nChat Picked  \nChat Reopened  \nChat Transferred  \nCustom Event  \nIncoming Message",
    "1-0": "BOT (Deprecated)",
    "1-1": "Custom Event  \nHandover  \nMilestone Reached  \nNotify  \nUnhandled Message",
    "2-0": "AI Agent",
    "2-1": "Trigger from AI Agent to initiate flow"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Triggering a Flow using Custom Event API or Inbound Webooks

[block:parameters]
{
  "data": {
    "h-0": "Custom Trigger",
    "h-1": "Possible Events",
    "0-0": "Webhook",
    "0-1": "Select an existing webhook  \nCreate a new webhook event",
    "1-0": "Custom event",
    "1-1": "Select an existing event  \nCreate a new event"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d8259a0-1.png",
        "Start Node Inbound SMS with a condition on the text message set as trigger to invoke the flow.png",
        "Screenshot of Conditional trigger to invoke a flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Inbound SMS with a condition on the text message set as trigger to invoke the flow"
    }
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7506a31-2.jpeg",
        "Start Node_Custom Event Configuration.png",
        "Screenshot of Configuring a Custom Event"
      ],
      "align": "center",
      "border": true,
      "caption": "Custom Event Configuration"
    }
  ]
}
[/block]


- The sample payload is dynamically generated for API request body based on the configured parameters. The event id i.e., `evtid` for the configured custom event is generated once you save the configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1e1cef5-json-body-in-custom-event.png",
        "json-body-in-custom-event.png",
        "Screenshot of Dynamically Generated Sample Payload"
      ],
      "align": "center",
      "caption": "Dynamically Generated Sample Payload"
    }
  ]
}
[/block]


You can start using the custom events in the flows. When you use the custom event node in a flow, the event URL is auto-populated and authentication is mandated.

## Conditional Trigger in SMS

<<prodname>> allows you to conditionally trigger a flow on receiving an incoming SMS message only if the configured conditions are met. Here's how you can use this feature:

1. Double-click the Start node and select 'SMS - Mobile Originated - MO' as the flow trigger.
2. Provide the required details like SMS event, Incoming Number, and Keyword.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f3afd70-Start_Node2.jpg",
        "Start Node Conditional Trigger.png",
        "Screenshot of Conditional Trigger only when there are no live sessions checkbox"
      ],
      "align": "center",
      "border": true,
      "caption": "Conditional Trigger"
    }
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Conditions (Trigger message and receive)",
    "h-1": "Checkbox status in different flows",
    "h-2": "Behavior",
    "0-0": "  _ Message 1 – Help  \n  _ Message 2 - Loan ",
    "0-1": "  _ Enabled for Flow 1  \n  _ Disabled for Flow 2  \n  _ Enabled for Flow 3  \n  _ Enabled for Flow 4  \n  _ NA for Flow 5  \n  _ Enabled/Disabled for Flow 6 ",
    "0-2": "  _ Message 1 triggers Flow 1 and Flow 2  \n  _ Message 2 will be received by Flow 1 and Flow 2 receive node ",
    "1-0": "_ Message 1 – Help  \n  _ Message 2 - Loan",
    "1-1": "  _ Enabled for Flow 1  \n  _ Disabled for Flow 2  \n  _ Enabled for Flow 3  \n  _ Disabled for Flow 4  \n  _ NA for Flow 5  \n  _ Enabled/Disabled for Flow 6 ",
    "1-2": "  _ Flow 1 and Flow 2 get triggered when Help is sent  \n  _ Message 2 triggers only Flow 4 and does not trigger Flow 3. ",
    "2-0": "  _ Message 1 – Total  \n  _ Message 2 - Loan ",
    "2-1": "  _ Enabled for Flow 1  \n  _ Disabled for Flow 2  \n  _ Disabled for Flow 3  \n  _ Disabled for Flow 4  \n  _ NA for Flow 5  \n  _ Enabled/Disabled for Flow 6 ",
    "2-2": "  _ Message 1 triggers Flow 3  \n  _ Message 2 triggers Flow 4 as the checkbox is disabled and will be received by Flow 3 Receive node ",
    "3-0": "  _ Message 1 – Total  \n  _ Message 2 - Loan ",
    "3-1": "  _ Enabled for Flow 1  \n  _ Disabled for Flow 2  \n  _ NA for Flow 3  \n  _ Disabled for Flow 4  \n  _ Enabled for Flow 5  \n  _ Enabled/Disabled for Flow 6 ",
    "3-2": "  _ Message 1 triggers Flow 5  \n  _ Message 2 triggers Flow 4 as the checkbox is disabled and will be received by Flow 5 Receive node ",
    "4-0": "  _ Message 1 – Total  \n  _ Message 2 - Balance ",
    "4-1": "  _ Enabled for Flow 1  \n  _ Disabled for Flow 2  \n  _ NA for Flow 3  \n  _ Disabled for Flow 4  \n  _ Enabled for Flow 5  \n  _ Disabled for Flow 6 ",
    "4-2": "  _ Message 1 triggers Flow 5  \n  _ Message 2 triggers Flow 6 as the checkbox is disabled and will be received by Flow 5 Receive node ",
    "5-0": "  _ Message 1 – Balance  \n  _ Message 2 - Loan ",
    "5-1": "  _ Enabled for Flow 1  \n  _ Disabled for Flow 2  \n  _ Disabled for Flow 3  \n  _ Disabled for Flow 4  \n  _ NA for Flow 5  \n  _ Disabled for Flow 6 ",
    "5-2": "  _ Message 1 triggers Flow 6  \n  _ Message 2 triggers Flow 3 and will be received by Flow 6 Receive node "
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Output Variables
> 
> Please refer to [Output Variables](https://help.imiconnect.io/docs/receive#output-variables) in Receive Node page to understand the details of Output Variables available for various channel events.

## Flow Trigger Behaviour in Digital Channels

> 📘 Note
> 
> This section is applicable to all the digital channels: WhatsApp, RCS, Messenger, Apple Messages for Business, Email, and Mobile and Web.
> 
> As an example WhatsApp is shown in the images.

<<prodname>> allows you to trigger a flow on receiving an incoming message only if the configured conditions are met. Here is how you can use this feature:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/353ed5f-image.png",
        null,
        "Screenshot of Configuring WhatsApp Event with a Incoming Message set as trigger to invoke the flow."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring WhatsApp Event with a Incoming Message set as trigger to invoke the flow."
    }
  ]
}
[/block]


**Illustration**

Let us look at an illustration to understand this clearly.

**Scenario 1 - within Same Service**

| Service 1                                                                                                                           |
| :---------------------------------------------------------------------------------------------------------------------------------- |
| Flow 1 - Start node event type (Postback for channel). Receive node waiting on ‘Incoming Message’ as event type.                    |
| Flow 2 - Start node event type (Incoming message for channel). Receive node waiting on ‘Incoming Message’ as event type.            |
| Flow 3 - Start node event type (Inbound Webhook for channel). Receive node waiting on ‘Incoming Message’ as event type for channel. |

The behavior of the flows is illustrated in the following table:

[block:parameters]
{
  "data": {
    "h-0": "User’s Messaging Behavior",
    "h-1": "Scenario breakdown",
    "h-2": "Behavior",
    "0-0": "User sends a Postback message followed by two Incoming messages, one after the other.",
    "0-1": "User sends a Postback message.",
    "0-2": "Flow 1 with Postback event gets triggered and the receive node is waiting.  \n  \nFlow 2 is not triggered.  \n  \nFlow 3 is not triggered.",
    "1-0": "",
    "1-1": "User sends a Incoming message.",
    "1-2": "Flow 1 is not triggered and the receive node is waiting.  \n  \nFlow 2 is triggered and the receive node is waiting.  \n  \nFlow 3 is not triggered.",
    "2-0": "",
    "2-1": "User sends another Incoming message.",
    "2-2": "Flow 1 is not triggered.  \n  \nFlow 2 is continued and ended successfully.  \n  \nFlow 3 is not triggered.",
    "3-0": "",
    "3-1": "After maximum time-out.",
    "3-2": "Flow 1 is completed with onTimeout and is shown as End-Incomplete.",
    "4-0": "User sends three Incoming messages one-by-one.",
    "4-1": "User sends first Incoming message.",
    "4-2": "Flow 2 is triggered and the receive node is waiting.  \n  \nFlow 1 and Flow 3 are not triggered.",
    "5-0": "",
    "5-1": "User sends second Incoming message.",
    "5-2": "After second Incoming Message is sent, Flow 2 is continued and completed successfully.  \n  \nFlow 1 and Flow 3 are not  triggered.",
    "6-0": "",
    "6-1": "User sends third Incoming message.",
    "6-2": "The third Incoming Message is triggered at Flow 2 and the receive node is waiting.  \n  \nFlow 1 and Flow 3 are not triggered.",
    "7-0": "User sends a Webhook trigger followed by Postback response and Incoming message.",
    "7-1": "User sends a Postback response.",
    "7-2": "Flow 1 is triggered and the receive node is waiting.  \n  \nFlow 3 is waiting at receive node.  \n  \nFlow 2 is not triggered.",
    "8-0": "",
    "8-1": "User sends a Postback response.",
    "8-2": "Flow 1 is triggered and the receive node is waiting.  \n  \nFlow 3 is waiting at receive node.  \n  \nFlow 2 is not triggered.",
    "9-0": "",
    "9-1": "User sends an Incoming message.",
    "9-2": "Flow 1 is not triggered and the receive node is waiting.  \n  \nFlow 3 is not triggered and the receive node is waiting.  \n  \nFlow 2 is triggered and the receive node is waiting.",
    "10-0": "",
    "10-1": "After time-out.",
    "10-2": "Flow 1 ended with onTimeout at receive node.  \n  \nFlow 3 ended with onTimeout at receive node.  \n  \nFlow 2 ended with onTimeout at receive node."
  },
  "cols": 3,
  "rows": 11,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Scenario 2 - with Two Services**

| Service 1                                                                                                                      | Service 2                                                                                                         |
| :----------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| Flow 1 - Start node event type (Postback for channel). Receive node waiting on ‘Incoming message’ as event type.               | Flow 4 - Start node event type (Post back for channel). Receive node waiting on ‘Incoming message’ as event type. |
| Flow 2 - Start node event type (Incoming message for channel). Receive node waiting on ‘Incoming message’ as event type.       | Flow 5 - Start node event type (Incoming message for channel). No Receive node.                                   |
| Flow 3 - Start node event type (Inbound Webhook) and a Receive node waiting on ‘Incoming message’ as event type for a channel. |                                                                                                                   |

The behavior of the flows is illustrated in the following table:

[block:parameters]
{
  "data": {
    "h-0": "User’s Messaging Behavior",
    "h-1": "Scenario breakdown",
    "h-2": "Behavior",
    "0-0": "User sends a Postback message followed by two Incoming messages, one after the other",
    "0-1": "User sends a Postback message.",
    "0-2": "Flow 1 in service 1 and Flow 4 in service 2 are triggered and the receive node is waiting.  \n  \nFlow 2 and Flow 3 in service 1 and Flow 5 service 2 are not triggered.",
    "1-0": "",
    "1-1": "User sends an Incoming message.",
    "1-2": "Flow 5 in service 2 is triggered and ended successfully.  \n  \nFlow 2 in service 1 is triggered and the receive node is waiting.  \n  \nFlow 1 in service 1 is not triggered and the receive node is waiting.  \n  \nFlow 4 in service 2 is not triggered and the receive node is waiting.  \n  \nFlow 3 in service 1 is not triggered.",
    "2-0": "",
    "2-1": "User sends another Incoming message.",
    "2-2": "Flow 2 is continued and ended successfully.  \n  \nFlow 5 in service 2 is triggered again and ended successfully.  \n  \nFlow 1 and 4 are waiting at receive node.  \n  \nFlow 3 in service 1 is not triggered.",
    "3-0": "",
    "3-1": "After time-out.",
    "3-2": "Flow 1 and Flow 4 ended with onTimeout at receive node.",
    "4-0": "User sends three Incoming messages one-by-one.",
    "4-1": "User sends first Incoming message.",
    "4-2": "Flow 2 is triggered and the receive node is waiting.  \n  \nFlow 5 is triggered and ended successfully.  \n  \nFlow 1 and 4 are not triggered.",
    "5-0": "",
    "5-1": "User sends second Incoming message.",
    "5-2": "Flow 2 is triggered with Incoming Message 1 is continued and ended successfully with Incoming Message.  \n  \nFlow 5 is triggered and ended successfully.  \n  \nFlow 1, 3 and 4 are not triggered.",
    "6-0": "",
    "6-1": "User sends third Incoming message.",
    "6-2": "Flow 5 is triggered and ended successfully.  \n  \nFlow 2 is triggered as a new transaction and the receive node waiting.  \n  \nFlow 1, 3, and 4 are not triggered.",
    "7-0": "",
    "7-1": "After time-out.",
    "7-2": "Flow 2 ended with onTimeout at receive node.",
    "8-0": "User sends a Webhook trigger followed by Postback and Incoming message.",
    "8-1": "User sends a Webhook trigger.",
    "8-2": "Flow 3 gets triggered and the receive node is waiting.  \n  \nFlow 1, 2, 4, and 5 are not triggered.",
    "9-0": "",
    "9-1": "User sends a Postback message.",
    "9-2": "Flow 1 and Flow 4 are triggered and the receive node is waiting.  \n  \nFlow 2 and Flow 5 are not triggered.  \n  \nFlow 3 is not triggered and the receive node is waiting.",
    "10-0": "",
    "10-1": "User sends a Incoming message.",
    "10-2": "Flow 2 gets triggered and the receive node is waiting.  \n  \nFlow 5 is triggered and ended  successfully.  \n  \nFlow 1, 4, and 3 are not triggered.",
    "11-0": "",
    "11-1": "After time-out.",
    "11-2": "Flow 1 ended with onTimeout at receive node.  \n  \nFlow 3 ended with onTimeout at receive node.  \n  \nFlow 2 ended with onTimeout at receive node.  \n  \nFlow 4 ended with onTimeout at receive node."
  },
  "cols": 3,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Conditional Trigger in RCS

When you access the Start Node in Flow Builder and select the RCS channel, you see the ‘Trigger only when there are no live sessions’ checkbox. When you enable this option, the RCS flow triggers only if no active sessions exist with a matching event type for the same RCS App and same user. If you enable Branded Text for the tenant, the system checks for active sessions across both RCS and Branded Text–enabled SMS flows.  
This prevents multiple flows from starting simultaneously for the same user, ensuring their conversation continues in the existing session until it either completes or times out.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e66506403bed718ef6c90cc4f5d1407e0f47ad598da5f976df1307c9dffec146-2025-09-15_13-26-52.png",
        "",
        "Screenshot of Configure RCS Event with Conditional Trigger."
      ],
      "align": "center",
      "border": true,
      "caption": "Configure RCS Event"
    }
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Current State of Flow 1 (F1),  \nService 1",
    "h-1": "Current State of Flow 2 (F2), Service 2, with Conditional Trigger Enabled",
    "h-2": "Outcome",
    "0-0": "Is at Start Node",
    "0-1": "Waiting on Receive Node",
    "0-2": "F1 will get triggered, and F2 will continue.",
    "1-0": "Waiting on Receive Node",
    "1-1": "Is at Start Node",
    "1-2": "F1 will continue; F2 will not trigger.",
    "2-0": "Is at Start Node",
    "2-1": "Is at Start Node",
    "2-2": "Both flows, F1 and F2, will trigger.",
    "3-0": "Waiting on Receive Node",
    "3-1": "Waiting on Receive Node",
    "3-2": "Both flows F1 and F2 will continue."
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


Please refer to the [Branded Text](https://help.webexconnect.io/docs/rcs-branded-text)  page for more information.