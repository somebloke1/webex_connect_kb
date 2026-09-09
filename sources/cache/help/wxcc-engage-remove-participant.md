# Remove Participant - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-remove-participant
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:17+00:00

This node calls imengage RemoveParticipant API to remove an agent from the conversation on imiengage. While configuring flows in Webex Connect, you’d need to use this node for removing the agent from the conversation. The agent details will be available from the “Modified event “.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.   

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Remove Participant ** 



![Screenshot of Removing a participant configuration page.](https://files.readme.io/5dafd5b-Remove_Paticipant.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Remove Participant | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onFailure  <br>  _ onRemoveParticipantFailure  <br>  _ onParticipantRemoved  <br>  _ onTimeout  |






| Channel | Field Value |
| --- | --- |
| All channels | CONVERSATION ID - $(mediaResourceId)  <br>PARTICIPANT - $(n2.webex.agentId) |




**Method Name - Remove Participant** 



| Input Variables | Output Variables |
| --- | --- |
| CONVERSATION ID – $(mediaResourceId)  <br>  <br>  \_ MediaResourceId from the output variables of the evaluate node is the Conversation ID  <br>  <br>PARTICIPANT - $(n2.webex.agentId)  <br>  <br>  \_ AgentId from the output variables of the start node is the participant | TransId |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).