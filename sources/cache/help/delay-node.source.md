The _Delay_ node enables you to pause a flow before proceeding to the next node. You can configure it to wait for a specific duration or until a certain date and time. 

To name a few, you can use a delay node in scenarios where you need to send reminders about an event at regular intervals, retry connecting to a server.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3caf79f-delay_icon.png",
        "delay_icon.png",
        "Screenshot of Delay Node"
      ],
      "align": "center",
      "caption": "Delay Node"
    }
  ]
}
[/block]


## Node Configuration

Double-click the node to configure it. You can configure the delay node using either **Delay time** or **Wait for date** options.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1b18e18-Delay_Node_Configuration.png",
        "Delay Node Configuration.png",
        "Screenshot of Delay Node Configuration Page"
      ],
      "align": "center",
      "caption": "Delay Node Configuration"
    }
  ]
}
[/block]


Configure the delay settings:

- **Delay time** - the duration for which the flow execution needs to be delayed
  - **Time out (in seconds)** - delay duration in seconds.
- **Wait for date** - the date till which the flow execution needs to be paused. Specify the date-time in the **dd-mm-yyyy hh:mm:ss** format. The platform automatically detects the server timezone.

> 📘 
> 
> Please note that when you configure 'x' seconds of delay using the delay node, the processing is delayed by at least 'x' seconds. It can sometimes be higher depending on the number of active flow execution sessions across all services within your tenant.

## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](doc:variable-management).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4d444f6-delay_input_variables.png",
        "delay_input_variables.png",
        "Screenshot of Input and Custom Variables"
      ],
      "align": "center",
      "caption": "Input and Custom Variables"
    }
  ]
}
[/block]


## Output Variables

You can see the data that this node generates as output variables. These [variables](doc:variable-management) are available for use in subsequent nodes. The following are the standard output variables for the delay node:

- **delay.waitTime** - contains the time duration for which the flow waits.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/60f889c-Delay_Node_Output_Variables.png",
        "Delay Node Output Variables.png",
        "Screenshot of Output Variables"
      ],
      "align": "center",
      "caption": "Output Variables"
    }
  ]
}
[/block]


## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.

| Node Edge              | Node Event/Outcome                                                                                          |
| :--------------------- | :---------------------------------------------------------------------------------------------------------- |
| Timeout (yellow/amber) | - **onTimeout** - the flow exits through this node outcome when the specified timeout duration is completed |
| Error (red)            | - **onError** - the flow exits through this node outcome when there is an error due to invalid input        |

## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ec023ef-Delay_Nose_Transition_Actions.png",
        "Delay Nose Transition Actions.png",
        "Screensht of Transition Actions."
      ],
      "align": "center",
      "caption": "Transition Actions"
    }
  ]
}
[/block]


### Example

A user loses connection to the email server. Before attempting to reconnect to the server, you can configure the flow such that there is a delay of 10 seconds.