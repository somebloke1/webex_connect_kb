This node calls imengage Add Participant API to add an agent to the conversation on imiengage. While configuring flows in <<prodname>>, you’d need to use this node for adding the agent to the conversation. The agent details will be available from the routed event 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Add Participant** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a80631a-Add_Participant.jpg",
        null,
        "Screenshot of Adding a participant configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding a participant configuration page."
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
    "0-0": "Add Participant",
    "0-1": "TransId",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ Failure  \n  _ OnAddParticipantFailure  \n  _ OnAddParticipantSuccess  \n  _ Success  \n  \\* onTimeout "
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
    "0-1": "CONVERSATION ID - $(mediaResourceId)  \nPARTICIPANT - $(n2.webex.agentId)"
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
    "0-0": "CONVERSATION ID – $(mediaResourceId)  \n  \n  \\_ MediaResourceId from the output variables of the evaluate node is the Conversation ID  \n  \nPARTICIPANT - $(n2.webex.agentId)  \n  \n  \\_ AgentId from the output variables of the start node is the participant",
    "0-1": "TransId",
    "0-2": "v1.0"
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