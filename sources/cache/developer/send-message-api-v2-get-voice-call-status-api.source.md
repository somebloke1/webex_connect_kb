> 📘 API Endpoint & Postman Collection
> 
> Voice channel is supported via Voice API and Send Message API v2. 
> 
> API endpoint for it is: [https://{YourRegion}.webexconnect.io/v2/messages/{messageId}].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [Postman Collection](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis) for trying Get Voice Call Status Using Send Message API v2.

> 📘 API Response and Error Codes
> 
> Send Message API v2 is asynchronous. You receive an HTTP response confirming acceptance of your request, while additional processing details are sent to your notify URL. For more information, see [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1).

## Request Body for Get Voice Call Status API

```curl Get Voice Call Status
curl --location 'https://baseURL/v2/messages/{MessageId}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'key: ServiceKey'
```

## Get Voice Call Status Path Parameters

| Parameter | Type   | Mandatory | Description                                                                                          |
| :-------- | :----- | :-------- | :--------------------------------------------------------------------------------------------------- |
| MessageId | string | yes       | Unique identifier for the message transaction. Returned in the response body of Send Message API v2. |

## Get Voice Call Status Header Parameters

| Parameter | Type   | Mandatory | Description                                                                               |
| :-------- | :----- | :-------- | :---------------------------------------------------------------------------------------- |
| key       | string | yes       | Authorization token for the request. Use a JWT signed with a secret key or a service key. |

## Sample Response Body

```json 200
{
    "callDuration": 4,
    "clientId": 3678,
    "toType": "msisdn",
    "requestTimestamp": "2024-12-03T17:44:33.151+05:30",
    "groupId": 4123,
    "answeredAt": "2024-12-03T17:44:50.842+05:30",
    "channel": "voice",
    "messageId": "c6f14a41-3358-XXXX-XXXX-1141ecfXXXXX",
    "requestedReceipts": [],
    "priority": "1",
    "version": "2.0",
    "content": {
        "ttsProcessor": "Azure",
        "voice": "Apollo",
        "gender": "Male",
        "fileSize": 0,
        "language": "en-IN",
        "text": "/logdata/apps/dvp/callflows/Play_media.txt",
        "type": "TTS",
        "region": "English (India)",
        "voiceType": "NEURAL"
    },
    "endedAt": "2024-12-03T17:44:54.512+05:30",
    "teamId": 4321,
    "callbackData": "test_callback_data",
    "notifyUrl": "https://01j7x8v422z889w32gkbt8vg5x00-097f245de45d94eaa1b9.requestinspector.com",
    "from": "+16403xxxxxx",
    "correlationId": "na1b2b1i1",
    "to": "+12985XXXXXX",
    "direction": "outbound",
    "status": "ANSWERED"
}
```

## Response Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "callDuration",
    "0-1": "Duration of the call in seconds.",
    "1-0": "clientId",
    "1-1": "Unique identifier for the client (tenant backend ID).",
    "2-0": "toType",
    "2-1": "msisdn: Outbound call to a mobile number.  \ncustomerId: Outbound call to the mobile number associated with the customer ID.",
    "3-0": "requestTimestamp",
    "3-1": "Timestamp when the request was submitted, in ISO8601 format.",
    "4-0": "groupId",
    "4-1": "Identifier for the group associated with the user.",
    "5-0": "answeredAt",
    "5-1": "Timestamp when the call was answered, in UTC.",
    "6-0": "channel",
    "6-1": "Set to Voice for all voice APIs.",
    "7-0": "messageId",
    "7-1": "Unique identifier for the message transaction being queried.",
    "8-0": "requestedReceipts",
    "8-1": "Events for which you will receive notifications. Possible values:  \n _ **Offered**: Call is offered to the network.  \n   **Accepted**:  Call is accepted by the network and placed to the end customer.  \n   **Answered**: Call is answered by the end customer.  \n   **Dropped**: Call is dropped due to an internal technical error.  \n   **Rejected**: Call is rejected (e.g., network failure, busy, or declined by the customer).  \n   **Released**: Call is ended by the platform.  \n   **Disconnected**: Call is disconnected by the end customer.  \n   **Trombone Connected**: Outbound call is connected to an agent; both the end customer and agent are on the call.  \n   **Trombone Released**: Agent exits the call.  \n   **Message Expired**: Call request expired after the configured expiry time. _",
    "9-0": "priority",
    "9-1": "Call priority.  \nPossible values:  \n1: Low  \n2: Medium  \n3: High",
    "10-0": "version",
    "10-1": "Messaging API version used for the request. Example: '2.0'.",
    "11-0": "content",
    "11-1": "Media details for the call, including TTS messages or other media.",
    "12-0": "ttsProcessor",
    "12-1": "Text-to-speech engine used. Only 'Azure' is supported.",
    "13-0": "voice",
    "13-1": "Voice selected for audio synthesis.",
    "14-0": "gender",
    "14-1": "Gender of the selected voice (e.g., 'Male', 'Female').",
    "15-0": "fileSize",
    "15-1": "Size of the generated audio file.",
    "16-0": "language",
    "16-1": "Language of the selected voice (e.g., 'en-US', 'hi-IN').",
    "17-0": "text",
    "17-1": "Input text sent for speech conversion.",
    "18-0": "type",
    "18-1": "Input text format. Use 'plain text' or 'SSML'.",
    "19-0": "region",
    "19-1": "Region of the TTS engine.",
    "20-0": "voiceType",
    "20-1": "Type of voice used. Only 'Neural' is supported.",
    "21-0": "endedAt",
    "21-1": "Timestamp when the call ended, in UTC.",
    "22-0": "teamId",
    "22-1": "Team identifier associated with the call. Present based on authorization.",
    "23-0": "callbackData",
    "23-1": "Data included in the 'callbackData' field of the request.",
    "24-0": "notifyUrl",
    "24-1": "URL to receive callback data and receipts.",
    "25-0": "from",
    "25-1": "Number initiating the outbound call.",
    "26-0": "correlationId",
    "26-1": "Correlation ID used in the call request, returned in the response.",
    "27-0": "to",
    "27-1": "Numbers to which the call is initiated.",
    "28-0": "direction",
    "28-1": "Indicates if the call is outbound or inbound.",
    "29-0": "status",
    "29-1": "Status of the call. Possible values:  \n   _**Initiated**: Call has been initiated.  \n   **Ringing**: Call is ringing and not yet answered.  \n   **In-progress**: Call is in progress.  \n   **Completed**: Call completed successfully.  \n   **Busy**: User's phone is busy.  \n   **No-answer**: Call was not answered by the user.  \n   **Canceled**: Call was rejected by the user.  \n   **Failed**: Call failed abruptly. _"
  },
  "cols": 2,
  "rows": 30,
  "align": [
    "left",
    "left"
  ]
}
[/block]