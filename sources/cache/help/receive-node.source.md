The receive node allows you to wait for a response from the user. The response can be a message, a voice call, or an event like a button click (for example, **Accept** button in an interactive push notification) or a selection from a list (for example, choosing an option from a List Picker on <<AMB>>). <br>

You can also use the receive node to wait for external events to occur before resuming the flow. For example, a web application can resume the flow by invoking a custom event API when a user visits a website and fills an inquiry form.<br> 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63a62d6-Receive.jpg",
        "Receive.jpg",
        "Screenshot of Receive Node."
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Receive Node"
    }
  ]
}
[/block]


## Node Configuration

Double-click the node to configure it. Select the desired _channel_ to wait for a message or a _custom event_ to wait for an event. You can configure multiple channels/custom events on a single receive node. <br>

Specify the duration (in seconds), in the **Max Timeout** field, for which the node waits to receive a message on the selected channel(s). If there is no incoming message/event within the specified time period, the flow exits the node from **ontimeout** edge.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ae800ca-Receive.jpg",
        "Receive Node Receive Node Configuration.png",
        "Screenshot of Receive Node Configuration"
      ],
      "align": "center",
      "border": true,
      "caption": "Receive Node Configuration"
    }
  ]
}
[/block]


## Channels and Events

The configuration window lists all the channels that the receiving node supports. The following table lists and explains all the required configurations for each of the channels:

[block:parameters]
{
  "data": {
    "h-0": "Channel - Property/Event",
    "h-1": "Description",
    "0-0": "**SMS** ",
    "0-1": "An inbound message (through SMS) from the user resumes the flow",
    "1-0": "Number",
    "1-1": "The number on which the user sends the message. This is the number you own on the platform.  \n  \nPlease note that the platform provides an option to select numbers from the dropdown along with an option for Dynamic Configuration. If you decide to use the dynamic configuration, you will need to select the list of Sender IDs you wish to use in your flow through the dynamic number configuration. This extra step is needed to associate the flow with respective Sender IDs.  \n  \nYou will be required to make this selection once you publish your flow by clicking on the Make Live button.",
    "2-0": "Keyword",
    "2-1": "A unique string received from the user to trigger the flow",
    "3-0": "From Number",
    "3-1": "The number from which the user sends the message",
    "4-0": "**Voice** ",
    "4-1": "An inbound voice call from the user resumes the flow",
    "5-0": "Voice Number",
    "5-1": "The number used to make outbound voice calls to the users. This is the number you own on the platform.",
    "6-0": "From",
    "6-1": "The number from which the user makes a voice call",
    "7-0": "**MMS**",
    "7-1": "An inbound message (through MMS) from the user resumes the flow",
    "8-0": "Number",
    "8-1": "The number on which the user sends the message. This is the number you own on the platform.",
    "9-0": "From Number",
    "9-1": "The number from which the user sends the message",
    "10-0": "**Messenger Message/Event**",
    "10-1": "An inbound message (through Messenger) from the user resumes the flow",
    "11-0": "From PSID",
    "11-1": "The PSID from which the user sends a message",
    "12-0": "Event Name:  \n  \nIncoming Message  \n  \nPostback ",
    "12-1": "Incoming Message event is triggered when a message has been sent to your Page.  \n  \nPostback occur when a postback button, Get Started button, or persistent menu item is tapped",
    "13-0": "**Instagram Message**   (Deprectaed) ",
    "13-1": "An inbound message (through Instagram) from the user resumes the flow.",
    "14-0": "From IGSID",
    "14-1": "The IGSID from which the user sends a message.",
    "15-0": "Event Name:  \n  \nIncoming Message  \n  \nPostback  \n  \nDelete Message",
    "15-1": "Incoming Message - This event occurs every time a user sends a text message with or without attachments to your Instagram account.  \n  \nPostback - This event is triggered when user clicks postback type button.  \n  \nMessage Deleted - This event occurs every time a user sends a delete message to your Instagram account.",
    "16-0": "**WhatsApp Message**",
    "16-1": "An inbound WhatsApp from the user resumes the flow.",
    "17-0": "From WhatsAppID",
    "17-1": "The number from which the user sends a WhatsApp message",
    "18-0": "Sender Name",
    "18-1": "The username from which the message is sent",
    "19-0": "Event Name:  \n  \nIncoming Message  \n  \nPostback  \n  \nList Message  \n  \nReply Buttons message",
    "19-1": "The event triggered by the user's response  \nIf a user taps a quick reply button, postback event is be used to process the event  \nThis event occurs every time a user selects one of the List Message options  \nThis event occurs every time a user selects one of the Reply Buttons  options",
    "20-0": "**Custom Event** ",
    "20-1": "The selected custom event resumes the flow along with post data from the event available as 'session data'",
    "21-0": "Custom Event",
    "21-1": "The trigger of the specified custom event resumes the flow",
    "22-0": "Resume Key",
    "22-1": "A unique key (per session) passed along with the custom event that resumes the flow",
    "23-0": "Value",
    "23-1": "A value for the resume key",
    "24-0": "Add Another Resume Key-Value",
    "24-1": "A button that lets you add another resume key-value pair",
    "25-0": "**Live Chat / In-App Messaging**",
    "25-1": "An inbound message within the app that resumes the flow",
    "26-0": "From (ThreadID)",
    "26-1": "A variable that contains thread id of the incoming message on the app",
    "27-0": "From (UserID)",
    "27-1": "The user id from which the app user sends the message",
    "28-0": "Event Name:  \n  \nIncoming Message  \n  \nPostback  \n  \nForm Response ",
    "28-1": "The event triggered by the user's response  \n  \nWhen a user taps on a quick reply button, or a button of type postback within a template message, then the response is received back on the platform as a Postback event.  \n  \n_Note: If you are configuring the receive node to wait on multiple live chat / in-app message response types at once, configure the 'Form Response' message type as the first to be able to configure the Form Response Content Type and Form Template details. Due to a bug, you won't be able to configure these if you don't configure Form Response as the first response event._",
    "29-0": "Content Type:  \n  \nStatic  \n  \nDynamic",
    "29-1": "If Static is selected as Content Type, select the Form template to receive the Form Response  \n  \nIf Dynamic is selected as Content Type, the output variable corresponding to the form will hold the entire payload which is received as the Form Response",
    "30-0": "Form Template",
    "30-1": "Select the required template when the Content Type is Static",
    "31-0": "**Email** ",
    "31-1": "An inbound email from the user resumes the flow  \n_Note: If the incoming email attachments contains.msg files,the.msg attachments sent by customers might not be delivered to businesses if sent from MS Outlook email client due to an issue with MS Outlook._",
    "32-0": "From (EmailID)",
    "32-1": "The email id from which the users sends the message​​​.  \nThe platform will not trigger or resume a flow, nor trigger a rule or an outbound webhook notification for incoming emails where Sender Email ID is same as the Recipient Email ID. However, details of such incoming emails will be available within Export Logs.  \n  \nFor email sent via SMTP channel, we do not support delivery tracking.",
    "33-0": "**<<AMB>> Message/Event**",
    "33-1": "An inbound <<AMB>> message or event from the user resumes the flow.",
    "34-0": "From (<<AMB>> ID)",
    "34-1": "The ID from which the customer sends a message on Apple Messages for Business. For invitation responses, enter the variable that contains the AMB opaque ID or the customer's mobile number.",
    "35-0": "Event Name:  \n  \nIncoming Message  \n  \nInteractiveMessageResponse: Invitation  \n  \nInteractiveMessageResponse: QuickReply  \n  \nInteractiveMessageResponse: ListPicker  \n  \nInteractiveMessageResponse: TimePicker  \n  \nInteractiveMessageResponse: FormMessage  \n  \nInteractiveMessageResponse: Payment  \n  \nInteractiveMessageResponse: ClassicalAuthentication  \n  \nInteractiveMessageResponse: NewAuthentication  \n  \nInteractiveMessageResponse: iMessageApp",
    "35-1": "The event triggered by the customer's response.  \n  \n`InteractiveMessageResponse: Invitation` resumes the flow when the customer responds to an Apple Messages for Business invitation message.",
    "36-0": "**RCS Message/Event** ",
    "36-1": "An inbound RCS message/event from the user resumes the flow",
    "37-0": "From MSISDN",
    "37-1": "The mobile number from which the user sends a message an RCS message",
    "38-0": "Event Name:  \n  \nIncoming Message  \n  \nPostback Response  \n  \nIncoming Attachment  \n  \nLocation Response ",
    "38-1": "The event triggered by the user's response"
  },
  "cols": 2,
  "rows": 39,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> For `InteractiveMessageResponse: Invitation`, the **From** field can contain the AMB opaque ID or the customer's mobile number. |

## Waiting for an Apple Messages for Business Invitation Response

You can configure the Receive node to wait for a customer's response to an Apple Messages for Business invitation message. The node resumes the flow when the customer responds to the invitation before the configured timeout.

To configure the Receive node for invitation response:

1. Double-click the **Receive** node.
2. Select **Apple Messages for Business** as the channel.
3. In **Event Name**, select `InteractiveMessageResponse: Invitation`.
4. In the **From** field, enter the variable that contains the customer's mobile number or AMB opaque user ID.
5. Specify the **Max Timeout** value.
6. Click **Save**.

**Note:** For invitation responses, Webex Connect can match the inbound response using the customer mobile number. After the customer responds, Webex Connect resolves the AMB opaque user ID, which can be used for subsequent standard Apple Messages for Business messages.

### AMB Invitation Response Output Variables

The following output variables are available when the Receive node resumes for an Apple Messages for Business invitation response:

| Output Variable          | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| `abc.abcUserId`          | Resolved Apple Messages for Business user ID.                                     |
| `abc.msisdn`             | Customer mobile number used for the invitation, when available.                   |
| `abc.invitationAccepted` | `true` if the customer selected **Yes**. `false` if the customer selected **No**. |
| `abc.invitationResponse` | Full invitation response payload.                                                 |
| `abc.requestIdentifier`  | Request identifier associated with the invitation response.                       |
| `abc.timestamp`          | Timestamp when the event was received.                                            |
| `abc.locale`             | Locale received in the invitation response, when available.                       |
| `receive.message`        | Message or response value received by the Receive node.                           |
| `receive.channel`        | Channel on which the response was received.                                       |
| `receive.payload`        | Payload received by the Receive node.                                             |
| `receive.attachment`     | Attachment details, if any.                                                       |

## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](doc:variable-management).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/97011e9-5.png",
        "fb72125-receive_input_variables.png",
        "Screenshot of Input and Custom Variables"
      ],
      "align": "center",
      "border": true,
      "caption": "Input and Custom Variables"
    }
  ]
}
[/block]


> 📘 Note
> 
> All the numbers in the **To field** are represented using the "E+164" format. This format displays the number with a "+" followed by the country code and the phone number. This is not applicable to the numbers in the From field.

## Output Variables

The node-level [variables](doc:variable-management) are auto-generated by each node and can be referenced in other nodes later in the flow. The auto-generated output variables contain the data that a node produces when the flow execution passes through that node. These variables are prefixed with the node id allowing unique access to each of these variables. For example, the customer response that a receive node captures is stored in the `nodeid.receive.message` output variable.<br>

> 📘 Note
> 
> The tables below provide a standard list of Receive Node and Start Node output variables.

The receive node has a set of output variables based on the channel. 

> 👍 PCI and Malware Scanning related Output Variables
> 
> Please note that PCI and Malware scanning related Output Variables documented below are applicable and available only when Webex CC or CCE integration is enabled for your Webex Connect tenant.

For more information, see the following tables:

**SMS Node Output Variables**

> 📘 Keyword in Incoming Message
> 
> The first word of an incoming message is used to determine if it matches a configured keyword. If the message consists of only that one word and it matches, only the `sms.keyword` parameter is set, while the `sms.message` parameter remains empty.
> 
> If the incoming message contains more than one word, and the first word matches the keyword, the `sms.keyword` parameter is set to that first word, and the rest of the message is stored in the sms.message parameter.
> 
> **Example**:  
> For the incoming message "stop this message", `sms.keyword` is set to "stop", and `sms.message` is set to "this message".

[block:parameters]
{
  "data": {
    "h-0": "Incoming Event",
    "h-1": "Output Variables",
    "h-2": "Description",
    "h-3": "Example",
    "0-0": "Mobile Originated - MO",
    "0-1": "sms.keyword",
    "0-2": "Contains the keyword, if the incoming message has a keyword configured.",
    "0-3": "Key",
    "1-0": "",
    "1-1": "sms.serviceNumber",
    "1-2": "The user's number the customer is sending the message to.  \nPrefix the inbound number with the correct country code.",
    "1-3": "4.47521E+11",
    "2-0": "",
    "2-1": "sms.message",
    "2-2": "Incoming text message from end-customer.",
    "2-3": "Flow",
    "3-0": "",
    "3-1": "sms.timestamp",
    "3-2": "Record of the time when the request is received on <<prodname>> platform. For e.g. 1582627917.",
    "3-3": "2020-02-25T07:10:45.051Z",
    "4-0": "",
    "4-1": "sms.transId",
    "4-2": "Unique identifier corresponding to the transaction.",
    "4-3": "234190eb-df62-45c8-9281-c4b6f5b09c20",
    "5-0": "",
    "5-1": "sms.senderNumber",
    "5-2": "Number of the customer's handset from where the incoming message is originating.",
    "5-3": "9.19676E+11",
    "6-0": "On Link Click",
    "6-1": "sms.linkStatus",
    "6-2": "",
    "6-3": "Active",
    "7-0": "",
    "7-1": "sms.timestamp",
    "7-2": "Record of the time when the request is received on <<prodname>> platform.",
    "7-3": "2020-02-21T09:41:37.517Z",
    "8-0": "",
    "8-1": "sms.transId",
    "8-2": "Unique identifier corresponding to the transaction.",
    "8-3": "8f02482e-060c-4d07-8256-66791830e71c_85218130063343228",
    "9-0": "",
    "9-1": "sms.senderNumber",
    "9-2": "Number of the customer's handset from where the incoming message is originating.",
    "9-3": "9.19676E+11"
  },
  "cols": 4,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 🚧 Note
> 
> It is mandatory to use the exact country code (for example, +44, +1) as the prefix to the numbers. Numbers without country code may lead to error in the receive node. "0" is not accepted as a valid country code.

**Voice Node Output Variables**

| Incoming Event | Output Variables    | Description                                                                                           | Example    |
| :------------- | :------------------ | :---------------------------------------------------------------------------------------------------- | :--------- |
| Missed Call    | voice.timestamp     | Record of the time when the request is received on <<prodname>> platform.                             | 1582627917 |
|                | voice.transId       | Unique identifier corresponding to the transaction.                                                   |            |
|                | voice.serviceNumber | Number on <<prodname>> to which the call was placed.                                                  |            |
|                | voice.msisdn        | Customer's number from which the call was placed.                                                     |            |
|                | voice.offeredOn     | Timestamp of the when the call was initiated.                                                         |            |
|                | voice.releasedOn    | Timestamp of end of the call.                                                                         |            |
|                | voice.callType      | Type of the call - Missed Call, IBD and OBD where IBD being inbound call and OBD being outbound call. |            |

**Messenger Node Output Variables**

| Incoming Event   | Output Variables            | Description                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :--------------- | :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Incoming message | messenger.message           | Incoming text message from end-customer.                                                                                                                                                                                           | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                  | messenger.psId              | Page-scoped Identifier of a messenger, user used to reply back to end-customer. It gets generated on first incoming message from end-customer.                                                                                     | Image, Video, GIFs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                  | messenger.attachmentUrl     | URL of the first attachment in case of multiple attachments.                                                                                                                                                                       | <https://scontent.xx.fbcdn.net/v/t1.15752-9/72730271_417889542250561_2125819214483685376_n.jpg?_nc_cat=103&_nc_ohc=V7t4vOxTCQYAX8iKoJA&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=3823f14c0eea111080f58d3ee4d8245c&oe=5EF6C203>                                                                                                                                                                                                                                                                                                                   |
|                  | messenger.attachments\*     | The full attachment object available such as attachment type and media URL sent by the app user as part of the incoming message. May contain caption in case of Image.                                                             | `{"payload":{"url":"https://scontent.xx.fbcdn.net/v/t1.15752-9/72730271_417889542250561_2125819214483685376_n.jpg?_nc_cat=103&_nc_ohc=V7t4vOxTCQYAX8iKoJA&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=3823f14c0eea111080f58d3ee4d8245c&oe=5EF6C203"},"type":"image"},{"payload":{"url":"https://scontent.xx.fbcdn.net/v/t1.15752-9/49442028_304527510181624_4550358914847211520_n.png?_nc_cat=103&_nc_ohc=aftIRUGfVdsAX8iQbkB&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=65561f3e90e1570f7feaf27af7400cda&oe=5EC19C85"},"type":"image"}` |
|                  | messenger.locationUrl       | URL for the website where the user downloaded the location information.                                                                                                                                                            | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                  | messenger.locationLatitude  | Lattitude of the location shared by the customer.                                                                                                                                                                                  | 17.437008131462.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                  | messenger.locationLongitude | Longitude of the location shared by the customer.                                                                                                                                                                                  | 78.39840389618.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.locationTitle     | Location Title.                                                                                                                                                                                                                    | Daspalla D-Convention Hall, Road no: 37, Jubilee Hills, Hyderabad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                  | messenger.name              | Name of the messenger.                                                                                                                                                                                                             | Jack Suraj                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                  | messenger.profilePicture    | Messenger returns Content Delivery Network (CDN) URLs which allow you to retrieve rich media content shared by users. The CDN URL is privacy-aware and will not return the media when the content has been deleted or has expired. | <https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=2534050010034596&width=1024&ext=1585393423&hash=AeSzgFDboc2HqIAm>                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                  | messenger.appId             | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                         | a_637183089024870000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                  | messenger.timestamp         | Record of the time when the request is received on <<prodname>> platform.                                                                                                                                                          | 1.5828E+12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                  | messenger.transId           | Unique identifier corresponding to the transaction.                                                                                                                                                                                | 6bbe6cb4-73b6-4c26-a8b6-fe39c13fdf26_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Postback         | messenger.postbackPayload   | Postback payload identifies customer's response to a quick reply, button or a persistent menu tap.                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.psId              | Page-scoped Identifier of a messenger, user used to reply back to end-customer. It gets generated on first incoming message from end-customer.                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.profilePicture    | URL of the first attachment in case of multiple attachments.                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.appId             | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.timestamp         | Record of the time when the request is received on <<prodname>> platform.                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.transId           | Unique identifier corresponding to the transaction.                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**MMS Node Output Variables**

[block:parameters]
{
  "data": {
    "h-0": "Incoming Event",
    "h-1": "Output Variables ",
    "h-2": "Description",
    "h-3": "Example",
    "0-0": "Mobile Originated - MO",
    "0-1": "mms.serviceNumber",
    "0-2": "The user's number the customer is sending the message to. Prefix the inbound number with the correct country code.",
    "0-3": "44 7111345232",
    "1-0": "",
    "1-1": "mms.timestamp",
    "1-2": "Record of the time when the request is received on Webex Connect platform. ",
    "1-3": "For e.g. 1582627917.  \n  \n2020-02-25T07:10:45.051Z",
    "2-0": "",
    "2-1": "mms.transId",
    "2-2": "Unique identifier corresponding to the transaction.",
    "2-3": "234190eb-df62-45c8-9281-c4b6f5b09c20",
    "3-0": "",
    "3-1": "mms.senderNumber",
    "3-2": "Number of the customer's handset from where the incoming message is originating.",
    "3-3": "19052342345",
    "4-0": "",
    "4-1": "receive.message ",
    "4-2": "Incoming text message from end-customer.",
    "4-3": "Ducati",
    "5-0": "",
    "5-1": "receive.channel",
    "5-2": "Identifies the channel from where the message has been received i.e. MMS.",
    "5-3": "MMS",
    "6-0": "",
    "6-1": "receive.payload",
    "6-2": "Any required value that is not included in any other output variable comes under payload.",
    "6-3": "",
    "7-0": "",
    "7-1": "receive.attachment",
    "7-2": "",
    "7-3": ""
  },
  "cols": 4,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Instagram Node Output Variables** 

> ❗️ 
> 
> The Instagram as a channel is deprecated.

[block:parameters]
{
  "data": {
    "h-0": "Incoming Event",
    "h-1": "Output Variables",
    "h-2": "Description",
    "h-3": "Example",
    "0-0": "Incoming Message, Postback, Message Deleted",
    "0-1": "instagram.messageId",
    "0-2": "Identifier for messages sent from the end customer to the business account",
    "0-3": "\"messageId\": \"aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDU1NTM5NjA0NzQ4OjM0MDI4MjM2Njg0MTcxMDMwMDk0OTEyODE4NzA2OTgxOTg2OTI4NDozMDY4Nzg2MzU1NzM1OTI1MDY4MTA0OTUxMTc5NDU3MzMxMgZDZD\"",
    "1-0": "Incoming Events",
    "1-1": "instagram.message",
    "1-2": "Incoming text message from end-customer.",
    "1-3": "Text Message: \"Hi\"",
    "2-0": "Postback",
    "2-1": "instagram.payload",
    "2-2": "Postback payload that identifies customer's response to a quick reply, template button.",
    "2-3": "\"quickReplyPayload\": \"{\"payload\":\"Add to cart\",\"title\":\"Add to card\"}\",",
    "3-0": "Postback",
    "3-1": "instagram.title",
    "3-2": "Title of the Instagram account holder.",
    "3-3": "",
    "4-0": "Postback, Incoming Message, Message Deleted",
    "4-1": "instagram.igsid",
    "4-2": "_ Page-scoped Identifier of an Instagram user used to reply back to end-customer. It gets generated on first incoming message from end-customer.  \n_ Identifier for messages sent from the end customer to the business account  \n\\* Identified for messages deleted from the business account.",
    "4-3": "\"igsid\": \"5275638769194520\"",
    "5-0": "Postback, Incoming Message, Message Deleted",
    "5-1": "instagram.igid",
    "5-2": "_ Page-scoped Identifier of an Instagram Business account used to reply to end-customer. It gets generated on first incoming message from end-customer.  \n_ Page-scoped Identifier of an Instagram Business account used to reply to end-customer. It gets generated on first incoming message from end-customer.  \n\\* Page-scoped identifier of an Instagram Business account used to delete a message from the customer.",
    "5-3": "“igid”: “17841454028327633“",
    "6-0": "Postback, Incoming Message, Message Deleted",
    "6-1": "instagram.timestamp",
    "6-2": "_ Record of the time when the request is received on Webex Connect platform.  \n_ Record of the time when the request is sent from the Webex Connect platform.  \n\\* Record of the time when the message is deleted from the Webex Connect platform.",
    "6-3": "\"timestamp\": \"1663597769637\"",
    "7-0": "Postback, Incoming Message, Message Deleted",
    "7-1": "instagram.event",
    "7-2": "\\* To identify the event type - postback, incoming, or message deleted.",
    "7-3": "\"event\": \"MO\" ,  \n\"event\": \"OnPostback\",  \n\"event\": \"OnMessageDeleted\",",
    "8-0": "Postback, Incoming Message, Message Deleted",
    "8-1": "instagram.userId",
    "8-2": "The unique identifier of the app user.",
    "8-3": "\"userId\": \"\",",
    "9-0": "Postback, Incoming Message, Message Deleted",
    "9-1": "instagram.appId",
    "9-2": "Unique identifier of the app from which the app user has sent the request.",
    "9-3": "\"appId\": \"a_637989151073720000\",",
    "10-0": "Postback",
    "10-1": "instagram.quickReplyPayload",
    "10-2": "Payload that identifies the business account's response to the customer's quick reply.",
    "10-3": "\"quickReplyPayload\": \"{\"payload\":\"Order status\"}\"",
    "11-0": "Incoming Message",
    "11-1": "instagram.attachment",
    "11-2": "The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message.",
    "11-3": "\"attachment\": \"\\`{\"payload\":{\"url\":\"[https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=1671821199864696&signature=AbzzQo9GUu0Ca9prExszWgmwdrEXjvxRgW74CwYj53axqORubYJNapprzYMzZ2J4iW65I0VVYyTC-ayR9LGtmQchQsljxhLaNF8jnyLNgE-4F5O0CVU2eCYesdXJV_cXPZJYQnFIHE43uOW9ehdipjggYglEUmG2PgJG5_QMmphrdOycd8c1mAzvjmfKBNHMV5QRI37Q-gtXbotihRyvi-iY-xCJSqg\\\"},\\\"type\\\":\\\"image\\\"}](https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=1671821199864696&signature=AbzzQo9GUu0Ca9prExszWgmwdrEXjvxRgW74CwYj53axqORubYJNapprzYMzZ2J4iW65I0VVYyTC-ayR9LGtmQchQsljxhLaNF8jnyLNgE-4F5O0CVU2eCYesdXJV_cXPZJYQnFIHE43uOW9ehdipjggYglEUmG2PgJG5_QMmphrdOycd8c1mAzvjmfKBNHMV5QRI37Q-gtXbotihRyvi-iY-xCJSqg\"},\"type\":\"image\"})]\",",
    "12-0": "Postback, Incoming Message, Message Deleted",
    "12-1": "instagram.messageId",
    "12-2": "Contains the message Id for the message.",
    "12-3": "\"messageId\": \"aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDU0MDI4MzI3NjMzOjM0MDI4MjM2Njg0MTcxMDMwMDk0OTEyODMwNjQwMjE1NjYyMzExMDozMDY4Nzk2OTMwMjU3ODk3OTU1MzAwNjU2NDU5ODA4NzY4MAZDZD\",",
    "13-0": "Incoming Message",
    "13-1": "instagram.attachmentType",
    "13-2": "Type of attachment i.e. image, gif, quick reply, and video.",
    "13-3": "\"attachmentType\": \"image\",  \n  \n\"attachmentType\": \"audio\",  \n  \n\"attachmentType\": \"video\",",
    "14-0": "Incoming Message",
    "14-1": "instagram.attachmentUrl",
    "14-2": "URL of the first attachment in case of multiple attachments.",
    "14-3": "\"attachmentUrl\": \"<https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=17964232888925487&signature=AbzxYfPgbyrbgqvQ4zWLayyMJo4fAM7JjR5atpeCLOQdFX5d3hObq1fw-kPBLDkyHiyYyTPbaOnzhVCPBrG9preKkdHA2W8sl0lCs7g8fWk2uaZ-lSu8MSnabAFfH91vWelUJl-8x_NN9ZEBOVTzThpbouP21CJA-IcOh_ODV79wAHaaLfB8v63XqgXv71fnXxKoA-gXneNwYxm3Y9r2nnWg6Na2gK8W\">,",
    "15-0": "Incoming Message",
    "15-1": "instagram.storyReplyUrl",
    "15-2": "URL of the posted story’s reply from the end customer.",
    "15-3": "\"storyReplyUrl\": \"<https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=17950801241174150&signature=AbzpNim0D-dMzZRWWmeGvcLBXGX8LjdfMHiS6_I6h_uXw8DslIq_INYv5HK2-dSGmANs3NaT2mraLIvKSVZoFAMl8Te-O9ahYqnmGlpaHDHxZInTCAjjBR6Ecao82ajuDF4c8Vuz9YjLemhC1Ct1L0ucQUPrCPH99xjWkTTA67PxHskgvuy95vS_MgPk1kNQF5Veqcb0Od-s6Jo8kspWRsNs16IXFflt>\"",
    "16-0": "Incoming Message",
    "16-1": "instagram.repliedMessageId",
    "16-2": "Unique identifier of the reply received from the end customer.",
    "16-3": "\"repliedMessageId\": \"aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDU0MDI4MzI3NjMzOjM0MDI4MjM2Njg0MTcxMDMwMDk0OTEyODMwNjQwMjE1NjYyMzExMDozMDY4Nzk3NjU3MjczMjk5Njk4MTMyNDM0MjA1MTczMzUwNAZDZD\",",
    "17-0": "Incoming Message",
    "17-1": "instagram.reaction",
    "17-2": "Unique identifier of the emoticon reply received from the end customer.",
    "17-3": "\"reaction\": \"{\"reaction\":\"love\",\"emoji\":\"❤️\",\"action\":\"react\"}\","
  },
  "cols": 4,
  "rows": 18,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**WhatsApp Node Output Variables**

[block:parameters]
{
  "data": {
    "h-0": "Incoming Event",
    "h-1": "Output Variables",
    "h-2": "Description",
    "h-3": "Example",
    "0-0": "Incoming Message",
    "0-1": "whatsapp.message",
    "0-2": "Incoming text message from end-customer.",
    "0-3": "Hello",
    "1-0": "",
    "1-1": "whatsapp.waId",
    "1-2": "The WhatsApp number of the end-customer.",
    "1-3": "9.19964E+11",
    "2-0": "",
    "2-1": "whatsapp.bsuid",
    "2-2": "The Business-scoped User ID of the customer",
    "2-3": "IN.746868",
    "3-0": "",
    "3-1": "whatsapp.userHandle",
    "3-2": "WhatsApp username/handle of the sender, when available.",
    "3-3": "\"\\*\\_ait_12\"",
    "4-0": "",
    "4-1": "whatsapp.attachmentType",
    "4-2": "Public url of the uploaded attachment.",
    "4-3": "Image, audio, video, document, and contact",
    "5-0": "",
    "5-1": "whatsapp.locationAddress",
    "5-2": "Full address of the location.",
    "5-3": "Webex Connect, Plot No 770, Rd Number 44, Hyderabad, Telangana 500033",
    "6-0": "",
    "6-1": "whatsapp.locationLatitude",
    "6-2": "Location Latitude.",
    "6-3": "17.434715270996",
    "7-0": "",
    "7-1": "whatsapp.locationLongitude",
    "7-2": "Location Longitude.",
    "7-3": "78.3984832763671",
    "8-0": "",
    "8-1": "whatsapp.locationName",
    "8-2": "URL for the website where the user downloaded the location information.",
    "8-3": "Webex Connect",
    "9-0": "",
    "9-1": "whatsapp.locationUrl",
    "9-2": "URL for the website where the user downloaded the location information.",
    "9-3": "",
    "10-0": "",
    "10-1": "whatsapp.imageUrl",
    "10-2": "URL of the image.",
    "10-3": "",
    "11-0": "",
    "11-1": "whatsapp.mimeType",
    "11-2": "Mime type of the attachment.",
    "11-3": "",
    "12-0": "",
    "12-1": "whatsapp.caption",
    "12-2": "Caption, if present along with image and video.",
    "12-3": "",
    "13-0": "",
    "13-1": "whatsapp.documentUrl",
    "13-2": "Direct URL of  the attachment ending with file type.",
    "13-3": "",
    "14-0": "",
    "14-1": "whatsapp.voiceUrl",
    "14-2": "Direct URL of  the attachment ending with file type.",
    "14-3": "",
    "15-0": "",
    "15-1": "whatsapp.audioUrl",
    "15-2": "Direct URL of  the attachment ending with file type.",
    "15-3": "",
    "16-0": "",
    "16-1": "whatsapp.attachments",
    "16-2": "The full attachment object available such as attachment type and media URL etc. sent by the app user as part of the incoming message.. May contain caption in case of image.",
    "16-3": "",
    "17-0": "",
    "17-1": "whatsapp.appId",
    "17-2": "Unique identifier of the app from which the app user has sent the request.",
    "17-3": "",
    "18-0": "",
    "18-1": "whatsapp.timestamp",
    "18-2": "Record of the time when the request is received on <<prodname>> platform.",
    "18-3": "",
    "19-0": "",
    "19-1": "whatsapp.contextId",
    "19-2": "WhatsApp message Id",
    "19-3": "wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA==",
    "20-0": "",
    "20-1": "whatsapp.systemBody",
    "20-2": "Removed",
    "20-3": "",
    "21-0": "",
    "21-1": "whatsapp.transId",
    "21-2": "Unique identifier corresponding to the transaction.",
    "21-3": "",
    "22-0": "",
    "22-1": "whatsapp.videoUrl",
    "22-2": "Direct URL of  the attachment ending with file type.",
    "22-3": "",
    "23-0": "",
    "23-1": "whatsapp.contacts",
    "23-2": "Full contact object containing addresses, phone numbers, emails etc.",
    "23-3": "Addresses: Array  \nBirthday: YYYY-MM-DD formatted string  \nContact_image: Base64-encoded image  \nEmails: Array  \nIMS: Array  \nName: Array  \nOrg: Array  \nPhones: Array  \nURLs: Array",
    "24-0": "",
    "24-1": "whatsapp.username",
    "24-2": "The username of the sender.",
    "24-3": "",
    "25-0": "",
    "25-1": "whatsapp.identityHash",
    "25-2": "Unique cryptographic hash key for a WhatsApp phone number.",
    "25-3": "1",
    "26-0": "Postback",
    "26-1": "whatsapp.waId",
    "26-2": "The WhatsApp number of the end-customer",
    "26-3": "\\+919876543210",
    "27-0": "",
    "27-1": "whatsapp.bsuid",
    "27-2": "The Business-scoped User ID of the customer",
    "27-3": "IN.746868",
    "28-0": "",
    "28-1": "whatsapp.userHandle",
    "28-2": "WhatsApp username/handle of the sender, when available.",
    "28-3": "\"\\*\\_ait_12\"",
    "29-0": "",
    "29-1": "whatsapp.buttonPayload",
    "29-2": "Developer-defined payload that will be returned when the button is clicked in addition to the display text on the button",
    "29-3": "",
    "30-0": "",
    "30-1": "whatsapp.buttonText",
    "30-2": "The button text that you have used while creating the template",
    "30-3": "",
    "31-0": "",
    "31-1": "whatsapp.contextId",
    "31-2": "WhatsApp message Id",
    "31-3": "wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA==",
    "32-0": "",
    "32-1": "whatsapp.appId",
    "32-2": "Unique identifier of the app from which the app user has sent the request",
    "32-3": "",
    "33-0": "",
    "33-1": "whatsapp.timestamp",
    "33-2": "Record of the time when the request is received on <<prodname>> platform.",
    "33-3": "",
    "34-0": "",
    "34-1": "whatsapp.transId",
    "34-2": "Unique identifier corresponding to the transaction.",
    "34-3": "",
    "35-0": "",
    "35-1": "whatsapp.identityHash",
    "35-2": "Unique cryptographic hash key for a WhatsApp phone number.",
    "35-3": "1",
    "36-0": "List Message",
    "36-1": "whatsapp.waId",
    "36-2": "The WhatsApp number of the end-customer.",
    "36-3": "",
    "37-0": "",
    "37-1": "whatsapp.bsuid",
    "37-2": "The Business-scoped User ID of the customer",
    "37-3": "IN.746868",
    "38-0": "",
    "38-1": "whatsapp.userHandle",
    "38-2": "WhatsApp username/handle of the sender, when available.",
    "38-3": "\"\\*\\_ait_12\"",
    "39-0": "",
    "39-1": "whatsapp.listRowTitle",
    "39-2": "",
    "39-3": "",
    "40-0": "",
    "40-1": "whatsapp.listRowIdentifier",
    "40-2": "",
    "40-3": "",
    "41-0": "",
    "41-1": "whatsapp.listDescription",
    "41-2": "",
    "41-3": "",
    "42-0": "",
    "42-1": "whatsapp.username",
    "42-2": "The username of the sender.",
    "42-3": "",
    "43-0": "",
    "43-1": "whatsapp.contextId",
    "43-2": "WhatsApp message Id",
    "43-3": "wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA==",
    "44-0": "",
    "44-1": "whatsapp.type",
    "44-2": "",
    "44-3": "",
    "45-0": "",
    "45-1": "whatsapp.appId",
    "45-2": "Unique identifier of the app from which the app user has sent the request.",
    "45-3": "",
    "46-0": "",
    "46-1": "whatsapp.timestamp",
    "46-2": "Record of the time when the request is received on <<prodname>> platform.",
    "46-3": "",
    "47-0": "",
    "47-1": "whatsapp.transId",
    "47-2": "Unique identifier corresponding to the transaction.",
    "47-3": "",
    "48-0": "",
    "48-1": "whatsapp.identityHash",
    "48-2": "Unique cryptographic hash key for a WhatsApp phone number.",
    "48-3": "1",
    "49-0": "Reply Buttons ",
    "49-1": "whatsapp.waId",
    "49-2": "The WhatsApp number of the end-customer",
    "49-3": "",
    "50-0": "",
    "50-1": "whatsapp.bsuid",
    "50-2": "The Business-scoped User ID of the customer",
    "50-3": "IN.746868",
    "51-0": "",
    "51-1": "whatsapp.userHandle",
    "51-2": "WhatsApp username/handle of the sender, when available.",
    "51-3": "\"\\*\\_ait_12\"",
    "52-0": "",
    "52-1": "whatsapp.replyButtonIdentifier",
    "52-2": "",
    "52-3": "",
    "53-0": "",
    "53-1": "whatsapp.replyButtonTitle",
    "53-2": "",
    "53-3": "",
    "54-0": "",
    "54-1": "whatsapp.username",
    "54-2": "The username of the sender.",
    "54-3": "",
    "55-0": "",
    "55-1": "whatsapp.contextId",
    "55-2": "WhatsApp message Id",
    "55-3": "wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA==",
    "56-0": "",
    "56-1": "whatsapp.type",
    "56-2": "",
    "56-3": "",
    "57-0": "",
    "57-1": "whatsapp.appId",
    "57-2": "Unique identifier of the app from which the app user has sent the request.",
    "57-3": "",
    "58-0": "",
    "58-1": "whatsapp.timestamp",
    "58-2": "Record of the time when the request is received on <<prodname>> platform.",
    "58-3": "",
    "59-0": "",
    "59-1": "whatsapp.transId",
    "59-2": "Unique identifier corresponding to the transaction.",
    "59-3": "",
    "60-0": "",
    "60-1": "whatsapp.identityHash",
    "60-2": "Unique cryptographic hash key for a WhatsApp phone number.",
    "60-3": "1"
  },
  "cols": 4,
  "rows": 61,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> WhatsApp.caption is only supported for image attachment.
> 
> WhatsApp only supports one attachment as part of incoming messages event. The payload will not be received if the end-user uploads multiple attachments.

**In-app Messaging Node Output Variables**

| Incoming Event               | Output Variables                       | Description                                                                                                                              | Example |
| :--------------------------- | :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| Custom Event                 | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.payload                 | Any required value that is not included in any other output variable comes under payload.                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.extras                  | Contains additional information received in the message                                                                                  |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
|                              | inappmessaging.formResponse            | Captures the response received on the pre-chat form                                                                                      |         |
|                              | inappmessaging.formFields.Issue        | The issue/reason stated on the pre-chat form                                                                                             |         |
|                              | inappmessaging.formFields.Date         | The date on which the pre-chat form was submitted                                                                                        |         |
| Incoming Message             | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.threadId                | The unique identifier corresponding to a thread.                                                                                         |         |
|                              | inappmessaging.completedOn             |                                                                                                                                          |         |
|                              | inappmessaging.threadTitle             | The name set as the title of a thread.                                                                                                   |         |
|                              | inappmessaging.threadStatus            | The status of the thread converying whether the thread is in open state or closed.                                                       |         |
|                              | inappmessaging.message                 | Incoming message by the end-customer.                                                                                                    |         |
|                              | inappmessaging.attachment              | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message. |         |
|                              | inappmessaging.version                 |                                                                                                                                          |         |
|                              | inappmessaging.deviceId                | Unique identifier correspnding to the device from which the app user has sent the message.                                               |         |
|                              | inappmessaging.origin                  |                                                                                                                                          |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Interactive Message Response | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.pushId                  | The token generated by FCM or APNS at the time of user registration.                                                                     |         |
|                              | inappmessaging.pushType                | The type of push notification, conveying whether it's a silent or normal push notification.                                              |         |
|                              | inappmessaging.interactivePushResponse | The response or the button tapped on by the user within the interactive notification.                                                    |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Location Change              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.completedOn             |                                                                                                                                          |         |
|                              | inappmessaging.deviceId                | Unique identifier correspnding to the device from which the app user has sent the message.                                               |         |
|                              | inappmessaging.origin                  |                                                                                                                                          |         |
|                              | inappmessaging.version                 |                                                                                                                                          |         |
| onLinkClick                  |                                        |                                                                                                                                          |         |
| On Network Change            | inappmessaging.completedOn             |                                                                                                                                          |         |
|                              | inappmessaging.version                 |                                                                                                                                          |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.deviceId                | Unique identifier correspnding to the device from which the app user has sent the message.                                               |         |
|                              | inappmessaging.origin                  |                                                                                                                                          |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | Node outcomes                          | This is not an output variable.                                                                                                          |         |
| On Web Push Click            | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.pushId                  | The token generated by FCM or APNS at the time of user registration.                                                                     |         |
|                              | inappmessaging.pushType                | The type of push notification, conveying whether it's a silent or normal push notification.                                              |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| On Connect                   | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the event when connection between the app on <<prodname>> is established.   |         |
| On Disconnect                | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the event when connection between the app on <<prodname>> is closed.        |         |
| Profile Creation             | inappmessaging.profile.make            | The manufacturer of the device from which the app user has registerd.                                                                    |         |
|                              | inappmessaging.profile.os              | The operating system of the device from which the app user has registered.                                                               |         |
|                              | inappmessaging.profile.osVersion       | The version of the operating system of the device.                                                                                       |         |
|                              | inappmessaging.profile.sdkVersion      | The <<prodname>> SDK version of the app.                                                                                                 |         |
|                              | inappmessaging.profile.model           | The model name of the device.                                                                                                            |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Profile Update               | inappmessaging.profile.make            | The manufacturer of the device from which the app user has registerd.                                                                    |         |
|                              | inappmessaging.profile.os              | The operating system of the device from which the app user has registered.                                                               |         |
|                              | inappmessaging.profile.osVersion       | The version of the operating system of the device.                                                                                       |         |
|                              | inappmessaging.profile.sdkVersion      | The <<prodname>> SDK version of the app.                                                                                                 |         |
|                              | inappmessaging.profile.model           | The model name of the device.                                                                                                            |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Roaming Change               |                                        |                                                                                                                                          |         |
| Subscribe                    | inappmessaging.topic                   | Name of the topic which the user has subsribed to.                                                                                       |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| unSubscribe                  | inappmessaging.topic                   | Name of the topic which the user has subsribed to.                                                                                       |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on <<prodname>> platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |

**Email Node Output Variables**

| Incoming Event        | Output Variables                     | Description                                                                                                                                                                                                                                                                                                                                           | Example                                                               |
| :-------------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| Incoming Message      | email.subject                        | Contains the subject of the incoming email.                                                                                                                                                                                                                                                                                                           | Email MO Start 1/2/3                                                  |
|                       | email.message                        | Contains the body of the incoming email.                                                                                                                                                                                                                                                                                                              | Email MO Start 2\\r\\n                                                |
|                       | email.emailId                        | Contains the email ID of the sender.                                                                                                                                                                                                                                                                                                                  | [connectautomation36@gmail.com](mailto:connectautomation36@gmail.com) |
|                       | email.transId                        | Unique identifier corresponding to the transaction.                                                                                                                                                                                                                                                                                                   | 2c25f71d-d014-4798-8e83-6d884b2931fa                                  |
|                       | email.timestamp                      | Record of the time when the request is received on <<prodname>> platform.                                                                                                                                                                                                                                                                             | 2020-03-04T06:03:32.184Z                                              |
|                       | email.attachments                    | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message.\_Note: If the incoming email attachments contains.msg files,the.msg attachments sent by customers might not be delivered to businesses if sent from MS Outlook email client due to an issue with MS Outlook. |                                                                       |
|                       | email.appId                          | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                                                                                                                                            | a_637172790998330000                                                  |
|                       | email.senderName                     | Contains the name of the sender                                                                                                                                                                                                                                                                                                                       |                                                                       |
|                       | email.toAddresses                    | Contains the recipient's email addresses                                                                                                                                                                                                                                                                                                              |                                                                       |
|                       | email.ccRecipents                    | Contains the email address for one or more cc recipients list                                                                                                                                                                                                                                                                                         |                                                                       |
|                       | email.bccRecipents                   | Contains the email address for one or more bcc recipients list                                                                                                                                                                                                                                                                                        |                                                                       |
|                       | email.htmlMessage                    | Contains the HTML message for the email                                                                                                                                                                                                                                                                                                               |                                                                       |
|                       | email.inReplyTo                      | Contains the inReplyTo value of which this email is a part of                                                                                                                                                                                                                                                                                         |                                                                       |
|                       | email.messageId                      | Contains the message Id for the email                                                                                                                                                                                                                                                                                                                 |                                                                       |
|                       | email.headers                        | Contains the email header                                                                                                                                                                                                                                                                                                                             |                                                                       |
|                       | email.assetType                      | Contains the asset type as email or image.                                                                                                                                                                                                                                                                                                            |                                                                       |
|                       | email.strippedText                   | Contains the value of stripped HTML as provided by SMTP server                                                                                                                                                                                                                                                                                        |                                                                       |
|                       | email.strippedHTML                   | Contains the value of stripped HTML as provided by SMTP server                                                                                                                                                                                                                                                                                        |                                                                       |
|                       | email.PCIInfo.isPCICompliance        | Is true when the data is PCI compliant                                                                                                                                                                                                                                                                                                                |                                                                       |
|                       | email.PCIInfo.isPCIValidationDone    | Is true when the PCI validation done                                                                                                                                                                                                                                                                                                                  |                                                                       |
|                       | email.PCIInfo.nonPCIComplianceReason | Contains the reason for which the data is dropped or masked.                                                                                                                                                                                                                                                                                          |                                                                       |
|                       | email.PCIInfo.droppedAttachmentCount | Contains the number of dropped attachments                                                                                                                                                                                                                                                                                                            |                                                                       |
|                       | email.PCIInfo.isAttachmentEnabled    | Contains if the message is enabled for the attachments                                                                                                                                                                                                                                                                                                |                                                                       |
| Subscribe/Unsubscribe | email.message                        | Contains the body of the incoming email.                                                                                                                                                                                                                                                                                                              | N/A                                                                   |
|                       | email.emailId                        | Contains the email ID of the sender.                                                                                                                                                                                                                                                                                                                  | [twitterbeta123@gmail.com](mailto:twitterbeta123@gmail.com)           |
|                       | email.transId                        | Unique identifier corresponding to the transaction.                                                                                                                                                                                                                                                                                                   | 1459722c-246c-4625-9ad6-7f4f8a4b1642                                  |
|                       | email.timestamp                      | Record of the time when the request is received on <<prodname>> platform.                                                                                                                                                                                                                                                                             | 2020-03-04T15:27:27.409+05:30                                         |
|                       | email.attachments                    | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message.                                                                                                                                                                                                              | N/A                                                                   |
|                       | email.appId                          | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                                                                                                                                            | a_637172790998330000                                                  |

**<<AMB>>(AMB) Node Output Variables**

> 📘 List Picker
> 
> Please note that you may receive duplicate responses for the List Picker, if the customer responds through non-iOS Apple devices such as the MacBook.

[block:parameters]
{
  "data": {
    "h-0": "Incoming Event",
    "h-1": "Output Variables",
    "h-2": "Description",
    "h-3": "Example",
    "0-0": "Form Messages",
    "0-1": "",
    "0-2": "",
    "0-3": "",
    "1-0": "",
    "1-1": "abc.abcUserId",
    "1-2": "Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device.",
    "1-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "2-0": "",
    "2-1": "abc.appId",
    "2-2": "Unique identifier of the app from which the app user has sent the request.",
    "2-3": "a_636893638318070000",
    "3-0": "",
    "3-1": "abc.type",
    "3-2": "Type of the message. It’s “interactive” for Form Messages.",
    "3-3": "",
    "4-0": "",
    "4-1": "abc.timestamp",
    "4-2": "Record of the time when the request is received on the Webex Connect platform. For e.g. 1582627917.",
    "4-3": "2020-02-28T04:44:15.077Z",
    "5-0": "",
    "5-1": "abc.locale",
    "5-2": "Language locale of the customer's device.",
    "5-3": "en_US",
    "6-0": "",
    "6-1": "abc.requestIdentifier",
    "6-2": "Request identifier of the form message that was sent to the customer is returned in this variable.",
    "6-3": "",
    "7-0": "",
    "7-1": "abc.transId (only for Start Node)",
    "7-2": "Unique identifier corresponding to the transaction.",
    "7-3": "",
    "8-0": "",
    "8-1": "service.serviceKey (only for Start Node)",
    "8-2": "Contains the service key used for authenticating while sending the message.",
    "8-3": "",
    "9-0": "",
    "9-1": "abc.selections",
    "9-2": "Form response payload that captures the user’s responses across various pages of the form",
    "9-3": "",
    "10-0": "",
    "10-1": "abc.selectionsCount",
    "10-2": "Total number of pages in the form",
    "10-3": "",
    "11-0": "",
    "11-1": "abc.capabilityList",
    "11-2": "Helps you find out if the device that you are using has the capability to support the Form Messages message feature. It is applicable for other message types too.",
    "11-3": "",
    "12-0": "",
    "12-1": "abc.replyMessageAlternateTitle",
    "12-2": "Title of the reply bubble as defined in the sent message.",
    "12-3": "Mar 20, 2020 at 12:00 PM",
    "13-0": "",
    "13-1": "abc.accountId",
    "13-2": "Unique account ID of the business as defined by Apple.",
    "13-3": "3364d419-4b4a-4f59-a767-ac7e60214baa",
    "14-0": "",
    "14-1": "abc.deviceAgent",
    "14-2": "Contains the information of the type of device the customer is messaging from.",
    "14-3": "iPhone OS",
    "15-0": "",
    "15-1": "abc.interactivePayload",
    "15-2": "Available only in Start Node. The corresponding variable on the Receive Node is 'receive.payload'.",
    "15-3": "Sample Payload  \n{  \n  \"replyMessage\": {  \n    \"imageIdentifier\": \"551a9527-e8c1-4395-9431-885c7e8615f2\",  \n    \"subtitle\": \"This is Subtitle\",  \n    \"style\": \"small\",  \n    \"alternateTitle\": \"Tap to view your response.\",  \n    \"title\": \"Tap to view your response.\"  \n  },  \n  \"formMessage\": {  \n    \"template\": \"messageForms\",  \n    \"private\": false,  \n    \"selections\": \\[  \n      {  \n        \"pageIdentifier\": \"1\",  \n        \"subtitle\": \"Was the merchandise you received defective or not as the merchant described?\",  \n        \"title\": \"Item Condition\",  \n        \"items\": [  \n          {  \n            \"identifier\": \"101\",  \n            \"type\": \"select\",  \n            \"title\": \"Defective\",  \n            \"value\": \"defective\"  \n          }  \n        ]  \n      },  \n      {  \n        \"pageIdentifier\": \"2\",  \n        \"subtitle\": \"Do you have any supporting documents that demonstrate that the product quality was not sufficient?\",  \n        \"title\": \"Supporting Documents\",  \n        \"items\": [  \n          {  \n            \"identifier\": \"202\",  \n            \"type\": \"select\",  \n            \"title\": \"No\",  \n            \"value\": \"no\"  \n          }  \n        ]  \n      }  \n    ],  \n    \"version\": \"1.1\"  \n  }  \n}",
    "16-0": "",
    "16-1": "abc.pciInfo.isPCICompliance",
    "16-2": "",
    "16-3": "",
    "17-0": "",
    "17-1": "abc.pciInfo.isPCIValidationDone",
    "17-2": "",
    "17-3": "",
    "18-0": "",
    "18-1": "abc.pciInfo.nonPCIComplianceReason",
    "18-2": "",
    "18-3": "",
    "19-0": "",
    "19-1": "abc.pciInfo.isAttachmentEnabled",
    "19-2": "",
    "19-3": "",
    "20-0": "",
    "20-1": "abc.pciInfo.droppedAttachmentCount",
    "20-2": "",
    "20-3": "",
    "21-0": "New Auth Response",
    "21-1": "",
    "21-2": "",
    "21-3": "",
    "22-0": "",
    "22-1": "abc.abcUserId",
    "22-2": "Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device.",
    "22-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "23-0": "",
    "23-1": "abc.authToken",
    "23-2": "Auth token returned by the authenticating system.",
    "23-3": "Authtoken: AQUxx-v6A7qc4dh-N9ZgCDc38LHKFzFM1zMxiiN1z9hgCo1b17NblPWDih3JSARgcv7cvBzNwSY3f9bgqWoYsmIJByG57UExQ4gw1fT0uCMUFbbPdJUx03rObWhUX47SPj_fI4v_T7ec1Jd3H5AQkzX-rTfJnawVIlC7fd8e-jm4GMxPqlkTjC3zWmmTZOYggdiQWBoj6g7EN0yBV-s0zwVdxE2ix7plbOfCkVo6qDVu6HLk0K3lPAQF5viXNcz9LXc8KHyj7zfjOV2bfUB2H6STkymRggKlC03O8F2RN3iDzK8kQq4-NlLvj_5OuvdKpReOXHFMMN-UCYhjngJ1lwmCKRmPbQ",
    "24-0": "",
    "24-1": "abc.authStatus",
    "24-2": "Status of the user authentication e.g., authenticated.",
    "24-3": "Authenticated",
    "25-0": "",
    "25-1": "abc.authReplyMessageTitle",
    "25-2": "Title of the reply bubble as defined in the sent message.",
    "25-3": "Reply message",
    "26-0": "",
    "26-1": "abc.authReplyMessageAlternateTitle",
    "26-2": "Alternate Title of the reply bubble as defined in the sent message.",
    "26-3": "Reply message",
    "27-0": "",
    "27-1": "abc.transId",
    "27-2": "Unique identifier corresponding to the transaction.",
    "27-3": "",
    "28-0": "",
    "28-1": "abc.accountId",
    "28-2": "Unique account ID of the business as defined by Apple.",
    "28-3": "",
    "29-0": "",
    "29-1": "abc.appId",
    "29-2": "Unique identifier of the app from which the app user has sent the request.",
    "29-3": "a_636893638318070000",
    "30-0": "",
    "30-1": "abc.timestamp",
    "30-2": "Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917.",
    "30-3": "2020-02-28T04:44:15.077Z",
    "31-0": "",
    "31-1": "abc.requestIdentifier",
    "31-2": "Request identifier of the new auth response message that was sent to the customer is returned in this variable.",
    "31-3": "",
    "32-0": "",
    "32-1": "service.serviceKey (only for Start Node)",
    "32-2": "Contains the service key used for authenticating while sending the message.",
    "32-3": "54251909-59b9-11ed-9c39-02a06e0e48bf",
    "33-0": "",
    "33-1": "abc.capabilityList",
    "33-2": "Helps you find out if the device that you are using has the capability of supporting the New Auth message feature. It is applicable for other message types as well.",
    "33-3": "",
    "34-0": "",
    "34-1": "abc.expiryTime",
    "34-2": "Expiry time of the access token expressed in seconds.",
    "34-3": "",
    "35-0": "",
    "35-1": "abc.type",
    "35-2": "Type of the Message.)",
    "35-3": "",
    "36-0": "iMessage App Response",
    "36-1": "",
    "36-2": "",
    "36-3": "",
    "37-0": "",
    "37-1": "abc.abcUserId",
    "37-2": "Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device.",
    "37-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "38-0": "",
    "38-1": "abc.appId",
    "38-2": "Unique identifier of the app from which the app user has sent the request.",
    "38-3": "a_636893638318070000",
    "39-0": "",
    "39-1": "abc.bid",
    "39-2": "",
    "39-3": "",
    "40-0": "",
    "40-1": "abc.timestamp",
    "40-2": "Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917.",
    "40-3": "2020-02-28T04:44:15.077Z",
    "41-0": "",
    "41-1": "abc.locale",
    "41-2": "Language locale of the customer's device.",
    "41-3": "en_US",
    "42-0": "",
    "42-1": "abc.requestIdentifier",
    "42-2": "Request identifier of the new auth response message that was sent to the customer is returned in this variable.",
    "42-3": "formmessage123",
    "43-0": "",
    "43-1": "abc.transId (only for Start Node)",
    "43-2": "Unique identifier corresponding to the transaction.",
    "43-3": "",
    "44-0": "",
    "44-1": "abc.url",
    "44-2": "",
    "44-3": "",
    "45-0": "",
    "45-1": "service.serviceKey (only for Start Node)",
    "45-2": "Contains the service key used for authenticating while sending the message.",
    "45-3": "54251909-59b9-11ed-9c39-02a06e0e48bf",
    "46-0": "",
    "46-1": "abc.attachments",
    "46-2": "The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message.",
    "46-3": "[{\"size\":\"146021\",\"name\":\"IMG_0869.jpeg\",\"mimeType\":\"image/jpeg\",\"type\":\"image\",\"url\":\"https://s3.amazonaws.com/appleattachment/366ffe58-0e96-4f67-953d-478f8bdc29d5.jpeg\"},{\"size\":\"845196\",\"name\":\"IMG_0990.mov\",\"mimeType\":\"video/quicktime\",\"type\":\"video\",\"url\":\"https://s3.amazonaws.com/appleattachment/f23aa2cc-13e6-44b4-9e37-57368d3b38ee.quicktime\"}]",
    "47-0": "",
    "47-1": "abc.capabilityList",
    "47-2": "This parameter helps you find out if the device that you are using has the capability of supporting the new auth response message feature. It is applicable for other message types as well.",
    "47-3": "",
    "48-0": "",
    "48-1": "abc.replyMessageAlternateTitle",
    "48-2": "Title of the reply bubble as defined in the sent message.",
    "48-3": "Mar 20, 2020 at 12:00 PM",
    "49-0": "",
    "49-1": "abc.accountId",
    "49-2": "Unique account ID of the business as defined by Apple.",
    "49-3": "3364d419-4b4a-4f59-a767-ac7e60214baa",
    "50-0": "",
    "50-1": "abc.deviceAgent",
    "50-2": "Contains the information of the type of device the customer is messaging from.",
    "50-3": "iPhone OS",
    "51-0": "",
    "51-1": "abc.type",
    "51-2": "Type of the message. ",
    "51-3": "",
    "52-0": "",
    "52-1": "abc.pciInfo.isPCICompliance",
    "52-2": "",
    "52-3": "",
    "53-0": "",
    "53-1": "abc.pciInfo.isPCIValidationDone",
    "53-2": "",
    "53-3": "",
    "54-0": "",
    "54-1": "abc.pciInfo.nonPCIComplianceReason",
    "54-2": "",
    "54-3": "",
    "55-0": "",
    "55-1": "abc.pciInfo.isAttachmentEnabled",
    "55-2": "",
    "55-3": "",
    "56-0": "",
    "56-1": "abc.pciInfo.droppedAtt\t  \nabc.abcUserIdachmentCount",
    "56-2": "",
    "56-3": "",
    "57-0": "Incoming Message",
    "57-1": "",
    "57-2": "",
    "57-3": "",
    "58-0": "",
    "58-1": "abc.message",
    "58-2": "Contains the body of the incoming message.",
    "58-3": "Incomingmessage",
    "59-0": "",
    "59-1": "abc.abcUserId",
    "59-2": "Unique user Id of the customer with the corresponding business that never changes even if the customer changes their device.",
    "59-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "60-0": "",
    "60-1": "abc.attachmentCount",
    "60-2": "Count of total number of attachments.",
    "60-3": "2",
    "61-0": "",
    "61-1": "abc.attachmentUrl",
    "61-2": "URL of the first attachment in case of multiple attachments.",
    "61-3": "<https://s3.amazonaws.com/appleattachment/366ffe58-0e96-4f67-953d-478f8bdc29d5.jpeg>",
    "62-0": "",
    "62-1": "abc.attachmentType",
    "62-2": "Type of attachment i.e. image, gif and video.",
    "62-3": "image/jpeg (Only first Url mimetype coming)",
    "63-0": "",
    "63-1": "abc.attachments",
    "63-2": "The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message.",
    "63-3": "`{\"size\":\"146021\",\"name\":\"IMG_0869.jpeg\",\"mimeType\":\"image/jpeg\",\"type\":\"image\",\"url\":\"https://s3.amazonaws.com/appleattachment/366ffe58-0e96-4f67-953d-478f8bdc29d5.jpeg\"},{\"size\":\"845196\",\"name\":\"IMG_0990.mov\",\"mimeType\":\"video/quicktime\",\"type\":\"video\",\"url\":\"https://s3.amazonaws.com/appleattachment/f23aa2cc-13e6-44b4-9e37-57368d3b38ee.quicktime\"}`",
    "64-0": "",
    "64-1": "abc.locale",
    "64-2": "Language locale of the customer's device.",
    "64-3": "en_US",
    "65-0": "",
    "65-1": "abc.accountId",
    "65-2": "Unique account Id of the business as defined by Apple.",
    "65-3": "3364d419-4b4a-4f59-a767-ac7e60214baa",
    "66-0": "",
    "66-1": "abc.appId",
    "66-2": "Unique identifier of the app from which the app user has sent the request.",
    "66-3": "a_636893638318070000",
    "67-0": "",
    "67-1": "abc.timestamp",
    "67-2": "Record of the time when the request is received on <<prodname>> platform. For e.g. 1582627917.",
    "67-3": "2020-02-28T04:44:15.077Z",
    "68-0": "",
    "68-1": "abc.transId",
    "68-2": "Unique identifier corresponding to the transaction.",
    "68-3": "c330c225-a541-c501-bdfe-971ada4cf168",
    "69-0": "",
    "69-1": "abc.intentId",
    "69-2": "Intent Id as configured in the entrypoint.",
    "69-3": "",
    "70-0": "",
    "70-1": "abc.groupId",
    "70-2": "Group Id as configured in the entry point.",
    "70-3": "",
    "71-0": "",
    "71-1": "abc.deviceAgent",
    "71-2": "Contains the information of the type of device the customer is messaging from.",
    "71-3": "iPhone OS",
    "72-0": "",
    "72-1": "abc.capabilities",
    "72-2": "Contains the information of the features capabilities of the customer device such as auth, pay etc.",
    "72-3": "AUTH,1.00",
    "73-0": "Date Picker",
    "73-1": "",
    "73-2": "",
    "73-3": "",
    "74-0": "",
    "74-1": "abc.message",
    "74-2": "Contains the body of the incoming message.",
    "74-3": "N/A",
    "75-0": "",
    "75-1": "abc.abcUserId",
    "75-2": "Unique userId of the customer with the corresponding business that never changes even if the customer changes their device.",
    "75-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "76-0": "",
    "76-1": "abc.datePickerTimeSlots",
    "76-2": "Array that contains the time slot selected by the customer e.g., [{\"duration\":\"1800\",\"identifier\":\"c020521e-cc3c-41fa-876e-a445237a6f83\",\"startTime\":\"2020-03-20T06:30+0000\"}].",
    "76-3": "`{\"duration\":\"1800\",\"identifier\":\"c020521e-cc3c-41fa-876e-a445237a6f83\",\"startTime\":\"2020-03-20T06:30+0000\"}`",
    "77-0": "",
    "77-1": "abc.datePickerTimeSlotsDuration",
    "77-2": "Duration of the time slot selected by the customer.",
    "77-3": "1800",
    "78-0": "",
    "78-1": "abc.datePickerTimeSlotsIdentifier",
    "78-2": "Identifier of the time slot selected by the customer.",
    "78-3": "c020521e-cc3c-41fa-876e-a445237a6f83",
    "79-0": "",
    "79-1": "abc.datePickerTimeSlotsStartTime",
    "79-2": "Start time of the time slot selected by the customer.",
    "79-3": "2020-03-20T06:30+0000",
    "80-0": "",
    "80-1": "abc.requestIdentifier",
    "80-2": "Request identifier of the timepicker message that was sent to the customer is returned in this variable.",
    "80-3": "datepicker123",
    "81-0": "",
    "81-1": "abc.replyMessageAlternateTitle",
    "81-2": "Title of the reply bubble as defined in the sent message.",
    "81-3": "Mar 20, 2020 at 12:00 PM",
    "82-0": "",
    "82-1": "abc.locale",
    "82-2": "Language locale of the customer's device.",
    "82-3": "",
    "83-0": "",
    "83-1": "abc.accountId",
    "83-2": "Unique account Id of the business as defined by Apple.",
    "83-3": "3364d419-4b4a-4f59-a767-ac7e60214baa",
    "84-0": "",
    "84-1": "abc.appId",
    "84-2": "Unique identifier of the app from which the app user has sent the request.",
    "84-3": "a_636893638318070000",
    "85-0": "",
    "85-1": "abc.timestamp",
    "85-2": "Record of the time when the request is received on <<prodname>> platform. For e.g. 1582627917.",
    "85-3": "2020-03-04T12:11:48.480Z",
    "86-0": "",
    "86-1": "abc.transId",
    "86-2": "Unique identifier corresponding to the transaction.",
    "86-3": "2a1d1f03-ead9-a6ca-011c-7a47def5f850",
    "87-0": "",
    "87-1": "abc.deviceAgent",
    "87-2": "Contains the information of the type of device the customer is messaging from.",
    "87-3": "iPhone OS",
    "88-0": "",
    "88-1": "abc.capabilities",
    "88-2": "Contains the information of the features capabilities of the customer device such as auth, pay etc.",
    "88-3": "AUTH,1.00",
    "89-0": "",
    "89-1": "abc.listPickeritems",
    "89-2": "Array that contains the list picker item(s) selected by the customer.",
    "89-3": "",
    "90-0": "",
    "90-1": "abc.listPickerOtherItems",
    "90-2": "Array that contains the list picker item(s) not selected by the customer.",
    "90-3": "",
    "91-0": "",
    "91-1": "service.serviceKey",
    "91-2": "Contains the service key used for authenticating while sending the message.",
    "91-3": "",
    "92-0": "",
    "92-1": "abc.capabilityList",
    "92-2": "This parameter helps you find out if the device that you are using has the capability of supporting the Date Picker message feature. It is applicable for other message types as well.",
    "92-3": "",
    "93-0": "",
    "93-1": "abc.type",
    "93-2": "Type of the message. It’s “interactive” for Date Picker\t",
    "93-3": "",
    "94-0": "",
    "94-1": "abc.interactivePayload",
    "94-2": "",
    "94-3": "Sample Payload:  \n{  \n  \"replyMessage\": {  \n    \"style\": \"small\",  \n    \"alternateTitle\": \"Dec 28, 2023 at 12:00 PM\",  \n    \"title\": \"Dec 28, 2023 at 12:00 PM\"  \n  },  \n  \"datePicker\": {  \n    \"identifier\": \"Date\",  \n    \"timezoneOffset\": \"330\",  \n    \"location\": {},  \n    \"title\": \"BookAppointment\",  \n    \"timeslots\": [  \n      {  \n        \"duration\": \"1800\",  \n        \"identifier\": \"653\",  \n        \"startTime\": \"2023-12-28T06:30+0000\"  \n      }  \n    ]  \n  }  \n}",
    "95-0": "List Picker",
    "95-1": "",
    "95-2": "",
    "95-3": "",
    "96-0": "",
    "96-1": "abc.message",
    "96-2": "Contains the body of the incoming message.",
    "96-3": "NA",
    "97-0": "",
    "97-1": "abc.abcUserId",
    "97-2": "Unique userId of the customer with the corresponding business that never changes even if the customer changes their device.",
    "97-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "98-0": "",
    "98-1": "abc.listPickerItems",
    "98-2": "Array that contains the list picker item(s) selected by the customer.",
    "98-3": "`{\"identifier\":\"a2323\",\"style\":\"default\",\"title\":\"I1title\",\"url\":\"https://s3.amazonaws.com/appleattachment/4d7483af-0eb8-4e1e-8ac5-e8b3f7e5d110.jpeg\",\"order\":\"0\"}`",
    "99-0": "",
    "99-1": "abc.listPickerOtherItems",
    "99-2": "Array that contains the list picker item(s) not selected by the customer.",
    "99-3": "`{\"identifier\":\"S1Item1Identifier@123\",\"style\":\"default\",\"title\":\"I1title\",\"url\":\"https://s3.amazonaws.com/appleattachment/0b2f916d-e8cf-4807-98f8-f001838eec2b.jpeg\",\"order\":\"0\"},{\"identifier\":\"S2Item2Identifier@123\",\"style\":\"default\",\"title\":\"I2title\",\"url\":\"https://s3.amazonaws.com/appleattachment/b75c7f8b-2112-4c97-a232-494cc5b5f9be.jpeg\",\"order\":\"1\"}`",
    "100-0": "",
    "100-1": "abc.requestIdentifier",
    "100-2": "Request identifier of the timepicker message that was sent to the customer is returned in this variable.",
    "100-3": "listpicker123",
    "101-0": "",
    "101-1": "abc.replyMessageAlternateTitle",
    "101-2": "Title of the reply bubble as defined in the sent message.",
    "101-3": "I1title and I2title",
    "102-0": "",
    "102-1": "abc.locale",
    "102-2": "Language locale of the customer's device.",
    "102-3": "Value not getting. Need to raise bug",
    "103-0": "",
    "103-1": "abc.accountId",
    "103-2": "Unique account Id of the business as defined by Apple.",
    "103-3": "3364d419-4b4a-4f59-a767-ac7e60214baa",
    "104-0": "",
    "104-1": "abc.appId",
    "104-2": "Unique identifier of the app from which the app user has sent the request.",
    "104-3": "a_636893638318070000",
    "105-0": "",
    "105-1": "abc.timestamp",
    "105-2": "Record of the time when the request is received on <<prodname>> platform. For e.g. 1582627917.",
    "105-3": "2020-03-04T11:16:48.987Z",
    "106-0": "",
    "106-1": "abc.transId",
    "106-2": "Unique identifier corresponding to the transaction.",
    "106-3": "7fdc3a1f-b461-f5b8-bfcc-047d1898e86a",
    "107-0": "",
    "107-1": "abc.deviceAgent",
    "107-2": "Contains the information of the type of device the customer is messaging from.",
    "107-3": "iPhone OS",
    "108-0": "",
    "108-1": "abc.capabilities",
    "108-2": "Contains the information of the features capabilities of the customer device such as auth, pay etc.",
    "108-3": "AUTH,1.00",
    "109-0": "",
    "109-1": "abc.listPickeritems",
    "109-2": "Array that contains the list picker item(s) selected by the customer.",
    "109-3": "",
    "110-0": "",
    "110-1": "abc.listPickerOtherItems",
    "110-2": "Array that contains the list picker item(s) not selected by the customer.",
    "110-3": "",
    "111-0": "",
    "111-1": "service.serviceKey",
    "111-2": "Contains the service key used for authenticating while sending the message.",
    "111-3": "",
    "112-0": "",
    "112-1": "abc.capabilityList",
    "112-2": "This parameter helps you find out if the device that you are using has the capability of supporting the List Picker message feature. It is applicable for other message types as well.",
    "112-3": "",
    "113-0": "",
    "113-1": "abc.type",
    "113-2": "Type of the message. It’s “interactive” for List Picker",
    "113-3": "",
    "114-0": "",
    "114-1": "abc.interactivePayload",
    "114-2": "",
    "114-3": "Sample Payload\t  \n{  \n  \"replyMessage\": {  \n    \"imageIdentifier\": \"9190df46-3054-20e0-f227-1f8f4dd4a2b2\",  \n    \"style\": \"large\",  \n    \"alternateTitle\": \"I6 alone\",  \n    \"title\": \"I6 alone\"  \n  },  \n  \"listPicker\": {  \n    \"otherItemCount\": 3,  \n    \"selectedItemCount\": 1,  \n    \"otherItems\": [  \n      {  \n        \"identifier\": \"a232323\",  \n        \"style\": \"default\",  \n        \"title\": \"I1\",  \n        \"url\": \"https://s3.amazonaws.com/stagingappleattachment/36e9cb72-15df-486b-8dff-b860fb9fa39d.jpeg\",  \n        \"order\": \"0\"  \n      },  \n      {  \n        \"identifier\": \"231231\",  \n        \"style\": \"default\",  \n        \"title\": \"I3\",  \n        \"url\": \"https://s3.amazonaws.com/stagingappleattachment/f6da952f-b346-4e82-a6cc-5020df300f87.jpeg\",  \n        \"order\": \"1\"  \n      },  \n      {  \n        \"identifier\": \"21312\",  \n        \"style\": \"default\",  \n        \"title\": \"I4\",  \n        \"order\": \"2\"  \n      }  \n    ],  \n    \"selectedItems\": [  \n      {  \n        \"identifier\": \"32423423423\",  \n        \"style\": \"default\",  \n        \"title\": \"I6\",  \n        \"order\": \"1\"  \n      }  \n    ]  \n  }  \n}",
    "115-0": "Apple Pay",
    "115-1": "",
    "115-2": "",
    "115-3": "",
    "116-0": "",
    "116-1": "abc.abcUserId",
    "116-2": "Unique userId of the customer with the corresponding business that never changes even if the customer changes their device.",
    "116-3": "urn:mbid:AQAAY0aPiHTsDEzUfCKpalC9GpjVmP8/qnC2h7QD1ZmACRkPGQAEt/1DlNkhZQ6wkMFdmTJZ2OPls6gckV7VboJj39NMCYERacHhmgJ57VO814j0lGUyYJap3sBD26hmleqIC07leuHV2fJcwC3FQQdvVg/RAVY=",
    "117-0": "",
    "117-1": "abc.paymentStatus",
    "117-2": "Payment status of the payment request sent to the customer e.g. paid.",
    "117-3": "Paid",
    "118-0": "",
    "118-1": "abc.paymentReplyMessageTitle",
    "118-2": "Title of the reply bubble as defined in the sent message.",
    "118-3": "Reply title",
    "119-0": "",
    "119-1": "abc.paymentReplyMessageSubtitle",
    "119-2": "Subtitle of the reply bubble as defined in the sent message.",
    "119-3": "Paid CN¥100.10 with Pay",
    "120-0": "",
    "120-1": "abc.transId",
    "120-2": "Unique identifier corresponding to the transaction.",
    "120-3": "",
    "121-0": "",
    "121-1": "abc.accountId",
    "121-2": "Unique account Id of the business as defined by Apple.",
    "121-3": "",
    "122-0": "",
    "122-1": "abc.appId",
    "122-2": "Unique identifier of the app from which the app user has sent the request.",
    "122-3": "",
    "123-0": "",
    "123-1": "abc.requestIdentifier",
    "123-2": "Request identifier of the timepicker message that was sent to the customer is returned in this variable.",
    "123-3": "",
    "124-0": "",
    "124-1": "abc.type",
    "124-2": "Type of the message.",
    "124-3": "",
    "125-0": "Classical Authentication(Deprecated)",
    "125-1": "",
    "125-2": "",
    "125-3": "",
    "126-0": "",
    "126-1": "abc.authToken",
    "126-2": "Auth token returned by the authenticating system.",
    "126-3": "Authtoken: AQUxx-v6A7qc4dh-N9ZgCDc38LHKFzFM1zMxiiN1z9hgCo1b17NblPWDih3JSARgcv7cvBzNwSY3f9bgqWoYsmIJByG57UExQ4gw1fT0uCMUFbbPdJUx03rObWhUX47SPj_fI4v_T7ec1Jd3H5AQkzX-rTfJnawVIlC7fd8e-jm4GMxPqlkTjC3zWmmTZOYggdiQWBoj6g7EN0yBV-s0zwVdxE2ix7plbOfCkVo6qDVu6HLk0K3lPAQF5viXNcz9LXc8KHyj7zfjOV2bfUB2H6STkymRggKlC03O8F2RN3iDzK8kQq4-NlLvj_5OuvdKpReOXHFMMN-UCYhjngJ1lwmCKRmPbQ",
    "127-0": "",
    "127-1": "abc.authStatus",
    "127-2": "Status of the user authentication e.g., authenticated.",
    "127-3": "Authenticated",
    "128-0": "",
    "128-1": "abc.capabilities",
    "128-2": "Contains the information of the features capabilities of the customer device such as auth, pay etc.",
    "128-3": "AUTH,1.00",
    "129-0": "",
    "129-1": "abc.authReplyMessageTitle",
    "129-2": "Title of the reply bubble as defined in the sent message.",
    "129-3": "Reply message",
    "130-0": "",
    "130-1": "abc.authReplyMessageSubtitle",
    "130-2": "Subtitle of the reply bubble as defined in the sent message.",
    "130-3": "Reply message",
    "131-0": "",
    "131-1": "abc.abcUserId",
    "131-2": "Unique userId of the customer with the corresponding business that never changes even if the customer changes their device.",
    "131-3": "urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg=",
    "132-0": "",
    "132-1": "abc.transId",
    "132-2": "Unique identifier corresponding to the transaction.",
    "132-3": "",
    "133-0": "",
    "133-1": "abc.accountId",
    "133-2": "Unique account Id of the business as defined by Apple.",
    "133-3": "",
    "134-0": "",
    "134-1": "abc.appId",
    "134-2": "Unique identifier of the app from which the app user has sent the request.",
    "134-3": "",
    "135-0": "",
    "135-1": "abc.requestIdentifier",
    "135-2": "Request identifier of the timepicker message that was sent to the customer is returned in this variable.",
    "135-3": "",
    "136-0": "",
    "136-1": "abc.timestamp",
    "136-2": "Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917.",
    "136-3": "",
    "137-0": "",
    "137-1": "service.serviceKey",
    "137-2": "Contains the service key used for authenticating while sending the message.",
    "137-3": "",
    "138-0": "",
    "138-1": "abc.capabilityList",
    "138-2": "This parameter helps you find out if the device that you are using has the capability of supporting the OAuth feature. It is applicable for other message types as well.",
    "138-3": "",
    "139-0": "",
    "139-1": "abc.type",
    "139-2": "Type of the Message",
    "139-3": "",
    "140-0": "Quick Reply ",
    "140-1": "",
    "140-2": "",
    "140-3": "",
    "141-0": "",
    "141-1": "abc.abcUserId",
    "141-2": "Unique userId of the customer with the corresponding business that never changes even if the customer changes their device.",
    "141-3": "",
    "142-0": "",
    "142-1": "abc.appId",
    "142-2": "Unique identifier of the app from which the app user has sent the request.",
    "142-3": "",
    "143-0": "",
    "143-1": "abc.type",
    "143-2": "Type of the message. It’s “interactive” for Quick Replies.Type of the message. It’s “interactive” for Quick Replies.",
    "143-3": "",
    "144-0": "",
    "144-1": "abc.locale",
    "144-2": "Language locale of the customer's device.",
    "144-3": "",
    "145-0": "",
    "145-1": "abc.requestIdentifier",
    "145-2": "Request identifier of the timepicker message that was sent to the customer is returned in this variable.",
    "145-3": "",
    "146-0": "",
    "146-1": "abc.timestamp",
    "146-2": "Record of the time when the request is received on <<prodname>> platform. For e.g. 1582627917.",
    "146-3": "",
    "147-0": "",
    "147-1": "abc.selectedIdentifier",
    "147-2": "The selected identifier of the item .",
    "147-3": "",
    "148-0": "",
    "148-1": "abc.selectedIndex",
    "148-2": "The selected item number from top order.",
    "148-3": "",
    "149-0": "",
    "149-1": "abc.quickReplyItems",
    "149-2": "The full array of section items that were available for selection.",
    "149-3": "",
    "150-0": "",
    "150-1": "service.serviceKey",
    "150-2": "Contains the service key used for authenticating while sending the message.",
    "150-3": "",
    "151-0": "",
    "151-1": "abc.capabilityList",
    "151-2": "This parameter helps you find out if the device that you are using has the capability of supporting the Quick Reply message feature. It is applicable for other message types as well.",
    "151-3": "",
    "152-0": "",
    "152-1": "abc.interactivePayload",
    "152-2": "",
    "152-3": "Sample Payload  \n{  \n    \"quickReply\": {  \n    \"selectedIdentifier\": \"OptionA\",  \n    \"items\": [  \n      {  \n        \"identifier\": \"OptionA\",  \n      /  \"title\": \"Confirm\"  \n      },  \n      {  \n        \"identifier\": \"OptionB\",  \n        \"title\": \"Cancel\"  \n      }  \n    ],  \n    \"selectedIndex\": 0  \n  }  \n}",
    "153-0": "",
    "153-1": "abc.accountid",
    "153-2": "Unique account Id of the business as defined by Apple.abc.listPickeritemsArray that contains the list picker item(s) selected by the customer.",
    "153-3": "",
    "154-0": "Conversation closed",
    "154-1": "",
    "154-2": "",
    "154-3": "",
    "155-0": "",
    "155-1": "abc.abcUserId",
    "155-2": "Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device.",
    "155-3": "",
    "156-0": "",
    "156-1": "service.serviceKey",
    "156-2": "Contains the service key used for authenticating while sending the message.",
    "156-3": "",
    "157-0": "",
    "157-1": "abc.capabilityList",
    "157-2": "This parameter helps you find out if the device that you are using has the capability of supporting the new auth response message feature. It is applicable for other message types as well.",
    "157-3": "",
    "158-0": "",
    "158-1": "abc.appId",
    "158-2": "Unique identifier of the app from which the app user has sent the request.",
    "158-3": "",
    "159-0": "",
    "159-1": "abc.accountId",
    "159-2": "Unique account Id of the business as defined by Apple.",
    "159-3": "",
    "160-0": "",
    "160-1": "abc.type",
    "160-2": "Type of the Message.",
    "160-3": ""
  },
  "cols": 4,
  "rows": 161,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**RCS Node Output Variables**

| Incoming Event      | Output Variables | Description                                                                                    | Example                                                                                                                                                |
| :------------------ | :--------------- | :--------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Incoming Message    | rcs.text         | Incoming text message from end-customer.                                                       | rcsflow                                                                                                                                                |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on <<prodname>> platform.                      | 1584602304                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 4bd0eed2-b14f-9b27-c192-0b5f757b68e2                                                                                                                   |
| Incoming Attachment | rcs.fileUrl      | URL containing the attachment sent by the customer.                                            | <https://rcs-user-content-us.storage.googleapis.com/2fa59f37-3aa6-4110-b472-1ac570249892/c28d0e7f8ad803d7a3c507b8c289bf8b5efc422e3c1954e6a478a72cade6> |
|                     | rcs.fileName     | Name of the attachment sent by the customer.                                                   | IMG_20200318_093646_01.jpg                                                                                                                             |
|                     | rcs.fileSize     | Size of attachment sent by the customer in kb.                                                 | 145984                                                                                                                                                 |
|                     | rcs.mimeType     | File type of the customer sent by the customer e.g., img/png.                                  | Image/jpeg                                                                                                                                             |
|                     | rcs.text         | Incoming text message from end-customer.                                                       |                                                                                                                                                        |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on <<prodname>> platform.                      | 1584608632                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 798d8999-8d3a-90c7-49bb-560e8930aeeb                                                                                                                   |
| Postback Response   | rcs.postbackData | Contains the postback data configured for the suggestion clicked by customer.                  | Simple reply                                                                                                                                           |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on <<prodname>> platform. For e.g. 1582627917. | 1584604585                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 432f0042-9ded-b747-10ba-89bb1b15aba6                                                                                                                   |
| Location Response   | rcs.lattitude    | Lattitude of the location shared by the customer.                                              | 17.4347002                                                                                                                                             |
|                     | rcs.longitude    | Longitude of the location shared by the customer.                                              | 78.3985753                                                                                                                                             |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on <<prodname>> platform.                      | 1584616556                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 74ece05e-ff79-9318-2de7-966b680696e9                                                                                                                   |

<br />

## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)<br>  \n  \n**Note**: You can see this node edge only when you complete the node configuration.",
    "0-1": "\\* **onSuccess** - the flow exits through this node when it is a success. This node is replaced by a channel-specific node for every channel that you configure. For example, if you configure SMS, the **onSuccess** node event is replaced by <code>sms.mo</code> and for WhatsApp, the node event is <code>whatsapp.mo</code>.",
    "1-0": "Timeout (yellow/amber)",
    "1-1": "\\* **onTimeout** - the flow exits through this node outcome when no message was received within the specified timeout duration",
    "2-0": "Error (red)",
    "2-1": "\\* **onError** - the flow exits through this node outcome when there is an error"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


See the [example](#section-example) for configuration details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f0ca1c0-Receive_Node_Node_Outcomes.png",
        "Receive Node Node Outcomes.png",
        "Screenshot of Node Outcomes"
      ],
      "align": "center",
      "border": true,
      "caption": "Node Outcomes"
    }
  ]
}
[/block]


## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/271a534-Receive_Node_Transition_Actions.png",
        "Receive Node Transition Actions.png",
        "Screenshot of Transition Actions"
      ],
      "align": "center",
      "border": true,
      "caption": "Transition Actions"
    }
  ]
}
[/block]


## Example

A healthcare app sends reminders to its users about their upcoming medical appointments. In this use case, the receiving node waits for users' response (through SMS) to either confirm or cancel their appointment.<br>  
The node waits for the specified duration (**Max Timeout**) to receive a message sent **From Number** on the specified **Number** with any **Keyword**. See the following screenshot to understand the configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cd18a0e-Receive_Node_Configuration_to_receive_an_SMS.png",
        "Receive Node Configuration to receive an SMS.png",
        "Screenshot of Configuration to receive an SMS"
      ],
      "align": "center",
      "border": true,
      "caption": "Configuration to receive an SMS"
    }
  ]
}
[/block]