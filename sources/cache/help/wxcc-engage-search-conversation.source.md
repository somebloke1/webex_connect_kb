This node calls imengage Search Conversation API to check for existing conversations on imiengage. While configuring flows in <<prodname>>, you’d need to use this node for searching for an existing conversation using the channel identifier such as PS Is, Email Id etc. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.   

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Search Conversation** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f4da2e7-Search_Conversation.jpg",
        null,
        "Screenshot of Search Conversion configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Search Conversion configuration page."
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
    "0-0": "Search Conversation",
    "0-1": "  _ conversationId  \n  _ aliasId  \n  _ conversationExistsBool  \n  _ status  \n  _ teamId  \n  _ userId  \n  _ apiStatus  \n  _ code  \n  _ description  \n  _ responsePayload ",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ noConversationFound  \n  _ conversationActive  \n  _ conversationClosed  \n  _ conversationInQueue  \n  _ conversationOnHold  \n  _ onTimeout "
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
    "0-0": "Facebook",
    "0-1": "FACEBOOK PAGE ID - $(FBpageid)  \nFACEBOOK PS ID - $(n2.messenger.psId)",
    "1-0": "SMS",
    "1-1": "BUSINESS LONGCODE/SHORTCODE - $(n2.sms.serviceNumber)  \nCUSTOMER MOBILE NUMBER - $(n2.sms.serviceNumber)",
    "2-0": "Email",
    "2-1": "BUSINESS EMAIL ID - $(n2.sms.serviceNumber)  \nFROM EMAIL ID - $(n2.email.emailId)  \nEMAIL SUBJECT - $(n2.email.subject)  \nTO RECEPIENTS - $(n2.email.toAddresses)  \nCC RECEPIENTS - $(n2.email.ccRecipients)  \nINREPLY TO - $(modifiedInReplyTo)",
    "3-0": "LiveChat",
    "3-1": "CUSTOMER ADDRESS - $(n2.inappmessaging.userId)  \nBIZ ADDRESS - IM28095016  \nTHREADID - $(n2.inappmessaging.threadId)  \nLIVECHAT BROWSER FINGERPRINT - $(n2.inappmessaging.userId)",
    "4-0": "WhatsApp",
    "4-1": "WA BUSINESS ID - $(WANumber)  \nCUSTOMER ID - $(n2.whatsapp.waId)"
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
    "h-2": "Versions",
    "0-0": "CHANNEL – Facebook Messenger  \n  \nFACEBOOK PAGE ID - $(FBpageid)  \n  \n  \\_ Messenger page Id is available in the Facebook section in the Assets section. When the flow is imported, the user must copy the Facebook page id from the assets section to the FBpageid custom variable  \n  \nFACEBOOK PS ID - $(n2.messenger.psId)  \n  \n  \\_ psId from the output variables of the start node is the Facebook PS ID",
    "0-1": "  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status ",
    "0-2": "The below Output variables are available in the v1.1  \n  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status  \n  \nThe The below Output variables are available in the v1.3  \n  _ conversationId  \n  _ aliasId  \n  _ conversationExistsBool  \n  _ status  \n  _ teamId  \n  _ userId  \n  _ apiStatus  \n  _ code  \n  _ description  \n  _ responsePayload"
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
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).

**Method Name - Search Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "CHANNEL – SMS  \n  \nBUSINESS LONGCODE/SHORTCODE  \n  \n- $(n2.sms.serviceNumber)  \\_ ServiceNumber from the output variables of the start node is the Business longcode/shortcode  \n  \nCUSTOMER MOBILE NUMBER  \n  \n- $(n2.sms.msisdn)\n\n  \\_ Msisdn from the output variables of the start node is the customer mobile number",
    "0-1": "  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status ",
    "0-2": "The below Output variables are available in the v1.1  \n  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status  \n  \nThe The below Output variables are available in the v1.3  \n  _ conversationId  \n  _ aliasId  \n  _ conversationExistsBool  \n  _ status  \n  _ teamId  \n  _ userId  \n  _ apiStatus  \n  _ code  \n  _ description  \n  _ responsePayload"
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
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "CHANNEL – Email  \n  \nBUSINESS EMAIL ID - $(bizemailid)  \n  \n  \\_ email id is available in the email section in the Assets section. When the flow is imported, the user must copy the email id from the assets section to the bizemailid custom variable  \n  \nFROM EMAIL ID - $(n2.email.emailId)  \n  \n  \\_ emailId in the output variables of the start node is from email id  \n  \nEMAIL SUBJECT - $(n2.email.subject)  \n  \n  \\_ Subject in the output variables of the start node is the subject  \n  \nTO RECEPIENTS - $(n2.email.toAddresses)  \n  \n  \\_ ToAddresses in the output variables of the start node is the To Recepients  \n  \nCC RECEPIENTS - $(n2.email.ccRecipients)  \n  \n  \\_ CcRecepients in the output variables of the start node is the CC Recepients  \n  \nINREPLY TO - $(modifiedInReplyTo)  \n  \n  \\_ ModifiedInReplyTo in the output variables of the start node is the In reply to",
    "0-1": "  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status ",
    "0-2": "The below Output variables are available in the v1.1  \n  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status  \n  \nThe The below Output variables are available in the v1.3  \n  _ conversationId  \n  _ aliasId  \n  _ conversationExistsBool  \n  _ status  \n  _ teamId  \n  _ userId  \n  _ apiStatus  \n  _ code  \n  _ description  \n  _ responsePayload"
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
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "CHANNEL – Livechat  \n  \nCUSTOMER ADDRESS - $(n2.inappmessaging.userId)  \n  \n  \\_ UserId from the output variables of the start node is the Customer Address  \n  \nLive chat App Id – $(n2,inappmessaging.appId)  \n  \n  \\_ BIZ address is available in the livechat section in the Assets section. When the flow is imported, the user must copy the livechat biz address id from the assets section to the livechatbizaddress custom variable  \n  \nTHREADID - $(n2.inappmessaging.threadId)  \n  \n  \\_ ThreadId from the output variables of the start node is the Thread Id  \n  \nLIVECHAT BROWSER FINGERPRINT - $(n2.inappmessaging.userId)  \n  \n  \\_ UserId from the output variables of the start node is the Livechat Browser Fingerprint",
    "0-1": "  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status ",
    "0-2": "The below Output variables are available in the v1.1  \n  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status  \n  \nThe The below Output variables are available in the v1.3  \n  _ conversationId  \n  _ aliasId  \n  _ conversationExistsBool  \n  _ status  \n  _ teamId  \n  _ userId  \n  _ apiStatus  \n  _ code  \n  _ description  \n  _ responsePayload"
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
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output  Variables",
    "h-2": "Versions",
    "0-0": "WA BUSINESS ID  \n  \nCUSTOMER ID - $(n2.whatsapp.waId)",
    "0-1": "_ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status",
    "0-2": "The below Output variables are available in the v1.1  \n  _ description  \n  _ conversationId  \n  _ conversationExistsBool  \n  _ status  \n  \nThe The below Output variables are available in the v1.3  \n  _ conversationId  \n  _ aliasId  \n  _ conversationExistsBool  \n  _ status  \n  _ teamId  \n  _ userId  \n  _ apiStatus  \n  _ code  \n  _ description  \n  _ responsePayload"
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