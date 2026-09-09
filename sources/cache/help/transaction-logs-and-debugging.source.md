Flow Debug provides a step-wise execution trace for your recent flow executions. You can find and fix problems in your flows using Flow Debug. This capability is typically meant to be used for troubleshooting purposes while configuring and iterating flows. We recommend you to use Debug Console for viewing old transaction logs.

You can launch the flow debug panel using the **Flow Debug** icon at the right navigation panel of your flow canvas. The **Flow Debug** panel opens in a split view at the bottom of your flow and displays a list of 10 most recent flow runs. Typically logs take about two minutes to show in the flow debug section. You may not see the logs for a recently initiated transaction immediately.

- Click the transaction ID to drill down to the details of each flow run (transaction)
- Filter the flow executions using the transaction ID 
- Filter the logs based on selected date range and time (Logs are available for the latest 30 days).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7a1cc13-2.jpg",
        "debug_canvas_split_view.png",
        "Debug -  Canvas split view"
      ],
      "align": "center",
      "border": true,
      "caption": "Debug - Canvas split view"
    }
  ]
}
[/block]


The information captured within logs is segregated into three levels based on the sensitivity of the data and the level of detail:<br>

- Level 1: Summary Logs
- Level 2: Sequence Summary
- Level 3: Node Execution Details.

You can now see the timezone along with the timestamp in the transaction logs.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bc3a21a-1.jpg",
        "transaction_logs_debug_console.png",
        "Transaction Logs Screen"
      ],
      "align": "center",
      "border": true,
      "caption": "Transaction Logs Screen"
    }
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/56dd4d9-3.jpg",
        "node_level_execution_details.png",
        800
      ],
      "align": "center",
      "border": true,
      "caption": "Node Level Execution Details"
    }
  ]
}
[/block]


In the case of voice flows, you can see the various voice nodes within the flow and the sequence in which the nodes are executed. If the flow contains the voice node group, then you can drill down to the individual nodes in the group.

When a voice flow has recordings, you can click **Recordings** to play the recordings directly in the debug console. You can also see the call duration and audio prompts configured and played to the caller during an ongoing call.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bc3a21a-1.jpg",
        "transaction_logs_debug_console.png",
        "Voice Flows - Transaction Logs"
      ],
      "align": "center",
      "border": true,
      "caption": "Voice Flows - Transaction Logs"
    }
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Event in Start node",
    "h-2": "Parameters to be shown in transaction logs",
    "0-0": "SMS",
    "0-1": "Mobile originated -MO",
    "0-2": "Timestamp  \nSender Number  \nService Number  \nMessage",
    "1-0": "SMS",
    "1-1": "On Link click",
    "1-2": "Timestamp  \nSender Number ",
    "2-0": "Voice",
    "2-1": "Inbound call",
    "2-2": "Service Number  \nTimestamp  \n MSISDN ",
    "3-0": "Voice",
    "3-1": "Missed  call",
    "3-2": "Service Number  \nTimestamp  \nMSISDN ",
    "4-0": "MMS",
    "4-1": "Mobile originated -MO",
    "4-2": "Sender Number ",
    "5-0": "Messenger",
    "5-1": "Incoming Message",
    "5-2": "AppId  \nPSID  \nMessage  \nAttachment URL  \nTimestamp  \nLocation URL ",
    "6-0": "Messenger",
    "6-1": "On link click",
    "6-2": "AppId  \nPSID  \nTim_estamp ",
    "7-0": "Messenger",
    "7-1": "Postback",
    "7-2": "AppId  \nPSID  \nTimestamp  \nPost_back Payload ",
    "8-0": "WhatsApp",
    "8-1": "Incoming Message",
    "8-2": "AppId  \nWaId  \nTimestamp  \nMessage  \nImage URL  \nLocation URL  \nVoice URL  \nAudio URL  \nVideo URL  \nSticker URL ",
    "9-0": "WhatsApp",
    "9-1": "Postback",
    "9-2": "AppId  \nWaId  \nTimestamp  \nButton Payload ",
    "10-0": "WhatsApp",
    "10-1": "List Message",
    "10-2": "AppId  \nWaId  \nTimestamp  \nList Description  \nRow Title  \nRow Identifier ",
    "11-0": "WhatsApp  \n  \nReply button Message",
    "11-1": "",
    "11-2": "AppId  \nWaId  \nTimestamp  \nReply Button Title  \nReply Button Identifier ",
    "12-0": "In-App / Live Chat",
    "12-1": "Custom event",
    "12-2": "UserId  \nPushId  \nTimestamp  \nAppId",
    "13-0": "In-App / Live Chat",
    "13-1": "Incoming Message",
    "13-2": "Timestamp  \nUserId  \nPushId  \nMessage  \nAttachments  \nDeviceId  \nVersion  \nThreadid",
    "14-0": "In-App / Live Chat",
    "14-1": "On thread close",
    "14-2": "Threadid  \nAppId  \nUserId",
    "15-0": "In-App / Live Chat",
    "15-1": "On postback",
    "15-2": "Timestamp  \nUserId  \nPushId  \nMessage  \nAttachments  \nDeviceId  \nVersion  \nThreadId  \nButton Payload",
    "16-0": "Email",
    "16-1": "Incoming Message",
    "16-2": "Message  \nEmailid  \nAppId  \nTo Address  \nAttachments  \nReceipts  \nTimestamp",
    "17-0": "Email",
    "17-1": "Subscribe",
    "17-2": "Emailid  \nAppId  \nAttachments  \nTimestamp",
    "18-0": "Email",
    "18-1": "unsubscribe",
    "18-2": "EmailId  \nAppId  \nAttachments  \nTimestamp",
    "19-0": "RCS",
    "19-1": "Incoming Message",
    "19-2": "Text  \nTimestamp  \nAppId  \nNumber",
    "20-0": "RCS",
    "20-1": "Message  \nIncoming attachment",
    "20-2": "Text  \nTimestamp  \nAppId  \nNumber  \nFile URL",
    "21-0": "RCS",
    "21-1": "Location response",
    "21-2": "Text  \nTimestamp  \nAppId  \nNumber",
    "22-0": "RCS",
    "22-1": "Postback",
    "22-2": "Text  \nTimestamp  \nAppId  \nNumber  \nPostback Data",
    "23-0": "Apple Messages for Business",
    "23-1": "Conversation closed",
    "23-2": "ABCUserId  \nAppId",
    "24-0": "Apple Messages for Business",
    "24-1": "Interactive Message authentication",
    "24-2": "AppId  \nAuthToken  \nAuthStatus",
    "25-0": "Apple Messages for Business",
    "25-1": "Interactive Message list picker",
    "25-2": "ABCUserId  \nAppId  \nTimestamp  \nDate Picker Time Slot  \nDate Picker Duration  \nTime Slot Identifier  \nTime Slot Start Time  \nList Picker Items  \nList Picker Other Items",
    "26-0": "Apple Messages for Business",
    "26-1": "Interactive Message payment",
    "26-2": "ABCUserId  \nAppId  \nTimestamp  \nPayment Status",
    "27-0": "Apple Messages for Business",
    "27-1": "Incoming Message",
    "27-2": "ABCUserId  \nAppId  \nTimestamp  \nMessage  \nAttachment URL",
    "28-0": "Apple Messages for Business",
    "28-1": "Interactive Message quick reply",
    "28-2": "ABCUserId  \nAppId  \nTimestamp  \nSelected Identifier  \nSelected Index",
    "29-0": "Apple Messages for Business",
    "29-1": "Interactive Message form response",
    "29-2": "ABCUserId  \nAppId  \nTimestamp  \nSelections  \nSelections Count",
    "30-0": "Apple Messages for Business",
    "30-1": "Typing indicator",
    "30-2": "ABCUserId  \nAppIdAppId  \nType",
    "31-0": "Apple Messages for Business",
    "31-1": "Interactive Message new authentication",
    "31-2": "AppId  \nAuthToken  \nAuthStatus",
    "32-0": "Apple Messages for Business",
    "32-1": "Interactive Message iMessage extension",
    "32-2": "AppId  \nURL",
    "33-0": "Custom event",
    "33-1": "",
    "33-2": "Payload  \nTimestamp",
    "34-0": "Google Business Messages",
    "34-1": "Incoming Message",
    "34-2": "AppId  \nConversationId  \nAgentId  \nSend Time  \nMessageId  \nText",
    "35-0": "Google Business Messages",
    "35-1": "User Status",
    "35-2": "AppId  \nConversationId  \nAgentId  \nSend Time  \nIsTyping  \nRequested Live Agent",
    "36-0": "Google Business Messages",
    "36-1": "Survey Response",
    "36-2": "AppId  \nConversationId  \nAgentId  \nSend Time  \nSurveyId  \nQuestion Response Text  \nQuestion Response Postback Data  \nQuestionIndex",
    "37-0": "Google Business Messages",
    "37-1": "Suggestion Response",
    "37-2": "AppId  \nConversationId  \nAgentId  \nSend Time  \nMessageId  \nPostback Data  \nText  \nSuggestion Type ",
    "38-0": "Instagram",
    "38-1": "Incoming Message",
    "38-2": "MessageId  \nIgsid  \nIgid  \nTimestamp  \nUserId  \nAppId  \nMessage Type  \nAttachment Type  \nAttachment Url  \nStory Reply Url  \nReplied MessageId",
    "39-0": "Instagram",
    "39-1": "Message Deleted",
    "39-2": "MessageId  \nIgsid  \nIgid  \nTimestamp  \nUserId  \nAppId  \nIsDeleted",
    "40-0": "Instagram",
    "40-1": "Postback",
    "40-2": "MessageId  \nIgsid  \nIgid  \nTimestamp  \nUserId  \nAppId  \nPayload  \nTitle  \nQuick Reply Payload"
  },
  "cols": 3,
  "rows": 41,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


Inbound events 

The following parameters are displayed in the Debug flow of the Receive Node:

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Events in Receive node",
    "h-2": "Parameters to be shown in transaction logs",
    "0-0": "SMS  \n  \n·     ",
    "0-1": "",
    "0-2": "Sender Number  \nService Number  \nMessage  \nAttachment  \nTimestamp",
    "1-0": "Voice",
    "1-1": "",
    "1-2": "MSISDN  \nService Number  \nMessage  \nTimestamp",
    "2-0": "Messenger",
    "2-1": "Incoming Message",
    "2-2": "PSID  \nAppId  \nMessage  \nAttachments  \nTimestamp",
    "3-0": "Messenger",
    "3-1": "Postback",
    "3-2": "PSID  \nAppId  \nPayload  \nTimestamp",
    "4-0": "WhatsApp",
    "4-1": "Incoming Message",
    "4-2": "AppId  \nWaId  \nTimestamp  \nMessage  \nImage URL  \nLocation URL  \nVoice URL  \nAudio URL  \nVideo URLSticker URL",
    "5-0": "WhatsApp",
    "5-1": "Postback",
    "5-2": "AppId  \nWaId  \nTimestamp  \nButton Payload",
    "6-0": "WhatsApp",
    "6-1": "List Message",
    "6-2": "AppId  \nWaId  \nTimestamp  \nList Description  \nRow Title Row Identifier",
    "7-0": "WhatsApp",
    "7-1": "Reply button Message",
    "7-2": "AppId  \nWaId  \nTimestamp  \nReply Button Title  \nReply Button Identifier",
    "8-0": "Custom event",
    "8-1": "",
    "8-2": "Payload",
    "9-0": "In-App / Live Chat",
    "9-1": "Incoming Message",
    "9-2": "Timestamp  \nUserId  \nPushId  \nMessage  \nAttachments  \nDeviceId  \nVersion  \nThreadId",
    "10-0": "In-App / Live Chat",
    "10-1": "Form response",
    "10-2": "Timestamp  \nUserId  \nPushId  \nForm Response  \nAttachments  \nDeviceIdVersion  \nThreadId",
    "11-0": "In-App / Live Chat",
    "11-1": "Postback",
    "11-2": "Timestamp  \nUserId  \nPushId  \nMessage  \nAttachments  \nDeviceId  \nVersion  \nThreadId  \nButton Payload",
    "12-0": "Apple Messages for Business",
    "12-1": "Interactive Message Time picker",
    "12-2": "ABCUserId  \nAppId  \nTimestamp  \nMessage  \nAttachment URL  \nDate Picker Timeslot  \nDate Picker Duration  \nTime Slot Identifier  \nTime Slot Start Time",
    "13-0": "Apple Messages for Business",
    "13-1": "Interactive Message authentication",
    "13-2": "AuthToken  \nAuthStatus",
    "14-0": "Apple Messages for Business",
    "14-1": "Interactive Message list picker",
    "14-2": "ABCUserId  \nAppId  \nTimestamp  \nList Picker Items  \nList Picker Other Items",
    "15-0": "Apple Messages for Business",
    "15-1": "Interactive Message payment",
    "15-2": "ABCUserId  \nAppId  \nTimestamp  \nPayment Status",
    "16-0": "Apple Messages for Business",
    "16-1": "Interactive Message form response",
    "16-2": "ABCUserId  \nAppId  \nTimestamp  \nSelections  \nSelections Count",
    "17-0": "Apple Messages for Business",
    "17-1": "Conversation closed",
    "17-2": "ABCUserId  \nAppId",
    "18-0": "Apple Messages for Business  ",
    "18-1": "Interactive Message new authentication",
    "18-2": "AppId  \nAuthToken  \nAuthStatus",
    "19-0": "Apple Messages for Business",
    "19-1": "Interactive Message quick reply",
    "19-2": "ABCUserId  \nAppId  \nTimestamp  \nSelected Identifier  \nSelected Index",
    "20-0": "Apple Messages for Business  ",
    "20-1": "Typing indicator",
    "20-2": "ABCUserId  \nAppId  \nType",
    "21-0": "Apple Messages for Business",
    "21-1": "Interactive Message iMessage extension",
    "21-2": "AppId  \nURL",
    "22-0": "Apple Messages for Business  ",
    "22-1": "Incoming Message",
    "22-2": "ABCUserId  \nAppId  \nTimestamp  \nMessage  \nAttachment URL",
    "23-0": "RCS",
    "23-1": "Incoming attachment",
    "23-2": "Text  \nTimestamp  \nAppId  \nNumber",
    "24-0": "RCS  ",
    "24-1": "Incoming Message",
    "24-2": "Text  \nTimestamp  \nAppId  \nNumber  \nFile URL",
    "25-0": "RCS",
    "25-1": "Location response",
    "25-2": "Text  \nTimestamp  \nAppId  \nNumber",
    "26-0": "RCS  ",
    "26-1": "Postback",
    "26-2": "Text  \nTimestamp  \nAppId  \nNumber  \nPostback Data"
  },
  "cols": 3,
  "rows": 27,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


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

<<prodname>> logs the list of the variables created or updated in node executions for all flow transactions under the 'Variables created/updated during node execution' section as shown below. The parameters which meet one of the following conditions will be listed in this section:

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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6afcc49-4.png",
        "",
        "Receive Node - Transaction Logs  "
      ],
      "align": "center",
      "border": true,
      "caption": "Receive Node - Transaction Logs"
    }
  ]
}
[/block]


## FAQs

### Question: Why are there escape characters (like forward slash '\') in the JSON parameters shown in the logs of <<prodname>> Flow Builder, especially in the Start Node or when using HTTP/Custom/Prebuilt Integration nodes? Do these characters alter the variable values at runtime?

No, the values of your variables are not altered during runtime. The escape characters you see (such as forward slash - \) are only added for representation purposes in the logs. They help display the raw JSON structure and ensure special characters are visible and preserved in the log output. For example, if your incoming JSON parameter is: {"email": "[Connect@Connect.com](mailto:Connect@Connect.com)"}, in the flow Debug Logs the value of email parameter may appear as: \"[Connect@Connect.com](mailto:Connect@Connect.com)\" . Here, the forward slash are just to "escape" the quotation marks inside the JSON string for clear display. At runtime, the actual value used in your flow (e.g., in Transition Actions) is the real, unescaped value - ‘[Connect@Connect.com](mailto:Connect@Connect.com)’. This means the flow logic operates on the correct variable value without the extra escape characters.

### Question: Why are escape characters used in the logs?

In the Start Node, HTTP Node, and Custom Prebuilt Flow Logs, the platform parses the incoming JSON payload and logs the string with escape characters for accurate representation. During the flow execution, the flow uses the parsed value directly without added escape characters.