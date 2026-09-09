# Update  Conversation - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-update-conversation
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:17+00:00

This node calls imengage Update Conversation API to update the conversation on imiengage. While configuring flows in Webex Connect, you’d need to use this node for updating the conversation.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Update Conversation**



![Screenshot of Update Conversion configuration page.](https://files.readme.io/849a9f8-Update_Conversation.jpg)






| Method Name | Output  Variables | Node Outcomes |
| --- | --- | --- |
| Update Conversation | transID |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ Failure  <br>  _ onConversationUpdatedFailure  <br>  _ onConversationUpdatedSuccess  <br>  _ Success  <br>  \* onTimeout  |






| Input Variables | Output  Variables | Versions |
| --- | --- | --- |
| Conversation ID - $(mediaResourceId)  <br>  <br>MediaResourceId from the output variables of the evaluate node is the Conversation ID  <br>  <br>Task ID - $(flid)  <br>  <br>Flow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. | transID | v1.0 |

