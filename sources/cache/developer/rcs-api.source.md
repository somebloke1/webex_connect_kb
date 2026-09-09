> 📘 Please Note
> 
> The RCS channel is supported via<<prodname>> Send Message API v2.
> 
> The API endpoint for it is: [https://{YourRegion}.webexconnect.io/v2/messages].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying various types of RCS messages supported by <<prodname>>.

> 📘 Note
> 
> - Some mobile network RCS service providers wait for a text message delivery receipt prior to sending any related suggestion.  Ensure that your test plans include each carrier your program will terminate to.
> - The 'fileMessage' and 'richCardMessage' parameter fileSize requested is related to image and videos contained in URLs.  The measurement will be in bytes, and while not all MaaPs require an accurate fileSize, the value of the size should not be 0.
> - Please note that the substitutions apply only to 'Text' field.

RCS supports the following message types:

1. [RCS Text](#request-body-to-send-rcs-text-sample-using-send-message-api-v2---samples)
2. [RCS Text with Suggestions](#rcs-text-with-suggestions)
3. [RCS Text with Scheduling](#rcs-text-with-scheduling)
4. [RCS Template](#rcs-template)
5. [RCS File ](#rcs-file)
6. [RCS File with Suggestions](#rcs-file-with-suggestions)
7. [RCS File with Scheduling](#rcs-file-with-scheduling)
8. [RCS Rich card](#rcs-rich-card)
9. [RCS Rich card with Suggestions](#rcs-rich-card-with-suggestions)
10. [RCS Rich card with Scheduling](#rcs-rich-card-with-scheduling)
11. [RCS Carousel](#rcs-carousel)
12. [RCS Carousel with Suggestions](#rcs-carousel-with-suggestions)
13. [RCS Carousel with Scheduling](#rcs-carousel-with-scheduling)
14. [RCS Typing Event](#rcs-typing-event)
15. [RCS Read Event](#rcs-read-event)

## Request Body to Send RCS Text Sample using Send Message API v2 - Samples

```json RCS Text
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3, //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Clicked",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": {
        "type": "text", //Mandatory. Mention the type of RCS message type
        "text": "This is the message reagrding $(rcs_parameter1).  Reply Yes or No." //Mandatory. Contains the RCS message content.
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //Optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //Optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

## Send Message API v2 for RCS channel: Common Body Parameters

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
    "0-3": "The value needs to be \"rcs\" when sending RCS messages.",
    "1-0": "from",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "The rcsAppId of the respective RCS asset setup in <<prodname>> platform under assets. ",
    "2-0": "to",
    "2-1": "JSONArray",
    "2-2": "yes",
    "2-3": "An array of destination JSON objects that contain the mandatory destination msisdn, optional personalised substitutions, and correlationId for each destination object.",
    "3-0": "msisdn",
    "3-1": "JSONArray",
    "3-2": "yes",
    "3-3": "Phone number, i.e., msisdn to which the RCS message has to be sent in E.164 format e.g., +44XXXXXXXXXX  \n  \n_Note: If +E.164 format is enabled for your tenant - all the numbers in the **to** field should follow the \"+E.164\" format.  \nThis format displays the number with a \"+\" followed by the country code and the phone number.  \n+E.164 format does not apply to the numbers in the **from** field._",
    "4-0": "substitutions",
    "4-1": "JSONObject",
    "4-2": "no",
    "4-3": "List of key-value pairs for dynamic fields in the RCS message content. They are typically used to specify the values for dynamic fields in an RCS template.  \n  \nThere are two ways to define the 'substitutions' parameter - one inside the 'to' block and another outside the 'to' block.  \n  \nThe 'substitutions' parameter inside the 'to' block takes precedence over the 'substitutions' block that is outside the 'to' block, in case these values are provided in both places.  \n_Note: substitutions are applicable only for the text content type _",
    "5-0": "correlationId",
    "5-1": "string",
    "5-2": "no",
    "5-3": "User-defined ID that is assigned to an individual message for unique identification.",
    "6-0": "options",
    "6-1": "JSONObject",
    "6-2": "no",
    "6-3": "A JSON object that contains additional, RCS-specific options such as smsFallback,smsSenderID, and Text in the API. ",
    "7-0": "smsFallback",
    "7-1": "boolean",
    "7-2": "no",
    "7-3": "When true, auto SMS fallback will be tried for RCS failures. If this parameter is not passed, SMS fallback will be disabled by default. Refer to the note below for details on how it works.  \n_Note: If the smsFallback parameter is set to 'true' in the <<prodname>> messaging API to enable SMS fallback for RCS messages, then the smsSenderId and text fields become mandatory, to ensure that the fallback message is sent successfully.  \nFor more information on how the feature works, refer to the [FAQs chapter](https://developers.imiconnect.io/reference/rich-communication-services-faqs) ._",
    "8-0": "smsSenderId",
    "8-1": "string",
    "8-2": "Mandatory if smsFallback is true, else optional",
    "8-3": "Sender ID that is already configured on your account",
    "9-0": "text",
    "9-1": "string",
    "9-2": "Mandatory if smsFallback is true, else optional",
    "9-3": "The maximum limit for text messages is up to 1024 chars.",
    "10-0": "carrierId",
    "10-1": "string",
    "10-2": "",
    "10-3": "Optional, carrier id of the mobile number given above can be passed to skip carrier lookup.",
    "11-0": "trackClicks",
    "11-1": "string",
    "11-2": "",
    "11-3": "Optional. When enabled, this tracks all links in the HTML body unless a link is tagged as no-track-connect within the anchor tags. Link tracking is supported only for Email app assets configured using AWS SES.",
    "12-0": "trackOpens",
    "12-1": "string",
    "12-2": "",
    "12-3": "Optional. When enabled, this tracks opens of the email. Open tracking is supported only for Email app assets configured using AWS SES.",
    "13-0": "fromName",
    "13-1": "string",
    "13-2": "",
    "13-3": "Optional. A string that will appear next to the from address in most email inboxes",
    "14-0": "shortenLinks",
    "14-1": "string",
    "14-2": "no",
    "14-3": "When enabled, this shortens any HTTPS links in the message request's body. The expiry of Shortened URL is 180 days.",
    "15-0": "domain",
    "15-1": "string",
    "15-2": "yes",
    "15-3": "It is the domain configuration for shortening the links.  \nNote: 'domain' is mandatory only when 'options' object is used in the payload.",
    "16-0": "tags",
    "16-1": "string",
    "16-2": "",
    "16-3": "Reporting tags for tracking the  shortened link creates and clicks.",
    "17-0": "allowFallbackURL",
    "17-1": "string",
    "17-2": "",
    "17-3": "If true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.",
    "18-0": "requestedReceipts",
    "18-1": "JSONArray",
    "18-2": "no",
    "18-3": "A JSON array that can filter message delivery webhooks to the notifyUrl.  \n  \nCan contain one or more of the following:  \n\"Sent\",  \n\"Delivered\",  \n\"Read\",  \n\"Failed\"  \n  \nCheck [Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks) for delivery receipt samples.",
    "19-0": "content",
    "19-1": "JSONObject",
    "19-2": "yes, if the template is not provided",
    "19-3": "It is the JSON object that contains mandatory parameters 'type' and 'text' for the RCS channel. ",
    "20-0": "type",
    "20-1": "string",
    "20-2": "yes",
    "20-3": "Used for specifying the message content type. The acceptable value is 'text'.  \n  \nPlease note that 'text' supports many common special characters as per the RCS specification and is preferred where possible. ",
    "21-0": "text",
    "21-1": "string",
    "21-2": "yes",
    "21-3": "The RCS message content. A maximum of 1024 characters can be supported.",
    "22-0": "callbackData",
    "22-1": "string",
    "22-2": "no",
    "22-3": "A string that is returned with each outbound webhook for the message (delivery, failed, etc.). The maximum number of characters allowed in callbackData including any spaces is 2000.",
    "23-0": "notifyUrl",
    "23-1": "string",
    "23-2": "no",
    "23-3": "If provided, updates related to the delivery status of this message will be posted to this URL. Refer to [notification samples](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts).",
    "24-0": "notifyUrlAuthId",
    "24-1": "string",
    "24-2": "no",
    "24-3": "Unique Authentication ID.",
    "25-0": "contactPolicy",
    "25-1": "JSONObject",
    "25-2": "no",
    "25-3": "JSON Object will specify contact policy checks before sending the outbound RCS message. The Contact Policy App should be configured to use this feature as a prerequisite.",
    "26-0": "contactPolicyGroup",
    "26-1": "string",
    "26-2": "yes (if you want to apply Contact Policy checks before sending the message)",
    "26-3": "The GroupID is to be applied. It is required if any of the following options are included and set to true.",
    "27-0": "channelCheckConsent",
    "27-1": "boolean",
    "27-2": "no",
    "27-3": "Optional, assumed false if not specified. Set to true to require opt-in before sending the message. At least one of the “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”.",
    "28-0": "channelApplyFrequencyCap",
    "28-1": "boolean",
    "28-2": "no",
    "28-3": "Optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”."
  },
  "cols": 4,
  "rows": 29,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Sample Response Body

```json 201 Result
{
    "requestTimestamp": "2024-09-05T00:03:01.708-04:00",
    "messageId": "a770f205-1234-XXXX-x5x3-6dc3e388b9b5",
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

## Examples

### RCS Text with Suggestions

```json RCS Text with Suggestions
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3, //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
       	"Clicked",	
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": {
        "type": "text", //Mandatory. Mention the type of RCS message type
        "text": "This is the message reagrding $(rcs_parameter1).  Reply Yes or No.", //Mandatory. Contains the RCS message content.
        "suggestions": [
            {
                "type": "reply", //Mandatory if this suggestion type is used. 
                "displayText": "", //Mandatory. Text displayed so that user can easily respond
                "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
            },
            {
                "type": "viewLocation", //Mandatory if this suggestion type is used.
                "address": "", // Optional. Address of the coordinates mentioned
                "displayText": "", // Mandatory
                "latitude": 43.649269, //Mandatory, latitude of the location
                "longitude": -79.378423, //Mandatory, longitude of the location
                "postbackData": "" //Optional, Preconfigured response to the display text selected by the user.
            },
            {
                "type": "shareLocation", //Mandatory if this suggestion type is used.
                "displayText": "", // Mandatory
                "postbackData": "" // Optional
            },
            {
                "type": "openUrl", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "url": "https://www.domain.com", //Mandatory, The URL to which the user will be redirected upon clicking on openURL.
                "postbackData": "" //Optional
            },
            {
                "type": "calendarEvent", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "startTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, Start timestamp of the event in ISO date time format 8601.
                "endTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, End timestamp of the event in ISO date time format 8601.
                "meetingTitle": "", //Mandatory, Meeting title of the calendar event.
                "meetingDescription": "", //Optional
                "postbackData": "" //Optional
            },
            {
                "type": "dialPhone", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "phone": "", //Mandatory, Configured phone number to dial
                "postbackData": "" //Optional
            }
        ]
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //Optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //Optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
    }
}
```

Following are the parameters required for sending message using RCS Text with Suggestions:

[block:parameters]
{
  "data": {
    "h-0": "Parameter ",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "Suggestions",
    "0-1": "Array Object",
    "0-2": "No",
    "0-3": "Suggestions is a JSON array that can contain up to 10 suggestions with a message, 2 when within a carousel and 4 when within a richcard.  \nThese are the following suggestion types:  \nreply  \nviewLocation  \nshareLocation  \nopenUrl  \ncalendarEvent  \ndialPhone  \nFor more information, refer to [Suggestions Object](https://developers.webexconnect.io/reference/rcs-api#suggestions-object) below."
  },
  "cols": 4,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


#### **Suggestions Object**:

For each of these message type, various suggestions are possible to configure. Currently, 5 types of suggestions are supported - Reply, Viewlocation, Sharelocation, dialphone, and Calendarevent.

**SuggestionType: Reply**  
Suggested replies help your chatbot guide users through conversations by providing responses that the chatbot knows how to react to. Your agent sends replies in suggestion chip lists or rich cards.

| Parameter    | Type   | Mandatory                                         | Description                                                                                                    |
| :----------- | :----- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------- |
| type         | string | Yes,Mandatory if this type of suggestion is added | If the type is reply, the displayText and postbackData are subsequent parameters to be passed.                 |
| displayText  | string | yes                                               | This text is usually a short, user-friendly prompt that conveys the main content or action of the RCS message. |
| postbackData | string | no                                                | The preconfigured response to the display text selected by the user.                                           |

**SuggestionType: viewLocation**

The View location action displays a location in the user's default map app. You can specify the location either by latitude and longitude.

| Parameter    | Type   | Mandatory                                         | Description                                                                                                                                    |
| :----------- | :----- | :------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| type         | string | Yes,Mandatory if this type of suggestion is added | If the suggestion type is viewLocation, the address,displayText, latitude, longitude, and postbackData are subsequent parameters to be passed. |
| address      | string | no                                                | The configured location of the user.                                                                                                           |
| displayText  | string | yes                                               | This text is usually a short, user-friendly prompt that conveys the main content or action of the RCS message.                                 |
| latitude     | int    | yes                                               | The latitude of the configured location.                                                                                                       |
| longitude    | int    | yes                                               | The longitude of the configured location.                                                                                                      |
| postbackData | string | no                                                | The preconfigured response to the display text selected by the user                                                                            |

**SuggestionType: shareLocation**

The Share location action lets the user send a location to your chatbot.

| Parameter    | Type   | Mandatory                                         | Description                                                                                                       |
| :----------- | :----- | :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| type         | string | Yes,Mandatory if this type of suggestion is added | If the suggestion type is shareLocation, the displayText and postbackData are subsequent parameters to be passed. |
| displayText  | string | yes                                               | This text is usually a short, user-friendly prompt that conveys the main content or action of the RCS message.    |
| postbackData | string | no                                                | The preconfigured response to the display text selected by the user                                               |

**SuggestionType: openUrl**

The Open URL action opens the user's web browser to the specified URL. If an app is registered as a default handler for the URL, the app opens instead, and the icon for the action is the app's icon.

| Parameter    | Type   | Mandatory                                         | Description                                                                                                       |
| :----------- | :----- | :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| type         | string | Yes,Mandatory if this type of suggestion is added | If the suggestion type is openUrl, the displayText, URL, and postbackData are subsequent parameters to be passed. |
| displayText  | string | yes                                               | This text is usually a short, user-friendly prompt that conveys the main content or action of the RCS message.    |
| URL          | string | yes                                               | The URL to which the user will be redirected upon clicking on openURL.                                            |
| postbackData | string | no                                                | The preconfigured response to the display text selected by the user                                               |

**SuggestionType: calendarEvent**

The Create calendar event action opens the user's calendar app and begins to create a new event with the specified information.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "type",
    "0-1": "string",
    "0-2": "Yes, mandatory if this type of suggestion is added",
    "0-3": "If the suggestion type is calendarEvent, the displayText,startTime,endTime,meetingTitle,meetingDescription, and postbackData are subsequent parameters to be passed.",
    "1-0": "displayText",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "This text is usually a short, user-friendly prompt that conveys the main content or action of the RCS message.",
    "2-0": "startTime",
    "2-1": "string",
    "2-2": "yes",
    "2-3": "The timestamp of the scheduled calendar event can be added to the calendar.Start timestamp of the event in ISO date time format 8601.  \n  \nFor example, 2024-09-26T13:47:18.000Z - UTC",
    "3-0": "endTime",
    "3-1": "string ",
    "3-2": "yes",
    "3-3": "Timestamp of the calendar event when it is supposed to end.End timestamp of the event in ISO date time format 8601.  \n  \nFor example, 2024-09-26T13:47:18.000Z - UTC",
    "4-0": "meetingTitle",
    "4-1": "string",
    "4-2": "yes",
    "4-3": "Meeting title of the calendar event.",
    "5-0": "meetingDescription",
    "5-1": "string",
    "5-2": "no",
    "5-3": "Details of the meeting that is scheduled by the user.",
    "6-0": "postbackData",
    "6-1": "string",
    "6-2": "no",
    "6-3": "Preconfigured response to the display text selected by the user."
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**SuggestionType: dialPhone**

The Dial action guides the user to dial a phone number that your chatbot specifies.

| Parameter    | Type   | Mandatory                                          | Description                                                                                                         |
| :----------- | :----- | :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| type         | string | Yes, mandatory if this type of suggestion is added | If the suggestion type is dialPhone the displayText, phone and postbackData are subsequent parameters to be passed. |
| displayText  | string | yes                                                | This text is usually a short, user-friendly prompt that conveys the main content or action of the RCS message.      |
| phone        |        | yes                                                | Configured phone number of the user.                                                                                |
| postbackData | string | no                                                 | Preconfigured response to the display text selected by the user.                                                    |

> 🚧 Limitation
> 
> The routing of SMS messages will be handled by the standard routing rules configured for your tenant. Please reach out to your account manager for more information

### RCS Text with Scheduling

```json RCS Text with Scheduling
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3, //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Clicked",
        "Delivered",
        "Read",
        "Failed"
    ],
    "sendAt": "2025-02-08T05:59:04.000Z", //Mandatory. Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). max can be upto 7 days
    "expireAt": "2025-02-08T06:57:04.000Z", //Mandatory. Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.
    "content": {
        "type": "text", //Mandatory. Mention the type of RCS message type
        "text": "This is the message reagrding $(rcs_parameter1).  Reply Yes or No." //Mandatory. Contains the RCS message content.
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //Optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //Optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

| Parameter | Type   | Mandatory | Description                                                                                                                                 |
| :-------- | :----- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| sendAt    | string | yes       | Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). |
| expireAt  | string | yes       | Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.              |

### RCS Template

```json RCS Template
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "template": {
        "id": "{{rcsTemplateId}}" //Mandatory. Represents the unique identifier for a template, as displayed in the Templates section under Tools in the Connect console.
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //Optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //Optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

Following are the parameters required for sending message using RCS Template:

| Parameter | Type   | Mandatory | Description                                                                                                                |
| :-------- | :----- | :-------- | :------------------------------------------------------------------------------------------------------------------------- |
| carrierId | string | no        | carrier id of the mobile number given above can be passed to skip carrier lookup                                           |
| template  | string |           | JSON object                                                                                                                |
| id        | string |           | Represents the unique identifier for a template, as displayed in the Templates section under Tools in the Connect console. |

### RCS File

```json RCS File
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset. 
    "to": [	
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "options": {
        "smsFallback": true,
        "smsSenderId": "{{senderid}}",
        "text": "fallback text"
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": {
        "type": "media", //Mandatory
        "mediaContentUrl": "https://asset.com/asset.jpg", //Mandatory. Publicly accessible direct media Url.
        "fileSize": 120534 //Optional. File size in KB, of the media.
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
    }
}
```

Following are the parameters required for sending message using RCS File:

| Parameter       | Type   | Mandatory            | Description                                                                    |
| :-------------- | :----- | :------------------- | :----------------------------------------------------------------------------- |
| type            | string | yes                  | Used for specifying the message content type. The acceptable value is 'media'. |
| mediaContentUrl | string | yes, if type = media | a publicly accessible direct media Url ending in the attachment mimeType       |
| fileSize        | int    | No                   | File size in KB, of the media                                                  |

### RCS File with Suggestions

```json RCS File with Suggestions
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. 
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "options": {
        "smsFallback": true,
        "smsSenderId": "{{senderid}}",
        "text": "fallback text"
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": {
        "type": "media", //Mandatory
        "mediaContentUrl": "https://asset.com/asset.jpg", //Mandatory. Publicly accessible direct media Url.
        "fileSize": 120534, //Optional, file size in KB, of the media
        "suggestions": [
            {
                "type": "reply", //Mandatory if this suggestion type is used. 
                "displayText": "", //Mandatory. Text displayed so that user can easily respond
                "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
            },
            {
                "type": "viewLocation", //Mandatory if this suggestion type is used.
                "address": "", // Optional. Address of the coordinates mentioned
                "displayText": "", // Mandatory
                "latitude": 43.649269, //Mandatory, latitude of the location
                "longitude": -79.378423, //Mandatory, longitude of the location
                "postbackData": "" //Optional, Preconfigured response to the display text selected by the user.
            },
            {
                "type": "shareLocation", //Mandatory if this suggestion type is used.
                "displayText": "", // Mandatory
                "postbackData": "" // Optional
            },
            {
                "type": "openUrl", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "url": "https://www.domain.com", //Mandatory, The URL to which the user will be redirected upon clicking on openURL.
                "postbackData": "" //Optional
            },
            {
                "type": "calendarEvent", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "startTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, Start timestamp of the event in ISO date time format 8601.
                "endTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, End timestamp of the event in ISO date time format 8601.
                "meetingTitle": "", //Mandatory, Meeting title of the calendar event.
                "meetingDescription": "", //Optional
                "postbackData": "" //Optional
            },
            {
                "type": "dialPhone", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "phone": "", //Mandatory, Configured phone number to dial
                "postbackData": "" //Optional
            }
        ]
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

Following are the parameters required for sending message using RCS File with Suggestions:

| Parameter   | Type   | Mandatory | Description                                                                                                                                    |
| :---------- | :----- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| suggestions | string | no        | For more information about suggestions, refer [suggestions](https://developers.webexconnect.io/reference/rcs-api#suggestions-object)  section. |

### RCS File with Scheduling

```json RCS File with Scheduling
{
	"channel": "rcs", //Mandatory. 
	"from": "{{rcsAppId}}", //Mandatory. 
	"to": [
		{
			"msisdn": [
				"{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
			],
			"correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
		}
	],
	"options": { //Optional.
		"smsFallback": true, //Optional
		"smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
		"text": "fallback text", //Mandatory if smsFallback is true, else optional
		"carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
	},
	"requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
		"Sent",
		"Delivered",
		"Read",
		"Failed"
	],
	"sendAt": "2025-02-08T05:59:04.000Z", //Mandatory. Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). max can be upto 7 days
	"expireAt": "2025-02-08T06:57:04.000Z", //Mandatory. Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.
	"content": {
		"type": "media", //Mandatory
		"mediaContentUrl": "https://asset.com/asset.jpg", //Mandatory. Publicly accessible direct media Url.
		"fileSize": 120534, //Optional, file size in KB, of the media
		"suggestions": [
			{
				"type": "reply", //Mandatory if this suggestion type is used. 
				"displayText": "", //Mandatory. Text displayed so that user can easily respond
				"postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
			},
			{
				"type": "viewLocation", //Mandatory if this suggestion type is used.
				"address": "", // Optional. Address of the coordinates mentioned
				"displayText": "", // Mandatory
				"latitude": 43.649269, //Mandatory, latitude of the location
				"longitude": -79.378423, //Mandatory, longitude of the location
				"postbackData": "" //Optional, Preconfigured response to the display text selected by the user.
			},
			{
				"type": "shareLocation", //Mandatory if this suggestion type is used.
				"displayText": "", // Mandatory
				"postbackData": "" // Optional
			},
			{
				"type": "openUrl", //Mandatory if this suggestion type is used.
				"displayText": "", //Mandatory
				"url": "https://www.domain.com", //Mandatory, The URL to which the user will be redirected upon clicking on openURL.
				"postbackData": "" //Optional
			},
			{
				"type": "calendarEvent", //Mandatory if this suggestion type is used.
				"displayText": "", //Mandatory
				"startTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, Start timestamp of the event in ISO date time format 8601.
				"endTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, End timestamp of the event in ISO date time format 8601.
				"meetingTitle": "", //Mandatory, Meeting title of the calendar event.
				"meetingDescription": "", //Optional
				"postbackData": "" //Optional
			},
			{
				"type": "dialPhone", //Mandatory if this suggestion type is used.
				"displayText": "", //Mandatory
				"phone": "", //Mandatory, Configured phone number to dial
				"postbackData": "" //Optional
			}
		]
	},
	"callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyUrl": "", //Optional.
  "notifyUrlAuthId": "TNPXXXT09U", //Optional.
	"contactPolicy": { //Optional.
		"contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
		"channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
		"channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
	}
}
```

Following are the parameters required for sending message using RCS File with Scheduling:

| Parameter | Type   | Mandatory | Description                                                                                                                                 |
| :-------- | :----- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| sendAt    | string | yes       | Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). |
| expireAt  | string | yes       | Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.              |

### RCS Rich Card

```json RCS Rich Card
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": {
        "type": "standalone",
        "richCard": {
            "title": "", //Mandatory. Title of the message card of the respective card section.
            "description": "", //Optional. Indicates the text content of the message.
            "orientation": "", //Mandatory, The orientation of the image that is being sent, can be `HORIZONTAL` or `VERTICAL`.
            "thumbnailAlignment": "", //Mandatory, alignment of the thumbnail can be `LEFT` or `RIGHT`.
            "media": {
                "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                "height": "", //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                "filesize": 1 //Optional. File size in KB of the media to be displayed.
            },
            "thumbnail": {
                "url": "https://asset.com/asset.gif", //Mandatory. Publicly accessible direct media Url.
                "fileSize": 12864, //Optional. File size in KB of the media to be displayed.
                "height": "MEDIUM", //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                "contentType": "image/gif", //Optional.
                "description": "" //Optional. Indicates the text content of the thumbnail.
            }
        }
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //OPtional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

Following are the parameters required for sending message using RCS Rich Card:

| parameter          | type        | mandatory                 | description                                                                                                      |
| :----------------- | :---------- | :------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| carrierId          | string      | no                        | Carrier id of the mobile number given above can be passed to skip carrier lookup                                 |
| type               | string      | yes                       | Used for specifying the message content type. The acceptable value is 'standalone'.                              |
| richCard           | JSONObject  | yes, if type = standalone | A JSON object containing rich card data and suggestions                                                          |
| title              | string      | yes                       | Title of the message or content                                                                                  |
| description        | string      | no                        | It indicates the content of the message                                                                          |
| orientation        | string      | yes                       | The orientation of the image that is being sent. The accepatable values are 'HORIZONTALacceptable' or 'VERTICAL' |
| thumbnailAlignment | string      | yes                       | The alignment of the thumbnail. The accepatable values are 'LEFT' or 'RIGHT'.                                    |
| media              | JSON Object | yes                       | Media includes images, video, or .gif file messages.                                                             |
| url                | string      | yes                       | Publicly accessible direct media url.                                                                            |
| filesize           | int         | No                        | The size of the media file in KB.                                                                                |
| height             | string      | yes                       | The height of the media file. The acceptable values are"SHORT/MEDIUM/TALL".                                      |

### RCS Rich Card with Suggestions

```json RCS Rich Card with Suggestions
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": {
        "type": "standalone",
        "richCard": {
            "title": "", //Mandatory. Title of the message card of the respective card section.
            "description": "", //Optional. Indicates the text content of the message.
            "orientation": "", //Mandatory, The orientation of the image that is being sent, can be `HORIZONTAL` or `VERTICAL`.
            "thumbnailAlignment": "", //Mandatory, alignment of the thumbnail can be `LEFT` or `RIGHT`.
            "media": {
                "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                "height": "", //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                "filesize": 1 //Optional. File size in KB of the media to be displayed.
            },
            "thumbnail": {
                "url": "https://asset.com/asset.gif", //Mandatory. Publicly accessible direct media Url.
                "fileSize": 12864, //Optional. File size in KB of the media to be displayed.
                "height": "MEDIUM", //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                "contentType": "image/gif", //Optional.
                "description": "" //Optional. Indicates the text content of the thumbnail.
            },
            "suggestions": [
                {
                    "type": "reply", //Mandatory if this suggestion type is used. 
                    "displayText": "", //Mandatory. Text displayed so that user can easily respond
                    "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                },
                {
                    "type": "viewLocation", //Mandatory if this suggestion type is used.
                    "address": "", // Optional. Address of the coordinates mentioned
                    "displayText": "", // Mandatory
                    "latitude": 43.649269, //Mandatory, latitude of the location
                    "longitude": -79.378423, //Mandatory, longitude of the location
                    "postbackData": "" //Optional, Preconfigured response to the display text selected by the user.
                },
                {
                    "type": "shareLocation", //Mandatory if this suggestion type is used.
                    "displayText": "", // Mandatory
                    "postbackData": "" // Optional
                },
                {
                    "type": "openUrl", //Mandatory if this suggestion type is used.
                    "displayText": "", //Mandatory
                    "url": "https://www.domain.com", //Mandatory, The URL to which the user will be redirected upon clicking on openURL.
                    "postbackData": "" //Optional
                },
                {
                    "type": "calendarEvent", //Mandatory if this suggestion type is used.
                    "displayText": "", //Mandatory
                    "startTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, Start timestamp of the event in ISO date time format 8601.
                    "endTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, End timestamp of the event in ISO date time format 8601.
                    "meetingTitle": "", //Mandatory, Meeting title of the calendar event.
                    "meetingDescription": "", //Optional
                    "postbackData": "" //Optional
                },
                {
                    "type": "dialPhone", //Mandatory if this suggestion type is used.
                    "displayText": "", //Mandatory
                    "phone": "", //Mandatory, Configured phone number to dial
                    "postbackData": "" //Optional
                }
            ]
        }
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //OPtional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

| parameter   | type       | mandatory | description                                                                                                                                    |
| :---------- | :--------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| carrierId   | string     | no        | Carrier id of the mobile number given above can be passed to skip carrier lookup                                                               |
| suggestions | JSON Array | no        | For more information about suggestions, refer [suggestions](https://developers.webexconnect.io/reference/rcs-api#suggestions-object)  section. |

### RCS Rich Card with Scheduling

```json RCS Rich Card with Scheduling
{
	"channel": "rcs", //Mandatory. 
	"from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset.
	"to": [ //Mandatory section.
		{
			"msisdn": [
				"{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
			],
			"substitutions": { //Optional. Applicable only for text content type.
				"{{rcs_parameter1}}": "{{rcs_value1}}"
			},
			"correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
		}
	],
	"substitutions": { //Optional. Applicable only for text content type.
		"{{rcs_parameter1}}": "{{rcs_value1}}"
	},
	"options": { //Optional.
		"smsFallback": true, //Optional
		"smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
		"text": "fallback text", //Mandatory if smsFallback is true, else optional
		"carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
	},
	"requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
		"Sent",
		"Delivered",
		"Read",
		"Failed"
	],
	"sendAt": "2025-02-08T05:59:04.000Z", //Mandatory. Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). max can be upto 7 days
	"expireAt": "2025-02-08T06:57:04.000Z", //Mandatory. Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.
	"content": {
		"type": "standalone",
		"richCard": {
			"title": "", //Mandatory. Title of the message card of the respective card section.
			"description": "", //Optional. Indicates the text content of the message.
			"orientation": "", //Mandatory, The orientation of the image that is being sent, can be `HORIZONTAL` or `VERTICAL`.
			"thumbnailAlignment": "", //Mandatory, alignment of the thumbnail can be `LEFT` or `RIGHT`.
			"media": {
				"url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
				"height": "", //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
				"filesize": 1 //Optional. File size in KB of the media to be displayed.
			},
			"thumbnail": {
				"url": "https://asset.com/asset.gif", //Mandatory. Publicly accessible direct media Url.
				"fileSize": 12864, //Optional. File size in KB of the media to be displayed.
				"height": "MEDIUM", //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
				"contentType": "image/gif", //Optional.
				"description": "" //Optional. Indicates the text content of the thumbnail.
			}
		}
	},
	"callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyUrl": "", //Optional.
  "notifyUrlAuthId": "TNPXXXT09U", //Optional.
	"contactPolicy": { //OPtional.
		"contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
		"channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
		"channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
	}
}
```

Following are the parameters required for sending messages using RCS Rich Card with Scheduling:

| parameter | type   | mandatory | description                                                                                                                                 |
| :-------- | :----- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| sendAt    | string | yes       | Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). |
| expireAt  | string | yes       | Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.              |

### RCS Carousel

```json RCS Carousel
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset. 
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": { // Mandatory. For carousel, two cards are mandatory.
        "type": "carousel",
        "width": "MEDIUM", //Mandatory. Indicates the width of the carousel cards. Supported values are `SMALL`/`MEDIUM`.
        "cards": [
            {
                "title": "", //Mandatory. Title of the message card of the respective card section.
                "description": "", //Optional. Indicates the text content of the message.
                "media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
                    "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                    "fileSize": 12053, //Optional. File size in KB of the media to be displayed.
                    "height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                },
                "suggestions": [
                    {
                        "type": "reply", //Mandatory. If this suggestion type is used.
                        "displayText": "", //Mandatory. Text displayed so that user can easily respond.
                        "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                    }
                ]
            },
            {
                "title": "", //Mandatory. Title of the message card of the respective card section.
                "description": "", //Optional. Indicates the text content of the message.
                "media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
                    "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                    "fileSize": 15860, //Optional. File size in KB of the media to be displayed.
                    "height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                },
                "suggestions": [
                    {
                        "type": "reply", //Mandatory. If this suggestion type is used.
                        "displayText": "", //Mandatory. Text displayed so that user can easily respond
                        "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                    }
                ]
            },
            {
                "title": "", //Mandatory. Title of the message card of the respective card section.
                "description": "", //Optional. Indicates the text content of the message.
                "media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
                    "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                    "fileSize": 15860, //Optional. File size in KB of the media to be displayed.
                    "height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                },
                "suggestions": [
                    {
                        "type": "reply", //Mandatory. If this suggestion type is used.
                        "displayText": "", //Mandatory. Text displayed so that user can easily respond.
                        "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                    }
                ]
            }
        ]
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

Following are the parameters required for sending messages using RCS Carousel:

| parameter   | type        | mandatory               | description                                                                                                                                    |
| :---------- | :---------- | :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| type        | string      | yes                     | Used for specifying the message content type.The acceptable value is 'carousel'.                                                               |
| width       | string      | yes, if type = carousel | A parameter that indicates the width of carousel cards. Supported values are `SMALL`/`MEDIUM`                                                  |
| cards       | JSONArray   | yes, if type = carousel | A JSON array containing carousel card objects and their suggestions                                                                            |
| title       | string      | yes                     | Title of the message card of the respective card                                                                                               |
| description | string      | no                      | It indicates the text content of the message                                                                                                   |
| media       | JSON Object | yes                     | Media includes images, videos, or .gif files                                                                                                   |
| url         | string      | yes                     | Publicly accessible direct media url.                                                                                                          |
| filesize    | int         | No                      | The size of the media file in KB.                                                                                                              |
| height      | string      | yes                     | The height of the media file. The acceptable values are"SHORT/MEDIUM/TALL".                                                                    |
| suggestions | JSON Array  | No                      | For more information about suggestions, refer [suggestions](https://developers.webexconnect.io/reference/rcs-api#suggestions-object)  section. |

### RCS Carousel with Suggestions

```json RCS Carousel with Suggestions
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset. 
    "to": [ //Mandatory section.
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "substitutions": { //Optional. Applicable only for text content type.
                "{{rcs_parameter1}}": "{{rcs_value1}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. Applicable only for text content type.
        "{{rcs_parameter1}}": "{{rcs_value1}}"
    },
    "options": { //Optional.
        "smsFallback": true, //Optional
        "smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
        "text": "fallback text", //Mandatory if smsFallback is true, else optional
        "carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
    },
    "requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
        "Sent",
        "Delivered",
        "Read",
        "Failed"
    ],
    "content": { // Mandatory. For carousel, two cards are mandatory.
        "type": "carousel",
        "width": "MEDIUM", //Mandatory. Indicates the width of the carousel cards. Supported values are `SMALL`/`MEDIUM`.
        "cards": [
            {
                "title": "", //Mandatory. Title of the message card of the respective card section.
                "description": "", //Optional. Indicates the text content of the message.
                "media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
                    "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                    "fileSize": 12053, //Optional. File size in KB of the media to be displayed.
                    "height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                },
                "suggestions": [
                    {
                        "type": "reply", //Mandatory. If this suggestion type is used.
                        "displayText": "", //Mandatory. Text displayed so that user can easily respond.
                        "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                    }
                ]
            },
            {
                "title": "", //Mandatory. Title of the message card of the respective card section.
                "description": "", //Optional. Indicates the text content of the message.
                "media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
                    "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                    "fileSize": 15860, //Optional. File size in KB of the media to be displayed.
                    "height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                },
                "suggestions": [
                    {
                        "type": "reply", //Mandatory. If this suggestion type is used.
                        "displayText": "", //Mandatory. Text displayed so that user can easily respond
                        "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                    }
                ]
            },
            {
                "title": "", //Mandatory. Title of the message card of the respective card section.
                "description": "", //Optional. Indicates the text content of the message.
                "media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
                    "url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
                    "fileSize": 15860, //Optional. File size in KB of the media to be displayed.
                    "height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
                },
                "suggestions": [
                    {
                        "type": "reply", //Mandatory. If this suggestion type is used.
                        "displayText": "", //Mandatory. Text displayed so that user can easily respond.
                        "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
                    }
                ]
            }
        ],
        "suggestions": [
            {
                "type": "reply", //Mandatory if this suggestion type is used. 
                "displayText": "", //Mandatory. Text displayed so that user can easily respond
                "postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
            },
            {
                "type": "viewLocation", //Mandatory if this suggestion type is used.
                "address": "", // Optional. Address of the coordinates mentioned
                "displayText": "", // Mandatory
                "latitude": 43.649269, //Mandatory, latitude of the location
                "longitude": -79.378423, //Mandatory, longitude of the location
                "postbackData": "" //Optional, Preconfigured response to the display text selected by the user.
            },
            {
                "type": "shareLocation", //Mandatory if this suggestion type is used.
                "displayText": "", // Mandatory
                "postbackData": "" // Optional
            },
            {
                "type": "openUrl", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "url": "https://www.domain.com", //Mandatory, The URL to which the user will be redirected upon clicking on openURL.
                "postbackData": "" //Optional
            },
            {
                "type": "calendarEvent", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "startTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, Start timestamp of the event in ISO date time format 8601.
                "endTime": "YYYY-MM-DDTHH:MM:SSZ", //Mandatory, End timestamp of the event in ISO date time format 8601.
                "meetingTitle": "", //Mandatory, Meeting title of the calendar event.
                "meetingDescription": "", //Optional
                "postbackData": "" //Optional
            },
            {
                "type": "dialPhone", //Mandatory if this suggestion type is used.
                "displayText": "", //Mandatory
                "phone": "", //Mandatory, Configured phone number to dial
                "postbackData": "" //Optional
            }
        ]
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

Following are the parameters required for sending messages using RCS Carousel with Suggestions:

| parameter   | type       | mandatory | description                                                                                                                                    |
| :---------- | :--------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| carrierId   | string     | no        | Carrier id of the mobile number given above can be passed to skip carrier lookup                                                               |
| suggestions | JSON Array | no        | For more information about suggestions, refer [suggestions](https://developers.webexconnect.io/reference/rcs-api#suggestions-object)  section. |

### RCS Carousel with Scheduling

```json RCS Carousel with Scheduling
{
	"channel": "rcs", //Mandatory. 
	"from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset. 
	"to": [ //Mandatory section.
		{
			"msisdn": [
				"{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
			],
			"substitutions": { //Optional. Applicable only for text content type.
				"{{rcs_parameter1}}": "{{rcs_value1}}"
			},
			"correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
		}
	],
	"substitutions": { //Optional. Applicable only for text content type.
		"{{rcs_parameter1}}": "{{rcs_value1}}"
	},
	"options": { //Optional.
		"smsFallback": true, //Optional
		"smsSenderId": "{{senderid}}", //Mandatory if smsFallback is true, else optional
		"text": "fallback text", //Mandatory if smsFallback is true, else optional
		"carrierId": 3 //Optional, carrier id of the mobile number given above can be passed to skip carrier lookup
	},
	"requestedReceipts": [ //Optional. A JSON array that can filter message delivery webhooks to the notifyUrl.
		"Sent",
		"Delivered",
		"Read",
		"Failed"
	],
	"sendAt": "2025-02-08T05:59:04.000Z", //Mandatory. Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). max can be upto 7 days
	"expireAt": "2025-02-08T06:57:04.000Z", //Mandatory. Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.
	"content": { // Mandatory. For carousel, two cards are mandatory.
		"type": "carousel",
		"width": "MEDIUM", //Mandatory. Indicates the width of the carousel cards. Supported values are `SMALL`/`MEDIUM`.
		"cards": [
			{
				"title": "", //Mandatory. Title of the message card of the respective card section.
				"description": "", //Optional. Indicates the text content of the message.
				"media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
					"url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
					"fileSize": 12053, //Optional. File size in KB of the media to be displayed.
					"height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
				},
				"suggestions": [
					{
						"type": "reply", //Mandatory. If this suggestion type is used.
						"displayText": "", //Mandatory. Text displayed so that user can easily respond.
						"postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
					}
				]
			},
			{
				"title": "", //Mandatory. Title of the message card of the respective card section.
				"description": "", //Optional. Indicates the text content of the message.
				"media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
					"url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
					"fileSize": 15860, //Optional. File size in KB of the media to be displayed.
					"height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
				},
				"suggestions": [
					{
						"type": "reply", //Mandatory. If this suggestion type is used.
						"displayText": "", //Mandatory. Text displayed so that user can easily respond
						"postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
					}
				]
			},
			{
				"title": "", //Mandatory. Title of the message card of the respective card section.
				"description": "", //Optional. Indicates the text content of the message.
				"media": { //Mandatory. Media includes details regarding images, videos, gif files etc.
					"url": "https://asset.com/asset.jpp", //Mandatory. Publicly accessible direct media Url.
					"fileSize": 15860, //Optional. File size in KB of the media to be displayed.
					"height": "MEDIUM" //Mandatory. Parameter that indicates the height of the media shared as  `SHORT`/`MEDIUM`/`TALL`.
				},
				"suggestions": [
					{
						"type": "reply", //Mandatory. If this suggestion type is used.
						"displayText": "", //Mandatory. Text displayed so that user can easily respond.
						"postbackData": "" //Optional. Preconfigured response to the display text selected by the user.
					}
				]
			}
		]
	},
	"callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyUrl": "", //Optional.
  "notifyUrlAuthId": "TNPXXXT09U", //Optional.
	"contactPolicy": { //Optional.
		"contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
		"channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
		"channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
	}
}
```

Following are the parameters required for sending messages using RCS Carousel with Scheduling:

| parameter | type   | mandatory | description                                                                                                                                 |
| :-------- | :----- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| sendAt    | string | yes       | Specifies the date and time at which the message should be sent. The format is : YYYY-MM-DDTHH:mm:ss.sssZ (e.g., 2024-12-17T15:40:04.000Z). |
| expireAt  | string | yes       | Defines the expiration time for the message, after which it will no longer be valid. The format is : YYYY-MM-DDTHH:mm:ss.sssZ.              |

Refer to the [Limits and Best Practices](https://help.webexconnect.io/docs/rcs-message-node#limits-and-best-practices) section for more information on Field/Element and their best practices.

Refer to the [Supported File Type for RCS Channel](https://help.webexconnect.io/docs/supported-file-types-for-channels#rcs)  section for more information on RCS file formats.

### RCS Typing Event

```json
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset. 
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "content": {
        "type": "agentEvent",
        "event": "IS_TYPING"
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

Following are the parameters required for sending message using RCS Typing:

| parameter | type   | mandatory                 | description                                                                         |
| :-------- | :----- | :------------------------ | :---------------------------------------------------------------------------------- |
| type      | string | yes                       | Used for specifying the message content type. The acceptable value is 'agentEvent'. |
| event     | string | yes, if type = agentEvent | A typing event is to be sent to the customer. The acceptable value is "IS_TYPING".  |

### RCS Read Event

```json
{
    "channel": "rcs", //Mandatory. 
    "from": "{{rcsAppId}}", //Mandatory. This is the app_id of the RCS asset. 
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended. Mobile number to which messages needs to be sent.
            ],
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "content": {
        "type": "agentEvent",
        "event": "READ",
        "messageId": "" //Mandatory. MessageId of the specific message.
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”.
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true”. 
    }
}
```

Following are the parameters required for sending message using RCS Read:

| parameter | type   | mandatory                 | description                                                                                       |
| :-------- | :----- | :------------------------ | :------------------------------------------------------------------------------------------------ |
| type      | string | yes                       | Used for specifying the message content type. The acceptable value is 'agentEvent'.               |
| event     | string | yes, if type = agentEvent | A reading event is to be sent to the customer. The acceptable value is "READ".                    |
| messageId | string |                           | MessageId of the specific message.Unique ID generated to record the messages sent using RCS read. |