# Generate OTP Node

Source: https://help.webexconnect.io/docs/generate-otp-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:54+00:00

A one-time password or pin (OTP) is a dynamic password generated randomly, which is valid only for a single session or transaction. OTPs are generally used for two-factor authentication or multi-factor authentication in some cases. You can use OTPs in multiple scenarios like confirming the identity of the user, checking the validity of accounts for business, securing information, and many more.<br>

The generate OTP node allows you to generate a dynamic one-time password for authentication purposes. Webex Connect sends OTPs to users over SMS/Voice/Email/Push Notifications or other supported channels. The generate OTP node and [validate OTP](https://help.webexconnect.io/docs/validate-otp-node) node are often used in conjunction to set up user authentication flows such as two-factor authentication.



![Generate OTP Node](https://files.readme.io/ef9fe6b-generate_otp_icon.png)




> 🚧 Known UI issue
> 
> Due to a UI issue you will not be able to Save the configurations of Generate OTP node when 'OTP Length' value is configured. The only workaround at the moment is to keep the 'OTP Length' field empty and then hit 'Save'. With this approach, the value will automatically be set to 6.

## Node Configuration

Drag and drop the generate OTP node onto the flow canvas and double-click it open the configuration window. Configure the following parameters:

1. Select an **OTP Format**. The default format is _Alphanumeric_. Webex Connect supports the following OTP formats:
   > - _Alphabetic_ - a string that contains a combination of lower case and upper case alphabetic characters
   > - _Numeric_ - a string that contains numeric characters
   > - _Alphanumeric_ - a string that contains a combination of alphabetic and numeric characters.
2. Use the increment or decrement arrows to select the OTP Length. The default length is six characters. The minimum OTP length is 4 and the maximum length is 64.  
   The **Sample OTP** displays an auto-generated random string of the selected format and length. This string changes every time you change the format and/or the length of the OTP.



![Generate OTP Configuration](https://files.readme.io/ac3a083-Generate_OTP_Node_Generate_OTP_Configurations.png)




3. Define **OTP Validity (in minutes)**. The OTP expires after this duration. On resend OTP request, the validity is reset. The default validity period of the OTP is 30 minutes.
4. Select the action for **On Resend OTP Request**, either _Generate new OTP_ or _Re-use current OTP_. The OTP validity is reset for either of the actions.
5. Enter a **Transaction Reference** or select a variable that contains this value. This is a unique reference code tied to the generated OTP that is used to validate it.
6. Enter any **Extra Parameters**. This is an optional step.  
   You can specify extra parameters in the form of key-value pairs (**Parameter** and **Value**). If defined, these extra parameters must be passed during OTP validation.
   > 🚧 OTP Node
   > 
   > Please note that if the service key is regenerated in between a session, the OTP nodes will fail for the older or existing sessions.

## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](https://help.webexconnect.io/docs/variable-management-in-flows).



![Input and Custom Variables](https://files.readme.io/c4634e1-generate_otp_input_variables.png)




## Output Variables

You can see the data that this node generates as output variables. These [variables](https://help.webexconnect.io/docs/variable-management-in-flows) are available for use in subsequent nodes. The following are the standard output variables for the generate OTP node:

- **generateOTP.OTP** - captures the generated OTP. 



![Output Variables](https://files.readme.io/4f69b2e-generate_otp_output_variables.png)




## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.



| Node Edge | Node Event/Outcome |
| --- | --- |
| Success (green)<br>  <br>  <br>**Note**: You can see this node edge only when you complete the node configuration. | \* **onSuccess** - the flow exits through this node when an OTP is generated successfully. |
| Error (red) | \* **onError** - the flow exits through this node outcome when the OTP generation request could not be processed due to invalid input. |




See the [example](#section-example) for configuration details.



![Node Outcomes](https://files.readme.io/e28dab5-Generate_OTP_Node_Node_Outcomes.png)




## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](https://help.webexconnect.io/docs/transition-actions).

### Example

A bank sends an OTP (a numeric string of 4 characters) to a user who is making an online bill payment. The OTP is valid for 10 minutes. If the user has not received the OTP in 10 minutes and hits Resend OTP before the OTP expires, the bank generates a new OTP and resends it with a validity of 10 minutes again.



![Sample Configuration of Generate OTP](https://files.readme.io/114d6d5-Generate_OTP_Node_Sample_Configuration_of_Generate_OTP.png)

