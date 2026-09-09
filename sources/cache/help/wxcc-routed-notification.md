# Routed Notification - WXCC

Source: https://help.webexconnect.io/docs/wxcc-routed-notification
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:15+00:00

This node calls Webex CC Routed Notification API to notify Webex CC whether adding an agent or participant to the conversation was successful or not. While configuring flows in Webex Connect, you’d need to use this node for notifying Webex CC about the participant/agent addition to conversation. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.   

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Routed Accept** 



![Screenshot of Routed Accepted configuration page.](https://files.readme.io/67d8acd-Routed_Accepted.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Routed Accepted | None |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onTaskRoutedFailure  <br>  _ onTaskRouted  <br>  \* onTimeout |






| Channel | Field Value |
| --- | --- |
| All channels | TASK ID - $(n2.webex.ID)  <br>ID - $(n2.webex.ID)  <br>AGENT ID - $(n2.webex.agentId)  <br>QUEUE ID - $(n2.webex.queue)  <br>MEDIA RESOURCE ID - $(mediaResourceId)  <br>MEDIA TYPE - $(n2.webex.mediaType) |






| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| TASK ID - $(n2.webex.ID)  <br>  <br>> \_ ID from the output variables of the routed event is the task IDID - $(n2.webex.ID)<br>><br>> \_ ID from the output variables of the routed event is the task IDAGENT ID - $(n2.webex.agentId)<br>><br>> \_ AgentId from the output variables of the routed event is the Agent IDQUEUE ID - $(n2.webex.queue)<br>><br>> \_ Queue from the output variables of the routed event is the Queue IDMEDIA RESOURCE ID - $(mediaResourceId)<br>><br>> \_ MediaResourceId from the output variables of the routed event is the Media Resource IDMEDIA TYPE - $(n2.webex.mediaType)<br>><br>> \_ MediaType from the output variables of the routed event is the Media Type | None | v1.1 and v1.0 |




> 📘 Note:
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

## Routed Rejected



![Screenshot of Routed Rejected configuration page.](https://files.readme.io/c385c59-Routed_Rejected.jpg)




**Method Name - Routed Reject** 



| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Routing Reject | None |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ onTaskRoutedFailure  <br>  _ onTaskRouted  <br>  \* onTimeout |






| Channel | Field Value |
| --- | --- |
| All channels | TASK ID - $(n2.webex.ID)  <br>ID - $(n2.webex.ID)  <br>AGENT ID - $(n2.webex.agentId)  <br>QUEUE ID - $(n2.webex.queue)  <br>MEDIA RESOURCE ID - $(mediaResourceId)  <br>MEDIA TYPE - $(n2.webex.mediaType)  <br>REASON - $(description)  <br>REASONCODE - $(code) |






| Input Variables | Output Variables |
| --- | --- |
| TASK ID - $(n2.webex.ID)  <br>  <br>> \_ ID from the output variables of the routed event is the task IDID - $(n2.webex.ID)<br>><br>> \_ ID from the output variables of the routed event is the task IDAGENT ID - $(n2.webex.agentId)<br>><br>> \_ AgentId from the output variables of the routed event is the Agent IdQUEUE ID - $(n2.webex.queue)<br>><br>> \_ Queue from the output variables of the routed event is the Queue IDMEDIA RESOURCE ID - $(mediaResourceId)<br>><br>> \_ MediaResourceId from the output variables of the routed event is the Media Resource IDMEDIA TYPE - $(n2.webex.mediaType)<br>><br>> \_ MediaType from the output variables of the routed event is the Media TypeREASON - $(description)<br>><br>> \_ $(description) will have the add participant failure reasonREASON CODE - $(code)<br>><br>> \_ $(code) will have the add participant failure reason code | None |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).