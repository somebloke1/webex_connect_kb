# Make Calls Using Send Message API v2

Source: https://developers.webexconnect.io/reference/send-message-api-v2-make-voice-call
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:44+00:00

> API Endpoint & Postman Collection
>
> Voice channel is supported via Voice API and Send Message API v2 . 
>
> API endpoint for it is: [https://{YourRegion}.webexconnect.io/v2/messages].
>
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
>
> Refer to [Postman Collection](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis) for trying Make Calls Using Send Message API v2.

> 📘 API Response and Error Codes
> 
> Send Message API v2 is asynchronous. You receive an HTTP response when your request is accepted, and further processing details are sent to your callback URL. For more information, see [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1).

With Send Message API v2, you can make calls in two ways:

- [Make Calls Using Send Message API v2](#request-body-to-make-calls-using-a-media-id) 
- [Make Calls Using Send Message API v2](#make-call-using-text-to-speech) 

## Request Body to Make Calls using a Media ID

```json Make Calls using a Media ID
{
    "channel": "voice", //Mandatory. 
    "from": "{{from}}", //Mandatory. E.164 format required/recommended.
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended.
            ]
        }
    ],
    "requestedReceipts": [ //Optional.
        "offered",
        "accepted",
        "answered",
        "released",
        "rejected",
        "disconnected",
        "dropped"
    ],
    "content": {
        "type": "media",
        "mediaId": "" // Media ID of the audio file you wish to play.
    },
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference to a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

## Make Calls using a Media ID Body Parameters

The following are the parameters of the request body:



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channel | string | yes | Set to 'voice' when sending voice messages. |
| from | string | yes | The phone number or asset to use for making the call. You must purchase a voice-enabled long code under Numbers. If you do not see the option to buy numbers, contact the Webex Connect Ops Team.⁣   |
| to | JSONArray | yes | Array of destination objects, each with a mobile number (msisdn), and a correlation ID (correlationId). |
| msisdn | JSONArray | yes | Array of phone numbers in E.164 format (e.g., +44XXXXXXXXXX) to which the voice call should be sent.  <br>  <br>**Note: **If +E.164 format is enabled for your tenant, all numbers in the 'to' field must follow this format. This does not apply to the 'from' field.  |
| requestedReceipts | JSONArray | no | JSON array that specifies which delivery receipt webhooks are sent to your notifyUrl.  <br>Valid values:  <br>**Offered: ** Call offered to the network.  <br>**Accepted: **Call accepted by the network and placed to the end customer.  <br>**Answered: ** Call answered by the end customer.  <br> **Dropped: ** Call dropped due to a technical error.  <br>**Rejected: ** Call rejected (e.g., network failure, busy, declined by the customer).  <br>**Released: **Call ended by the platform.  <br>**Disconnected: ** Call disconnected by the end customer.  <br>  <br>See [Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks) for examples. |
| content | JSONObject | yes  | JSON object containing the required 'type' and 'mediaId' parameters for the voice channel. |
| type | string | yes | Message content type. Set to 'media' or 'Text-to-Speech'. |
| mediaId | string | yes | Media ID of the audio file to play. Required if type is "media". Use the ID of the prompt uploaded in Webex Connect. |
| notifyUrlAuthId | string | no | Authentication ID for securing webhook notifications. |
| contactPolicy | JSONObject | no | JSON object specifying contact policy checks before making the outbound voice call. Requires Contact Policy App configuration. |
| contactPolicyGroup | string | yes (if you want to apply Contact Policy checks before sending the message) | Group ID for applying contact policy checks. Required if either 'channelCheckConsent' or 'channelApplyFrequencyCap' is set to 'true'. |
| channelCheckConsent | boolean | no | Set to 'true' to require opt-in consent before making a voice call. Defaults to 'false'. Atleast one of 'channelCheckConsent' or 'channelApplyFrequencyCap' must be 'true'.  |
| channelApplyFrequencyCap | boolean | no | Set to 'true' to enforce the group frequency cap for the channel. Defaults to 'false'. At least one of 'channelCheckConsent' or 'channelApplyFrequencyCap' must be 'true'. |




## Sample Response Body

```json 201 Result
{
    "requestTimestamp": "2024-09-05T00:03:01.708-04:00",
    "messageId": "a770f205-1234-XXXX-XXXX-6dc3e388b9b5",
    "correlationId": "12345",
    "status": "queued"
}
```
```json 400 Bad Request
   {
        "code": "7000",
        "message": "Invalid JSON"
    }
```
```Text 401 Unauthorised
No response body
```

## Response Parameters

| Parameter        | Description                                                                                                                                                                      |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requestTimestamp | Date and time when the request was submitted, in ISO8601 format.                                                                                                                 |
| messageId        | Unique transaction ID for the message request.                                                                                                                                   |
| correlationId    | Correlation ID provided in the request, returned for tracking.                                                                                                                   |
| status           | Status of the call. Possible values: 'Queued' or 'Rejected'.                                                                                                                     |
| code             | Response code for the request. See [Channel Specific Status Codes](https://developers.webexconnect.io/reference/channel-specific-status-codes-1#voice) section for more details. |
| message          | Description of the error or status message, such as 'Parameter missing' or 'Invalid parameter'.                                                                                  |

### HTTP Response Codes



| Response Codes | Description |
| --- | --- |
| 200 OK | Successful |
| 201 Created | Created |
| 201 Partial Content | Partial Content. |
| 400 Bad Request | Bad input parameter. The error description should indicate which one and why. |
| 401 Unauthorized | Customer doesn’t exist.  <br>Customer account over quota. |
| 404 Not Found | Resource not found. |
| 405 Method Not Allowed | The resource doesn't support the specified HTTP verb. |
| 409 Conflict | Conflict |
| 429 Too Many Requests | Too many requests for rate limiting. |
| 500 Internal Server Error | Servers are not working as expected. The request is probably valid but needs to be requested again later. |
| 503 Service Unavailable | Service Unavailable. |




## Examples

### Make Call using Text-to-Speech (TTS)

```json Make Call using Text-to-Speech
{
    "channel": "voice", //Mandatory. 
    "from": "{{from}}",  //Mandatory. E.164 format required/recommended.
    "to": [
        {
            "msisdn": [
                "{{msisdn}}"  //Mandatory. E.164 format required/recommended.
            ]
        }
    ],
    "content": {
        "type": "TTS",
        "ttsProcessor": "Azure",
        "language": "en-US",
        "voice": "GuyNeural",
        "region": "Canada",
        "text": "This is a notification of school closure",
        "voiceType": "Neural",
        "gender": "male"
    },
    "correlationid": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

The following are the parameters required to make a call using Text-to-Speech:



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | yes | Specifies the message type for dynamic TTS conversion. |
| ttsProcessor | string | yes (Applicable only if content type is "TTS") | TTS engine to use for conversion. Required if 'type' is 'TTS'. Only Azure is supported. |
| language | string | yes (Applicable only if content type is "TTS") | Refer to [Azure Documentation](https://docs.microsoft.com/en-in/azure/cognitive-services/speech-service/#pivot=start&panel=texttospeech).  <br>Click the [Supported Languages ](https://help.webexconnect.io/docs/supported-languages-for-voice) section for a list of all supported TTS languages. |
| voice | string | yes (Applicable only if content type is "TTS") | Refer to [Azure Documentation](https://docs.microsoft.com/en-in/azure/cognitive-services/speech-service/#pivot=start&panel=texttospeech). Click the [Supported Voice](https://help.webexconnect.io/docs/supported-languages-for-voice)   section for a list of all supported voices. |
| region | string | yes (Applicable only if content type is "TTS") | Refer to [Azure Documentation](https://docs.microsoft.com/en-in/azure/cognitive-services/speech-service/#pivot=start&panel=texttospeech).  |
| text | string | yes (Applicable only if content type is "TTS") | Text to convert to speech and play to the end user when the call is answered. Maximum 2000 characters. |
| voiceType | string | yes (Applicable only if content type is "TTS") | The voiceType is 'Neural'. |
| gender | string | yes (Applicable only if content type is "TTS") | Gender of the voice used for text-to-speech. Click the [Supported Gender](https://help.webexconnect.io/docs/supported-languages-for-voice) section for a list of all supported gender. |



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
