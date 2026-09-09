This node calls Webex Engage Re-open Conversation API to re-open the closed conversation on Webex Engage. While configuring flows in <<prodname>>, you’d need to use this node to re-open the conversation and queue it. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Re-Open Converstation** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9859e51-update_conversation.png",
        "update_conversation.png",
        "Interface section displaying the method name \"Reopen Conversation\""
      ],
      "align": "center",
      "border": true,
      "caption": "Interface section displaying the method name \"Reopen Conversation\""
    }
  ]
}
[/block]


**Method Name - Close Conversation** 

[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Reopen Conversation",
    "0-1": "TransId",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ onFailure  \n  _ ConversationReopened  \n  _ ConversationReopenFailed  \n  _ onTimeout "
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


| Channel      | Field Value                            |
| :----------- | :------------------------------------- |
| All channels | CONVERSATION ID - $(n6.conversationId) |

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "0-0": "CONVERSATION ID – $(n6.conversationId)  \n  \n  \\* Conversation id from the output variables of the search conversation node is the Conversation ID ",
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