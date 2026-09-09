# Queue Task - WXCC

Source: https://help.webexconnect.io/docs/wxcc-queue-task
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:15+00:00

This node calls Webex CC Queue Task API to queue the contact at Webex CC. While configuring flows in Webex Connect, you’d need to use this node for queuing the contact on Webex CC. Flow developer can configure the Skill based routing setting by selecting the appropriate skills and values on the node.

> 👍 Important
> 
> If you have a scenario where multiple Queue Task nodes are required-such as in a Webex Contact Center (WxCC) flow where user input determines whether the call should be routed to a billing agent, account agent, login agent, or general query agent-you may need to use several Queue Task nodes. In these cases, we recommend creating separate sub-flow from branch that leads to a Queue Task node. Then, use the "Call Workflow" node to invoke these sub-flows from your main flow.
> 
> Key benefits:  
> 	1.	Reduces the overall complexity of your main flow.  
> 	2.	Makes the flow design cleaner and more organized.  
> 	3.	Clearly separates repetitive tasks from the main business logic.  
> 	4.	Helps reduce the total flow size. Since the maximum allowed flow size is 10 MB, we recommend keeping your flow size below this limit to avoid issues with saving or publishing flows.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here is a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Queue Task** 



![Screenshot of Queue Task configuration page.](https://files.readme.io/f51538a8a68317e4a5fa409b44b5940f5b9ecd2cd7f1eacdf4f2634ea0a8181d-image.png)




<br />



![Screenshot of Queue details.](https://files.readme.io/c5f0810405b01ee65db12e4d753de9d1fc2b08f352b7d553e4345541c5f8b587-image.png)




<br />

> 📘 Note
> 
> - Dynamic Queues are supported only in Node version 1.5 and later.
> - Please note that the Skill Settings section visible in the screenshot above will be available only when a queue with skill-based routing is selected in 'Queue Name' dropdown.



| Method Name | Output Variables | Node Outcomes |
| --- | --- | --- |
| Queue Task | taskId  <br>  <br>agentId  | onInvalidData  <br>  <br>onError  <br>  <br>onInvalidChoice  <br>  <br>onauthorizatonfail  <br>  <br>Error  <br>  <br>taskFailed  <br>  <br>Queued  <br>  <br>onTimeout |






| Channel | Field Value |
| --- | --- |
| SMS, Facebook Messenger, WhatsApp, Live Chat, Email, and, Apple Messages for Business. | TASK ID - $(flid)  <br>CONVERSATION ID - $(conversationId)  <br>MEDIA TYPE  <br>MEDIA CHANNEL  <br>QUEUE NAME |






| Input Variables | Output Variables | Versions |
| --- | --- | --- |
| TASK ID - $(flid)  <br>  <br>Flow transaction Id from the start node is converted into UUID in the evaluate node and passed to create task node for creating task with flid as task Id.  <br>  <br>CONVERSATION ID - $(conversationId)  <br>  <br>Conversation Id from the create conversation node.  <br>  <br>MEDIA TYPE -  <br>  <br>This field specifies the type of media on Webex CC while making task API call.  <br>  <br>Media Type can be selected from the dropdown:  <br>  <br>For SMS, Facebook Messenger, WhatsApp, and, Apple Messages for Business the media type is “Social”.  <br>  <br>For Email, media type is “Email”.  <br>  <br>For Live Chat/ In-App Messaging, media type is “Chat”.  <br>  <br>MEDIA CHANNEL -  <br>  <br>This field specifies the channel on Webex CC while making task API call.  <br>Facebook Messenger, SMS, Email, WhatsApp, Apple Messages for Business, and Live Chat/ In-App Messaging can be selected from the dropdown.  <br>  <br>QUEUE DETAILS -  <br>  <br>Choose a queue type, static or dynamic.  <br>STATIC QUEUE - Select a queue to which the contact must be queued: Longest Available Agent and Skill Based Routing. New queues can be added from WxCC admin.  <br>  <br>If you select Skill Based Routing, you must configure Skill settings and provide values for Skill, Skill Condition, and Skill Value. You can add multiple skills or add a Skill relaxation rule. The default timeout for the skill relaxation rule is 60. You may also add Skill, Skill Condition, and Skill Values if you added Skill relaxation is added.  <br>DYNAMIC QUEUE - Enter the Queue ID to which contact must be queued.  <br>CONTACT PRIORITY - Contact Priority allows contacts to be prioritized over other contacts in the queue.  <br>  <br>CONTACT PRIORITY - Contact Priority allows contacts to be prioritized over other contacts in the queue.  <br>  <br>Select a priority between numbers 1-9.  <br>  <br>The default priority for the field is 10. We can pass a number between 1-9, where 1 denotes the highest priority, and 9 denotes the lowest priority.  <br>  <br>Note: v1.3 is recommended because the version is upgraded to address any issues related to skill relaxation configuration. | taskId  <br>  <br>agentId | TASK ID, CONVERSATION ID,  <br>MEDIA TYPE,  <br>MEDIA CHANNEL,  <br>QUEUE NAME are available with v1.0, v1.1, v1.2, and v1.3. |




> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).