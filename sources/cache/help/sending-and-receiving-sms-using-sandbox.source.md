By using the <<prodname>> Sandbox you can send and receive SMS from the interface, APIs, SDKs and advanced flows. In the Sandbox mode, we support one-way communication (send SMS) for more than 70 countries and two-way communication (send and receive SMS) for 18 countries. By using our pre-defined code snippets for requests and responses, you can seamlessly integrate into your application(s).

> 📘 SMS Support in Sandbox
> 
> - Refer to [a list of countries](https://developers.imiconnect.io/reference/sms-and-voice-support-in-sandbox) that you can send and/or receive SMS messages in using <<prodname>> sandbox mode.
> - Please note you can send a maximum of 10000 SMS or WhatsApp API requests (combined limit) over the lifetime of <<prodname>> Sandbox usage.

## Sandbox Home UI

<<prodname>> sandbox allows you to send and/or receive SMS messages using following three options:

- Home Screen
- SMS API
- Flow Builder 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0952a13-2.jpg",
        "SMS.jpg",
        "Screenshot of the Sandbox Home screen displaying SMS sending feature"
      ],
      "align": "center",
      "border": true,
      "caption": "Sending SMS from Sandbox Home Screen"
    }
  ]
}
[/block]


### Sending SMS from Sandbox Home screen

As shown above, Sandbox Home screen contains explorer interface to help you send test messages to your registered phone number(s) using pre-provisioned phone numbers/sender IDs simply by providing sample message text and clicking send. By default the API credentials associated with pre-provisioned 'My First Service' are used to send these messages, and the sample code is visible on the right side of the screen. Additionally, the sample API response once you have sent the messages shows-up in the 'Sample API Response' section on the right side.

Here's a brief description of various parameters / fields that are used for sending the message. These values need to be provided when you use <<prodname>> sandbox SMS API (please note that <<prodname>> sandbox mode offers a separate endpoint for SMS messaging) to send outbound messages:

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "0-0": "Service Key",
    "0-1": "The unique service key associated with the service selected under the Service Name dropdown. This key is used for authenticating the API request to send the SMS message.",
    "1-0": "From Number",
    "1-1": "The Phone Number or the Sender ID used for sending the message from <<prodname>>. This value is automatically populated in Sandbox mode and cannot be changed.  \n  \nDepending on the country you are sending messaging to, this will either be a local phone number, or an Alpha Sender ID.",
    "2-0": "To Number",
    "2-1": "Phone number of the message recipient.  \n  \nFrom the drop-down list, select the number where you want your message to be sent. The sandbox limits you to only sending messages to your verified phone number(s). You can register up to 5 phone numbers (all belonging to the same country) for sending and receiving test messages.",
    "3-0": "Message Type",
    "3-1": "Select Text or Unicode. Select Unicode if you want to include special characters or emojis in your message.",
    "4-0": "Message",
    "4-1": "Type the message you want to deliver to the recipient."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


As you make changes in the above field, the API code snippet visible on the right side of the screen is automatically updated to help you understand how the <<prodname>> SMS API works.

### Receiving SMS from Sandbox Home screen

Under the SMS Receive tab you can test your incoming messages. To test your incoming messages, click the SMS Receive tab. 

Receiving SMS is only supported in countries for which the sandbox supports two-way messaging. Check for [a list of countries](https://developers.imiconnect.io/reference/sms-and-voice-support-in-sandbox) that support this function.

To test a message, send an SMS message to the pre-provisioned phone number from one of your registered test numbers. The phone number is shown in the Number to message field. The most recently received message will be displayed in the Recently Received SMS field. The payload will be shown on the right-side SMS Receive Payload panel once you send the message.  

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f973ad5-Receive_SMS.jpeg",
        "Receive SMS.jpg",
        "Screenshot of the Sandbox Home screen displaying SMS receiving feature"
      ],
      "align": "center",
      "border": true,
      "caption": "Receiving SMS from Sandbox Home Screen"
    }
  ]
}
[/block]


> 📘 Note
> 
> You will see the Receive SMS section only if your country supports two-way communication.

## SMS API

In addition to the Sandbox Home user interface, you can embed SMS messaging capabilities within your messaging apps using <<prodname>> APIs and Outbound Webhooks.

- Refer <<prodname>> Sandbox API reference for [SMS messaging](https://developers.imiconnect.io/reference/sms-api-sdk)
- Refer [Outbound Webhook](https://developers.imiconnect.io/reference/sms-1) configuration details for handling incoming messages

## Visual Flow Builder

If you want to configure and deploy two-way customer interactions or journeys in a serverless environment you can use <<prodname>> flow builder. See [Creating a Flow on Webex Connect](https://help.imiconnect.io/docs/create-a-new-flow) for information about creating, managing, viewing, and deleting flows.

Please note that while <<prodname>> visual flow builder has more than 50+ nodes available in the full platform license mode, the access is limited to ~15 nodes in the sandbox mode. Please refer FAQs for more details.

> 📘 
> 
> <<prodname>> offers a feature called 'Rules' to automate simple user cases like sending an auto-response when a given keyword is received in an incoming message, etc. However, that option is not available in the Sandbox mode.