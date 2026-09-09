# Create Conversation - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-create-conversation
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:16+00:00

This node calls imengage Create Conversation API to create conversation on imiengage. While configuring flows in Webex Connect, you’d need to use this node for creating a conversation with the customer and channel details

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Create Conversation** 



![Screenshot of Create Conversion configuration page.](https://files.readme.io/c8f6f24-LC_Create.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Create Conversation | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onTimeout  <br>  _ onauthorizationfail  <br>  _ Failure  <br>  _ onConversationCreated  <br>  _ onConversationFailed  |






| Channel | Field Value |
| --- | --- |
| Facebook Messenger | FACEBOOK PAGE ID - $(FBpageid)  <br>FACEBOOK PS ID - $(n2.messenger.psId)  <br>CUSTOMER NAME - $(n2.messenger.name)  <br>DIRECTION - Inbound  <br>MESSAGE TYPE - Text/text with attachments  <br>TEXT - $(n2.messenger.message)  <br>TIMESTAMP (IN UTC) - $(n2.messenger.ts) |
| SMS | BUSINESS LONGCODE/SHORTCODE - $(n2.sms.serviceNumber)  <br>CUSTOMER MOBILE NUMBER - $(n2.sms.senderNumber)  <br>CUSTOMER NAME - $(n2.sms.name)  <br>DIRECTION - Inbound  <br>TEXT - $(n2.sms.message)  <br>TIMESTAMP (IN UTC) - $(n2.sms.ts) |
| Email | BUSINESS EMAIL ID - $(bizemailid)  <br>FROM EMAIL ID - $(n2.email.emailId)  <br>DIRECTION – Inbound  <br>TIMESTAMP (IN UTC) - $(n2.email.timestamp)  <br>FROM ADDRESS - $(n2.email.emailId)  <br>TO RECEPIENTS - $(n2.email.toAddresses)  <br>CC RECEPIENTS - $(n2.email.ccRecipients)  <br>SUBJECT - $(n2.email.subject)  <br>EMAIL HEADERS - $(n2.email.headers)  <br>PLAIN BODY - $(messageStrippedText)  <br>HTML BODY - $(messageHTML)  <br>STRIPPED HTML - $(messageStrippedHTML)  <br>ATTACHMENTS - $(parsedattachments) |
| LiveChat | CUSTOMER NAME - Customer  <br>THREAD ID - $(n2.inappmessaging.threadId)  <br>LIVECHAT USER ID - $(n2.inappmessaging.userId)  <br>LIVECHAT APP ID - $(n2.inappmessaging.appId)  <br>LIVECHAT WEBSITE DOMAIN - Need to be configured in custom variables  <br>LIVECHAT PROACTIVE ID  - $(proactiveId) - Fetch this from `$(inappmessage.message.extras)`variable from the start node and parse the `proactive_id` field within an Evaluate node  <br>DIRECTION - Inbound, Outbound, Announcement  <br>MESSAGE TYPE - Text With Attachments  <br>TEXT - $(message)  <br>TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  <br>ATTACHMENTS - $(parseDataAttachment)  <br>LIVE CHAT WITH QUICK REPLIES  <br>LIVE CHAT WITH CAROUSALS |
| WhatsApp | WA BUSINESS ID - $(n2.whatsapp.waId)  <br>CUSTOMER NAME - $(n2.whatsapp.username)  <br>DIRECTION - Inbound  <br>MESSAGE TYPE - Text With Attachments  <br>TEXT - $(messageFromCustomer)  <br>TIMESTAMP (IN UTC) - $(n2.whatsapp.ts)  <br>ATTACHMENTS - $(parseDataAttachment) |






| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CHANNEL – Facebook  <br>  <br>DIRECTION – Inbound  <br>  <br>MESSAGE TYPE - Text With Attachments  <br>  <br>TEXT - $(messageFromCustomer)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming message from the  customer.  <br>  <br>TIMESTAMP (IN UTC) - $(n2.messenger.ts)  <br>  <br>  \_ Timestamp in the output variables of the start node which contains the Messenger Timestamp  <br>  <br>FACEBOOK PAGE ID - $(FBpageid)  <br>  <br>  \_ Messenger page Id is available in the Facebook section in the Assets section. When the flow is imported, the user must copy the Facebook page id from the assets section to the FBpageid custom variable  <br>  <br>FACEBOOK PS ID - $(n2.messenger.psId)  <br>	  <br>  \_ psId from the output variables of the start node is the Facebook PS ID  <br>  <br>CUSTOMER NAME - $(n2.messenger.name)  <br>  <br>  \_ name from the output variables of the start node is the Customer Name  <br>  <br>Attachments – $(parseDataAttachment)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively | TransId | v1.3, v1.2, and v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).



| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CHANNEL – SMS  <br>  <br>DIRECTION – Inbound  <br>  <br>TEXT - $(n2.sms.message)  <br>  <br>  \_ Message from the output variables of the start node which contains the message.  <br>  <br>TIMESTAMP (IN UTC) - $(n2.sms.ts)  <br>  <br>  \_ Timestamp in the output variables of the start node which contains the SMS Timestamp  <br>  <br>BUSINESS LONGCODE/SHORTCODE  <br>  <br>- $(n2.sms.serviceNumber)  \_ ServiceNumber from the output variables of the start node is the Business longcode/shortcodeCUSTOMER MOBILE NUMBER  <br>  <br>- $(n2.sms.msisdn)  \_ Msisdn from the output variables of the start node is the customer mobile numberCUSTOMER NAME  <br>  <br>- $(n2.sms.msisdn)  \* Msisdn from the output variables of the start node is the customer name | TransId | v1.3, v1.2, and v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)



| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CHANNEL – EMAIL  <br>  <br>BUSINESS EMAIL ID - $(bizemailid)  <br>  <br>  \_ email id is available in the email section in the Assets section. When the flow is imported, the user must copy the email id from the assets section to the bizemailid custom variable  <br>  <br>DIRECTION – Inbound  <br>  <br>FROM EMAIL ID - $(n2.email.emailId)  <br>  <br>  \_ emailId in the output variables of the start node is from email id  <br>  <br>EMAIL SUBJECT - $(n2.email.subject)  <br>  <br>  \_ Subject in the output variables of the start node is the subject  <br>  <br>TO RECEPIENTS - $(n2.email.toAddresses)  <br>  <br>  \_ ToAddresses in the output variables of the start node is the To Recepients  <br>  <br>CC RECEPIENTS - $(n2.email.ccRecipients)  <br>  <br>  \_ ccRecepients in the output variables of the start node is the CC Recepients  <br>  <br>TIMESTAMP (IN UTC) - $(n2.email.timestamp)  <br>  <br>  \_ ccRecepients in the output variables of the start node is the CC Recepients  <br>  <br>EMAIL HEADERS - $(n2.email.headers)  <br>  <br>  \_ ccRecepients in the output variables of the start node is the CC Recepients  <br>  <br>PLAIN BODY - $(messageStrippedText)  <br>  <br>  \_ messageStrippedText in the custom variables is the Plain body  <br>  <br>HTML BODY - $(messageHTML)  <br>  <br>  \_ MessageHTML in the custom variables is the HTML body  <br>  <br>STRIPPED HTML - $(messageStrippedHTML)  <br>  <br>  \_ messageStrippedHTML in the custom variables is the Stripped HTML  <br>  <br>ATTACHMENTS - $(parsedattachments)  <br>  <br>  \* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively | TransId | v1.3, v1.2, and v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

> 📘 Note
> 
> Live Chat Create Conversation has two versions 1.0 and 1.2



| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CHANNEL – LIVE CHAT  <br>  <br>CUSTOMER NAME - Customer  <br>  <br>  \_ message in the custom variables is the message  <br>  <br>THREAD ID - $(n2.inappmessaging.threadId)  <br>  <br>  \_ ThreadId in the start node output variables is the Thread Id  <br>  <br>LIVE CHAT USER ID - $(n2.inappmessaging.userId)  <br>  <br>  \_ User Id in the output variables of the start node is the Livechat user Id  <br>  <br>LIVE CHAT APP ID - $(n2.inappmessaging.appId)  <br>  <br>  \_ AppId in the output variables of the start node is the Live Chat App Id  <br>  <br>LIVE CHAT WEBSITE DOMAIN  <br>  <br>  \_ Website domain in which the Live Chat widget is embedded. The website domain is available in the app settings page.  <br>  <br>DIRECTION – Inbound  <br>  <br>MESSAGE TYPE -  <br>_ Text With Attachments  <br>_ Live Chat Form Response  <br>\_ Live Chat with Carousel Response - If ‘Live Chat Carousel Response’ is selected it displays two fields: Live Chat Carousel Response object (JSON or flow variable) and Timestamp  <br>  <br>\_ Live Chat with Quick Replies Response - If ‘Live Chat Quick Replies Response’ is selected it displays two fields: Live Chat Quick Replies Response object (JSON or flow variable) and Timestamp  <br>  <br>Live Chat Quick Replies Response Object/Live Chat Carousels Response Object: $(Inappmessaging.postback)  <br>  <br>DIRECTION – Outbound  <br>  <br>MESSAGE TYPE -  <br>  <br>\_ Text With Attachments  <br>  <br>\_ Live Chat Text with Carousel  <br>  <br>- If ‘Text with carousel’ is selected it displays three fields: Text (String or flow variable), Carousel object (expected value: JSON or flow variable) and Timestamp\_ Live Chat Text with Quick Replies - If ‘Text with quick replies' selected it displays three fields: Text (String or flow variable), Quick replies object (expected value: JSON or flow variable) and TimestampDIRECTION - Announcement  <br>  _ Text  <br>  _ TimeStamp  <br>  <br>Live Chat Quick Replies Object/Live Chat Carousels Object: $(send.template) or $(send.quickreplies)  <br>  <br>TEXT - $(message)  <br>  <br>  _ message in the custom variables is the message  <br>  _ $(send.text) (Quick Replies or Carousal)  <br>  <br>TIMESTAMP (IN UTC) -  <br>  <br>  \_ Timestamp in the output variables of the start node which contains the Live Chat Timestamp  <br>  <br>ATTACHMENTS - $(parseDataAttachment)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively  <br>  <br>CONVERSATION ID - $(n6.conversationId) (Here, n6 is the respective node ID)  <br>  <br>  \_ Conversation from the output variables of the Search Conversation is the Conversation ID  <br>DIRECTION – Inbound  <br>  <br>MESSAGE TYPE - Text With Attachments  <br>  <br>TEXT - $(message)  <br>  <br>  _ message in the custom variables is the message  <br>  _ $(send.text) (Quick Replies or Carousal)  <br>  <br>TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  <br>  <br>  \_ $(n2.inappmessaging.timestamp) in the custom variables is the Timestamp  <br>  <br>ATTACHMENTS - $(parseDataAttachment)  <br>  <br>  \_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively  <br>  <br>DIRECTION – Announcement  <br>  <br>TEXT - $(message)  <br>  <br>  \_ message in the custom variables is the message  <br>  <br>  \_ TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  <br>  <br>` \_ Timestamp in the output variables of the start node which contains the Live Chat Timestamp` | TransId | Text With Attachments, Live Chat Form Response, Live Chat Carousel Response,  <br>Live Chat Quick Replies Response are available in v1.2 for Inbound Direction  <br>  <br>Text With Attachments, Live Chat Text With Carousel, Live Chat Text With Quick Replies are available in v1.2 for Outbound Direction  <br>  <br>Announcement is available in v1.2 |




> 📘 Note:
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)



| Input Variables | Output Variables | Versions  |
| --- | --- | --- |
| CHANNEL - WhatsApp  <br>  <br>  \_ WA Business ID - $(WANumber)  <br>  <br>  \_ CUSTOMER ID - $(n2.whatsapp.waId)  <br>  <br>  \_ CUSTOMER NAME - $(n2.whatsapp.username)  <br>  <br>  \_ Direction – Inbound/Outbound  <br>  <br>  \_ Message type – Text with Attachments  <br>  <br>  \_ Text – $(messageFromCustomer)  <br>  <br>` \_ This is one of the Evaluate node variables which contains the processed incoming message from the  customer.`  \_ Timestamp - $(n2.whatsapp.ts)  <br>  <br>` \_ Timestamp in the output variables of the start node which contains the WhatsApp Timestamp`  \_ Attachments – $(parseDataAttachment)  <br>  <br>` \* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively` | TransId | v1.3, v1.2, and v1.0 |

