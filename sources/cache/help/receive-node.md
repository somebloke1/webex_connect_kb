# Receive Node

Source: https://help.webexconnect.io/docs/receive-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:52+00:00

The receive node allows you to wait for a response from the user. The response can be a message, a voice call, or an event like a button click (for example, **Accept** button in an interactive push notification) or a selection from a list (for example, choosing an option from a List Picker on Apple Messages for Business). <br>

You can also use the receive node to wait for external events to occur before resuming the flow. For example, a web application can resume the flow by invoking a custom event API when a user visits a website and fills an inquiry form.<br> 



![Receive Node](https://files.readme.io/63a62d6-Receive.jpg)




## Node Configuration

Double-click the node to configure it. Select the desired _channel_ to wait for a message or a _custom event_ to wait for an event. You can configure multiple channels/custom events on a single receive node. <br>

Specify the duration (in seconds), in the **Max Timeout** field, for which the node waits to receive a message on the selected channel(s). If there is no incoming message/event within the specified time period, the flow exits the node from **ontimeout** edge.



![Receive Node Configuration](https://files.readme.io/ae800ca-Receive.jpg)




## Channels and Events

The configuration window lists all the channels that the receiving node supports. The following table lists and explains all the required configurations for each of the channels:



| Channel - Property/Event | Description |
| --- | --- |
| **SMS**  | An inbound message (through SMS) from the user resumes the flow |
| Number | The number on which the user sends the message. This is the number you own on the platform.  <br>  <br>Please note that the platform provides an option to select numbers from the dropdown along with an option for Dynamic Configuration. If you decide to use the dynamic configuration, you will need to select the list of Sender IDs you wish to use in your flow through the dynamic number configuration. This extra step is needed to associate the flow with respective Sender IDs.  <br>  <br>You will be required to make this selection once you publish your flow by clicking on the Make Live button. |
| Keyword | A unique string received from the user to trigger the flow |
| From Number | The number from which the user sends the message |
| **Voice**  | An inbound voice call from the user resumes the flow |
| Voice Number | The number used to make outbound voice calls to the users. This is the number you own on the platform. |
| From | The number from which the user makes a voice call |
| **MMS** | An inbound message (through MMS) from the user resumes the flow |
| Number | The number on which the user sends the message. This is the number you own on the platform. |
| From Number | The number from which the user sends the message |
| **Messenger Message/Event** | An inbound message (through Messenger) from the user resumes the flow |
| From PSID | The PSID from which the user sends a message |
| Event Name:  <br>  <br>Incoming Message  <br>  <br>Postback  | Incoming Message event is triggered when a message has been sent to your Page.  <br>  <br>Postback occur when a postback button, Get Started button, or persistent menu item is tapped |
| **Instagram Message**   (Deprectaed)  | An inbound message (through Instagram) from the user resumes the flow. |
| From IGSID | The IGSID from which the user sends a message. |
| Event Name:  <br>  <br>Incoming Message  <br>  <br>Postback  <br>  <br>Delete Message | Incoming Message - This event occurs every time a user sends a text message with or without attachments to your Instagram account.  <br>  <br>Postback - This event is triggered when user clicks postback type button.  <br>  <br>Message Deleted - This event occurs every time a user sends a delete message to your Instagram account. |
| **WhatsApp Message** | An inbound WhatsApp from the user resumes the flow. |
| From WhatsAppID | The number from which the user sends a WhatsApp message |
| Sender Name | The username from which the message is sent |
| Event Name:  <br>  <br>Incoming Message  <br>  <br>Postback  <br>  <br>List Message  <br>  <br>Reply Buttons message | The event triggered by the user's response  <br>If a user taps a quick reply button, postback event is be used to process the event  <br>This event occurs every time a user selects one of the List Message options  <br>This event occurs every time a user selects one of the Reply Buttons  options |
| **Custom Event**  | The selected custom event resumes the flow along with post data from the event available as 'session data' |
| Custom Event | The trigger of the specified custom event resumes the flow |
| Resume Key | A unique key (per session) passed along with the custom event that resumes the flow |
| Value | A value for the resume key |
| Add Another Resume Key-Value | A button that lets you add another resume key-value pair |
| **Live Chat / In-App Messaging** | An inbound message within the app that resumes the flow |
| From (ThreadID) | A variable that contains thread id of the incoming message on the app |
| From (UserID) | The user id from which the app user sends the message |
| Event Name:  <br>  <br>Incoming Message  <br>  <br>Postback  <br>  <br>Form Response  | The event triggered by the user's response  <br>  <br>When a user taps on a quick reply button, or a button of type postback within a template message, then the response is received back on the platform as a Postback event.  <br>  <br>_Note: If you are configuring the receive node to wait on multiple live chat / in-app message response types at once, configure the 'Form Response' message type as the first to be able to configure the Form Response Content Type and Form Template details. Due to a bug, you won't be able to configure these if you don't configure Form Response as the first response event._ |
| Content Type:  <br>  <br>Static  <br>  <br>Dynamic | If Static is selected as Content Type, select the Form template to receive the Form Response  <br>  <br>If Dynamic is selected as Content Type, the output variable corresponding to the form will hold the entire payload which is received as the Form Response |
| Form Template | Select the required template when the Content Type is Static |
| **Email**  | An inbound email from the user resumes the flow  <br>_Note: If the incoming email attachments contains.msg files,the.msg attachments sent by customers might not be delivered to businesses if sent from MS Outlook email client due to an issue with MS Outlook._ |
| From (EmailID) | The email id from which the users sends the message​​​.  <br>The platform will not trigger or resume a flow, nor trigger a rule or an outbound webhook notification for incoming emails where Sender Email ID is same as the Recipient Email ID. However, details of such incoming emails will be available within Export Logs.  <br>  <br>For email sent via SMTP channel, we do not support delivery tracking. |
| **Apple Messages for Business Message/Event** | An inbound Apple Messages for Business message or event from the user resumes the flow. |
| From (Apple Messages for Business ID) | The ID from which the customer sends a message on Apple Messages for Business. For invitation responses, enter the variable that contains the AMB opaque ID or the customer's mobile number. |
| Event Name:  <br>  <br>Incoming Message  <br>  <br>InteractiveMessageResponse: Invitation  <br>  <br>InteractiveMessageResponse: QuickReply  <br>  <br>InteractiveMessageResponse: ListPicker  <br>  <br>InteractiveMessageResponse: TimePicker  <br>  <br>InteractiveMessageResponse: FormMessage  <br>  <br>InteractiveMessageResponse: Payment  <br>  <br>InteractiveMessageResponse: ClassicalAuthentication  <br>  <br>InteractiveMessageResponse: NewAuthentication  <br>  <br>InteractiveMessageResponse: iMessageApp | The event triggered by the customer's response.  <br>  <br>`InteractiveMessageResponse: Invitation` resumes the flow when the customer responds to an Apple Messages for Business invitation message. |
| **RCS Message/Event**  | An inbound RCS message/event from the user resumes the flow |
| From MSISDN | The mobile number from which the user sends a message an RCS message |
| Event Name:  <br>  <br>Incoming Message  <br>  <br>Postback Response  <br>  <br>Incoming Attachment  <br>  <br>Location Response  | The event triggered by the user's response |




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

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](https://help.webexconnect.io/docs/variable-management-in-flows).



![Input and Custom Variables](https://files.readme.io/97011e9-5.png)




> 📘 Note
> 
> All the numbers in the **To field** are represented using the "E+164" format. This format displays the number with a "+" followed by the country code and the phone number. This is not applicable to the numbers in the From field.

## Output Variables

The node-level [variables](https://help.webexconnect.io/docs/variable-management-in-flows) are auto-generated by each node and can be referenced in other nodes later in the flow. The auto-generated output variables contain the data that a node produces when the flow execution passes through that node. These variables are prefixed with the node id allowing unique access to each of these variables. For example, the customer response that a receive node captures is stored in the `nodeid.receive.message` output variable.<br>

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



| Incoming Event | Output Variables | Description | Example |
| --- | --- | --- | --- |
| Mobile Originated - MO | sms.keyword | Contains the keyword, if the incoming message has a keyword configured. | Key |
|  | sms.serviceNumber | The user's number the customer is sending the message to.  <br>Prefix the inbound number with the correct country code. | 4.47521E+11 |
|  | sms.message | Incoming text message from end-customer. | Flow |
|  | sms.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 2020-02-25T07:10:45.051Z |
|  | sms.transId | Unique identifier corresponding to the transaction. | 234190eb-df62-45c8-9281-c4b6f5b09c20 |
|  | sms.senderNumber | Number of the customer's handset from where the incoming message is originating. | 9.19676E+11 |
| On Link Click | sms.linkStatus |  | Active |
|  | sms.timestamp | Record of the time when the request is received on Webex Connect platform. | 2020-02-21T09:41:37.517Z |
|  | sms.transId | Unique identifier corresponding to the transaction. | 8f02482e-060c-4d07-8256-66791830e71c_85218130063343228 |
|  | sms.senderNumber | Number of the customer's handset from where the incoming message is originating. | 9.19676E+11 |




> 🚧 Note
> 
> It is mandatory to use the exact country code (for example, +44, +1) as the prefix to the numbers. Numbers without country code may lead to error in the receive node. "0" is not accepted as a valid country code.

**Voice Node Output Variables**

| Incoming Event | Output Variables    | Description                                                                                           | Example    |
| :------------- | :------------------ | :---------------------------------------------------------------------------------------------------- | :--------- |
| Missed Call    | voice.timestamp     | Record of the time when the request is received on Webex Connect platform.                             | 1582627917 |
|                | voice.transId       | Unique identifier corresponding to the transaction.                                                   |            |
|                | voice.serviceNumber | Number on Webex Connect to which the call was placed.                                                  |            |
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
|                  | messenger.timestamp         | Record of the time when the request is received on Webex Connect platform.                                                                                                                                                          | 1.5828E+12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                  | messenger.transId           | Unique identifier corresponding to the transaction.                                                                                                                                                                                | 6bbe6cb4-73b6-4c26-a8b6-fe39c13fdf26_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Postback         | messenger.postbackPayload   | Postback payload identifies customer's response to a quick reply, button or a persistent menu tap.                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.psId              | Page-scoped Identifier of a messenger, user used to reply back to end-customer. It gets generated on first incoming message from end-customer.                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.profilePicture    | URL of the first attachment in case of multiple attachments.                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.appId             | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.timestamp         | Record of the time when the request is received on Webex Connect platform.                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.transId           | Unique identifier corresponding to the transaction.                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**MMS Node Output Variables**



| Incoming Event | Output Variables  | Description | Example |
| --- | --- | --- | --- |
| Mobile Originated - MO | mms.serviceNumber | The user's number the customer is sending the message to. Prefix the inbound number with the correct country code. | 44 7111345232 |
|  | mms.timestamp | Record of the time when the request is received on Webex Connect platform.  | For e.g. 1582627917.  <br>  <br>2020-02-25T07:10:45.051Z |
|  | mms.transId | Unique identifier corresponding to the transaction. | 234190eb-df62-45c8-9281-c4b6f5b09c20 |
|  | mms.senderNumber | Number of the customer's handset from where the incoming message is originating. | 19052342345 |
|  | receive.message  | Incoming text message from end-customer. | Ducati |
|  | receive.channel | Identifies the channel from where the message has been received i.e. MMS. | MMS |
|  | receive.payload | Any required value that is not included in any other output variable comes under payload. |  |
|  | receive.attachment |  |  |




**Instagram Node Output Variables** 

> ❗️ 
> 
> The Instagram as a channel is deprecated.



| Incoming Event | Output Variables | Description | Example |
| --- | --- | --- | --- |
| Incoming Message, Postback, Message Deleted | instagram.messageId | Identifier for messages sent from the end customer to the business account | "messageId": "aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDU1NTM5NjA0NzQ4OjM0MDI4MjM2Njg0MTcxMDMwMDk0OTEyODE4NzA2OTgxOTg2OTI4NDozMDY4Nzg2MzU1NzM1OTI1MDY4MTA0OTUxMTc5NDU3MzMxMgZDZD" |
| Incoming Events | instagram.message | Incoming text message from end-customer. | Text Message: "Hi" |
| Postback | instagram.payload | Postback payload that identifies customer's response to a quick reply, template button. | "quickReplyPayload": "{"payload":"Add to cart","title":"Add to card"}", |
| Postback | instagram.title | Title of the Instagram account holder. |  |
| Postback, Incoming Message, Message Deleted | instagram.igsid | _ Page-scoped Identifier of an Instagram user used to reply back to end-customer. It gets generated on first incoming message from end-customer.  <br>_ Identifier for messages sent from the end customer to the business account  <br>\* Identified for messages deleted from the business account. | "igsid": "5275638769194520" |
| Postback, Incoming Message, Message Deleted | instagram.igid | _ Page-scoped Identifier of an Instagram Business account used to reply to end-customer. It gets generated on first incoming message from end-customer.  <br>_ Page-scoped Identifier of an Instagram Business account used to reply to end-customer. It gets generated on first incoming message from end-customer.  <br>\* Page-scoped identifier of an Instagram Business account used to delete a message from the customer. | “igid”: “17841454028327633“ |
| Postback, Incoming Message, Message Deleted | instagram.timestamp | _ Record of the time when the request is received on Webex Connect platform.  <br>_ Record of the time when the request is sent from the Webex Connect platform.  <br>\* Record of the time when the message is deleted from the Webex Connect platform. | "timestamp": "1663597769637" |
| Postback, Incoming Message, Message Deleted | instagram.event | \* To identify the event type - postback, incoming, or message deleted. | "event": "MO" ,  <br>"event": "OnPostback",  <br>"event": "OnMessageDeleted", |
| Postback, Incoming Message, Message Deleted | instagram.userId | The unique identifier of the app user. | "userId": "", |
| Postback, Incoming Message, Message Deleted | instagram.appId | Unique identifier of the app from which the app user has sent the request. | "appId": "a_637989151073720000", |
| Postback | instagram.quickReplyPayload | Payload that identifies the business account's response to the customer's quick reply. | "quickReplyPayload": "{"payload":"Order status"}" |
| Incoming Message | instagram.attachment | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message. | "attachment": "\`{"payload":{"url":"[https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=1671821199864696&signature=AbzzQo9GUu0Ca9prExszWgmwdrEXjvxRgW74CwYj53axqORubYJNapprzYMzZ2J4iW65I0VVYyTC-ayR9LGtmQchQsljxhLaNF8jnyLNgE-4F5O0CVU2eCYesdXJV_cXPZJYQnFIHE43uOW9ehdipjggYglEUmG2PgJG5_QMmphrdOycd8c1mAzvjmfKBNHMV5QRI37Q-gtXbotihRyvi-iY-xCJSqg\"},\"type\":\"image\"}](https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=1671821199864696&signature=AbzzQo9GUu0Ca9prExszWgmwdrEXjvxRgW74CwYj53axqORubYJNapprzYMzZ2J4iW65I0VVYyTC-ayR9LGtmQchQsljxhLaNF8jnyLNgE-4F5O0CVU2eCYesdXJV_cXPZJYQnFIHE43uOW9ehdipjggYglEUmG2PgJG5_QMmphrdOycd8c1mAzvjmfKBNHMV5QRI37Q-gtXbotihRyvi-iY-xCJSqg"},"type":"image"})]", |
| Postback, Incoming Message, Message Deleted | instagram.messageId | Contains the message Id for the message. | "messageId": "aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDU0MDI4MzI3NjMzOjM0MDI4MjM2Njg0MTcxMDMwMDk0OTEyODMwNjQwMjE1NjYyMzExMDozMDY4Nzk2OTMwMjU3ODk3OTU1MzAwNjU2NDU5ODA4NzY4MAZDZD", |
| Incoming Message | instagram.attachmentType | Type of attachment i.e. image, gif, quick reply, and video. | "attachmentType": "image",  <br>  <br>"attachmentType": "audio",  <br>  <br>"attachmentType": "video", |
| Incoming Message | instagram.attachmentUrl | URL of the first attachment in case of multiple attachments. | "attachmentUrl": "<https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=17964232888925487&signature=AbzxYfPgbyrbgqvQ4zWLayyMJo4fAM7JjR5atpeCLOQdFX5d3hObq1fw-kPBLDkyHiyYyTPbaOnzhVCPBrG9preKkdHA2W8sl0lCs7g8fWk2uaZ-lSu8MSnabAFfH91vWelUJl-8x_NN9ZEBOVTzThpbouP21CJA-IcOh_ODV79wAHaaLfB8v63XqgXv71fnXxKoA-gXneNwYxm3Y9r2nnWg6Na2gK8W">, |
| Incoming Message | instagram.storyReplyUrl | URL of the posted story’s reply from the end customer. | "storyReplyUrl": "<https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=17950801241174150&signature=AbzpNim0D-dMzZRWWmeGvcLBXGX8LjdfMHiS6_I6h_uXw8DslIq_INYv5HK2-dSGmANs3NaT2mraLIvKSVZoFAMl8Te-O9ahYqnmGlpaHDHxZInTCAjjBR6Ecao82ajuDF4c8Vuz9YjLemhC1Ct1L0ucQUPrCPH99xjWkTTA67PxHskgvuy95vS_MgPk1kNQF5Veqcb0Od-s6Jo8kspWRsNs16IXFflt>" |
| Incoming Message | instagram.repliedMessageId | Unique identifier of the reply received from the end customer. | "repliedMessageId": "aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDU0MDI4MzI3NjMzOjM0MDI4MjM2Njg0MTcxMDMwMDk0OTEyODMwNjQwMjE1NjYyMzExMDozMDY4Nzk3NjU3MjczMjk5Njk4MTMyNDM0MjA1MTczMzUwNAZDZD", |
| Incoming Message | instagram.reaction | Unique identifier of the emoticon reply received from the end customer. | "reaction": "{"reaction":"love","emoji":"❤️","action":"react"}", |




**WhatsApp Node Output Variables**



| Incoming Event | Output Variables | Description | Example |
| --- | --- | --- | --- |
| Incoming Message | whatsapp.message | Incoming text message from end-customer. | Hello |
|  | whatsapp.waId | The WhatsApp number of the end-customer. | 9.19964E+11 |
|  | whatsapp.bsuid | The Business-scoped User ID of the customer | IN.746868 |
|  | whatsapp.userHandle | WhatsApp username/handle of the sender, when available. | "\*\_ait_12" |
|  | whatsapp.attachmentType | Public url of the uploaded attachment. | Image, audio, video, document, and contact |
|  | whatsapp.locationAddress | Full address of the location. | Webex Connect, Plot No 770, Rd Number 44, Hyderabad, Telangana 500033 |
|  | whatsapp.locationLatitude | Location Latitude. | 17.434715270996 |
|  | whatsapp.locationLongitude | Location Longitude. | 78.3984832763671 |
|  | whatsapp.locationName | URL for the website where the user downloaded the location information. | Webex Connect |
|  | whatsapp.locationUrl | URL for the website where the user downloaded the location information. |  |
|  | whatsapp.imageUrl | URL of the image. |  |
|  | whatsapp.mimeType | Mime type of the attachment. |  |
|  | whatsapp.caption | Caption, if present along with image and video. |  |
|  | whatsapp.documentUrl | Direct URL of  the attachment ending with file type. |  |
|  | whatsapp.voiceUrl | Direct URL of  the attachment ending with file type. |  |
|  | whatsapp.audioUrl | Direct URL of  the attachment ending with file type. |  |
|  | whatsapp.attachments | The full attachment object available such as attachment type and media URL etc. sent by the app user as part of the incoming message.. May contain caption in case of image. |  |
|  | whatsapp.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | whatsapp.timestamp | Record of the time when the request is received on Webex Connect platform. |  |
|  | whatsapp.contextId | WhatsApp message Id | wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA== |
|  | whatsapp.systemBody | Removed |  |
|  | whatsapp.transId | Unique identifier corresponding to the transaction. |  |
|  | whatsapp.videoUrl | Direct URL of  the attachment ending with file type. |  |
|  | whatsapp.contacts | Full contact object containing addresses, phone numbers, emails etc. | Addresses: Array  <br>Birthday: YYYY-MM-DD formatted string  <br>Contact_image: Base64-encoded image  <br>Emails: Array  <br>IMS: Array  <br>Name: Array  <br>Org: Array  <br>Phones: Array  <br>URLs: Array |
|  | whatsapp.username | The username of the sender. |  |
|  | whatsapp.identityHash | Unique cryptographic hash key for a WhatsApp phone number. | 1 |
| Postback | whatsapp.waId | The WhatsApp number of the end-customer | \+919876543210 |
|  | whatsapp.bsuid | The Business-scoped User ID of the customer | IN.746868 |
|  | whatsapp.userHandle | WhatsApp username/handle of the sender, when available. | "\*\_ait_12" |
|  | whatsapp.buttonPayload | Developer-defined payload that will be returned when the button is clicked in addition to the display text on the button |  |
|  | whatsapp.buttonText | The button text that you have used while creating the template |  |
|  | whatsapp.contextId | WhatsApp message Id | wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA== |
|  | whatsapp.appId | Unique identifier of the app from which the app user has sent the request |  |
|  | whatsapp.timestamp | Record of the time when the request is received on Webex Connect platform. |  |
|  | whatsapp.transId | Unique identifier corresponding to the transaction. |  |
|  | whatsapp.identityHash | Unique cryptographic hash key for a WhatsApp phone number. | 1 |
| List Message | whatsapp.waId | The WhatsApp number of the end-customer. |  |
|  | whatsapp.bsuid | The Business-scoped User ID of the customer | IN.746868 |
|  | whatsapp.userHandle | WhatsApp username/handle of the sender, when available. | "\*\_ait_12" |
|  | whatsapp.listRowTitle |  |  |
|  | whatsapp.listRowIdentifier |  |  |
|  | whatsapp.listDescription |  |  |
|  | whatsapp.username | The username of the sender. |  |
|  | whatsapp.contextId | WhatsApp message Id | wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA== |
|  | whatsapp.type |  |  |
|  | whatsapp.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | whatsapp.timestamp | Record of the time when the request is received on Webex Connect platform. |  |
|  | whatsapp.transId | Unique identifier corresponding to the transaction. |  |
|  | whatsapp.identityHash | Unique cryptographic hash key for a WhatsApp phone number. | 1 |
| Reply Buttons  | whatsapp.waId | The WhatsApp number of the end-customer |  |
|  | whatsapp.bsuid | The Business-scoped User ID of the customer | IN.746868 |
|  | whatsapp.userHandle | WhatsApp username/handle of the sender, when available. | "\*\_ait_12" |
|  | whatsapp.replyButtonIdentifier |  |  |
|  | whatsapp.replyButtonTitle |  |  |
|  | whatsapp.username | The username of the sender. |  |
|  | whatsapp.contextId | WhatsApp message Id | wamid.HBgMOTE4MDk2MTIwNDA4FQIAERgSNzlBQUMwNTQ3NDFBNjdDQzkzAA== |
|  | whatsapp.type |  |  |
|  | whatsapp.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | whatsapp.timestamp | Record of the time when the request is received on Webex Connect platform. |  |
|  | whatsapp.transId | Unique identifier corresponding to the transaction. |  |
|  | whatsapp.identityHash | Unique cryptographic hash key for a WhatsApp phone number. | 1 |




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
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.extras                  | Contains additional information received in the message                                                                                  |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
|                              | inappmessaging.formResponse            | Captures the response received on the pre-chat form                                                                                      |         |
|                              | inappmessaging.formFields.Issue        | The issue/reason stated on the pre-chat form                                                                                             |         |
|                              | inappmessaging.formFields.Date         | The date on which the pre-chat form was submitted                                                                                        |         |
| Incoming Message             | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
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
| Interactive Message Response | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.pushId                  | The token generated by FCM or APNS at the time of user registration.                                                                     |         |
|                              | inappmessaging.pushType                | The type of push notification, conveying whether it's a silent or normal push notification.                                              |         |
|                              | inappmessaging.interactivePushResponse | The response or the button tapped on by the user within the interactive notification.                                                    |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Location Change              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.completedOn             |                                                                                                                                          |         |
|                              | inappmessaging.deviceId                | Unique identifier correspnding to the device from which the app user has sent the message.                                               |         |
|                              | inappmessaging.origin                  |                                                                                                                                          |         |
|                              | inappmessaging.version                 |                                                                                                                                          |         |
| onLinkClick                  |                                        |                                                                                                                                          |         |
| On Network Change            | inappmessaging.completedOn             |                                                                                                                                          |         |
|                              | inappmessaging.version                 |                                                                                                                                          |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.deviceId                | Unique identifier correspnding to the device from which the app user has sent the message.                                               |         |
|                              | inappmessaging.origin                  |                                                                                                                                          |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | Node outcomes                          | This is not an output variable.                                                                                                          |         |
| On Web Push Click            | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.pushId                  | The token generated by FCM or APNS at the time of user registration.                                                                     |         |
|                              | inappmessaging.pushType                | The type of push notification, conveying whether it's a silent or normal push notification.                                              |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| On Connect                   | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the event when connection between the app on Webex Connect is established.   |         |
| On Disconnect                | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the event when connection between the app on Webex Connect is closed.        |         |
| Profile Creation             | inappmessaging.profile.make            | The manufacturer of the device from which the app user has registerd.                                                                    |         |
|                              | inappmessaging.profile.os              | The operating system of the device from which the app user has registered.                                                               |         |
|                              | inappmessaging.profile.osVersion       | The version of the operating system of the device.                                                                                       |         |
|                              | inappmessaging.profile.sdkVersion      | The Webex Connect SDK version of the app.                                                                                                 |         |
|                              | inappmessaging.profile.model           | The model name of the device.                                                                                                            |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Profile Update               | inappmessaging.profile.make            | The manufacturer of the device from which the app user has registerd.                                                                    |         |
|                              | inappmessaging.profile.os              | The operating system of the device from which the app user has registered.                                                               |         |
|                              | inappmessaging.profile.osVersion       | The version of the operating system of the device.                                                                                       |         |
|                              | inappmessaging.profile.sdkVersion      | The Webex Connect SDK version of the app.                                                                                                 |         |
|                              | inappmessaging.profile.model           | The model name of the device.                                                                                                            |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| Roaming Change               |                                        |                                                                                                                                          |         |
| Subscribe                    | inappmessaging.topic                   | Name of the topic which the user has subsribed to.                                                                                       |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |
| unSubscribe                  | inappmessaging.topic                   | Name of the topic which the user has subsribed to.                                                                                       |         |
|                              | inappmessaging.userId                  | The unique identifier of the app user.                                                                                                   |         |
|                              | inappmessaging.timestamp               | Record of the time when the request is received on Webex Connect platform.                                                                |         |
|                              | inappmessaging.appId                   | Unique identifier of the app from which the app user has sent the request.                                                               |         |
|                              | inappmessaging.transId                 | Unique identifier corresponding to the transaction, which is the custom event in this case.                                              |         |

**Email Node Output Variables**

| Incoming Event        | Output Variables                     | Description                                                                                                                                                                                                                                                                                                                                           | Example                                                               |
| :-------------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| Incoming Message      | email.subject                        | Contains the subject of the incoming email.                                                                                                                                                                                                                                                                                                           | Email MO Start 1/2/3                                                  |
|                       | email.message                        | Contains the body of the incoming email.                                                                                                                                                                                                                                                                                                              | Email MO Start 2\\r\\n                                                |
|                       | email.emailId                        | Contains the email ID of the sender.                                                                                                                                                                                                                                                                                                                  | [connectautomation36@gmail.com](mailto:connectautomation36@gmail.com) |
|                       | email.transId                        | Unique identifier corresponding to the transaction.                                                                                                                                                                                                                                                                                                   | 2c25f71d-d014-4798-8e83-6d884b2931fa                                  |
|                       | email.timestamp                      | Record of the time when the request is received on Webex Connect platform.                                                                                                                                                                                                                                                                             | 2020-03-04T06:03:32.184Z                                              |
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
|                       | email.timestamp                      | Record of the time when the request is received on Webex Connect platform.                                                                                                                                                                                                                                                                             | 2020-03-04T15:27:27.409+05:30                                         |
|                       | email.attachments                    | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message.                                                                                                                                                                                                              | N/A                                                                   |
|                       | email.appId                          | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                                                                                                                                            | a_637172790998330000                                                  |

**Apple Messages for Business(AMB) Node Output Variables**

> 📘 List Picker
> 
> Please note that you may receive duplicate responses for the List Picker, if the customer responds through non-iOS Apple devices such as the MacBook.



| Incoming Event | Output Variables | Description | Example |
| --- | --- | --- | --- |
| Form Messages |  |  |  |
|  | abc.abcUserId | Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. | a_636893638318070000 |
|  | abc.type | Type of the message. It’s “interactive” for Form Messages. |  |
|  | abc.timestamp | Record of the time when the request is received on the Webex Connect platform. For e.g. 1582627917. | 2020-02-28T04:44:15.077Z |
|  | abc.locale | Language locale of the customer's device. | en_US |
|  | abc.requestIdentifier | Request identifier of the form message that was sent to the customer is returned in this variable. |  |
|  | abc.transId (only for Start Node) | Unique identifier corresponding to the transaction. |  |
|  | service.serviceKey (only for Start Node) | Contains the service key used for authenticating while sending the message. |  |
|  | abc.selections | Form response payload that captures the user’s responses across various pages of the form |  |
|  | abc.selectionsCount | Total number of pages in the form |  |
|  | abc.capabilityList | Helps you find out if the device that you are using has the capability to support the Form Messages message feature. It is applicable for other message types too. |  |
|  | abc.replyMessageAlternateTitle | Title of the reply bubble as defined in the sent message. | Mar 20, 2020 at 12:00 PM |
|  | abc.accountId | Unique account ID of the business as defined by Apple. | 3364d419-4b4a-4f59-a767-ac7e60214baa |
|  | abc.deviceAgent | Contains the information of the type of device the customer is messaging from. | iPhone OS |
|  | abc.interactivePayload | Available only in Start Node. The corresponding variable on the Receive Node is 'receive.payload'. | Sample Payload  <br>{  <br>  "replyMessage": {  <br>    "imageIdentifier": "551a9527-e8c1-4395-9431-885c7e8615f2",  <br>    "subtitle": "This is Subtitle",  <br>    "style": "small",  <br>    "alternateTitle": "Tap to view your response.",  <br>    "title": "Tap to view your response."  <br>  },  <br>  "formMessage": {  <br>    "template": "messageForms",  <br>    "private": false,  <br>    "selections": \[  <br>      {  <br>        "pageIdentifier": "1",  <br>        "subtitle": "Was the merchandise you received defective or not as the merchant described?",  <br>        "title": "Item Condition",  <br>        "items": [  <br>          {  <br>            "identifier": "101",  <br>            "type": "select",  <br>            "title": "Defective",  <br>            "value": "defective"  <br>          }  <br>        ]  <br>      },  <br>      {  <br>        "pageIdentifier": "2",  <br>        "subtitle": "Do you have any supporting documents that demonstrate that the product quality was not sufficient?",  <br>        "title": "Supporting Documents",  <br>        "items": [  <br>          {  <br>            "identifier": "202",  <br>            "type": "select",  <br>            "title": "No",  <br>            "value": "no"  <br>          }  <br>        ]  <br>      }  <br>    ],  <br>    "version": "1.1"  <br>  }  <br>} |
|  | abc.pciInfo.isPCICompliance |  |  |
|  | abc.pciInfo.isPCIValidationDone |  |  |
|  | abc.pciInfo.nonPCIComplianceReason |  |  |
|  | abc.pciInfo.isAttachmentEnabled |  |  |
|  | abc.pciInfo.droppedAttachmentCount |  |  |
| New Auth Response |  |  |  |
|  | abc.abcUserId | Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.authToken | Auth token returned by the authenticating system. | Authtoken: AQUxx-v6A7qc4dh-N9ZgCDc38LHKFzFM1zMxiiN1z9hgCo1b17NblPWDih3JSARgcv7cvBzNwSY3f9bgqWoYsmIJByG57UExQ4gw1fT0uCMUFbbPdJUx03rObWhUX47SPj_fI4v_T7ec1Jd3H5AQkzX-rTfJnawVIlC7fd8e-jm4GMxPqlkTjC3zWmmTZOYggdiQWBoj6g7EN0yBV-s0zwVdxE2ix7plbOfCkVo6qDVu6HLk0K3lPAQF5viXNcz9LXc8KHyj7zfjOV2bfUB2H6STkymRggKlC03O8F2RN3iDzK8kQq4-NlLvj_5OuvdKpReOXHFMMN-UCYhjngJ1lwmCKRmPbQ |
|  | abc.authStatus | Status of the user authentication e.g., authenticated. | Authenticated |
|  | abc.authReplyMessageTitle | Title of the reply bubble as defined in the sent message. | Reply message |
|  | abc.authReplyMessageAlternateTitle | Alternate Title of the reply bubble as defined in the sent message. | Reply message |
|  | abc.transId | Unique identifier corresponding to the transaction. |  |
|  | abc.accountId | Unique account ID of the business as defined by Apple. |  |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. | a_636893638318070000 |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 2020-02-28T04:44:15.077Z |
|  | abc.requestIdentifier | Request identifier of the new auth response message that was sent to the customer is returned in this variable. |  |
|  | service.serviceKey (only for Start Node) | Contains the service key used for authenticating while sending the message. | 54251909-59b9-11ed-9c39-02a06e0e48bf |
|  | abc.capabilityList | Helps you find out if the device that you are using has the capability of supporting the New Auth message feature. It is applicable for other message types as well. |  |
|  | abc.expiryTime | Expiry time of the access token expressed in seconds. |  |
|  | abc.type | Type of the Message.) |  |
| iMessage App Response |  |  |  |
|  | abc.abcUserId | Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. | a_636893638318070000 |
|  | abc.bid |  |  |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 2020-02-28T04:44:15.077Z |
|  | abc.locale | Language locale of the customer's device. | en_US |
|  | abc.requestIdentifier | Request identifier of the new auth response message that was sent to the customer is returned in this variable. | formmessage123 |
|  | abc.transId (only for Start Node) | Unique identifier corresponding to the transaction. |  |
|  | abc.url |  |  |
|  | service.serviceKey (only for Start Node) | Contains the service key used for authenticating while sending the message. | 54251909-59b9-11ed-9c39-02a06e0e48bf |
|  | abc.attachments | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message. | [{"size":"146021","name":"IMG_0869.jpeg","mimeType":"image/jpeg","type":"image","url":"https://s3.amazonaws.com/appleattachment/366ffe58-0e96-4f67-953d-478f8bdc29d5.jpeg"},{"size":"845196","name":"IMG_0990.mov","mimeType":"video/quicktime","type":"video","url":"https://s3.amazonaws.com/appleattachment/f23aa2cc-13e6-44b4-9e37-57368d3b38ee.quicktime"}] |
|  | abc.capabilityList | This parameter helps you find out if the device that you are using has the capability of supporting the new auth response message feature. It is applicable for other message types as well. |  |
|  | abc.replyMessageAlternateTitle | Title of the reply bubble as defined in the sent message. | Mar 20, 2020 at 12:00 PM |
|  | abc.accountId | Unique account ID of the business as defined by Apple. | 3364d419-4b4a-4f59-a767-ac7e60214baa |
|  | abc.deviceAgent | Contains the information of the type of device the customer is messaging from. | iPhone OS |
|  | abc.type | Type of the message.  |  |
|  | abc.pciInfo.isPCICompliance |  |  |
|  | abc.pciInfo.isPCIValidationDone |  |  |
|  | abc.pciInfo.nonPCIComplianceReason |  |  |
|  | abc.pciInfo.isAttachmentEnabled |  |  |
|  | abc.pciInfo.droppedAtt	  <br>abc.abcUserIdachmentCount |  |  |
| Incoming Message |  |  |  |
|  | abc.message | Contains the body of the incoming message. | Incomingmessage |
|  | abc.abcUserId | Unique user Id of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.attachmentCount | Count of total number of attachments. | 2 |
|  | abc.attachmentUrl | URL of the first attachment in case of multiple attachments. | <https://s3.amazonaws.com/appleattachment/366ffe58-0e96-4f67-953d-478f8bdc29d5.jpeg> |
|  | abc.attachmentType | Type of attachment i.e. image, gif and video. | image/jpeg (Only first Url mimetype coming) |
|  | abc.attachments | The full attachment object available such as images, videos, locations, files etc. sent by the app user as part of the incoming message. | `{"size":"146021","name":"IMG_0869.jpeg","mimeType":"image/jpeg","type":"image","url":"https://s3.amazonaws.com/appleattachment/366ffe58-0e96-4f67-953d-478f8bdc29d5.jpeg"},{"size":"845196","name":"IMG_0990.mov","mimeType":"video/quicktime","type":"video","url":"https://s3.amazonaws.com/appleattachment/f23aa2cc-13e6-44b4-9e37-57368d3b38ee.quicktime"}` |
|  | abc.locale | Language locale of the customer's device. | en_US |
|  | abc.accountId | Unique account Id of the business as defined by Apple. | 3364d419-4b4a-4f59-a767-ac7e60214baa |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. | a_636893638318070000 |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 2020-02-28T04:44:15.077Z |
|  | abc.transId | Unique identifier corresponding to the transaction. | c330c225-a541-c501-bdfe-971ada4cf168 |
|  | abc.intentId | Intent Id as configured in the entrypoint. |  |
|  | abc.groupId | Group Id as configured in the entry point. |  |
|  | abc.deviceAgent | Contains the information of the type of device the customer is messaging from. | iPhone OS |
|  | abc.capabilities | Contains the information of the features capabilities of the customer device such as auth, pay etc. | AUTH,1.00 |
| Date Picker |  |  |  |
|  | abc.message | Contains the body of the incoming message. | N/A |
|  | abc.abcUserId | Unique userId of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.datePickerTimeSlots | Array that contains the time slot selected by the customer e.g., [{"duration":"1800","identifier":"c020521e-cc3c-41fa-876e-a445237a6f83","startTime":"2020-03-20T06:30+0000"}]. | `{"duration":"1800","identifier":"c020521e-cc3c-41fa-876e-a445237a6f83","startTime":"2020-03-20T06:30+0000"}` |
|  | abc.datePickerTimeSlotsDuration | Duration of the time slot selected by the customer. | 1800 |
|  | abc.datePickerTimeSlotsIdentifier | Identifier of the time slot selected by the customer. | c020521e-cc3c-41fa-876e-a445237a6f83 |
|  | abc.datePickerTimeSlotsStartTime | Start time of the time slot selected by the customer. | 2020-03-20T06:30+0000 |
|  | abc.requestIdentifier | Request identifier of the timepicker message that was sent to the customer is returned in this variable. | datepicker123 |
|  | abc.replyMessageAlternateTitle | Title of the reply bubble as defined in the sent message. | Mar 20, 2020 at 12:00 PM |
|  | abc.locale | Language locale of the customer's device. |  |
|  | abc.accountId | Unique account Id of the business as defined by Apple. | 3364d419-4b4a-4f59-a767-ac7e60214baa |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. | a_636893638318070000 |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 2020-03-04T12:11:48.480Z |
|  | abc.transId | Unique identifier corresponding to the transaction. | 2a1d1f03-ead9-a6ca-011c-7a47def5f850 |
|  | abc.deviceAgent | Contains the information of the type of device the customer is messaging from. | iPhone OS |
|  | abc.capabilities | Contains the information of the features capabilities of the customer device such as auth, pay etc. | AUTH,1.00 |
|  | abc.listPickeritems | Array that contains the list picker item(s) selected by the customer. |  |
|  | abc.listPickerOtherItems | Array that contains the list picker item(s) not selected by the customer. |  |
|  | service.serviceKey | Contains the service key used for authenticating while sending the message. |  |
|  | abc.capabilityList | This parameter helps you find out if the device that you are using has the capability of supporting the Date Picker message feature. It is applicable for other message types as well. |  |
|  | abc.type | Type of the message. It’s “interactive” for Date Picker	 |  |
|  | abc.interactivePayload |  | Sample Payload:  <br>{  <br>  "replyMessage": {  <br>    "style": "small",  <br>    "alternateTitle": "Dec 28, 2023 at 12:00 PM",  <br>    "title": "Dec 28, 2023 at 12:00 PM"  <br>  },  <br>  "datePicker": {  <br>    "identifier": "Date",  <br>    "timezoneOffset": "330",  <br>    "location": {},  <br>    "title": "BookAppointment",  <br>    "timeslots": [  <br>      {  <br>        "duration": "1800",  <br>        "identifier": "653",  <br>        "startTime": "2023-12-28T06:30+0000"  <br>      }  <br>    ]  <br>  }  <br>} |
| List Picker |  |  |  |
|  | abc.message | Contains the body of the incoming message. | NA |
|  | abc.abcUserId | Unique userId of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.listPickerItems | Array that contains the list picker item(s) selected by the customer. | `{"identifier":"a2323","style":"default","title":"I1title","url":"https://s3.amazonaws.com/appleattachment/4d7483af-0eb8-4e1e-8ac5-e8b3f7e5d110.jpeg","order":"0"}` |
|  | abc.listPickerOtherItems | Array that contains the list picker item(s) not selected by the customer. | `{"identifier":"S1Item1Identifier@123","style":"default","title":"I1title","url":"https://s3.amazonaws.com/appleattachment/0b2f916d-e8cf-4807-98f8-f001838eec2b.jpeg","order":"0"},{"identifier":"S2Item2Identifier@123","style":"default","title":"I2title","url":"https://s3.amazonaws.com/appleattachment/b75c7f8b-2112-4c97-a232-494cc5b5f9be.jpeg","order":"1"}` |
|  | abc.requestIdentifier | Request identifier of the timepicker message that was sent to the customer is returned in this variable. | listpicker123 |
|  | abc.replyMessageAlternateTitle | Title of the reply bubble as defined in the sent message. | I1title and I2title |
|  | abc.locale | Language locale of the customer's device. | Value not getting. Need to raise bug |
|  | abc.accountId | Unique account Id of the business as defined by Apple. | 3364d419-4b4a-4f59-a767-ac7e60214baa |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. | a_636893638318070000 |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 2020-03-04T11:16:48.987Z |
|  | abc.transId | Unique identifier corresponding to the transaction. | 7fdc3a1f-b461-f5b8-bfcc-047d1898e86a |
|  | abc.deviceAgent | Contains the information of the type of device the customer is messaging from. | iPhone OS |
|  | abc.capabilities | Contains the information of the features capabilities of the customer device such as auth, pay etc. | AUTH,1.00 |
|  | abc.listPickeritems | Array that contains the list picker item(s) selected by the customer. |  |
|  | abc.listPickerOtherItems | Array that contains the list picker item(s) not selected by the customer. |  |
|  | service.serviceKey | Contains the service key used for authenticating while sending the message. |  |
|  | abc.capabilityList | This parameter helps you find out if the device that you are using has the capability of supporting the List Picker message feature. It is applicable for other message types as well. |  |
|  | abc.type | Type of the message. It’s “interactive” for List Picker |  |
|  | abc.interactivePayload |  | Sample Payload	  <br>{  <br>  "replyMessage": {  <br>    "imageIdentifier": "9190df46-3054-20e0-f227-1f8f4dd4a2b2",  <br>    "style": "large",  <br>    "alternateTitle": "I6 alone",  <br>    "title": "I6 alone"  <br>  },  <br>  "listPicker": {  <br>    "otherItemCount": 3,  <br>    "selectedItemCount": 1,  <br>    "otherItems": [  <br>      {  <br>        "identifier": "a232323",  <br>        "style": "default",  <br>        "title": "I1",  <br>        "url": "https://s3.amazonaws.com/stagingappleattachment/36e9cb72-15df-486b-8dff-b860fb9fa39d.jpeg",  <br>        "order": "0"  <br>      },  <br>      {  <br>        "identifier": "231231",  <br>        "style": "default",  <br>        "title": "I3",  <br>        "url": "https://s3.amazonaws.com/stagingappleattachment/f6da952f-b346-4e82-a6cc-5020df300f87.jpeg",  <br>        "order": "1"  <br>      },  <br>      {  <br>        "identifier": "21312",  <br>        "style": "default",  <br>        "title": "I4",  <br>        "order": "2"  <br>      }  <br>    ],  <br>    "selectedItems": [  <br>      {  <br>        "identifier": "32423423423",  <br>        "style": "default",  <br>        "title": "I6",  <br>        "order": "1"  <br>      }  <br>    ]  <br>  }  <br>} |
| Apple Pay |  |  |  |
|  | abc.abcUserId | Unique userId of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAY0aPiHTsDEzUfCKpalC9GpjVmP8/qnC2h7QD1ZmACRkPGQAEt/1DlNkhZQ6wkMFdmTJZ2OPls6gckV7VboJj39NMCYERacHhmgJ57VO814j0lGUyYJap3sBD26hmleqIC07leuHV2fJcwC3FQQdvVg/RAVY= |
|  | abc.paymentStatus | Payment status of the payment request sent to the customer e.g. paid. | Paid |
|  | abc.paymentReplyMessageTitle | Title of the reply bubble as defined in the sent message. | Reply title |
|  | abc.paymentReplyMessageSubtitle | Subtitle of the reply bubble as defined in the sent message. | Paid CN¥100.10 with Pay |
|  | abc.transId | Unique identifier corresponding to the transaction. |  |
|  | abc.accountId | Unique account Id of the business as defined by Apple. |  |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | abc.requestIdentifier | Request identifier of the timepicker message that was sent to the customer is returned in this variable. |  |
|  | abc.type | Type of the message. |  |
| Classical Authentication(Deprecated) |  |  |  |
|  | abc.authToken | Auth token returned by the authenticating system. | Authtoken: AQUxx-v6A7qc4dh-N9ZgCDc38LHKFzFM1zMxiiN1z9hgCo1b17NblPWDih3JSARgcv7cvBzNwSY3f9bgqWoYsmIJByG57UExQ4gw1fT0uCMUFbbPdJUx03rObWhUX47SPj_fI4v_T7ec1Jd3H5AQkzX-rTfJnawVIlC7fd8e-jm4GMxPqlkTjC3zWmmTZOYggdiQWBoj6g7EN0yBV-s0zwVdxE2ix7plbOfCkVo6qDVu6HLk0K3lPAQF5viXNcz9LXc8KHyj7zfjOV2bfUB2H6STkymRggKlC03O8F2RN3iDzK8kQq4-NlLvj_5OuvdKpReOXHFMMN-UCYhjngJ1lwmCKRmPbQ |
|  | abc.authStatus | Status of the user authentication e.g., authenticated. | Authenticated |
|  | abc.capabilities | Contains the information of the features capabilities of the customer device such as auth, pay etc. | AUTH,1.00 |
|  | abc.authReplyMessageTitle | Title of the reply bubble as defined in the sent message. | Reply message |
|  | abc.authReplyMessageSubtitle | Subtitle of the reply bubble as defined in the sent message. | Reply message |
|  | abc.abcUserId | Unique userId of the customer with the corresponding business that never changes even if the customer changes their device. | urn:mbid:AQAAYw0Y67QGE2NeYq9uX3t+UeD3B07eJDj86A/uU/XrcUiI6MNNF0VFr0iEsBjZGZLFY8sxy3Ia4FgBwguB7rja8tFvvYIJuvDzbFwDl3TIERGzlpN1sxk3rgbPSVyyzgODUIWc924JOO6WSDiFkzz8WHHoxwg= |
|  | abc.transId | Unique identifier corresponding to the transaction. |  |
|  | abc.accountId | Unique account Id of the business as defined by Apple. |  |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | abc.requestIdentifier | Request identifier of the timepicker message that was sent to the customer is returned in this variable. |  |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. |  |
|  | service.serviceKey | Contains the service key used for authenticating while sending the message. |  |
|  | abc.capabilityList | This parameter helps you find out if the device that you are using has the capability of supporting the OAuth feature. It is applicable for other message types as well. |  |
|  | abc.type | Type of the Message |  |
| Quick Reply  |  |  |  |
|  | abc.abcUserId | Unique userId of the customer with the corresponding business that never changes even if the customer changes their device. |  |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | abc.type | Type of the message. It’s “interactive” for Quick Replies.Type of the message. It’s “interactive” for Quick Replies. |  |
|  | abc.locale | Language locale of the customer's device. |  |
|  | abc.requestIdentifier | Request identifier of the timepicker message that was sent to the customer is returned in this variable. |  |
|  | abc.timestamp | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. |  |
|  | abc.selectedIdentifier | The selected identifier of the item . |  |
|  | abc.selectedIndex | The selected item number from top order. |  |
|  | abc.quickReplyItems | The full array of section items that were available for selection. |  |
|  | service.serviceKey | Contains the service key used for authenticating while sending the message. |  |
|  | abc.capabilityList | This parameter helps you find out if the device that you are using has the capability of supporting the Quick Reply message feature. It is applicable for other message types as well. |  |
|  | abc.interactivePayload |  | Sample Payload  <br>{  <br>    "quickReply": {  <br>    "selectedIdentifier": "OptionA",  <br>    "items": [  <br>      {  <br>        "identifier": "OptionA",  <br>      /  "title": "Confirm"  <br>      },  <br>      {  <br>        "identifier": "OptionB",  <br>        "title": "Cancel"  <br>      }  <br>    ],  <br>    "selectedIndex": 0  <br>  }  <br>} |
|  | abc.accountid | Unique account Id of the business as defined by Apple.abc.listPickeritemsArray that contains the list picker item(s) selected by the customer. |  |
| Conversation closed |  |  |  |
|  | abc.abcUserId | Unique user ID of the customer with the corresponding business that never changes even if the customer changes their device. |  |
|  | service.serviceKey | Contains the service key used for authenticating while sending the message. |  |
|  | abc.capabilityList | This parameter helps you find out if the device that you are using has the capability of supporting the new auth response message feature. It is applicable for other message types as well. |  |
|  | abc.appId | Unique identifier of the app from which the app user has sent the request. |  |
|  | abc.accountId | Unique account Id of the business as defined by Apple. |  |
|  | abc.type | Type of the Message. |  |




**RCS Node Output Variables**

| Incoming Event      | Output Variables | Description                                                                                    | Example                                                                                                                                                |
| :------------------ | :--------------- | :--------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Incoming Message    | rcs.text         | Incoming text message from end-customer.                                                       | rcsflow                                                                                                                                                |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on Webex Connect platform.                      | 1584602304                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 4bd0eed2-b14f-9b27-c192-0b5f757b68e2                                                                                                                   |
| Incoming Attachment | rcs.fileUrl      | URL containing the attachment sent by the customer.                                            | <https://rcs-user-content-us.storage.googleapis.com/2fa59f37-3aa6-4110-b472-1ac570249892/c28d0e7f8ad803d7a3c507b8c289bf8b5efc422e3c1954e6a478a72cade6> |
|                     | rcs.fileName     | Name of the attachment sent by the customer.                                                   | IMG_20200318_093646_01.jpg                                                                                                                             |
|                     | rcs.fileSize     | Size of attachment sent by the customer in kb.                                                 | 145984                                                                                                                                                 |
|                     | rcs.mimeType     | File type of the customer sent by the customer e.g., img/png.                                  | Image/jpeg                                                                                                                                             |
|                     | rcs.text         | Incoming text message from end-customer.                                                       |                                                                                                                                                        |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on Webex Connect platform.                      | 1584608632                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 798d8999-8d3a-90c7-49bb-560e8930aeeb                                                                                                                   |
| Postback Response   | rcs.postbackData | Contains the postback data configured for the suggestion clicked by customer.                  | Simple reply                                                                                                                                           |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on Webex Connect platform. For e.g. 1582627917. | 1584604585                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 432f0042-9ded-b747-10ba-89bb1b15aba6                                                                                                                   |
| Location Response   | rcs.lattitude    | Lattitude of the location shared by the customer.                                              | 17.4347002                                                                                                                                             |
|                     | rcs.longitude    | Longitude of the location shared by the customer.                                              | 78.3985753                                                                                                                                             |
|                     | rcs.number       | Number of the customer's handset where the incoming message is originating from.               | 9.16304E+11                                                                                                                                            |
|                     | rcs.timestamp    | Record of the time when the request is received on Webex Connect platform.                      | 1584616556                                                                                                                                             |
|                     | rcs.appId        | Unique identifier of the app from which the app user has sent the request.                     | a_157017189286805250                                                                                                                                   |
|                     | rcs.transId      | Unique identifier corresponding to the transaction.                                            | 74ece05e-ff79-9318-2de7-966b680696e9                                                                                                                   |

<br />

## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.



| Node Edge | Node Event/Outcome |
| --- | --- |
| Success (green)<br>  <br>  <br>**Note**: You can see this node edge only when you complete the node configuration. | \* **onSuccess** - the flow exits through this node when it is a success. This node is replaced by a channel-specific node for every channel that you configure. For example, if you configure SMS, the **onSuccess** node event is replaced by <code>sms.mo</code> and for WhatsApp, the node event is <code>whatsapp.mo</code>. |
| Timeout (yellow/amber) | \* **onTimeout** - the flow exits through this node outcome when no message was received within the specified timeout duration |
| Error (red) | \* **onError** - the flow exits through this node outcome when there is an error |




See the [example](#section-example) for configuration details.



![Node Outcomes](https://files.readme.io/f0ca1c0-Receive_Node_Node_Outcomes.png)




## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](https://help.webexconnect.io/docs/transition-actions).



![Transition Actions](https://files.readme.io/271a534-Receive_Node_Transition_Actions.png)




## Example

A healthcare app sends reminders to its users about their upcoming medical appointments. In this use case, the receiving node waits for users' response (through SMS) to either confirm or cancel their appointment.<br>  
The node waits for the specified duration (**Max Timeout**) to receive a message sent **From Number** on the specified **Number** with any **Keyword**. See the following screenshot to understand the configuration.



![Configuration to receive an SMS](https://files.readme.io/cd18a0e-Receive_Node_Configuration_to_receive_an_SMS.png)

