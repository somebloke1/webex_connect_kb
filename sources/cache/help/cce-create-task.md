# Create Task - CCE

Source: https://help.webexconnect.io/docs/cce-create-task
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:22+00:00

This node calls Contact Center Enterprise Task API to create a new Task. While configuring flows in Webex Connect, you’d need to use this node for creating the task on Contact Center Enterprise.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Create Task** 



![ Interface section displaying the method name "Create Task".](https://files.readme.io/2f86c77-CCE_Create_Task_1.png)




> 📘 Note
> 
> Based on the Channel you have selected, the Conversation ID will change accordingly.



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| \_ Method Name  <br>Name of the CCE task.  <br>  <br>\_ Tracking ID  <br>The Tracking ID used to track individual requests.  <br>  <br>\_ Domain - $(domain) One of the custom variables that must contain the finesse public accessible domain name for your business. A domain name is a string of text that maps to a numeric IP address, used to access a website from client software. Example: [www.google.com](http://www.google.com).  <br>  <br> **Task Details**  <br>  <br>   \_ Task ID - $(flid)  <br>Flow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. $(flid) is one of the custom variables that contains the processed task ID value which is evaluated in the Evaluate node.  <br>  <br>- Disposition Code - The unique identifier for the type of conversation between the customer and the live agent. \_ Conversation ID - $(conversationId) - This is async variable from the Create Conversation node. This variable automatically gets available in Webex Connect platform once create conversation executed with success. \_ Destination - $(destination) One of the custom variables that must contain the value for customer's identifier. For example, the value of "PSID" in case of Facebook Messenger, "MSISDN" in case of SMS channel, and so on for other channels. Destination the customer contacted. For telephony, this is the number the contact called. For chat, this is the URL of the page where the chat takes place. For email, it is the email address contacted. \_ Media Type  <br>      Media type of the task. Acceptable values are email \| chat \| telephony \| social \| Web Callback For SMS, the media type is - Social. The Media Type for Email is 'Email', for Live chat, the Media Type is 'Chat', and for Callbacks, the Media Type is 'Telephony', and for Web Callback it is 'Web Callback'. \_ Media Channel  <br>    Media channel of the task. Eg. For a Social media type, the mediaChannel could be Facebook. Acceptable values for different media types are as follows:- Media Type Valid Media Channels - email, telephony, voice chat, chat, social, facebook messenger, sms, WhatsApp, and Web Callback.\_ Preferred Owner - $(preferredOwner) - One of the custom variable that must contain the relevant agent ID  <br>  The Preferred Agent ID of the Agent to whom the task should be assigned to. This is the Agent Skill Target ID in CCE.\_ Script Selector - $(scriptSelector)  <br>Information that is used to select a routing script for the task  <br>  <br>**Customer Details**  <br>  <br>\_ Customer ID  <br>Identification for the customer  <br>  <br>\_ Mobile Number (Origin)  <br>Customer's mobile number  <br>  <br>\_ Customer Name  <br>Customer's name  <br>  <br>**Optional Variables**  <br>  <br>  \_ Call Variables - $(val1)  <br>Value of the call variable. Maximum allowed value length is up to 40 bytes.  <br>  <br>  \_ User Variables - $(val1)  <br>User variables consist of Key, Type, and Value.  <br>  <br>\_ Extension Variables - $(val1)  <br>Extension variables consist of Key, Type, and Value. | CCE Create Task -  <br>_ location  <br>_ responsePayload | _ ok - 200 - Success  <br>_ Successfully Created - 201 - Success  <br>_ Forbidden - 403 - Erro  <br>_ Not Found - 404 - Error  <br>_ Internal Server Error - 500 - Error  <br>_ Bad Request - 400 - Error  <br>_ Unreachable - HTTP Status - 502 Error  <br>_ Service Unavailable - 503 - Error  <br>\* Task Already Exists - 20200 - Success |




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



| Channel | Field Value |
| --- | --- |
| SMS | Task ID - $(flid)  <br>Conversation ID - $(conversationId)  <br> Destination - $(n2.sms.serviceNumber)  <br> Media Type - Social  <br> Media Channel - SMS  <br> Preferred Owner - $(1100)  <br> Script Selector - $(ScriptSelector)  <br>Customer Details  <br>Customer ID -$(n2.sms.senderNumber)  <br> Mobile Number (Origin) - $(n2.sms.senderNumber)  <br> Customer Name - $(n2.sms.senderNumber)  <br>  <br>- Call Variables -<br>- User Variables - |
| Facebook Messenger | Task ID - $(flid)  <br>  Conversation ID - $(conversationId)  <br>  Destination - $(n2.messenger.appId)  <br>  Media Type - Social  <br>  Media Channel - Facebook Messenger  <br>  Preferred Owner - $(0000)  <br>  Script Selector - $(ScriptSelector)  <br>Customer Details  <br>  Customer ID - $(n2.messenger.psId)  <br>  Customer Name - $(CustomerName)  <br>  Facebook Messenger PS Id - $(n2.messenger.psId)  <br>Call Variables -  <br>User Variables -  <br>Extension Variables -  <br>  <br>- Key -  facebookID<br>- Value - $(n2.messenger.psId) |
| WhatsApp | Task ID - $(flid)  <br>  Conversation ID - $(conversationId)  <br>  Destination - $(n2.whatsapp.appId)  <br>  Media Type - Social  <br>  Media Channel - WhatsApp  <br>  Preferred Owner - $(0000)  <br>  Script Selector - $(ScriptSelector)  <br>Customer Details  <br>  Customer ID - $(n2.whatsapp.waId)  <br>  WhatsApp WA Id - $(n2.whatsapp.waId)  <br>  Customer Name - $(customerName)  <br>  Call Variables -  <br>  User Variables - |
| Email | Task ID - $(flid)  <br>  Conversation ID - $(conversationId)  <br>  Destination - $(n2.email.appId)  <br>  Media Type - Email  <br>  Media Channel - Email  <br>  Preferred Owner - $(0000)  <br>  Script Selector - Insurance  <br>Customer Details  <br>  Customer ID - $(n2.email.emailId)  <br>  Customer Name - $(n2.email.senderName)  <br>  $(n2.email.senderName) - $(n2.email.emailId)  <br>Call Variables -  <br>User Variables -  <br>_ Key - \_DR_EmailSubject  <br>_ Type - String  <br>Value - $(n2.email.subject) |
| Live Chat | Task ID - $(flid)  <br>  Conversation ID - $(conversationId)  <br>  Destination - $(n2.inappmessaging.appId)  <br>  Media Type - Chat  <br>  Media Channel - Live Chat/In App Messaging  <br>  Preferred Owner - $(0000)  <br>  Script Selector - $(n38.inappmessaging.formFields.Query)  <br>Customer Details  <br>  Customer ID - $(n38.inappmessaging.formFields.Email)  <br>  Mobile Number (Origin) -  <br>  Customer Name - $(n38.inappmessaging.formFields.Name)  <br>Live Chat User Id (Origin)- $(n2.inappmessaging.userId)  <br>Call Variables -  <br>User Variables  <br>_ Type - String  <br>_ Value - $(n2.inappmessaging.threadId) |
| Web Calback | Task ID - $(taskid_Callback)  <br>  Conversation ID - $(conversationId)  <br>  Destination - $(n2.inappmessaging.appId)  <br>  Media Type - Web Callback  <br>  Media Channel - Web Callback  <br>  Preferred Owner - $(0000)  <br>  Script Selector - $(ScriptSelector)\_Callback  <br>Customer Details  <br>  Customer ID - $(CustomerID)  <br>  Phone Number (Origin) -  $(CustomerPhoneNumber)  <br>  Customer Name - $(CustomerName)  <br>Call Variables -  <br>User Variables  <br>Extension Variables  <br>  LiveChatUserId (Origin)- $(ChatuserID)  <br>  LiveChatThread - $(ChatThreadID)  <br>  LiveChatAppID - $(aphid)  <br>Type - String |
| Apple Messages for Business | Task ID - $(flid)  <br>  Conversation ID - $(conversationId)  <br>  Destination - $(n2.abc.appId)  <br>  Media Type - Social  <br>  Media Channel – Apple Messages for Business  <br>  Preferred Owner -  $(0000)  <br>  Script Selector - $(ScriptSelector)  <br>Customer Details  <br>  Customer ID - $(n2.abc.abcUserId)  <br>  Apple Business for Messages User Id(Origin)- $(n2.abc.abcUserId)  <br>Call Variables - $(customerName)  <br>User Variables - |

