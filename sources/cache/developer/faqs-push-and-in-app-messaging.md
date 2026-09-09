# Push, Live Chat & In-App Messaging FAQs

Source: https://developers.webexconnect.io/reference/faqs-push-and-in-app-messaging
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:52+00:00

## Can I get notified when a mobile app user revokes push notification permission?

No, this is not possible because there is no event that is raised by the operating system to notify our SDKs when a user revokes the push notification permission. When you try to send a push notification to a user who has revoked push notification permissions, it will result in an 'UNREGISTERED' error from FCM. However, this error code can be returned in other scenarios as well such as when a user uninstalls the app. For more information, please refer to [ErrorCode](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode).

> 📘 Unregistered Error
> 
> Unregistered Error is specific to FCM. This is not received if you use APNS as the underlying push service. Hence if you use APNS as the underlying push service, we would not be able to identify whether a user has uninstalled your app from their device.

## Can I get notified when a customer uninstalls our mobile app?

No, this is not possible because there is no event that is raised by the operating system to notify our platform when a user uninstalls the mobile app. When you try to send a push notification to such a user it will result in an 'UNREGISTERED' error from FCM. 

## What are the supported media attachment types in push notifications?

Here's is a list of media attachment types supported by Android and iOS for push notifications:

- Android: Image
- iOS: Audio, Video, and Image 

One notification can have only one media attachment.

## Are there any size limits for push, live chat, and in-app message payloads?

- The push notification payload limit is 4KB per message across Android, iOS, and web
- The size limit for live chat and in-app messages is 4KB

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
