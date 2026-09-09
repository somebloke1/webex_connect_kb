The Debug Console allows you to view transaction details and historical logs for all your API, flow, and rule executions on <<prodname>>. This includes details such as event/message status, transaction timestamp, service name, source of the transaction, errors, and more.

## Understanding the Debug Console

Webex Connect has two types of logging mechanisms, and here are the differences between the two types:

- Realtime Logs: Realtime logs contain data recorded at high speed, enabling quick querying and analysis.
- Buffered Logs : Buffered logs are designed for high-volume traffic that doesn’t demand frequent analysis or querying. They are recorded at a slower pace than Real-time logs.
- Some other differences between Realtime vs Buffered logs:

  - Real-time logs are available with a slight delay of about two minutes, while Buffered logs take some time to become accessible, potentially extending up to 10 minutes under high-traffic conditions. Additionally, querying buffered logs is slower than querying Real-time logs.
  - Real-time logs support querying data for any period within the past 30 days, whereas buffered logs are limited to querying data for a single day within the same 30-day timeframe.

  [block:image]{"images":[{"image":["https://files.readme.io/cbe2479379c68b9fb3b06871324c55dd0463bae2d74707b4d1ed8b1151ad910a-dc59fa14-7ab9-41fe-b206-1af01181fb3e.png","","Screeenshot for Buffered Logs"],"align":"center","border":true,"caption":"Buffered Logs"}]}[/block]
- The default querying period is 30 days. However, if [archive search](https://help.imiconnect.io/docs/archive-search) is enabled and the retention period is set for archive search, then records of up to a maximum range of 60 to 90 days can also be queried at a time in both tabs i.e., Channels and Integrations. 
- Decrypting Logs - Logs are visible in the encrypted mode by default. The Decrypt Logs button is enabled for users who have permissions associated with their user account. If permissions are granted, then the Decrypt Logs button is enabled for the user. The <<prodname>> platform uses AES and secure key for encrypting personal information.
  > 📘 Note
  > 
  > For Outbound Logs - **To**, **Message Body**, and **Payload** are the encrypted fields.
  > 
  > For Inbound Logs - **From**, **Message**, or any personal information are the encrypted fields.  
  > When you click Decrypt Logs, the logs are decrypted using the Master Key associated with your tenant. The Master Key must be auto regenerated on regular intervals, with '**1**' month being the minimum and '**60**' months being the maximum. The default interval is 12 months. Reach out to your account manager for configuration-related information.
- Refresh - The Refresh button allows you to refresh the query pages if filters are changed or any other changes are made. The Refresh button is enabled when you search for any transaction logs.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1914b2e-1.jpg",
        "Debug Console.jpg",
        "Image showing the Debug Console interface"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Debug Console"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/920ab82-2.jpg",
        "",
        "Image showing the Debug Console interface"
      ],
      "align": "center",
      "caption": "Screenshot displaying the Debug Console"
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "S.No",
    "h-1": "Element",
    "h-2": "Description ",
    "0-0": "1",
    "0-1": "Channels or Integrations tab  \n(Mandatory for performing a query)",
    "0-2": "This represents the primary option. You must specify the type of logs you are searching for.  The Channels tab shows the channel transaction logs and the integration logs shown in the Integrations tab assist in reviewing logs related to integrations, such as Prebuilt Integrations.",
    "1-0": "2",
    "1-1": "Select Time Range  \n(Mandatory for performing a query)",
    "1-2": "Select the time range for which you want to query the logs.",
    "2-0": "3",
    "2-1": "Channel Selection  \n(Optional for performing a query)",
    "2-2": "Choose a channel for which you want to query the log.  \nIt is a single selection. Not selecting any channel will query all the transaction logs for all channels for the selected time range.",
    "3-0": "4",
    "3-1": "Channel Identifier  \n(Optional for performing a query)",
    "3-2": "Enter the channel Identifier for which you want to perform the query.  \nExample – For SMS channel the channel identifier is MSISDN, for Email channel it is emailID.  \nPopular use case - querying with channel identifier allows you to fetch all the transaction logs for a customer. Example – Assume a user’s email is [ABC@abc.com](mailto:ABC@abc.com). Querying with  Email as channel and [ABC@abc.com](mailto:ABC@abc.com) as the channel identifier will fetch all the transaction logs in the selected time range for the user [ABC@abc.com](mailto:ABC@abc.com).",
    "4-0": "5",
    "4-1": "Select Service  \n(Optional for performing a query)",
    "4-2": "This option allows you to fetch transaction logs that are executed within a specific Service or using the service key associated with that Service.",
    "5-0": "6",
    "5-1": "Source  \n(Optional for performing a query)",
    "5-2": "Choose either All or any combination of Flow, Messaging API, and Rule. This option enables you to filter the query based on the specific part of the platform where the transaction occurred. For instance, if a message was sent using a Send node in the Flows, selecting Flows as the source will retrieve transactions specifically performed through flows. On the other hand, if Messaging API and Rule are selected as sources, the query will fetch a list of transactions executed using both the Messaging API and Rule.",
    "6-0": "7",
    "6-1": "Search by Transaction ID  \n(Optional for performing a query)",
    "6-2": "Perform the query using a Transaction ID i.e., the transaction identifier that the Webex Connect platform returns as part of the response payload when you invoke the messages API to send a message, or invoke a flow using Custom Event API v1 or Inbound Webhook.",
    "7-0": "8",
    "7-1": "Search",
    "7-2": "Click Search to perform the query.  \nIt is important to note that the search button is enabled only after selecting a Time Range.",
    "8-0": "9",
    "8-1": "Decrypt Logs",
    "8-2": "Allows users to view the decrypted logs.  \nIt is important to note that the user should have ‘Decrypt Access’ to be able to see the decrypted logs.",
    "9-0": "10",
    "9-1": "Prebuilt Integration",
    "9-2": "The Prebuilt Integration is selected by default, as the Integrations tab only supports prebuilt integration logs.",
    "10-0": "11",
    "10-1": "Integration  \n(Optional for performing a query)",
    "10-2": "Select the prebuilt integration for which you wish to query logs.",
    "11-0": "12",
    "11-1": "Transaction ID  \n(Optional for performing a query)",
    "11-2": "Perform the query using a Transaction ID i.e., the transaction identifier that the <<prodname>> platform has captured as part of Prebuilt node execution.",
    "12-0": "13",
    "12-1": "Resume Key  \n(Optional for performing a query)",
    "12-2": "Search prebuilt integration transaction logs using the resume key used in the events of prebuilt node."
  },
  "cols": 3,
  "rows": 13,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> The logs typically take about two minutes to show in the flow debug console.

### Query by Transaction ID

You can search for transaction logs using the channels or transactional ID returned by the Messaging API or the Custom Event API. You can view channel-specific transaction id documentation under [Outbound Webhooks](https://developers.imiconnect.io/reference/outbound-webhooks). When you search using transaction ID, a table showing recent data associated with that transaction ID appears as shown below.  
The table contains the following details:

- Source Transaction ID – the source transaction ID. Click this ID to go to the transaction details page.
- Service Name - the service through which the transaction was initiated.
- Source - the source of the transaction - Messaging API /Flow /Rule. You can see all the transactions are grouped on the source type.
- Status - the status of the transaction - _Completed_ /_Received_ /_In Session_ /_Submitted_ /_Inactive_/ _Clicked_/ _Unresolved_. 
- Created On - the date and time on which the transaction was created.

### Querying Channels

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/52148bf-Debug_console1.jpg",
        "Debug console1.jpg",
        "Screenshot displaying the Debug Console"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Debug Console"
    }
  ]
}
[/block]


You can filter using the query parameters listed below after selecting the time range, in any number of combinations with no restrictions.

- Channel

- Destination ID

- Service

- Source

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/042ee21-DC1.jpg",
        "DebugConsole_Channels_Expanded_Transaction.png",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


When you expand the Transaction ID, you can view details such as the message associated with the transaction, its status, and the “created on” timestamp.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7e1d070-DC2.jpg",
        "DebugConsole_Channels_QuerybyTransactionID.png",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


Clicking the hyperlink on the transaction ID takes you to the Transaction Details page with additional information.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39229da-DC3.jpg",
        "DebugConsole_Channels_QuerybyTransactionID_TraceDetails.png",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


Clicking on the hyperlinks for Actions and Trace Details displays the flow transaction details and node details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4b24031-DC4.jpg",
        "DebugConsole_Channels_QuerybyTransactionID_MessageDetails.png",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


Clicking the hyperlink in the message ID of a specific transaction of the Debug Console query page takes you to the page enclosing the Message Details, Process Log, and Error & Warnings.

### Querying by Channel - Live Chat/ In-App

To query for transaction logs by Channels:

1. Select the Channel (Live Chat/ In-App Messaging) from the drop-down list.
2. Select the required service from the Service drop-down.
3. Select the Time Range.
4. Click Search.  
   All the query transactions are populated.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/64171b1-Debug_Console.jpeg",
        "Debug Console-Transactions logs.jpg",
        2676
      ],
      "align": "center",
      "border": true,
      "caption": "Transaction ID Flow Details"
    }
  ]
}
[/block]


Click the Transaction ID if you want to get further flow details. Clicking a Transaction ID link will open the transaction details page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6f77a39-Debug_Console1.jpeg",
        "Debug Console-Transactions logs1.jpg",
        2674
      ],
      "align": "center",
      "border": true,
      "caption": "Transaction ID Query"
    }
  ]
}
[/block]


> 📘 Note:
> 
> If Branded Text is enabled for your client, you can view the ‘Attempted Upgrade to’ and ‘Upgrade Result,’ on the transaction details page when querying using the Transaction ID.  
> To enable Branded Text for your number, please refer to the [Branded Text](https://help.webexconnect.io/docs/rcs-branded-text) page for more information.

> 🚧 Availability
> 
> You can only see the transaction logs for the last 30 days.

> 📘 Note
> 
> If +E.164 format is enabled for your tenant - all the sender and recipient numbers will be displayed in E.164 format.
> 
> Search will be supported with or without +E.164 format.
> 
> This format displays the number with a "+" followed by the country code and the phone number.

### Query by Channel - SMS 

To query for transaction logs by Channels:

1. Select the Channel (SMS) from the drop-down list.
2. Select the Service from the Service drop-down .
3. Select the Time Range.
4. Click Search.  
   All the the query transactions are populated.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9a61a86-SMPP_-_Debug.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


### Query by Destination ID

You can search for all the sent and received messages to a customer based on customer identity. When a user searches using Destination ID, a table showing recent data associated with that Destination ID appears.

The table contains the following details:

- **Source Transaction ID** – the source transaction ID. Click this ID to go to the transaction details page
- **Service Name** - the service through which the transaction was initiated
- **Source** - the source of the transaction - _Messaging API_ /_Flow_ /_Rule_. You can see all the transactions are grouped on the source type.
- **Status **- the status of the transaction - _Completed_ /_Received_ /_In Session_ /_Submitted_ /_Inactive_/ _Clicked_. 
- **Created On** - the date and time on which the transaction was created

You can view all the source transactions and messages grouped by Source Transaction ID in a single page view. 

List of source transactions ID’s along with message ID’s are grouped under each is shown with filter options:

- Service
- Source
- Status 
- Time Period

All the transactions are grouped according to the source type. 

Moreover, you can also check node executions of each source transaction associated with the Destination ID by clicking on the respective Source Transaction ID and/or Message ID links that redirects you to the respective details page. 

Following are the source types:

- Flow 
- Rule
- API

**Note:** Status at source transaction-level appears as per the type of transaction. Click the drill-down button of the source transaction to expand the details.

Click the Message ID if you want to get further message details. Clicking on a message ID link will open the message details page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9a5a681-1.jpg",
        "debug_destid_msg.png",
        1366
      ],
      "align": "center",
      "border": true,
      "caption": "Grouping based on Source"
    }
  ]
}
[/block]


**Note:**  

- Status column in the source transaction row is status of the flow execution but in the message id row it is message status. 
- The status filter has both flow transaction status and message status which can be selected using the list items in filter dropdown. 
- Sorting by default is by created on (latest record on top).  
- All the messages are grouped by source transaction ID, in case of flows you can see the messages grouped by flow transaction.  

| Channel                     | Identity                                                                                                                                                                                                                                                                                                                |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SMS                         | MSISDN - Phone number in E164 format                                                                                                                                                                                                                                                                                    |
| Voice                       | MSISDN - Phone number in E164 format                                                                                                                                                                                                                                                                                    |
| MMS                         | MSISDN - Phone number in E164 format                                                                                                                                                                                                                                                                                    |
| Instagram                   | IGSID - Received in the first and subsequent incoming messages from customers on Instagram message                                                                                                                                                                                                                      |
| Messenger                   | PS ID - Received in the first and subsequent incoming messages from customers on Facebook Messenger                                                                                                                                                                                                                     |
| In-app Messaging            | User ID - Can be set by the app developer by calling the SDK methods                                                                                                                                                                                                                                                    |
| WhatsApp                    | WA ID - The E164 formatted phone number of the user                                                                                                                                                                                                                                                                     |
| Push Notifications          | Push ID - Received when a user is registered for a push by the app developer                                                                                                                                                                                                                                            |
| Email                       | Email ID                                                                                                                                                                                                                                                                                                                |
| Apple Messages for Business | ABC ID - Received in the first and subsequent incoming messages from customers on Apple Messages for Business                                                                                                                                                                                                           |
| All Channels                | Customer ID - If you create a profile of the customer using the [Profile APIs ](https://developers.imiconnect.io/reference/profile-api-overview)and link the channel profiles to the user profile, you can query by customer ID which displays all messages sent to the user through <<prodname>> over the last 30 days |

> 🚧 Availability
> 
> Transaction logs are stored for up to 30 days on the platform.

## Voice calls

You can query the summary of a call by the destination​. This provides a detailed view of how the call progressed​. You can also listen to prompts played to the user and recordings.​

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/716ee67-2.jpg",
        "query-by-dest-voice.png",
        "Screenshot displaying on how to select the Query by Destination ID for Voice Calls"
      ],
      "align": "center",
      "border": true,
      "caption": "Query by Destination ID for Voice Calls"
    }
  ]
}
[/block]


## WhatsApp

Using the debug logs, you can see all the transactions and the details of each transaction.

1. Select **WhatsApp** as Channel.
2. Enter/select all the other search criteria.
3. Click **Search**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7176ce2-4.jpg",
        "WhatsApp Debug Console.jpg",
        "Screenshot displaying the Interface for debug logs with WhatsApp selected as the channel"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the transactions logs in debug console by selecting WhatsApp channel"
    }
  ]
}
[/block]


Here you can view all the transaction logs along with the status of the messages.- Read, Submitted, in-session, Delivered, Failed, Invoked, Unresolved, and so on. You can filter the logs by status.

> ❗️ 
> 
> Please note that Call Duration is showing up as Zero currently in Debug Console results when you view the details for a large number of calls at once due to a bug that's planned to be fixed in a future release. However, the duration is available when looking at an individual transaction.

Drill-down the log to view more details like message ID, direction (inbound or outbound), created date, body, source, from, to, message priority, and payload

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b2b981-5.jpg",
        "WhatsApp Debug Console1.jpeg",
        "Screenshot of view more details of message"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of view more details of message"
    }
  ]
}
[/block]


### Historical Logs

It allows you to search for all incoming and outgoing messages on a channel over a specific time period.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1e7599d-3.jpg",
        "Query by Historical logs.jpg",
        "Screenshot displaying the Historical Logs for SMS"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Historical Logs for SMS"
    }
  ]
}
[/block]


### Querying Integrations

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/40086a4-Debug_console2.jpg",
        "Debug console2.jpg",
        "Screenshot displaying on how to select Prebuilt Integrations"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying on how to select Prebuilt Integrations"
    }
  ]
}
[/block]


Before the time range is selected, only the filter parameters in the above screen capture are visible.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a088fc6-Debug_Console9.png",
        "DebugConsole_Integrations_Filters.png",
        "Screenshot displaying the Prebuilt Integration Logs"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Prebuilt Integration Logs"
    }
  ]
}
[/block]


After you select the time range and click the Search button, some additional filter criteria are displayed as shown in the above screen capture.

You can select or add the search parameters listed below in after selecting the time range, in any number of combinations with no restrictions.

[block:parameters]
{
  "data": {
    "h-0": "S.No",
    "h-1": "Search Parameters",
    "h-2": "Description",
    "0-0": "1.",
    "0-1": "Prebuilt Integrations",
    "0-2": "This option is preselected because the debug console currently supports only prebuilt integration logs. You cannot change this selection.",
    "1-0": "2.",
    "1-1": "Integration (Optional)",
    "1-2": "Select the name of the prebuilt integration for which you want to view logs. If you do not select an integration, the search returns logs for all integration executions in your tenant.",
    "2-0": "3.",
    "2-1": "Transaction ID (Optional) ",
    "2-2": "Enter a prebuilt integration transaction ID to find a specific transaction.",
    "3-0": "4.",
    "3-1": "Resume Key  \n(Optional)",
    "3-2": "Enter a Resume Key to find transactions where this key was used.",
    "4-0": "5.",
    "4-1": "Node (Optional)",
    "4-2": "Select the node for which you want to view logs. An integration can have one or more nodes.",
    "5-0": "6.",
    "5-1": "Method (Optional)",
    "5-2": "Select the method for which you want to view logs. A node can have one or more methods.",
    "6-0": "7.",
    "6-1": "Service (Optional)",
    "6-2": "Fetch transaction logs executed within a specific service.",
    "7-0": "8.",
    "7-1": "Source",
    "7-2": "Displays the flow name under which the integration, node, or method was executed.",
    "8-0": "9.",
    "8-1": "Status",
    "8-2": "Displays the status code received after method or node execution."
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/401d10b-Debug_Console10.png",
        "DebugConsole_Integrations_FlowDetails_Expand.png",
        "Image showing the Flow Transaction Details."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Flow Transaction Details"
    }
  ]
}
[/block]


Clicking the expand button next to a flow transaction displays the request details by the connect system to the integrating system and the response received from the integrating system.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5ed6b6d-Debug_Console11.png",
        "DebugConsole_Integrations_Flow_TraceDetails.png",
        "Image showing the Flow Transaction Details."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Flow Transaction Details"
    }
  ]
}
[/block]


Clicking on the hyperlink of the flow transaction takes you to the flow transaction details page. Clicking o the hyperlinks for Actions and Trace Details displays related information on the screen.

Types of Flow Transactions

\*There are three types of flow transactions. They are indicated in the **Type **column of the main query page.

\*Node Outbound: Refers to API calls sent by the <<prodname>> system to the integrating system.

\*Inbound Event: Refers to API calls sent by the integrating system to the <<prodname>> system.

\*Async Event: Refers to API calls sent to the integrating system for which response is received after a certain time lag.

### Unresolved Status

When a message or event received from an end customer is not resolved to any flow and/or rule (i.e., no trigger condition matched with the incoming message or event), such messages and events for all channels are categorised as 'Unresolved' in the Debug Console. The same happens for Inbound Webhooks and Event API triggers that are not mapped with any Flow and/or Rule.

To see the list of the unresolved messages and events:

1. Go to Debug Console.
2. Select the Channel for which you want to see the unresolved messages and events.
3. Select the Time Range.
4. Select any other search criteria you want.
5. Click Search.
6. From the search results, filter the Status column to display Unresolved.
7. Click any transaction to see the details.

You can see that the status is Unresolved, Source and Service are NA (Not Applicable), and the Rules Triggered is 0, because the transaction is not resolved.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0159769-Unresolved1.jpg",
        null,
        "Image showing the Transaction Details interface with an Unresolved Status highlighted."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Unresolved Status in Transaction Details"
    }
  ]
}
[/block]