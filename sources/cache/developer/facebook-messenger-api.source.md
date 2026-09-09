> 📘 Please Note
> 
> - Facebook Messenger channel is supported via <<prodname>>Messaging API v1. The endpoint for it is:[https://{YourRegion}.webexconnect.io/resources/v1/messaging].
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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "text",
    "0-1": "String",
    "0-2": "No",
    "0-3": "Specifies the message text. Note: Either _text \\_or \\_attachment_ or _sender_action_ is mandatory.",
    "1-0": "attachment",
    "1-1": "JSONObject",
    "1-2": "No",
    "1-3": "A block consists of the following parameters:  \n  \n\\_ type  \n  \n\\_ payload  \n  \nNote: Either _text \\_or \\_attachment_ or _sender_action_ is mandatory.",
    "2-0": "notification_type",
    "2-1": "String",
    "2-2": "No",
    "2-3": "Specifies the notification to be received with a sound or without sound. The options are:  \n  \n\\_ REGULAR (Default): The notification will be sent with a sound.  \n  \n\\_ NO_PUSH: The notification will not be sent.",
    "3-0": "sender_action",
    "3-1": "String",
    "3-2": "No",
    "3-3": "Specifies the message state. The options are:  \n  \n\\_ mark_seen  \n  \n\\_ typing_on  \n  \n\\_ typing_off  \n  \nNote: Either _text \\_or \\_attachment_ or \\_sender_action\\* is mandatory.",
    "4-0": "quick_replies",
    "4-1": "JSONArray",
    "4-2": "No",
    "4-3": "Specifies an options in the text message to reply back to the sender. When the quick reply is tapped, the message is sent with the option tapped. Once the message is sent, the options disappear.",
    "5-0": "messaging_type",
    "5-1": "String",
    "5-2": "No",
    "5-3": "Specifies the messaging type. The options are:  \n  \n\\_ RESPONSE - Use this messaging type if you are responding to a received message. This includes messages sent inside the 24-hour standard messaging window. For example, use this tag to respond if a person asks for a reservation confirmation or an status update.  \n  \n\\_ UPDATE - Use this messaging type if you are proactively sending a message and not in response to a received message. This includes messages sent inside the the 24-hour standard messaging window.  \n  \n\\* MESSAGE_TAG - Message is non-promotional and is being sent outside the 24-hour standard messaging window with a message tag. The message must match the allowed use case for the tag  \nSpecify the tag using 'tag' field.  \n  \nRefer to [Messenger Node](https://help.imiconnect.io/docs/messenger#supported-message-tags) to know the list of supported tags.",
    "6-0": "notifyurlAuthId",
    "6-1": "String",
    "6-2": "No",
    "6-3": "Unique Authentication ID."
  },
  "cols": 4,
  "rows": 7,
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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "options",
    "0-1": "object",
    "0-2": "yes",
    "0-3": "JSON Object",
    "1-0": "trackClicks",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "Optional. When enabled, this tracks all links in the HTML body unless a link is tagged as no-track-connect within the anchor tags. Link tracking is supported only for Email app assets configured using AWS SES.",
    "2-0": "shortenLinks",
    "2-1": "boolean",
    "2-2": "no",
    "2-3": "When enabled, this shortens any HTTPS links in the message request's body. The expiry of Shortened URL is 180 days.",
    "3-0": "domain",
    "3-1": "string",
    "3-2": "yes",
    "3-3": "It is the domain configuration for shortening the links.  \n_Note: 'domain' is mandatory only when 'options' object is used in the payload._",
    "4-0": "tags",
    "4-1": "string",
    "4-2": "yes",
    "4-3": "Reporting tags for tracking the  shortened link creates and clicks.",
    "5-0": "allowFallbackURL",
    "5-1": "string",
    "5-2": "yes",
    "5-3": "if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link."
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


### **Attachments - Media**

Media Attachments can be broadly categorised into the following:

- File
- Image
- Audio
- Video

**Common Attachment Parameters**

The parameters below are common to Media attachments and Template attachments, both.

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
    "0-3": "Specifies the type of the attachment. The options are:  \n  \n- file\n- image\n- audio\n- video\n- template",
    "1-0": "payload",
    "1-1": "JSONObject",
    "1-2": "Yes",
    "1-3": "Specifies the payload of attachment. The parameters of payload are:  \n  \ntemplate_type: There are three types of templates:  \n  \n- Generic\n- Button\n- Receiptelements: Specifies the parameters of the selected template type in an array."
  },
  "cols": 4,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/08959f4-generictemplate.gif",
        "generictemplate.gif",
        "Screenshot of Generic Template."
      ],
      "align": "center",
      "caption": "Screenshot of Generic Template."
    }
  ]
}
[/block]


**Generic Template Parameter Table**

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
    "1-0": "item_url",
    "1-1": "String",
    "1-2": "No",
    "1-3": "Specifies the URL that is opened when bubble is tapped.",
    "2-0": "image_url",
    "2-1": "String",
    "2-2": "No",
    "2-3": "Specifies the bubble image.",
    "3-0": "subtitle",
    "3-1": "String",
    "3-2": "No",
    "3-3": "Specifies the bubble subtitle. It has a limit of 80 characters.",
    "4-0": "buttons",
    "4-1": "JSONArray",
    "4-2": "No",
    "4-3": "Specifies a set of buttons that appears as call-to-actions. You can add up to 3 buttons only. The parameters are:  \n  \n\\_ type  \n  \n\\_ title  \n  \n\\_ url  \n  \n\\_ payload"
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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/98b53f8-buttontemplate.png",
        "buttontemplate.png",
        "Screenshot of Button Template."
      ],
      "align": "center",
      "caption": "Screenshot of Button Template."
    }
  ]
}
[/block]


**Button Template Parameter Table**:

| Parameter | Type      | Mandatory | Description                                                                                                                                                                          |
| :-------- | :-------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text      | String    | Yes       | The text that appears in the main body.                                                                                                                                              |
| buttons   | JSONArray | No        | Specifies a set of buttons that appears as call-to-actions. Click [button object reference](http://docs.imiconnect.com/reference#section-facebook-buttons)to view the button object. |

 You can add up to 3 buttons only. The parameters are:

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
    "0-3": "Specifies the value for button. The options are:  \n  \n\\_ web_url  \n  \n\\_ postback",
    "1-0": "title",
    "1-1": "String",
    "1-2": "Yes",
    "1-3": "Specifies the button title.",
    "2-0": "url",
    "2-1": "String",
    "2-2": "Yes",
    "2-3": "Specifies the web_url for buttons. It opens a browser when the button is tapped.",
    "3-0": "payload",
    "3-1": "String",
    "3-2": "Yes",
    "3-3": "When the postback button is clicked an event is raised that can be used to write rules."
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a3dadc0-receipttemplate.png",
        "receipttemplate.png",
        "Screenshot of Receipt Template."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Receipt Template."
    }
  ]
}
[/block]


**Receipt Template Parameter Table**

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "recipient_name",
    "0-1": "String",
    "0-2": "Yes",
    "0-3": "Specifies the recipients name.",
    "1-0": "order_number",
    "1-1": "String",
    "1-2": "Yes",
    "1-3": "specifies the order number.",
    "2-0": "currency",
    "2-1": "String",
    "2-2": "Yes",
    "2-3": "Specifies the currency for order.",
    "3-0": "payment_method",
    "3-1": "String",
    "3-2": "Yes",
    "3-3": "Specifies the payment method details.",
    "4-0": "timestamp",
    "4-1": "String",
    "4-2": "No",
    "4-3": "Specifies the timestamp of order. It must be a unique number.",
    "5-0": "order_url",
    "5-1": "String",
    "5-2": "No",
    "5-3": "Specifies the URL of order.",
    "6-0": "[elements](#section-facebook-receipt-elements)",
    "6-1": "JSONArray",
    "6-2": "Yes",
    "6-3": "Specifies the details of the order. The parameters are:  \n  \n\\_ title  \n  \n\\_ subtitle  \n  \n\\_ quantity  \n  \n\\_ price  \n  \n\\_ currency  \n  \n\\_ image_url",
    "7-0": "[address](#section-facebook-receipt-address)",
    "7-1": "JSONObject",
    "7-2": "No",
    "7-3": "Specifies the details of the shipping address. The parameters are:  \n  \n\\_ street_1  \n  \n\\_ street_2  \n  \n\\_ city  \n  \n\\_ postal_code",
    "8-0": "[summary](#section-facebook-receipt-summary)",
    "8-1": "JSONObject",
    "8-2": "Yes",
    "8-3": "Specifies the payment summary details. The parameters are:  \n  \n\\_ subtotal  \n  \n\\_ shipping_cost  \n  \n\\* total_tax",
    "9-0": "[adjustments](#section-facebook-receipt-adjustments)",
    "9-1": "JSONArray",
    "9-2": "No",
    "9-3": "Specifies the payment adjustments. The parameters are:  \n  \n\\_ name  \n  \n\\_ amount"
  },
  "cols": 4,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/22c1082-senderaction.png",
        "senderaction.png",
        "Screenshot of Sender Action."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Sender Action."
    }
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f8c9738-quickreplies.png",
        "quickreplies.png",
        "Screenshot of Quick Reply."
      ],
      "align": "center",
      "caption": "Screenshot of Quick Reply."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "content_type",
    "0-1": "String",
    "0-2": "Yes",
    "0-3": "Specifies the type of content. The options are:  \n  \n\\_ text  \n  \n\\_ location",
    "1-0": "title",
    "1-1": "String",
    "1-2": "Yes. This is applicable only when _content_type_ is set as _text_.",
    "1-3": "Specifies the caption for button.  You can add up to 20 characters as title.",
    "2-0": "payload",
    "2-1": "String",
    "2-2": "Yes. This is applicable only when _content_type_ is set as _text_.",
    "2-3": "Specifies the custom data that will be sent back to you through web hook.  The limit of this payload is 1000 characters.",
    "3-0": "image_url",
    "3-1": "String",
    "3-2": "No",
    "3-3": "Specifies the URL of the image sent as _quick_replies_."
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

> ❗️ Quick Reply image URL
> 
> The quick reply component currently requires the image_url as a mandatory parameter. We are working to gain a better understanding of this requirement and will have a resolution soon