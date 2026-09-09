[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


## WhatsApp Reply buttons -Video/Image

```json
{  
   "deliverychannel":"whatsapp",
   "appid":"<WAAppid>",
    "destination":[  
      {  
         "waid":[  
            "<waid>"
         ]
      }
   ],
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "type": "reply",
                "reply": {
                    "header": {
                        "type": "text/document/video/image",
                        "text": "Reply button your text",//OR//
                        "document": {
                            "url": "http://www.africau.edu/images/default/sample.pdf",
                            "provider": {
                                "name": "provider-name"
                            },
                            "filename": "some-file-name"
                        },//OR//
                        "video": {
                            "url": "https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_480_1_5MG.mp4",
                            "provider": {
                                "name": "provider-name"
                            }
                        },//OR//
                        "image": {
                            "url": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg",
                            "provider": {
                                "name": "provider-name"
                            }
                        }
                    },
                    "body": {
                        "text": "Body text mssage"
                    },
                    "footer": {
                        "text": "Footer text message"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "ButtonId1",
                                    "title": "First Button"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "ButtonId2",
                                    "title": "Secound Button"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "ButtonId3",
                                    "title": "Third Button"
                                }
                            }
                        ]
                    }
                }
            }
        }
    },
    "correlationid": "",
	"callbackData": "",
  "notifyurl": "",
  "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

| Parameter / Object | Parameters within an object | Mandatory | Description                                                                       |
| :----------------- | :-------------------------- | :-------- | :-------------------------------------------------------------------------------- |
| type               |                             |           |                                                                                   |
|                    | reply                       | Yes       | Specifies the message type.                                                       |
| header             |                             |           |                                                                                   |
|                    | text                        | Yes       | Contains the text for the header. Maximum of 60 characters is supported for text. |
|                    | image                       | Yes       | Contains the URL of the image                                                     |
|                    | video                       | Yes       | Contains the URL of the video                                                     |
|                    | document                    | Yes       | Contains the URL of the document                                                  |
| body               | text                        | Yes       | Body of the message. Maximum of 1024 characters is supported.                     |
| footer             | text                        | Optional  | Contains the footer text message.                                                 |
| action             |                             |           |                                                                                   |
|                    | button                      | Yes       | A button field with your button’s content.                                        |
|                    | type                        | Yes       |                                                                                   |
|                    | id                          | Yes       | A unique identification number for the button                                     |
|                    | title                       | Yes       | A title for the button                                                            |

> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.