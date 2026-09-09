📘 API Endpoints & Postman Collection

> The Voice channel is supported via Voice API v1 and Send Message API v2. 
>
> The API endpoint for it is: [https://api.{YourRegion}.webexconnect.io/v1/voice/calls/{sessionId}]. 
>
> Please modify YourRegion in the URL as per your tenant’s region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
>
> Refer to [Postman Collection](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis) for trying Get Call Status Using Voice API v1.

> 📘 API Response and Error Codes
> 
> Voice API v1 is asynchronous. When you invoke the API, you receive an HTTP response confirming acceptance of your request. Further processing details are sent to your callback URL (notify URL) specified in the API request. For more information, see [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1).

## Request Body for Get Call Status API

```curl Get Call Status API
curl --location 'https://baseURL/v1/voice/calls/{sessionId}' \
--header 'Accept: application/json' \
--header 'Authorization: ServiceKey'
```

## Get Call Status Path Parameters

| Parameter | Type   | Mandatory | Description                                                                    |
| :-------- | :----- | :-------- | :----------------------------------------------------------------------------- |
| sessionId | string | yes       | Unique identifier for the call. Returned in the response body of Voice API v1. |

## Get Call Status Header Parameters

| Parameter     | Type   | Mandatory | Description                                                                               |
| :------------ | :----- | :-------- | :---------------------------------------------------------------------------------------- |
| Authorization | string | yes       | Authorization token (this can be either a JWT signed by a secret key or the service key). |

## Sample Response Body

```json Success
{
    "durationSeconds": 21,
    "statusTime": "2025-01-28T19:37:09.875+05:30",
    "offeredTime": "2025-01-28T19:36:49.739+05:30",
    "answeredTime": "2025-01-28T19:37:09.875+05:30",
    "status": "ANSWERED"
}
```
```Text 404 Not Found
<No Response Body>
```

### Response Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "durationSeconds",
    "0-1": "Integer",
    "0-2": "Duration of the call, in seconds.",
    "1-0": "statusTime",
    "1-1": "string",
    "1-2": "Timestamp of the call status, in UTC format.",
    "2-0": "offeredTime",
    "2-1": "string",
    "2-2": "Timestamp when the call was placed, in UTC format.",
    "3-0": "answeredTime",
    "3-1": "string",
    "3-2": "Timestamp when the call was answered, in UTC format.",
    "4-0": "status",
    "4-1": "string",
    "4-2": "**Status of the call. Possible values:**  \n**Answered**: The end customer answered the call.  \n**Dropped: ** The call was dropped due to a technical error.  \n**Rejected: ** The call was rejected (e.g., network failure, busy, or declined by the customer).  \n**Released: ** The call was ended by the platform.  \n**Disconnected: ** The end customer disconnected the call.  \n**Trombone Connected: ** Both the end customer and agent are connected.  \n**Trombone Released: ** The agent exited the call.  \n**Message Expired: ** The call request expired after the configured expiry time."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]