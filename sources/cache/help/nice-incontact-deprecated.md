# Nice inContact - Deprecated

Source: https://help.webexconnect.io/docs/nice-incontact-deprecated
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:11+00:00

> ❗️ Deprecation Alert
> 
> Please note that this integration has been deprecated and is no longer available.

The integration enables inContact vendors to support chat with their end customers on multiple channels (Example: Facebook Messenger, In-app Messaging) along with their own primary channel like web chat.

Chat agents using InContact integrated with Webex Connect use the same interface as that of native CCSP, but additionally will be able to receive messages from multiple channels using the same interface. When the chat agent reply, the message is sent back to the customer on the same channel from which the message was received.

The channels supported by InContact  are

- SMS
- Messenger
- In-App

For example, if an end customer interacts through the Facebook Messenger channel, the message is received by Webex Connect and is routed to an inContact agent. When the agent responds to the message, the message is received by Webex Connect and then forwarded to the end customer's Facebook Messenger account.

When the chat is closed after successful interaction, Webex Connect can trigger events and rules that are configured to collect additional information that maybe of interest to the businesses such as customer feedback on the recent conversation.

| Field                          | Description                                                                                                                        |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| NAME                           | Provide a name for the inContact integration that you are configuring.                                                             |
| **InContact App details**      | Details to integrate incontact app with Webex Connect. These details are share by inContact when you get registered with inContact. |
| APP NAME                       | Name of vendor application alloted for vender for inContact integration.                                                           |
| INCONTACT BUSINESS UNIT NUMBER | Unique id for each vendor.                                                                                                         |
| VENDOR NAME                    | Name of the vendor.                                                                                                                |
| API VERSION                    | inContact API version we are interacting                                                                                           |
| **Admin Details**              | Administration details to log in to the Admin portal and to access API.                                                            |
| ADMIN USERNAME                 | Username allocated by inContact to login into admin portal and to access API                                                       |
| PASSWORD                       | Password to login into the inContact admin portal and to access API.                                                               |

_Note: This integration is available only in the cloud version of Webex Connect._