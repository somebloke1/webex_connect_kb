# Re-Open Conversation - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-re-open-conversation
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:17+00:00

This node calls imengage Re-open Conversation API to re-open the closed conversation on imiengage. While configuring flows in Webex Connect, you’d need to use this node to re-open the conversation and queue it. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Re-Open Conversation** 



![Screenshot of Reopen Conversation configuration page.](https://files.readme.io/3c5f431-Re-open_Conversation.jpg)




**Method Name - Reopen Conversation** 



| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Reopen Conversation | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onFailure  <br>  _ ConversationReopened  <br>  _ ConversationReopenFailed  <br>  _ onTimeout  |




| Channel      | Field Value                            |
| :----------- | :------------------------------------- |
| All channels | CONVERSATION ID - $(n6.conversationId) |



| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| CONVERSATION ID – $(n6.conversationId)  <br>  <br>  \* Conversation id from the output variables of the search conversation node is the Conversation ID  | TransId | v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).