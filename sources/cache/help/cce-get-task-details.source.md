This node calls Contact Center Enterprise Task API to get details of a Task. While configuring flows in <<prodname>>, you’d need to use this node for getting details of the task on Contact Center Enterprise.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Get Task Details** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2f3b713-CC_Get_Task_Details.png",
        "CC_Get_Task_Details.png",
        "Interface section showing the method name \"Get Task Details\"."
      ],
      "align": "center",
      "caption": "Interface section showing the method name \"Get Task Details\"."
    }
  ]
}
[/block]


> 📘 Note
> 
> Based on the Channel you have selected, the Conversation ID will change accordingly.

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "\\_ Method Name  \nName of the CCE task.  \n  \n\\_ Tracking ID  \nThe Tracking ID used to track individual requests.  \n  \n\\_ Domain - $(domain) One of the custom variables that must contain the finesse public accessible domain name for your business. A domain name is a string of text that maps to a numeric IP address, used to access a website from client software. Example: [www.google.com](http://www.google.com).  \n  \n **Task Details**  \n  \n \\_ Task ID - $(flid)  \nFlow transaction id from the state node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id. $(flid) is one of the custom variables that contains the processed task ID value which is evaluated in the Evaluate node.",
    "0-1": "_ preferredOwner  \n_ taskId  \n_ customerId  \n_ origin  \n_ destination  \n_ mediaType  \n_ mediaChannel  \n_ state  \n_ direction  \n_ createdTime  \n_ lastUpdatedTime  \n_ scriptSelector  \n_ variables  \n_ history  \n_ estimatedWaitTime  \n_ responsePayload",
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