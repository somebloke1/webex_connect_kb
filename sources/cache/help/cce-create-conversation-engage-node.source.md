This node calls Webex Engage Create Conversation API to create conversation on Webex Engage. While configuring flows in <<prodname>>, you’d need to use this node for creating a conversation with the customer and channel details

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Create Conversation** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c8f6f24-LC_Create.jpg",
        "LC Create.jpg",
        "Interface section displaying the method name \"Create Conversation\"."
      ],
      "align": "center",
      "border": true,
      "caption": "Interface section displaying the method name \"Create Conversation\"."
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
    "0-0": "Create Conversation",
    "0-1": "TransId",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onTimeout  \n  _ onauthorizationfail  \n  _ Failure  \n  _ onConversationCreated  \n  _ onConversationFailed "
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
    "0-1": "FACEBOOK PAGE ID - $(FBpageid)  \nFACEBOOK PS ID - $(n2.messenger.psId)  \nCUSTOMER NAME - $(n2.messenger.name)  \nDIRECTION - Inbound  \nMESSAGE TYPE - Text/text with attachments  \nTEXT - $(n2.messenger.message)  \nTIMESTAMP (IN UTC) - $(n2.messenger.ts)",
    "1-0": "SMS",
    "1-1": "BUSINESS LONGCODE/SHORTCODE - $(n2.sms.serviceNumber)  \nCUSTOMER MOBILE NUMBER - $(n2.sms.senderNumber)  \nCUSTOMER NAME - $(n2.sms.name)  \nDIRECTION - Inbound  \nTEXT - $(n2.sms.message)  \nTIMESTAMP (IN UTC) - $(n2.sms.ts)",
    "2-0": "Email",
    "2-1": "BUSINESS EMAIL ID - $(bizemailid)  \nFROM EMAIL ID - $(n2.email.emailId)  \nDIRECTION – Inbound  \nTIMESTAMP (IN UTC) - $(n2.email.timestamp)  \nFROM ADDRESS - $(n2.email.emailId)  \nTO RECEPIENTS - $(n2.email.toAddresses)  \nCC RECEPIENTS - $(n2.email.ccRecipients)  \nSUBJECT - $(n2.email.subject)  \nEMAIL HEADERS - $(n2.email.headers)  \nPLAIN BODY - $(messageStrippedText)  \nHTML BODY - $(messageHTML)  \nSTRIPPED HTML - $(messageStrippedHTML)  \nATTACHMENTS - $(parsedattachments)",
    "3-0": "LiveChat",
    "3-1": "CUSTOMER NAME - Customer  \nTHREAD ID - $(n2.inappmessaging.threadId)  \nLIVECHAT USER ID - $(n2.inappmessaging.userId)  \nLIVECHAT APP ID - $(n2.inappmessaging.appId)  \nLIVECHAT WEBSITE DOMAIN - Need to be configured in custom variables  \nDIRECTION - Inbound, Outbound, Announcement  \nMESSAGE TYPE - Text With Attachments  \nTEXT - $(message)  \nTIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  \nATTACHMENTS - $(parseDataAttachment)  \nLIVE CHAT WITH QUICK REPLIES  \nLIVE CHAT WITH CAROUSALS",
    "4-0": "WhatsApp",
    "4-1": "WA BUSINESS ID - $(n2.whatsapp.waId)  \nCUSTOMER NAME - $(n2.whatsapp.username)  \nDIRECTION - Inbound  \nMESSAGE TYPE - Text With Attachments  \nTEXT - $(messageFromCustomer)  \nTIMESTAMP (IN UTC) - $(n2.whatsapp.ts)  \nATTACHMENTS - $(parseDataAttachment)"
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL – Facebook  \n  \nDIRECTION – Inbound  \n  \nMESSAGE TYPE - Text With Attachments  \n  \nTEXT - $(messageFromCustomer)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming message from the  customer.  \n  \nTIMESTAMP (IN UTC) - $(n2.messenger.ts)  \n  \n  \\_ Timestamp in the output variables of the start node which contains the Messenger Timestamp  \n  \nFACEBOOK PAGE ID - $(FBpageid)  \n  \n  \\_ Messenger page Id is available in the Facebook section in the Assets section. When the flow is imported, the user must copy the Facebook page id from the assets section to the FBpageid custom variable  \n  \nFACEBOOK PS ID - $(n2.messenger.psId)  \n\t  \n  \\_ psId from the output variables of the start node is the Facebook PS ID  \n  \nCUSTOMER NAME - $(n2.messenger.name)  \n  \n  \\_ name from the output variables of the start node is the Customer Name  \n  \nAttachments – $(parseDataAttachment)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively",
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

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL – SMS  \n  \nDIRECTION – Inbound  \n  \nTEXT - $(n2.sms.message)  \n  \n  \\_ Message from the output variables of the start node which contains the message.  \n  \nTIMESTAMP (IN UTC) - $(n2.sms.ts)  \n  \n  \\_ Timestamp in the output variables of the start node which contains the SMS Timestamp  \n  \nBUSINESS LONGCODE/SHORTCODE  \n  \n- $(n2.sms.serviceNumber)  \\_ ServiceNumber from the output variables of the start node is the Business longcode/shortcode  \n  \nCUSTOMER MOBILE NUMBER  \n  \n- $(n2.sms.msisdn)  \\_ Msisdn from the output variables of the start node is the customer mobile number  \n  \nCUSTOMER NAME  \n  \n- $(n2.sms.msisdn)  \\* Msisdn from the output variables of the start node is the customer name",
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

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL – EMAIL  \n  \nBUSINESS EMAIL ID - $(bizemailid)  \n  \n  \\_ email id is available in the email section in the Assets section. When the flow is imported, the user must copy the email id from the assets section to the bizemailid custom variable  \n  \nDIRECTION – Inbound  \n  \nFROM EMAIL ID - $(n2.email.emailId)  \n  \n  \\_ emailId in the output variables of the start node is from email id  \n  \nEMAIL SUBJECT - $(n2.email.subject)  \n  \n  \\_ Subject in the output variables of the start node is the subject  \n  \nTO RECEPIENTS - $(n2.email.toAddresses)  \n  \n  \\_ ToAddresses in the output variables of the start node is the To Recepients  \n  \nCC RECEPIENTS - $(n2.email.ccRecipients)  \n  \n  \\_ ccRecepients in the output variables of the start node is the CC Recepients  \n  \nTIMESTAMP (IN UTC) - $(n2.email.timestamp)  \n  \n  \\_ ccRecepients in the output variables of the start node is the CC Recepients  \n  \nEMAIL HEADERS - $(n2.email.headers)  \n  \n  \\_ ccRecepients in the output variables of the start node is the CC Recepients  \n  \nPLAIN BODY - $(messageStrippedText)  \n  \n  \\_ messageStrippedText in the custom variables is the Plain body  \n  \nHTML BODY - $(messageHTML)  \n  \n  \\_ MessageHTML in the custom variables is the HTML body  \n  \nSTRIPPED HTML - $(messageStrippedHTML)  \n  \n  \\_ messageStrippedHTML in the custom variables is the Stripped HTML  \n  \nATTACHMENTS - $(parsedattachments)  \n  \n  \\* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively",
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

> 📘 Note
> 
> Live Chat Create Conversation has two versions 1.0 and 1.2

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "CHANNEL – LIVE CHAT  \n  \nCUSTOMER NAME - Customer  \n  \n  \\_ message in the custom variables is the message  \n  \nTHREAD ID - $(n2.inappmessaging.threadId)  \n  \n  \\_ ThreadId in the start node output variables is the Thread Id  \n  \nLIVE CHAT USER ID - $(n2.inappmessaging.userId)  \n  \n  \\_ User Id in the output variables of the start node is the Livechat user Id  \n  \nLIVE CHAT APP ID - $(n2.inappmessaging.appId)  \n  \n  \\_ AppId in the output variables of the start node is the Live Chat App Id  \n  \nLIVE CHAT WEBSITE DOMAIN  \n  \n  \\_ Website domain in which the Live Chat widget is embedded. The website domain is available in the app settings page.  \n  \nDIRECTION – Inbound  \n  \nMESSAGE TYPE -  \n_ Text With Attachments  \n_ Live Chat Form Response  \n\\_ Live Chat with Carousel Response - If ‘Live Chat Carousel Response’ is selected it displays two fields: Live Chat Carousel Response object (JSON or flow variable) and Timestamp  \n  \n\\_ Live Chat with Quick Replies Response - If ‘Live Chat Quick Replies Response’ is selected it displays two fields: Live Chat Quick Replies Response object (JSON or flow variable) and Timestamp  \n  \nLive Chat Quick Replies Response Object/Live Chat Carousels Response Object: $(Inappmessaging.postback)  \n  \nDIRECTION – Outbound  \n  \nMESSAGE TYPE -  \n  \n\\_ Text With Attachments  \n  \n\\_ Live Chat Text with Carousel  \n  \n- If ‘Text with carousel’ is selected it displays three fields: Text (String or flow variable), Carousel object (expected value: JSON or flow variable) and Timestamp\\_ Live Chat Text with Quick Replies - If ‘Text with quick replies' selected it displays three fields: Text (String or flow variable), Quick replies object (expected value: JSON or flow variable) and Timestamp  \n  \nDIRECTION - Announcement  \n  _ Text  \n  _ TimeStamp  \n  \nLive Chat Quick Replies Object/Live Chat Carousels Object: $(send.template) or $(send.quickreplies)  \n  \nTEXT - $(message)  \n  \n  _ message in the custom variables is the message  \n  _ $(send.text) (Quick Replies or Carousal)  \n  \nTIMESTAMP (IN UTC) -  \n  \n  \\_ Timestamp in the output variables of the start node which contains the Live Chat Timestamp  \n  \nATTACHMENTS - $(parseDataAttachment)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively  \n  \nCONVERSATION ID - $(n6.conversationId) (Here, n6 is the respective node ID)  \n  \n  \\_ Conversation from the output variables of the Search Conversation is the Conversation ID  \nDIRECTION – Inbound  \n  \nMESSAGE TYPE - Text With Attachments  \n  \nTEXT - $(message)  \n  \n  _ message in the custom variables is the message  \n  _ $(send.text) (Quick Replies or Carousal)  \n  \nTIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  \n  \n  \\_ $(n2.inappmessaging.timestamp) in the custom variables is the Timestamp  \n  \nATTACHMENTS - $(parseDataAttachment)  \n  \n  \\_ This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively  \n  \nDIRECTION – Announcement  \n  \nTEXT - $(message)  \n  \n  \\_ message in the custom variables is the message  \n  \n  \\_ TIMESTAMP (IN UTC) - $(n2.inappmessaging.timestamp)  \n  \n```\n \\_ Timestamp in the output variables of the start node which contains the Live Chat Timestamp\n```",
    "0-1": "TransId",
    "0-2": "Text With Attachments, Live Chat Form Response, Live Chat Carousel Response,  \nLive Chat Quick Replies Response are available in v1.2 for Inbound Direction  \n  \nText With Attachments, Live Chat Text With Carousel, Live Chat Text With Quick Replies are available in v1.2 for Outbound Direction  \n  \nAnnouncement is available in v1.2"
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


> 📘 Note:
> 
> When the variable is selected from the previous node output variables, the nodeid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CHANNEL - WhatsApp  \n  \n  \\_ WA Business ID - $(WANumber)  \n  \n  \\_ CUSTOMER ID - $(n2.whatsapp.waId)  \n  \n  \\_ CUSTOMER NAME - $(n2.whatsapp.username)  \n  \n  \\_ Direction – Inbound/Outbound  \n  \n  \\_ Message type – Text with Attachments  \n  \n  \\_ Text – $(messageFromCustomer)  \n  \n```\n \\_ This is one of the Evaluate node variables which contains the processed incoming message from the  customer.\n```  \\_ Timestamp - $(n2.whatsapp.ts)  \n  \n```\n \\_ Timestamp in the output variables of the start node which contains the WhatsApp Timestamp\n```  \\_ Attachments – $(parseDataAttachment)  \n  \n```\n \\* This is one of the Evaluate node variables which contains the processed incoming attachment array object from customer respectively\n```",
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