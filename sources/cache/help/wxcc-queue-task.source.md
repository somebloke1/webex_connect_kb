This node calls Webex CC Queue Task API to queue the contact at Webex CC. While configuring flows in <<prodname>>, you’d need to use this node for queuing the contact on Webex CC. Flow developer can configure the Skill based routing setting by selecting the appropriate skills and values on the node.

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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f51538a8a68317e4a5fa409b44b5940f5b9ecd2cd7f1eacdf4f2634ea0a8181d-image.png",
        null,
        "Screenshot of Queue Task configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Queue Task configuration page."
    }
  ]
}
[/block]


<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c5f0810405b01ee65db12e4d753de9d1fc2b08f352b7d553e4345541c5f8b587-image.png",
        null,
        "Screenshot of Queue details"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Queue details."
    }
  ]
}
[/block]


<br />

> 📘 Note
> 
> - Dynamic Queues are supported only in Node version 1.5 and later.
> - Please note that the Skill Settings section visible in the screenshot above will be available only when a queue with skill-based routing is selected in 'Queue Name' dropdown.

[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Queue Task",
    "0-1": "taskId  \n  \nagentId ",
    "0-2": "onInvalidData  \n  \nonError  \n  \nonInvalidChoice  \n  \nonauthorizatonfail  \n  \nError  \n  \ntaskFailed  \n  \nQueued  \n  \nonTimeout"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Field Value",
    "0-0": "SMS, Facebook Messenger, WhatsApp, Live Chat, Email, and, Apple Messages for Business.",
    "0-1": "TASK ID - $(flid)  \nCONVERSATION ID - $(conversationId)  \nMEDIA TYPE  \nMEDIA CHANNEL  \nQUEUE NAME"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "TASK ID - $(flid)  \n  \nFlow transaction Id from the start node is converted into UUID in the evaluate node and passed to create task node for creating task with flid as task Id.  \n  \nCONVERSATION ID - $(conversationId)  \n  \nConversation Id from the create conversation node.  \n  \nMEDIA TYPE -  \n  \nThis field specifies the type of media on Webex CC while making task API call.  \n  \nMedia Type can be selected from the dropdown:  \n  \nFor SMS, Facebook Messenger, WhatsApp, and, Apple Messages for Business the media type is “Social”.  \n  \nFor Email, media type is “Email”.  \n  \nFor Live Chat/ In-App Messaging, media type is “Chat”.  \n  \nMEDIA CHANNEL -  \n  \nThis field specifies the channel on Webex CC while making task API call.  \nFacebook Messenger, SMS, Email, WhatsApp, Apple Messages for Business, and Live Chat/ In-App Messaging can be selected from the dropdown.  \n  \nQUEUE DETAILS -  \n  \nChoose a queue type, static or dynamic.  \nSTATIC QUEUE - Select a queue to which the contact must be queued: Longest Available Agent and Skill Based Routing. New queues can be added from WxCC admin.  \n  \nIf you select Skill Based Routing, you must configure Skill settings and provide values for Skill, Skill Condition, and Skill Value. You can add multiple skills or add a Skill relaxation rule. The default timeout for the skill relaxation rule is 60. You may also add Skill, Skill Condition, and Skill Values if you added Skill relaxation is added.  \nDYNAMIC QUEUE - Enter the Queue ID to which contact must be queued.  \nCONTACT PRIORITY - Contact Priority allows contacts to be prioritized over other contacts in the queue.  \n  \nCONTACT PRIORITY - Contact Priority allows contacts to be prioritized over other contacts in the queue.  \n  \nSelect a priority between numbers 1-9.  \n  \nThe default priority for the field is 10. We can pass a number between 1-9, where 1 denotes the highest priority, and 9 denotes the lowest priority.  \n  \nNote: v1.3 is recommended because the version is upgraded to address any issues related to skill relaxation configuration.",
    "0-1": "taskId  \n  \nagentId",
    "0-2": "TASK ID, CONVERSATION ID,  \nMEDIA TYPE,  \nMEDIA CHANNEL,  \nQUEUE NAME are available with v1.0, v1.1, v1.2, and v1.3."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).