<<prodname>>communications APIs allow you to send proactive outbound messages and calls, and/or respond to incoming customer messages and/or calls across various channels supported by the platform.<be>

This includes:

- [SMS](https://developers.webexconnect.io/reference/sms-apis-new-set)
- [Voice](https://developers.webexconnect.io/reference/call)
- [RCS Business Messaging](https://developers.webexconnect.io/reference/rcs)
- [MMS](https://developers.webexconnect.io/reference/mms-api)
- [Email](https://developers.webexconnect.io/reference/email-api)
- [Push Notifications (Android, iOS, Web)](https://developers.webexconnect.io/reference/push)
- [In-App Messaging and Live Chat (Real-Time App Messaging)](https://developers.webexconnect.io/reference/in-app-live-chat)
- [Apple Messages for Business](https://developers.webexconnect.io/reference/apple-messages-for-business)
- [Facebook Messenger ](https://developers.webexconnect.io/reference/facebook)
- [WhatsApp](https://developers.webexconnect.io/reference/whatsapp-api-docs)

## Getting Started

Refer to our [Getting Started](https://developers.webexconnect.io/reference/apioverview#getting-started) guide for all the Webex Connect APIs to familiarise yourselves with various aspects such as API Endpoints, Authentication, Response and Error Codes, and more.

## Batching Requests

You can send a message to a single recipient or to multiple recipients by making a single API call. If you want to send messages to multiple recipients at once you would need to provide the list of recipients in the destination array while making the API call. For example, a bank can send a personalized greeting message to its customers using the delivery channel as SMS. Using batch message API requests, you can send messages to up to 1000 destinations (subject to your TPS limits). E.g., if your messaging API TPS configuration is 10 you can send messages to up to 10 destinations at once.

Additionally, you can send batch messages on multiple channels with a single API request.

> 📘 Shortened URLs
> 
> Support for shortened URLs and link tracking in Messaging APIs v1 and v2 has been extended to all messaging channels, excluding AMB, Voice, Instagram, Push, and the Sandbox environment. Furthermore, read receipt functionality for clicked notifications is now offered on Messaging API v2 channels.
> 
> Please get in touch with your account manager to enable the Shortened URLs feature on your tenant.
> 
> To configure this feature, please refer to points 2 and 3 from [Prerequisites](https://help.webexconnect.io/docs/link-shortener#pre-requisites) section within the [ Shortened URLs ](https://help.webexconnect.io/docs/link-shortener) page.