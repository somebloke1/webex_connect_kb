# Append Conversation - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-append-conversation
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:16+00:00

This node calls imengage Append Conversation API to append the message to an existing conversation on imiengage. While configuring flows in Webex Connect, you’d need to use this node for appending a message from the end-user to an existing conversation. So that the same will be reflected in the agent desktop.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. .  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Append Conversation** 



![Screenshot of Append Conversion configuration page.](https://files.readme.io/3ef896b-LC_Append.jpg)




> 📘 
> 
> In the tables below, "n6" refers to the respective node ID.



| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Append conversation | TransId | _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ Failure  <br>  _ onAppendMessageFailure  <br>  _ onAppendMessageSuccess  <br>  _ onTimeout |






| Channel | Field Value |
| --- | --- |
| Facebook Messenger | CHANNEL - Facebook  <br>CONVERSATION ID - $(n6.conversationId)  <br>DIRECTION - Inbound  <br>MESSAGE TYPE - Text With Attachments  <br>TEXT - $(n2.messenger.message)  <br>TIMESTAMP (IN UTC) - $(n2.messenger.ts) |
| SMS | CHANNEL - SMS  <br>CONVERSATION ID - $(n6.conversationId)  <br>DIRECTION - Inbound  <br>TEXT - $(n2.sms.message)  <br>TIMESTAMP (IN UTC) - $(n2.sms.ts) |
| Email | CONVERSATION ID - $(n6.conversationId)  <br>DIRECTION – Inbound  <br>TIMESTAMP (IN UTC) - $(n2.email.timestamp)  <br>FROM ADDRESS - $(n2.email.emailId)  <br>TO RECEPIENTS - $(n2.email.toAddresses)  <br>CC RECEPIENTS - $(n2.email.ccRecipients)  <br>SUBJECT - $(n2.email.subject)  <br>EMAIL HEADERS - $(n2.email.headers)  <br>PLAIN BODY - $(messageStrippedText)  <br>HTML BODY - $(messageHTML)  <br>STRIPPED HTML - $(messageStrippedHTML)  <br>ATTACHMENTS - $(parseDataAttachments) |
| Live Chat | CHANNEL - Live Chat  <br>CONVERSATION ID - $(n6.conversationId)  <br>DIRECTION - Inbound, Outbound, Announcement  <br>  <br>Direction Inbound - MESSAGE TYPE -  <br>                                   - Text  <br>                                   - Text With Attachments  <br>                                   - Live Chat Form Response  <br>                                   - Live Chat Carousel Response  <br>                                   - Live Chat Quick Replies  <br>                                      Response  <br>  <br>Direction Outbound - MESSAGE TYPE -  <br>                                      - Text With Attachments  <br>                                      - Live Chat Text with Carousel  <br>                                      - Live Chat  Text with Quick  <br>                                         Replies  <br>  <br>Direction Announcement - Text  <br>                                           - TIMESTAMP (IN UTC)  <br>  <br>TEXT - $(message)  <br>  <br>TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  <br>  <br>ATTACHMENTS - $(parseDataAttachment)  <br>  <br>QUICK REPLIES (Inbound) - $(n2.Inappmessaging.postback)  <br>  <br>CAROUSALS (Inbound) - $(n2.Inappmessaging.postback)  <br>  <br>QUICK REPLIES (Outbound) -  $(n<nodeId>.send.quickreplies)  <br>  <br>CAROUSALS (Outbound) - $(n<nodeId>.send.template) |
| WhatsApp | CHANNEL - WhatsApp  <br>  <br>Conversation ID - $(conversationId)  <br>  <br>TEXT - $(messageFromCustomer)  <br>  <br>TIMESTAMP (IN UTC) - $(n2.whatsapp.ts)  <br>  <br>ATTACHMENTS - $(parseDataAttachment) |




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



| Input Variables | Output Variable |
| --- | --- |
| CHANNEL – Facebook Messenger  <br>  <br>CONVERSATION ID - $(n6.conversationId)  <br>  <br>  \_ Conversation from the output variables of the Search Conversation is the Conversation ID  <br>  <br>DIRECTION – Inbound  <br>  <br>TEXT - $(messageFromCustomer)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming message object from customer respectively  <br>  <br>  \_ Message from the output variables of the start node is the message. The message will be appended to the conversation  <br>  <br>TIMESTAMP (IN UTC) - $(n2.messenger.ts)  <br>  <br>  \_ $(n2.messenger.ts) is the timestamp of the message  <br>  <br>ATTACHMENT - $(parseDataAttachment)  <br>  <br>  \* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively | TransId |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).

**Method Name - Append Conversation** 



| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – SMS  <br>  <br>CONVERSATION ID - $(n6.conversationId)  <br>  <br>•	Conversation from the output variables of the Search Conversation is the Conversation ID  <br>DIRECTION – Inbound  <br>  <br>TEXT - $(n2.sms.message)  <br>  <br>•	Message from the output variables of the start node is the message. The message will be appended to the conversation  <br>  <br>TIMESTAMP (IN UTC) - $(n2.sms.ts)  <br>  <br>•	$(n2.sms.ts) is the timestamp of the message  <br>  <br>Note: when the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable.  <br>  <br>Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber) | TransId |




**Method Name - Append Conversation** 



| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – EMAIL  <br>  <br>CONVERSATION ID - $(n6.conversationId)  <br>  <br>  \_ Conversation from the output variables of the Search Conversation is the Conversation ID  <br>  <br>DIRECTION – Inbound  <br>  <br>FROM EMAIL ID - $(n2.email.emailId)  <br>  <br>  \_ emailId in the output variables of the start node is from email id  <br>  <br>EMAIL SUBJECT - $(n2.email.subject)  <br>  <br>  \_ Subject in the output variables of the start node is the subject  <br>  <br>TO RECEPIENTS - $(n2.email.toAddresses)  <br>  <br>  \_ ToAddresses in the output variables of the start node is the To Recepients  <br>  <br>CC RECEPIENTS - $(n2.email.ccRecipients)  <br>  <br>  \_ ccRecepients in the output variables of the start node is the CC Recepients  <br>  <br>TIMESTAMP (IN UTC) - $(n2.email.timestamp)  <br>  <br>  \_ Timestamp in the output variables of the start node which contains the Email Timestamp  <br>  <br>EMAIL HEADERS - $(n2.email.headers)  <br>  <br>  \_ Email Headersvin the output variables of the start node is the Email Headers  <br>  <br>PLAIN BODY - $(messageStrippedText)  <br>  <br>  \_ messageStrippedText in the custom variables is the Plain body  <br>  <br>HTML BODY - $(messageHTML)  <br>  <br>  \_ MessageHTML in the custom variables is the HTML body  <br>  <br>STRIPPED HTML - $(messageStrippedHTML)  <br>  <br>  \_ messageStrippedHTML in the custom variables is the Stripped HTML  <br>  <br>ATTACHMENT - $(parseDataAttachment)  <br>  <br>  \* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively | TransId |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Append Conversation** 

> 📘 Note
> 
> Append Conversation has two versions 1.0 and 1.3



| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CHANNEL – LIVECHAT  <br>  <br>CONVERSATION ID - $(n6.conversationId) (Here, n6 is the respective node ID)  <br>  <br>  \_ Conversation from the output variables of the Search Conversation is the Conversation ID  <br>  <br>DIRECTION – Inbound  <br>  <br>MESSAGE TYPE -  <br>_ Text  <br>_ Text With Attachments  <br>_ Live Chat Form Response  <br>_ Live Chat with Carousel Response  <br>\_ Live Chat with Quick Replies Response  <br>  <br>Live Chat Quick Replies Response Object/Live Chat Carousels Response Object: $(Inappmessaging.postback)  <br>  <br>DIRECTION – Outbound  <br>  <br>MESSAGE TYPE -  <br>_ Text With Attachments  <br>_ Live Chat Text with Carousel  <br>\_ Live Chat Text with Quick Replies  <br>  <br>Live Chat Quick Replies Object/Live Chat Carousels Object: $(n<nodeId>.send.template) or $(n<nodeId>.send.quickreplies)  <br>  <br>ATTACHMENT - $(parseDataAttachment)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively  <br>  <br>TEXT - $(message)  <br>  <br>  \_ message is one of the custom variables which contains the message  <br>  <br>TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  <br>  <br>  \_ $(n2.inappmessaging.timestamp) is one of the start node variables which contains the Timestamp  <br>  <br>DIRECTION – Announcement  <br>  <br>TEXT - $(message)  <br>  <br>  \_ message is one of the custom variable which contains the message  <br>  <br>TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  <br>  \_ Timestamp in the output variables of the start node which contains the Timestamp  <br>  <br>  \* $(n2.inappmessaging.timestamp) is one of the start node variables which contains the Timestamp | TransId | Text With Attachments, Live Chat Carousel Response,  <br>Live Chat Quick Replies Response are available in v1.3 for Inbound Direction  <br>  <br>Text With Attachments, Live Chat Text With Carousel, Live Chat Text With Quick Replies are available in v1.3 for Outbound Direction  <br>  <br>Announcement is available in v1.3 |




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



| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – WhatsApp  <br>  <br>CONVERSATION ID - $(conversationId)  <br>  <br>  \_ Conversation ID from the output variables of the Search Conversation  <br>  <br>Direction – Inbound/Outbound  <br>  <br>Text – $(messageFromCustomer)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming message from the  customer.  <br>  <br>  \_ Message text from end customer  <br>  <br>Timestamp - $(n2.whatsapp.ts)  <br>  <br>  \_ Timestamp in UTC  <br>  <br>Attachments – $(parseDataAttachment)  <br>  <br>  \* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively | TransId |

