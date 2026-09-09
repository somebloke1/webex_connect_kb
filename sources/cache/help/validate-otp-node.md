# Validate OTP Node

Source: https://help.webexconnect.io/docs/validate-otp-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:54+00:00

The validate OTP node enables you to validate the OTP settings. While configuring this node, you need to specify the same settings, which you have configured in the generate OTP node. 



![Validate OTP Node](https://files.readme.io/6ff51cc-validate_otp_icon.png)




## Node Configuration

Double-click the node to open the configuration window where you can specify the various parameters required for validating an OTP. Perform the following steps to configure the node:

1. Enter the variable name that contains the **OTP** entered by the user.
2. Provide the prefix and/or suffix of the OTP, if any in the **OTP Format** field. You need to enter these values only if you have preceded or succeeded in the OTP with any text. The node strips these values from the OTP before validation.
3. Enter the **Transaction Reference**. The node verifies the OTP obtained in step 1 against this transaction reference.
4. Provide a URL in the **Notify URL** field. This is the URL to which the node sends a success or failure notification. This is optional.
5. Enter a keyword to look for within the OTP input variable in the **Resend OTP Command** field. This is optional. The node looks for a match with this keyword within the OTP while validating it.
6. Enter the **Extra Parameters** (the key-value pairs that were set in the generate OTP node) in the form of **Parameter** and **Value**. This is optional. Repeat this step to add multiple parameters.
   > 🚧 Validate OTP
   > 
   > Please note that if the service key is regenerated in between a session, the OTP nodes will fail for the older or existing sessions.



![Validate OTP Configuration](https://files.readme.io/de8bab8-validate_otp_configuration.png)




## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](https://help.webexconnect.io/docs/variable-management-in-flows).



![Input and Custom Variables](https://files.readme.io/32d8290-validate_otp_input_variables.png)




## Output Variables

This node does not have any standard output variables.

## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.

| Node Edge       | Node Event/Outcome                                                                                        |
| :-------------- | :-------------------------------------------------------------------------------------------------------- |
| Success (green) | \* **onSuccess** - the flow exits through this node outcome when the OTP is successfully verified.        |
| Error (red)     | \* **onError** - the flow exits through this node outcome when the validation fails due to invalid input. |
|                 | \* **onFail** - the flow exits through this node outcome when the validation fails due to incorrect OTP.  |

## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](https://help.webexconnect.io/docs/transition-actions).