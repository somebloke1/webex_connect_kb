# Create Task - WXCC

Source: https://help.webexconnect.io/docs/wxcc-create-task
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:15+00:00

This node calls Cisco Webex Contact Center Task API to create a new Task. While configuring flows in Webex Connect, you’d need to use this node for creating the task on Webex CC.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Create Task** 



![Screenshot of Create Task configuration page.](https://files.readme.io/e565816-Create_Task.jpg)




> 📘 Note
> 
> Based on the Channel you have selected, the Conversation ID will change accordingly.



| Input Variables | Output Variables | Node Outcomes | Versions |
| --- | --- | --- | --- |
| **TASK ID - $(flid) **  <br>  <br>Flow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id.  <br>  <br>**CONVERSATION ID - $(ConversationID) **  <br>  <br>Conversation id from the create conversation node  <br>  <br>**DESTINATION **  <br>  <br>  _ Destination refers to the app id for the channel apps, and service number for SMS channel, which will be available as start node output variable  <br>  _ For Facebook Messenger - destination is $(nodetid.messenger.appid)  <br>  _ For Email – destination is $(nodetid.email.appid)  <br>  _ For Livechat – destination is $(nodetid.inappmessaging.appid)  <br>  _ For SMS – destination is $(nodetid.sms.serviceNumber)  <br>  _ For WhatsApp WA  ID(ORIGIN) - desitnation is $(n2.whatsapp.waId)  <br>  <br>**MEDIA TYPE **  <br>  <br>  _ This field specifies the type of media on Webex CC while making task API call  <br>  _ Media type can be selected from the dropdown  <br>  _ For SMS and Facebook Messenger, media type is “Social”  <br>  _ For Email. Media type is “Email”  <br>  \_ For Live chat, media is “Chat”  <br>  <br>**MEDIA CHANNEL**  <br>  _ This field specifies the channel on Webex CC while making task API call  <br>  _ Channel (Facebook Messenger, SMS, Email, Livechat and WhatsApp) can be selected from the dropdown  <br>  <br>**Subject**  <br>The subject line of the incoming email is to be mapped to this field. This field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'.  <br>  <br>**To Recipients**  <br>This field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'.  The values related to this field are received as part of the Start Node variables and is expected to be mapped here.  <br>  <br>**CC Recipients**  <br>This field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'. The values related to this field are received as part of the Start Node variables and is expected to be mapped here.  <br>  <br>**Has Attachments**  <br>This field appears only when the option selected in the 'MEDIA TYPE' and 'MEDIA CHANNEL' field is 'Email'. Please refer to this link for more information on [Media-specific Work Flow logic](https://github.com/CiscoDevNet/webexcc-digital-channels/tree/main/Webex%20Connect%20Flows/v3.4/Template/Media%20Specific%20Workflows).   <br>  <br>**CUSTOMER NAME - $(n2.messenger.name)  <br>**  <br>  _ Customer name is available in the output variables of start node  <br>  _ For Facebook Messenger, customer name is $(n2.messenger.name)  <br>  _ For SMS, customer name is $(n2.sms.senderNumber)  <br>  _ For  Email , customer name is $(n2.email.senderName)  <br>  _ For Livechat, customer name is $(n2.inappmessaging.name)  <br>  _ For WhatsApp , customer name is $(n2.whatsapp.username)  <br>  <br>**CUSTOMER ID - $(n2.messenger.psId)**  <br>  <br>  _ Customer Ids available in the output variables of start node  <br>  _ For Facebook Messenger, customer id is $(n2.messenger.psid)  <br>  _ For SMS, customer id is $(n2.sms.senderNumber)  <br>  _ For Email , customer id is $(n2.email.emailId)  <br>  \_ For Livechat, customer id is $(n2.inappmessaging.appid)  <br>  \* For WhatsApp, customer id is $(n2.whatsapp.waId) | Task ID  <br>  <br>Conversation ID |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ Error  <br>  _ Task failed  <br>  _ created  <br>  _ onTimeout  | v1.2 and v.1.0 |




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



| Channel | Field Value |
| --- | --- |
| Messenger | TASK ID - $(flid)  <br>CONVERSATION ID - $(conversationId)  <br>DESTINATION - $(appid)  <br>MEDIA TYPE - Social  <br>MEDIA CHANNEL – Facebook Messenger  <br>CUSTOMER NAME - $(n2.messenger.name)  <br>CUSTOMER ID - $(n2.messenger.psId)  <br>FACEBOOK PS ID(ORIGIN) - $(n2.messenger.psId) |
| SMS | TASK ID - $(flid)  <br>CONVERSATION ID - $(conversationId)  <br>DESTINATION - $(n2.sms.serviceNumber)  <br>MEDIA TYPE - Social  <br>MEDIA CHANNEL - SMS  <br>CUSTOMER NAME - $(n2.sms.senderNumber)  <br>CUSTOMER ID - $(n2.sms.senderNumber)  <br>Mobile Number(ORIGIN) - $(n2.sms.senderNumber) |
| Email | TASK ID - $(flid)  <br>CONVERSATION ID - $(conversationId)  <br>DESTINATION - $(n2.email.appId)  <br>MEDIA TYPE - Email  <br>MEDIA CHANNEL - Email  <br>CUSTOMER NAME - $(n2.email.senderName)  <br>CUSTOMER ID - $(n2.email.emailId)  <br>EMAIL ID(ORIGIN) $(n2.email.emailId)  <br>Subject $(n2.email.subject) |
| Live Chat | TASK ID - $(flid)  <br>CONVERSATION ID - $(conversationId)  <br>DESTINATION - $(n2.inappmessaging.appId)  <br>MEDIA TYPE - Chat  <br>MEDIA CHANNEL - Livechat  <br>CHAT TYPE - Regular / Proactive  <br>DIRECTION - Inbound / Outbound  <br>CUSTOMER NAME - $(n38.inappmessaging.formFields.Name)  <br>CUSTOMER ID - $(n38.inappmessaging.formFields.Email)  <br>LIVECHAT USER ID (ORIGIN) - $(n38.inappmessaging.userId) |
| WhatsApp | TASK ID - $(n2.whatsapp.transId)  <br>CONVERSATION ID - $(conversationId)  <br>DESTINATION - $(n2.whatsapp.waId)  <br>Source Number - $(sourceNumber)  <br>MEDIA TYPE - Social  <br>MEDIA CHANNEL - WhatsApp  <br>CUSTOMER ID - $(n2.whatsapp.waId)  <br>WhatsApp WA ID(Origin)- $(n2.whatsapp.waId)  <br>CUSTOMER NAME - $(n2.whatsapp.username) |




> 📘 Note
> 
> WhatsApp Source Number is "WhatsApp Business Number" without country code.  
> It is configured in flow using custom variable. For e.g., in this case we have created a custom variable with name 'sourceNumber' and it is passed as '$(sourceNumber)' in 'Source Number' field at Create Task node