By using the <<prodname>> Sandbox you can send and receive WhatsApp messages from the interface, APIs, SDKs and advanced flows. We support two-way communications across all countries supported by WhatsApp. By using our pre-defined code snippets for inbound and outbound requests, you can seamlessly integrate WhatsApp messaging into your application(s).

> 📘 WhatsApp Support in Sandbox
> 
> Please note you can send a maximum of 10000 WhatsApp or SMS messages (combined limit) over the lifetime of <<prodname>> Sandbox usage.

## Sandbox Home UI

<<prodname>> sandbox allows you to send and/or receive WhatsApp messages using following three options:

- Home Screen
- WhatsApp API
- Flow Builder 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e6cbb339991cfdda7f0e41f79cc9a188f3d5bafc33900554607eed2473ed0ad4-Screenshot_2024-10-17_at_4.24.14_PM.png",
        "",
        "Screenshot of the Sandbox Home screen displaying WhatsApp sending feature"
      ],
      "align": "center",
      "caption": "Sending WhatsApp from Sandbox Home Screen"
    }
  ]
}
[/block]


## Sending WhatsApp from Sandbox Home screen

As shown above, Sandbox Home screen contains explorer interface to help you send test messages to your registered phone number(s) using the pre-provisioned phone numbers/sender IDs simply by providing sample message text. By default the API credentials associated with pre-provisioned 'My First Service' are used to send these messages, and the sample code is visible on the right side of the screen. Additionally, the sample API response once you have sent the messages shows-up in the 'WhatsApp API Response' section on the right side.

Here's a brief description of various parameters / fields that are used for sending the WhatsApp message. These values need to be provided when you use <<prodname>>  sandbox WhatsApp API (please note that <<prodname>>  sandbox mode offers a separate endpoint for WhatsApp messaging) to send outbound messages:

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "0-0": "Service Key",
    "0-1": "The unique service key associated with the service selected under the Service Name dropdown. This key is used for authenticating the API request to send the WhatsApp message.",
    "1-0": "From Number",
    "1-1": "The Phone Number or the Sender ID used for sending the message from <<prodname>>. This value is automatically populated in Sandbox mode and cannot be changed.  \n  \nDepending on the country you are sending a WhatsApp message to, this will either be a local phone number, or an Alpha Sender ID.",
    "2-0": "To Number",
    "2-1": "Phone number of the message recipient.  \n  \nFrom the drop-down list, select the number where you want your message to be sent. The sandbox limits you to only sending messages to your verified phone number(s). You can register up to 5 phone numbers (all belonging to the same country) for sending and receiving test messages.",
    "3-0": "Message Type",
    "3-1": "Select Text Template, Media Template, Interactive Template or Free-Form Message.",
    "4-0": "Free-Form Message",
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