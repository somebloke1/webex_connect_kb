> 📘 API Endpoints & Postman Collection
> 
> The Voice channel is supported via Voice API v1 and Send Message API v2. 
> 
> The API endpoint for it is: [https://api.{YourRegion}.webexconnect.io/v1/voice/calls]. 
> 
> Please modify YourRegion in the URL as per your tenant’s region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [Postman Collection](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis) for trying Programable Voice Calls Using Voice API v1.

> 📘 API Response and Error Codes
> 
> Voice API v1 is asynchronous. The HTTP response confirming acceptance of your request is sent immediately after you invoke the API. Further processing details are sent to your callback URL (the notify URL specified in your request). Refer to [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1) for more information.

With <<prodname>>’s Voice API, you can build custom voice-calling applications (developer application) that connect to our voice network using an HTTPS-based interface. Embed both inbound and outbound voice capabilities with a set of well-defined APIs.

Develop voice-enabled applications by sending and receiving HTTPS requests. When an incoming call is received on a number in your tenant, <<prodname>> notifies your application with a webhook event. Your application can then respond with actions to control call flow and features.

Supported actions:

- Answer
- Play (optionally collect DTMF and speech)
- Record
- Call Patch
- Hangup

## Make a Phone Call

To make an outbound call from a <<prodname>> number, send a POST request to the API v1 Make Call endpoint.

Once the call is answered, <<prodname>> sends an event to your CallbackUrl specified in the request. Your application should respond with one of the following actions to continue the call:

- Play
- Record
- Call Patch
- Hangup

## Request Body to Making a Phone Call

```json Make a Phone Call
{
    "callerId": "", //Mandatory. The Webex Connect asset/number from which you want the call to be initiated. The number must be voice enabled.
    "dialedNumber": "", //Mandatory. Number to dial and start call sessions with.
    "recordCallSeconds": 0, //Integer. If present and a positive value, record the call for these many seconds. A value of'0' indicates recording until the end of the call.
    "detectVoiceMail": true, //Optional, If the value is 'true', then the system will send a check if the call is answered by voicemail or a human. If the call is answered by voicemail, then your application will receive a voicemail-detected event.   
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference of a particular transaction or event. This is configured as a part of the request.
    "callbackUrl": "", //Optional. URL for sending call-related events. You will have to respond with an action for these events.
   "callbackUrlAuthId":"TNPXXXT09U" //Optional.
}
```

## Make a Phone Call Body Parameters

The following are the parameters of the request body:

| Parameter         | Type    | Mandatory | Description                                                                                                                                                                                                                                                                 |
| :---------------- | :------ | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| callerId          | string  | yes       | The <<prodname>> asset/number from which you want the call to be initiated. The number must be voice-enabled.                                                                                                                                                               |
| dialedNumber      | string  | yes       | Number to dial and start call sessions.                                                                                                                                                                                                                                     |
| recordCallSeconds | integer | no        | Specify the number of seconds the call must be recorded for after it is answered. If present and a positive value, record the call for these many seconds. A value of '0' indicates recording until the end of the call.                                                    |
| detectVoiceMail   | boolean | no        | If the value is 'true', then the system will send a check if the call is answered by voicemail or a human. If the call is answered by voicemail, then your application will receive a voicemail-detected event. If the value provided does not match, it defaults to false. |
| correlationId     | string  | no        | User-defined ID that is assigned to an individual message for unique identification.                                                                                                                                                                                        |
| callbackUrl       | string  | no        | URL for sending call-related [events](#Events). You will have to respond with an [action](#Actions) for these events.                                                                                                                                                       |
| callbackUrlAuthId | string  | no        | Unique authentication ID.                                                                                                                                                                                                                                                   |

## Receive a Phone Call

To handle incoming calls with APIs, set the callback URL in the [Numbers](https://help.webexconnect.io/docs/phone-numbers#handle-incoming-calls-via-callback-url) section of <<prodname>>. When a call is received, <<prodname>> sends a notification to your callback URL with caller and dialed number information. Your application should respond with one of the following actions to continue the call: 

- Answer
- Play
- Record
- Call Patch
- Hangup

> 📘 Note:
> 
> Use the ANSWER action only for inbound calls, and only in response to the ACCEPTED event.

For further details, refer to the [Handle incoming calls via callback URL](https://help.webexconnect.io/docs/phone-numbers#handle-incoming-calls-via-callback-url)  section.

### Events

| Event Name         | Description                                                                                                                                                                                                                                         |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accepted           | 'ACCEPTED' event is sent from <<prodname>> to developer applications when incoming calls are received on the configured number. For this request, the developer can send an ANSWER or HANGUP action.                                                |
| Answered           | 'ANSWERED' event is sent from <<prodname>> to developer application when the calls are answered. For the answered event, the developer application can send a PLAY, RECORD, CALL PATCH, or HANGUP action.                                           |
| Dropped            | 'DROPPED' event is sent from <<prodname>> to developer application when the call gets disconnected.                                                                                                                                                 |
| Played             | 'PLAYED' event is sent from <<prodname>> to developer application when ongoing play is completed for a call. You can send a PLAY, RECORD, CALL PATCH, or HANGUP action.                                                                             |
| Streamed           | 'STREAMED' event is sent from <<prodname>> to developer application when this speech collection is completed in the play action. You can send a PLAY, RECORD, CALL PATCH, or HANGUP action.                                                         |
| Recorded           | 'RECORDED' event is sent from <<prodname>> to the developer application when the record action is completed. You can send a PLAY, RECORD, CALL PATCH, or HANGUP action.                                                                             |
| Failure            | For any failures while executing an action, <<prodname>> will send the FAILURE EVENT with failure status and reason.                                                                                                                                |
| Patched            | 'PATCHED' event is sent from <<prodname>> to developer application when a B party is successfully added to the call as part of a CALL PATCH action.                                                                                                 |
| Collected Digits   | 'COLLECTED DIGITS' event is sent from <<prodname>> to developer application when multiple Dual Tone Multi Frequency digits are collected as part of the play action. You can send a PLAY, RECORD, CALL PATCH, or HANGUP action.                     |
| Voicemail Detected | 'VMDETECTED' event is sent from <<prodname>> to developer application when the call is answered by voicemail. This event is triggered within 5 to 7 seconds after the call is answered, and the anticipated response to the event is a PLAY action. |

```json ACCEPTED EVENT
{
    "event": "ACCEPTED",
    "callerId": "+4475XXXXXXXX",
    "dialedNumber": "+4474XXXXXXXX",
    "offeredTime": "2023-04-25T05:14:50.178Z",
    "eventTime": "2023-04-25T05:14:52.031Z",
    "sessionId": "c51e56af-0c71-XXXX-XXXX-53d299012e46"
}
```
```json ANSWERED EVENT
{
    "event": "ANSWERED",
    "callerId": "+1315XXXXXXXX",
    "dialedNumber": "+9185XXXXXXXX",
    "offeredTime": "2022-11-17T09:22:55.624Z",
    "answeredTime": "2022-11-17T09:23:06.139Z",
    "eventTime": "2022-11-17T09:23:06.161Z",
    "sessionId": "a12c95ad-1999-XXXX-XXXX-25ed04d2d7c2"
}
```
```json DROPPED EVENT
{
    "event": "DROPPED",
    "status": "SUCCESS",
    "droppedBy": "CALLEE",
    "error": {
        "code": "2008",
        "message": "Call Dropped by Network/End user"
    },
    "eventTime": "2023-02-21T10:08:52.562Z",
    "sessionId": "a4a45c38-0a4d-XXXX-XXXX-f1f96796b258"
}
```
```json PLAYED EVENT
{
    "status": "SUCCESS",
    "playedDuration": 1,
    "event": "PLAYED",
    "eventTime": "2023-04-26T13:12:47.233Z",
    "sessionId": "64277de6-XXXX-XXXX-XXXX-54392465376d",
    "transactionId": "c63cab3c-XXXX-XXXX-8529-2960395e811d"
}
```
```json STREAMED EVENT
{
    "event": "STREAMED",
    "callerId": "+131XXXXXXXX",
    "dialedNumber": "+9189XXXXXXXX",
    "status": "SUCCESS",
    "text": "credit card",
    "eventTime": "2022-12-07T16:46:06.343Z",
    "sessionId": "a12c95ad-1999-XXXX-XXXX-25ed04d2d7c2",
    "transactionId": "3afd709e-XXXX-XXXX-b797-ba6bf2a4b366"
}
```
```json RECORDED EVENT
{
    "event": "RECORDED",
    "status": "SUCCESS",
    "recordingFileName": "https://anydomain.imiconnect.ca/voice-recordings/menu_1681891700_909100209630299_5.wav",
    "recordingLength": 6,
    "eventTime": "2023-04-19T08:08:32.132Z",
    "sessionId": "133941b7-c052-XXXX-XXXX-026b790c2644",
    "transactionId": "2bde1a0d-XXXX-XXXX-8ece-136893348466"
}
```
```json FAILURE EVENT
{
    "event": "STREAMED",
    "callerId": "+131XXXX521",
    "dialedNumber": "+918XXXX726",
    "status": "FAILURE",
    "error": {
        "message": "HttpStream failed, error code 500"
    },
    "eventTime": "2025-12-07T16:48:12.891Z",
    "sessionId": "a12c95ad-XXXX-XXXX-ba72-25ed04d2d7c2",
    "transactionId": "1427e243-d3ed-XXXX-XXXX-7108f88a5084"
}
```
```json PATCHED EVENT
{
    "event": "PATCHED",
    "eventTime": "2022-12-07T16:48:12.891Z",
    "sessionId": "a12c95ad-1999-XXXX-XXXX-25ed04d2d7c2",
    "transactionId": "1427e243-d3ed-XXXX-XXXX-7108f88a5084",
    "status": "SUCCESS",
    "ConnectedOn": "2022-12-07T16:48:15.891Z"
    "recordingFileName": [
        "1.wav",
        "2.wav"
    ]
    "droppedBy": "CALLER"
}
```
```json COLLECTED DIGITS EVENT
{
    "event": "COLLECTED_DIGITS",
    "eventTime": "2022-12-07T16:48:12.891Z",
    "sessionId": "a12c95ad-1999-XXXX-XXXX-25ed04d2d7c2",
    "transactionId": "1427e243-d3ed-XXXX-XXXX-7108f88a5084",
    "status": "SUCCESS",
    "numOfDigits": 8
    "digitsReceived": "234XXX76",
    "terminationDigit": "1",
    "playedDuration": 300,
}
```
```json VOICEMAIL DETECTED
{
    "callerId": "+120XXX4345",
    "dialedNumber": "+447XXX22222",
    "event": "VMDETECTED",
    "eventTime": "2025-01-08T16:14:57.125Z",
    "sessionId": "870ab7d3-550f-XXXX-XXXX-2de285d2c8f5",
    "correlationId": "test123",
    "transactionId": "92332ada-2739-XXXX-XXXX-f3af37e443f0"
}
```

### Actions

| Action Name | Description                                                                                                                                                                                                                      |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Answer      | 'ANSWER' action is sent from the developer application to <<prodname>>, to inform <<prodname>> to answer the call.                                                                                                               |
| Hangup      | 'HANGUP' action is sent from the developer application to <<prodname>>, to inform <<prodname>> to hang up or reject the call.                                                                                                    |
| Play        | 'PLAY' action is sent from the developer application to <<prodname>> to play a content file or use Text-to-Speech to play the specified audio. You can also collect Dual Tone Multi Frequency (DTMF) input or speech, if needed. |
| Patch       | 'PATCH' action is sent from the developer application to <<prodname>>, to inform <<prodname>> to add a B party to the ongoing call.                                                                                              |
| Record      | 'RECORD' action is sent from the developer application to <<prodname>>, to inform <<prodname>> to record the ongoing call for a specific duration.                                                                               |

```json ANSWER ACTION
{
  "action": "ANSWER"
}
```
```json HANGUP ACTION
{
    "action": "REJECT",
    "reason": "Call Failed due to configured menu in reject state"
}
```
```json PLAY ACTION
{
    "action": "PLAY",
    "audio": [
        {
            "type": "URL",
            "location": "https://www2.cs.uic.edu/~i101/SoundFiles/CantinaBand3.wav"
        },
        {
            "type": "TTS",
            "style": "NEURAL",
            "language": "en-US",
            "voice": "GuyNeural;Male",
            "gender": "MALE",
            "engine": "AZURE",
            "text": "greetings from cisco please enter 3 digits pin followed by # to patch "
        }
    ],
    "collectInput": {
        "terminationDigit": "#",
        "maxDigits": 0,
        "digitTimeout": 5
    },
    "streamInput": {
        "timeout": 20,
        "maxsilence": 5,
        "model": "DEFAULT",
        "language": "en-US",
        "asrEngine": "GOOGLE",
        "recordStream": true,
        "singleUtterence": false,
        "alternateLanguages": [
            "fr-CA",
            "en-CA"
        ]
    }
}
```
```json PATCH ACTION
{
    "action": "PATCH",
    "recordCall": true,
    "holdAudio": {
        "type": "URL",
        "location": "https://www2.cs.uic.edu/~i101/SoundFiles/CantinaBand3.wav"
    },
    "greetingAudio": {
        "type": "TTS",
        "text": "thank you for waiting call is connected now"
    },
    "greetingRepeatCount": 0,
    "patchCallerId": "+1530XXXX584",
    "dialedNumber": "+9199XXXX7784",
    "passDtmf": false
}
```
```json RECORD ACTION
{
    "action": "RECORD",
    "audio": [
        {
            "type": "TTS",
            "style": "NEURAL",
            "language": "en-US",
            "voice": "GuyNeural;Male",
            "gender": "MALE",
            "engine": "AZURE",
            "text": " Hello buddy start recording now"
        }
    ],
    "timeoutSeconds": 20,
    "terminationDigit": "5"
}
```

Refer to the [Supported Languages for Voice TTS (Text-to-Speech)](https://help.webexconnect.io/docs/supported-languages-for-voice) page for more information..