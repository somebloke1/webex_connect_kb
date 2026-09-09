This node calls <<WebexCC>> Task API to create a new Task. While configuring flows in <<prodname>>, you’d need to use this node for creating the task on Webex CC.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Create Task** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e565816-Create_Task.jpg",
        null,
        "Screenshot of Create Task configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Create Task configuration page."
    }
  ]
}
[/block]


> 📘 Note
> 
> Based on the Channel you have selected, the Conversation ID will change accordingly.

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "h-3": "Versions",
    "0-0": "**TASK ID - $(flid) **  \n  \nFlow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id.  \n  \n**CONVERSATION ID - $(ConversationID) **  \n  \nConversation id from the create conversation node  \n  \n**DESTINATION **  \n  \n  _ Destination refers to the app id for the channel apps, and service number for SMS channel, which will be available as start node output variable  \n  _ For Facebook Messenger - destination is $(nodetid.messenger.appid)  \n  _ For Email – destination is $(nodetid.email.appid)  \n  _ For Livechat – destination is $(nodetid.inappmessaging.appid)  \n  _ For SMS – destination is $(nodetid.sms.serviceNumber)  \n  _ For WhatsApp WA  ID(ORIGIN) - desitnation is $(n2.whatsapp.waId)  \n  \n**MEDIA TYPE **  \n  \n  _ This field specifies the type of media on Webex CC while making task API call  \n  _ Media type can be selected from the dropdown  \n  _ For SMS and Facebook Messenger, media type is “Social”  \n  _ For Email. Media type is “Email”  \n  \\_ For Live chat, media is “Chat”  \n  \n**MEDIA CHANNEL**  \n  _ This field specifies the channel on Webex CC while making task API call  \n  _ Channel (Facebook Messenger, SMS, Email, Livechat and WhatsApp) can be selected from the dropdown  \n  \n**Subject**  \nThe subject line of the incoming email is to be mapped to this field. This field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'.  \n  \n**To Recipients**  \nThis field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'.  The values related to this field are received as part of the Start Node variables and is expected to be mapped here.  \n  \n**CC Recipients**  \nThis field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'. The values related to this field are received as part of the Start Node variables and is expected to be mapped here.  \n  \n**Has Attachments**  \nThis field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'. Please refer to this link for more information on [Media-specific Work Flow logic](https://github.com/CiscoDevNet/webexcc-digital-channels/tree/main/Webex%20Connect%20Flows/v3.4/Template/Media%20Specific%20Workflows).   \n  \n**CUSTOMER NAME - $(n2.messenger.name)  \n**  \n  _ Customer name is available in the output variables of start node  \n  _ For Facebook Messenger, customer name is $(n2.messenger.name)  \n  _ For SMS, customer name is $(n2.sms.senderNumber)  \n  _ For  Email , customer name is $(n2.email.senderName)  \n  _ For Livechat, customer name is $(n2.inappmessaging.name)  \n  _ For WhatsApp , customer name is $(n2.whatsapp.username)  \n  \n**CUSTOMER ID - $(n2.messenger.psId)**  \n  \n  _ Customer Ids available in the output variables of start node  \n  _ For Facebook Messenger, customer id is $(n2.messenger.psid)  \n  _ For SMS, customer id is $(n2.sms.senderNumber)  \n  _ For Email , customer id is $(n2.email.emailId)  \n  \\_ For Livechat, customer id is $(n2.inappmessaging.appid)  \n  \\* For WhatsApp, customer id is $(n2.whatsapp.waId)",
    "0-1": "Task ID  \n  \nConversation ID",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ Error  \n  _ Task failed  \n  _ created  \n  _ onTimeout ",
    "0-3": "v1.2 and v.1.0"
  },
  "cols": 4,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

> 📘 Version Upgrade
> 
> It is recommended for all users to move to the latest version that consists of simplified flows for hassle-free and optimal performance. The workaround suggested above for the ‘Has Attachments field’ is not necessary to be executed after the version upgrade.

## Sample configurations for various channels

> 📘 Note:
> 
> Below are the channel specific field. These will be applicable for the respective channels
> 
> FACEBOOK PS ID(ORIGIN) - $(n2.messenger.psId)  
> EMAIL ID(ORIGIN) - $(n2.email.emailId)  
> MOBILE NUMBER(ORIGIN) - $(n2.sms.senderNumber)  
> LIVECHAT USER ID(ORIGIN) - $(n2.livechat.userId)  
> WhatsApp WA  ID(ORIGIN) - $(n2.whatsapp.waId)

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Field Value",
    "0-0": "Messenger",
    "0-1": "TASK ID - $(flid)  \nCONVERSATION ID - $(conversationId)  \nDESTINATION - $(appid)  \nMEDIA TYPE - Social  \nMEDIA CHANNEL – Facebook Messenger  \nCUSTOMER NAME - $(n2.messenger.name)  \nCUSTOMER ID - $(n2.messenger.psId)  \nFACEBOOK PS ID(ORIGIN) - $(n2.messenger.psId)",
    "1-0": "SMS",
    "1-1": "TASK ID - $(flid)  \nCONVERSATION ID - $(conversationId)  \nDESTINATION - $(n2.sms.serviceNumber)  \nMEDIA TYPE - Social  \nMEDIA CHANNEL - SMS  \nCUSTOMER NAME - $(n2.sms.senderNumber)  \nCUSTOMER ID - $(n2.sms.senderNumber)  \nMobile Number(ORIGIN) - $(n2.sms.senderNumber)",
    "2-0": "Email",
    "2-1": "TASK ID - $(flid)  \nCONVERSATION ID - $(conversationId)  \nDESTINATION - $(n2.email.appId)  \nMEDIA TYPE - Email  \nMEDIA CHANNEL - Email  \nCUSTOMER NAME - $(n2.email.senderName)  \nCUSTOMER ID - $(n2.email.emailId)  \nEMAIL ID(ORIGIN) $(n2.email.emailId)  \nSubject $(n2.email.subject)",
    "3-0": "Live Chat",
    "3-1": "TASK ID - $(flid)  \nCONVERSATION ID - $(conversationId)  \nDESTINATION - $(n2.inappmessaging.appId)  \nMEDIA TYPE - Chat  \nMEDIA CHANNEL - Livechat  \nCHAT TYPE - Regular / Proactive  \nDIRECTION - Inbound / Outbound  \nCUSTOMER NAME - $(n38.inappmessaging.formFields.Name)  \nCUSTOMER ID - $(n38.inappmessaging.formFields.Email)  \nLIVECHAT USER ID (ORIGIN) - $(n38.inappmessaging.userId)",
    "4-0": "WhatsApp",
    "4-1": "TASK ID - $(n2.whatsapp.transId)  \nCONVERSATION ID - $(conversationId)  \nDESTINATION - $(n2.whatsapp.waId)  \nSource Number - $(sourceNumber)  \nMEDIA TYPE - Social  \nMEDIA CHANNEL - WhatsApp  \nCUSTOMER ID - $(n2.whatsapp.waId)  \nWhatsApp WA ID(Origin)- $(n2.whatsapp.waId)  \nCUSTOMER NAME - $(n2.whatsapp.username)"
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
> WhatsApp Source Number is "WhatsApp Business Number" without country code.  
> It is configured in flow using custom variable. For e.g., in this case we have created a custom variable with name 'sourceNumber' and it is passed as '$(sourceNumber)' in 'Source Number' field at Create Task node