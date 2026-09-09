This node calls Webex CC Routed Notification API to notify Webex CC whether adding an agent or participant to the conversation was successful or not. While configuring flows in <<prodname>>, you’d need to use this node for notifying Webex CC about the participant/agent addition to conversation. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.   

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Routed Accept** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/67d8acd-Routed_Accepted.jpg",
        null,
        "Screenshot of Routed Accepted configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Routed Accepted configuration page."
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
    "0-0": "Routed Accepted",
    "0-1": "None",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ onTaskRoutedFailure  \n  _ onTaskRouted  \n  \\* onTimeout"
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
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "TASK ID - $(n2.webex.ID)  \n  \n> \\_ ID from the output variables of the routed event is the task IDID - $(n2.webex.ID)\n>\n> \\_ ID from the output variables of the routed event is the task IDAGENT ID - $(n2.webex.agentId)\n>\n> \\_ AgentId from the output variables of the routed event is the Agent IDQUEUE ID - $(n2.webex.queue)\n>\n> \\_ Queue from the output variables of the routed event is the Queue IDMEDIA RESOURCE ID - $(mediaResourceId)\n>\n> \\_ MediaResourceId from the output variables of the routed event is the Media Resource IDMEDIA TYPE - $(n2.webex.mediaType)\n>\n> \\_ MediaType from the output variables of the routed event is the Media Type",
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


> 📘 Note:
> 
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)

## Routed Rejected

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c385c59-Routed_Rejected.jpg",
        null,
        "Screenshot of Routed Rejected configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Routed Rejected configuration page."
    }
  ]
}
[/block]


**Method Name - Routed Reject** 

[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Routing Reject",
    "0-1": "None",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ onTaskRoutedFailure  \n  _ onTaskRouted  \n  \\* onTimeout"
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
    "0-1": "TASK ID - $(n2.webex.ID)  \nID - $(n2.webex.ID)  \nAGENT ID - $(n2.webex.agentId)  \nQUEUE ID - $(n2.webex.queue)  \nMEDIA RESOURCE ID - $(mediaResourceId)  \nMEDIA TYPE - $(n2.webex.mediaType)  \nREASON - $(description)  \nREASONCODE - $(code)"
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
    "0-0": "TASK ID - $(n2.webex.ID)  \n  \n> \\_ ID from the output variables of the routed event is the task IDID - $(n2.webex.ID)\n>\n> \\_ ID from the output variables of the routed event is the task IDAGENT ID - $(n2.webex.agentId)\n>\n> \\_ AgentId from the output variables of the routed event is the Agent IdQUEUE ID - $(n2.webex.queue)\n>\n> \\_ Queue from the output variables of the routed event is the Queue IDMEDIA RESOURCE ID - $(mediaResourceId)\n>\n> \\_ MediaResourceId from the output variables of the routed event is the Media Resource IDMEDIA TYPE - $(n2.webex.mediaType)\n>\n> \\_ MediaType from the output variables of the routed event is the Media TypeREASON - $(description)\n>\n> \\_ $(description) will have the add participant failure reasonREASON CODE - $(code)\n>\n> \\_ $(code) will have the add participant failure reason code",
    "0-1": "None"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> When the variable is selected from the previous node output variables, the node Id will be the prefix for the variable. For example, if sms.serviceNumber is an output variable of start node (node Id 2), then the variable becomes $(n2.sms.serviceNumber).