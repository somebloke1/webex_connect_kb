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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "deliverychannel",
    "0-1": "string",
    "0-2": "Yes",
    "0-3": "Channel used to send the message, i.e., 'sms'. ",
    "1-0": "destination",
    "1-1": "array of objects",
    "1-2": "Yes",
    "1-3": "Array of destination IDs, i.e., the phone numbers to which the SMS messages are to be sent.",
    "2-0": "msisdn",
    "2-1": "JSON Array",
    "2-2": "Yes",
    "2-3": "Phone number i.e., MSISDN to which the SMS has to be sent in the E.164 format.  e.g., +44XXXXXXXXXX  \n  \n_Note: If +E.164 format is enabled for your tenant - all the numbers in the **destination(to)** field should follow the \"+E.164\" format.  \nThis format displays the number with a \"+\" followed by the country code and the phone number.  \n+E.164 format does not apply to the numbers in the **senderid(from)** field._",
    "3-0": "channels",
    "3-1": "JSON Object",
    "3-2": "Yes",
    "3-3": "JSON object that contains mandatory 'sms' JSON object parameter.",
    "4-0": "sms",
    "4-1": "JSON Object",
    "4-2": "Yes",
    "4-3": "JSON object that contains mandatory 'sender ID' and 'text' parameters.",
    "5-0": "senderid",
    "5-1": "string",
    "5-2": "Yes",
    "5-3": "SMS Sender ID, i.e., the long code, short code, or the Sender ID to be used for sending the message.  \n  \n**Note:** The senderid asset must be pre-configured and associated with the channel.",
    "6-0": "text",
    "6-1": "string",
    "6-2": "Yes",
    "6-3": "The SMS message content. A maximum of 1024 characters can be supported.  \nTo include a new line within the content of an SMS message, insert the characters `\\n` at the desired location in your message text. The `\\n` sequence represents a line break and will cause the text following it to appear on a new line when the message is displayed.",
    "7-0": "sendLinkAsAppClip",
    "7-1": "boolean",
    "7-2": "No",
    "7-3": "Option used to send a link as an App Clip.",
    "8-0": "type",
    "8-1": "string",
    "8-2": "No",
    "8-3": "Used for specifying the message content type. Acceptable values are: '1', '3', and '4'. The following are the supported message types that depict (1, 3, 4) as below:  \n1 - Text (default)  \n 3 - Binary  \n4 - Unicode  \nIf no parameter is specified, type defaults to 'Text'.  \n  \nPlease note that 'text' supports many common special characters as per the SMS specification and is preferred where possible. Using 'unicode' enables the use of multi-byte encoding, which allows full character set and emoji support, but results in 2 or 3 times more SMS traffic than plain SMS text.",
    "9-0": "storeRegion",
    "9-1": "string",
    "9-2": "No, if 'sendLinkAsAppClip' is 'false'.",
    "9-3": "The store region is auto-selected as 'US' if there is no region specified by you.",
    "10-0": "body",
    "10-1": "string",
    "10-2": "Yes (when type is set to 3)",
    "10-3": "When **type** is set to 3, the body shall contain hexadecimal content for binary type message.",
    "11-0": "options",
    "11-1": "JSONObject",
    "11-2": "No",
    "11-3": "A JSON object that contains additional, SMS-specific options such as trackClicks, shortenLinks, and domain in the API.",
    "12-0": "trackClicks",
    "12-1": "boolean",
    "12-2": "No",
    "12-3": "You can receive ‘CLICKED’ notifications for shorten links on your notifyUrl by enabling trackClicks. You can also receive them on your SMS webhook if the ‘Clicked’ option is selected.  \nThe ‘trackClicks’ option is set to ‘false’ by default.  \nClicked format available [SMS Outbound Webhook](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts) page.",
    "13-0": "shortenLinks",
    "13-1": "boolean",
    "13-2": "No",
    "13-3": "When enabled, this shortens any HTTPS links in the message request's body. For more information, refer to the [configure shortenLinks](https://developers.webexconnect.io/reference/send-sms-message-api-v2#steps-for-configuring-branded--short-urls-for-smartlinks--shortenlinks-capability) section . The expiry of the shortened URL is 180 days.",
    "14-0": "domain",
    "14-1": "string",
    "14-2": "Yes",
    "14-3": "It is the domain configuration for shortening the links.  \n_Note: 'domain' is mandatory only when 'options' object is used in the payload._",
    "15-0": "tags",
    "15-1": "string",
    "15-2": "Yes",
    "15-3": "The reporting tags are for tracking the shortened link's creates and clicks.",
    "16-0": "allowFallbackURL",
    "16-1": "string",
    "16-2": "",
    "16-3": "If true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.",
    "17-0": "correlationid",
    "17-1": "string",
    "17-2": "No",
    "17-3": "User-defined ID that is assigned to an individual message for unique identification.",
    "18-0": "callbackData",
    "18-1": "string",
    "18-2": "No",
    "18-3": "A string that is returned with each outbound webhook for the message (delivery, failed, etc.). The maximum number of characters allowed in callbackData including any spaces, is 2000.",
    "19-0": "notifyurl",
    "19-1": "string",
    "19-2": "No",
    "19-3": "If provided, updates related to the delivery status of this message will be posted to this URL. Refer to [SMS Delivery Receipts](https://developers.webexconnect.io/reference/sms-1)  page for notification samples.",
    "20-0": "notifyurlAuthId",
    "20-1": "string",
    "20-2": "No",
    "20-3": "Unique Authentication ID.",
    "21-0": "contactPolicy",
    "21-1": "JSON Object",
    "21-2": "No",
    "21-3": "JSON Object to specify contact policy checks before sending the outbound SMS. Contact Policy App should be configured to use this feature as a prerequisite.",
    "22-0": "contactPolicyGroup",
    "22-1": "string",
    "22-2": "No",
    "22-3": "The GroupID is to be applied. Required if any of the following options are included and set to true.",
    "23-0": "channelCheckConsent",
    "23-1": "boolean",
    "23-2": "No",
    "23-3": "Optional, assumed false if not specified. Set to true to require opt-in before sending the message. At least one of the “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”.",
    "24-0": "channelApplyFrequencyCap",
    "24-1": "boolean",
    "24-2": "No",
    "24-3": "Optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one of “channelCheckConsent” or “channelApplyFrequencyCap” parameters should be set to “true”."
  },
  "cols": 4,
  "rows": 25,
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
| linkid     | string     | yes                                | Unique smartlink ID. This value is generated within <<prodname>>platform, when you configure a smartlink. |
| validity   | string     | yes                                | Validity of the smartlink                                                                                 |