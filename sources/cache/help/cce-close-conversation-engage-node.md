# Close Conversation - CCE

Source: https://help.webexconnect.io/docs/cce-close-conversation-engage-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:24+00:00

This node calls Webex Engage Close Conversation API to close the conversation on Webex Engage. While configuring flows in Webex Connect, you’d need to use this node for closing the conversation.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes 

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods

**Method Name - Close Chat** 



![Interface section displaying the method name "Close Conversation".](https://files.readme.io/966f420-Close_Chat.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Send Plain Test Message | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onFailure  <br>  _ onCloseConversationFailure  <br>  _ onConversationClosed  <br>  _ onTimeout  |




| Channels     | Field Value                          |
| :----------- | :----------------------------------- |
| All channels | CONVERSATION ID - $(mediaResourceId) |



| Input Variables | Output Variables |
| --- | --- |
| CONVERSATION ID – $(mediaResourceId)  <br>  <br>- MediaResourceId from the output variables of the evaluate node is the Conversation ID  | TransId |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)