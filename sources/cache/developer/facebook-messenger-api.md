# Facebook Messenger API

Source: https://developers.webexconnect.io/reference/facebook-messenger-api
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:42+00:00

> 📘 Please Note
> 
> - Facebook Messenger channel is supported via Webex ConnectMessaging API v1. The endpoint for it is:[https://{YourRegion}.webexconnect.io/resources/v1/messaging].
> 
>   Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> - Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying various message types.

## Request Body for Facebook Messenger Messages:

```json Sample Messenger message
{
    "appid": "<app-id>",
    "deliverychannel": "fb",
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "text": "Welcome to Webex Connect",
                "notification_type": "NO_PUSH"or"SILENT_PUSH",
                "messaging_type": "MESSAGE_TAG",
                "tag": "HUMAN_AGENT",
								"quick_replies": [{
                    "content_type": "text",
                    "title": "Red",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
                }, {
                    "content_type": "text",
                    "title": "Green",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN"
                }],
                "type": "conversation"
            }
        }
    },
    "destination": [
        {
            "psid": [
                "<psid>"
            ]
        }
    ]
     },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

### **Facebook Messenger Messaging Parameters**



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | String | No | Specifies the message text. Note: Either _text \_or \_attachment_ or _sender_action_ is mandatory. |
| attachment | JSONObject | No | A block consists of the following parameters:  <br>  <br>\_ type  <br>  <br>\_ payload  <br>  <br>Note: Either _text \_or \_attachment_ or _sender_action_ is mandatory. |
| notification_type | String | No | Specifies the notification to be received with a sound or without sound. The options are:  <br>  <br>\_ REGULAR (Default): The notification will be sent with a sound.  <br>  <br>\_ NO_PUSH: The notification will not be sent. |
| sender_action | String | No | Specifies the message state. The options are:  <br>  <br>\_ mark_seen  <br>  <br>\_ typing_on  <br>  <br>\_ typing_off  <br>  <br>Note: Either _text \_or \_attachment_ or \_sender_action\* is mandatory. |
| quick_replies | JSONArray | No | Specifies an options in the text message to reply back to the sender. When the quick reply is tapped, the message is sent with the option tapped. Once the message is sent, the options disappear. |
| messaging_type | String | No | Specifies the messaging type. The options are:  <br>  <br>\_ RESPONSE - Use this messaging type if you are responding to a received message. This includes messages sent inside the 24-hour standard messaging window. For example, use this tag to respond if a person asks for a reservation confirmation or an status update.  <br>  <br>\_ UPDATE - Use this messaging type if you are proactively sending a message and not in response to a received message. This includes messages sent inside the the 24-hour standard messaging window.  <br>  <br>\* MESSAGE_TAG - Message is non-promotional and is being sent outside the 24-hour standard messaging window with a message tag. The message must match the allowed use case for the tag  <br>Specify the tag using 'tag' field.  <br>  <br>Refer to [Messenger Node](https://help.imiconnect.io/docs/messenger#supported-message-tags) to know the list of supported tags. |
| notifyurlAuthId | String | No | Unique Authentication ID. |




> 📘 Note
> 
> - Authorization ID: It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs. The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL. The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.
> - Message Tag: Meta has deprecated several message tags (Confirmed Event Update, Post Purchase Update, and Account Update). These tags are no longer functional. Businesses should now use the HUMAN_AGENT tag for manual agent responses outside the 24-hour window.

## Types of Facebook Messages Supported:

Here's a list of Facebook Messenger message types supported by \<<prodname>. Click the hyperlinks below to see the API documentation for each of these.

### [Facebook Messenger : Text](https://developers.webexconnect.io/reference/facebook#text)

### [Facebook Messenger : Attachments - Media](https://developers.webexconnect.io/reference/facebook#attachments---media)

### [Facebook Messenger : Attachments - Templates](https://developers.webexconnect.io/reference/facebook#attachment---templates)

### [Facebook Messenger : Sender Action](https://developers.webexconnect.io/reference/facebook#sender-action)

### [Facebook Messenger : Quick Replies](https://developers.webexconnect.io/reference/facebook#quick-replies)

### **Text**

#### Text Payload Sample

```json Text
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "text": "Welcome to IMIconnect" //Mandatory.
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
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

The following are the parameters of the request body:



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | object | yes | JSON Object |
| trackClicks | string | yes | Optional. When enabled, this tracks all links in the HTML body unless a link is tagged as no-track-connect within the anchor tags. Link tracking is supported only for Email app assets configured using AWS SES. |
| shortenLinks | boolean | no | When enabled, this shortens any HTTPS links in the message request's body. The expiry of Shortened URL is 180 days. |
| domain | string | yes | It is the domain configuration for shortening the links.  <br>_Note: 'domain' is mandatory only when 'options' object is used in the payload._ |
| tags | string | yes | Reporting tags for tracking the  shortened link creates and clicks. |
| allowFallbackURL | string | yes | if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link. |




### **Attachments - Media**

Media Attachments can be broadly categorised into the following:

- File
- Image
- Audio
- Video

**Common Attachment Parameters**

The parameters below are common to Media attachments and Template attachments, both.



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | String | Yes | Specifies the type of the attachment. The options are:  <br>  <br>- file<br>- image<br>- audio<br>- video<br>- template |
| payload | JSONObject | Yes | Specifies the payload of attachment. The parameters of payload are:  <br>  <br>template_type: There are three types of templates:  <br>  <br>- Generic<br>- Button<br>- Receiptelements: Specifies the parameters of the selected template type in an array. |




**Payloads for Attachment Type - Media**

```json Attachment type as image
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "image", //Mandatory.
                    "payload": {
                        "url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR5LtraajVrX9XqOtN9nhyFG9i9aJhhKcFG4LLZuw34ognS6zXQWkwOnILR" //Mandatory.
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Attachment type as audio
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "audio", //Mandatory.
                    "payload": {
                        "url": "<audio-url>" //Mandatory.
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Attachment type as video
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "video", //Mandatory.
                    "payload": {
                        "url": "<video-url>" //Mandatory.
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Attachment type as file
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "file", //Mandatory.
                    "payload": {
                        "url": "<file-url>" //Mandatory.
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

```json Attachment Type as File
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "file", //Mandatory.
                    "payload": {
                        "url": "<file-url>" //Mandatory.
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Attachment Type as Image Quick Reply
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "image", //Mandatory.
                    "payload": {
                        "url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR5LtraajVrX9XqOtN9nhyFG9i9aJhhKcFG4LLZuw34ognS6zXQWkwOnILR" //Mandatory.
                    }
                },
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Red",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED",
                        "image_url": "http://www.gstatic.com/webp/gallery/1.jpg"
                    },
                    {
                        "content_type": "text",
                        "title": "Green",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Yellow",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_YELLOW",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Orange",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_ORANGE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Pink",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_PINK",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Brown",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BROWN",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Blue",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLUE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Voilate",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_VOILATE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    }
                ]
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

### **Attachment - Templates**

Template attachments can be broadly categorised into the following:

- Template Attachments. They are categorised into the following:
  - [Generic](https://developers.webexconnect.io/v6.6.2/reference/facebook#generic-template)
  - [Button](https://developers.webexconnect.io/v6.6.2/reference/facebook#button-template) 
  - [Receipt](https://developers.webexconnect.io/v6.6.2/reference/facebook#receipt-template)

#### **Generic Template**

Generic template allows you to send horizontal scrollable set of images with an option to configure short description and buttons to request input from the users. You can add up to 10 images per message. For more information, refer to the [Generic Template](https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template) documentation.

**Generic Template Payload Sample**:

```json Facebook Messenger - Generic Template
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "conversationid": "",
    "route": "",
    "message": {
        "template": ""
    },
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "template", //Mandatory.
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Classic White T-Shirt",
                                "image_url": "http://petersapparel.parseapp.com/img/item100-thumb.png",
                                "subtitle": "Soft white cotton t-shirt",
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://petersapparel.parseapp.com/view_item?item_id=100",
                                        "title": "View Item"
                                    },
                                    {
                                        "type": "postback",
                                        "title": "Bookmark Item",
                                        "payload": "USER_DEFINED_PAYLOAD_FOR_ITEM100"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Facebook Messenger - Generic Template Quick Reply
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "conversationid": "",
    "route": "",
    "message": {
        "template": ""
    },
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "template", //Mandatory.
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Classic White T-Shirt",
                                "image_url": "http://petersapparel.parseapp.com/img/item100-thumb.png",
                                "subtitle": "Soft white cotton t-shirt",
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://petersapparel.parseapp.com/view_item?item_id=100",
                                        "title": "View Item"
                                    },
                                    {
                                        "type": "postback",
                                        "title": "Bookmark Item",
                                        "payload": "USER_DEFINED_PAYLOAD_FOR_ITEM100"
                                    }
                                ]
                            }
                        ]
                    }
                },
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Red",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED",
                        "image_url": "http://www.gstatic.com/webp/gallery/1.jpg"
                    },
                    {
                        "content_type": "text",
                        "title": "Green",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Yellow",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_YELLOW",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Orange",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_ORANGE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Pink",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_PINK",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Brown",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BROWN",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Blue",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLUE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Voilate",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_VOILATE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    }
                ]
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```



![Screenshot of Generic Template.](https://files.readme.io/08959f4-generictemplate.gif)




**Generic Template Parameter Table**



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| title | String | Yes | Specifies the bubble title. It has a limit of 80 characters. |
| item_url | String | No | Specifies the URL that is opened when bubble is tapped. |
| image_url | String | No | Specifies the bubble image. |
| subtitle | String | No | Specifies the bubble subtitle. It has a limit of 80 characters. |
| buttons | JSONArray | No | Specifies a set of buttons that appears as call-to-actions. You can add up to 3 buttons only. The parameters are:  <br>  <br>\_ type  <br>  <br>\_ title  <br>  <br>\_ url  <br>  <br>\_ payload |




#### **Button Template**

Button template allows you to send a text and buttons attachment to request input from the user. The buttons can open a URL or make a back-end call to your webhook. For more information, refer to the [Button Template](https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template) documentation.

**Button Template Payload Sample**:

```json Facebook - Button Template
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "conversationid": "",
    "route": "",
    "message": {
        "template": ""
    },
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "template", //Mandatory.
                    "payload": {
                        "template_type": "button",
                        "text": "What do you want to do next?",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://petersapparel.parseapp.com",
                                "title": "Show Website"
                            },
                            {
                                "type": "postback",
                                "title": "Start Chatting",
                                "payload": "USER_DEFINED_PAYLOAD"
                            }
                        ]
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```



![Screenshot of Button Template.](https://files.readme.io/98b53f8-buttontemplate.png)




**Button Template Parameter Table**:

| Parameter | Type      | Mandatory | Description                                                                                                                                                                          |
| :-------- | :-------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text      | String    | Yes       | The text that appears in the main body.                                                                                                                                              |
| buttons   | JSONArray | No        | Specifies a set of buttons that appears as call-to-actions. Click [button object reference](http://docs.imiconnect.com/reference#section-facebook-buttons)to view the button object. |

 You can add up to 3 buttons only. The parameters are:



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | String | Yes | Specifies the value for button. The options are:  <br>  <br>\_ web_url  <br>  <br>\_ postback |
| title | String | Yes | Specifies the button title. |
| url | String | Yes | Specifies the web_url for buttons. It opens a browser when the button is tapped. |
| payload | String | Yes | When the postback button is clicked an event is raised that can be used to write rules. |




#### **Receipt Template**

Receipt template allows you to send an order confirmation, with the transaction summary and description for each item. For more information, refer to the [Receipt Template](https://developers.facebook.com/docs/messenger-platform/send-api-reference/receipt-template) documentation.

**Receipt Template Payload Sample**:

```json Facebook Messenger - Receipt Template
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "template", //Mandatory.
                    "payload": {
                        "template_type": "receipt",
                        "recipient_name": "Sivacharan",
                        "order_number": "12345678902",
                        "currency": "GBP",
                        "payment_method": "Visa 2314",
                        "order_url": "http://petersapparel.parseapp.com/order?order_id=123456",
                        "timestamp": "1428444852",
                        "elements": [
                            {
                                "title": "iPhone 7 Plus 256GB - Gold",
                                "subtitle": "This is 7",
                                "quantity": 1,
                                "price": 919.99,
                                "currency": "GBP",
                                "image_url": "http://argos.scene7.com/is/image/Argos/6043731_R_Z002A?fmt=pjpg&wid=1536&hei=1382"
                            },
                            {
                                "title": "iPhone 7 Plus Leather Case - Midnight Blue",
                                "subtitle": "Designed in California. Made in China",
                                "quantity": 2,
                                "price": 40,
                                "currency": "GBP",
                                "image_url": "http://argos.scene7.com/is/image/Argos/6049319_R_Z001A?fmt=pjpg&wid=1536&hei=1382"
                            }
                        ],
                        "address": {
                            "street_1": "Unit 5, Newbury Retail Park",
                            "street_2": "",
                            "city": "Newbury",
                            "postal_code": "RG14 7HUH",
                            "state": "Berkshire",
                            "country": "UK"
                        },
                        "summary": {
                            "subtotal": 999.99,
                            "shipping_cost": 4.95,
                            "total_tax": 56.19,
                            "total_cost": 1031.3
                        },
                        "adjustments": [
                            {
                                "name": "New Customer Discount",
                                "amount": 20
                            },
                            {
                                "name": "$10 Off Coupon",
                                "amount": 10
                            }
                        ]
                    }
                }
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

<br />



![Screenshot of Receipt Template.](https://files.readme.io/a3dadc0-receipttemplate.png)




**Receipt Template Parameter Table**



| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recipient_name | String | Yes | Specifies the recipients name. |
| order_number | String | Yes | specifies the order number. |
| currency | String | Yes | Specifies the currency for order. |
| payment_method | String | Yes | Specifies the payment method details. |
| timestamp | String | No | Specifies the timestamp of order. It must be a unique number. |
| order_url | String | No | Specifies the URL of order. |
| [elements](#section-facebook-receipt-elements) | JSONArray | Yes | Specifies the details of the order. The parameters are:  <br>  <br>\_ title  <br>  <br>\_ subtitle  <br>  <br>\_ quantity  <br>  <br>\_ price  <br>  <br>\_ currency  <br>  <br>\_ image_url |
| [address](#section-facebook-receipt-address) | JSONObject | No | Specifies the details of the shipping address. The parameters are:  <br>  <br>\_ street_1  <br>  <br>\_ street_2  <br>  <br>\_ city  <br>  <br>\_ postal_code |
| [summary](#section-facebook-receipt-summary) | JSONObject | Yes | Specifies the payment summary details. The parameters are:  <br>  <br>\_ subtotal  <br>  <br>\_ shipping_cost  <br>  <br>\* total_tax |
| [adjustments](#section-facebook-receipt-adjustments) | JSONArray | No | Specifies the payment adjustments. The parameters are:  <br>  <br>\_ name  <br>  <br>\_ amount |




Specifies the details of the order in receipt template. It accepts an array.

| Parameter | Type    | Mandatory | Description                      |
| :-------- | :------ | :-------- | :------------------------------- |
| title     | String  | Yes       | Specifies the title of the item. |
| subtitle  | String  | No        | Specifies the sub title of item. |
| quantity  | Integer | No        | Specifies the quantity of item.  |
| price     | Double  | No        | Specifies the item price.        |
| currency  | String  | No        | Specifies the currency of price. |
| image_url | String  | No        | Specifies the image URL of item. |

Specifies the details of the shipping address. 

| Parameter   | Type   | Mandatory | Description                                         |
| :---------- | :----- | :-------- | :-------------------------------------------------- |
| street_1    | String | Yes       | Specifies the street address, line 1.               |
| street_2    | String | No        | Specifies the street address, line 2.               |
| city        | String | Yes       | Specifies the city details.                         |
| postal_code | String | Yes       | Specifies the postal code.                          |
| state       | String | Yes       | Specifies the state  abbreviation of a country.     |
| country     | String | Yes       | Specifies the two letter abbreviation of a country. |

Specifies the payment summary details. The parameters are:

| Parameter     | Type   | Mandatory | Description                     |
| :------------ | :----- | :-------- | :------------------------------ |
| subtotal      | Number | No        | Specifies the subtotal.         |
| shipping_cost | Number | No        | Specifies the cost of shipping. |
| total_tax     | Number | No        | Specifies the total tax.        |
| total_cost    | Number | No        | Specifies the total cost.       |

Specifies the payment adjustments. The parameters are:

| Parameter | Type   | Mandatory | Description                       |
| :-------- | :----- | :-------- | :-------------------------------- |
| name      | String | No        | Specifies the name of adjustment. |
| amount    | Number | No        | Specifies the adjusted amount.    |

### **Sender Action**

Sender action feature allows you to set typing indicators or send read receipts to let users know that someone is typing or the message is read. Typically this feature is used in chat conversations. When you are processing a time-consuming request, you can send a typing indicator. The typing indicator gives an impression to your users that someone is replying to their request. For more information, refer to the [Sender Actions](https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions) documentation.

**Sender Action Payload Sample**:

```json Facebook - Sender action
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "sender_action": "typing_on" //Mandatory.
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

<br />



![Screenshot of Sender Action.](https://files.readme.io/22c1082-senderaction.png)




### **Quick Replies**

Quick Replies are buttons with some text that appears above the text composer. Users can tap on the button to respond to the message. Once the message is tapped, the options disappear. You can add up to 10 buttons. These buttons are useful to get a specific response from the users. You can configure buttons to have a plain text or a combination of text and image. You can also configure a button with location so that users can send geographic locations in the conversation. You can configure the button with a payload that can have custom data that will be sent back to the enterprises through a webhook. For additional information, refer to the [Quick Replies](https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies) documentation.

You can find Quick Reply payload samples for Generic Template and Attachment - Image, in their respectice sections above.

> ❗️ Quick Reply image URL
> 
> The quick reply component currently requires the image_url as a mandatory parameter. We are working to gain a better understanding of this requirement and will have a resolution soon

**Payload Samples**:

```json Text - Quick reply
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "text": "Customer id check 1", //Mandatory.
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Red",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
                    },
                    {
                        "content_type": "text",
                        "title": "Green",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN"
                    },
                    {
                        "content_type": "text",
                        "title": "Yellow",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_YELLOW"
                    },
                    {
                        "content_type": "text",
                        "title": "Orange",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_ORANGE"
                    },
                    {
                        "content_type": "text",
                        "title": "Pink",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_PINK"
                    },
                    {
                        "content_type": "text",
                        "title": "Brown",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BROWN"
                    },
                    {
                        "content_type": "text",
                        "title": "Blue",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLUE"
                    },
                    {
                        "content_type": "text",
                        "title": "Black",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLACK"
                    },
                    {
                        "content_type": "text",
                        "title": "Magenta",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLACK"
                    },
                    {
                        "content_type": "text",
                        "title": "Voilate",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_VOILATE"
                    }
                ],
                "type": "conversation"
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
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Text and Image - Quick reply
{
    "deliverychannel": "fb", //Mandatory.
    "appid": "{{fbmAppid}}", //Mandatory.
    "destination": [
        {
            "psid": [
                "{{psid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "OTT-Messaging": {
            "fb": {
                "attachment": {
                    "type": "image", //Mandatory.
                    "payload": {
                        "url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR5LtraajVrX9XqOtN9nhyFG9i9aJhhKcFG4LLZuw34ognS6zXQWkwOnILR" //Mandatory.
                    }
                },
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Red",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED",
                        "image_url": "http://www.gstatic.com/webp/gallery/1.jpg"
                    },
                    {
                        "content_type": "text",
                        "title": "Green",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Yellow",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_YELLOW",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Orange",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_ORANGE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Pink",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_PINK",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Brown",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BROWN",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Blue",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLUE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    },
                    {
                        "content_type": "text",
                        "title": "Voilate",
                        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_VOILATE",
                        "image_url": "https://www.gstatic.com/webp/gallery3/1.png"
                    }
                ]
            }
        }
    },
    "correlationid": "", //Optional.
    "callbackData": "", //Optional.
    "notifyurl": "", //Optional.
    "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

<br />



![Screenshot of Quick Reply.](https://files.readme.io/f8c9738-quickreplies.png)






| Parameter | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_type | String | Yes | Specifies the type of content. The options are:  <br>  <br>\_ text  <br>  <br>\_ location |
| title | String | Yes. This is applicable only when _content_type_ is set as _text_. | Specifies the caption for button.  You can add up to 20 characters as title. |
| payload | String | Yes. This is applicable only when _content_type_ is set as _text_. | Specifies the custom data that will be sent back to you through web hook.  The limit of this payload is 1000 characters. |
| image_url | String | No | Specifies the URL of the image sent as _quick_replies_. |




<br />

> ❗️ Quick Reply image URL
> 
> The quick reply component currently requires the image_url as a mandatory parameter. We are working to gain a better understanding of this requirement and will have a resolution soon

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
