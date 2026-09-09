[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


> 📘 Note
> 
> Please use URL-friendly file names for attachments, and avoid using special characters such as “+” in file names.

## Other Text Attachments

```json Text with attachment-PDF
{
    "deliverychannel": "AppleBusinessChat",
    "appid": "{{ambAppid}}",
    "destination": [
        {
            "abcUserId": [
                "{{abcUserId}}"
            ]
        }
    ],
    "channels": {
        "AppleBusinessChat": {
            "type": "text",
            "text": "\\uFFFC",
            "attachments": [
                {
                    "url": "https://sample-videos.com/doc/Sample-doc-file-100kb.doc",
                    "mimeType": "application/msword",
                    "name": "Sample-doc-file-100kb.doc",
                    "size": "102400"
                }
            ]
        }
    },
    "correlationid": "",
    "callbackData": "",
  "notifyurl": "",
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Text with attachment- .mp4 file
{
    "deliverychannel": "AppleBusinessChat",
    "appid": "{{ambAppid}}",
    "destination": [
        {
            "abcUserId": [
                "{{abcUserId}}"
            ]
        }
    ],
    "channels": {
        "AppleBusinessChat": {
            "type": "text",
            "text": " Aravindha Sametha Veera Raghava \\uFFFC",
            "attachments": [
                {
                    "url": "https://stgrtmedia.s3.amazonaws.com/re04101516/30341916739262892.mp4",
                    "mimeType": "video/mp4"
                }
            ]
        }
    },
    "correlationid": "",
    "callbackData": "",
    "notifyurl": "",
   "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Text with attachment-Different fles(Image,Video and audio)
{
    "deliverychannel": "AppleBusinessChat",
    "appid": "{{ambAppid}}",
    "destination": [
        {
            "abcUserId": [
                "{{abcUserId}}"
            ]
        }
    ],
    "channels": {
        "AppleBusinessChat": {
            "type": "text",
            "text": " Attachment1 \\uFFFC Attachment2  \\uFFFC Attachment3 \\uFFFC Attachment4  \\uFFFC Attachment5  \\uFFFC Attachment6 \\uFFFC Attachment7 \\uFFFC Attachment8 \\uFFFC Attachment9 \\uFFFC Attachment10 \\uFFFC",
            "attachments": [
                {
                    "url": "https://timesofindia.indiatimes.com/videos/entertainment/music/telugu/aravindha-sametha-song-reddamma-thalli/videoshow/66349017.cms",
                    "mimeType": "application/pdf"
                },
                {
                    "url": "https://www.livemint.com/rf/Image-621x414/LiveMint/Period2/2016/08/23/Photos/Processed/sampleflat-U10141249868INC--621x414@LiveMint.jpg",
                    "mimeType": "image/jpeg"
                },
                {
                    "url": "http://file-examples.com/index.php/sample-audio-files/sample-mp3-download/",
                    "mimeType": "application/pdf"
                },
                {
                    "url": "http://www.africau.edu/images/default/sample.pdf",
                    "mimeType": "image/jpeg"
                }
            ]
        }
    },
    "correlationid": "",
    "callbackData": "",
    "notifyurl": "",
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

Common Parameters for other text attachment types

| Parameter/Object | Parameter within the Object | Mandatory | Description                                                                                                                                                                                                                                                      |
| :--------------- | :-------------------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delivery channel |                             |           | Channel used to send the message i.e., Apple Messages for Business in this case.                                                                                                                                                                                 |
| app id           |                             | Yes       | Contains the applicationid                                                                                                                                                                                                                                       |
| destination      |                             |           | User's Opaque ID that uniquely identifies a user and is specific to the business                                                                                                                                                                                 |
|                  | abcUserId                   |           | Unique user ID                                                                                                                                                                                                                                                   |
| correlationid    |                             |           | The corrrelationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.                                                                                    |
| callbackData     |                             |           | Data that you have configured to receive on the notify Url. This is configured as a part of the request.                                                                                                                                                         |
| notifyurl        |                             |           | Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries. |
| notifyurlAuthId  | string                      | No        | Unique Authentication ID.                                                                                                                                                                                                                                        |

> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

Additional details for the various text attachment types:

**Text with attachment-PDF**

| Parameter/Object | Parameter within the Object | Mandatory | Description                                                         |
| :--------------- | :-------------------------- | :-------- | :------------------------------------------------------------------ |
| channels         |                             |           |                                                                     |
|                  | AppleBusinessChat           |           | JSON object for AppleBusinessChat configuration.                    |
|                  | type                        | Yes       | Options: text, richlink, interactive                                |
|                  | text                        | Yes       | The text of the text message, which can contain URLs and formatting |
|                  | attachments                 | No        | Contains the attachment object                                      |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media          |
|                  | mimeType                    | Yes       | The MIME type                                                       |
|                  | name                        |           | name of the attachment                                              |
|                  | size                        |           | size of the attachment                                              |
| conversationid   |                             |           |                                                                     |

**Text with attachment-.mp4**

| Parameter/Object | Parameter within the Object | Mandatory | Description                                                         |
| :--------------- | :-------------------------- | :-------- | :------------------------------------------------------------------ |
| channels         |                             |           |                                                                     |
|                  | AppleBusinessChat           |           | JSON object for AppleBusinessChat configuration.                    |
|                  | type                        | Yes       | Options: text, richlink, interactive                                |
|                  | text                        | Yes       | The text of the text message, which can contain URLs and formatting |
|                  | attachments                 | No        | Contains the attachment object                                      |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media          |
|                  | mimetype                    | Yes       | The MIME type                                                       |

**Text with attachment-Different fles(Image,Video and audio)**

| Parameter/Object | Parameter within the Object | Mandatory | Description                                                         |
| :--------------- | :-------------------------- | :-------- | :------------------------------------------------------------------ |
| channels         |                             |           |                                                                     |
|                  | AppleBusinessChat           |           | JSON object for AppleBusinessChat configuration.                    |
|                  | type                        | Yes       | Options: text, richlink, interactive                                |
|                  | text                        | Yes       | The text of the text message, which can contain URLs and formatting |
|                  | attachments                 | No        | Contains the attachment object                                      |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media          |
|                  | mimetype                    | Yes       | The MIME type                                                       |

## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.