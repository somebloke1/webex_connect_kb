This node calls Webex CC Modify Notification API to notify Webex CC whether conferencing or transferring an agent or participant to the conversation was successful or not. While configuring flows in <<prodname>>, you’d need to use this node for notifying Webex CC about the agent conference/transfer status. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. .  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Modified Accept** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1e85be2-Modify_Accept.jpg",
        null,
        "Screenshot of Modified Accept configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Modified Accept configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Modified Accept",
    "0-1": "None",
    "0-2": "_ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ onTimeout  \n  _ onModifiedAcceptSuccess  \n  \\* onModifiedFailure"
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
    "0-0": "All channels",
    "0-1": "TASK ID - $(n2.webex.ID)  \nID - $(n2.webex.ID)  \nAGENT ID - $(n2.webex.agentId)  \nQUEUE ID - $(n2.webex.queue)  \nMEDIA RESOURCE ID - $(mediaResourceId)  \nMEDIA TYPE - $(n2.webex.mediaType)"
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
    "h-0": "Input Variable",
    "h-1": "Output Variable",
    "h-2": "Versions",
    "0-0": "TASK ID - $(n2.webex.ID)  \n  \n  \\* ID from the output variables of the modified event is the task ID",
    "0-1": "None",
    "0-2": "V1.1 and v1.0",
    "1-0": "ID - $(n2.webex.ID)  \n  \n  \\* ID from the output variables of the modified event is the task ID ",
    "1-1": "",
    "1-2": "",
    "2-0": "AGENT ID - $(n2.webex.agentId)  \n  \n  \\* AgentId from the output variables of the modified event is the Agent ID",
    "2-1": "",
    "2-2": "",
    "3-0": "QUEUE ID - $(n2.webex.queue)  \n  \n  \\* Queue from the output variables of the modified event is the Queue ID",
    "3-1": "",
    "3-2": "",
    "4-0": "MEDIA RESOURSE ID - $(mediaResourceId)  \n  \n  \\* MediaResourceId from the output variables of the modified event is the Media Resource ID",
    "4-1": "",
    "4-2": "",
    "5-0": "MEDIA TYPE - $(n2.webex.mediaType)  \n  \n  \\* MediaType from the output variables of the modified event is the Media Type",
    "5-1": "",
    "5-2": ""
  },
  "cols": 3,
  "rows": 6,
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

**Method Name - Modified Reject** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fa977c3-Modify_Reject.jpg",
        null,
        "Screenshot of Modified Reject configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Modified Reject configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Modified Reject",
    "0-1": "None",
    "0-2": "_ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ onModifiedRejectFailure  \n  _ onModifiedRejectSuccess  \n  \\* onTimeout"
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
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "TASK ID - $(n2.webex.ID)  \n  \n  \\* ID from the output variables of the modified event is the task ID",
    "0-1": "None",
    "0-2": "V1.1 and v1.0",
    "1-0": "ID - $(n2.webex.ID)  \n  \n  \\* ID from the output variables of the modified event is the task ID",
    "1-1": "",
    "1-2": "",
    "2-0": "AGENT ID - $(n2.webex.agentId)  \n  \n  \\* AgentId from the output variables of the modified event is the Agent ID",
    "2-1": "",
    "2-2": "",
    "3-0": "QUEUE ID - $(n2.webex.queue)  \n  \n  \\* Queue from the output variables of the modified event is the Queue ID ",
    "3-1": "",
    "3-2": "",
    "4-0": "MEDIA RESOURSE ID - $(mediaResourceId)  \n  \n  \\* MediaResourceId from the output variables of the modified event is the Media Resource ID",
    "4-1": "",
    "4-2": "",
    "5-0": "MEDIA TYPE - $(n2.webex.mediaType)  \n  \n  \\* MediaType from the output variables of the modified event is the Media Type",
    "5-1": "",
    "5-2": "",
    "6-0": "REASON - $(description)  \n  \n  \\* $(description) will have the add/remove participant failure reason",
    "6-1": "",
    "6-2": "",
    "7-0": "REASON CODE - $(code)  \n  \n  \\* $(code) will have the add/remove participant failure reason code",
    "7-1": "",
    "7-2": ""
  },
  "cols": 3,
  "rows": 8,
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