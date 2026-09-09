The **Transition Actions (optional)** tab is available in every flow [node](doc:nodes). This tab lists the node transition actions (actions to be performed by the flow) either while entering or leaving the node.  

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a935960-Transition_Actions.jpg",
        "node_transition_actions.png",
        "Screenshot of Node transition actions."
      ],
      "align": "center",
      "sizing": "550px",
      "border": true,
      "caption": "Node transition actions"
    }
  ]
}
[/block]


<<prodname>> supports four transition actions for each of the nodes:

## Set Variable

You can use a variable to set a value. This option supports two types of actions:

- Capture a [node output variable](doc:variable-management) value into a custom variable. This allows data to be passed between flows when a flow is invoked from another flow.
- Set a custom variable value to a fixed value. For example, set the status code on receiving an API response.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "Variable",
    "0-1": "Select the custom variable into which you want to save data. You can also add a new custom variable.",
    "1-0": "Value",
    "1-1": "Set the value that you want to store in the custom variable.  \nThis is a mandatory field.",
    "2-0": "\\+Add",
    "2-1": "Use to add and set multiple custom variable - values."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### [DEBUG] Log all Flow Variables to Transaction Log

This action captures a snapshot of all [custom variable](doc:variable-management) values into flow transaction logs for quick view in [debug view](doc:debugging). This action is functional only when you enable the [**Descriptive logging**](doc:flow-settings#section-general) option in Flow settings.

### [DEBUG] Log a Value to Transaction Log

This action allows you to capture a given variable value into the transaction log for quick validation of the variable value during flow runtime. Flow transaction logs are available in the [debug view](doc:debugging).  
This action is functional only if you enable the [**Descriptive logging**](doc:flow-settings#section-general) option in Flow settings.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "Log ID",
    "0-1": "Provide a Log id for reference within the flow transaction logs against which data is to be logged.  \nThe log id must be an integer great than 1000.",
    "1-0": "Value",
    "1-1": "Set the value that you want to capture into the transaction log."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 🚧 
> 
> Please note that the data logged using '[Debug] Log all Flow Variables to Transaction Log' and '[Debug] Log a Value to Transaction Log' is meant for storing some contextual information to help with troubleshooting during Flow Prototyping and Testing phase. We do not recommend using this feature to store any sensitive or personally identifiable information (PII) as these details are not stored in an encrypted format.

## Log a Value to Logbook

This action allows capturing data into custom logs using an existing [logbook](doc:logbook). You can capture one or more flow variables data into the logbook.  

> 📘 Note
> 
> This option is visible only if the logbooks feature is enabled for your tenant in admin portal.

If you have already configured to log values to logbooks and then the logbooks feature is disabled, you can still see the configuration, but the data will not be logged in the logbook. You also see a message “Logbook is disabled for the tenant. Flow runtime data will not be logged into the mapped logbook. To enable logbook please reach ...”

> 📘 Note
> 
> When the logbooks feature is disabled and if you click Edit live flow and open the node, the message disappears and you can no longer see the Log a Value to Logbook option.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dae3641-logging_data_logbook_attribute.png",
        "logging_data_logbook_attribute.png",
        "Screenshot of Logging data into a Logbook Attribute."
      ],
      "align": "center",
      "border": true,
      "caption": "Logging data into a Logbook Attribute"
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "Logbook",
    "0-1": "Select an existing logbook that is mapped to this flow.",
    "1-0": "Attribute",
    "1-1": "Select the attributes within the logbook into which data must be logged.  \nLogbook attributes can be manged from [Tools - Logbooks](doc:logbook#section-custom-attributes)",
    "2-0": "Value",
    "2-1": "Set the value that you want to store in the logbook attribute.",
    "3-0": "\\+Add",
    "3-1": "Add and set multiple logbook attribute values."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 
> 
> Ensure that you have mapped the logbook to the flow under [Flow Settings - Custom Logs](doc:flow-settings#section-custom-logs) so that it is available for use within the transition action of nodes used within that flow.