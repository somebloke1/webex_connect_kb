# Send Message API v2

Source: https://developers.webexconnect.io/reference/send-sms-message-api-v2
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:35:07+00:00

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



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channel | string | yes | The value needs to be 'sms' when sending SMS messages. |
| from | string | yes | SMS Sender ID, i.e., the long code, short code, or the Sender ID to be used for sending the message. |
| to | JSONArray | yes | An array of destination JSON objects that contain the mandatory destination msisdn, optional personalised substitutions, and correlationId for each destination object. |
| msisdn | JSONArray | yes | Phone number, i.e., msisdn to which the SMS has to be sent in E.164 format e.g., +44XXXXXXXXXX  <br>  <br>_Note: If +E.164 format is enabled for your tenant - all the numbers in the **to** field should follow the "+E.164" format.  <br>This format displays the number with a "+" followed by the country code and the phone number.  <br>+E.164 format does not apply to the numbers in the **from** field._ |
| correlationId | string | no | User defined ID that is assigned to an individual message for unique identification. |
| substitutions | JSONObject | no | List of key-value pairs for dynamic fields in the SMS message content. They are typically used for specifying the values for dynamic fields in an SMS template. |
| options | JSONObject | no | A JSON object that contains additional, SMS-specific options such as trackClicks, shortenLinks, and domain in the API.  |
| trackClicks | boolean | no | You can receive ‘CLICKED’ notifications for shorten links on your notifyUrl by enabling trackClicks. You can also receive them on your SMS webhook if the ‘Clicked’ option is selected.  <br>The ‘trackClicks’ option is set to ‘false’ by default.  <br>Clicked format available [SMS Outbound Webhook](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts)  page. |
| shortenLinks | boolean | no | When enabled, this shortens any HTTPS links in the message request's body. For more information, refer to [configure shortenLinks section](https://developers.webexconnect.io/reference/send-sms-message-api-v2#steps-for-configuring-branded--short-urls-for-smartlinks--shortenlinks-capability) . The expiry of the shortened URL is 180 days. |
| domain | string | yes | It is the domain configuration for shortening the links.  <br>_Note: 'domain' is mandatory only when 'options' object is used in the payload._ |
| tag1 and tag2 | string | yes | The reporting tags are for tracking the shortened link's creates and clicks. |
| allowFallbackURL | string | yes | If true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link. |
| requestedReceipts | JSONArray | no | A JSON array that can filter message delivery webhooks to the notifyUrl.  <br>  <br>Can contain one or more of the following:  <br>"SUBMITTED"  <br>"SENT" (Note: ‘SENT’ is supported for legacy implementations and behaves the same as ‘‘SUBMITTED’’. We recommend using ‘‘SUBMITTED") ,  <br>"DELIVERED",  <br>"CLICKED",  <br>"FAILED"  <br>Refer to [Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks) for delivery receipt samples. |
| content | JSONObject | yes, if the template is not provided | It is the JSON object that contains mandatory parameters 'type' and 'text' for SMS channel.  |
| type | string | yes | Used for specifying the message content type. Acceptable values are: 'text' and 'unicode'.  <br>  <br>Please note that 'text' supports many common special characters as per the SMS specification and is preferred where possible. Using 'unicode' enables the use of multi-byte encoding, which allows full character set and emoji support, but results in 2 or 3 times more SMS traffic than plain SMS text. |
| text | string | yes | The SMS message content. A maximum of 4000 characters can be supported. We recommend that you keep SMS messages below 450 characters for better deliverability and user experience.  <br>To include a new line within the content of an SMS message, insert the characters `\n` at the desired location in your message text. The `\n` sequence represents a line break and will cause the text following it to appear on a new line when the message is displayed. |
| sendAt | string | no | The timestamp for sending the message when scheduling ahead of time. You can schedule a message upto 7 days in advance.  <br>  <br>For example, 2024-09-26T13:47:18.000Z - UTC  |
| expireAt | string | no | Timestamp post which the message has to be expired and not sent to the intended recipient, in case the Send SMS request is yet to be processed.You can set the expiry date up to 7 days in advance.  <br>  <br>For example, 2024-09-26T13:47:18.000Z - UTC  <br>_Note: The expireAt setting enforces message expiry at the system level. If an SMS arrives at Webex Connect after the specified expireAt time, the system will expire the message and will not forward it to the operator. This expiry process is managed internally by the system._ |
| validity | string | no | The time period is in seconds. E.g., 60 for sixty seconds.  <br>  <br>Only one of 'expireAt' or 'validity' should be sent in the request. The request will not be accepted if both values are present in the payload.  <br>  <br>If both, 'sendAt' and 'validity parameters' are present in the same request, the validity time period will be added to the 'sendAt time' to decide the expiry time.  <br>  <br>_Note: Message validity now extends to the operator’s network, ensuring expiration at both the system and carrier levels. You can set message validity for up to 72 hours. For example, if you set validity to 2 days, the carrier will attempt delivery for up to 2 days. If the recipient’s phone is off for 1 day and then turns on, the carrier will deliver the message. If the phone remains off for more than 2 days, the message will expire and the carrier will not deliver it. This feature ensures that carriers enforce the specified validity period._ |
| callbackData | string | no | A string that is returned with each outbound webhook for the message (delivery, failed, etc.). The maximum number of characters allowed in callbackData including any spaces is 2000. |
| notifyUrl | string | no | If provided, updates related to the delivery status of this message will be posted to this URL. Refer to [SMS Delivery Receipts](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts) page for notification samples. |
| notifyUrlAuthId  | string | no | Unique authentication ID. |
| template | JSONObject | yes, if content is not provided | This is a JSON object which contains the mandatory 'ID' parameter. The value for the 'ID' parameter is the unique template ID of the configured SMS template on the UI. |
| contactPolicy | JSONObject | no | JSON Object to specify contact policy checks before sending the outbound SMS. Contact Policy App should be configured to use this feature as a prerequisite. |
| contactPolicyGroup | string | yes (if you want to apply Contact Policy checks before sending the message) | The GroupID is to be applied. It is required if any of the following options are included and set to true. |
| channelCheckConsent | boolean | no | Optional, assumed false if not specified. Set to true to require opt-in before sending the message. At least one of the “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”. |
| channelApplyFrequencyCap | boolean | no | Optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”. |




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
| smartlinkId | string     | yes                                | Unique smartlink ID. This value is generated within Webex Connectplatform, when you configure a smartlink. |
| validity    | string     | yes                                | Validity of the smartlink                                                                                 |

<ShortenLinks />

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "post",
  "url": "/messages",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": " {\n        \"requestTimestamp\": \"2019-10-04T10:42:27.728Z\",\n        \"messageId\": \"2002fcc6-d500-43e8-b3ab-8f86f15891cb\",\n        \"correlationId\": \"na1b2b1i1\",\n        \"status\": \"queued\"\n }",
        "language": "json",
        "status": 201
      },
      {
        "name": "",
        "code": "{\"code\":\"7004\",\"message\":\"Invalid parameter - sendAt\"}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [
    {
      "name": "Content-Type",
      "type": "string",
      "enumValues": "",
      "default": "application/json",
      "desc": "",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "66b2593eeb24730052754c25",
      "id": "66b2593eeb24730052754c25"
    },
    {
      "name": "key",
      "type": "string",
      "enumValues": "",
      "default": "<Service Key>",
      "desc": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your Webex Connect tenant.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "66b2593eeb24730052754c24",
      "id": "66b2593eeb24730052754c24"
    },
    {
      "name": "Authorization",
      "type": "string",
      "enumValues": "",
      "default": "Bearer <Token>",
      "desc": "Bearer {{token}}. Applicable if you want to use JWT tokens for API authentication. Use either of 'key' or 'Authorization' header param.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "66b2593eeb24730052754c23",
      "id": "66b2593eeb24730052754c23"
    }
  ],
  "examples": {
    "codes": []
  },
  "apiSetting": "6a675233ec1c893d8a7f6824"
}
```

## OpenAPI operation and component schemas

Operation extraction: not_present_in_supplied_openapi. Missing operation definitions must not be inferred from this cache.

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Messaging API v2 New",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://api.{YourRegion}.webexconnect.io/v2",
      "variables": {
        "YourRegion": {
          "default": "YourRegion"
        }
      }
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/messages",
  "method": "post",
  "path_parameters": [],
  "operation": {},
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "key"
      }
    }
  },
  "operation_status": "not_present_in_supplied_openapi"
}
```
