# Get Call Recordings Using Voice API v1

Source: https://developers.webexconnect.io/reference/voice-only-api-v1-get-call-recordings-api
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:44+00:00

> 📘 API Endpoints & Postman Collection
> 
> The Voice channel is supported via Voice API v1 and Send Message API v2. 
> 
> The API endpoint for it is: [https://api.{YourRegion}.webexconnect.io/v1/voice/calls/{sessionId}/recordings]. 
> 
> Please modify YourRegion in the URL as per your tenant’s region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [Postman Collection](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis) for trying Get Call Recordings Using Voice API v1.

> 📘 API Response and Error Codes
> 
> Voice API v1 is asynchronous. You receive an HTTP response confirming acceptance of your request immediately after invoking the API. Further processing details are sent to your callback URL. For more information, see [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1).

## Request Body for Get Call Recordings API

```curl Get Call Recordings API
curl --location 'https://baseURL/v1/voice/calls/{sessionId}/recordings' \
--header 'Accept: application/json' \
--header 'Authorization: ServiceKey'
```

## Get Call Recordings Path Parameters

| Parameter | Type   | Mandatory | Description                                                              |
| :-------- | :----- | :-------- | :----------------------------------------------------------------------- |
| sessionId | string | yes       | Unique identifier for the call. Returned in the response body of events. |

## Get Call Recordings Header Parameters

| Parameter     | Type   | Mandatory | Description                                                                               |
| :------------ | :----- | :-------- | :---------------------------------------------------------------------------------------- |
| Authorization | string | yes       | Authorization token (this can be either a JWT signed by a secret key or the service key). |

### Sample Response Body

```json Success
{
    "recordings": [
        {
            "durationSeconds": 4,
            "url": "https://anydomain.imiconnect.co/voice-recordings/menu_1738073208_900201219666667_7.wav"
        },
        {
            "durationSeconds": 20,
            "url": "https://anydomain.imiconnect.co/voice-recordings/call_1738073208_900201219666667_4.wav"
        }
    ],
    "sessionId": "0c6f0ad0-7340-XXXX-XXXX-300ac310dee0"
}
```
```Text 404 Not Found
<No Sample Body>
```

### Response Parameters

| Parameter       | Type       | Description                                                                    |
| :-------------- | :--------- | :----------------------------------------------------------------------------- |
| recordings      | JSON Array | Array of objects, each containing 'durationSeconds' and 'url' for a recording. |
| durationSeconds | integer    | Duration of the recording in seconds.                                          |
| url             | string     | URL to the recording file for the session.                                     |
| sessionId       | string     | Unique identifier for the call associated with the recording.                  |

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
