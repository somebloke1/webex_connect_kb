# End Task - CCE

Source: https://help.webexconnect.io/docs/cce-end-task
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:23+00:00

This node calls Contact Center Enterprise Close task API to notify Contact Center Enterprise about the success/failure in closing a conversation. While configuring flows in Webex Connect, you’d need to use this node for notifying Contact Center Enterprise about the success/failure in closing a conversation. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.



![Interface section showing the method name "End Task Details".](https://files.readme.io/f87d5d6-CCE_End_Task.jpg)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| \_ Method Name  <br>Name of the CCE task.  <br>  <br>\_ Tracking ID  <br>The Tracking ID used to track individual requests.  <br>  <br>\_ Domain - $(domain) One of the custom variables that must contain the finesse public accessible domain name for your business. A domain name is a string of text that maps to a numeric IP address, used to access a website from client software. Example: [www.google.com](http://www.google.com).  <br>  <br> **Task Details**  <br>  <br>   \_ Task ID - $(flid)  <br>Flow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. $(flid) is one of the custom variables that contains the processed task ID value which is evaluated in the Evaluate node.  <br>  <br>**Optional Variables**  <br>  <br>  \_ Call Variables - $(val1)  <br>Value of the call variable. Maximum allowed value length is up to 40 bytes.  <br>  <br>  \_ User Variables - $(val1)  <br>User variables consist of Key, Type, and Value.  <br>  <br>\_ Extension Variables - $(val1)  <br>Extension variables consist of Key, Type, and Value. | CCE End Task -  <br>_ location  <br>_ responsePayload | _ ok - 200 - Success  <br>_ Successfully Created - 201 - Success  <br>_ Forbidden - 403 - Erro  <br>_ Not Found - 404 - Error  <br>_ Internal Server Error - 500 - Error  <br>_ Bad Request - 400 - Error  <br>_ Unreachable - HTTP Status - 502 Error  <br>_ Service Unavailable - 503 - Error  <br>\* Task Already Exists - 20200 - Success |




**Method Name - Close Task** 



| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Close Task | None |   _ onInvalidData  <br>  _ onError  <br>  _ onInvalidChoice  <br>  _ onauthorizationfail  <br>  _ Error  <br>  _ Success  <br>  \* onTimeout |






| Channel | Field Value |
| --- | --- |
| All Channels | TASK ID - $(n2.webex.ID)  <br>ID - $(n2.webex.ID)  <br>QUEUE ID - $(n2.webex.queue)  <br>CONVERSATION ID - $(mediaResourceId) |

