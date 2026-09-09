# Modify Notification - WXCC

Source: https://help.webexconnect.io/docs/wxcc-modify-notification
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:15+00:00

This node calls Webex CC Modify Notification API to notify Webex CC whether conferencing or transferring an agent or participant to the conversation was successful or not. While configuring flows in Webex Connect, you’d need to use this node for notifying Webex CC about the agent conference/transfer status. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. .  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Modified Accept** 



![Screenshot of Modified Accept configuration page.](https://files.readme.io/1e85be2-Modify_Accept.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Modified Accept | None | _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onTimeout  <br>  _ onModifiedAcceptSuccess  <br>  \* onModifiedFailure |






| Channel | Field Value |
| --- | --- |
| All channels | TASK ID - $(n2.webex.ID)  <br>ID - $(n2.webex.ID)  <br>AGENT ID - $(n2.webex.agentId)  <br>QUEUE ID - $(n2.webex.queue)  <br>MEDIA RESOURCE ID - $(mediaResourceId)  <br>MEDIA TYPE - $(n2.webex.mediaType) |






| Input Variable | Output Variable | Versions |
| --- | --- | --- |
| TASK ID - $(n2.webex.ID)  <br>  <br>  \* ID from the output variables of the modified event is the task ID | None | V1.1 and v1.0 |
| ID - $(n2.webex.ID)  <br>  <br>  \* ID from the output variables of the modified event is the task ID  |  |  |
| AGENT ID - $(n2.webex.agentId)  <br>  <br>  \* AgentId from the output variables of the modified event is the Agent ID |  |  |
| QUEUE ID - $(n2.webex.queue)  <br>  <br>  \* Queue from the output variables of the modified event is the Queue ID |  |  |
| MEDIA RESOURSE ID - $(mediaResourceId)  <br>  <br>  \* MediaResourceId from the output variables of the modified event is the Media Resource ID |  |  |
| MEDIA TYPE - $(n2.webex.mediaType)  <br>  <br>  \* MediaType from the output variables of the modified event is the Media Type |  |  |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Modified Reject** 



![Screenshot of Modified Reject configuration page.](https://files.readme.io/fa977c3-Modify_Reject.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Modified Reject | None | _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onModifiedRejectFailure  <br>  _ onModifiedRejectSuccess  <br>  \* onTimeout |






| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| TASK ID - $(n2.webex.ID)  <br>  <br>  \* ID from the output variables of the modified event is the task ID | None | V1.1 and v1.0 |
| ID - $(n2.webex.ID)  <br>  <br>  \* ID from the output variables of the modified event is the task ID |  |  |
| AGENT ID - $(n2.webex.agentId)  <br>  <br>  \* AgentId from the output variables of the modified event is the Agent ID |  |  |
| QUEUE ID - $(n2.webex.queue)  <br>  <br>  \* Queue from the output variables of the modified event is the Queue ID  |  |  |
| MEDIA RESOURSE ID - $(mediaResourceId)  <br>  <br>  \* MediaResourceId from the output variables of the modified event is the Media Resource ID |  |  |
| MEDIA TYPE - $(n2.webex.mediaType)  <br>  <br>  \* MediaType from the output variables of the modified event is the Media Type |  |  |
| REASON - $(description)  <br>  <br>  \* $(description) will have the add/remove participant failure reason |  |  |
| REASON CODE - $(code)  <br>  <br>  \* $(code) will have the add/remove participant failure reason code |  |  |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).