# Flow Debug

Source: https://help.webexconnect.io/docs/transaction-logs-and-debugging
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:47+00:00

Flow Debug provides a step-wise execution trace for your recent flow executions. You can find and fix problems in your flows using Flow Debug. This capability is typically meant to be used for troubleshooting purposes while configuring and iterating flows. We recommend you to use Debug Console for viewing old transaction logs.

You can launch the flow debug panel using the **Flow Debug** icon at the right navigation panel of your flow canvas. The **Flow Debug** panel opens in a split view at the bottom of your flow and displays a list of 10 most recent flow runs. Typically logs take about two minutes to show in the flow debug section. You may not see the logs for a recently initiated transaction immediately.

- Click the transaction ID to drill down to the details of each flow run (transaction)
- Filter the flow executions using the transaction ID 
- Filter the logs based on selected date range and time (Logs are available for the latest 30 days).



![Debug - Canvas split view](https://files.readme.io/7a1cc13-2.jpg)




The information captured within logs is segregated into three levels based on the sensitivity of the data and the level of detail:<br>

- Level 1: Summary Logs
- Level 2: Sequence Summary
- Level 3: Node Execution Details.

You can now see the timezone along with the timestamp in the transaction logs.



![Transaction Logs Screen](https://files.readme.io/bc3a21a-1.jpg)




## Transaction Sequence Summary

This view lists the complete sequence of nodes executed for the selected transaction. It also lists the time taken to execute each step and the outcome of each step. _Step_ here refers to the runtime execution of a particular node. This view allows you to verify the business logic within the flow without going into technical details.

Since navigating to a specific node in a large flow can be cumbersome, flow debug automatically shifts the canvas to the respective node when you click on a node name under the 'Node' column.

> 🚧 Encryption
> 
> Summary logs do not contain personally identifiable information (PII) and are therefore not encrypted. However, the details of node execution may contain PII, in which case such information is encrypted. Only users who are authorized by the client admin can decrypt these detailed logs to view them in plain text.

## Node Execution Details

The node execution details are available only to users authorized by the tenant onwer. This view, by default, shows PII in encrypted form. However, basic information such as the outcome of the node and the execution parameters like start time is available to all users in plain text.

> 📘 Note
> 
> For all the flows created after the v6.3.0 release, there is a limit of 1000 for the number of node executions within a single flow. If the number of node executions exceeds 1000, the node execution fails with an error “Node execution limit reached.”

> ❗️ Capturing Node Execution Details during Initial Set-up.
> 
> You must enable the **Descriptive Logs** option under [flow settings](https://help.imiconnect.io/docs/flow-settings) to capture node execution details. Please note that this feature is suggested to be used only during initial flow set-up and troubleshooting. Enabling this feature in production mode can impact your tenant performance.



![Node Level Execution Details](https://files.readme.io/56dd4d9-3.jpg)




In the case of voice flows, you can see the various voice nodes within the flow and the sequence in which the nodes are executed. If the flow contains the voice node group, then you can drill down to the individual nodes in the group.

When a voice flow has recordings, you can click **Recordings** to play the recordings directly in the debug console. You can also see the call duration and audio prompts configured and played to the caller during an ongoing call.



![Voice Flows - Transaction Logs](https://files.readme.io/bc3a21a-1.jpg)




## Transaction Logs

- **Decrypts Logs**: the additional description of the action performed by the node under the transaction in encrypted mode.  
- **Time Stamp**:  the time at which the flow execution started 
- **Transaction ID**: the ID number created for the transaction
- **Invoked By**: the trigger that invoked the flow
- **Time Taken**: the time taken to execute the entire flow
- **Last Node**: the last node that was in use when the flow ended
- **NodeID **: ID of the current node in the flow
- **Outcome**:  the node event of each node
- **Details**: details of the node execution.

> 👍 
> 
> As mentioned above, flow debug allows you to analyse step wise execution of your recent flow executions and is mainly best suited for understanding how your flow is progressing and where there are issues, if any, during initial flow configuration and prototyping phases. If you want to analyse a transaction within last 30 days period, or want to look at the past 30 days of message exchanges for a given customer or channel, you can use [Debug Console](https://help.imiconnect.io/docs/console) feature.

## Transaction Channels

The following parameters are displayed in the Debug flow of the Start Node:



| Channel | Event in Start node | Parameters to be shown in transaction logs |
| --- | --- | --- |
| SMS | Mobile originated -MO | Timestamp  <br>Sender Number  <br>Service Number  <br>Message |
| SMS | On Link click | Timestamp  <br>Sender Number  |
| Voice | Inbound call | Service Number  <br>Timestamp  <br> MSISDN  |
| Voice | Missed  call | Service Number  <br>Timestamp  <br>MSISDN  |
| MMS | Mobile originated -MO | Sender Number  |
| Messenger | Incoming Message | AppId  <br>PSID  <br>Message  <br>Attachment URL  <br>Timestamp  <br>Location URL  |
| Messenger | On link click | AppId  <br>PSID  <br>Tim_estamp  |
| Messenger | Postback | AppId  <br>PSID  <br>Timestamp  <br>Post_back Payload  |
| WhatsApp | Incoming Message | AppId  <br>WaId  <br>Timestamp  <br>Message  <br>Image URL  <br>Location URL  <br>Voice URL  <br>Audio URL  <br>Video URL  <br>Sticker URL  |
| WhatsApp | Postback | AppId  <br>WaId  <br>Timestamp  <br>Button Payload  |
| WhatsApp | List Message | AppId  <br>WaId  <br>Timestamp  <br>List Description  <br>Row Title  <br>Row Identifier  |
| WhatsApp  <br>  <br>Reply button Message |  | AppId  <br>WaId  <br>Timestamp  <br>Reply Button Title  <br>Reply Button Identifier  |
| In-App / Live Chat | Custom event | UserId  <br>PushId  <br>Timestamp  <br>AppId |
| In-App / Live Chat | Incoming Message | Timestamp  <br>UserId  <br>PushId  <br>Message  <br>Attachments  <br>DeviceId  <br>Version  <br>Threadid |
| In-App / Live Chat | On thread close | Threadid  <br>AppId  <br>UserId |
| In-App / Live Chat | On postback | Timestamp  <br>UserId  <br>PushId  <br>Message  <br>Attachments  <br>DeviceId  <br>Version  <br>ThreadId  <br>Button Payload |
| Email | Incoming Message | Message  <br>Emailid  <br>AppId  <br>To Address  <br>Attachments  <br>Receipts  <br>Timestamp |
| Email | Subscribe | Emailid  <br>AppId  <br>Attachments  <br>Timestamp |
| Email | unsubscribe | EmailId  <br>AppId  <br>Attachments  <br>Timestamp |
| RCS | Incoming Message | Text  <br>Timestamp  <br>AppId  <br>Number |
| RCS | Message  <br>Incoming attachment | Text  <br>Timestamp  <br>AppId  <br>Number  <br>File URL |
| RCS | Location response | Text  <br>Timestamp  <br>AppId  <br>Number |
| RCS | Postback | Text  <br>Timestamp  <br>AppId  <br>Number  <br>Postback Data |
| Apple Messages for Business | Conversation closed | ABCUserId  <br>AppId |
| Apple Messages for Business | Interactive Message authentication | AppId  <br>AuthToken  <br>AuthStatus |
| Apple Messages for Business | Interactive Message list picker | ABCUserId  <br>AppId  <br>Timestamp  <br>Date Picker Time Slot  <br>Date Picker Duration  <br>Time Slot Identifier  <br>Time Slot Start Time  <br>List Picker Items  <br>List Picker Other Items |
| Apple Messages for Business | Interactive Message payment | ABCUserId  <br>AppId  <br>Timestamp  <br>Payment Status |
| Apple Messages for Business | Incoming Message | ABCUserId  <br>AppId  <br>Timestamp  <br>Message  <br>Attachment URL |
| Apple Messages for Business | Interactive Message quick reply | ABCUserId  <br>AppId  <br>Timestamp  <br>Selected Identifier  <br>Selected Index |
| Apple Messages for Business | Interactive Message form response | ABCUserId  <br>AppId  <br>Timestamp  <br>Selections  <br>Selections Count |
| Apple Messages for Business | Typing indicator | ABCUserId  <br>AppIdAppId  <br>Type |
| Apple Messages for Business | Interactive Message new authentication | AppId  <br>AuthToken  <br>AuthStatus |
| Apple Messages for Business | Interactive Message iMessage extension | AppId  <br>URL |
| Custom event |  | Payload  <br>Timestamp |
| Google Business Messages | Incoming Message | AppId  <br>ConversationId  <br>AgentId  <br>Send Time  <br>MessageId  <br>Text |
| Google Business Messages | User Status | AppId  <br>ConversationId  <br>AgentId  <br>Send Time  <br>IsTyping  <br>Requested Live Agent |
| Google Business Messages | Survey Response | AppId  <br>ConversationId  <br>AgentId  <br>Send Time  <br>SurveyId  <br>Question Response Text  <br>Question Response Postback Data  <br>QuestionIndex |
| Google Business Messages | Suggestion Response | AppId  <br>ConversationId  <br>AgentId  <br>Send Time  <br>MessageId  <br>Postback Data  <br>Text  <br>Suggestion Type  |
| Instagram | Incoming Message | MessageId  <br>Igsid  <br>Igid  <br>Timestamp  <br>UserId  <br>AppId  <br>Message Type  <br>Attachment Type  <br>Attachment Url  <br>Story Reply Url  <br>Replied MessageId |
| Instagram | Message Deleted | MessageId  <br>Igsid  <br>Igid  <br>Timestamp  <br>UserId  <br>AppId  <br>IsDeleted |
| Instagram | Postback | MessageId  <br>Igsid  <br>Igid  <br>Timestamp  <br>UserId  <br>AppId  <br>Payload  <br>Title  <br>Quick Reply Payload |




Inbound events 

The following parameters are displayed in the Debug flow of the Receive Node:



| Channel | Events in Receive node | Parameters to be shown in transaction logs |
| --- | --- | --- |
| SMS  <br>  <br>·      |  | Sender Number  <br>Service Number  <br>Message  <br>Attachment  <br>Timestamp |
| Voice |  | MSISDN  <br>Service Number  <br>Message  <br>Timestamp |
| Messenger | Incoming Message | PSID  <br>AppId  <br>Message  <br>Attachments  <br>Timestamp |
| Messenger | Postback | PSID  <br>AppId  <br>Payload  <br>Timestamp |
| WhatsApp | Incoming Message | AppId  <br>WaId  <br>Timestamp  <br>Message  <br>Image URL  <br>Location URL  <br>Voice URL  <br>Audio URL  <br>Video URLSticker URL |
| WhatsApp | Postback | AppId  <br>WaId  <br>Timestamp  <br>Button Payload |
| WhatsApp | List Message | AppId  <br>WaId  <br>Timestamp  <br>List Description  <br>Row Title Row Identifier |
| WhatsApp | Reply button Message | AppId  <br>WaId  <br>Timestamp  <br>Reply Button Title  <br>Reply Button Identifier |
| Custom event |  | Payload |
| In-App / Live Chat | Incoming Message | Timestamp  <br>UserId  <br>PushId  <br>Message  <br>Attachments  <br>DeviceId  <br>Version  <br>ThreadId |
| In-App / Live Chat | Form response | Timestamp  <br>UserId  <br>PushId  <br>Form Response  <br>Attachments  <br>DeviceIdVersion  <br>ThreadId |
| In-App / Live Chat | Postback | Timestamp  <br>UserId  <br>PushId  <br>Message  <br>Attachments  <br>DeviceId  <br>Version  <br>ThreadId  <br>Button Payload |
| Apple Messages for Business | Interactive Message Time picker | ABCUserId  <br>AppId  <br>Timestamp  <br>Message  <br>Attachment URL  <br>Date Picker Timeslot  <br>Date Picker Duration  <br>Time Slot Identifier  <br>Time Slot Start Time |
| Apple Messages for Business | Interactive Message authentication | AuthToken  <br>AuthStatus |
| Apple Messages for Business | Interactive Message list picker | ABCUserId  <br>AppId  <br>Timestamp  <br>List Picker Items  <br>List Picker Other Items |
| Apple Messages for Business | Interactive Message payment | ABCUserId  <br>AppId  <br>Timestamp  <br>Payment Status |
| Apple Messages for Business | Interactive Message form response | ABCUserId  <br>AppId  <br>Timestamp  <br>Selections  <br>Selections Count |
| Apple Messages for Business | Conversation closed | ABCUserId  <br>AppId |
| Apple Messages for Business   | Interactive Message new authentication | AppId  <br>AuthToken  <br>AuthStatus |
| Apple Messages for Business | Interactive Message quick reply | ABCUserId  <br>AppId  <br>Timestamp  <br>Selected Identifier  <br>Selected Index |
| Apple Messages for Business   | Typing indicator | ABCUserId  <br>AppId  <br>Type |
| Apple Messages for Business | Interactive Message iMessage extension | AppId  <br>URL |
| Apple Messages for Business   | Incoming Message | ABCUserId  <br>AppId  <br>Timestamp  <br>Message  <br>Attachment URL |
| RCS | Incoming attachment | Text  <br>Timestamp  <br>AppId  <br>Number |
| RCS   | Incoming Message | Text  <br>Timestamp  <br>AppId  <br>Number  <br>File URL |
| RCS | Location response | Text  <br>Timestamp  <br>AppId  <br>Number |
| RCS   | Postback | Text  <br>Timestamp  <br>AppId  <br>Number  <br>Postback Data |




**HTTP node logs** 

For HTTP nodes, the flow transactions logs are: 

- Request Timestamp
- Request URL
- Request Data
- Response timestamp
- Response Data

**Custom node logs**

For Custom nodes, the flow transactions logs are: 

- Request timestamp
- Request URL
- Request Data
- Response timestamp
- Response Data

> 📘 
> 
> Transaction details for Custom event/Webhook is available for a maximum of 7 days.

**Prebuilt Transaction Details - Outbound and Async events**

For Prebuilt nodes, the flow transactions logs are:

- Resume key
- Request timestamp
- Request URL
- Request Data
- Response timestamp
- Response Data

## Variables Created or Updated during the Node Execution

Webex Connect logs the list of the variables created or updated in node executions for all flow transactions under the 'Variables created/updated during node execution' section as shown below. The parameters which meet one of the following conditions will be listed in this section:

- A variable is one of the Output variables of the node and it is used in later part of the flow (mentioned as a variable in the configuration of other nodes).
- The value of the variable used in the node execution is updated after it is used in the previous node.

> 📘 Note
> 
> These logs are generated only when Descriptive logs are not enabled.

> 📘 Note
> 
> Variables created as an object in **Evaluate** node are replaced in the logs with values received from Rhino engine.
> 
> Example -`var Array_vechicle = ['Car', ‘Bike’, ‘Ship’];`
> 
> The value captured in the logs for Array_vechicle: org.mozilla.javascript.NativeArray@99582cf denoting the Array_vechicle is a native array in the Evaluate node script.

The screenshot below is an example of the transaction log from the Receive node:



![Receive Node - Transaction Logs](https://files.readme.io/6afcc49-4.png)




## FAQs

### Question: Why are there escape characters (like forward slash '\') in the JSON parameters shown in the logs of Webex Connect Flow Builder, especially in the Start Node or when using HTTP/Custom/Prebuilt Integration nodes? Do these characters alter the variable values at runtime?

No, the values of your variables are not altered during runtime. The escape characters you see (such as forward slash - \) are only added for representation purposes in the logs. They help display the raw JSON structure and ensure special characters are visible and preserved in the log output. For example, if your incoming JSON parameter is: {"email": "[Connect@Connect.com](mailto:Connect@Connect.com)"}, in the flow Debug Logs the value of email parameter may appear as: \"[Connect@Connect.com](mailto:Connect@Connect.com)\" . Here, the forward slash are just to "escape" the quotation marks inside the JSON string for clear display. At runtime, the actual value used in your flow (e.g., in Transition Actions) is the real, unescaped value - ‘[Connect@Connect.com](mailto:Connect@Connect.com)’. This means the flow logic operates on the correct variable value without the extra escape characters.

### Question: Why are escape characters used in the logs?

In the Start Node, HTTP Node, and Custom Prebuilt Flow Logs, the platform parses the incoming JSON payload and logs the string with escape characters for accurate representation. During the flow execution, the flow uses the parsed value directly without added escape characters.