The close task is a global node. This node calls Webex CC Close task API to notify Webex CC whether closing a conversation was successful or not. While configuring flows in <<prodname>>, you’d need to use this node for notifying Webex CC about the success/failure in closing a conversation. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

 **Method Name - Close Task Accept** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/669e9b6-Close_Task_Accept.jpg",
        null,
        "Screenshot of Close Task Accept configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Close Task Accept configuration page"
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "TASK ID - $(n2.webex.taskId)  \n  \n  \\_ ID from the output variables of the closed event is the task ID  \n  \nID - $(n2.webex.taskId)  \n  \n  \\_ ID from the output variables of the closed event is the task ID  \n  \nQUEUE ID - $(n2.webex.queue)  \n  \n  \\_ Queue from the output variables of the closed event is the Queue ID  \n  \nCONVERSATION ID  \n  \n  \\_ ID from the output variables of the closed event  \n  \nMedia Type - $(mediaType)  \n  \n  \\* The output variables of the closed event is the Media Type",
    "0-1": "None",
    "0-2": "v1.1 and v1.0"
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
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

**Method Name - Close Task Reject** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/90ca145-Close_Task_Reject.jpg",
        null,
        "Screenshot of Close Task Reject configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Close Task Reject configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variable",
    "h-1": "Output Variable",
    "h-2": "Versions",
    "0-0": "TASK ID - $(n2.webex.taskId)  \n  \n  \\_ ID from the output variables of the closedevent is the task ID  \n  \nID - $(n2.webex.taskId)  \n  \n  \\_ ID from the output variables of the closed event is the task ID  \n  \nAgent ID - $(n2.webex.agent)  \n  \n  \\_ Agent ID from the output variables of the closed event  \n  \nCONVERSATION ID- $(mediaResourceId)  \n  \n  \\_ MediaResourceId from the output variables of the closed event is the Media Resource ID  \n  \nREASON - $(description)  \n  \n  \\_ $(description) will have the close conversation failure reason  \n  \nReason Code  \n  \nContains the close conversation failure code  \n  \nMedia Type - $(mediaType)  \n  \n  \\_ The output variables of the closed event is the Media Type",
    "0-1": "None",
    "0-2": "v1.1 and v1.0"
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

**Method Name - Close Task on WxCC** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b0b1411-Close_Task_On_WXCC.jpg",
        null,
        "Screenshot of Close Task on WxCC configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Close Task on WxCC configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variable",
    "h-1": "Output Variable",
    "h-2": "Versions",
    "0-0": "TASK ID - $(n2.webex.taskId)  \n  \n  \\_ ID from the output variables of the closed event is the task ID  \n  \nID - $(n2.webex.taskId)  \n  \n  \\_ ID from the output variables of the closed event is the task ID  \n  \nCONVERSATION ID- $(mediaResourceId)  \n  \n  \\_ MediaResourceId from the output variables of the closed event is the Media Resource ID  \n  \nMedia Type - $(mediaType)  \n  \n  \\_ The output variables of the closed event is the Media Type",
    "0-1": "NA",
    "0-2": "v1.1 and v1.0"
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