# Transition Actions

Source: https://help.webexconnect.io/docs/transition-actions
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:51+00:00

The **Transition Actions (optional)** tab is available in every flow [node](https://help.webexconnect.io/docs/nodes). This tab lists the node transition actions (actions to be performed by the flow) either while entering or leaving the node.  



![Node transition actions](https://files.readme.io/a935960-Transition_Actions.jpg)




Webex Connect supports four transition actions for each of the nodes:

## Set Variable

You can use a variable to set a value. This option supports two types of actions:

- Capture a [node output variable](https://help.webexconnect.io/docs/variable-management-in-flows) value into a custom variable. This allows data to be passed between flows when a flow is invoked from another flow.
- Set a custom variable value to a fixed value. For example, set the status code on receiving an API response.



| Parameter | Description |
| --- | --- |
| Variable | Select the custom variable into which you want to save data. You can also add a new custom variable. |
| Value | Set the value that you want to store in the custom variable.  <br>This is a mandatory field. |
| \+Add | Use to add and set multiple custom variable - values. |




### [DEBUG] Log all Flow Variables to Transaction Log

This action captures a snapshot of all [custom variable](https://help.webexconnect.io/docs/variable-management-in-flows) values into flow transaction logs for quick view in [debug view](https://help.webexconnect.io/docs/transaction-logs-and-debugging). This action is functional only when you enable the [**Descriptive logging**](https://help.webexconnect.io/docs/flow-settings#section-general) option in Flow settings.

### [DEBUG] Log a Value to Transaction Log

This action allows you to capture a given variable value into the transaction log for quick validation of the variable value during flow runtime. Flow transaction logs are available in the [debug view](https://help.webexconnect.io/docs/transaction-logs-and-debugging).  
This action is functional only if you enable the [**Descriptive logging**](https://help.webexconnect.io/docs/flow-settings#section-general) option in Flow settings.



| Parameter | Description |
| --- | --- |
| Log ID | Provide a Log id for reference within the flow transaction logs against which data is to be logged.  <br>The log id must be an integer great than 1000. |
| Value | Set the value that you want to capture into the transaction log. |




> 🚧 
> 
> Please note that the data logged using '[Debug] Log all Flow Variables to Transaction Log' and '[Debug] Log a Value to Transaction Log' is meant for storing some contextual information to help with troubleshooting during Flow Prototyping and Testing phase. We do not recommend using this feature to store any sensitive or personally identifiable information (PII) as these details are not stored in an encrypted format.

## Log a Value to Logbook

This action allows capturing data into custom logs using an existing [logbook](https://help.webexconnect.io/docs/logbook). You can capture one or more flow variables data into the logbook.  

> 📘 Note
> 
> This option is visible only if the logbooks feature is enabled for your tenant in admin portal.

If you have already configured to log values to logbooks and then the logbooks feature is disabled, you can still see the configuration, but the data will not be logged in the logbook. You also see a message “Logbook is disabled for the tenant. Flow runtime data will not be logged into the mapped logbook. To enable logbook please reach ...”

> 📘 Note
> 
> When the logbooks feature is disabled and if you click Edit live flow and open the node, the message disappears and you can no longer see the Log a Value to Logbook option.



![Logging data into a Logbook Attribute](https://files.readme.io/dae3641-logging_data_logbook_attribute.png)






| Parameter | Description |
| --- | --- |
| Logbook | Select an existing logbook that is mapped to this flow. |
| Attribute | Select the attributes within the logbook into which data must be logged.  <br>Logbook attributes can be manged from [Tools - Logbooks](https://help.webexconnect.io/docs/logbook#section-custom-attributes) |
| Value | Set the value that you want to store in the logbook attribute. |
| \+Add | Add and set multiple logbook attribute values. |




> 📘 
> 
> Ensure that you have mapped the logbook to the flow under [Flow Settings - Custom Logs](https://help.webexconnect.io/docs/flow-settings#section-custom-logs) so that it is available for use within the transition action of nodes used within that flow.