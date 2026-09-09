The _Call User_ node is used to initiate an outbound call to the configured number. This node cannot exist within the [Voice Node Group](doc:voice-node-group). When you drag-and-drop the _Call User_ node onto the visual flow builder, its **onAnswer** node event gets connected to the voice node group container automatically. Based on your use case you can decide which nodes exist in the node voice group.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4c52ea8-call-user.png",
        "call-user.png",
        "Screenshot of Call User Node"
      ],
      "align": "center",
      "caption": "Call User Node"
    }
  ]
}
[/block]


## Node Configuration

Drag-and-drop the node onto the visual flow builder and double-click it to open the configuration window.

1. Select the **Destination Type**: _msisdn_ or _Customer Id_. MSISDN is the mobile number of the user and the customer id is the unique identifier that identifies the user.

> 📘 Number Format
> 
> The phone number should be in E.164 format.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5c83403-Call_User_Node_Call_User_Node_Configuration.png",
        "Call User Node Call User Node Configuration.png",
        "Screenshot of Call User Node Configuration."
      ],
      "align": "center",
      "caption": "Call User Node Configuration"
    }
  ]
}
[/block]


2. Select the **From Number** from the drop-down list of available numbers. This is the number from which the outbound call gets initiated to the user. The platform supports dynamic 'FROM NUMBER' configuration as well. Simply select the ‘Dynamic’ option dropdown and configure the variable name that contains the ‘FROM NUMBER’.
3. In the **Destination** field, enter the variable that contains the selected destination type or provide an absolute value.
4. Configure Correlation ID, Callback Data, and Notify URL options are added to be able to pass data back to the client’s system to notify every call status. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries. This field accepts only a valid URL or a variable.  
   These are optional and accept dynamic values as well. The callback data size is however limited to 2KB and exceeding that will cause the node to exit through the policy error without making any calls.
5. Expiry Time: There are two types of expiry. You can select a specific date or number of seconds after which the request should expire. You can define the maximum time, within which the node execution must complete by providing the expiry time in UTC or seconds. You can define the date and time after which the calls should not be made.
   > 📘 Note
   > 
   > For a better customer experience, we strongly advise utilizing the expiry time whenever using the "Call User Node" for voice calls. This practice helps prevent voice calls being made after designated expiry time which otherwise could be disruptive and bothersome.

Here is a list of milestone events and when they occur while making a call:

- Offered: when <<prodname>> platform offers a call to the network to place a call
- Accepted: when the network accepts the call offered by <<prodname>> and places it to end-customer
- Answered: when the end-customer answers the call
- Dropped: when the call is dropped because of an internal technical error
- Rejected: when the call gets rejected; it can be due to various reasons like network failure, the customer is busy, rejected by the customer, etc.
- Released: when the call is ended by the platform
- Disconnected: when the end-customer disconnects the call
- Trombone Connected: when the <<prodname>> platform sends an outbound call to the customer and the customer asks to talk to an agent. The Trombone Connect event occurs when both parties A (end-customer) and B (agent) are connected.
- Trombone Released: when the party B (agent) exits the call.
- Message Expired: when the call request comes in after the configured expiry time, the request expires.  
  The endpoints will be automatically be notified of the occurrence of all the events.

5. Click **Save** to complete the configuration.

## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](doc:variable-management#section-custom-variables).

## Output Variables

You can see the data that this node generates as output variables. These [variables](doc:variable-management) are available for use in subsequent nodes. The following are the standard output variables for the _Call User_ node:

- **call.fromNumber** - stores the number from which the outbound call is initiated
- **call.destination** - stores the number or batch of numbers to which the outbound call is made
- **call.transId** - stores the transaction id of the outbound call
- **call.timestamp** - stores the timestamp of the outbound call.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8d7c8bb-Call_User_Node_Output_Variables.png",
        "Call User Node Output Variables.png",
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

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)",
    "0-1": "**onAnswer** - the flow exits through this node outcome when the configured audio prompts are played successfully.  \n  \nThis node outcome is automatically connected to the voice node group.",
    "1-0": "Error (red)",
    "1-1": "**onError** - the node exits with an error when there is an invalid user ID or missing digits in the customer's phone number. However, we noticed that the success rate of retried calls is significantly low. So, we suggest not to retry calling in such scenarios.  \n**oncallfail** - the flow exits through this node outcome when the call could not be connected due to network issues.  \n**onnoanswer** - the flow exits through this node outcome when the call is not answered.  \n**onbusy** - the flow exits through this node outcome when there is a busy tone on the receiver's side.  \n**onreject** - the flow exits through this node outcome when the call is rejected.  \n**onPolicyFail** - the flow exits through this node outcome when there is a policy failure.",
    "2-0": "Timeout (orange)",
    "2-1": "onExpiry - the flow exits through this node outcome when the call request expires."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> - The onExpiry node outcome is available only when Expiry is configured.
> - All the newly created flows exit through the onExpiry node outcome when the call request expires.
> - For existing flows, the flow exits through the onError node outcome when the call request expires. However, once you edit the flow, it exits through the onExpiry node outcome when the call request expires.

<br />

## Transition Actions

Use this tab to configure the transition actions for `On-enter`/`On-leave` events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).