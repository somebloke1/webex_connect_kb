# Send Message API v1

Source: https://developers.webexconnect.io/reference/send-message-api-v1
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:35:06+00:00

> 📘 API Endpoint & Postman Collection
> 
> SMS channel is supported via Send SMS API v1, Send Message API v2, and Send Message API v1. Refer to this Refer to the [SMS APIs](https://developers.webexconnect.io/reference/sms) section for information on which API is best suited for your use case.
> 
> The endpoint for it is: [https://{YourRegion}.webexconnect.io/resources/v1/messaging].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying Send Message API v1.
> 
> **Authentication**
> 
> Refer to the [API Authentication](https://developers.webexconnect.io/reference/authentication-2) section for information on API Authentication.

> 🚧 
> 
> While [Send Message API v1](https://developers.webexconnect.io/reference/send-sms-using-messaging-api-v1) supports SMS as one of the channels, we do not recommend using this API for any new SMS services. We continue to support it to avoid any impact on the previously configured services. We no longer add any new capabilities to this API for the SMS channel.

> 📘 API Response and Error Codes
> 
> This API is an asynchronous API. The HTTP response confirming acceptance of your request is send as soon as you invoke the API however the subsequent request processing details are notified via the callback i.e., notify URL mentioned in your API request. For more information, refer to the [Channel-Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1) documentation.

## Request Body to Send SMS Using Send Message API v1

```json Send Message API v1
{
    "deliverychannel": "sms", //Mandatory. 
    "destination": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. 
            ]
        }
    ],
    "channels": {
        "sms": {
            "senderid": "{{SENDERID}}", //Mandatory. 
            "text": "Sending first SMS using Webex Connect" //Mandatory. 
        }
    },
    "options": { //Optional.
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "correlationid": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional.
    "notifyurlAuthId":"TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.JSON Object to specify contact policy checks before sending the outbound SMS. 
        "contactPolicyGroup": "", //The GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional,assumed false if not specified. Set to true to require opt-in before sending the message. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
    }
}
```

## Send Message API v1 Parameters

The following are the parameters of the request body:



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deliverychannel | string | Yes | Channel used to send the message, i.e., 'sms'.  |
| destination | array of objects | Yes | Array of destination IDs, i.e., the phone numbers to which the SMS messages are to be sent. |
| msisdn | JSON Array | Yes | Phone number i.e., MSISDN to which the SMS has to be sent in the E.164 format.  e.g., +44XXXXXXXXXX  <br>  <br>_Note: If +E.164 format is enabled for your tenant - all the numbers in the **destination(to)** field should follow the "+E.164" format.  <br>This format displays the number with a "+" followed by the country code and the phone number.  <br>+E.164 format does not apply to the numbers in the **senderid(from)** field._ |
| channels | JSON Object | Yes | JSON object that contains mandatory 'sms' JSON object parameter. |
| sms | JSON Object | Yes | JSON object that contains mandatory 'sender ID' and 'text' parameters. |
| senderid | string | Yes | SMS Sender ID, i.e., the long code, short code, or the Sender ID to be used for sending the message.  <br>  <br>**Note:** The senderid asset must be pre-configured and associated with the channel. |
| text | string | Yes | The SMS message content. A maximum of 1024 characters can be supported.  <br>To include a new line within the content of an SMS message, insert the characters `\n` at the desired location in your message text. The `\n` sequence represents a line break and will cause the text following it to appear on a new line when the message is displayed. |
| sendLinkAsAppClip | boolean | No | Option used to send a link as an App Clip. |
| type | string | No | Used for specifying the message content type. Acceptable values are: '1', '3', and '4'. The following are the supported message types that depict (1, 3, 4) as below:  <br>1 - Text (default)  <br> 3 - Binary  <br>4 - Unicode  <br>If no parameter is specified, type defaults to 'Text'.  <br>  <br>Please note that 'text' supports many common special characters as per the SMS specification and is preferred where possible. Using 'unicode' enables the use of multi-byte encoding, which allows full character set and emoji support, but results in 2 or 3 times more SMS traffic than plain SMS text. |
| storeRegion | string | No, if 'sendLinkAsAppClip' is 'false'. | The store region is auto-selected as 'US' if there is no region specified by you. |
| body | string | Yes (when type is set to 3) | When **type** is set to 3, the body shall contain hexadecimal content for binary type message. |
| options | JSONObject | No | A JSON object that contains additional, SMS-specific options such as trackClicks, shortenLinks, and domain in the API. |
| trackClicks | boolean | No | You can receive ‘CLICKED’ notifications for shorten links on your notifyUrl by enabling trackClicks. You can also receive them on your SMS webhook if the ‘Clicked’ option is selected.  <br>The ‘trackClicks’ option is set to ‘false’ by default.  <br>Clicked format available [SMS Outbound Webhook](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts) page. |
| shortenLinks | boolean | No | When enabled, this shortens any HTTPS links in the message request's body. For more information, refer to the [configure shortenLinks](https://developers.webexconnect.io/reference/send-sms-message-api-v2#steps-for-configuring-branded--short-urls-for-smartlinks--shortenlinks-capability) section . The expiry of the shortened URL is 180 days. |
| domain | string | Yes | It is the domain configuration for shortening the links.  <br>_Note: 'domain' is mandatory only when 'options' object is used in the payload._ |
| tags | string | Yes | The reporting tags are for tracking the shortened link's creates and clicks. |
| allowFallbackURL | string |  | If true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link. |
| correlationid | string | No | User-defined ID that is assigned to an individual message for unique identification. |
| callbackData | string | No | A string that is returned with each outbound webhook for the message (delivery, failed, etc.). The maximum number of characters allowed in callbackData including any spaces, is 2000. |
| notifyurl | string | No | If provided, updates related to the delivery status of this message will be posted to this URL. Refer to [SMS Delivery Receipts](https://developers.webexconnect.io/reference/sms-1)  page for notification samples. |
| notifyurlAuthId | string | No | Unique Authentication ID. |
| contactPolicy | JSON Object | No | JSON Object to specify contact policy checks before sending the outbound SMS. Contact Policy App should be configured to use this feature as a prerequisite. |
| contactPolicyGroup | string | No | The GroupID is to be applied. Required if any of the following options are included and set to true. |
| channelCheckConsent | boolean | No | Optional, assumed false if not specified. Set to true to require opt-in before sending the message. At least one of the “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”. |
| channelApplyFrequencyCap | boolean | No | Optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”. |




> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Sample Response Body

```json 200 Success
{
  "response": [
    {
      "code": "1001",
      "transid": "3f09295d-9xx3-XXXX-4xx5-a3272e5f00c1",
      "description": "Queued"//'Queued in burst mode'returned when the request is accepted in burst mode.
    }
  ]
}
```
```json 200 Authentication failed
{
  "response": {
    "code": "7001",
    "description": "Authentication failed.",
    "transid": "7670c9a8-123x-XXXX-xx15-17f6109340d6"
  }
}
```
```json 200 Invalid JSON
{
  "response": {
    "code": "7000",
    "description": "Invalid JSON",
    "transid": "2b2c0bfb-1234-XXXXX-456x-44ee007c130f"
  }
}
```

## Example

### Sending SMS with Smartlink

```json Sending SMS with Smartlink
{
    "deliverychannel": "sms", //Mandatory. 
    "destination": [
        {
            "msisdn": [
                "{{msisdn}}" //Mandatory. 
            ]
        }
    ],
    "channels": {
        "smartlinks": [
            {
                "linkid": "",
                "validity": ""
            }
        ],
        "sms": {
            "senderid": "{{SENDERID}}", //Mandatory. 
            "type": "1",
            "text": "Sending first SMS with smart link using Webex Connect. Click the link to get surprise gift {{link_5}}" //Mandatory. 
        }
    },
    "options": { //Optional.
        "trackClicks": "true",
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "correlationid": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional.
    "notifyurlAuthId":"TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.JSON Object to specify contact policy checks before sending the outbound SMS. 
        "contactPolicyGroup": "", //The GroupID to be applied. Required if any of the following options are included and set to true.
        "channelCheckConsent": true, //optional,assumed false if not specified. Set to true to require opt-in before sending the message. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
        "channelApplyFrequencyCap": true //optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameter should be set to “true”. 
    }
}
```

The following are the parameters required to send messages using Smartlink. Smartlinks need to be mentioned in the SMS text field, as shown in the payload sample above.

| parameter  | type       | mandatory                          | description                                                                                               |
| :--------- | :--------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| smartlinks | JSONObject | yes, if you want to use smartlinks | This is a JSON object which contains the mandatory fields required for using smartlinks.                  |
| linkid     | string     | yes                                | Unique smartlink ID. This value is generated within Webex Connectplatform, when you configure a smartlink. |
| validity   | string     | yes                                | Validity of the smartlink                                                                                 |

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
        "code": "{\n    \"response\": [\n        {\n            \"code\": \"1001\",\n            \"transid\": \"3f09295d-9eb3-4c9e-8ee8-a3272e5f00c1\",\n            \"description\": \"Queued\"\n        }\n    ]\n}",
        "language": "json",
        "status": 200
      },
      {
        "name": "Authentication Failed",
        "code": "{\n    \"response\": {\n        \"code\": \"7001\",\n        \"description\": \"Authentication failed.\",\n        \"transid\": \"7670c9a8-131f-4166-ac30-17f6109340d6\"\n    }\n}",
        "language": "json",
        "status": 200
      },
      {
        "code": "{\n    \"response\": {\n        \"code\": \"7000\",\n        \"description\": \"Invalid JSON\",\n        \"transid\": \"2b2c0bfb-4396-444a-880d-44ee007c130f\"\n    }\n}",
        "language": "json",
        "status": 200,
        "name": "Invalid JSON"
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
      "_id": "66b2523fc3aa01006e3711d2",
      "id": "66b2523fc3aa01006e3711d2"
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
      "_id": "66b2523fc3aa01006e3711d1",
      "id": "66b2523fc3aa01006e3711d1"
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
      "_id": "66b2523fc3aa01006e3711d0",
      "id": "66b2523fc3aa01006e3711d0"
    }
  ],
  "examples": {
    "codes": [
      {
        "code": "",
        "language": "json",
        "name": null
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f6825"
}
```

## OpenAPI operation and component schemas

Operation extraction: not_present_in_supplied_openapi. Missing operation definitions must not be inferred from this cache.

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Messaging API v1 New",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://api.{YourRegion}.webexconnect.io/resources/v1",
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
