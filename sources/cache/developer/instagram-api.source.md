> 🚧 API Endpoint and Authentication
> 
> - Your API endpoint varies based on where your imiconnect account is hosted. Visit [Know Your API Endpoint](https://developers.imiconnect.io/reference/endpoints) section to know more. 
> 
> - You can use either Service Key or JSON Web Tokens (JWT) for authentication. If you use both JWT authentication and Service Key in an API request, JWT authentication takes priority, and the Service Key is ignored.

> ❗️ API Access
> 
> This API is only available on an on-request basis. Please reach out to your support contact for enabling Instagram APIs.

## **Instagram**

```json Text
{
    "content": "A while back I needed to count the amount of letters that a piece of text in an email template had (to avoid passing any character limits). Unfortunately",
    "contentType": "TEXT",
    "from": "a_637921640978680000",
    "to": "7947908538583264",
    "callbackUrl": "https://requestinspector.com/inspect/01g1mv0mvndfpy19bc009tqvh6",
    "callbackData": "customerID123|1234|new_sale",
    "correlationId": "de36bb32-3f5d-46c9-b132-15e010a80ccc",
    "notificationType": "REGULAR",
    "messagingType": "RESPONSE"
}
```
```json Generic Template
{
    "content": "hello",
    "contentType": "TEMPLATE",
    "from": "a_637921640978680000",
    "to": "7947908538583264",
    "callbackUrl": "https://my.website.com/callback",
    "callbackData": "customerID123|1234|new_sale",
    "correlationId": "de36bb32-3f5d-46c9-b132-15e010a80ccc",
    "notificationType": "REGULAR",
    "messagingType": "RESPONSE",
    "template": [
        {
            "title": "Welcome!",
            "subtitle": "We have the right hat for everyone.",
            "imageUrl": "https://sample-videos.com/img/Sample-jpg-image-2mb.jpg",
            "defaultAction": {
                "type": "WEB_URL",
                "url": "https://www.originalcoastclothing.com"
            },
            "buttons": [
                {
                    "type": "web_url",
                    "url": "www.google.com",
                    "title": "View Website"
                },
                {
                    "type": "postback",
                    "title": "Start Chatting",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                },
                {
                    "type": "postback",
                    "title": "Start Chatting",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                }
            ]
        }
    ]
}
```
```json Media-Image
{
    "url": "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Image-file-Download.png",
    "contentType": "MEDIA",
    "from": "a_637921640978680000",
    "to": "7947908538583264",
    "callbackUrl": "https://requestinspector.com/inspect/01g6t5dkqvhr2fy7nwp60y17hn",
    "callbackData": "customerID123|1234|new_sale",
    "correlationId": "de36bb32-3f5d-46c9-b132-15e010a80ccc",
    "notificationType": "REGULAR",
    "messagingType": "RESPONSE"
}
```
```json Sticker
{
    "type": "like_heart",
    "contentType": "STICKER",
    "from": "a_637921640978680000",
    "to": "7947908538583264",
    "callbackUrl": "https://my.website.com/callback",
    "callbackData": "customerID123|1234|new_sale",
    "correlationId": "de36bb32-3f5d-46c9-b132-15e010a80ccc",
    "notificationType": "REGULAR",
    "messagingType": "RESPONSE"
}'
```
```json Quick Reply
{
    "content": "Please confirm to proceed.",
    "contentType": "TEXT",
    "from": "app-id",
    "to": "igsid",
    "callbackUrl": "https://my.website.com/callback",
    "callbackData": "customerID123|1234|new_sale",
    "correlationId": "de36bb32-3f5d-46c9-b132-15e010a80ccc",
    "notificationType": "REGULAR",
    "messagingType": "RESPONSE",
    "quickReplies": [
        {
            "type": "TEXT",
            "title": "Confirm",
            "payload": "confirm"
      
        },
        {
            "type": "TEXT",
            "title": "Cancel",
            "payload": "cancel"
        
        }
    ]
}
```

### Instagram Text Message

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "content",
    "0-1": "String",
    "0-2": "Yes",
    "0-3": "Specifies the message text. Note: Either text or attachment or sender_action is mandatory.",
    "1-0": "contentType",
    "1-1": "String",
    "1-2": "Yes",
    "1-3": "Specifies message type. Specify from the following:  \n_ TEXT  \n_ TEMPLATE  \n_ MEDIA  \n_ STICKER",
    "2-0": "quickReplies",
    "2-1": "JSONArray",
    "2-2": "No",
    "2-3": "Specifies an option in the text message to reply back to the sender. When the quick reply is tapped, the message is sent with the option tapped. Once the message is sent, the options disappear.",
    "3-0": "from",
    "3-1": "String",
    "3-2": "Yes",
    "3-3": "Your Instagram app Id",
    "4-0": "to",
    "4-1": "String",
    "4-2": "Yes",
    "4-3": "Instagram recipient Id i.e. igsid"
  },
  "cols": 4,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


### Instagram Generic Template

Generic template allows you to send horizontal scrollable set of images with an option to configure short description and buttons to request input from the users. You can add up to 10 images per message.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "type",
    "0-1": "String",
    "0-2": "Yes",
    "0-3": "Specifies the type of the attachment. The options are:  \n_ image  \n_ audio  \n_ video  \n_ file  \n\\* template",
    "1-0": "template",
    "1-1": "JSONObject",
    "1-2": "Yes",
    "1-3": "Specifies the payload of attachment. The parameters of payload are:  \n_ template_type: There are two types of templates:  \n   _ generic  \n   _ button  \n_ elements: Specifies the parameters of the selected template type in an array.",
    "2-0": "quickReplies",
    "2-1": "JSONArray",
    "2-2": "No",
    "2-3": "Specifies an option in the text message to reply back to the sender. When the quick reply is tapped, the message is sent with the option tapped. Once the message is sent, the options disappear."
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## Buttons object

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "title",
    "0-1": "String",
    "0-2": "Yes",
    "0-3": "Specifies the bubble title. It has a limit of 80 characters.",
    "1-0": "defaultAction.type",
    "1-1": "String",
    "1-2": "Yes",
    "1-3": "Specify as WEB_URL",
    "2-0": "defaultAction.url",
    "2-1": "String",
    "2-2": "Yes",
    "2-3": "Specifies the URL that is opened when bubble is tapped.",
    "3-0": "image_url",
    "3-1": "String",
    "3-2": "No",
    "3-3": "Specifies the bubble image.",
    "4-0": "subtitle",
    "4-1": "String",
    "4-2": "No",
    "4-3": "Specifies the bubble subtitle. It has a limit of 80 characters.",
    "5-0": "buttons",
    "5-1": "JSONArray",
    "5-2": "No",
    "5-3": "Specifies a set of buttons that appears as call-to-actions. You can add up to 3 buttons only. The parameters are:  \n_ type  \n_ title  \n_ url  \n_ payload"
  },
  "cols": 4,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## quickReplies

Quick Replies are buttons with some text that appears above the text composer. Users can tap on the button to respond to the message. Once the message is tapped, the options disappear. You can add up to 10 buttons. These buttons are useful to get a specific response from the users. You can configure buttons to have a plain text or a combination of text and image. You can also configure a button with location so that users can send geographic locations in the conversation. You can configure the button with a payload that can have custom data that will be sent back to the enterprises through a webhook.

| Parameter    | Type   | Mandatory | Description                                                                                                             |
| :----------- | :----- | :-------- | :---------------------------------------------------------------------------------------------------------------------- |
| content_type | String | Yes       | Specifies the type of content. Supported value: TEXT                                                                    |
| title        | String | Yes.      | Specifies the caption for button. You can add up to 20 characters as title.                                             |
| payload      | String | Yes.      | Specifies the custom data that will be sent back to you through web hook. The limit of this payload is 1000 characters. |

## Media

| Parameter    | Type      | Mandatory | Description                                                                                                                                                                                       |
| :----------- | :-------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| content_type | String    | Yes       | Specify as MEDIA                                                                                                                                                                                  |
| url          | String    | Yes       | URL of the image media file. The channel only supports image at the moment                                                                                                                        |
| quickReplies | JSONArray | No        | Specifies an option in the text message to reply back to the sender. When the quick reply is tapped, the message is sent with the option tapped. Once the message is sent, the options disappear. |

## Sticker

| Parameter    | Type      | Mandatory | Description                                                                                                                                                                                       |
| :----------- | :-------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| content_type | String    | Yes       | Specify as STICKER                                                                                                                                                                                |
| type         | String    | Yes       | Specify as 'like_heart'. The channel only supports like_heart sticker at the moment                                                                                                               |
| quickReplies | JSONArray | No        | Specifies an option in the text message to reply back to the sender. When the quick reply is tapped, the message is sent with the option tapped. Once the message is sent, the options disappear. |