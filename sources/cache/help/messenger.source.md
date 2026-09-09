The Messenger node enables you to send text messages, images, audio files, video files, and a set of predefined templates to your customers over Facebook Messenger. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cf5fbd6-Messenger.jpg",
        "Messenger.jpg",
        "Screenshot of Messenger Node"
      ],
      "align": "center",
      "caption": "Messenger Node"
    }
  ]
}
[/block]


> 📘 Messenger Usage
> 
> - Messenger Usage in European Economic Area (EEA): Facebook Messenger has introduced some changes to comply with new privacy rules in Europe (refer [FAQs](https://developers.facebook.com/docs/messenger-platform/europe-updates/faq/)) starting 16 Dec 2020. Please [read this post](https://help.imiconnect.io/changelog/facebook-messenger-breaking-changes-for-europe) to understand how does this impact usage of <<prodname>> for Messenger.
> - Messenger as a channel is currently not supported in the Canada region.

## Prerequisites

1. [Messenger App](doc:messenger) - Configure a Facebook Messenger app on <<prodname>> from Assets -> Apps -> Configure New App' section to authorize <<prodname>> to use your Messenger page to send and receive messages.
2. Facebook Messenger requires the first message to be initiated by a customer or an explicit opt-in by the customer before you can send an outbound message using your Facebook page.

## Usage Guidelines for Messenger

[Messenger Standard Messaging Guidelines](https://developers.facebook.com/docs/messenger-platform/send-messages#standard_messaging): Typically, a Messenger page can only respond within a 24-hour window of having received the last customer message. Messages can be sent outside the 24-hour window for specific use cases using message tags.<br>

Below are the cases when a  user action would open the 24-hour standard messaging window for sending outbound messages:

1. The user sends a message to the Facebook Page
2. The user clicks a call-to-action button like **Get Started** within a Messenger conversation

## Messenger Messaging Types

The messages that you send using the Messenger node can be classified under one of the following messaging types:

- **Response** - The message is a response to a received message. This includes promotional and non-promotional messages sent inside the 24-hour standard messaging window or under the 24+1 policy. For example, use this messaging type to respond if a user asks for a reservation confirmation or a status update.
- **Update** - The message is being sent proactively and is not in response to a received message. This includes promotional and non-promotional messages sent inside the 24-hour standard messaging window or under the 24+1 policy.
- **Message Tags** - The message tags enable businesses to send important and personally relevant 1:1 updates to users outside the 24-hour standard messaging window for a set of approved use cases. For example, you may send updates about shipping and delivery, an upcoming reservation or flight, or alerts about a user's account. Refer [table](#section-supported-message-tags):

For more details about message tags and their supported use-cases, refer to [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) guide.

## Node Configuration

Double-click the node to open the configuration window. Select/specify various parameters to complete the node configuration.

1. Select a **Destination Type**.

**PS Id** - Facebook generates a unique identifier for each customer when they initiate a conversation with a Facebook Page. It is referred to as the page-scoped ID (PS Id) of that customer. PS Id of a Messenger user/customer is specific to a page, i.e., a user has different PS Ids for different Facebook pages.  
**Customer Id** - Primary key of the customer (user) profile. A customer profile can be created to link one or more channel-specific identifiers. <<prodname>> looks for the corresponding channel identifier for a given customer profile, based on the channel context and this allows for cross-channel communication. This can be used for customers whose PS Id has been associated with their customer id already.  
**Facebook User Ref** - [_Note: This used to be an option in <<prodname>> v4.x. This has now been deprecated and is not relevant for <<prodname>> 5.x platform users_.] The checkbox plug-in by Facebook is used to collect opt-ins from your website visitors to receive messages from you on Messenger. The checkbox plug-in is optimized for forms. For example, you can include the plug-in on an e-commerce website, where you wish to send receipts and order updates to the user. The [plug-in](https://developers.facebook.com/docs/messenger-platform/discovery) pushes a unique ID, i.e., user ref of your user when they opt-in to receive messages. This user ref is unique not just for every user, but for every time the plug-in is rendered.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a15f43d-Messenger.jpg",
        "Messenger Node Node Configuration.png",
        "Screenshot of Node Configuration Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Node Configuration"
    }
  ]
}
[/block]


2. Enter a **Destination** value.  
   The destination value must correspond to the selected destination type. This value can be static or dynamic. For example, on an incoming message/event to your Facebook page, the PS Id of the sender is stored in a session variable that can be accessed using the $(**messenger.psid**) output variable while replying.
3. Select a **Notification Type** (Optional)  
   REGULAR: sound/vibration  
   SILENT_PUSH: on-screen notification only  
   NO_PUSH: no notification.  
   Defaults to REGULAR.
4. Select a suitable **Message Type**.

### Text

It allows you to send simple text messages. Allows up to 2000 UTF-8 characters. Preview is not available for URLs in the text body.

**Text Formatting**: To format your messages use the following formatting symbols

[block:parameters]
{
  "data": {
    "h-0": "Formatting",
    "h-1": "Symbol",
    "h-2": "Example",
    "0-0": "**Bold**",
    "0-1": "Asterisk(\\*)",
    "0-2": "Input:  \n`Your total is *$10.50*.`  \nOutput:  \nYour total is **$10.50**.",
    "1-0": "_Italics_",
    "1-1": "Underscore (\\_)",
    "1-2": "Input:  \n`Welcome to _WhatsApp_!`  \nOutput:  \nWelcome to _WhatsApp_!",
    "2-0": "~~Strikethrough~~",
    "2-1": "Tilde (~)",
    "2-2": "Input:  \n`This is ~better~ best!`  \nOutput:  \nThis is ~~better~~ best!",
    "3-0": "`Monospace`",
    "3-1": "Three backticks (\\`\\`\\`)",
    "3-2": "Input:  \n` print 'Hello World';`  \nOutput:  \n`print 'Hello World'; `"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Image/Audio/Video/File

Use this option to include media like images/audios/videos or files in your messages. The supported types are:

- _Text_ - 
- _Image_
- _Audio_
- _Video_  
  Provide the attachment URL such that it ends with the file extension. The attachment size (image, audio, video or file) must not exceed 25 MB.

### Generic Template

A structured message that includes a title, subtitle, image, and up to three buttons. You can specify a bubble URL that will open in the Messenger web-view when the user taps the template.

Configure the following fields to send a message using a generic template:

- **Bubble Image Orientation** - the aspect ratio of the button used to render the image. Select _landscape_ (1.91:1) or _square_ (1:1). The default option is _landscape_.
- **Buttons** - allows you to offer the message recipient actions the user can take in response to the template, such as opening the Messenger web-view, sending a postback message to your webhook, and more. You can provision the following on-click actions using buttons:
- Postback - the event payload is sent back to <<prodname>> 
- Web URL - the webpage opens in a new tab
- Phone - the Dialer app opens with the pre-populated number
- Share - forwards the generic template message.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cc755e6-Generic_Template.PNG",
        "Generic Template.PNG",
        "Screenshot of Generic Template"
      ],
      "align": "center",
      "caption": "Generic Template"
    }
  ]
}
[/block]


### Button Template

The button template allows you to send a structured message that includes text with up to three attached buttons. This template is useful for offering the message recipient options to choose from, such as pre-determined responses to a question, or actions to take.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f0fbfa6-Button_Template.PNG",
        "Button Template.PNG",
        "Screenshot of Button Template"
      ],
      "align": "center",
      "caption": "Button Template"
    }
  ]
}
[/block]


### Receipt Template

The receipt template allows you to send an order confirmation as a structured message.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/64d509e-Receipt_template.PNG",
        "Receipt template.PNG",
        "Screenshot of Receipt Template."
      ],
      "align": "center",
      "caption": "Receipt Template"
    }
  ]
}
[/block]


Configure the below fields to send a receipt template message:

[block:parameters]
{
  "data": {
    "h-0": "Category",
    "h-1": "Content Items",
    "0-0": "Receipt Details",
    "0-1": "**Recipient Name** (String): The recipient's name.  \n**Order Number** (String): Unique identifier of the order.  \n**Currency** (String): The currency of the payment.  \n**Payment Method** (String): The payment method used. Providing enough information for the customer to decipher which payment method and account they used is recommended. This can be a custom string, such as, \"Visa 1234\".  \n**Order URL** (String): Redirection URL of the order.  \n**Timestamp** (String): Timestamp of the order in seconds.",
    "1-0": "Order Elements",
    "1-1": "**Title **(String): The name to display for the item.  \n**Subtitle **(String) :  _Optional_. The subtitle for the item, usually a brief item description.  \n**Quantity **(Number) : _Optional_. The quantity of the item purchased.  \n**Price **(Number): The price of the item. For free items, '0' is allowed.  \n**Currency **(String) : _Optional_. The currency of the item price.  \n**Image URL** (String) : _Optional_. The URL of the image to be displayed with the item.",
    "2-0": "Address",
    "2-1": "**Street 1** (String): The street address, line 1.  \n**Street 2** (String) : _Optional_. The street address, line 2.  \n**City** (String): The city name of the address.  \n**Postal Code** (String): The postal code of the address.  \n**State** (String): The state abbreviation for U.S. addresses, or the region/province for non-U.S. addresses  \n**Country** (String): The two-letter country abbreviation of the address.",
    "3-0": "Summary",
    "3-1": "**Subtotal** (Number) : _Optional_. The sub-total of the order.  \n**Shipping Cost** (Number) : Optional. The shipping cost of the order.  \n**Total Tax** (Number) : Optional. The tax of the order.  \n**Total Cost** (Number): The total cost of the order, including sub-total, shipping, and tax.  \n**Adjustments** (Array): Name and amount of the adjustment."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


#### Quick Replies

Quick replies provide a way to present a set of up to 11 buttons in-conversation that contains a title and optional image and appear prominently above the composer. You can also use quick replies to request a person's location. Quick replies can be configured for any of the above message types.

When a quick reply is tapped, the buttons are dismissed, and the title of the tapped button is posted to the conversation as a message. The button title and the payload of the chosen quick reply will be posted back to <<prodname>> for taking further actions.

> ❗️ Quick Reply image URL
> 
> The quick reply component currently requires the image_url as a mandatory parameter. We are working to gain a better understanding of this requirement and will have a resolution soon

### Correlation ID

You can assign a unique ID of your choice to each message. This ID is returned to the platform with the delivery report and can be used to identify the message.

### Callback Data

In case there is additional data to be sent along with the delivery reports to the URL, you must specify that here.

**Validations forCallback Data & Correlation ID**:

1. Callback Data, Correlation Id fields are optional for all the channels. Send node can be saved without providing these fields.
2. All characters, Alphabets, Numbers, and special characters are accepted.
3. Variables can be added.
4. Hard coded values are accepted.
5. On Platform side, there is no Max or Min length validation for these fields.

### Notify URL

You can choose to notify a URL with the delivery report for your preferred channel. This field accepts only a valid URL or a variable. If an invalid URL is passed in an API request or via a variable, then such a request will not be considered eligible for retries.

**Validations for Notify URL field:**

- It is an optional field for all the channels. Send node can be executed without including these values.
- The notify URL should be updated with the proper URL format. The system returns the error message when the Notify URL field is not updated correctly as ‘Invalid URL: field accepts only valid URL or variable.’
- When you provide a space in front of the URL, the system displays the 'Invalid URL: field accepts only valid URLs or variables' error message.
- When you provide space at the end of the URL, the system trims and ignores the space, and the URL receives delivery receipts (DRs).
- Select the **Enable Notify URL Auth** checkbox to activate the authentication of the notify URL.
- There is no maximum length validation defined for this field.
- Variables can be added to this field.

> 📘 Note:
> 
> Notify URLs track the status of delivery receipts (DRs) for sent messages.
> 
> If Enable Notify URL Auth is enabled for your node and an Auth ID that is random, invalid, or deleted is used, the payload will be parked in <<prodname>> and not forwarded to the receiver's server. However, this does not impact the delivery of the message.
> 
> If Enable Notify URL Auth is not enabled, the payload is forwarded to the receiver's server regardless of any invalid Auth ID used.

### Optional Parameters

- **Wait For**: The flow waits for one of the following conditions to be met for exiting the node.
  - _None_: The default option, exits the node immediately after executing the send.
  - _Gateway Submit_: Exits the node upon submitting the message to Facebook.
  - _Delivery Report_: Waits until receiving the delivery receipt for the message sent
- **Timeout**: Maximum time in seconds until which the node should wait for one of the 'Wait for' conditions to be met. The node exits through the `onDeliveryReportFail` node outcome edge when the set time elapses.
- **Expiry**: Two types of message expiry checks are supported
  - _UTC_: Time in UTC within which the message send should be attempted. For example, if the value is set to 2019-23-04 03:06:48 AM, the message is suppressed if a send attempt is made beyond the set time. 
  - _Seconds_: Maximum time in seconds within which the message must be submitted to WhatsApp.

The node exits through the `onPolicyFail` node outcome edge when the expiry condition cannot be met.

## Input Variables

You can see a list of all the flow variables available for this node under this pane. You can also search for a variable using the Search field. For more information, see the [Variable Management](doc:variable-management) section.

## Custom Variables

You can see the list of variables that you explicitly create and configure for this node under the Custom Variables pane. For more information, see the [Variable Management](doc:variable-management) section.

## Output Variables

You can see the data that this node generates as output variables. These [variables](doc:variable-management) are available for use in subsequent nodes. The standard output variables for this node are:

- **send.sendDateTime** - contains the date and time at which the message was sent from the node
- **send.gatewayId** - contains the gateway transaction id of the message
- **send.deliveryStatusDescription** - contains the delivery status - success or failure
- **send.deliveryStatusCode** - contains the delivery status code. See the[API Status Codes section](doc:api-codes) for the status codes.
- **send.repsonse_data** - contains the response that is received
- **send.response_interactive** - contains the response received through the interactive messages.

| Incoming Event   | Output Variables            | Receive Node | Start Node | Description                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :--------------- | :-------------------------- | :----------- | :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Incoming message | messenger.message           | Yes          | Yes        | Incoming text message from end-customer.                                                                                                                                                                                           | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                  | messenger.psId              | Yes          | Yes        | Page-scoped Identifier of a messenger, user used to reply back to end-customer. It gets generated on first incoming message from end-customer.                                                                                     | Image, Video, GIFs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                  | messenger.attachmentUrl     | Yes          | Yes        | URL of the first attachment in case of multiple attachments.                                                                                                                                                                       | <https://scontent.xx.fbcdn.net/v/t1.15752-9/72730271_417889542250561_2125819214483685376_n.jpg?_nc_cat=103&_nc_ohc=V7t4vOxTCQYAX8iKoJA&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=3823f14c0eea111080f58d3ee4d8245c&oe=5EF6C203>                                                                                                                                                                                                                                                                                                                     |
|                  | messenger.attachments\*     | Yes          | Yes        | The full attachment object available such as attachment type and media URL sent by the app user as part of the incoming message. May contain caption in case of Image.                                                             | [{"payload":{"url":"<https://scontent.xx.fbcdn.net/v/t1.15752-9/72730271_417889542250561_2125819214483685376_n.jpg?_nc_cat=103&_nc_ohc=V7t4vOxTCQYAX8iKoJA&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=3823f14c0eea111080f58d3ee4d8245c&oe=5EF6C203"},"type":"image"},{"payload":{"url":"https://scontent.xx.fbcdn.net/v/t1.15752-9/49442028_304527510181624_4550358914847211520_n.png?_nc_cat=103&_nc_ohc=aftIRUGfVdsAX8iQbkB&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=65561f3e90e1570f7feaf27af7400cda&oe=5EC19C85"},"type":"image"}>] |
|                  | messenger.locationUrl       | Yes          | Yes        | URL for the website where the user downloaded the location information.                                                                                                                                                            | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                  | messenger.locationLatitude  | Yes          | Yes        | Lattitude of the location shared by the customer.                                                                                                                                                                                  | For eg. 17.437008131462.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                  | messenger.locationLongitude | Yes          | Yes        | Longitude of the location shared by the customer.                                                                                                                                                                                  | For e.g. 78.39840389618.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                  | messenger.locationTitle     | Yes          | Yes        | Location Title.                                                                                                                                                                                                                    | For e.g. Daspalla D-Convention Hall, Road no: 37, Jubilee Hills, Hyderabad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                  | messenger.name              | Yes          | Yes        | Name of the messenger.                                                                                                                                                                                                             | For e.g. Jack Suraj.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                  | messenger.profilePicture    | Yes          | Yes        | Messenger returns Content Delivery Network (CDN) URLs which allow you to retrieve rich media content shared by users. The CDN URL is privacy-aware and will not return the media when the content has been deleted or has expired. | <https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=2534050010034596&width=1024&ext=1585393423&hash=AeSzgFDboc2HqIAm>                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | messenger.appId             | Yes          | Yes        | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                         | a_637183089024870000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                  | messenger.timestamp         | Yes          | Yes        | Record of the time when the request is received on IMIconnect platform.                                                                                                                                                            | 1.5828E+12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                  | messenger.transId           | Yes          | Yes        | Unique identifier corresponding to the transaction.                                                                                                                                                                                | 6bbe6cb4-73b6-4c26-a8b6-fe39c13fdf26_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                  | messenger.gender            | No           |            | Gender of the messenger.                                                                                                                                                                                                           | Male/Female                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Postback         | messenger.postbackPayload   |              |            | Postback payload identifies customer's response to a quick reply, button or a persistent menu tap.                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                  | messenger.psId              |              |            | Page-scoped Identifier of a messenger, user used to reply back to end-customer. It gets generated on first incoming message from end-customer.                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                  | messenger.profilePicture    |              |            | URL of the first attachment in case of multiple attachments.                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                  | messenger.appId             |              |            | Unique identifier of the app from which the app user has sent the request.                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                  | messenger.timestamp         |              |            | Record of the time when the request is received on IMIconnect platform.                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                  | messenger.transId           |              |            | Unique identifier corresponding to the transaction.                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. The node exits through one of the node edges corresponding to the outcome of the node.

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)",
    "0-1": "\\* **onSubmit** - the flow exits through this node when the message has been submitted.",
    "1-0": "Timeout (yellow/amber)",
    "1-1": "\\* **onTimeout** - the flow exits through this node when message request times out.",
    "2-0": "Error (red)",
    "2-1": "_ **onDeliveryReportFail** - the flow exits through this node when the delivery report has failed.  \n_ **onPolicyFail** - the flow exits through this node when there is a failure in the policy.  \n\\* **onError** - the flow exits through this node when there is an error."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Transition Actions

Use this tab to configure the transition actions for `On-enter`/`On-leave` events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

## Supported Message Tags

The message tags enable businesses to send important and personally relevant 1:1 updates to users outside the 24-hour standard messaging window for a set of approved use cases. 

### Supported Tags

| HUMAN_AGENT | When this tag is added to a message to a customer, it allows a human agent to respond to a person's message. Messages can be sent within 7 days of the person's. Human agent support is for issues that cannot be resolved within the standard 24 hour messaging window. |    |    |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :- | :- |

#### Message Tags Deprecated on **March 4, 2020**

The following table lists the messaging tags that are currently supported until March 04, 2020. Visit [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) guide for more information.

[block:parameters]
{
  "data": {
    "h-0": "Tag",
    "h-1": "Examples",
    "h-2": "Migration Notes",
    "0-0": "BUSINESS_PRODUCTIVITY",
    "0-1": "_ Notifications on services or products that a business has subscribed to or purchased from a service provider  \n_ Reminders or alerts on upcoming invoices or service maintenance  \n\\* Reports on performance, metrics, or recommended actions for the business",
    "0-2": "Partially covered as a the new tag POST_PURCHASE_UPDATE",
    "1-0": "COMMUNITY_ALERT",
    "1-1": "_ Request a safety check  \n_ Notify of an emergency or utility alerts",
    "1-2": "Partially covered as a the new tag NON_PROMOTIONAL_SUBSCRIPTION",
    "2-0": "CONFIRMED_EVENT_REMINDER",
    "2-1": "_ Upcoming classes or events that a person has signed up for  \n_ Confirmation of attendance to an accepted event or appointment",
    "2-2": "Partially covered as a the new tag CONFIRMED_EVENT_UPDATE",
    "3-0": "NON_PROMOTIONAL_SUBSCRIPTION",
    "3-1": "See Platform Policy Overview - Subscription Messaging",
    "3-2": "After March 04, 2020 will only be available to Pages on the Facebook News Page Index (NPI)",
    "4-0": "PAIRING_UPDATE",
    "4-1": "_ Match identified in dating app  \n_ Parking spot available",
    "4-2": "Not supported after January 15, 2020",
    "5-0": "APPLICATION_UPDATE",
    "5-1": "_ Application is being reviewed  \n_ Application has been approved  \n\\* Job application status",
    "5-2": "Partially covered as the tag ACCOUNT_UPDATE",
    "6-0": "ACCOUNT_UPDATE",
    "6-1": "_ Profile has changed  \n_ Preferences are updated  \n_ Settings have changed  \n_ Membership has expired  \n\\* Password has changed",
    "6-2": "Has a new expanded definition",
    "7-0": "PAYMENT_UPDATE",
    "7-1": "_ Send a receipt  \n_ Send an out-of-stock notification  \n_ Notify an auction has ended  \n_ Status on a payment transaction has changed",
    "7-2": "Partially covered as the new tag POST_PURCHASE_UPDATE",
    "8-0": "PERSONAL_FINANCE_UPDATE",
    "8-1": "_ Bill-pay reminders  \n_ Scheduled payment reminder  \n_ Payment receipt notification  \n_ Funds transfer confirmation or update  \n\\* Other transactional activities in financial services",
    "8-2": "Partially covered as the new tag ACCOUNT_UPDATE",
    "9-0": "SHIPPING_UPDATE",
    "9-1": "_ Product is shipped  \n_ Status changes to in-transit  \n_ Product is delivered  \n_ Shipment is delayed",
    "9-2": "Partially covered as the new tag POST_PURCHASE_UPDATE",
    "10-0": "RESERVATION_UPDATE",
    "10-1": "_ Itinerary changes  \n_ Location changes  \n_ Cancellation is confirmed  \n_ Hotel booking is cancelled  \n_ Car rental pick-up time changes  \n_ Room upgrade is confirmed",
    "10-2": "Partially covered as the new tag POST_PURCHASE_UPDATE",
    "11-0": "ISSUE_RESOLUTION",
    "11-1": "_ Issue is resolved  \n_ Issue status is updated  \n_ Issue requires a request for additional information  \n_ Follow up on a customer inquiry or support ticket",
    "11-2": "Partially covered as the new tag HUMAN_AGENT",
    "12-0": "APPOINTMENT_UPDATE",
    "12-1": "_ Appointment time changes  \n_ Appointment location changes  \n\\* Appointment is cancelled",
    "12-2": "Partially covered as the new tag CONFIRMED_EVENT_UPDATE",
    "13-0": "GAME_EVENT",
    "13-1": "_ Player's in-game crops are ready to be collected  \n_ Player's daily tournament is about to start  \n\\* Person's favorite soccer team is about to begin a match",
    "13-2": "Not supported after January 15, 2020",
    "14-0": "TRANSPORTATION_UPDATE",
    "14-1": "_ Flight status changes  \n_ Ride is canceled  \n_ Trip is started  \n_ Ferry has arrived",
    "14-2": "Partially covered as the new tag CONFIRMED_EVENT_UPDATE",
    "15-0": "FEATURE_FUNCTIONALITY_UPDATE",
    "15-1": "_ Chat with a live agent is added to your bot  \n_ A new skill is added to your bot",
    "15-2": "Partially covered as the new tag HUMAN_AGENT",
    "16-0": "TICKET_UPDATE",
    "16-1": "_ Concert start time changes  \n_ Event location changes  \n_ Show is cancelled  \n_ A refund opportunity is made available",
    "16-2": "Partially covered as the new tag CONFIRMED_EVENT_UPDATE"
  },
  "cols": 3,
  "rows": 17,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]