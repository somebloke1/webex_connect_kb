[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n display callout; \n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


## Other Media Types

**The audio, document, video and sticker objects** 

```json Video
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., WhatsApp in this case.
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
```json Audio
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., WhatsApp in this case.
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
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., WhatsApp in this case.
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
```json Sticker
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., WhatsApp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
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

Common Parameters for Other Media Types

[block:parameters]
{
  "data": {
    "h-0": "Parameter/Object",
    "h-1": "Parameters with in the Object",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "deliverychannel",
    "0-1": "",
    "0-2": "",
    "0-3": "Channel used to send the message i.e., WhatsApp in this case.",
    "1-0": "appid",
    "1-1": "",
    "1-2": "",
    "1-3": "Contains the applicationid",
    "2-0": "destination",
    "2-1": "",
    "2-2": "",
    "2-3": "Unique user id for the recipient of the message on WhatsApp.",
    "3-0": "",
    "3-1": "waid",
    "3-2": "Yes",
    "3-3": "WhatsApp ID or phone number for the person you want to send a message to.",
    "4-0": "",
    "4-1": "bsuid",
    "4-2": "When both WAID and BSUID are present, WAID takes priority as the** primary identifier**.  \n  \nA **single identifier** is used by preferring WAID or copying BSUID into WAID if empty.  \n**  \nNormalization** ensures consistent use across systems with flags indicating derived values and compatibility maintained in APIs and logs",
    "4-3": "The BSUID is a unique, business-specific identifier generated by Meta for every user-business portfolio pairing.",
    "5-0": "correlationid",
    "5-1": "",
    "5-2": "",
    "5-3": "The corrrelationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
    "6-0": "callbackData",
    "6-1": "",
    "6-2": "",
    "6-3": "Data that you have configured to receive on the notify Url. This is configured as a part of the request.",
    "7-0": "notifyurl",
    "7-1": "",
    "7-2": "",
    "7-3": "Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.",
    "8-0": "notifyurlAuthId",
    "8-1": "string",
    "8-2": "No",
    "8-3": "Unique Authenticaiton ID.",
    "9-0": "type",
    "9-1": "",
    "9-2": "Yes, when type is image, audio, document or sticker",
    "9-3": "image, audio, document, video or sticker. Refer below table to know more about each of these types.",
    "10-0": "caption",
    "10-1": "",
    "10-2": "No",
    "10-3": "Describes the specified image, video, or document media. Do not use with audio or sticker media.",
    "11-0": "url",
    "11-1": "",
    "11-2": "yes",
    "11-3": "Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.",
    "12-0": "mimeType",
    "12-1": "",
    "12-2": "yes",
    "12-3": "Supported mime types."
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


> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

Additional details for the various media message types:

**Video**

[block:parameters]
{
  "data": {
    "h-0": "Parameter/Object",
    "h-1": "Parameters with in the Object",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "channels",
    "0-1": "",
    "0-2": "",
    "0-3": "",
    "1-0": "",
    "1-1": "OTT-Messaging",
    "1-2": "",
    "1-3": "JSON object for social channel message configuration",
    "2-0": "",
    "2-1": "waid",
    "2-2": "Yes",
    "2-3": "WhatsApp ID or phone number for the person you want to send a message to.",
    "3-0": "",
    "3-1": "bsuid",
    "3-2": "When both WAID and BSUID are present, WAID takes priority as the** primary identifier**.  \n  \nA **single identifier** is used by preferring WAID or copying BSUID into WAID if empty.  \n**  \nNormalization** ensures consistent use across systems with flags indicating derived values and compatibility maintained in APIs and logs",
    "3-3": "The BSUID is a unique, business-specific identifier generated by Meta for every user-business portfolio pairing.",
    "4-0": "",
    "4-1": "type(Video)",
    "4-2": "",
    "4-3": "video",
    "5-0": "",
    "5-1": "video",
    "5-2": "",
    "5-3": "The media object containing a video",
    "6-0": "",
    "6-1": "url",
    "6-2": "",
    "6-3": "Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.",
    "7-0": "",
    "7-1": "mimeType",
    "7-2": "",
    "7-3": "Supported [mime types](https://help.imiconnect.io/docs/supported-file-types-for-channels#whatsapp)."
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


**Audio**

[block:parameters]
{
  "data": {
    "h-0": "Parameter/Object",
    "h-1": "Parameters with in the Object",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "channels",
    "0-1": "",
    "0-2": "",
    "0-3": "",
    "1-0": "",
    "1-1": "OTT-Messaging",
    "1-2": "",
    "1-3": "JSON object for social channel message configuration",
    "2-0": "",
    "2-1": "waid",
    "2-2": "Yes",
    "2-3": "WhatsApp ID or phone number for the person you want to send a message to.",
    "3-0": "",
    "3-1": "bsuid",
    "3-2": "When both WAID and BSUID are present, WAID takes priority as the** primary identifier**.  \n  \nA **single identifier** is used by preferring WAID or copying BSUID into WAID if empty.  \n**  \nNormalization** ensures consistent use across systems with flags indicating derived values and compatibility maintained in APIs and logs",
    "3-3": "The BSUID is a unique, business-specific identifier generated by Meta for every user-business portfolio pairing.",
    "4-0": "",
    "4-1": "type (Audio)",
    "4-2": "",
    "4-3": "audio ",
    "5-0": "",
    "5-1": "audio",
    "5-2": "",
    "5-3": "The media object containing audio.  \nSupported audio formats are aac, mp4, mpeg, amr and ogg (only opus codecs, base ogg is not supported)",
    "6-0": "",
    "6-1": "url",
    "6-2": "",
    "6-3": "Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.",
    "7-0": "",
    "7-1": "mimeType",
    "7-2": "",
    "7-3": "Supported [mime types](https://help.imiconnect.io/docs/supported-file-types-for-channels#whatsapp) ."
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


**Document**

[block:parameters]
{
  "data": {
    "h-0": "Parameter/Object",
    "h-1": "Parameters with in the Object",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "channels",
    "0-1": "",
    "0-2": "",
    "0-3": "",
    "1-0": "",
    "1-1": "OTT-Messaging",
    "1-2": "",
    "1-3": "JSON object for social channel message configuration",
    "2-0": "",
    "2-1": "waid",
    "2-2": "Yes",
    "2-3": "WhatsApp ID or phone number for the person you want to send a message to.",
    "3-0": "",
    "3-1": "bsuid",
    "3-2": "When both WAID and BSUID are present, WAID takes priority as the** primary identifier**.  \n  \nA **single identifier** is used by preferring WAID or copying BSUID into WAID if empty.  \n**  \nNormalization** ensures consistent use across systems with flags indicating derived values and compatibility maintained in APIs and logs",
    "3-3": "The BSUID is a unique, business-specific identifier generated by Meta for every user-business portfolio pairing.",
    "4-0": "",
    "4-1": "type (document)",
    "4-2": "",
    "4-3": "document ",
    "5-0": "",
    "5-1": "document",
    "5-2": "",
    "5-3": "The media object containing a document.  \nSupported document formats are PDF, DOC(X), PPT(X), The media object containing a videoXLS(X).",
    "6-0": "",
    "6-1": "url",
    "6-2": "",
    "6-3": "Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.",
    "7-0": "",
    "7-1": "filename",
    "7-2": "",
    "7-3": "filename of the document",
    "8-0": "",
    "8-1": "mimeType",
    "8-2": "",
    "8-3": "Supported [mime types](https://help.imiconnect.io/docs/supported-file-types-for-channels#whatsapp) ."
  },
  "cols": 4,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Sticker**

[block:parameters]
{
  "data": {
    "h-0": "Parameter/Object",
    "h-1": "Parameters with in the Object",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "conversationid",
    "0-1": "",
    "0-2": "",
    "0-3": "",
    "1-0": "channels",
    "1-1": "",
    "1-2": "",
    "1-3": "",
    "2-0": "",
    "2-1": "OTT-Messaging",
    "2-2": "",
    "2-3": "JSON object for social channel message configuration",
    "3-0": "",
    "3-1": "waid",
    "3-2": "Yes",
    "3-3": "WhatsApp ID or phone number for the person you want to send a message to.",
    "4-0": "",
    "4-1": "bsuid",
    "4-2": "When both WAID and BSUID are present, WAID takes priority as the** primary identifier**.  \n  \nA **single identifier** is used by preferring WAID or copying BSUID into WAID if empty.  \n**  \nNormalization** ensures consistent use across systems with flags indicating derived values and compatibility maintained in APIs and logs",
    "4-3": "The BSUID is a unique, business-specific identifier generated by Meta for every user-business portfolio pairing.",
    "5-0": "",
    "5-1": "type(sticker)",
    "5-2": "",
    "5-3": "sticker.",
    "6-0": "",
    "6-1": "sticker",
    "6-2": "",
    "6-3": "The media object containing a sticker.",
    "7-0": "",
    "7-1": "url",
    "7-2": "",
    "7-3": "Direct URL pointing to the media file. The URL should end with specified file-format. You can use our Media manager under Tools to upload a file and get a public URL.",
    "8-0": "",
    "8-1": "mimeType",
    "8-2": "",
    "8-3": "Supported [mime types](https://help.imiconnect.io/docs/supported-file-types-for-channels#whatsapp) ."
  },
  "cols": 4,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.