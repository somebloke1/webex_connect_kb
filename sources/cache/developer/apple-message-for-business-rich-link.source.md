[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


## Rich Link with Video

```json Rich Link with Video
{
	"deliverychannel": "AppleBusinessChat",
	"appid": "{{ambAppid}}",
	"destination": [{
		"abcUserId": ["{{abcUserId}}"]
	}],

	"channels": {
		"AppleBusinessChat": {
			"type": "richLink",
			"richLinkData": {
				"url": "https://youtu.be/gM0qOa_H-rs",
				"title": "Mpbile Testing3",
				"assets": {
					"image": {
						"url": "http://clipart-library.com/data_images/320464.png",
						"mimeType": "image/png"
					},

					"video": {
						"url": "https://youtu.be/gM0qOa_H-rs",
						"mimeType": "video/mp4"
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

| Parameter/Object | Parameter within the object | Mandatory | Description                                                                                                                                                                                                                                                      |
| :--------------- | :-------------------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delivery channel |                             |           | Channel used to send the message i.e., Apple Message for Business in this case.                                                                                                                                                                                  |
| app id           |                             |           | Contains the applicationid                                                                                                                                                                                                                                       |
| destination      |                             |           | Unique user id for the recipient of the message on Apple Message for Business.                                                                                                                                                                                   |
|                  | abcUserId                   |           | Unique user id                                                                                                                                                                                                                                                   |
| channels         |                             |           |                                                                                                                                                                                                                                                                  |
|                  | AppleBusinessChat           |           | JSON object for ApplleBusinessChat configuration                                                                                                                                                                                                                 |
|                  | type                        | Yes       | Type of the outbound event. It can be text,typing_start,typing_end,richlink or interactive.                                                                                                                                                                      |
|                  | richLinkData                | Yes       | Rich link object                                                                                                                                                                                                                                                 |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media                                                                                                                                                                                                       |
|                  | title                       | Yes       | Title of the rich link message                                                                                                                                                                                                                                   |
|                  | assets                      | Yes       | Contains image or video asset                                                                                                                                                                                                                                    |
|                  | image                       |           |                                                                                                                                                                                                                                                                  |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media                                                                                                                                                                                                       |
|                  | mimeType                    | Yes       | The MIME type                                                                                                                                                                                                                                                    |
|                  | video                       |           |                                                                                                                                                                                                                                                                  |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media                                                                                                                                                                                                       |
|                  | mimeType                    | Yes       | The MIME type                                                                                                                                                                                                                                                    |
| correlationid    |                             |           | The corrrelationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.                                                                                    |
| callbackData     |                             |           | Data that you have configured to receive on the notify Url. This is configured as a part of the request.                                                                                                                                                         |
| notifyurl        |                             |           | Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries. |

> 📘 Note:
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.