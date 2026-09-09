This node calls Webex CC Screen pop API. While configuring flows in <<prodname>>, you’d need to use this node for sending a screen pop message to the agent contact on Webex CC. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

> 📘 Note
> 
> - Within the Agent desktop, the screen pop feature only allows one URL to be displayed, and the tab will be labeled **Screen Pop**.

**Method Name - Screen Pop** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2ab99ac-Screen_Pop.jpg",
        null,
        ""
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Screen Pop configuration page."
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
    "0-0": "Screenpop",
    "0-1": "None",
    "0-2": "_ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ Error  \n  _ onScreenpopSuccess  \n  _ onScreenpopFailure  \n  _ Queued  \n  \\* onTimeout"
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
    "0-1": "TASK ID - $(flid)  \nAGENT ID - $(conversationId)  \nSCREENPOP URL  \nSCREENPOP LOADING URL"
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
    "0-0": "TASK ID - $(flid)  \n  \n  \\_ Flow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id  \n  \nAGENT ID - $(n2.webex.agentId)  \n  \n  \\_ AgentId from the output variables of the routed event is the Agent Id  \n  \nSCREENPOP URL  \n  \n  \\_ Enter the URL to which the agent must be navigated  \n  \nQUERY PARAMS -  \n  \n  \\_ Enter The additional key-value pairs that must be sent to  the agent  \n  \nDisplay Settings - Screen Pop Loading Behavior  \n  \n  \\* Select the required screen pop loading behavior from the list:  Inside Desktop, New Browser Tab, and Existing Browser Tab",
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

> 📘 Note
> 
> A user can use different screen pops using a branch node in the flow, and configure the branch node with different conditions and connect them with each screen pop.
> 
> The variable labels will not be translated in the agent desktop.