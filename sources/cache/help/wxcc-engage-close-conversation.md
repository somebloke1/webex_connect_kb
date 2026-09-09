# Close Conversation - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-close-conversation
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:17+00:00

This node calls imengage Close Conversation API to close the conversation on imiengage. While configuring flows in Webex Connect, you’d need to use this node for closing the conversation.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods

**Method Name - Close Chat** 



![Screenshot of Close Conversation configuration page.](https://files.readme.io/0820917-Close_Conversation.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Close Chat | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onFailure  <br>  _ onCloseConversationFailure  <br>  _ onConversationClosed  <br>  _ onTimeout  |




| Channels     | Field Value                          |
| :----------- | :----------------------------------- |
| All channels | CONVERSATION ID - $(mediaResourceId) |



| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CONVERSATION ID – $(mediaResourceId)  <br>  <br>  \* MediaResourceId from the output variables of the evaluate node is the Conversation ID  | TransId | v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).