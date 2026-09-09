> 📘 API Endpoint & Postman Collection
> 
> SMS channel is supported via Send SMS API v1, Send Message API v2, and Send Message API v1. Refer to the [SMS APIs](https://developers.webexconnect.io/reference/sms) section for information on which API is best suited for your use case.
> 
> API endpoint for it is:[https://{YourRegion}.webexconnect.io/v2/messages].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f)  for trying Send Message API v2.
> 
> **Authentication** 
> 
> Refer to the [API Authentication](https://developers.webexconnect.io/reference/authentication-2) section for information on API Authentication.

> 📘 API Response and Error Codes
> 
> The Send Message API v2 API is an asynchronous API. The HTTP response confirming acceptance of your request is sent as soon as you invoke the API. However, the subsequent request processing details are notified via the callback i.e., notify URL mentioned in your API request. For more information, refer to the [Channel-Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1) documentation.

## Request Body to Send SMS Using Send Message API v2

```json Send Message API v2
{
    "channel": "sms", //Mandatory. 
    "from": "{{from}}", //Mandatory. Country code with phone number but without '+' sign, or the short code/sender ID.
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended.
            ],
            "substitutions": { //Optional.
                "{{sms_parameter1}}": "{{sms_value1}}",
                "{{sms_parameter2}}": "{{sms_value2}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional.
        "{{sms_parameter3}}": "{{sms_value3}}",
        "{{sms_parameter4}}": "{{sms_value4}}"
    },
    "options": { //Optional.
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "requestedReceipts": [ //Optional.
        "SUBMITTED", 
        "SENT",//‘SENT’ is supported for legacy implementations and behaves the same as ‘SUBMITTED’. We recommend using ‘SUBMITTED’.
        "DELIVERED",
        "CLICKED",//Applicable only when shortenLinks and trackClicks feature is being used.
        "FAILED"
    ],
    "content": {
        "type": "text", //Mandatory. 
        "text": "This is sample content" //Mandatory.
    },
    "sendAt": "{{DateTimeinUTC}}", //Optional. For e.g., YYYY-MM-DDThh:mm:ss.sZ
    "expireAt": "{{DateTimeinUTC}}", //Optional. For e.g., YYYY-MM-DDThh:mm:ss.sZ
    "validity": "time period in seconds", //Optional. For e.g., 60 for 60 seconds
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional. 
    "contactPolicy": { //Optional.JSON Object to specify contact policy checks before sending the outbound SMS. 
        "contactPolicyGroup": "", //The GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional,assumed false if not specified. Set to true to require opt-in before sending the message. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
    }
}
```

## Send Message API v2 Body Parameters

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
    "0-3": "The value needs to be 'sms' when sending SMS messages.",
    "1-0": "from",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "SMS Sender ID, i.e., the long code, short code, or the Sender ID to be used for sending the message.",
    "2-0": "to",
    "2-1": "JSONArray",
    "2-2": "yes",
    "2-3": "An array of destination JSON objects that contain the mandatory destination msisdn, optional personalised substitutions, and correlationId for each destination object.",
    "3-0": "msisdn",
    "3-1": "JSONArray",
    "3-2": "yes",
    "3-3": "Phone number, i.e., msisdn to which the SMS has to be sent in E.164 format e.g., +44XXXXXXXXXX  \n  \n_Note: If +E.164 format is enabled for your tenant - all the numbers in the **to** field should follow the \"+E.164\" format.  \nThis format displays the number with a \"+\" followed by the country code and the phone number.  \n+E.164 format does not apply to the numbers in the **from** field._",
    "4-0": "correlationId",
    "4-1": "string",
    "4-2": "no",
    "4-3": "User defined ID that is assigned to an individual message for unique identification.",
    "5-0": "substitutions",
    "5-1": "JSONObject",
    "5-2": "no",
    "5-3": "List of key-value pairs for dynamic fields in the SMS message content. They are typically used for specifying the values for dynamic fields in an SMS template.",
    "6-0": "options",
    "6-1": "JSONObject",
    "6-2": "no",
    "6-3": "A JSON object that contains additional, SMS-specific options such as trackClicks, shortenLinks, and domain in the API. ",
    "7-0": "trackClicks",
    "7-1": "boolean",
    "7-2": "no",
    "7-3": "You can receive ‘CLICKED’ notifications for shorten links on your notifyUrl by enabling trackClicks. You can also receive them on your SMS webhook if the ‘Clicked’ option is selected.  \nThe ‘trackClicks’ option is set to ‘false’ by default.  \nClicked format available [SMS Outbound Webhook](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts)  page.",
    "8-0": "shortenLinks",
    "8-1": "boolean",
    "8-2": "no",
    "8-3": "When enabled, this shortens any HTTPS links in the message request's body. For more information, refer to [configure shortenLinks section](https://developers.webexconnect.io/reference/send-sms-message-api-v2#steps-for-configuring-branded--short-urls-for-smartlinks--shortenlinks-capability) . The expiry of the shortened URL is 180 days.",
    "9-0": "domain",
    "9-1": "string",
    "9-2": "yes",
    "9-3": "It is the domain configuration for shortening the links.  \n_Note: 'domain' is mandatory only when 'options' object is used in the payload._",
    "10-0": "tag1 and tag2",
    "10-1": "string",
    "10-2": "yes",
    "10-3": "The reporting tags are for tracking the shortened link's creates and clicks.",
    "11-0": "allowFallbackURL",
    "11-1": "string",
    "11-2": "yes",
    "11-3": "If true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.",
    "12-0": "requestedReceipts",
    "12-1": "JSONArray",
    "12-2": "no",
    "12-3": "A JSON array that can filter message delivery webhooks to the notifyUrl.  \n  \nCan contain one or more of the following:  \n\"SUBMITTED\"  \n\"SENT\" (Note: ‘SENT’ is supported for legacy implementations and behaves the same as ‘‘SUBMITTED’’. We recommend using ‘‘SUBMITTED\") ,  \n\"DELIVERED\",  \n\"CLICKED\",  \n\"FAILED\"  \nRefer to [Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks) for delivery receipt samples.",
    "13-0": "content",
    "13-1": "JSONObject",
    "13-2": "yes, if the template is not provided",
    "13-3": "It is the JSON object that contains mandatory parameters 'type' and 'text' for SMS channel. ",
    "14-0": "type",
    "14-1": "string",
    "14-2": "yes",
    "14-3": "Used for specifying the message content type. Acceptable values are: 'text' and 'unicode'.  \n  \nPlease note that 'text' supports many common special characters as per the SMS specification and is preferred where possible. Using 'unicode' enables the use of multi-byte encoding, which allows full character set and emoji support, but results in 2 or 3 times more SMS traffic than plain SMS text.",
    "15-0": "text",
    "15-1": "string",
    "15-2": "yes",
    "15-3": "The SMS message content. A maximum of 4000 characters can be supported. We recommend that you keep SMS messages below 450 characters for better deliverability and user experience.  \nTo include a new line within the content of an SMS message, insert the characters `\\n` at the desired location in your message text. The `\\n` sequence represents a line break and will cause the text following it to appear on a new line when the message is displayed.",
    "16-0": "sendAt",
    "16-1": "string",
    "16-2": "no",
    "16-3": "The timestamp for sending the message when scheduling ahead of time. You can schedule a message upto 7 days in advance.  \n  \nFor example, 2024-09-26T13:47:18.000Z - UTC ",
    "17-0": "expireAt",
    "17-1": "string",
    "17-2": "no",
    "17-3": "Timestamp post which the message has to be expired and not sent to the intended recipient, in case the Send SMS request is yet to be processed.You can set the expiry date up to 7 days in advance.  \n  \nFor example, 2024-09-26T13:47:18.000Z - UTC  \n_Note: The expireAt setting enforces message expiry at the system level. If an SMS arrives at Webex Connect after the specified expireAt time, the system will expire the message and will not forward it to the operator. This expiry process is managed internally by the system._",
    "18-0": "validity",
    "18-1": "string",
    "18-2": "no",
    "18-3": "The time period is in seconds. E.g., 60 for sixty seconds.  \n  \nOnly one of 'expireAt' or 'validity' should be sent in the request. The request will not be accepted if both values are present in the payload.  \n  \nIf both, 'sendAt' and 'validity parameters' are present in the same request, the validity time period will be added to the 'sendAt time' to decide the expiry time.  \n  \n_Note: Message validity now extends to the operator’s network, ensuring expiration at both the system and carrier levels. You can set message validity for up to 72 hours. For example, if you set validity to 2 days, the carrier will attempt delivery for up to 2 days. If the recipient’s phone is off for 1 day and then turns on, the carrier will deliver the message. If the phone remains off for more than 2 days, the message will expire and the carrier will not deliver it. This feature ensures that carriers enforce the specified validity period._",
    "19-0": "callbackData",
    "19-1": "string",
    "19-2": "no",
    "19-3": "A string that is returned with each outbound webhook for the message (delivery, failed, etc.). The maximum number of characters allowed in callbackData including any spaces is 2000.",
    "20-0": "notifyUrl",
    "20-1": "string",
    "20-2": "no",
    "20-3": "If provided, updates related to the delivery status of this message will be posted to this URL. Refer to [SMS Delivery Receipts](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts) page for notification samples.",
    "21-0": "notifyUrlAuthId ",
    "21-1": "string",
    "21-2": "no",
    "21-3": "Unique authentication ID.",
    "22-0": "template",
    "22-1": "JSONObject",
    "22-2": "yes, if content is not provided",
    "22-3": "This is a JSON object which contains the mandatory 'ID' parameter. The value for the 'ID' parameter is the unique template ID of the configured SMS template on the UI.",
    "23-0": "contactPolicy",
    "23-1": "JSONObject",
    "23-2": "no",
    "23-3": "JSON Object to specify contact policy checks before sending the outbound SMS. Contact Policy App should be configured to use this feature as a prerequisite.",
    "24-0": "contactPolicyGroup",
    "24-1": "string",
    "24-2": "yes (if you want to apply Contact Policy checks before sending the message)",
    "24-3": "The GroupID is to be applied. It is required if any of the following options are included and set to true.",
    "25-0": "channelCheckConsent",
    "25-1": "boolean",
    "25-2": "no",
    "25-3": "Optional, assumed false if not specified. Set to true to require opt-in before sending the message. At least one of the “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”.",
    "26-0": "channelApplyFrequencyCap",
    "26-1": "boolean",
    "26-2": "no",
    "26-3": "Optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”."
  },
  "cols": 4,
  "rows": 27,
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

### Sending SMS with Scheduler

```json Sending SMS with Scheduler
{
    "channel": "sms", //Mandatory. 
    "from": "{{from}}", //Mandatory. E.164 format required/recommended.
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended.
            ],
            "substitutions": { //Optional.
                "{{sms_parameter1}}": "{{sms_value1}}",
                "{{sms_parameter2}}": "{{sms_value2}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional.
        "{{sms_parameter3}}": "{{sms_value3}}",
        "{{sms_parameter4}}": "{{sms_value4}}"
    },
    "options": { //Optional.
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "requestedReceipts": [ //Optional.
        "SUBMITTED",
        "SENT", //‘SENT’ is supported for legacy implementations and behaves the same as ‘SUBMITTED’. We recommend using ‘SUBMITTED’.
        "DELIVERED",
        "CLICKED", //Applicable only when shortenLinks and trackClicks feature is being used.
        "FAILED"
    ],
    "batchId": "{{batchId}}",
    "sendAt": "{{TimeinUTC}}", //Optional. For e.g., YYYY-MM-DDThh:mm:ss.sZ
    "expireAt": "{{TimeinUTC}}", //Optional. For e.g., YYYY-MM-DDThh:mm:ss.sZ
    "validity": "time period in seconds", //Optional. For e.g., 60 for 60 seconds
    "content": {
        "type": "text", //Mandatory. 
        "text": "Hi schedule request in new staging with short domain https://www.google.com" //Mandatory. 
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.JSON Object to specify contact policy checks before sending the outbound SMS. 
        "contactPolicyGroup": "", //The GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional,assumed false if not specified. Set to true to require opt-in before sending the message. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
    }
}
```

Following are the parameters required for sending a message using the scheduler: 

| parameter | type   | mandatory | description                                    |
| :-------- | :----- | :-------- | :--------------------------------------------- |
| batchId   | string | yes       | Unique batch ID of the SMS messages scheduled. |

### Sending SMS Using Templates

```json Sending SMS Using Templates
{
    "channel": "sms", //Mandatory. 
    "from": "{{from}}", //Mandatory. Country code with phone number but without '+' sign, or the short code/sender ID.
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended.
            ],
            "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
            "substitutions": { //Optional.
                "{{sms_parameter1}}": "{{sms_value1}}"
            }
        }
    ],
    "substitutions": { //Optional.
        "{{sms_parameter2}}": "{{sms_value2}}"
    },
    "requestedReceipts": [ //Optional.
        "SUBMITTED",
        "SENT", //‘SENT’ is supported for legacy implementations and behaves the same as ‘SUBMITTED’. We recommend using ‘SUBMITTED’.
        "DELIVERED",
        "CLICKED", //Applicable only when shortenLinks and trackClicks feature is being used.
        "FAILED"
    ],
    "template": {
        "id": "5S2XXXXFNR"
    },
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
   "notifyUrl": "", //Optional.
   "notifyUrlAuthId": "TNPXXXT09U", //Optional.
   "contactPolicy": { //Optional.JSON Object to specify contact policy checks before sending the outbound SMS. 
        "contactPolicyGroup": "", //The GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional,assumed false if not specified. Set to true to require opt-in before sending the message. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
    }
}
```

Following are the parameters required for sending message using templates: 

| parameter | type       | mandatory                       | description                                                                                                                                                             |
| :-------- | :--------- | :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| template  | JSONObject | yes, if content is not provided | This is a JSON object which contains the mandatory 'ID' parameter. The value for the 'ID' parameter is the unique template ID of the configured SMS template on the UI. |
| id        | string     | yes (when using templates)      | Unique templated ID of the SMS template configured on the UI.                                                                                                           |

### Sending SMS with Smartlinks

```json Sending SMS with Smartlinks
{
    "channel": "sms", //Mandatory. 
    "from": "{{from}}", //Mandatory. 
    "to": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. E.164 format required/recommended.
            ],
            "substitutions": { //Optional.
                "{{sms_parameter1}}": "{{sms_value1}}",
                "{{sms_parameter2}}": "{{sms_value2}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional.
        "{{sms_parameter3}}": "{{sms_value3}}",
        "{{sms_parameter4}}": "{{sms_value4}}"
    },
    "smartlinks": [
        {
            "smartlinkId": {{smartlinkID}},
            "validity": 1
        }
    ],
    "options": { //Optional.
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "requestedReceipts": [ //Optional.
        "SUBMITTED",
        "SENT", //‘SENT’ is supported for legacy implementations and behaves the same as ‘SUBMITTED’. We recommend using ‘SUBMITTED’.
        "DELIVERED",
        "CLICKED", //Applicable only when shortenLinks and trackClicks feature is being used.
        "FAILED"
    ],
    "content": {
        "type": "text", //Mandatory. 
        "text": "Hi {{smartlink_4371}}, API V2 with smartlink" //Mandatory. 
    },
    "sendAt": "{{TimeinUTC}}", //Optional. For e.g., YYYY-MM-DDThh:mm:ss.sZ
    "expireAt": "{{TimeinUTC}}", //Optional. For e.g., YYYY-MM-DDThh:mm:ss.sZ
    "validity": "time period in seconds", //Optional. For e.g., 60 for 60 seconds
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional
    "contactPolicy": { //Optional.JSON Object to specify contact policy checks before sending the outbound SMS. 
        "contactPolicyGroup": "", //The GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional,assumed false if not specified. Set to true to require opt-in before sending the message. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
    }
}
```

The following are the parameters required to send messages using Smartlink. 'Smartlinks' need to be mentioned in the SMS text field, as shown in the payload sample above.

| parameter   | type       | mandatory                          | description                                                                                               |
| :---------- | :--------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| smartlinks  | JSONObject | yes, if you want to use smartlinks | This is a JSON object which contains the mandatory fields required for using smartlinks.                  |
| smartlinkId | string     | yes                                | Unique smartlink ID. This value is generated within <<prodname>>platform, when you configure a smartlink. |
| validity    | string     | yes                                | Validity of the smartlink                                                                                 |

<ShortenLinks />