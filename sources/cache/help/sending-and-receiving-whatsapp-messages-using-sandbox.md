# Sending and Receiving WhatsApp Messages using Sandbox

Source: https://help.webexconnect.io/docs/sending-and-receiving-whatsapp-messages-using-sandbox
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:48+00:00

By using the Webex Connect Sandbox you can send and receive WhatsApp messages from the interface, APIs, SDKs and advanced flows. We support two-way communications across all countries supported by WhatsApp. By using our pre-defined code snippets for inbound and outbound requests, you can seamlessly integrate WhatsApp messaging into your application(s).

> 📘 WhatsApp Support in Sandbox
> 
> Please note you can send a maximum of 10000 WhatsApp or SMS messages (combined limit) over the lifetime of Webex Connect Sandbox usage.

## Sandbox Home UI

Webex Connect sandbox allows you to send and/or receive WhatsApp messages using following three options:

- Home Screen
- WhatsApp API
- Flow Builder 



![Sending WhatsApp from Sandbox Home Screen](https://files.readme.io/e6cbb339991cfdda7f0e41f79cc9a188f3d5bafc33900554607eed2473ed0ad4-Screenshot_2024-10-17_at_4.24.14_PM.png)




## Sending WhatsApp from Sandbox Home screen

As shown above, Sandbox Home screen contains explorer interface to help you send test messages to your registered phone number(s) using the pre-provisioned phone numbers/sender IDs simply by providing sample message text. By default the API credentials associated with pre-provisioned 'My First Service' are used to send these messages, and the sample code is visible on the right side of the screen. Additionally, the sample API response once you have sent the messages shows-up in the 'WhatsApp API Response' section on the right side.

Here's a brief description of various parameters / fields that are used for sending the WhatsApp message. These values need to be provided when you use Webex Connect  sandbox WhatsApp API (please note that Webex Connect  sandbox mode offers a separate endpoint for WhatsApp messaging) to send outbound messages:



| Field Name | Description |
| --- | --- |
| Service Key | The unique service key associated with the service selected under the Service Name dropdown. This key is used for authenticating the API request to send the WhatsApp message. |
| From Number | The Phone Number or the Sender ID used for sending the message from Webex Connect. This value is automatically populated in Sandbox mode and cannot be changed.  <br>  <br>Depending on the country you are sending a WhatsApp message to, this will either be a local phone number, or an Alpha Sender ID. |
| To Number | Phone number of the message recipient.  <br>  <br>From the drop-down list, select the number where you want your message to be sent. The sandbox limits you to only sending messages to your verified phone number(s). You can register up to 5 phone numbers (all belonging to the same country) for sending and receiving test messages. |
| Message Type | Select Text Template, Media Template, Interactive Template or Free-Form Message. |
| Free-Form Message | Type the message you want to deliver to the recipient. |

