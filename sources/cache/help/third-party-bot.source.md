The integration between the BOT platform and <<prodname>> is setup using webhooks. The platform will provide incoming and outgoing webhooks.<br>

The outgoing webhook will be used to notify the BOT platform of events such as an incoming message from an end customer (if the customer interaction channel is managed by IMI) or an agent’s response.

## Adding a BOT Integration

A BOT integration allows <<prodname>> to route messages to and from your BOT.<br>

To add a new BOT:

1. Click **Assets** > **Integrations** > **Add Integration** > **Generic Bot**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/597fbc0-Third_Party.jpeg",
        "img1.jpg",
        "Screenshot of Adding Integrations."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding Integrations"
    }
  ]
}
[/block]


2. Select  **BOT PLATFORM** and click **Next**.  
   Choose **IMI BOT** to allow <<prodname>> to route messages to and from a BOT. Otherwise, choose **OTHERS**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8a80ef4-img1.jpg",
        "img1.jpg",
        "Screenshot of Selecting BOT Platform"
      ],
      "align": "center",
      "border": true,
      "caption": "Select BOT Platform"
    }
  ]
}
[/block]


3. _For IMI BOT platform_, enter a name for the integration and click **Next**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dadb879-img3.jpg",
        "img3.jpg",
        "Screenshot of Enter Integration Name"
      ],
      "align": "center",
      "border": true,
      "caption": "Enter Integration Name"
    }
  ]
}
[/block]


4. **(For IMI BOT Only)** A BOT endpoint is used to notify your BOT of <<prodname>> events via HTTPS POST request using the BOTs access token for verification in every interaction with the BOT.  
   In the BOT Endpoint window. Enter a value in BOT's endpoint URL and BOT's access token.
5. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f9e5074-Third_Party1.jpeg",
        "imibot.jpg",
        "Screenshot of Configuring Bot Endpoint"
      ],
      "align": "center",
      "border": true,
      "caption": "IMI Bot: Bot Endpoint"
    }
  ]
}
[/block]


6. _For Other_ platform, enter a name for the integration and click **Next**.
7. **(For Generic BOT only)** In the **Outbound Webhook** window, enter values for the following:
   - **Webhook URL**: This is used to notify your BOT of <<prodname>> events via an HTTPS POST request.
   - **Verification Token**: The webhook will return this verification token as part of the response to every POST request.

User must configure the Webhook URL on which the BOT will receive the events from <<prodname>>. This Webhook will notify <<prodname>> of the BOT events via HTTPS POST requests.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/75366d3-img2.jpg",
        "img2.jpg",
        "Screenshot of Configuring Outbound Webhook."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring Outbound Webhook."
    }
  ]
}
[/block]


7. Click **Verify** and then **Save**.

## Using Bot in a Service

To use a BOT in a service,

1. On the integration list, map the added BOT integration to a service and click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/85d02d4-img5.jpg",
        "img5.jpg",
        "Screenshot of Adding Integration to Service."
      ],
      "align": "center",
      "border": true,
      "caption": "Add Integration to Service"
    }
  ]
}
[/block]


2. Create a rule with incoming message on the added channel asset as the trigger, to perform one of the following actions:

- Forward the message to CCSP integration 
- Forward the message to BOT
- Forward the message to be handled by BOT + CCSP

3. Select an event from the available list and enter trigger conditions:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4e1c8d7-img7.jpg",
        "img7.jpg",
        "Screenshot of Selecting Event"
      ],
      "align": "center",
      "border": true,
      "caption": "Select Event"
    }
  ]
}
[/block]


The **Handover** event is raised when the BOT decides to handover the chat to a CCSP integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8034548-img8.jpg",
        "img8.jpg",
        "Screenshot of Select Trigger Channel"
      ],
      "align": "center",
      "border": true,
      "caption": "Select Trigger Channel"
    }
  ]
}
[/block]


The first message is always received by the BOT, then the CCSP will hold the flag to route all future messages from the same user on that particular channel asset.  
All the messages, that is, from the customer or agent, are forwarded to the BOT so that it can collate the data.

### Communicating with BOT

1. After the rule with a BOT, the action is configured in the service, a new message from the customer on the configured rule trigger channel will be sent to the BOT on the configured Webhook, via chat engine.
2. Chat engine will create a unique conversation ID of type BOT for a unique combination of asset ID, user identifier on the channel, the service, and the BOT.  
   **While communicating with a BOT, the same conversation ID must be used, unless the BOT chooses to close the conversation**.
3. If the Webhook does not respond within five seconds or there is an error, then a maximum of four retry attempts will occur over the next hour. 
4. If there are five consecutive failures observed, then the Webhook is made temporarily inactive. To reactivate the BOT integration must be edited and Webhook must be re-verified. 
5. With each event, a unique conversation ID parameter is also passed. This conversation ID is used to identify a unique customer conversation; the BOT platform is expected to pass the conversation ID back to the <<prodname>> to identify the activity on the same conversation ID.
6. The BOTs response is received on the Webhook URL that was generated for the added integration.

```json Incoming message on a channel
{
Conversationid : "", // auto-generated by IMI
ConversationType : "BOT" // if the conversation is of type BOT then only the BOT is expected to send a response
Message : "",
MessageType : "",
Messageid :"",
Media:"",
Channel : "",
Event : "Incoming message",
Timestamp : "YYYY-MM-DD hh:mm:ss.SS", //S in GMT
}
```
```text Sample POSTBACK event
{
Conversationid : "",
ConversationType : "BOT"
PostbackPayload : “PAYLOAD VALUE”,
Channel : "FB",
Event : "FB POSTBACK",
Timestamp: "YYYY-MM-DD hh:mm:ss.SS",//in GMT
}
```
```text Sample message delivery
{
Conversationid : "",
ConversationType : "BOT"
Messageid :"",
Channel : "",
Event : "Message Delivery",
DeliveryStatus :”Delivered/Failed/Read”,
Description :”Error description”, //only in case of failures
Timestamp: "YYYY-MM-DD hh:mm:ss.SS",//in GMT
}
```

```text BOTs Reply
{
eventid : "1001",
conversation_id : "",
message : ""
Messagetype: "",
Timestamp: "", //YYYY-MM-DD hh:mm:ss.SSS in GMT
customparam1 :"",
.
.
.
customparamN: ""
}
```
```text Conversation Handover to Agent
{ 
eventid : "1002",//can be event type as the key name and predefined text as value well which ever suits the dev. 
conversation_id : "", 
Timestamp: "", //YYYY-MM-DD hh:mm:ss.SSS in GMT customparam1 :"", 
… 
customparamN: "" 
}
```

## Conversation Between BOT and CCSP

When a rule is configured for BOT and CCSP, the first message of the conversation is always received by the BOT. Only when the handover event is received from BOT, the subsequent messages from the customer is sent to the CCSP.

The conversation ID with a BOT is the same during all interactions, unless the BOT closes the conversation, whereas, every conversation with the CCSP agent has a new conversation ID, which is closed on chat engine (when an agent closes the conversation).