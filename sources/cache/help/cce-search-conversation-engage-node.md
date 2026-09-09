# Search Conversation - CCE

Source: https://help.webexconnect.io/docs/cce-search-conversation-engage-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:23+00:00

This node calls Webex Engage Search Conversation API to check for existing conversations on Webex Engage. While configuring flows in Webex Connect, you’d need to use this node for searching for an existing conversation using the channel identifier such as PS Is, Email Id etc. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.   

## Methods and Outcomes 

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Search Conversation** 



![Interface section displaying the method name "Search Conversation".](https://files.readme.io/dbdf70e-Search.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Search Conversation |   _ description  <br>  _ conversationId  <br>  _ conversationExistsBool  <br>  _ status  |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ noConversationFound  <br>  _ conversationActive  <br>  _ conversationClosed  <br>  _ conversationInQueue  <br>  _ conversationOnHold  <br>  _ onTimeout  |






| Channel | Field Value |
| --- | --- |
| Facebook | FACEBOOK PAGE ID - $(FBpageid)  <br>FACEBOOK PS ID - $(n2.messenger.psId) |
| SMS | BUSINESS LONGCODE/SHORTCODE - $(n2.sms.serviceNumber)  <br>CUSTOMER MOBILE NUMBER - $(n2.sms.serviceNumber) |
| Email | BUSINESS EMAIL ID - $(n2.sms.serviceNumber)  <br>FROM EMAIL ID - $(n2.email.emailId)  <br>EMAIL SUBJECT - $(n2.email.subject)  <br>TO RECEPIENTS - $(n2.email.toAddresses)  <br>CC RECEPIENTS - $(n2.email.ccRecipients)  <br>INREPLY TO - $(modifiedInReplyTo) |
| LiveChat | CUSTOMER ADDRESS - $(n2.inappmessaging.userId)  <br>BIZ ADDRESS - IM28095016  <br>THREADID - $(n2.inappmessaging.threadId)  <br>LIVECHAT BROWSER FINGERPRINT - $(n2.inappmessaging.userId) |
| WhatsApp | WA BUSINESS ID - $(WANumber)  <br>CUSTOMER ID - $(n2.whatsapp.waId) |






| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – Facebook Messenger  <br>  <br>FACEBOOK PAGE ID - $(FBpageid)  <br>  <br>  \_ Messenger page Id is available in the Facebook section in the Assets section. When the flow is imported, the user must copy the Facebook page id from the assets section to the FBpageid custom variable  <br>  <br>FACEBOOK PS ID - $(n2.messenger.psId)  <br>  <br>  \_ psId from the output variables of the start node is the Facebook PS ID | description  <br>conversationId  <br>conversationExistsBool  <br>status |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 



| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – SMS  <br>  <br>BUSINESS LONGCODE/SHORTCODE  <br>  <br>- $(n2.sms.serviceNumber)  \_ ServiceNumber from the output variables of the start node is the Business longcode/shortcode  <br>  <br>CUSTOMER MOBILE NUMBER  <br>  <br>- $(n2.sms.msisdn)<br><br>  \_ Msisdn from the output variables of the start node is the customer mobile number | description  <br>conversationId  <br>conversationExistsBool  <br>status |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 



| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – Email  <br>  <br>BUSINESS EMAIL ID - $(bizemailid)  <br>  <br>  \_ email id is available in the email section in the Assets section. When the flow is imported, the user must copy the email id from the assets section to the bizemailid custom variable  <br>  <br>FROM EMAIL ID - $(n2.email.emailId)  <br>  <br>  \_ emailId in the output variables of the start node is from email id  <br>  <br>EMAIL SUBJECT - $(n2.email.subject)  <br>  <br>  \_ Subject in the output variables of the start node is the subject  <br>  <br>TO RECEPIENTS - $(n2.email.toAddresses)  <br>  <br>  \_ ToAddresses in the output variables of the start node is the To Recepients  <br>  <br>CC RECEPIENTS - $(n2.email.ccRecipients)  <br>  <br>  \_ CcRecepients in the output variables of the start node is the CC Recepients  <br>  <br>INREPLY TO - $(modifiedInReplyTo)  <br>  <br>  \_ ModifiedInReplyTo in the output variables of the start node is the In reply to | description  <br>conversationId  <br>conversationExistsBool  <br>status |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 



| Input Variables | Output Variables |
| --- | --- |
| CHANNEL – Livechat  <br>  <br>CUSTOMER ADDRESS - $(n2.inappmessaging.userId)  <br>  <br>  \_ UserId from the output variables of the start node is the Customer Address  <br>  <br>Live chat App Id – $(n2,inappmessaging.appId)  <br>  <br>  \_ BIZ address is available in the livechat section in the Assets section. When the flow is imported, the user must copy the livechat biz address id from the assets section to the livechatbizaddress custom variable  <br>  <br>THREADID - $(n2.inappmessaging.threadId)  <br>  <br>  \_ ThreadId from the output variables of the start node is the Thread Id  <br>  <br>LIVECHAT BROWSER FINGERPRINT - $(n2.inappmessaging.userId)  <br>  <br>  \_ UserId from the output variables of the start node is the Livechat Browser Fingerprint | description  <br>conversationId  <br>conversationExistsBool  <br>status |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Search Conversation** 



| Input Variables | Output  Variables |
| --- | --- |
| WA BUSINESS ID  <br>  <br>CUSTOMER ID | description  <br>conversationId  <br>conversationExistsBool  <br>status  <br>  <br>$(n2.whatsapp.waId) |

