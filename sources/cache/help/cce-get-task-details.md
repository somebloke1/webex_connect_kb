# Get Task Details - CCE

Source: https://help.webexconnect.io/docs/cce-get-task-details
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:22+00:00

This node calls Contact Center Enterprise Task API to get details of a Task. While configuring flows in Webex Connect, you’d need to use this node for getting details of the task on Contact Center Enterprise.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Get Task Details** 



![Interface section showing the method name "Get Task Details".](https://files.readme.io/2f3b713-CC_Get_Task_Details.png)




> 📘 Note
> 
> Based on the Channel you have selected, the Conversation ID will change accordingly.



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| \_ Method Name  <br>Name of the CCE task.  <br>  <br>\_ Tracking ID  <br>The Tracking ID used to track individual requests.  <br>  <br>\_ Domain - $(domain) One of the custom variables that must contain the finesse public accessible domain name for your business. A domain name is a string of text that maps to a numeric IP address, used to access a website from client software. Example: [www.google.com](http://www.google.com).  <br>  <br> **Task Details**  <br>  <br> \_ Task ID - $(flid)  <br>Flow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. $(flid) is one of the custom variables that contains the processed task ID value which is evaluated in the Evaluate node. | _ preferredOwner  <br>_ taskId  <br>_ customerId  <br>_ origin  <br>_ destination  <br>_ mediaType  <br>_ mediaChannel  <br>_ state  <br>_ direction  <br>_ createdTime  <br>_ lastUpdatedTime  <br>_ scriptSelector  <br>_ variables  <br>_ history  <br>_ estimatedWaitTime  <br>_ responsePayload | _ ok - 200 - Success  <br>_ Successfully Created - 201 - Success  <br>_ Forbidden - 403 - Erro  <br>_ Not Found - 404 - Error  <br>_ Internal Server Error - 500 - Error  <br>_ Bad Request - 400 - Error  <br>_ Unreachable - HTTP Status - 502 Error  <br>_ Service Unavailable - 503 - Error  <br>\* Task Already Exists - 20200 - Success |

