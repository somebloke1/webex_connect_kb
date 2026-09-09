[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


#### Apple Pay

```json Apple Pay
{
	"deliverychannel": "AppleBusinessChat",
	"appid": "{{ambAppid}}",
	"destination": [{
		"abcUserId": ["{{abcUserId}}"]
	}],
	"channels": {
		"AppleBusinessChat": {
			"type": "interactive",
			"x_msg_seq": 1,
			"interactiveData": {
				"data": {
					"version": "1.0",
					"requestIdentifier": "21d4a1c4-327c-ba35-45b1-36a050b15ad2",
					"images": [{
							"identifier": "6de6a59c-846f-45d8-a1d7-24382d9919db",
							"url": "http://clipart-library.com/data_images/320464.png"
						}

					],
					"payment": {
						"paymentRequest": {
							"lineItems": [{
								"amount": "1.50",
								"type": "final",
								"label": "Adoption fee"
							}],
							"shippingMethods": [{
								"label": "shipping charges (Optional)",
								"amount": "8",
								"detail": "fast delivery (Optional)",
								"identifier": "b3062736-e911-42db-b7a2-b5c603805858"
							}],
							"requiredShippingContactFields": [
								"postalAddress",
								"name",
								"phone"
							],
							"countryCode": "US",
							"requiredBillingContactFields": [
								"postalAddress",
								"name",
								"phone"
							],
							"currencyCode": "USD",
							"total": {
								"amount": "3.0",
								"type": "final",
								"label": "Your Total"
							}
						}
					}
				},
				"useLiveLayout": true,
				"receivedMessage": {
					"title": "The best deals on new iPhones!"
				},
				"replyMessage": {
					"title": "Reply Title"
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

| Parameter/Object | Parameter within the Object | Mandatory | Description                                                                                                                                                                                                                                                           |
| :--------------- | :-------------------------- | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delivery channel |                             | Yes       | Options: text, richlink, interactive                                                                                                                                                                                                                                  |
| app id           |                             | Yes       | Rich link object                                                                                                                                                                                                                                                      |
| destination      |                             |           | Unique user id for the recipient of the message on WhatsApp.                                                                                                                                                                                                          |
|                  | abcUserId                   |           | Unique user id                                                                                                                                                                                                                                                        |
| channels         |                             |           |                                                                                                                                                                                                                                                                       |
|                  | AppleBusinessChat           |           |                                                                                                                                                                                                                                                                       |
|                  | type                        |           | Options: text, richlink, interactive                                                                                                                                                                                                                                  |
|                  | interactiveData             | Yes       | Contains the list/Time Picker (Date Picker) and Quick Reply data                                                                                                                                                                                                      |
|                  | data                        |           |                                                                                                                                                                                                                                                                       |
|                  | version                     | Yes       | A string representing the version number of the message extension schema. Should be 1.0.                                                                                                                                                                              |
|                  | requestIdentifier           | Yes       | A string that representing a unique identifier for the request. imiconnect returns the ID in the response it sends back to the client application                                                                                                                     |
|                  | images                      | Yes       | An array of image dictionaries                                                                                                                                                                                                                                        |
|                  | identifier                  | Yes       | An identifier to identify the item.                                                                                                                                                                                                                                   |
|                  | url                         | Yes       | Publicly accessible URL that is a direct link to the media                                                                                                                                                                                                            |
|                  | authenticate                |           |                                                                                                                                                                                                                                                                       |
|                  | oauth2                      |           |                                                                                                                                                                                                                                                                       |
|                  | responseType                |           |                                                                                                                                                                                                                                                                       |
|                  | scope                       |           |                                                                                                                                                                                                                                                                       |
|                  | receivedMessage             |           |                                                                                                                                                                                                                                                                       |
|                  | subtitle                    |           |                                                                                                                                                                                                                                                                       |
|                  | title                       |           |                                                                                                                                                                                                                                                                       |
|                  | imageIdentifier             |           |                                                                                                                                                                                                                                                                       |
|                  | replyMessage                |           |                                                                                                                                                                                                                                                                       |
| correlationid    |                             |           | The corrrelationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.                                                                                         |
| callbackData     |                             |           | Data that you have configured to receive on the notify Url. This is configured as a part of the request.                                                                                                                                                              |
| notifyurl        |                             |           | Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in an API request or via a variable, then such a request will not be considered eligible for retries. |

> 📘 Note:
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.