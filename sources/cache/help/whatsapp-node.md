# WhatsApp Node

Source: https://help.webexconnect.io/docs/whatsapp-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:52+00:00

WhatsApp node allows you to send text messages, messages with media attachments (audio, video, document and image), and template messages to your WhatsApp customers using a verified WhatsApp business account.



![WhatsApp Node](https://files.readme.io/397b4bf-Whatsapp.jpg)




## Prerequisites

The following are the prerequisites to use the WhatsApp node in your flows.

1. Configure a WhatsApp app on Webex Connect from Assets -> Apps -> Configure New App' section to authorize Webex Connect to use your WhatsApp account to send and receive messages.
2. To send proactive notification messages to your customers, you should create and submit a respective message template which should be approved by WhatsApp for the allowed messaging [use-cases](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates). You should configure these templates, submit them for approval and track the approval status from 'Tools -> Templates' section within Webex Connect.
   > 🚧 Get Opt-In for notification messages
   > 
   > You are required to obtain opt-in before opening marketing, utility, and authentication conversations with customers outside the 24-hour window. You can obtain opt-in in a multitude of ways, both on and off WhatsApp. Refer to the [Getting Opt-Ins](https://help.imiconnect.io/docs/whatsapp#getting-opt-ins) section in WhatsApp documentation for more details.

## Node Configuration

Drag and drop the WhatsApp node on the flow canvas. Double-click the node to configure a message request.



![Node Configuration](https://files.readme.io/cf3ede1-WhatsApp.jpg)




### Destination type

The destination type can be one of the following two options:

- ** WA ID **: WhatsApp ID (phone number including country code) of your customer/ recipient of this message.
- **Customer ID **: Primary key of customer profile. A customer profile can be created to link one or more channel-specific identifiers. Webex Connect intelligently looks up for the corresponding channel identifier under a given customer profile based on the channel context. This allows for cross-channel communication.

### Destination

The destination value corresponding to the selected Destination Type. The value can be static or dynamic.  
For e.g., on an incoming message/event to your WhatsApp business number, the WA ID of the sender will be stored in a session variable that can be accessed using $(whatsapp.whatsappId) while replying.

> 📘 Note
> 
> If +E.164 format is enabled for your tenant - all the numbers in the **To** field should follow the "+E.164" format.
> 
> This format displays the number with a "+" followed by the country code and the phone number.
> 
> \+E.164 format is not applicable to the numbers in the **From** field.

### Message Type

WhatsApp supports the following message types:

- **Text**: Text message; the length of the message is limited to 4096 characters.
- **Media**: Media attached messages including audio files, video files, documents, stickers, and images along with a caption (optional).
- **Template**: Rich message templates that can include media objects  (image/video/document), header, footer, and/or interactive components (like Call-to-action - CTA buttons and Quick Replies).
- **Location**: Send location by specifying latitude and longitude with an optional name and address.
- **Contact**: Share contacts to customers including details like addresses, phone numbers, websites, and so on.
- **List Messages**: Messages including a menu of up to 10 options. This type of message offers a simpler and more consistent way for users to make a selection when interacting with a business.
- **Reply Buttons**: Messages including up to 3 options —each option is a button. This type of message offers a quicker way for users to make a selection from a menu when interacting with a business. Reply buttons have the same user experience as interactive templates with buttons. 

> 📘 24 hour rolling window
> 
> Once a user contacts a business, the business can respond with any type of message in the next 24 hours. But if the business is contacting the user before user sends a message, or after 24 hours have passed, it can only send message using the template message type leveraging an approved template, created from within Tools->Templates section.
> 
> Free-form text messages, media, location, contact message, reply buttons or list messages will not work outside this 24 hour window. They will result in a failure callback with error.

#### Text

- **Text body**: The content of the text message, which can contain URLs and formatting. The length of the message is limited to 4096 characters. To format your messages use the following formatting symbols:



| Formatting | Symbol | Example |
| --- | --- | --- |
| **Bold**  | Asterisk(\*) | Input:  <br>`Your total is *$10.50*.`  <br>Output:  <br>Your total is **$10.50**. |
| _Italics_  | Underscore (\_) | Input:  <br>`Welcome to _WhatsApp_!`  <br>Output:  <br>Welcome to _WhatsApp_! |
| ~~Strikethrough~~ | Tilde (~) | Input:  <br>`This is ~better~ best!`  <br>Output:  <br>This is ~~better~~ best! |
| `Monospace` | Three backticks (\`\`\`) | Input:  <br>` print 'Hello World';`  <br>Output:  <br>`print 'Hello World'; ` |




- **Preview URL** (Optional): WhatsApp recognizes a URL in a text message and makes them clickable. Enable the checkbox to include a preview for the URL and make sure the URL begins with http\:// or https\://. If multiple URLs are in the body text string, only the first URL will be rendered. Follow the guidelines mentioned in [this](https://developers.facebook.com/docs/whatsapp/link-previews) page to make sure the URL preview is rendered by WhatsApp.

#### Media

- **File type & MIME type**: Select the appropriate file type and the corresponding MIME type. Here is a list of supported File types and MIME types.



| File type | MIME types | Maximum Size |
| --- | --- | --- |
| Audio | AAC, AMR, MPEG, OGG  <br>Note: For OGG MIME Type, only media codec supported by WhatsApp. Also, OPUS MIME Type is no longer supported by WhatsApp. | 16MB |
| Document | PDF, DOC, DOC(X), PPT, PPT(X), XLS, XLS(X), .TXT | 100MB |
| Image | JPG, JPEG, PNG | 5MB |
| Video | MP4, 3GPP  <br>Note: Only H.264 video codec and AAC audio codec is supported for MP4 Mime Type. | 16MB |
| Sticker | WEBP | Static stickers: 100KB  <br>Animated stickers: 500KB |




- **Payload**: Publicly accessible URL that is a direct link to the media. 

> 👍 WhatsApp Media Best Practices
> 
> - While uploading the media and setting the mime-type make sure you are following the guidelines mentioned in [MDN documentation](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Configuring_server_MIME_types#how_to_set_up_your_server_to_send_the_correct_mime_types).
> - The publicly accessible URL used while configuring the message must end in the same file format set under the 'File MIME type'. It should not have any geo-restriction and the URL should not have any jurisdiction.
> - Supported incoming media message mime-types are identical to outbound message media mime-types in Send node and Messaging API. The mime-type of the incoming media message can be captured as part of the following: 
>   - Start node and Receive node output variable i.e., "**whatsApp.mimetype**", 
>   - Outbound webhooks, Debug logs and Export logs with JSON path "**attachments.mime_type**"
> - WebP is a modern image format that provides superior lossless compression and creates smaller and richer images that makes web faster. The source libraries to use for converting an image to WebP file-format are available at the [Google WebP documentation](https://developers.google.com/speed/webp). You can also use various third-party converters publicly available to convert images to WebP file-format.

- **File Name** - Applicable for document media type. The document file will be saved as the entered 'file name' on the user’s device.

- **Caption**: Applicable for images and videos. The caption text is displayed along with the attachment.  
  Caption field had been previously used to identify filename for a document attachment in some scenarios. Make sure to copy the filename here as well for a document media attachment.

#### Stickers

Users can now send and receive custom Stickers through WhatsApp. You need to follow the below steps if you want to send a sticker.

- Select **WhatsApp** from the panel and double-click.
- Select **Message Type** as 'Media'.
- Select **Sticker ** from the **File Type** dropdown in the Message Configuration 
- Select **WebP** from the **MIME Type** dropdown (currently only WebP is available).

> 📘 Note
> 
> WebP is a modern image format that provides superior lossless compression and creates smaller and richer images that makes web faster. The source libraries to use for converting an image to WebP file-format are available here [<https://developers.google.com/speed/webp>]. You can also use various third-party converters publicly available to convert images to WebP file-format.

- Enter the direct URL pointing to the sticker in Payload.  



![Stickers](https://files.readme.io/d654221-WhatsApp1.jpg)




> 🚧 Note
> 
> Custom stickers must meet the following requirements:
> 
> - Each sticker has a transparent background.
> - Stickers must be exactly 512x512 pixels.
> - Each sticker must be less than 100 KB.

Apart from the above, the below points are also recommended while customizing a sticker:

- Adding an 8-pixel #FFFFFF stroke to the outside of each sticker is advised to be able to work with a variety of backgrounds, including white, black, colored, and patterned.
- The sticker image and the edge of the 512x512 pixel canvas should have a 16-pixel margin in between.



![Sticker Outline](https://files.readme.io/e485177-3d1bcfc-sticker_outline.png)




### Notification Messages using Templates

Once a user contacts a business, the business can respond with any type of message in the next 24 hours. These types of messages are free.

But if the business is contacting a user before the user sends a message or after more than 24 hours have passed, it can only send a message template. This is a paid notification.

Free-form text messages, media, document, or a contact message will not work outside this 24 hour window. They will result in a failure callback with error.

#### Template

> 📘 24-hour rolling window
> 
> Once a user contacts a business, the business can respond with any type of message in the next 24 hours. But if the business is contacting a user before the user sends a message or after more than 24 hours have passed, it can only send message using the template message type using an approved template from within Tools->Templates section.
> 
> Free-form text messages, media, document, contact message, reply buttons or list messages will not work outside this 24 hour window. They will result in a failure callback with error.

This message type allows you to send proactive messages using a pre-defined template to your users. A template should be registered from Tools > Templates section within Webex Connect platform. Include the following as part of a notification message using the template message type:

- Attachment (Video, Image and Document)
- Header and Footer text.
- Interactive buttons (Quick Reply and Call-to-action buttons)

For more information on how to create a template, refer [Template](https://help.imiconnect.io/docs/templates-whatsapp) doc.

Provide the following details under **Message Configuration**:



| Parameter | Description |
| --- | --- |
| Template Name | Select the required template from the drop-down list. The drop-down list displays all the pre-defined templates for WhatsApp that are already approved. |
| Header Parameters | Under **Header Parameters**, enter/select the following:  <br>  <br>> _ **Parameter Name** - the name of the parameter. This field is auto-populated based on the template you have selected.  <br>> _ **Parameter Type** - the type of the parameter. Supported types are _Text_, _Currency_, _Date-time_. Currency and Date time should be used to localize the content based on user's locale.  <br>> _ **Media URL** - a URL pointing to the document, video or image attachment.  <br>> _ **File Name** -  filename for document attachment.  <br>> \* **Value** - the value of the parameter. |
| Body Parameters | Under **Body Parameters**, enter/select the following:  <br>  <br>> _ **Parameter Name** - the name of the parameter. This field is auto-populated based on the template you have selected. The parameter name is "OTP" for Authentication templates.  <br>> _ **Parameter Type** - the type of the parameter. Supported types are _Text_, _Currency_, _Date-time_. Currency and Date time should be used to localize the content based on user's locale.<br>><br>> > _ **Currency** params- **Code** indicates the code of the language or locale to use; **Amount** is the currency amount multiplied by 1000. E.g, for USD 9.99, specify the amount as 9990; the **Default value** is used when the localization fails.  <br>> > _ **Date and time** - Epoch timestamp is the Unix timestamp showing the number of seconds that have elapsed since 00:00:00, 1 January 1970 (UTC), minus leap seconds. [JavaScript](https://jsfiddle.net/tbxac0de/) for converting local time to Unix epoch; the **Default value** is used when the localization fails.  <br>> > \* **Value** - the value of the parameter.The following buttons can only be configured with Authentication category Templates\> - OTP - the value of the One-time-Password |
| Identity Key Hash | Enter the Identity key hash of the customer. Use this to authenticate the identity of the customer. If there is a mismatch of the hash, the message will not be delivered. This is an optional field. |
| Footer (Optional) | Optional footer text. This needs to be specified while creating a template. |
| Buttons (Optional) | You can see the configured interactive buttons in this section. The interactive buttons can either be a Call-To-Action (CTA) or a Quick Reply (QR) button.  <br>**Call-To-Action** (CTA) - Supported types: Call phone and Visit website. In case of Visit website, you can define a dynamic URL path to append with URL domain (domain should be pre-defined while registering a template).  <br>You can have a maximum of one button type of each type per message, i.e, one Call Phone Number button and one Visit Website button. WhatsApp allows a maximum of two CTA buttons.  <br>**Quick Replies** (QR) - use this button to configure quick replies like Yes, No, Maybe. You can use a maximum of three QR buttons.  <br>Define a payload to each QR button, this will be received back as part of the Postback event in receive node.  <br>The following buttons can only be configured with Authentication category Templates  <br>\_ **OTP transfer buttons **  <br>**Auto-fill**- This button type will include a button for sharing the code with your app when the customer taps the button on their device.  <br>**Copy-Code** -This button type will include a button for customers to copy and paste the code into their app. |






![WhatsApp Message Previews for Template Messages](https://files.readme.io/9da9053-Hash.png)




You can create your own templates, submit them for approval to WhatsApp, and track approval status using Webex Connect's Template Management section accessible under 'Tools > Templates'.

When you select a template that has interactive buttons within it you need to configure it. In the case of a template with CTA buttons, you need to provide the URL Suffix. The URL Suffix appends to the pre-defined URL and personalizes the link for the users. For QR buttons, you need to provide the button payload. The payload that you configure here identifies the QR button.

The following image shows the configuration for an interactive template with CTA buttons:



![Interactive Template with CTA Buttons](https://files.readme.io/332e6aa-3.png)




The following image shows the configuration for an interactive template with QR buttons:



![Interactive Template with QR Buttons](https://files.readme.io/56b11f0-4.png)




The following image shows the configuration for an authentication template with the Auto-fill option enabled:



![Authentication Template with Auto-fill button](https://files.readme.io/6f64f7f-WhatsApp25.png)




### Supported Media Types for Marketing and Utility category templates

| Media    | Template Message - Header Media URL file format | Maximum Size |
| :------- | :---------------------------------------------- | :----------- |
| Document | TXT, PDF, PPT, DOC, DOC(X), PPT(X), XLS(X)      | 100 MB       |
| Video    | 3GPP, MP4                                       | 16MB         |
| Image    | PNG, JPEG                                       | 5MB          |

### Location

This message type allows you to send location details to your users. Provide the following details under **Message Configuration**:

| Parameter | Description                                                                            |
| :-------- | :------------------------------------------------------------------------------------- |
| Latitude  | The latitude of the location                                                           |
| Longitude | The longitude of the location                                                          |
| Name      | The name of the location                                                               |
| Address   | The address of the location. The address is displayed only if the location has a name. |

### Contact

This message type allows you to send contact details to your users. Provide the following details under **Message Configuration**:



| Parameter | Description |
| --- | --- |
| Formatted Name | The full name of the contact as it normally appears |
| Prefix | The prefix of the contact like Mr, Ms, Mrs, Dr, Col etc.  <br>  <br>Do not use punctuation in this field. |
| First Name | The first name of the contact |
| Last Name | The last name of the contact |
| Middle Name | The middle name of the contact |
| Suffix | The prefix of the contact like Jr, Sr, PhD, MD, Ret etc.  <br>  <br>Do not use punctuation in this field. |
| Address(es) (optional) | The address or addresses of the contact, if any |
| Email(s) (optional) | The email or email addresses of the contact, if any |
| Phone Number(s) (optional) | The phone number(s) of the contact, if any |
| Birthday (optional) | The birthday fo the contact, if you wish to provide |
| Website(s) (optional) | The website of the contact, if any |
| Organization (optional) | The organization of the contact, if you wish to provide |




### List Message

- Header Text – Description about the list. It must be in text format. This is an optional field. Maximum of 60 characters is supported.
- Message Body – Body of the message. Maximum of 1024 characters is supported.
- Footer Text – Additional notes. It must be in text format. This is an optional field. Maximum of 60 characters is supported.
- List Title – Title of the list button. Maximum of 24 characters is supported.
- Configure List Items – Click this to configure the list of the options.
- List Section: Must contain a title and at least one row. You can add a maximum of 10 sections.
  - Row Title: Title of the row.
  - Identifier: A unique identifier for the row. This is returned as part of the incoming event when the row is selected by the user. Maximum of 200 characters is supported.
  - Description: Optional description about the row. Maximum of 72 characters is supported.
  - Add Row: Click this to add another row in the section.
  - '+' icon: Click this to add another section in your list.
  - '>' icon: Use this to navigate between sections.
  - Save: Click this to save the list options.
- List Messages are best for presenting several options, such as:
  - A customer care or FAQ menu
  - A take-out menu
  - Selection of nearby stores or locations
  - Available reservation times
  - Choosing a recent order to repeat

### Reply Buttons

- Reply Buttons: Messages including up to 3 options —each option is a button. This type of message offers a quicker way for users to make a selection from a menu when interacting with a business. Reply buttons have the same user experience as interactive templates with buttons. 
- Header Type – Text, image, video, or document.  Provide a media URL for video, image, and document. For text, add a text field with the required content. Maximum of 60 characters is supported for text.
- Message Body – Body of the message. Maximum of 1024 characters is supported.
- Footer Text – Additional notes. It must be in text format. This is an optional field. Maximum of 60 characters is supported.
- Replies – You can configure up to 3 reply buttons.
- Reply Title: Unique title for the reply option. Maximum of 20 characters is supported.
- Identifier: A unique identifier for the reply option. This is returned as part of the incoming event when the option is selected by the user. Maximum of 200 characters is supported.
- Add New: Click this to add a new reply option.
- Save: Click this to save the configuration. 

Reply Buttons are best for offering quick responses from a limited set of options, such as:

- Airtime recharge
- Changing personal details
- Reordering a previous order
- Requesting a return
- Adding optional extras to a food order
- Choosing a payment method

Reply buttons are particularly valuable for ‘personalized’ use cases where a generic response is not adequate.

### List Message and Reply Buttons Specifications

- List Messages and Reply Buttons can be combined together in the same flow.
- A user can only select one option at the same time from a list or button message, but they can go back and re-select a previous message.
- List or reply button messages cannot be used as notifications. Currently, they can only be sent within 24 hours of the last message sent by the user. If you try to send a message outside the 24-hour window, you get an error message.
- Supported platforms: iOS, Android, and web.

See how text messages compare to interactive messages:



![Screenshot of Interactive Messages.](https://files.readme.io/0428ca0-WhatsApp_List.png)




See an example of how List messages and Reply buttons can be combined in the same flow:

[block:embed]
{
  "html": false,
  "url": "https://awsprodemailassets.s3.amazonaws.com/8716f921-4921-4b93-9d4c-9a0732eb37cd/check2_2260738676879633.mp4",
  "title": "iframe",
  "favicon": null,
  "provider": "awsprodemailassets.s3.amazonaws.com",
  "href": "https://awsprodemailassets.s3.amazonaws.com/8716f921-4921-4b93-9d4c-9a0732eb37cd/check2_2260738676879633.mp4",
  "typeOfEmbed": "iframe",
  "height": "500px",
  "width": "500%",
  "iframe": true
}
[/block]


### Identity key hash

WhatsApp enables you to authenticate the identity of the customer to make sure you are communicating with the intended person. This becomes critical for use-cases such as sending OTP messages. As a solution for this, businesses can utilise the cryptographic identity key hash field managed by WhatsApp against customer’s identity.  
The hash is matched with the hash in the message requests sent from Webex Connect platform.

You can capture the Identity key hash of a trusted WhatsApp customer (at the time) as part of the output variables of Start Node, Receive Node, and within the [Delivery Receipt payloads](https://developers.imiconnect.io/reference/whatsapp-outbound-webhooks) 

When sending any sensitive information, PII data or an authentication template message (containing one-time password), business should include the Identity key hash within the WhatsApp send node or messaging API.

Whenever there is a **potential identity change** (due to theft or user updating to a new device), WhatsApp updates the cryptographic hash. When business sends a message to the WhatsApp user with the old hash, the delivery of the message fails as the hashes do not match. Subsequently, an error code is sent to notify about the message delivery failure as part of the delivery receipts. This indicates that the customer’s phone number can no longer be authenticated.

> 📘 Messages without Identity key hash
> 
> Messages sent without including the Identity key hash will continue to be delivered as expected, disregarding any number ownership change or potential impersonation of the intended customer.

#### Getting new Identity key hash

Business might need to resume communication with the WhatsApp customer in-case the potential identity change was inaccurately suggested by WhatsApp. To identify such scenario business should re-authenticate the customer using a trusted channel outside of WhatsApp. Once the customer is re-authenticated, business can capture the new Identity key hash by either of the following two methods:

- Sending a message to the WhatsApp customer without including the Identity key hash. The updated hash can be captured as part of the delivery receipt.
- When a messages is received from the customer, the new hash can be captured as part of incoming message payload within Outbound webhooks, Export Logs, Debug logs, Start Node, and Receive Node.

> 🚧 Managing Hash
> 
> Business should save and manage the hash for their customers and include the hash in the messages containing any sensitive information, PII data or an authentication template message (containing one-time password).

### Correlation ID

You can assign a unique ID of your choice to each WhatsApp message. This ID is returned to the platform with the delivery report and can be used to identify the message.

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
> If Enable Notify URL Auth is enabled for your node and an Auth ID that is random, invalid, or deleted is used, the payload will be parked in Webex Connect and not forwarded to the receiver's server. However, this does not impact the delivery of the message.
> 
> If Enable Notify URL Auth is not enabled, the payload is forwarded to the receiver's server regardless of any invalid Auth ID used.

### Optional Parameters

- **Wait For**: The flow waits for one of the following conditions to be met for exiting the node.
  - None: The default option, exits the node immediately after executing the send
  - Gateway Submit: Exits the node upon submitting the message to WhatsApp
  - Delivery Report: Waits until receiving the delivery receipt for the message sent
  - Read: Waits until the customer has read the message.
- **Timeout**: Maximum time in seconds until which the node should wait for one of the 'Wait for' conditions to be met. The node exits via the 'onDeliveryReportFail' node outcome edge when the set time elapses.

> 📘 Wait for condition on Read
> 
> If a customer disables read receipt in their WhatsApp privacy settings, the node keeps waiting for the read receipt until the set expiry time.

- **Expiry**: 2 types of message expiry checks are supported
- UTC: Time in UTC within which the message send should be attempted. For example, if the value is set to 2019-23-04 03:06:48 AM, the message is suppressed if a send attempt is made beyond the set time. 
- Seconds: Maximum time in seconds within which the message must be submitted to WhatsApp.

The node exits via the 'onPolicyFail' node outcome edge when the expiry condition cannot be met.

## Output Variables

You can see the data that this node generates as output [variables](https://help.webexconnect.io/docs/variable-management-in-flows). These variables are available for use in subsequent nodes. 

| Output Variable                | Description                                                                              | Example                                                                                   |
| :----------------------------- | :--------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| send.deliveryStatusCode        | [List of status codes](https://developers.imiconnect.io/reference#section-whats-app)     |                                                                                           |
| send.deliveryStatusDescription | [Status code descriptions](https://developers.imiconnect.io/reference#section-whats-app) | Success                                                                                   |
| send.sentDateTime              | Send request initiation timestamp in UTC                                                 | 2019-06-02T17:17:15.575Z                                                                  |
| send.gatewayTid                | Unique TransactionID (TID) of the message send request                                   | 48ceebcb-8035-40d0-8f22-3608b915e2b6                                                      |
| send.response_interactive      | Captures if the interactive button in the message is tapped                              |                                                                                           |
| send.response_data             | The response data received from the user.                                                | [{"code":"1001","transid":"48ceebcb-8035-40d0-8f22-3608b915e2b6","description":"Queued"}] |

## Node Outcomes

The node exits via one of the node edges correspondings to the outcome of the node. 



| Node edge | Outcome name |
| --- | --- |
| Green | _ **onSuccess** - When waiting for the condition is set to \_none_ and upon successfully executing the send request  <br>_ **onSubmit** - When waiting for the condition is set to wait for \_Gateway Submit_ and upon successfully submitting the message within the set timeout value  <br>\_ **onDeliveryReportSuccess** - When wait for the condition is set to \_receive delivery report\* and upon successfully receiving the DR within the set timeout value |
| Yellow / Amber | \* **onTimeout** - When one of the waits for conditions is set and no acknowledgment is received within the timeout window set |
| Red | _ **onError** - When node execution failed. Any errors arising from passing invalid field values  <br>[List of response codes](https://developers.imiconnect.io/reference#section-twitter) corresponding to onError outcome  <br>_ **onPolicyFail** - When one of the policy checks failed.  <br>E.g. Send was attempted after the expiry time  <br>\_ **onDeliveryReportFail** - When wait for the condition is set to receive  \_delivery report\* or and when no corresponding DR is received within the timeout window set. |




### WhatsApp Business Platform Onboarding Guide for Developers

By now, you would have set yourself up on Webex Connect with your WhatsApp number. If not, click here to know how.

#### 1. Testing

After adding your number to Webex Connect, you can test it by sending a message to the number from your phone. You will be able to respond to it using the APIs or Flows.

To send proactive outbound messages, you will need to submit a template for approval. You can do this from Tools > Templates within your Webex Connect account.

#### 2. Receiving Messages & Webhooks

To receive incoming messages and events from your customers, you can configure outbound webhooks under integrations by choosing the WhatsApp Business API app from the entity dropdown.

Once you set up your webhook successfully, you will see that your messages start landing on your webhook endpoint.

#### 3. Messaging API

You can also test outbound messages through our API collection provided on [Postman](https://www.getpostman.com/collections/c7007a72dee5432c363c). 

You will need to update your service key in the API collection.

#### 4. Message Types

We support the following message types offered by WhatsApp today:

- Text
- Media
- Contact
- Location
- Templates
- Reply Buttons Message
- List Message

#### 5. Entry Points

WhatsApp supports free entry points that are user generated. You can send a link, like the one below, to your customers to get them to initiate a chat. 

<https://wa.me/15551234567?text=I'm%20interested%20in%20your%20car%20for%20sale>

This link can also be converted to a QR code or embedded as a button on a website or an email.