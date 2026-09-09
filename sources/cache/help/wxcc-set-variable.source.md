Webex Contact Center supports the use of global variables and custom flow variables (local variables) while building flows for the digital channels.

> 👍  Important
> 
> If you have a scenario where multiple Set Variable and Queue Task nodes are required-such as in a Webex Contact Center (WxCC) flow where user input determines whether the call should be routed to a billing agent, account agent, login agent, or general query agent-you may need to use several Queue Task nodes. In these cases, we recommend creating separate sub-flow from branch that leads to Set Variable and a Queue Task node. Then, use the "Call Workflow" node to invoke these sub-flows from your main flow.
> 
> Key benefits:  
> 	1.	Reduces the overall complexity of your main flow.  
> 	2.	Makes the flow design cleaner and more organized.  
> 	3.	Clearly separates repetitive tasks from the main business logic.  
> 	4.	Helps reduce the total flow size. Since the maximum allowed flow size is 10 MB, we recommend keeping your flow size below this limit to avoid issues with saving or publishing flows.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information. 

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

**Method Name - Set Global Variable** 

Global variables are defined in the Webex CC Admin Portal. Flow developers can fetch and use these variables within flows to set and pass values in the context of interactions handled in the contact center.

## How to Fetch variables

To fetch variables:

1. Select the **Method Name**.
2. Select the required Node Runtime Authorization from the list.
3. Enter the **Task ID**.
4. Click **Fetch Global Variables** to fetch the variables.  
   All the fetched variables are pre-populated with values.
5. Select the required variables from the Fetch Global Variables pane.
6. Enter the value for the selected variable which can be used within the node.
7. Click **Save**.

> 📘 Note
> 
> Maximum number of variables that can be added/updated are 30.
> 
> The variable labels will not be translated in the agent desktop.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/87440fa-Set_Global_Variables.jpg",
        "Set Global Variables.jpg",
        "Screenshot of Set Global Variables configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Set Global Variables configuration page."
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
    "0-0": "**TASK ID - $(flid) **  \n  \nFlow transaction id from the start node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id.",
    "0-1": "Task ID  \n  \nresponsePayload",
    "0-2": "_ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onTimeout  \n  _ onauthorizationfail  \n  _ Invalid Token  \n  _ Bad Request  \n  _ Not Found  \n  _ serviceUnavailable  \n  _ Task Updated  \n  \\* Task Failed"
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
> All the global variable that are fetched with the default values can be modified and be used in the flow.
> 
> It is mandatory to use the latest version.

**Method Name - Set Flow Variable** 

Flow variables are defined in the flow. Flow developers can create and use these variables within flows to set and pass values in the context of interactions handled in the contact center.

## How to Add variables

To add variables:

1. Select the **Method Name**.
2. Select the required Node Runtime Authorization from the list.
3. Enter the **Task ID**.
4. Click **Add Variable**.
5. Enter the data in the required fields in the Set Variables pane.
6. Toggle the **Make Agent Viewable** to make all the variables can be viewable to the agent.
7. Select the **Agent Editable** checkbox to allow the agent to make changes to the variables in the flow.
8. Click **Save**.

> 📘 Note
> 
> To Delete a set of variables, click Delete icon the right-side of the Set Variables pane.
> 
> Maximum number of variables that can be added/updated are 30.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ce293b6-Set_Flow_Variable.jpg",
        "Set Flow Variable.jpg",
        "Screenshot of Set Flow Variables configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Set Flow Variables configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variable",
    "h-2": "Node Outcomes",
    "0-0": "**TASK ID - $(flid) **  \n  \nFlow transaction id from the start node is converted into UUID in the evaluate node, and passed to create task node, for creating task with flid as task id.",
    "0-1": "Task ID  \n  \nresponsePayload",
    "0-2": "  _ onInvalidData  \n  _ onError  \n  _ onInvalidChoice  \n  _ onTimeout  \n  _ onauthorizationfail  \n  _ Invalid Token  \n  _ Bad Request  \n  _ Not Found  \n  _ serviceUnavailable  \n  _ Task Updated  \n  \\* Task Failed ",
    "1-0": "Name - Name for the variable. Contains the alphanumeric value. Maximum length is 80 characters",
    "1-1": "",
    "1-2": "",
    "2-0": "Type - Type of the variable you want to associate with the flow  \n  _ String  \n  _ Boolean  \n  _ Integer  \n  _ Decimal  \n  \\* Date Time ",
    "2-1": "",
    "2-2": "",
    "3-0": "  _ Value - String - Contains the alphanumeric value. Maximum length is 256 characters  \n  _ Value - Boolean - Contains True or False value  \n  _ Value - Integer - Contains integer value  \n  _ Value - Decimal - Contains decimal value  \n  \\* Value - Date Time - Contains epoch timestamp in seconds ",
    "3-1": "",
    "3-2": "",
    "4-0": "Description - Contains the details  \nof the flow",
    "4-1": "",
    "4-2": "",
    "5-0": "Desktop Label - Contains the name for the label which is seen by the agent. Contains the alphanumeric value. Maximum length is 50 characters",
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
> Multi-language allowed for 'Description', 'Desktop Label' And 'Value' field (for Value field multi-language allowed in case when 'Type' field is **String** only)

> 🚧 
> 
> Note that using Set Variable node a large number of times (typically more than 25) in the same flow canvas can at times cause loading issues leading to the inability to save your flow configurations. Please modularise your flow using the Call Workflow node in such cases.