Outbound Webhooks can be used to forward the following events on <<prodname>> to your web application:

- [Delivery Receipts](https://developers.imiconnect.io/reference/outbound-webhooks#delivery-receipts)
- [Incoming Messages & Events](https://developers.imiconnect.io/reference/outbound-webhooks#incoming-messages--events)

> ❗️ URL Endpoint Notifications
> 
> - We only support HTTPs URLs. All URLs must return a 200 HTTP Response to a HEAD request to be successfully saved on the UI. All notifications will be delivered as POST requests and expect a 200 HTTP Response.
> - In case <<prodname>> is not able to send a notification because of an unreachable URL, it will retry sending notifications three times each, after 60 seconds. The maximum request timeout for each notification is 10 seconds. The HTTP Responses for which retries are not performed are - 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 402, 404, 405, 406, 407, 408, 409, 410, 411, 414, 415, 416, 418, 505.

> 📘 Configuring Outbound Webhooks
> 
> For more information on how to configure Outbound Webhooks, refer to [Outbound Webhooks](https://help.imiconnect.io/docs/outbound-webhooks)

## Enable Hub Secret (Optional)

The value of the hub secret is used as the key to creating a signature of the notification data, and is sent along with the notification, which can then be verified by the receiving server. The signature is the hexadecimal (40-byte) representation of an SHA-256 or SHA-512 signature computed using the HMAC algorithm as defined in RFC2104.

When enabled, you will receive an additional header called x-hub-signature.

> 📘 Secret Key in the x-hub-signature
> 
> The consumer (client) of the Outbound Webhook provides the Secret Key in the x-hub-signature of the Outbound Webhook. This allows the client to calculate the signature on the client-side and match the signature for the incoming payload in the Outbound webhook.

## Delivery Receipts

To receive delivery receipts for your messages:

1. Select a **Service** under entity
2. Select the **Outbound Channel** for which you want to receive the delivery receipts. These messages must have sent from a Messaging API authenticated with the selected service key or through flows or rules inside the selected service

- Select the delivery receipt type for the selected channel - Different channels have different capabilities in terms of the kind of the receipts that are available

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/af28534-ee771e6000aa13a1a1667df739cac933.png",
        "ee771e6000aa13a1a1667df739cac933.png",
        "Screenshot of Delivery Receipt Webhook - Entity is One-way intelligent service and channel is SMS"
      ],
      "align": "center",
      "border": true,
      "caption": "Example Delivery Receipt Webhook - Entity is One-way intelligent service and channel is SMS"
    }
  ]
}
[/block]


## Incoming Messages & Events

To receive incoming messages or events sent to your numbers or your apps by your customers -

1. Select a **Number** or an **App** under entity
2. Select the **Incoming messages/events option** for the corresponding app/number

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cacdc28-fac5959731d4f86cdf4b6a40a100c8fc.png",
        "fac5959731d4f86cdf4b6a40a100c8fc.png",
        "Screenshot of Example Inbound Message & Event Webhook - Entity is JS SDK App."
      ],
      "align": "center",
      "border": true,
      "caption": "Example Inbound Message & Event Webhook - Entity is JS SDK App"
    }
  ]
}
[/block]


> 📘 Note
> 
> We have introduced "x-wx-gtrid" in the headers.