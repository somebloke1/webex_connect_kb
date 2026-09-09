# WhatsApp API

Source: https://developers.webexconnect.io/reference/whatsapp-apis
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:42+00:00

> 📘 Please note:
> 
> - WhatsApp channel is supported via Webex Connect Messaging API v1. The endpoint for it is: [https://{YourRegion}.webexconnect.io/resources/v1/messaging].
> 
>   Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> - Please note that proactive outbound messaging on WhatsApp requires Template Registration and Approval using the Templates Module within Webex Connect.
> - While the payload samples for various message types are covered below, you can use our Try It feature (click on the Message Type name to get routed to it) to send some test messages. You would be required to provide the WhatsApp asset details, service key, template content, etc. from your account to use this. This apart you can[ use our Postman Collection ](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f)for trying variations that are not covered through the Try It feature.

## Types of WhatsApp Messages Supported

Here's a list of WhatsApp message types supported by Webex Connect with payload samples. Click the hyperlinks below to see the API documentation for each of the message types. 

### [Text  Messages](https://developers.imiconnect.io/reference/whatsapp-text-message)

Used for responding to an incoming customer message, or follow-up messages within the 24-hour reply window as per WhatsApp's messaging guidelines.

```json
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "text", //Mandatory. Specify WhatsApp message type as 'text'
                "text": { //Mandatory.
                    "body": "This is a whatsapp message" //Mandatory. Specify the body of the message
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
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
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```



| Parameter | Mandatory | Description |
| --- | --- | --- |
| text | Yes | Contains the body field that you can use to pass the message content. The message can contain URLs and text formatting tags. |
| type | Yes | Specifies that message type. E.g., text. |
| preview_url | No | Options: false (default), true  <br>  <br>To include a URL preview, set preview_url to true and make sure the URL begins with http\:// or https\://.  If multiple URLs are in the body text string, only the first URL will be rendered. Follow the [guidelines](https://developers.facebook.com/docs/whatsapp/link-previews) to make sure the URL preview is rendered by WhatsApp. |
| identity_key_hash | No | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented in [WhatsApp Node](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field) documentation. |
| options | No | A JSON object that contains additional, SMS-specific options such as trackClicks, shortenLinks, and domain in the API. |
| trackClicks | No | You can receive ‘CLICKED’ notifications for shorten links on your notifyUrl by enabling trackClicks. You can also receive them on your SMS webhook if the ‘Clicked’ option is selected.  <br>The ‘trackClicks’ option is set to ‘false’ by default.  <br>Clicked format details are available [WhatsApp Delivery Receipts](https://developers.webexconnect.io/reference/whatsapp-outbound-webhooks#whatsapp-delivery-receipts) documentation. |
| shortenLinks | No | When enabled, this shortens any HTTPS links in the message request's body. For more information, refer to[ configure shortenLinks ](https://developers.webexconnect.io/reference/send-sms-message-api-v2#steps-for-configuring-branded--short-urls-for-smartlinks--shortenlinks-capability)section.The expiry of the shortened URL is 180 days. |
| domain | Yes | It is the domain configuration for shortening the links.  <br>_Note: 'domain' is mandatory only when 'options' object is used in the payload._ |
| tags | Yes | The reporting tags are for tracking the shortened link's creates and clicks. |
| allowFallbackURL | Yes | If true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link. |
| notifyurlAuthId  | No |  |




### [Media Messages](https://developers.imiconnect.io/reference/whatsapp-media-message)

Used for responding to an incoming customer message, or follow-up messages within the 24-hour reply window as per WhatsApp's messaging guidelines. Use this option when you want to send a response message with image, document, audio, video, or sticker.

**The audio, document, image, video and sticker objects** 

```json Audio
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
  
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "audio", //Mandatory. Specify the media type of WhatsApp message. Supported types are image, audio, document, video or sticker.
                "audio": {
                    "url": "<your-media-url>", //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.
                    "mimeType": "audio/aac" //Mandatory. Specify mime type of media for e.g. image/png, video/mp4, audio/aac
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Document
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "document", //Mandatory. Specify the media type of WhatsApp message. Supported types are image, audio, document, video or sticker.
                "document": {
                    "url": "<your-media-url>", //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.
                    "filename": "Document test", //Optional
                    "mimeType": "application/pdf" //Mandatory. Specify mime type of media for e.g. image/jpg, image/png, image/webp, video/mp4, audio/aac, application/pdf
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Image
{{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "image", //Mandatory. Specify the media type of WhatsApp message. Supported types are image, audio, document, video or sticker.
                "image": {
                    "url": "<your-media-url>", //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.
                    "caption": "", //Optional. Describes the specified image, video, or document media. Do not use with audio or sticker media.
                    "mimeType": "image/jpg" //Mandatory. Specify mime type of media for e.g. image/jpg, image/png, video/mp4, audio/aac
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

               },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Video
{{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "video", //Mandatory. Specify the media type of WhatsApp message. Supported types are image, audio, document, video or sticker.
                "video": {
                    "url": "<your-media-url>", //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.
                    "mimeType": "<VIDEO/MP4>" //Mandatory. Specify mime type of media for e.g. image/png, video/mp4
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Sticker
{{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "conversationid": "",
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "sticker", //Mandatory. Specify the media type of WhatsApp message. Supported types are image, audio, document, video or sticker.
                "sticker": {
                    "url": "<your-media-url>", //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.
                    "mimeType": "image/WEBP" //Mandatory. Specify mime type of media for e.g. image/jpg, image/png, image/webp, video/mp4, audio/aac
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}


```



| Parameter | Mandatory | Description |
| --- | --- | --- |
| type | Yes, when type is image, audio, document or sticker | image, audio, document, video or sticker. Refer below table to know more about each of these types. |
| caption | No | Describes the specified image, video, or document media. Do not use with audio or sticker media. |
| url | yes | Direct URL pointing to the media file. The URL should end with specified file-format.  <br>  <br>You can use our Media manager under Tools to upload a file and get a public URL. |
| mimeType | yes | Supported mime types. Find more details [here](https://help.imiconnect.io/docs/supported-file-types-for-channels#whatsapp) |
| identity_key_hash | No | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented [here.](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field)  |




Additional details for the various media message types:



| Parameter | Mandatory | Description | Maximum Size |
| --- | --- | --- | --- |
| audio | Yes, when "type": "audio". | The media object containing audio.  <br>Supported audio formats are AAC, MP4, MPEG, AMR,  <br>OGG; codecs=opus  <br>Note: The base ogg type is not supported.  <br>OPUS is deprecated. | 16 MB |
| document | Yes, when "type": "document". | The media object containing a document.  <br>Supported document formats are TXT, PDF, XLS, DOC, PPT, XLS(X), DOC(X) and PPT(X), The media object containing a XLS(X) file | 100 MB |
| image | Yes, when "type": "image". | The media object containing an image.  <br>Supported image formats are JPEG and PNG | 5 MB |
| video | Yes, when "type": "video" | The media object containing a video. Supported formats are 3GPP and MP4  <br>Notes:  <br>Only H.264 video codec and AAC audio codec is supported.  <br>WhatsApp support videos with a single audio stream or no audio stream. | 16 MB |
| sticker | Yes, when "type":"sticker" | The media object containing a sticker. Supported format WEBP | Static stickers: 100KB  <br>  <br>Animated stickers: 500KB |




<br />

> 👍 WhatsApp Media Best Practices
> 
> - While uploading the media and setting the mime-type make sure you follow the [guidelines](https://developers.facebook.com/docs/whatsapp/on-premises/get-started/migrate-existing-whatsapp-number-to-a-business-account).
> - The publicly accessible URL used while configuring the message must end in the same file format set under the 'File MIME type'. It should not have any geo-restriction and should be accessible from a server located within USA premises.
> - Supported incoming media message mime-types are identical to outbound message media mime-types in Send node and Messaging API. The mime-type of the incoming media message can be captured as part of the following: 
>   - Start node and Receive node output variable i.e., "**whatsApp.mimetype**", 
>   - Outbound webhooks, Debug logs and Export logs with JSON path "**attachments.mime_type**"
> - WebP is a modern image format that provides superior lossless compression and creates smaller and richer images that makes web faster. The source libraries to use for converting an image to WebP file-format are available in [WebP](https://developers.google.com/speed/webp) documentation. You can also use various third-party converters publicly available to convert images to WebP file-format.

### [Location Messages](https://developers.imiconnect.io/reference/whatsapp-location-message)

Share location as a message on WhatsApp to your customers. This message type can be sent within 24 hour window after a customer-initiated message.

```json Sample request
{{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "location", //Specifies the message type. The value needs to be 'location' for sending location messages.
                "location": {
                    "longitude": 0.0, //Longitude of the location
                    "latitude": 0.0, //Latitude of the location
                    "name": "", //Name of the location
                    "address": "" //Address of the location. Only displayed if name is present.
                },  
           	"identity_key_hash":"<identity-key-hash-value>"//Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```

**Parameters**

| Parameter         | Mandatory | Description                                                                                                                                                                                                                    |
| :---------------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type              | Yes       | Specifies the message type. The value needs to be 'location' for sending location messages.                                                                                                                                    |
| longitude         | Yes       | Longitude of the location                                                                                                                                                                                                      |
| latitude          | Yes       | Latitude of the location                                                                                                                                                                                                       |
| name              | No        | Name of the location                                                                                                                                                                                                           |
| address           | No        | Address of the location. Only displayed if name is present.                                                                                                                                                                    |
| identity_key_hash | No        | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented in the [WhatsApp Node](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field) documentation. |

### [Contact Message](https://developers.imiconnect.io/reference/whatsapp-contacts-messages)

Share contacts on WhatsApp to your customers. This message type can be sent within 24 hour window after a customer initiated message

```json Sample request
{{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
"channels": {
        "OTT-Messaging": {
            "wa": {  
           	    "identity_key_hash":"<identity-key-hash-value>", //Optional. Pass this value to validate the identity of your customer.
                "type": "contacts", //Specify the message type
                "contacts": [
                    {
                        "addresses": [
                            {
                                "city": "", //City name
                                "country": "", //Full country name
                                "country_code": "", //Two-letter country abbreviation
                                "state": "", //State abbreviation
                                "street": "", //Street number and name
                                "type": "", //Standard Values: HOME, WORK
                                "zip": "" //ZIP code
                            }
                        ],
                        "birthday": "", //YYYY-MM-DD formatted string
                        "emails": [
                            {
                                "email": "", //Email address
                                "type": "" //Standard Values: HOME, WORK
                            }
                        ],
                        "name": {
                            "first_name": "", //First name
                            "formatted_name": "", //Full name as it normally appears. At least one of the optional parameters needs to be included along with the formatted_name parameter.
                            "last_name": "" //Last name
                        },
                        "org": {
                            "company": "", //Name of the contact's company
                            "department": "", //Name of the contact's department
                            "title": "" //Contact's business title
                        },
                        "phones": [
                            {
                                "phone": "", //Contact phone number
                                "type": "" //Standard Values: CELL, MAIN, IPHONE, HOME, WORK
                            }
                        ],
                        "urls": [
                            {
                                "url": "", //URL
                                "type": "" //Standard Values: HOME, WORK
                            }
                        ]
                    }
                ]
            }
        }
    },
    "correlationid": "", //The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```

| Parameter / Object | Parameters within an object | Description                                                                                                                                                                                                                | Mandatory                                                                                                  |
| :----------------- | :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| type               |                             | Specifies the message type. The value needs to be 'location' for sending location messages.                                                                                                                                | Yes                                                                                                        |
| addresses          |                             | Full contact address(es)                                                                                                                                                                                                   | No                                                                                                         |
|                    | street                      | Street number and name                                                                                                                                                                                                     | No                                                                                                         |
|                    | city                        | City name                                                                                                                                                                                                                  | No                                                                                                         |
|                    | state                       | State abbreviation                                                                                                                                                                                                         | No                                                                                                         |
|                    | zip                         | ZIP code                                                                                                                                                                                                                   | No                                                                                                         |
|                    | country                     | Full country name                                                                                                                                                                                                          | No                                                                                                         |
|                    | country_code                | Two-letter country abbreviation                                                                                                                                                                                            |                                                                                                            |
|                    | type                        | Standard Values: HOME, WORK                                                                                                                                                                                                | No                                                                                                         |
| birthday           |                             | YYYY-MM-DD formatted string                                                                                                                                                                                                | No                                                                                                         |
| emails             |                             | Contact email address(es)                                                                                                                                                                                                  | No                                                                                                         |
|                    | email                       | Email address                                                                                                                                                                                                              | No                                                                                                         |
|                    | type                        | Standard Values: HOME, WORK                                                                                                                                                                                                | No                                                                                                         |
| name               |                             | Full contact name                                                                                                                                                                                                          | No                                                                                                         |
|                    | formatted_name              | Full name as it normally appears                                                                                                                                                                                           | Yes, At least one of the optional parameters needs to be included along with the formatted_name parameter. |
|                    | first_name                  | First name                                                                                                                                                                                                                 | Optional\*                                                                                                 |
|                    | last_name                   | Last name                                                                                                                                                                                                                  | Optional\*                                                                                                 |
|                    | middle_name                 | Middle name                                                                                                                                                                                                                | Optional\*                                                                                                 |
|                    | suffix                      | Name suffix                                                                                                                                                                                                                | Optional\*                                                                                                 |
|                    | prefix                      | Name prefix                                                                                                                                                                                                                | Optional\*                                                                                                 |
| org                |                             | Contact organization information                                                                                                                                                                                           | No                                                                                                         |
|                    | company                     | Name of the contact's company                                                                                                                                                                                              | No                                                                                                         |
|                    | department                  | Name of the contact's department                                                                                                                                                                                           | No                                                                                                         |
|                    | title                       | Contact's business title                                                                                                                                                                                                   | No                                                                                                         |
| phones             |                             | Contact phone number(s)                                                                                                                                                                                                    | No                                                                                                         |
|                    | phone                       | Automatically populated with the wa_id value as a formatted phone number.                                                                                                                                                  | No                                                                                                         |
|                    | type                        | Standard Values: CELL, MAIN, IPHONE, HOME, WORK                                                                                                                                                                            | No                                                                                                         |
|                    | wa_id                       | WhatsApp ID                                                                                                                                                                                                                | No                                                                                                         |
| urls               |                             | Contact URL(s)                                                                                                                                                                                                             | No                                                                                                         |
|                    | url                         | URL                                                                                                                                                                                                                        | No                                                                                                         |
|                    | type                        | Standard Values: HOME, WORK                                                                                                                                                                                                | No                                                                                                         |
| identity_key_hash  |                             | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented in [WhatsApp Node](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field) documentation. | No                                                                                                         |

### [List Messages](https://developers.imiconnect.io/reference/whatsapp-list-messages)

List Message includes a menu of up to 10 options. This type of message offers a simpler and more consistent way for users to make a selection when interacting with a business.

```json
{{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "list", //Mandatory. specifies message type
                "list": {
                    "header": { //Optional.
                        "type": "text", //Mandatory. Contains the header type. Supported value: ' text'
                        "text": "Sample Header" //Optional. Contains the text for the header. Maximum of 60 characters is supported for text.
                    },
                    "body": {
                        "text": "Sample Body" //Mandatory. Body of the message. Maximum of 1024 characters is supported.
                    },
                    "footer": { //Optional.
                        "text": "Sample Footer" //Optional. Contains the footer text message.
                    },
                    "action": {
                        "button": "Main Menu", //Mandatory. Specifies the button text for your list. Maximum of 20 characters are supported.
                        "sections": [ //Array of section objects. Minimum of 1, maximum of 10.
                            {
                                "title": "Section-title-1", //Title of the section. Required if the message has more than one section. Maximum length: 24 characters. 
                                "rows": [ //Contains a list of rows. You can have a total of 10 rows across your sections.
                                    {
                                        "id": "unique-row-identifier-1", //Mandatory. unique id of the row
                                        "title": "Row-title-1", //Mandatory. title of the row
                                        "description": "Row-description" //Optional. Row description
                                    }
                                ]
                            }
                        ]
                    }
                },
                "identity_key_hash": "<identity-key-hash-value>" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```

| Parameter / Object | Parameters within an object | Mandatory | Description                                                                                                                                                                                                                    |
| :----------------- | :-------------------------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type               |                             |           |                                                                                                                                                                                                                                |
|                    | header                      | Optional  |                                                                                                                                                                                                                                |
|                    | text                        |           | Contains the text for the header. Maximum of 60 characters is supported for text.                                                                                                                                              |
| body               | text                        | Yes       | Body of the message. Maximum of 1024 characters is supported.                                                                                                                                                                  |
| footer             | text                        | Optional  | Contains the footer text message.                                                                                                                                                                                              |
| action             |                             |           |                                                                                                                                                                                                                                |
|                    | button                      | Yes       | A button field with your button’s content. Maximum of 20 characters is supported.                                                                                                                                              |
|                    | title                       | Yes       | A title for the button                                                                                                                                                                                                         |
|                    | id                          | Yes       | A unique identification number for the button                                                                                                                                                                                  |
|                    | description                 | Yes       | Contains the description for the action                                                                                                                                                                                        |
| identity_key_hash  |                             | No        | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented in the [WhatsApp Node](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field) documentation. |

### [Reply Buttons](https://developers.imiconnect.io/reference/whatsapp-reply-buttons)

Reply Buttons Message includes up to 3 options —each option is a button. This type of message offers a quicker way for users to make a selection from a menu when interacting with a business. Reply buttons have the same user experience as interactive templates with buttons.

```json
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "reply", //Mandatory. Specify the message type.
                "reply": {
                    "header": {
                        "type": "text/document/video/image", //Mandatory. Specifies the header type. Supported values (text/document/video/image)
                        "text": "Reply button your text", //Mandatory. Contains the text for the header. Maximum of 60 characters is supported for text.
                        "document": {
                            "url": "",
                            "provider": {
                                "name": "provider-name"
                            },
                            "filename": "some-file-name"
                        }, //OR//
                        "video": {
                            "url": "",
                            "provider": {
                                "name": "provider-name"
                            }
                        }, //OR//
                        "image": {
                            "url": "",
                            "provider": {
                                "name": "provider-name"
                            }
                        }
                    },
                    "body": {
                        "text": "" //Mandatory. Body of the message. Maximum of 1024 characters is supported.
                    },
                    "footer": { //Optional.
                        "text": "" //Optional. An object with the footer of the message. The footer object contains the following field: textstring – Required if footer is present. The footer content. Emojis, markdown, and links are supported. Maximum length: 60 characters.
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply", //Mandatory. specifies of the type of action
                                "reply": {
                                    "id": "ButtonId1", //Mandatory. key-value pair. You can define your custom key and pass respective value. In this example custom key is 'id' and 'title' and respective value is 'ButtonId1'
                                    "title": "First Button" //Mandatory. key-value pair. You can define your custom key and pass respective value. In this example custom key is 'title' and 'title' and respective value is 'First Button'
                                }
                            }
                        ]
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```

| Parameter / Object | Parameters within an object | Mandatory | Description                                                                                                                                                                                                                    |
| :----------------- | :-------------------------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type               |                             |           |                                                                                                                                                                                                                                |
|                    | reply                       | Yes       | Specifies the message type.                                                                                                                                                                                                    |
| header             |                             |           |                                                                                                                                                                                                                                |
|                    | text                        | Yes       | Contains the text for the header. Maximum of 60 characters is supported for text.                                                                                                                                              |
|                    | image                       | Yes       | Contains the URL of the image                                                                                                                                                                                                  |
|                    | video                       | Yes       | Contains the URL of the video                                                                                                                                                                                                  |
|                    | document                    | Yes       | Contains the URL of the document                                                                                                                                                                                               |
| body               | text                        | Yes       | Body of the message. Maximum of 1024 characters is supported.                                                                                                                                                                  |
| footer             | text                        | Optional  | Contains the footer text message.                                                                                                                                                                                              |
| action             |                             |           |                                                                                                                                                                                                                                |
|                    | button                      | Yes       | A button field with your button’s content.                                                                                                                                                                                     |
|                    | type                        | Yes       |                                                                                                                                                                                                                                |
|                    | id                          | Yes       | A unique identification number for the button                                                                                                                                                                                  |
|                    | title                       | Yes       | A title for the button                                                                                                                                                                                                         |
| identity_key_hash  |                             | No        | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented in the [WhatsApp Node](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field) documentation. |

### [HSMs Text-based Proactive Notification Message-Deprecated](https://developers.imiconnect.io/reference/whatsapp-hsms-text-based-proactive-notification-message)

Send business initiated messages using message templates beyond the 24 hour window to your customers. This message type includes text based templates without a header, footer or buttons.

> ❗️ HSM Message Deprecation Alert
> 
> WhatsApp has announced that they will be deprecating the HSM message type sometime in early 2022. We recommend you to use Template message type instead of HSM messages, and migrate any existing HSMs to Template Message type. Unlike HSM which was meant to be used only for text messages, Template message type can be used to configure template messages of multiple components including text.

| Parameter | Mandatory                   | Description                                                                                                                                          |    |
| :-------- | :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :- |
| type      | Yes (for Message Templates) | The type of message being sent                                                                                                                       |    |
| hsm       | Yes (for Message Templates) | The containing element for the message content — Indicates that the message is highly structured. Parameters contained within provide the structure. |    |

  **The hsm object (To be Deprecated by WhatsApp by Early 2022)** 

```json HSM - sample
{
	"appid": "{{appid}}",
	"deliverychannel": "whatsapp",
	"channels": {
		"OTT-Messaging": {
			"wa": {
      	"type": "hsm",
                "hsm": {
                    "namespace": "59ae27be_a774_420c_18ae_22040d30978f",
                    "element_name": "chaitanya",
                    "language": {
                        "code": "en",
                        "policy": "deterministic"
                    },
                    "localizable_params": [{
                        "default": "Chaitanya"
                    },
                    {
                        "default": "Marella"
                    }]
				}
			}
		}
	},
	"destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
]

```

> 🚧 
> 
> Some of the below values such as namespace, element_name, etc. are not available on imiconnect platform UI and need to be taken from WhatsApp Business Manager by reaching out to your regional support team. However, you wouldn't need it as we now recommend you to use Template message type instead of HSM.



| Parameter / Object | Parameters within an object | Mandatory | Description |
| --- | --- | --- | --- |
| namespace | Yes | Yes | The namespace that will be used. |
| element_name | Yes | Yes | The element name that indicates which template to use within the namespace. |
| language |  |  | The language parameter sets the language policy for a Message Template. |
|  | policy | Yes | Options:  <br>  <br>  \_ deterministic — Deliver the Message Template in exactly the language and locale asked for.  <br>  <br>  \_ fallback (Deprecated) — Deliver the Message Template in the language that matches the user's language/locale setting on the device. If one can't be found, deliver using the specified fallback language. |
|  | code | Yes | The code of the language or locale to use — Accepts both language and language_locale formats (e.g., en and en_US). |
| localizable_params | Yes | Yes | This field is an array of values to apply to variables in the template  <br>See the Localizable Parameters section for more information. |




> ❗️ WhatsApp Language Policy Change
> 
> Please note that the fallback language policy has been deprecated and the deterministic language policy is now the default policy. Do not use 'fallback' language policy while sending HSMs as it may lead to message delivery failures.

- **_Localizable Parameters_**

When sending a Message Template, the hsm object is required. To define Message Templates, you specify a namespace and an element_name pair that identify a template. Templates have parameters that will be dynamically incorporated into the message. For the example used in this document, the Message Template looks like this:

| Parameters | Type             | Mandatory | Description                                                                                    |
| :--------- | :--------------- | :-------- | :--------------------------------------------------------------------------------------------- |
| default    | String           | Yes       | Default text if localization fails                                                             |
| currency   | currency object  | No        | If the currency object is used, it contains required parameters currency_code and amount_1000. |
| date_time  | date_time object | No        | If the date_time object is used, further definition of the date and time is required.          |

### [Template Messages Text-based Proactive Notification Message](https://developers.imiconnect.io/reference/whatsapp-template-messages)

Send business initiated messages using message templates beyond the 24 hour window to your customers. A message template can be text-based, media-based, or interactive.Used for sending proactive messages (including text-only, text with media or other components such as Header, Footer, Images, Document, Video, Call-to-Action Buttons, and/or Quick Replies).

Used for send proactive messages (including text-only, text with media or other components such as Header, Footer, Images, Document, Video, Call-to-Action Buttons, and/or Quick Replies).

> 🚧 Template API usage
> 
> The template should be registered and approved from **Tools -> Templates** section within imiconnect platform, before it can be used to send notification messages. You can also use interactive message templates like **Call-To-Action** buttons or **Quick Replies** buttons.

The following includes Template API definition and various samples. The API structure is dynamic and varies based on the parameters defined in the template at the time of template creation. 

```json API definition
{
    "appid": "a_157967534853754560",
    "deliverychannel": "whatsapp",
    "message": {
        "template": "5139722425xxxxx", //Configure Template Id. Template Id can be fetched from the Tools - Template listing page.//

        "parameters": {

            //Header Configuration - Configure either Text Header or Media Header i.e. Image Video or Document

            "image/video/document": {
                "link": "http://mattfarmer.net/projects/thickbox/images/plant4.jpg"
            }, //Configure Media header variable. Configure parameter key as image video or document for a image video or document type header
            //or

            "headerText": "This is a sample Header text", //Configure Text header variable. Configured parameter key <headerText> is the name of the variable specified during template creation
            //Body configuration - Configure from simple text variables or localisable variables i.e. Time or Currency.


            "movie": "joker", //Simple text variable. Configured parameter key <movie> is the name of the variable specified during template creation
            "venue": "hyderabad",
            "seat1": "balcony",
            "seat2": "first class",

            "time": {
                "type": "date_time",
                "fallback_value": "Feb 20th, 2023 8:45pm",
                "timestamp": "1782231500"
            }, //Localisable time variable. Configured parameter key <time> is the name of the variable specified during template creation

            "purchase_value": {
                "type": "currency",
                "currency_code": "USD",
                "amount_1000": "150000",
                "fallback_value": "EUR 300"
            }, //Localisable currency variable. Configured parameter key <purchase_value> is the name of the variable specified during template creation


            //Buttons Configuration. Configure either CTA button variable Quick Replies or OTP button.

            //Configure CTA button URL variable

            "ctaVariable": { //CTA button dynamic URL configuration. Configured parameter key <ctaVariable> is the name of the variable specified during template creation.
                "type": "url",
                "payload": "url_extension" //Specify Dynamic Extenstion of the URL
            }, 

            //Configure upto three quick reply buttons
            
            "quickReply": [
                {
                    "button_text": "Button 1", //Configure the value of the <buttontext> as the name of the button specified during template creation here.
                    "payload": "BUTTON 1 PAYLOAD" //Configure unique button payload. This will be returned back as part of Postback event in Webex Connect incoming components.
                },
                {
                    "button_text": "Button 2",
                    "payload": "BUTTON 2 PAYLOAD"
                },
                {
                    "button_text": "Button 3",
                    "payload": "BUTTON 3 PAYLOAD"
                }
            ],

           //Configure value of the OTP. This is applicable only in case of Authentication template.
    	  		   "otp": {
                 			 "type": "otp",
                 			 "value": "12xxxx"
                 }

        }
    },
    "channels": {
          "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
     "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
]

```
```json Header - Text
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "image": {
                "link": ""
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
]

```
```json Header - Image
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
      {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "image": {
                "link": ""
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}


```
```json Header - Video
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "video": {
                "link": ""
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Header - Document
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],

    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "document": {
                "link": "", //Mandatory.
                "filename": "" //Optional.
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}


```

| Parameter   | Mandatory | Description                                                                                  |
| :---------- | :-------- | :------------------------------------------------------------------------------------------- |
| appid       | Yes       | Refers to WhatsApp asset id. You can obtain this from the Apps page on the platform.         |
| template    | Yes       | Refers to template id. You can obtain this from Tools --> Templates section on the platform. |
| parameters  | Yes \*    | The block that contains the template parameters.                                             |
| destination | Yes       | The mobile number on which the WhatsApp message will be sent                                 |

> 📘 Parameters Object Configuration
> 
> The parameters object should be configured depending on how the variables were configured at the time of template creation for a given template. Refer below to configure Header, Body and Button parameters.

<br />

| Parameter name    | Description                                                                                                                                                                                                                    | Mandatory |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| identity_key_hash | Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented in the [WhatsApp Node](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field) documentation. | No        |

**Header Parameters Configuration** - Configure either Text Header or Media Header i.e. Image Video or Document

| Parameter name       | Description                                                                                                                                  | Object Configuration                                                                                                                                                                                                                                                                                               |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image/video/document | Configure Media header variable. Configure parameter key as image video or document for a image video or document type header                | **link**: The media URL of the image, video or document ending with the file format. This is a mandatory parameter. Refer to [Whats App](https://help.imiconnect.io/docs/supported-file-types-for-channels#whatsapp) section in Supported File Types for Channels, for more details about mime-type and media size |
| headerText           | Configure Text header variable. Configured parameter key <headerText> should be the name of the variable specified during template creation. | NA                                                                                                                                                                                                                                                                                                                 |

**Body Parameters configuration** - Configure from simple text variables or localisable variables i.e. Time or Currency



| Parameter name | Description | Object Configuration |
| --- | --- | --- |
| movie/venue/seat1/seat2 | Simple text variable. Configured parameter key for e.g., <movie> should be the name of the variable specified during template creation.  | NA |
| time | Localisable time variable. Configured parameter key <time> should be the name of the variable specified during template creation | _ **Fallback_value**: The fallback value that appears to the customer when the localization fails. This is a mandatory parameter.  <br>_ **Timestamp**: UNIX epoch timestamp that is used to calculate the localized date and time. Go to [epoch convertor](https://www.epochconverter.com/) for timestamp conversion. |
| purchase_value | Localisable currency variable. Configured parameter key \<purchase_value> should be the name of the variable specified during template creation. | _ **type**:	Parameter indicates the type as "currency".  <br>_ **currencycode**_:	The currency code for e.g., USD, EUR, INR, etc.  <br>_ **amount1000**_: 	The actual amount multiplied by 1000.  <br>_ **fallback_value**:	The fallback value that appears to the customer when the localization fails.  <br>_Note: All parameters are mandatory_ |




**Buttons Parameter configuration** - Configure a CTA button variable, Quick Replies or an OTP button.



| Parameter name | Description | Object Configuration |
| --- | --- | --- |
| ctaVariable | CTA button dynamic URL configuration. Configured parameter key <ctaVariable> should be the name of the variable specified during template creation. |  **type**: Extension of the URL in case of CTA buttons. It cannot be the domain of the URL.  <br> **payload**: Specify Dynamic Extension of the URL  <br>_Note: All parameters are mandatory_ |
| quickReply | Configure upto three quick reply buttons. Specify parameter key as 'quickReply'. | _ **button_text**: Configure the value of the <buttontext> as the name of the button specified during template creation here.  <br>_ **payload**: Configure unique button payload. This will be returned back as part of Postback event in Webex Connect incoming components.  <br>_Note: All parameters are mandatory_ |
| otp | Configure value of the OTP. This is applicable only in case of Authentication template. Specify parameter key as 'otp'. | _ **type**: specify type as ‘otp' under the otp object to pass the code value within the 'value field’.  <br>_ **value**: Configure the OTP value without spaces with maximum character supported upto 15 characters.  <br>_Note: All parameters are mandatory_ |




```json CTA Buttons
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],

    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "{{ctaVariable}}": {
                "type": "url", //Mandatory.
                "payload": "URL_EXTENSION" //Mandatory.
            }
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Quick Replies
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],

    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "quickReply": [
                {
                    "button_text": "{{buttonText1}}", //Mandatory. Configure the value of the <buttontext> as the name of the button specified during template creation here.
                    "payload": "BUTTON 1 PAYLOAD" //Mandatory. Configure unique button payload. This will be returned back as part of Postback event in Webex Connect incoming components.
                },
                {
                    "button_text": "{{buttonText2}}",
                    "payload": "BUTTON 2 PAYLOAD"
                },
                {
                    "button_text": "{{buttonText3}}",
                    "payload": "BUTTON 3 PAYLOAD"
                }
            ]
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}

```
```json Authentication template
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
  {
    // Provide at least one recipient identifier. Either waid or bsuid.
    // waid accepts a WhatsApp ID, phone number, or a normalized WAID value such as IN.2149372115xxxxxx.
    // If a normalized WAID/BSUID-formatted value is passed in waid, the platform will treat it as a normalized WAID case.
    "waid": [
      "{{waid}}"
    ],

    // bsuid is the explicit BSUID recipient field.
    // Use this when you already have the recipient BSUID and want to send using BSUID directly.
    "bsuid": [
      "{{bsuid}}"
    ]
  }
],

    "message": {
        "template": "<Template-ID>",
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "otp": {
                "type": "otp", //Mandatory.
                "value": "12xxxx" //Mandatory.
            }
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "" //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "params": [],
  "examples": {
    "codes": []
  },
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
  }
}
```
