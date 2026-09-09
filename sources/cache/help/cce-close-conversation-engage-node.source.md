This node calls Webex Engage Close Conversation API to close the conversation on Webex Engage. While configuring flows in <<prodname>>, you’d need to use this node for closing the conversation.

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
        "https://files.readme.io/966f420-Close_Chat.jpg",
        "Close Chat.jpg",
        "Interface section displaying the method name \"Close Conversation\""
      ],
      "align": "center",
      "caption": "Interface section displaying the method name \"Close Conversation\"."
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
    "0-0": "Send Plain Test Message",
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
    "0-0": "CONVERSATION ID – $(mediaResourceId)  \n  \n- MediaResourceId from the output variables of the evaluate node is the Conversation ID ",
    "0-1": "TransId"
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
> When the variable is selected from the previous node output variables, the nodetid will be the prefix for the variable. Eg., sms.serviceNumber is an output variable of start node (node id 2), then the variable becomes $(n2.sms.serviceNumber)