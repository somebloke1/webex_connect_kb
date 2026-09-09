This node calls Webex Engage Append Conversation API to append the message to an existing conversation on Webex Engage. While configuring flows in <<prodname>>, you’d need to use this node for appending a message from the end-user to an existing conversation. So that the same will be reflected in the agent desktop.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. .  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Append Conversation** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3ef896b-LC_Append.jpg",
        "LC Append.jpg",
        "Interface section displaying the method name \"Append Conversation\"."
      ],
      "align": "center",
      "border": true,
      "caption": "Interface section displaying the method name \"Append Conversation\"."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Append conversation",
    "0-1": "TransId",
    "0-2": "_ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ Failure  \n  _ onAppendMessageFailure  \n  _ onAppendMessageSuccess  \n  _ onTimeout"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Field Value",
    "0-0": "Facebook Messenger",
    "0-1": "CHANNEL - Facebook  \nCONVERSATION ID - $(n6.conversationId)  \nDIRECTION - Inbound  \nMESSAGE TYPE - Text With Attachments  \nTEXT - $(n2.messenger.message)  \nTIMESTAMP (IN UTC) - $(n2.messenger.ts)",
    "1-0": "SMS",
    "1-1": "CHANNEL - SMS  \nCONVERSATION ID - $(n6.conversationId)  \nDIRECTION - Inbound  \nTEXT - $(n2.sms.message)  \nTIMESTAMP (IN UTC) - $(n2.sms.ts)",
    "2-0": "Email",
    "2-1": "CONVERSATION ID - $(n6.conversationId)  \nDIRECTION – Inbound  \nTIMESTAMP (IN UTC) - $(n2.email.timestamp)  \nFROM ADDRESS - $(n2.email.emailId)  \nTO RECEPIENTS - $(n2.email.toAddresses)  \nCC RECEPIENTS - $(n2.email.ccRecipients)  \nSUBJECT - $(n2.email.subject)  \nEMAIL HEADERS - $(n2.email.headers)  \nPLAIN BODY - $(messageStrippedText)  \nHTML BODY - $(messageHTML)  \nSTRIPPED HTML - $(messageStrippedHTML)  \nATTACHMENTS - $(parseDataAttachments)",
    "3-0": "Live Chat",
    "3-1": "CHANNEL - Live Chat  \nCONVERSATION ID - $(n6.conversationId)  \nDIRECTION - Inbound, Outbound, Announcement  \n  \nDirection Inbound - MESSAGE TYPE -  \n                                   - Text  \n                                   - Text With Attachments  \n                                   - Live Chat Form Response  \n                                   - Live Chat Carousel Response  \n                                   - Live Chat Quick Replies  \n                                      Response  \n  \nDirection Outbound - MESSAGE TYPE -  \n                                      - Text With Attachments  \n                                      - Live Chat Text with Carousel  \n                                      - Live Chat  Text with Quick  \n                                         Replies  \n  \nDirection Announcement - Text  \n                                           - TIMESTAMP (IN UTC)  \n  \nTEXT - $(message)  \n  \nTIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  \n  \nATTACHMENTS - $(parseDataAttachment)  \n  \nQUICK REPLIES (Inbound) - $(n2.Inappmessaging.postback)  \n  \nCAROUSALS (Inbound) - $(n2.Inappmessaging.postback)  \n  \nQUICK REPLIES (Outbound) -  $(n<nodeId>.send.quickreplies)  \n  \nCAROUSALS (Outbound) - $(n<nodeId>.send.template)",
    "4-0": "WhatsApp",
    "4-1": "CHANNEL - WhatsApp  \n  \nConversation ID - $(conversationId)  \n  \nTEXT - $(messageFromCustomer)  \n  \nTIMESTAMP (IN UTC) - $(n2.whatsapp.ts)  \n  \nATTACHMENTS - $(parseDataAttachment)"
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> Based on the Direction selected in Live Chat the Message Type will be changed accordingly.  
> When Direction is selected as Inbound the Message Types are:
> 
> - Text
> - Live Chat Form Response
> - Text With Attachments is default value selected
> - Live Chat Carousel Response
> - Live Chat Quick Replies Response

**Method Name - Append Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variable",
    "0-0": "CHANNEL – Facebook Messenger  \n  \nCONVERSATION ID - $(n6.conversationId)  \n  \n  \\_ Conversation from the output variables of the Search Conversation is the Conversation ID  \n  \nDIRECTION – Inbound  \n  \nTEXT - $(messageFromCustomer)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming message object from customer respectively  \n  \n  \\_ Message from the output variables of the start node is the message. The message will be appended to the conversation  \n  \nTIMESTAMP (IN UTC) - $(n2.messenger.ts)  \n  \n  \\_ $(n2.messenger.ts) is the timestamp of the message  \n  \nATTACHMENT - $(parseDataAttachment)  \n  \n  \\* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively",
    "0-1": "TransId"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Append Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL – SMS  \n  \nCONVERSATION ID - $(n6.conversationId)  \n  \n•\tConversation from the output variables of the Search Conversation is the Conversation ID  \nDIRECTION – Inbound  \n  \nTEXT - $(n2.sms.message)  \n  \n•\tMessage from the output variables of the start node is the message. The message will be appended to the conversation  \n  \nTIMESTAMP (IN UTC) - $(n2.sms.ts)  \n  \n•\t$(n2.sms.ts) is the timestamp of the message  \n  \nNote: when the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable.  \n  \nEg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)",
    "0-1": "TransId"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


**Method Name - Append Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL – EMAIL  \n  \nCONVERSATION ID - $(n6.conversationId)  \n  \n  \\_ Conversation from the output variables of the Search Conversation is the Conversation ID  \n  \nDIRECTION – Inbound  \n  \nFROM EMAIL ID - $(n2.email.emailId)  \n  \n  \\_ emailId in the output variables of the start node is from email id  \n  \nEMAIL SUBJECT - $(n2.email.subject)  \n  \n  \\_ Subject in the output variables of the start node is the subject  \n  \nTO RECEPIENTS - $(n2.email.toAddresses)  \n  \n  \\_ ToAddresses in the output variables of the start node is the To Recepients  \n  \nCC RECEPIENTS - $(n2.email.ccRecipients)  \n  \n  \\_ ccRecepients in the output variables of the start node is the CC Recepients  \n  \nTIMESTAMP (IN UTC) - $(n2.email.timestamp)  \n  \n  \\_ Timestamp in the output variables of the start node which contains the Email Timestamp  \n  \nEMAIL HEADERS - $(n2.email.headers)  \n  \n  \\_ Email Headersvin the output variables of the start node is the Email Headers  \n  \nPLAIN BODY - $(messageStrippedText)  \n  \n  \\_ messageStrippedText in the custom variables is the Plain body  \n  \nHTML BODY - $(messageHTML)  \n  \n  \\_ MessageHTML in the custom variables is the HTML body  \n  \nSTRIPPED HTML - $(messageStrippedHTML)  \n  \n  \\_ messageStrippedHTML in the custom variables is the Stripped HTML  \n  \nATTACHMENT - $(parseDataAttachment)  \n  \n  \\* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively",
    "0-1": "TransId"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Append Conversation** 

> 📘 Note
> 
> Append Conversation has two versions 1.0 and 1.3

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "CHANNEL – LIVECHAT  \n  \nCONVERSATION ID - $(n6.conversationId) (Here, n6 is the respective node ID)  \n  \n  \\_ Conversation from the output variables of the Search Conversation is the Conversation ID  \n  \nDIRECTION – Inbound  \n  \nMESSAGE TYPE -  \n_ Text  \n_ Text With Attachments  \n_ Live Chat Form Response  \n_ Live Chat with Carousel Response  \n\\_ Live Chat with Quick Replies Response  \n  \nLive Chat Quick Replies Response Object/Live Chat Carousels Response Object: $(Inappmessaging.postback)  \n  \nDIRECTION – Outbound  \n  \nMESSAGE TYPE -  \n_ Text With Attachments  \n_ Live Chat Text with Carousel  \n\\_ Live Chat Text with Quick Replies  \n  \nLive Chat Quick Replies Object/Live Chat Carousels Object: $(n<nodeId>.send.template) or $(n<nodeId>.send.quickreplies)  \n  \nATTACHMENT - $(parseDataAttachment)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively  \n  \nTEXT - $(message)  \n  \n  \\_ message is one of the custom variables which contains the message  \n  \nTIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  \n  \n  \\_ $(n2.inappmessaging.timestamp) is one of the start node variables which contains the Timestamp  \n  \nDIRECTION – Announcement  \n  \nTEXT - $(message)  \n  \n  \\_ message is one of the custom variable which contains the message  \n  \nTIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  \n  \\_ Timestamp in the output variables of the start node which contains the Timestamp  \n  \n  \\* $(n2.inappmessaging.timestamp) is one of the start node variables which contains the Timestamp",
    "0-1": "TransId",
    "0-2": "Text With Attachments, Live Chat Carousel Response,  \nLive Chat Quick Replies Response are available in v1.3 for Inbound Direction  \n  \next With Attachments, Live Chat Text With Carousel, Live Chat Text With Quick Replies are available in v1.3 for Outbound Direction  \n  \nAnnouncement is available in v1.3"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Append Conversation** 

**WhatsApp Rich Messages:**

> 🚧 Unsupported variable
> 
> The $(n30.send.response_interactive) variable is not supported for WhatsApp Buttons or Lists. To implement these features, you must manually construct a JSON payload that conforms to the following schemas.

**Outbound Payloads **

To send interactive messages, use the following JSON structures:

```json Buttons
{
  "header": { "type": "text", "text": "your text" },
  "body": { "text": "your-text-body-content" },
  "footer": { "text": "your-text-footer-content" },
  "action": {
    "buttons": [
      { "type": "reply", "reply": { "id": "unique-id", "title": "Button Title" } }
    ]
  }
}
```
```json Lists
{
  "header": { "type": "text", "text": "your text" },
  "body": { "text": "your-text-body-content" },
  "footer": { "text": "your-text-footer-content" },
  "action": {
    "button": "cta-button-content",
    "sections": [
      { "title": "section-title", "rows": [{ "id": "row-id", "title": "row-title" }] }
    ]
  }
}
```

**Inbound Payloads **

When processing inbound interactive responses, the system expects the following format:

```json Interactive response
{
  "title": "Option 1",
  "identifier": "b0c75e59-3196-442d-9de5-bafaaa83b402"
}
```

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL – WhatsApp  \n  \nCONVERSATION ID - $(conversationId)  \n  \n  \\_ Conversation ID from the output variables of the Search Conversation  \n  \nDirection – Inbound/Outbound  \n  \nText – $(messageFromCustomer)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming message from the  customer.  \n  \n  \\_ Message text from end customer  \n  \nTimestamp - $(n2.whatsapp.ts)  \n  \n  \\_ Timestamp in UTC  \n  \nAttachments – $(parseDataAttachment)  \n  \n  \\* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively",
    "0-1": "TransId"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### FAQ###

**What should be done if messages containing special characters need to be passed to the Append Conversation node **

 To pass messages containing special characters to the Append Conversation node:

- Use an Evaluate node before the Append Conversation node.
- In the Evaluate node write the following script:  
  `Var_Response = Var_Response.replace(/[\\]/g, '\\\\').replace(/[\"]/g, '\\\"').replace(/[\/]/g, '\\/').replace(/[\b]/g, '\\b').replace(/[\f]/g, '\\f').replace(/[\n]/g, '\\n').replace(/[\r]/g, '\\r').replace(/[\t]/g, '\\t')`
- Use the 'Var_Response' variable in the Append Conversation node. The 'Var_Response' can be either TextResponse or aiResponse depending on the node from where the message is received.

For example, consider a scenari where your AI Agent provides a response that needs to be pasted back to the transcript. If the response contains special characters, then the system might display '400 Bad Request error'. In this case, use the Evaluate node in between the AI Agent node and the Append Conversation node. Paste the above script in the Evaluate node.