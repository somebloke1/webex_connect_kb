> 📘 API Endpoints & Postman Collection
> 
> The Voice channel is supported via Voice API v1 and Send Message API v2. 
> 
> The API Endpoint: [https://api. {YourRegion}. webexconnect.io/v1/voice/messages]. 
> 
> Replace YourRegion in the URL with your tenant's region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [Postman Collection](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis) for trying Make Outbound Calls Using Voice API v1.

> 📘 API Response and Error Codes
> 
> Voice API v1 is asynchronous. The API immediately returns an HTTP response confirming acceptance of your request. All subsequent processing details are sent to the callback URL (the notify URL specified in your request).  
> For more information, see [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1).

Voice API v1 supports both simple outbound notifications and programmable voice for interactive, two-way calling experiences. To get started, see the simple outbound call examples below. For details on interactive programmable voice features, visit the [Programmable Voice Calls Using Voice API v1](https://developers.webexconnect.io/reference/voice-only-api-v1-programmable-voice-api) page. 

Voice API v1 allows you to make voice calls in the following ways:

- [Play a text-to-speech message](#request-body-to-play-a-tts-message-using-voice-api-v1)
- [Play a pre-recorded media](#play-pre-recorded-media)
- [Play message by passing the media URL](#play-message-by-passing-the-url)
- [Play SSML-based text-to-speech message](#play-an-ssml-message)  

## Request Body to Play a Text-to-Speech (TTS) message using Voice API v1

```json Play a TTS message
{
    "callerId": "", //Mandatory. The Webex Connect asset/number from which you want the call to be initiated. The number must be voice enabled.
    "dialedNumber": "", //Mandatory. Number to dial and start call sessions with.
    "audio": { //Mandatory.
        "type": "TTS", //Mandatory.
        "style": "NEURAL", //Mandatory. Neural voice. Default value is NEURAL.
        "language": "en-US", //Mandatory. Language of the text being synthesized Default value is en-US.
        "voice": "AriaNeural", //Mandatory. The desired voice for the rendered speech.
        "gender": "FEMALE", //Mandatory. Gender of the synthesized voice. Default value is FEMALE.
        "engine": "AZURE", //Mandatory. Which TTS engine to use to render the speech. Default value is AZURE. 
        "textFormat": "TEXT", //Mandatory. Format of text feild. If TEXT, text field contains plain text. If SSML, text field contains valid SSML script. Default value is TEXT.
        "text": "Hello, Good morning! We are calling from Webex", //Mandatory. The text that you wish to be rendered to speech via the TTS engine. This can be plain text or SSML.
    },
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference to a particular transaction or event. This is configured as a part of the request.
    "callbackUrl": "", //Optional. URL for sending delivery status of the call.
    "callbackUrlAuthId":"TNPXXXT09U" //Optional.
}
```

## Play a TTS message using Voice API v1 Body Parameters

The following are the parameters of the request body:

| Parameter         | Type   | Mandatory | Description                                                                                                                                                                                            |
| :---------------- | :----- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| callerId          | string | yes       | <<prodname>> asset or number to initiate the call from. Must be voice-enabled.                                                                                                                         |
| dialedNumber      | string | no        | The number to dial and start the call session.                                                                                                                                                         |
| audio             | object | yes       | Object defining the text-to-speech parameters for audio rendering.                                                                                                                                     |
| type              | string | yes       | Type of audio. Set to 'TTS'.                                                                                                                                                                           |
| style             | string | yes       | Neural voice style. Defaults to 'NEURAL' if an invalid value is provided.                                                                                                                              |
| language          | string | yes       | Language for text synthesis. Defaults to 'en-US' if an invalid value is provided. Refer the [link ](https://help.webexconnect.io/docs/supported-languages-for-voice)for supported languages.           |
| voice             | string | yes       | Desired voice for speech rendering. Defaults to 'AriaNeural' if an invalid value is provided. Refer the [link ](https://help.webexconnect.io/docs/supported-languages-for-voice) for supported voices. |
| gender            | string | yes       | Gender of the synthesized voice. Defaults to 'FEMALE' if an invalid value is provided. Refer the [link ](https://help.webexconnect.io/docs/supported-languages-for-voice) for supported gender.        |
| engine            | string | yes       | TTS engine for speech rendering. Defaults to 'AZURE' if an invalid value is provided.                                                                                                                  |
| textFormat        | string | yes       | Format of the text field. Use 'TEXT' for plain text or 'SSML' for valid SSML script.                                                                                                                   |
| text              | string | yes       | Text to be converted to speech. Can be plain text or [SSML](<# Play an SSML Message>).                                                                                                                 |
| correlationId     | string | no        | User-defined ID for uniquely identifying the API request.                                                                                                                                              |
| callbackUrl       | string | no        | URL to receive delivery status updates for the voice call. See [Voice Outbound Webhooks](https://developers.webexconnect.io/reference/voice-only-api-v1-make-outbound-calls) for notification samples. |
| callbackUrlAuthId | string | no        | Unique authentication ID.                                                                                                                                                                              |

## Sample Response Body

```json 202 Success Code
{
    "acceptedTime": "2024-09-04T06:42:16.520-04:00",
    "messageId": "acc27bb5-1234-XXXX-XXXX-1a6036fcced5",
    "correlationId": "1234"
}
```
```json 400 Invalid Parameter
{
    "code": "7004",
    "message": "Invalid parameter -  : contentType"
}
```
```json 403 Forbidden
{
    "code": "7001",
    "message": "Authentication failed."
}
```

## Response Parameters

| Parameter     | Description                                                                                                                                                                  |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| acceptedTime  | Date and time when the request was accepted.                                                                                                                                 |
| messageId     | Unique transaction ID of the message request.                                                                                                                                |
| correlationId | Correlation ID provided in the request, returned in the response for tracking.                                                                                               |
| code          | Response code for the request. See the [Channel Specific Status Codes](https://developers.webexconnect.io/reference/channel-specific-status-codes-1#voice) for more details. |
| message       | Description of the error or status message, such as "Parameter missing" or "Invalid parameter."                                                                              |

## Examples

### Play pre-recorded media

```json Play pre-recorded media
{
    "callerId": "", //Mandatory. The Webex Connect asset/number from which you want the call to be initiated. The number must be voice enabled.
    "dialedNumber": "", //Mandatory. Number to dial and start call sessions with.
    "audio": { //Mandatory.
        "type": "MEDIA", //Mandatory.
        "mediaId": "" //Mandatory. Media ID of the audio file you wish to play.
    },
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackUrl": "", //Optional. URL for sending delivery status of the call.
    "callbackUrlAuthId":"TNPXXXT09U" //Optional.
}
```

The following are the parameters required to play pre-recorded media:

| Parameter | Type   | Mandatory | Description                                                                                                                             |
| :-------- | :----- | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| type      | string | yes       | Type is 'MEDIA'.                                                                                                                        |
| mediaId   | string | yes       | mediaId of the audio file you wish to play. You can find the mediaId in the voice media section after you have uploaded the audio file. |

### Play message by passing the media URL

```json Play message by passing the media URL
{
    "callerId": "", //Mandatory. The Webex Connect asset/number from which you want the call to be initiated. The number must be voice enabled.
    "dialedNumber": "", //Mandatory. Number to dial and start call sessions with.
    "audio": { //Mandatory.
        "type": "URL", //Mandatory.
        "location": "" //Mandatory. URL to the audio file you wish to play.
    },
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackUrl": "" //Optional. URL for sending delivery status of the call.
}
```

The following are the parameters required to play a message by passing the media URL:

| Parameter | Type   | Mandatory | Description                                                                      |
| :-------- | :----- | :-------- | :------------------------------------------------------------------------------- |
| type      | string | yes       | Field for the 'URL'.                                                             |
| location  | string | yes       | URL to the audio file you wish to play. The supported formats are .wav and .mp3. |

### Play Speech Synthesis Markup Language (SSML)-based Text-to Speech message

```json Play Speech Synthesis Markup Language (SSML)-based TTS message
{				
    "callerId": "+120160473xxx", //Mandatory. The calling party number to use when placing the call to the dialed number.
    "dialedNumber":"+9199851xxxx", //Mandatory. Number to dial and start call sessions with. 
          "audio": {//Mandatory.
        "type": "TTS", //Mandatory.
        "style": "NEURAL", //Mandatory. Neural voice. Default value is NEURAL.
        "language": "en-US", //Mandatory. Language of the text being synthesized Default value is en-US
        "voice": "AriaNeural", //Mandatory.The desired voice for the rendered speech
        "gender": "FEMALE", //Mandatory.Gender of the synthesized voice. Default value is FEMALE
        "engine": "AZURE", //Mandatory. Which TTS engine to use to render the speech. Default value is AZURE. 
        "textFormat": "SSML", //Mandatory. Format of text feild. If TEXT, text field contains plain text. If SSML, text field contains valid SSML script. Default value is TEXT
        "text": "<text>Hello, world!!</text>" //Mandatory. The text that you wish to be rendered to speech via the TTS engine. This can be plain text or SSML.     
    },
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackUrl": "", //Optional. URL for sending notifications after call gets completed or failed.
    "callbackUrlAuthId": "TNPXXXT09U" //Optional.
}
```

The following are the parameters required to play an SSML-based TTS message:

| Parameter  | Type   | Mandatory | Description                                                                            |
| :--------- | :----- | :-------- | :------------------------------------------------------------------------------------- |
| textFormat | string | yes       | Format of the 'text' field. Use 'TEXT' for plain text or 'SSML' for valid SSML script. |
| text       | string | yes       | The text to be rendered to speech by the TTS engine. Can be plain text or SSML.        |