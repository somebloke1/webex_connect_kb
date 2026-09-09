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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "channel",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "Set to 'voice' when sending voice messages.",
    "1-0": "from",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "The phone number or asset to use for making the call. You must purchase a voice-enabled long code under Numbers. If you do not see the option to buy numbers, contact the <<prodname>> Ops Team.⁣  ",
    "2-0": "to",
    "2-1": "JSONArray",
    "2-2": "yes",
    "2-3": "Array of destination objects, each with a mobile number (msisdn), and a correlation ID (correlationId).",
    "3-0": "msisdn",
    "3-1": "JSONArray",
    "3-2": "yes",
    "3-3": "Array of phone numbers in E.164 format (e.g., +44XXXXXXXXXX) to which the voice call should be sent.  \n  \n**Note: **If +E.164 format is enabled for your tenant, all numbers in the 'to' field must follow this format. This does not apply to the 'from' field. ",
    "4-0": "requestedReceipts",
    "4-1": "JSONArray",
    "4-2": "no",
    "4-3": "JSON array that specifies which delivery receipt webhooks are sent to your notifyUrl.  \nValid values:  \n**Offered: ** Call offered to the network.  \n**Accepted: **Call accepted by the network and placed to the end customer.  \n**Answered: ** Call answered by the end customer.  \n **Dropped: ** Call dropped due to a technical error.  \n**Rejected: ** Call rejected (e.g., network failure, busy, declined by the customer).  \n**Released: **Call ended by the platform.  \n**Disconnected: ** Call disconnected by the end customer.  \n  \nSee [Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks) for examples.",
    "5-0": "content",
    "5-1": "JSONObject",
    "5-2": "yes ",
    "5-3": "JSON object containing the required 'type' and 'mediaId' parameters for the voice channel.",
    "6-0": "type",
    "6-1": "string",
    "6-2": "yes",
    "6-3": "Message content type. Set to 'media' or 'Text-to-Speech'.",
    "7-0": "mediaId",
    "7-1": "string",
    "7-2": "yes",
    "7-3": "Media ID of the audio file to play. Required if type is \"media\". Use the ID of the prompt uploaded in <<prodname>>.",
    "8-0": "notifyUrlAuthId",
    "8-1": "string",
    "8-2": "no",
    "8-3": "Authentication ID for securing webhook notifications.",
    "9-0": "contactPolicy",
    "9-1": "JSONObject",
    "9-2": "no",
    "9-3": "JSON object specifying contact policy checks before making the outbound voice call. Requires Contact Policy App configuration.",
    "10-0": "contactPolicyGroup",
    "10-1": "string",
    "10-2": "yes (if you want to apply Contact Policy checks before sending the message)",
    "10-3": "Group ID for applying contact policy checks. Required if either 'channelCheckConsent' or 'channelApplyFrequencyCap' is set to 'true'.",
    "11-0": "channelCheckConsent",
    "11-1": "boolean",
    "11-2": "no",
    "11-3": "Set to 'true' to require opt-in consent before making a voice call. Defaults to 'false'. Atleast one of 'channelCheckConsent' or 'channelApplyFrequencyCap' must be 'true'. ",
    "12-0": "channelApplyFrequencyCap",
    "12-1": "boolean",
    "12-2": "no",
    "12-3": "Set to 'true' to enforce the group frequency cap for the channel. Defaults to 'false'. At least one of 'channelCheckConsent' or 'channelApplyFrequencyCap' must be 'true'."
  },
  "cols": 4,
  "rows": 13,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Response Codes",
    "h-1": "Description",
    "0-0": "200 OK",
    "0-1": "Successful",
    "1-0": "201 Created",
    "1-1": "Created",
    "2-0": "201 Partial Content",
    "2-1": "Partial Content.",
    "3-0": "400 Bad Request",
    "3-1": "Bad input parameter. The error description should indicate which one and why.",
    "4-0": "401 Unauthorized",
    "4-1": "Customer doesn’t exist.  \nCustomer account over quota.",
    "5-0": "404 Not Found",
    "5-1": "Resource not found.",
    "6-0": "405 Method Not Allowed",
    "6-1": "The resource doesn't support the specified HTTP verb.",
    "7-0": "409 Conflict",
    "7-1": "Conflict",
    "8-0": "429 Too Many Requests",
    "8-1": "Too many requests for rate limiting.",
    "9-0": "500 Internal Server Error",
    "9-1": "Servers are not working as expected. The request is probably valid but needs to be requested again later.",
    "10-0": "503 Service Unavailable",
    "10-1": "Service Unavailable."
  },
  "cols": 2,
  "rows": 11,
  "align": [
    "left",
    "left"
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "type",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "Specifies the message type for dynamic TTS conversion.",
    "1-0": "ttsProcessor",
    "1-1": "string",
    "1-2": "yes (Applicable only if content type is \"TTS\")",
    "1-3": "TTS engine to use for conversion. Required if 'type' is 'TTS'. Only Azure is supported.",
    "2-0": "language",
    "2-1": "string",
    "2-2": "yes (Applicable only if content type is \"TTS\")",
    "2-3": "Refer to [Azure Documentation](https://docs.microsoft.com/en-in/azure/cognitive-services/speech-service/#pivot=start&panel=texttospeech).  \nClick the [Supported Languages ](https://help.webexconnect.io/docs/supported-languages-for-voice) section for a list of all supported TTS languages.",
    "3-0": "voice",
    "3-1": "string",
    "3-2": "yes (Applicable only if content type is \"TTS\")",
    "3-3": "Refer to [Azure Documentation](https://docs.microsoft.com/en-in/azure/cognitive-services/speech-service/#pivot=start&panel=texttospeech). Click the [Supported Voice](https://help.webexconnect.io/docs/supported-languages-for-voice)   section for a list of all supported voices.",
    "4-0": "region",
    "4-1": "string",
    "4-2": "yes (Applicable only if content type is \"TTS\")",
    "4-3": "Refer to [Azure Documentation](https://docs.microsoft.com/en-in/azure/cognitive-services/speech-service/#pivot=start&panel=texttospeech). ",
    "5-0": "text",
    "5-1": "string",
    "5-2": "yes (Applicable only if content type is \"TTS\")",
    "5-3": "Text to convert to speech and play to the end user when the call is answered. Maximum 2000 characters.",
    "6-0": "voiceType",
    "6-1": "string",
    "6-2": "yes (Applicable only if content type is \"TTS\")",
    "6-3": "The voiceType is 'Neural'.",
    "7-0": "gender",
    "7-1": "string",
    "7-2": "yes (Applicable only if content type is \"TTS\")",
    "7-3": "Gender of the voice used for text-to-speech. Click the [Supported Gender](https://help.webexconnect.io/docs/supported-languages-for-voice) section for a list of all supported gender."
  },
  "cols": 4,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]