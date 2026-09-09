# Close Task - WXCC

Source: https://help.webexconnect.io/docs/wxcc-close-task
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:16+00:00

The close task is a global node. This node calls Webex CC Close task API to notify Webex CC whether closing a conversation was successful or not. While configuring flows in Webex Connect, you’d need to use this node for notifying Webex CC about the success/failure in closing a conversation. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

 **Method Name - Close Task Accept** 



![Screenshot of Close Task Accept configuration page](https://files.readme.io/669e9b6-Close_Task_Accept.jpg)






| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| TASK ID - $(n2.webex.taskId)  <br>  <br>  \_ ID from the output variables of the closed event is the task ID  <br>  <br>ID - $(n2.webex.taskId)  <br>  <br>  \_ ID from the output variables of the closed event is the task ID  <br>  <br>QUEUE ID - $(n2.webex.queue)  <br>  <br>  \_ Queue from the output variables of the closed event is the Queue ID  <br>  <br>CONVERSATION ID  <br>  <br>  \_ ID from the output variables of the closed event  <br>  <br>Media Type - $(mediaType)  <br>  <br>  \* The output variables of the closed event is the Media Type | None | v1.1 and v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Close Task Reject** 



![Screenshot of Close Task Reject configuration page.](https://files.readme.io/90ca145-Close_Task_Reject.jpg)






| Input Variable | Output Variable | Versions |
| --- | --- | --- |
| TASK ID - $(n2.webex.taskId)  <br>  <br>  \_ ID from the output variables of the closedevent is the task ID  <br>  <br>ID - $(n2.webex.taskId)  <br>  <br>  \_ ID from the output variables of the closed event is the task ID  <br>  <br>Agent ID - $(n2.webex.agent)  <br>  <br>  \_ Agent ID from the output variables of the closed event  <br>  <br>CONVERSATION ID- $(mediaResourceId)  <br>  <br>  \_ MediaResourceId from the output variables of the closed event is the Media Resource ID  <br>  <br>REASON - $(description)  <br>  <br>  \_ $(description) will have the close conversation failure reason  <br>  <br>Reason Code  <br>  <br>Contains the close conversation failure code  <br>  <br>Media Type - $(mediaType)  <br>  <br>  \_ The output variables of the closed event is the Media Type | None | v1.1 and v1.0 |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).

**Method Name - Close Task on WxCC** 



![Screenshot of Close Task on WxCC configuration page.](https://files.readme.io/b0b1411-Close_Task_On_WXCC.jpg)






| Input Variable | Output Variable | Versions |
| --- | --- | --- |
| TASK ID - $(n2.webex.taskId)  <br>  <br>  \_ ID from the output variables of the closed event is the task ID  <br>  <br>ID - $(n2.webex.taskId)  <br>  <br>  \_ ID from the output variables of the closed event is the task ID  <br>  <br>CONVERSATION ID- $(mediaResourceId)  <br>  <br>  \_ MediaResourceId from the output variables of the closed event is the Media Resource ID  <br>  <br>Media Type - $(mediaType)  <br>  <br>  \_ The output variables of the closed event is the Media Type | NA | v1.1 and v1.0 |

