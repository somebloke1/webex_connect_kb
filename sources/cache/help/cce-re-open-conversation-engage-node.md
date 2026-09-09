# Re-open Conversation - CCE

Source: https://help.webexconnect.io/docs/cce-re-open-conversation-engage-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:25+00:00

This node calls Webex Engage Re-open Conversation API to re-open the closed conversation on Webex Engage. While configuring flows in Webex Connect, you’d need to use this node to re-open the conversation and queue it. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Re-Open Converstation** 



![Interface section displaying the method name "Reopen Conversation"](https://files.readme.io/9859e51-update_conversation.png)




**Method Name - Close Conversation** 



| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Reopen Conversation | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onFailure  <br>  _ ConversationReopened  <br>  _ ConversationReopenFailed  <br>  _ onTimeout  |




| Channel      | Field Value                            |
| :----------- | :------------------------------------- |
| All channels | CONVERSATION ID - $(n6.conversationId) |



| Input Variables | Output Variables |
| --- | --- |
| CONVERSATION ID – $(n6.conversationId)  <br>  <br>  \* Conversation id from the output variables of the search conversation node is the Conversation ID  | TransId |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)