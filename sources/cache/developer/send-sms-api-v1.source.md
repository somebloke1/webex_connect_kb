> 📘 API Endpoints & Postman Collection
> 
> The SMS channel is supported via Send SMS API v1, Send Message API v2, and Send Message API v1. Refer to this [SMS APIs page](https://developers.webexconnect.io/reference/sms) for information on which API is best suited for your use case.
> 
> The API endpoint for Send SMS API v1 is: [https://api.{YourRegion}.webexconnect.io/v1/sms/messages]. 
> 
> Please modify YourRegion in the URL as per your tenant’s region. See [Know Your Endpoint Page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying Send SMS API v1.
> 
> **Authentication**
> 
> Refer to [authentication](https://developers.webexconnect.io/reference/authentication-2) for information on API Authentication.

> 📘 API Response and Error Codes
> 
> SMS API v1 is an asynchronous API. The HTTP response confirming acceptance of your request is sent as soon as you invoke the API. However, the subsequent request processing details are notified via the callback URL i.e., notify URL mentioned in your API request. Refer to [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1) for more information.

## Request Body to Send SMS Using Send SMS API v1

```json Send SMS API v1
{
    "from": "12233XXXXXX", //Mandatory. Country code with phone number but without '+' sign, or the short code/sender ID.
    "to": "+1647XXXXXXX", //Mandatory. E.164 format required/recommended.
    "content": "SMS- $(sms_parameter1) API v1- $(sms_parameter2)", //Mandatory. 
    "contentType": "text", //Mandatory. 
    "substitutions": { //Optional.
        "{{sms_parameter1}}": "{{sms_value1}}",
        "{{sms_parameter2}}": "{{sms_value2}}"
    },
    "dltTemplateId": "", //Specifies the DLT template ID used for this message. This is applicable only for India.
    "shortenUrls": true, // Boolean. When enabled, this shortens any https links found in the body the message request.
    "shortUrlDomain": "https://www.domain.tld", //Domain configured for shortening the links. Needs to be configured through Support team.
    "trackShortUrlClicks": true, // Boolean. When shortenUrls is true, you can receive CLICKED receipts on your notifyUrl if trackShortUrlClicks is true. 
    "expireAt": "{{TimeinUTC}}",
    "correlationId": "", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
  "callbackData": "", //Optional. Data that you have configured to receive on the callback Url. This is configured as a part of the request. 
"callbackUrl": "", //Optional. Callback URL for getting notified about the request status.
"callbackUrlAuthId":"TNPXXXT09U" //Optional.
}
```

## Send SMS API v1 Body Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "from",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "SMS Sender ID, i.e., the long code, short code, or the Sender ID to be used for sending the message.  \nIf you are using a long code, please include the country code, along with the phone number, without adding the '+' symbol.  \nFor example, \"12233XXXXXX\".",
    "1-0": "to",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "Phone number i.e., MSISDN to which the SMS has to be sent in the E.164 format.",
    "2-0": "content",
    "2-1": "string",
    "2-2": "yes, if template is not provided",
    "2-3": "Contains the actual SMS message content. A maximum of 4000 characters can be supported. We recommend that you keep SMS messages below 450 characters for better deliverability and user experience.  \nTo include a new line within the content of an SMS message, insert the characters `\\n` at the desired location in your message text. The `\\n` sequence represents a line break and will cause the text following it to appear on a new line when the message is displayed.",
    "3-0": "contentType",
    "3-1": "string",
    "3-2": "no",
    "3-3": "Used for specifying the message content type. Acceptable values are: 'text' and 'unicode'.  \n  \nPlease note that 'text' supports many common special characters as per the SMS specification and is the preferred type wherever possible to be used. Using 'unicode' enables the use of multi-byte encoding, which allows full character set and emoji support, but results in 2 or 3 times more SMS traffic than plain SMS 'text' type content.",
    "4-0": "substitutions",
    "4-1": "JSONObject",
    "4-2": "no",
    "4-3": "List of key-value pairs for dynamic fields in the SMS message content. Typically used for specifying the values for dynamic fields in an SMS template.",
    "5-0": "dltTemplateId    ",
    "5-1": "string",
    "5-2": "no",
    "5-3": "Specifies the DLT template ID used for this message. This applies only to India.",
    "6-0": "shortenUrls",
    "6-1": "boolean",
    "6-2": "no",
    "6-3": "When enabled, this shortens any HTTPS links found in the body of the message request. The expiry of the shortened URL is 180 days.",
    "7-0": "shortUrlDomain",
    "7-1": "string",
    "7-2": "no",
    "7-3": "Domain configuration for shortening the links. It needs to be configured as a prerequisite following the steps mentioned in  the last section of this page.",
    "8-0": "trackShortUrlClicks",
    "8-1": "boolean",
    "8-2": "no",
    "8-3": "When _shortenUrls_ is set to true, you can receive CLICKED receipts on your _callbackUrl_ if _trackShortUrlClicks_ is set to true. 'Clicked' format is available on the [SMS Oubound Webhook](https://developers.imiconnect.io/reference#sms-1) page.",
    "9-0": "expireAt",
    "9-1": "date and time",
    "9-2": "no",
    "9-3": "A timestamp post, in which the message has to be expired and not sent to the intended recipient, in case the Send SMS request has yet to be processed.  \n  \nFor example, 2024-06-26T13:47:18.000Z - UTC",
    "10-0": "correlationId  ",
    "10-1": "string",
    "10-2": "no",
    "10-3": "User defined ID that is assigned to an individual message for unique identification.",
    "11-0": "callbackData",
    "11-1": "string",
    "11-2": "no",
    "11-3": "A string that is returned with each outbound webhook notification for the message delivery status (delivered, failed, etc.). The maximum number of characters allowed for callbackData including any spaces is 2000.",
    "12-0": "callbackUrl",
    "12-1": "string",
    "12-2": "no",
    "12-3": "If provided, updates related to the delivery status of this message will be posted to this URL. Refer to [SMS Delivery Receipts ](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts) section for notification samples.",
    "13-0": "callbackUrlAuthId",
    "13-1": "string",
    "13-2": "no",
    "13-3": "Unique authentication ID."
  },
  "cols": 4,
  "rows": 14,
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

```json 202 Success Code
{
    "acceptedTime": "2024-09-04T06:42:16.520-04:00",
    "messageId": "acc27bb5-1234-XXXX-xx23-1a6036fcced5",
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

<ShortenLink />