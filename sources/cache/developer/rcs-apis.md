# RCS APIs

Source: https://developers.webexconnect.io/reference/rcs-apis
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:41+00:00

Webex Connect makes it easy for you to send  RCS messages programmatically by offering a rich set of Restful APIs. 

Rich Communication Services, or RCS, is a leap forward for the most commonly used app on mobile phones—the SMS inbox. The power of RCS lies in the features it brings to native mobile messaging. RCS harnesses advanced device capabilities and enhanced UI elements to provide an app-like experience to traditional text messaging.

## Pre-requisite

- Set up RCS channel assets. For more information, refer to the [configure-rcs-application](https://help.webexconnect.io/docs/rcs#configure-rcs-application-on-webex-connect) page.

## APIs for Sending RCS Messages:

The following APIs are available for RCS using Webex Connect:

- [RCS Capability Lookup API ](https://developers.webexconnect.io/reference/capability-api) - This API is used to check if a user's device is RCS-enabled and capable of communicating with an RCS chatbot.
- [RCS API ](https://developers.webexconnect.io/reference/rcs-api)- This API is used to send RCS messages using Send Message API v2 on the Webex Connect platform.  
  RCS supports the following message types: 
  1. [Text](https://developers.webexconnect.io/reference/rcs-api#request-body-to-send-rcs-text-sample-using-send-message-api-v2---samples)
  2. [File / Media](https://developers.webexconnect.io/reference/rcs-api#rcs-file)
  3. [Standalone card (Rich card)](https://developers.webexconnect.io/reference/rcs-api#rcs-rich-card)
  4. [Carousel](https://developers.webexconnect.io/reference/rcs-api#rcs-carousel)
  5. [Typing](https://developers.webexconnect.io/reference/rcs-api#rcs-typing-event)
  6. [Read](https://developers.webexconnect.io/reference/rcs-api#rcs-read-event)

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
