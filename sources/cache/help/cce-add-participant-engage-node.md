# Add Participant - CCE

Source: https://help.webexconnect.io/docs/cce-add-participant-engage-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:24+00:00

This node calls Webex Engage Add Participant API to add an agent to the conversation on Webex Engage. While configuring flows in Webex Connect, you’d need to use this node for adding the agent to the conversation. The agent details will be available from the routed event 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes 

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Add Participant** 



![Interface section displaying the method name "Add Participant"](https://files.readme.io/189b433-Add_Participant.jpg)






| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Add Participant | TransId |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ Failure  <br>  _ OnAddParticipantFailure  <br>  _ OnAddParticipantSuccess  <br>  _ Success  <br>  <br>- onTimeout  |






| Channel | Field Value |
| --- | --- |
| All channels | CONVERSATION ID - $(mediaResourceId)  <br>PARTICIPANT - $(n2.webex.agentId) |






| Input Variables | Output Variables |
| --- | --- |
| CONVERSATION ID – $(mediaResourceId)  <br>  <br>  \_ MediaResourceId from the output variables of the evaluate node is the Conversation ID  <br>  <br>PARTICIPANT - $(n2.webex.agentId)  <br>  <br>  \_ AgentId from the output variables of the start node is the participant |  |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)