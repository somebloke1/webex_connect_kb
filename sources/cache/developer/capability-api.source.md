> 📘 Please Note
> 
> The RCS channel is supported via <<prodname>> RCS Capability Lookup API v1.
> 
> The API endpoint for it is: [https://{YourRegion}.webexconnect.io/v1/rcs/capabilities].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying various types of RCS messages supported by <<prodname>>.

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

[block:parameters]
{
  "data": {
    "h-0": "Parameters",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "msisdn",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "Phone number, i.e., msisdn to which the RCS messages have to be sent in E.164 format e.g., +44XXXXXXXXXX  \n  \n_Note: If the \"+E.164\" format is enabled for your tenant, all the numbers in the 'to' field should follow the \"+E.164\" format.  \nThis format displays the number with a '+' followed by the country code and the phone number.  \n+E.164 format does not apply to the numbers in the 'from' field._",
    "1-0": "appId",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "Unique ID of RCS asset that is set up in <<prodname>>platform. ",
    "2-0": "forceRefresh",
    "2-1": "string",
    "2-2": "No",
    "2-3": "if true, capability look up is repeated even if its available in memory."
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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