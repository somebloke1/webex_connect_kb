# RCS Capability Lookup API

Source: https://developers.webexconnect.io/reference/capability-api
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:41+00:00

> 📘 Please Note
> 
> The RCS channel is supported via Webex Connect RCS Capability Lookup API v1.
> 
> The API endpoint for it is: [https://{YourRegion}.webexconnect.io/v1/rcs/capabilities].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying various types of RCS messages supported by Webex Connect.

## Request Body to Verify RCS device capability Using RCS Capability Lookup API

```json RCS Capability
{
    "msisdn": [
        "{{msisdn}}" //Mandatory. E.164 format required/recommended.
    ],
    "appId": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "forceRefresh": true // Optional, if true, capability look up is repeated even if its available in memory. 
}
```



| Parameters | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msisdn | string | yes | Phone number, i.e., msisdn to which the RCS messages have to be sent in E.164 format e.g., +44XXXXXXXXXX  <br>  <br>_Note: If the "+E.164" format is enabled for your tenant, all the numbers in the 'to' field should follow the "+E.164" format.  <br>This format displays the number with a '+' followed by the country code and the phone number.  <br>+E.164 format does not apply to the numbers in the 'from' field._ |
| appId | string | yes | Unique ID of RCS asset that is set up in Webex Connectplatform.  |
| forceRefresh | string | No | if true, capability look up is repeated even if its available in memory. |




## Sample Response Body

```json 200 Success Response
[
    {
        "resolveTimestamp": "2024-11-06T16:15:46.799+05:30",
        "capabilities": [
            "ACTION_CREATE_CALENDAR_EVENT",
            "ACTION_DIAL",
            "ACTION_OPEN_URL",
            "ACTION_SHARE_LOCATION",
            "ACTION_VIEW_LOCATION",
            "CHAT",
            "FILE_TRANSFER",
            "PAYMENTS_V1",
            "REVOCATION",
            "RICHCARD_CAROUSEL",
            "RICHCARD_STANDALONE"
        ],
        "carrierCode": 106,
        "serviceProvider": "GOOGLE",
        "id": "pyf65kz2fXXXXXrchgqkosyt3m",
        "msisdn": "+91987XXXX123",
        "enabled": true,
        "timestamp": "2024-11-06T16:15:46.799+05:30"
    }
]
```
```json 400 Bad Request
Status code- 400 - Bad Request

[
    {
        "code": "7104",
        "message": "Invalid app ID"
    }
]
```

| Response Parameter           | Type    | Description                                                                                                           |
| :--------------------------- | :------ | :-------------------------------------------------------------------------------------------------------------------- |
| resolveTimestamp             | string  | The timestamp of the response received.                                                                               |
| capabilities                 | string  | An array listing the user's device's capabilities.                                                                    |
| ACTION_CREATE_CALENDAR_EVENT | string  | Action to create a calendar event.                                                                                    |
| ACTION_DIAL                  | string  | Action to dial a number.                                                                                              |
| ACTION_OPEN_URL              | string  | Action to open a URL in a browser.                                                                                    |
| ACTION_SHARE_LOCATION        | string  | Action to share a location.                                                                                           |
| ACTION_VIEW_LOCATION         | string  | Action to view a location in a map app.                                                                               |
| CHAT                         | string  |                                                                                                                       |
| FILE_TRANSFER                | string  |                                                                                                                       |
| REVOCATION                   | string  | If the user supports revocation, the agent can revoke a message it sent before the RBM platform delivers the message. |
| RICHCARD_CAROUSEL            | string  | Carousel of rich cards.                                                                                               |
| RICHCARD_STANDALONE          | string  | Standalone rich cards.                                                                                                |
| carrierCode                  | int     | Carrier code of the msisdns being requested.                                                                          |
| serviceProvider              | string  | Messaging service provider.                                                                                           |
| id                           | string  | Capability request id.                                                                                                |
| msisdn                       | string  | MSISDN in "E164" format.The device's phone number, to which the capability request was sent.                          |
| enabled                      | boolean | Indicates If RCS is enabled for the device.                                                                           |
| timestamp                    | string  | The timestamp of the capability request sent.                                                                         |

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
