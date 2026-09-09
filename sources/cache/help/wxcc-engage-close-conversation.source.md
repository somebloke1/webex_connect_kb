This node calls imengage Close Conversation API to close the conversation on imiengage. While configuring flows in <<prodname>>, you’d need to use this node for closing the conversation.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods

**Method Name - Close Chat** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0820917-Close_Conversation.jpg",
        null,
        "Screenshot of Close Conversation configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Close Conversation configuration page."
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
    "0-0": "Close Chat",
    "0-1": "TransId",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ onFailure  \n  _ onCloseConversationFailure  \n  _ onConversationClosed  \n  _ onTimeout "
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


| Channels     | Field Value                          |
| :----------- | :----------------------------------- |
| All channels | CONVERSATION ID - $(mediaResourceId) |

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Versions",
    "0-0": "CONVERSATION ID – $(mediaResourceId)  \n  \n  \\* MediaResourceId from the output variables of the evaluate node is the Conversation ID ",
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