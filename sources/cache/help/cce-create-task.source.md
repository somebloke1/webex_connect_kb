This node calls Contact Center Enterprise Task API to create a new Task. While configuring flows in <<prodname>>, you’d need to use this node for creating the task on Contact Center Enterprise.

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
        "https://files.readme.io/2f86c77-CCE_Create_Task_1.png",
        "CCE_Create_Task_1.png",
        " Interface section displaying the method name \"Create Task\"."
      ],
      "align": "center",
      "caption": " Interface section displaying the method name \"Create Task\"."
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
    "0-0": "\\_ Method Name  \nName of the CCE task.  \n  \n\\_ Tracking ID  \nThe Tracking ID used to track individual requests.  \n  \n\\_ Domain - $(domain) One of the custom variables that must contain the finesse public accessible domain name for your business. A domain name is a string of text that maps to a numeric IP address, used to access a website from client software. Example: [www.google.com](http://www.google.com).  \n  \n **Task Details**  \n  \n   \\_ Task ID - $(flid)  \nFlow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. $(flid) is one of the custom variables that contains the processed task ID value which is evaluated in the Evaluate node.  \n  \n- Disposition Code - The unique identifier for the type of conversation between the customer and the live agent. \\_ Conversation ID - $(conversationId) - This is async variable from the Create Conversation node. This variable automatically gets available in Webex Connect platform once create conversation executed with success. \\_ Destination - $(destination) One of the custom variables that must contain the value for customer's identifier. For example, the value of \"PSID\" in case of Facebook Messenger, \"MSISDN\" in case of SMS channel, and so on for other channels. Destination the customer contacted. For telephony, this is the number the contact called. For chat, this is the URL of the page where the chat takes place. For email, it is the email address contacted. \\_ Media Type  \n      Media type of the task. Acceptable values are email | chat | telephony | social | Web Callback For SMS, the media type is - Social. The Media Type for Email is 'Email', for Live chat, the Media Type is 'Chat', and for Callbacks, the Media Type is 'Telephony', and for Web Callback it is 'Web Callback'. \\_ Media Channel  \n    Media channel of the task. Eg. For a Social media type, the mediaChannel could be Facebook. Acceptable values for different media types are as follows:- Media Type Valid Media Channels - email, telephony, voice chat, chat, social, facebook messenger, sms, WhatsApp, and Web Callback.\\_ Preferred Owner - $(preferredOwner) - One of the custom variable that must contain the relevant agent ID  \n  The Preferred Agent ID of the Agent to whom the task should be assigned to. This is the Agent Skill Target ID in CCE.\\_ Script Selector - $(scriptSelector)  \nInformation that is used to select a routing script for the task  \n  \n**Customer Details**  \n  \n\\_ Customer ID  \nIdentification for the customer  \n  \n\\_ Mobile Number (Origin)  \nCustomer's mobile number  \n  \n\\_ Customer Name  \nCustomer's name  \n  \n**Optional Variables**  \n  \n  \\_ Call Variables - $(val1)  \nValue of the call variable. Maximum allowed value length is up to 40 bytes.  \n  \n  \\_ User Variables - $(val1)  \nUser variables consist of Key, Type, and Value.  \n  \n\\_ Extension Variables - $(val1)  \nExtension variables consist of Key, Type, and Value.",
    "0-1": "CCE Create Task -  \n_ location  \n_ responsePayload",
    "0-2": "_ ok - 200 - Success  \n_ Successfully Created - 201 - Success  \n_ Forbidden - 403 - Erro  \n_ Not Found - 404 - Error  \n_ Internal Server Error - 500 - Error  \n_ Bad Request - 400 - Error  \n_ Unreachable - HTTP Status - 502 Error  \n_ Service Unavailable - 503 - Error  \n\\* Task Already Exists - 20200 - Success"
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


> 📘 
> 
> Note:
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

## Sample configurations for various channels

> 📘 Note:
> 
> Below are the channel specific field. These will be applicable for the respective channels
> 
> EMAIL ID(ORIGIN) - $(n2.email.emailId)  
> MOBILE NUMBER(ORIGIN) - $(n2.sms.senderNumber)  
> LIVECHAT USER ID(ORIGIN) - $(n2.livechat.userId)

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Field Value",
    "0-0": "SMS",
    "0-1": "Task ID - $(flid)  \nConversation ID - $(conversationId)  \n Destination - $(n2.sms.serviceNumber)  \n Media Type - Social  \n Media Channel - SMS  \n Preferred Owner - $(1100)  \n Script Selector - $(ScriptSelector)  \nCustomer Details  \nCustomer ID -$(n2.sms.senderNumber)  \n Mobile Number (Origin) - $(n2.sms.senderNumber)  \n Customer Name - $(n2.sms.senderNumber)  \n  \n- Call Variables -\n- User Variables -",
    "1-0": "Facebook Messenger",
    "1-1": "Task ID - $(flid)  \n  Conversation ID - $(conversationId)  \n  Destination - $(n2.messenger.appId)  \n  Media Type - Social  \n  Media Channel - Facebook Messenger  \n  Preferred Owner - $(0000)  \n  Script Selector - $(ScriptSelector)  \nCustomer Details  \n  Customer ID - $(n2.messenger.psId)  \n  Customer Name - $(CustomerName)  \n  Facebook Messenger PS Id - $(n2.messenger.psId)  \nCall Variables -  \nUser Variables -  \nExtension Variables -  \n  \n- Key -  facebookID\n- Value - $(n2.messenger.psId)",
    "2-0": "WhatsApp",
    "2-1": "Task ID - $(flid)  \n  Conversation ID - $(conversationId)  \n  Destination - $(n2.whatsapp.appId)  \n  Media Type - Social  \n  Media Channel - WhatsApp  \n  Preferred Owner - $(0000)  \n  Script Selector - $(ScriptSelector)  \nCustomer Details  \n  Customer ID - $(n2.whatsapp.waId)  \n  WhatsApp WA Id - $(n2.whatsapp.waId)  \n  Customer Name - $(customerName)  \n  Call Variables -  \n  User Variables -",
    "3-0": "Email",
    "3-1": "Task ID - $(flid)  \n  Conversation ID - $(conversationId)  \n  Destination - $(n2.email.appId)  \n  Media Type - Email  \n  Media Channel - Email  \n  Preferred Owner - $(0000)  \n  Script Selector - Insurance  \nCustomer Details  \n  Customer ID - $(n2.email.emailId)  \n  Customer Name - $(n2.email.senderName)  \n  $(n2.email.senderName) - $(n2.email.emailId)  \nCall Variables -  \nUser Variables -  \n_ Key - \\_DR_EmailSubject  \n_ Type - String  \nValue - $(n2.email.subject)",
    "4-0": "Live Chat",
    "4-1": "Task ID - $(flid)  \n  Conversation ID - $(conversationId)  \n  Destination - $(n2.inappmessaging.appId)  \n  Media Type - Chat  \n  Media Channel - Live Chat/In App Messaging  \n  Preferred Owner - $(0000)  \n  Script Selector - $(n38.inappmessaging.formFields.Query)  \nCustomer Details  \n  Customer ID - $(n38.inappmessaging.formFields.Email)  \n  Mobile Number (Origin) -  \n  Customer Name - $(n38.inappmessaging.formFields.Name)  \nLive Chat User Id (Origin)- $(n2.inappmessaging.userId)  \nCall Variables -  \nUser Variables  \n_ Type - String  \n_ Value - $(n2.inappmessaging.threadId)",
    "5-0": "Web Calback",
    "5-1": "Task ID - $(taskid_Callback)  \n  Conversation ID - $(conversationId)  \n  Destination - $(n2.inappmessaging.appId)  \n  Media Type - Web Callback  \n  Media Channel - Web Callback  \n  Preferred Owner - $(0000)  \n  Script Selector - $(ScriptSelector)\\_Callback  \nCustomer Details  \n  Customer ID - $(CustomerID)  \n  Phone Number (Origin) -  $(CustomerPhoneNumber)  \n  Customer Name - $(CustomerName)  \nCall Variables -  \nUser Variables  \nExtension Variables  \n  LiveChatUserId (Origin)- $(ChatuserID)  \n  LiveChatThread - $(ChatThreadID)  \n  LiveChatAppID - $(aphid)  \nType - String",
    "6-0": "Apple Messages for Business",
    "6-1": "Task ID - $(flid)  \n  Conversation ID - $(conversationId)  \n  Destination - $(n2.abc.appId)  \n  Media Type - Social  \n  Media Channel – Apple Messages for Business  \n  Preferred Owner -  $(0000)  \n  Script Selector - $(ScriptSelector)  \nCustomer Details  \n  Customer ID - $(n2.abc.abcUserId)  \n  Apple Business for Messages User Id(Origin)- $(n2.abc.abcUserId)  \nCall Variables - $(customerName)  \nUser Variables -"
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]