# WhatsApp Reply Buttons

Source: https://developers.webexconnect.io/reference/whatsapp-reply-buttons
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:43+00:00



<div></div>

<style>
  .rm-ReferenceMain .rm-Article {
    display: flex;
    flex-direction: column;
}
 
.rm-ParamContainer {
    order: 1;
}
 
.field-description, .markdown-body {
    order: 2;
}
 
.rm-ReferenceMain .markdown-body {
  margin-top: 10px
}
 
.rm-ReferenceMain .rm-Article .rm-APISectionHeader {
    order: 3;
}
 
[class^="APIResponseSchemaPicker"] {
    order: 4;
}
 
[class^="Footer-desktop"] {
  order: 5
}

</style>




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

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "post",
  "url": "/",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{\n    \"response\": [\n        {\n            \"code\": \"1001\",\n            \"transid\": \"3f09295d-9eb3-4c9e-8ee8-a3272e5f00c1\",\n            \"description\": \"Queued\"\n        }\n    ]\n}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{\n  \"response\": {\n    \"code\": \"7001\",\n    \"description\": \"Authentication failed.\",\n    \"transid\": \"7670c9a8-131f-4166-ac30-17f6109340d6\"\n  }\n}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [
    {
      "name": "key",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your WebexConnect tenant.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "6454bccd33840d000bfddec3",
      "id": "6454bccd33840d000bfddec3"
    },
    {
      "name": "deliverychannel",
      "type": "string",
      "enumValues": "",
      "default": "whatsapp",
      "desc": "Channel used to send the message i.e., whatsapp in this case.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454bccd33840d000bfddec2",
      "id": "6454bccd33840d000bfddec2"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Contains the applicationid",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454bccd33840d000bfddec1",
      "id": "6454bccd33840d000bfddec1"
    },
    {
      "name": "destination",
      "type": "array_object",
      "enumValues": "",
      "default": "",
      "desc": "Unique user id for the recipient of the message on whatsapp",
      "required": true,
      "in": "body",
      "ref": "bsuid",
      "_id": "6454bccd33840d000bfddec0",
      "id": "6454bccd33840d000bfddec0"
    },
    {
      "name": "channels",
      "type": "object",
      "enumValues": "",
      "default": "",
      "desc": "Channels used for incoming messages",
      "required": false,
      "in": "body",
      "ref": "channels",
      "_id": "6454bccd33840d000bfddebf",
      "id": "6454bccd33840d000bfddebf"
    },
    {
      "name": "correlationid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454bccd33840d000bfddebe",
      "id": "6454bccd33840d000bfddebe"
    },
    {
      "name": "callbackData",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Data that you have configured to receive on the notify Url. This is configured as a part of the request.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454bccd33840d000bfddebd",
      "id": "6454bccd33840d000bfddebd"
    },
    {
      "name": "notifyurl",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454bccd33840d000bfddebc",
      "id": "6454bccd33840d000bfddebc"
    },
    {
      "name": "authorization",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "JSON Web Token (JWT) for authentication (e.g. bearer <token>) used alternatively to Service Key.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "646470e13356db0011b23bf7",
      "id": "646470e13356db0011b23bf7"
    },
    {
      "name": "notifyurlAuthId",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Unique Authentication ID.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "68c10cb7cfa53bec9ee0f60e",
      "id": "68c10cb7cfa53bec9ee0f60e"
    }
  ],
  "examples": {
    "codes": [
      {
        "code": "{\n    \"deliverychannel\": \"whatsapp\", //Mandatory. Channel used to send the message i.e., whatsapp in this case.\n    \"appid\": \"{{WAAppid}}\", //Mandatory. Contains the applicationid\n    \"destination\": [\n        {\n            \"waid\": [\n                \"{{waid}}\" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.\n            ]\n        }\n    ],\n    \"channels\": {\n        \"OTT-Messaging\": {\n            \"wa\": {\n                \"type\": \"reply\", //Mandatory. Specify the message type.\n                \"reply\": {\n                    \"header\": {\n                        \"type\": \"text/document/video/image\", //Mandatory. Specifies the header type. Supported values (text/document/video/image)\n                        \"text\": \"Reply button your text\", //Mandatory. Contains the text for the header. Maximum of 60 characters is supported for text.\n                        \"document\": {\n                            \"url\": \"\",\n                            \"provider\": {\n                                \"name\": \"provider-name\"\n                            },\n                            \"filename\": \"some-file-name\"\n                        }, //OR//\n                        \"video\": {\n                            \"url\": \"\",\n                            \"provider\": {\n                                \"name\": \"provider-name\"\n                            }\n                        }, //OR//\n                        \"image\": {\n                            \"url\": \"\",\n                            \"provider\": {\n                                \"name\": \"provider-name\"\n                            }\n                        }\n                    },\n                    \"body\": {\n                        \"text\": \"\" //Mandatory. Body of the message. Maximum of 1024 characters is supported.\n                    },\n                    \"footer\": { //Optional.\n                        \"text\": \"\" //Optional. An object with the footer of the message. The footer object contains the following field: textstring – Required if footer is present. The footer content. Emojis, markdown, and links are supported. Maximum length: 60 characters.\n                    },\n                    \"action\": {\n                        \"buttons\": [\n                            {\n                                \"type\": \"reply\", //Mandatory. specifies of the type of action\n                                \"reply\": {\n                                    \"id\": \"ButtonId1\", //Mandatory. key-value pair. You can define your custom key and pass respective value. In this example custom key is 'id' and 'title' and respective value is 'ButtonId1'\n                                    \"title\": \"First Button\" //Mandatory. key-value pair. You can define your custom key and pass respective value. In this example custom key is 'title' and 'title' and respective value is 'First Button'\n                                }\n                            }\n                        ]\n                    }\n                }\n            }\n        }\n    },\n    \"correlationid\": \"\", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.\n    \"callbackData\": \"\", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.\n    \"notifyurl\": \"\" //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.\n    \"notifyurlAuthId\": \"TNPBXKT09U\" //Optional.\n}",
        "language": "json",
        "name": "WhatsApp Reply Buttons "
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67f7"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "WhatsApp Reply Buttons",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://{YourRegion}.webexconnect.io/resources/v1/messaging",
      "variables": {
        "YourRegion": {
          "default": "YourRegion"
        }
      }
    }
  ],
  "security": [
    {}
  ],
  "path": "/",
  "method": "post",
  "path_parameters": [],
  "operation": {
    "summary": "WhatsApp Reply Buttons",
    "description": "Reply Buttons Message includes up to 3 options —each option is a button. This type of message offers a quicker way for users to make a selection from a menu when interacting with a business. Reply buttons have the same user experience as interactive templates with buttons.  _Note: Modify YourRegion in the URL to the right to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints)._",
    "operationId": "whatsapp-reply-buttons",
    "parameters": [
      {
        "name": "key",
        "in": "header",
        "description": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your WebexConnect tenant.",
        "schema": {
          "type": "string"
        }
      },
      {
        "name": "authorization",
        "in": "header",
        "description": "JSON Web Token (JWT) for authentication (e.g. bearer <token>) used alternatively to Service Key.",
        "schema": {
          "type": "string"
        }
      }
    ],
    "requestBody": {
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "required": [
              "destination"
            ],
            "properties": {
              "deliverychannel": {
                "type": "string",
                "description": "Channel used to send the message i.e., whatsapp in this case.",
                "default": "whatsapp"
              },
              "appid": {
                "type": "string",
                "description": "Contains the applicationid"
              },
              "destination": {
                "type": "array",
                "description": "Unique user id for the recipient of the message on whatsapp",
                "items": {
                  "properties": {}
                }
              },
              "channels": {
                "type": "object",
                "description": "Channels used for incoming messages",
                "properties": {
                  "OTT-Messaging": {
                    "type": "object",
                    "description": "Channels used for incoming messages",
                    "properties": {
                      "wa": {
                        "type": "object",
                        "description": "JSON object for WhatsApp message configuration",
                        "properties": {
                          "type": {
                            "type": "string",
                            "description": "Specify the message type.",
                            "default": "reply"
                          },
                          "reply": {
                            "type": "object",
                            "description": "Configure the reply message",
                            "properties": {
                              "header": {
                                "type": "object",
                                "description": "Header content displayed on top of a message",
                                "required": [
                                  "type"
                                ],
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "description": "Specifies the header type. Supported values (text/document/video/image)_Note: For more information refer [section](https://developers.imiconnect.io/v6.3.0/reference/whatsapp-reply-buttons#whatsapp-reply-buttons--videoimage)._._"
                                  },
                                  "text": {
                                    "type": "string",
                                    "description": "Configure if header type is 'text'. Maximum of 60 characters is supported for header text."
                                  },
                                  "document": {
                                    "type": "object",
                                    "description": "Configure if header type is 'document'.",
                                    "properties": {
                                      "url": {
                                        "type": "string",
                                        "description": "Contains the URL of the document"
                                      },
                                      "filename": {
                                        "type": "string",
                                        "description": "Specifies file name"
                                      }
                                    }
                                  },
                                  "image": {
                                    "type": "object",
                                    "description": "Configure if header type is 'image'.",
                                    "required": [
                                      "url"
                                    ],
                                    "properties": {
                                      "url": {
                                        "type": "string",
                                        "description": "Contains the URL of the image"
                                      },
                                      "provider": {
                                        "type": "object",
                                        "description": "JSON object for provider configuration.",
                                        "properties": {
                                          "name": {
                                            "type": "string",
                                            "description": "provider-name"
                                          }
                                        }
                                      }
                                    }
                                  },
                                  "video": {
                                    "type": "object",
                                    "description": "Configure if header type is 'video'.",
                                    "properties": {
                                      "url": {
                                        "type": "string",
                                        "description": "Contains the URL of the video"
                                      },
                                      "provider": {
                                        "type": "object",
                                        "description": "JSON object for configuring provider",
                                        "properties": {
                                          "name": {
                                            "type": "string",
                                            "description": "provider-name"
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              },
                              "body": {
                                "type": "object",
                                "description": "An object with the body of the message.  The body object contains the following field: textstring – Required if body is present. The content of the message. Emojis and markdown are supported. Maximum length: 1024 characters.",
                                "properties": {
                                  "text": {
                                    "type": "string",
                                    "description": "Body of the message. Maximum of 1024 characters is supported."
                                  }
                                }
                              },
                              "footer": {
                                "type": "object",
                                "description": "Optional. An object with the footer of the message.  The footer object contains the following field: textstring – Required if footer is present. The footer content. Emojis, markdown, and links are supported. Maximum length: 60 characters.",
                                "properties": {
                                  "text": {
                                    "type": "string",
                                    "description": "Contains the footer text message."
                                  }
                                }
                              },
                              "action": {
                                "type": "object",
                                "description": "JSON object for action configuration. Action you want the user to perform after reading the message.",
                                "properties": {
                                  "buttons": {
                                    "type": "array",
                                    "items": {
                                      "properties": {
                                        "type": {
                                          "type": "string",
                                          "description": "Configure 'reply' as the type for reply buttons. This is the only supported value at the moment.",
                                          "default": "reply"
                                        },
                                        "reply": {
                                          "type": "object",
                                          "description": "Configure the Reply Button Id and Button Title as part of this object.",
                                          "properties": {
                                            "id": {
                                              "type": "string"
                                            },
                                            "title": {
                                              "type": "string"
                                            }
                                          }
                                        }
                                      },
                                      "type": "object"
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      },
                      "identity_key_hash": {
                        "type": "string",
                        "description": "Pass this value to validate the identity of your customer. More details on Identity Key Hash feature are documented [here](https://help.webexconnect.io/docs/whatsapp-node#identity-hash-field)."
                      }
                    }
                  }
                }
              },
              "correlationid": {
                "type": "string",
                "description": "The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request."
              },
              "callbackData": {
                "type": "string",
                "description": "Data that you have configured to receive on the notify Url. This is configured as a part of the request."
              },
              "notifyurl": {
                "type": "string",
                "description": "Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries."
              },
              "notifyurlAuthId": {
                "type": "string",
                "description": "Unique Authentication ID."
              }
            }
          }
        }
      }
    },
    "responses": {
      "200": {
        "description": "200",
        "content": {
          "application/json": {
            "examples": {
              "Result": {
                "value": "{\n    \"response\": [\n        {\n            \"code\": \"1001\",\n            \"transid\": \"3f09295d-9eb3-4c9e-8ee8-a3272e5f00c1\",\n            \"description\": \"Queued\"\n        }\n    ]\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "response": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "code": {
                        "type": "string",
                        "example": "1001"
                      },
                      "transid": {
                        "type": "string",
                        "example": "3f09295d-9eb3-4c9e-8ee8-a3272e5f00c1"
                      },
                      "description": {
                        "type": "string",
                        "example": "Queued"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "400": {
        "description": "400",
        "content": {
          "application/json": {
            "examples": {
              "Result": {
                "value": "{\n  \"response\": {\n    \"code\": \"7001\",\n    \"description\": \"Authentication failed.\",\n    \"transid\": \"7670c9a8-131f-4166-ac30-17f6109340d6\"\n  }\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "response": {
                  "type": "object",
                  "properties": {
                    "code": {
                      "type": "string",
                      "example": "7001"
                    },
                    "description": {
                      "type": "string",
                      "example": "Authentication failed."
                    },
                    "transid": {
                      "type": "string",
                      "example": "7670c9a8-131f-4166-ac30-17f6109340d6"
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "deprecated": false
  },
  "components": {
    "securitySchemes": {}
  }
}
```
