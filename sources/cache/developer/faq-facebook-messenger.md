# Facebook Messenger FAQs

Source: https://developers.webexconnect.io/reference/faq-facebook-messenger
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:52+00:00

## Using Facebook Messenger as a marketing channel

Facebook Messenger's messaging policy is best described as complex, the different types are best described below

a. Standard Messaging - With this businesses can only send messages within a sliding 24-hour window that resets every time the customer sends a message to the business. One message outside the window is allowed to follow up on the conversation, alternatively businesses can choose to send sponsored messages to customers outside the 24-hour window. To learn more, refer to [24-hour window](https://developers.facebook.com/docs/messenger-platform/policy/policy-overview#24hours_window).  
The interesting thing here is that the messages can be promotional, although within that 24-hour window. 

b. Subscription messaging (Beta) - Subscription messaging is limited to certain [use cases](https://developers.facebook.com/docs/messenger-platform/policy/policy-overview#eligible_use_cases). These messages can be sent anytime outside the 24-hour window but message content cannot be promotional or be an advertisement of any sort.

c. Sponsored messages - These messages are basically one more type of paid ad on Facebook which can be promotional or non-promotional. These messages should comply with Facebook's other advertisement policies. To get more details, refer to [Sponsored Messaging](https://developers.facebook.com/docs/messenger-platform/policy/policy-overview#sponsored_messaging).

Webex Connect by default gives you access to standard and subscription messaging via your Facebook pages linked in your Webex Connect account. But, we expect that businesses adhere to the guidelines for sending promotional content as described above.

## Can I broadcast messages on Facebook Messenger and/or Twitter DM?

While it is possible to broadcast messages to customers who have initiated a conversation with your business in the past on Facebook Messenger and Twitter, businesses are not suggested to use these channels for unsolicited bulk messaging/marketing. 

Please refer to the messaging guidelines for respective channels to get more information.

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [],
  "examples": {
    "codes": []
  }
}
```
