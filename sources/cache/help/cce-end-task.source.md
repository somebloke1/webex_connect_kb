This node calls Contact Center Enterprise Close task API to notify Contact Center Enterprise about the success/failure in closing a conversation. While configuring flows in <<prodname>>, you’d need to use this node for notifying Contact Center Enterprise about the success/failure in closing a conversation. 

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.  

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f87d5d6-CCE_End_Task.jpg",
        "CCE_End_Task.jpg",
        "Interface section showing the method name \"End Task Details\"."
      ],
      "align": "center",
      "border": true,
      "caption": "Interface section showing the method name \"End Task Details\"."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "\\_ Method Name  \nName of the CCE task.  \n  \n\\_ Tracking ID  \nThe Tracking ID used to track individual requests.  \n  \n\\_ Domain - $(domain) One of the custom variables that must contain the finesse public accessible domain name for your business. A domain name is a string of text that maps to a numeric IP address, used to access a website from client software. Example: [www.google.com](http://www.google.com).  \n  \n **Task Details**  \n  \n   \\_ Task ID - $(flid)  \nFlow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. $(flid) is one of the custom variables that contains the processed task ID value which is evaluated in the Evaluate node.  \n  \n**Optional Variables**  \n  \n  \\_ Call Variables - $(val1)  \nValue of the call variable. Maximum allowed value length is up to 40 bytes.  \n  \n  \\_ User Variables - $(val1)  \nUser variables consist of Key, Type, and Value.  \n  \n\\_ Extension Variables - $(val1)  \nExtension variables consist of Key, Type, and Value.",
    "0-1": "CCE End Task -  \n_ location  \n_ responsePayload",
    "0-2": "_ ok - 200 - Success  \n_ Successfully Created - 201 - Success  \n_ Forbidden - 403 - Erro  \n_ Not Found - 404 - Error  \n_ Internal Server Error - 500 - Error  \n_ Bad Request - 400 - Error  \n_ Unreachable - HTTP Status - 502 Error  \n_ Service Unavailable - 503 - Error  \n\\* Task Already Exists - 20200 - Success"
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


**Method Name - Close Task** 

[block:parameters]
{
  "data": {
    "h-0": "Method Name",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Close Task",
    "0-1": "None",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onauthorizationfail  \n  _ Error  \n  _ Success  \n  \\* onTimeout"
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
    "0-0": "All Channels",
    "0-1": "TASK ID - $(n2.webex.ID)  \nID - $(n2.webex.ID)  \nQUEUE ID - $(n2.webex.queue)  \nCONVERSATION ID - $(mediaResourceId)"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]