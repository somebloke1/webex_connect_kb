The Live Chat/In-App Messaging node enables you to send rich messages comprising images, videos, location, files, etc along with text, to the mobile and web apps that use <<prodname>>’s SDKs.  

It can be used to send automated responses to customers or to send one-off messages like exclusive offers, promo codes, terms, and conditions, etc. In combination with the Receive node, it can be used to build an end to end chatbot. There are options to wait for a delivery receipt or read receipt, before proceeding to the next node. These are helpful in cases where you only want to reach out to your customers, once they have received or read a particular message. 

Messages can have special attributes attached to it. For e.g. if there are two types of messages, namely promotional and non-promotional, you can use an [Extra Parameter](https://developers.imiconnect.io/reference/send-message) to categorize the messages into these two types.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/79d63d8-In-App.jpg",
        "In-App.jpg",
        "Screenshot of Live Chat/In-App Messaging Node."
      ],
      "align": "center",
      "caption": "Live Chat/In-App Messaging Node"
    }
  ]
}
[/block]


## Prerequisites

To be able to send In-App messages one must have:  

1. An **[App Asset](https://developers.imiconnect.io/docs/create-mobile-application-on-imiconnect-platform#create-a-mobile-app-asset-in-webex-connect)** created on <<prodname>>. 
2. **<<prodname>>’s SDK** integrated within your app, with appropriate App ID and Client Key, corresponding to the App asset, embedded within the app. 

> 📘 Note
> 
> The app should have at least one registered user, whose User ID, Push Token, or Customer ID can be used as a destination.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0f3fe03-In-App.jpg",
        "Live Chat In-App Messaging Node Window.png",
        "Screenshot of Live Chat/In-App Messaging Node Configuration Window."
      ],
      "align": "center",
      "sizing": "100",
      "border": true,
      "caption": "Screenshot of Live Chat/In-App Messaging Node Configuration Window."
    }
  ]
}
[/block]


## Node Configuration

All the parameters and input fields that you need to define within the node window are explained below. 

### Destination Type

There are different types of identifiers supported in <<prodname>> to target a user, namely: 

- **Customer-ID** is a master ID that is linked to all different channel-specific user IDs of a user within the customer profile. <<prodname>>'s customer profile is used to store multiple channel identifiers and customer communication preferences for various customers. It is useful in cross channel communication. For e.g: You want to send an exclusive promo code to a user’s app because of previous positive feedback that they have given via Messenger. If you have the customer profile configured with details of both Facebook Messenger PSID and user id linked with the same customer ID, you can use the Customer-ID of the user since it will remain constant across both the channels. 

- **User-ID** is the identifier specific to Push and In-App channels. This is generally created when a user registers on your mobile/web app. It is stored in the application profile. User-ID is used to orchestrate to and fro in-app communication, where you’ll directly get the required user-ID when a user initiates the chat. 

- **Topic** is used to broadcast messages that come under a particular section of interest. Any user who subscribes to a topic starts receiving messages published to that topic. 

> 📘 Note
> 
> The destination type **Topic** is not visible in the list, if the Topic Messaging option is disabled for your tenant.

- **Segment** is used when you want to target users that have subscribed to a specific combination of topics. You can create a segment containing the desired combination of topics and publish messages to that segment. 

> 📘 Note
> 
> The destination type **Segment** is not visible in the list, if the Segment Messaging option is disabled for your tenant.

### Destination

Corresponding to the selected destination type, you need to assign the value of the destination. It can be static or dynamic. For Eg: If the destination type is Customer-ID, the Destination can be kept dynamic by declaring it as $(customerID). 

### Message Configuration

This section contains all the elements required to orchestrate the message.

Message Type

- Message
- Form 
- Generic Template
- Message with Quick Replies

#### Message

The body of the message is defined in this field.

1. Select the required Destination Type from the list.
2. Enter the **Destination ID** or **Name** based on the Destination Type selected.
3. Select the Message Type as **Message**.
4. Enter the content for the **Message**.
5. Enter the variables for Template Elements.
6. Enter the **Thread ID**, **Notification Title**, and **Notification** Text.
7. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/85f4d9d-In-App_-_Message_Type_Message.jpg",
        "In-App - Message Type_Message.jpg",
        "creenshot of Live Chat/In-App Messaging Node Configuration Window."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Live Chat/In-App Messaging Node Configuration Window."
    }
  ]
}
[/block]


#### Form

1. Select the required **Destination Type** from the list.
2. Enter the **Destination ID** or **Name** based on the Destination Type selected.
3. Select the **Message Type** as Form.
4. Select the Content Type as:
   - **Static** to send a static form message that is configured in the Form Template. Select the required template from the **Form Template**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/93148d8-Form_Static.png",
        "Form Static.png",
        "Screenshot of the interface showing the configuration where Message Type is set to Form and Content Type is set to Static."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting Message Type to Form and Content Type to Static."
    }
  ]
}
[/block]


- Select the Content Type as **Dynamic** to send a form body dynamically as a variable in the run time. Enter the JSON variable in the **Form Body**. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b2d83d0-Form_Dynamic.png",
        "Form Dynamic.png",
        "Screenshot of the interface showing the configuration where Message Type is set to Form and Content Type is set to Dynamic."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting Message Type to Form and Content Type to Dynamic"
    }
  ]
}
[/block]


\*_Dynamic Content Type Sample Payload _ 

```json
{
  "reference": "feedback-form",
  "title": "Hi there, please fill the form below",
  "fields": [
    {
      "type": "text",
      "name": "full_name",
      "label": "Full name",
      "description": "Full name of the customer",
      "mandatory": true
    },
    {
      "type": "text",
      "Email": "full_Email",
      "label": "Email Address",
      "description": "Full Email of the customer",
      "mandatory": true
    },
    {
      "type": "dropdown",
      "name": "category",
      "label": "Category dropwon",
      "description": "Select categories applicable",
      "options": [
        "debit",
        "credit",
        "netbanking"
      ],
      "mandatory": true
    },
    {
      "type": "multiSelectDropdown",
      "name": "category",
      "label": "Multiselect dropdownCategory",
      "description": "MultiSelect categories applicable",
      "options": [
        "debit",
        "credit",
        "netbanking"
      ],
      "mandatory": true
    }
  ]
}
```

5. Enter the **Thread ID**.
6. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3f61c26-In-App-_Form.jpg",
        "In-App- Form.jpg",
        "Screenshot displaying to Enter Thread ID."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying to Enter Thread ID"
    }
  ]
}
[/block]


#### Message with Quick Replies - Static

1. Select the required Destination Type from the list.
2. Enter the Destination ID or Name based on the Destination Type selected.
3. Select the Message Type as Message with Quick Replies.
4. Enter the content for the Message.
5. Select the Content Type as Static.
6. Enter the Reference, Button Title, Button Identifier, Image URL, and Payload.
7. Enter the Thread ID, Notification Title, and Notification Text.
8. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5945fa5-In-App1.jpg",
        "In-App- Messages with Quick Replies.png",
        "Screenshot of Setting Message Type to Message with Quick Replies."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting Message Type to Message with Quick Replies."
    }
  ]
}
[/block]


#### Message with Quick Replies - Dynamic

1. Select the required Destination Type from the list.
2. Enter the Destination ID or Name based on the Destination Type selected.
3. Select the Message Type as Message with Quick Replies.
4. Enter the Message.
5. Select the Content Type as Dynamic.
6. Enter the variables for Quick Replies.
7. Enter the Thread ID, Notification Title, and Notification Text.
8. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4100184-In-App2.jpg",
        "In-App- Messages with Quick Replies-Dynamic.png",
        "Screenshot of Setting Content Type to Dynamic"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Setting Content Type to Dynamic."
    }
  ]
}
[/block]


#### Generic Template - Static

1. Select the required Destination Type from the list.
2. Enter the Destination ID or Name based on the Destination Type selected. 
3. Select the Message Type as Generic Template.
4. Enter the content for the Message.
5. To define static content in the node, select the Content Type as Static.
6. Provide the desired value for Reference, Title, Subtitle and  Image URL fields
7. Select the Button Type as either Postback or Web URL depending on your usecase.
8. Fill the Button Title, Button Identifier, and Payload fields
9. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2e98f68-In-App4.jpg",
        "Send Node- Generic Template.jpeg",
        "Screenshot of Setting Message Type to Generic Template."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting Message Type to Generic Template."
    }
  ]
}
[/block]


#### Generic Template - Dynamic

1. Select the required Destination Type from the list.
2. Enter the Destination ID or Name based on the Destination Type selected.
3. Select the Message Type as Generic Template
4. Enter the content for the Message.
5. Select the Content Type as Dynamic.
6. Enter the variables for Template Elements.
7. Enter the Thread ID, Notification Title, and Notification Text.
8. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5212b76-In-App3.jpg",
        "Live Chat Generic Template_Dynamic.jpg",
        "Screenshot of Setting Content Type to Dynamic."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting Content Type to Dynamic"
    }
  ]
}
[/block]


## Content Type

Content Type can be static or dynamic. Select Static if you want to enter static values. Select Dynamic, if you want to pass dynamic values as quick replies.

If you select Static, enter the following fields:

- Reference - This field can be used to pass some message tag  that can be used as reference.
- Title - Title of the template. This is only for Generic Template.
- Subtitle - Subtitle of the template. This is only for Generic Template.
- Image URL - URL of the image that is sent as an attachment in the template.
- Button Type - Select the button type as Web URL or Postback. This is only for Generic Template.
- Button Title - Title or label of the button.
- Button Identifier - Unique identification number corresponding to the button.
- Payload -  Enter the payload that must be returned when clicked on button
- Add Button - Click this to add another button. This is only for Generic Template
- Add Template Element - Click this to add another template element. This is only for Generic Template.

If you select Dynamic, provide the variable that contains the complete JSON objects for Template Elements.

### Add SMART LINK

SmartLink is a single URL, which contains multiple offers in it. For example, you can create a single URL for multiple network marketing channels including email, SMS, company website, and social. (content review required) 

### Thread-ID

Each message is always linked to a thread that has a unique Thread-ID. A thread can be imagined as a container that holds all the to and fro messages that are linked to it. It is usually used to fetch all the messages corresponding to one chat session and display it in the form of a conversation. 

### Notification Title

It's an optional parameter that is used if you want to send a notification for the particular in-app message, in-case the user is not using the app at the moment.

### Notification Text

Contains the text message which is sent to the user.

### Message Attachment

To send a rich message that contains attachments you need to declare the:

- Attachment Type: Select the required type (Image, Video, Documents, and Location) from the dropdown.
- Attachment URL: Enter the attachment URL. It is used for sending images with notifications.
- Attachment Size: Enter the attachment size in MB.

## OS Specific Parameters

Some properties of the message like notification sound, notification action, etc differ across OS. These can be configured in the below sections:

- [Android Extras](https://help.imiconnect.io/docs/push#section-android)
- [iOS Extras  ](https://help.imiconnect.io/docs/push#section-i-os)
- [Web Extras ](https://help.imiconnect.io/docs/push#section-web-push)

## Extra Parameters

Along with the message, you can send additional information like some user-specific property, or any custom parameter that is required to display the message in a certain fashion within the app. This information can be sent in the form of extra parameters.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7976c36-LiveChat.jpg",
        null,
        "Screenshot of Extra Parameters."
      ],
      "align": "center",
      "sizing": "650px",
      "border": true,
      "caption": "Screenshot of Extra Parameters."
    }
  ]
}
[/block]


### Correlation ID

You can assign a unique ID of your choice to each Live Chat/ In-App Messaging message. This ID is returned to the platform with the delivery report and can be used to identify the message.

### Callback Data

In case there is additional data to be sent along with the delivery reports to the URL, you must specify that here.

**Validations forCallback Data & Correlation ID**:

1. Callback Data, Correlation Id fields are optional for all the channels. Send node can be saved without providing these fields.
2. All characters, Alphabets, Numbers, and special characters are accepted.
3. Variables can be added.
4. Hard coded values are accepted.
5. On Platform side, there is no Max or Min length validation for these fields.

### Notify URL

You can choose to notify a URL with the delivery report for the Live Chat/ In-App Messaging message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.

**Validations for Notify URL**:

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

## Advance Options

### Wait For

The life-cycle of Live Chat/In-App Messaging consists of three stages. You can wait for a callback at any of the stages before proceeding further in the flow by selecting any one of the following:

1. Gateway Submit: The first stage where the configured message along with the destination is submitted to the gateway for delivery.
2. Delivery Report: The second stage, in which the message is delivered to the targeted device. 
3. Read Report: The last stage is when the target user actually reads the message.
4. Clicked (Generic Template only): Flow will wait for the template to be clicked. Once the template is clicked the flow will continue.

### Expiry

Time in seconds or UTC, after which node session will timeout and the flow would proceed to the next node.  

## Output Variables

You can see the data that this node generates as output variables.

[block:parameters]
{
  "data": {
    "h-0": "Output Variable",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "send.sentDateTime",
    "0-1": "The date and time on which the message is sent.",
    "0-2": "2019-06-02T17:17:15.575Z",
    "1-0": "send.gatewayTid",
    "1-1": "The system generated transaction Id received from gateway.",
    "1-2": "[{\"code\":\"1001\",\"transid\":\"48ceebcb-8035-40d0-8f22-3608b915e2b6\",\"description\":\"Queued\"}]",
    "2-0": "send.deliveryStatusDescription",
    "2-1": "Status of the delivery.",
    "2-2": "Submitted/Delivered/Read.",
    "3-0": "send.deliveryStatusCode",
    "3-1": "The status code of the delivery message.",
    "3-2": "101",
    "4-0": "send.response_data",
    "4-1": "The response data received from the user.",
    "4-2": "[{\"code\":\"1001\",\"transid\":\"48ceebcb-8035-40d0-8f22-3608b915e2b6\",\"description\":\"Queued\"}]",
    "5-0": "send.response_interactive  \n  \nThe interactive response data.",
    "5-1": "Captures if the interactive button in the message is tapped.",
    "5-2": ""
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Node Outcomes

- onsuccess: Node executed successfully. 
- onsubmit: Submitted to a gateway. 
- ondrsuccess: Received DR for the transaction. 
- Onread: Received RR for the transaction. 
- onpolicyfail: the flow exits through this node outcome when the expiry condition cannot be met.
- ondrfail: Failed to receive DR.
- onerror: the flow exits through this node outcome when there is an error.
- Ontimeout: Session timeout.