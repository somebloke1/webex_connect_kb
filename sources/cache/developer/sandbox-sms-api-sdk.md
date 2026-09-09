# SMS APIs & SDKs

Source: https://developers.webexconnect.io/reference/sandbox-sms-api-sdk
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:39+00:00

> 📘 Note
> 
> Please check [Countries supported in Sandbox](https://developers.imiconnect.io/reference/sms-and-voice-support-in-sandbox)  for the complete list of supported countries.

## Overview

Webex Connect sandbox mode offer the following APIs for SMS channel:

- Send SMS API for sending an SMS message
- Retrieve SMS Status API to retrieve the delivery status of a message sent using Webex Connect 

This apart we offer a NodeJS SDK for sending SMS messages. You can access the [SDK](https://www.npmjs.com/package/connect-sdk-node#sending-a-sms-message) on npmjs portal.

## Authentication

Webex Connect sandbox mode currently supports key based authentication using Service Key. JWT Authentication that's supported as part of the production accounts isn't available in sandbox mode at the moment.

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
