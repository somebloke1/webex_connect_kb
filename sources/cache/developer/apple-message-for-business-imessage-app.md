# Apple Message for Business: iMessage App

Source: https://developers.webexconnect.io/reference/apple-message-for-business-imessage-app
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:42+00:00



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




> 📘 Note:
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
        "code": "{\n  \"response\": {\n    \"code\": \"7001\",\n    \"description\": \"Authentication failed.\",\n    \"transid\": \"7670c9a8-131f-4166-ac30-17f6109340d6\"\n  }\n}",
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
      "desc": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your webexconnect tenant.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "642be33394de830af2082ec4",
      "id": "642be33394de830af2082ec4"
    },
    {
      "name": "deliverychannel",
      "type": "string",
      "enumValues": "",
      "default": "AppleBusinessChat",
      "desc": "Channel used to send the message i.e., AppleBusinessChat in this case.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6431ab8f2d2a02006637c346",
      "id": "6431ab8f2d2a02006637c346"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The ID of the app asset that you can obtain from the Connect platform.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6431ab8f2d2a02006637c345",
      "id": "6431ab8f2d2a02006637c345"
    },
    {
      "name": "destination",
      "type": "array_object",
      "enumValues": "",
      "default": "",
      "desc": "User's Opaque ID that uniquely identifies a user and is specific to the business",
      "required": false,
      "in": "body",
      "ref": "destination",
      "_id": "6431ab8f2d2a02006637c344",
      "id": "6431ab8f2d2a02006637c344"
    },
    {
      "name": "channels",
      "type": "object",
      "enumValues": "",
      "default": "",
      "desc": "Channels object used for messaging.",
      "required": false,
      "in": "body",
      "ref": "channels",
      "_id": "6431ab8f2d2a02006637c343",
      "id": "6431ab8f2d2a02006637c343"
    },
    {
      "name": "correlationid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6431ab8f2d2a02006637c342",
      "id": "6431ab8f2d2a02006637c342"
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
      "_id": "6431ab8f2d2a02006637c341",
      "id": "6431ab8f2d2a02006637c341"
    },
    {
      "name": "notifyurl",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Configure a URL to get notifications on delivery reports for a Apple message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6431ab8f2d2a02006637c340",
      "id": "6431ab8f2d2a02006637c340"
    },
    {
      "name": "authorization",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "JSON Web Token (JWT) for authentication (e.g. bearer [token]) used alternatively to Service Key",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "6465f00930f3d20b8f5f1aea",
      "id": "6465f00930f3d20b8f5f1aea"
    },
    {
      "name": "notifyurlAuthId",
      "type": "string",
      "enumValues": "",
      "default": "No",
      "desc": "Unique Authentication ID.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "68c0664b524b5fc9a9ddaf22",
      "id": "68c0664b524b5fc9a9ddaf22"
    }
  ],
  "examples": {
    "codes": [
      {
        "code": "{\n\t\"deliverychannel\": \"AppleBusinessChat\",\n\t\"appid\": \"{{ambAppid}}\",\n\t\"destination\": [{\n\t\t\"abcUserId\": [\"{{ambUserId}}\"]\n\t}],\n    \"channels\": {\n        \"AppleBusinessChat\": {\n            \"type\": \"interactive\",\n            \"interactiveData\": {\n                \"appStoreId\": 1065520552,\n                \"appName\": \"API Explorer\",\n                \"teamId\": \"ADTJF9P7YB\",\n                \"extensionId\": \"com.imimobile.fcmconnect.MessagesExtension\",\n                \"url\": \"?name=samplepackage&extraCharge=1.5&deliveryDate=27-11-2022&destinationName=Home&street=1infiniteloop&state=CA&city=Hyderabad&country=IND&postalCode=500084&latitude=17.331686&longitude=78.030656&isMyLocation=false&isFinalDestination=false\",\n                \"appIcon\": \"https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg\",\n                \"sessionIdentifier\": \"76dbffd0-7f2b-4c92-a396-ae533d8a68e9\",\n                \"useLiveLayout\": \"true\",\n                \"images\": [\n                        {\n                            \"url\": \"https://media.croma.com/image/upload/v1663261950/Croma%20Assets/Small%20Appliances/Vacuum%20Cleaners/Images/259150_qs58bu.png\",\n                            \"identifier\": \"vimg1\"\n                        },\n                        {\n                            \"url\": \"https://media.croma.com/image/upload/v1632142476/Croma%20Assets/Small%20Appliances/Fryers%20and%20Grills/Images/243342_osqmdr.png\",\n                            \"identifier\": \"vimg2\"\n                        },\n                        {\n                            \"url\": \"https://res.cloudinary.com/jerrick/image/upload/f_jpg,fl_progressive,q_auto,w_1024/609a695d49932b001dce1ce5.jpg\",\n                            \"identifier\": \"vimg3\"\n                        }\n                    ],\n                \"receivedMessage\": {\n                    \"title\": \"Title of Bubble youtube\",\n                    \"subtitle\": \"Subtitle to be displayed under title\",\n                    \"imageTitle\": \"Title of image attachment\",\n                    \"imageIdentifier\": \"vimg3\",\n                    \"imageSubtitle\": \"Subtitle of the image attachment.\",\n                    \"secondarySubtitle\": \"Title that is aligned right\",\n                    \"tertiarySubtitle\": \"Subtitle that is aligned right\"\n                }\n            }\n        }\n    },\n\t\"correlationid\": \"\",\n\t\"callbackData\": \"\",\n  \"notifyurl\": \"\",\n  \"notifyurlAuthId\":\"TNPBXKT09U\" //Optional.\n}",
        "language": "json"
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67fe"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Apple Message for Business: iMessage App",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://api.{YourRegion}.webexconnect.io/resources/v1/messaging",
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
    "summary": "Apple Message for Business: iMessage App",
    "description": "Provides a unique user experience with custom interactive messages. _Note: Modify YourRegion in the URL to the right to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints)._",
    "operationId": "apple-message-for-business-imessage-app",
    "parameters": [
      {
        "name": "key",
        "in": "header",
        "description": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your webexconnect tenant.",
        "schema": {
          "type": "string"
        }
      },
      {
        "name": "authorization",
        "in": "header",
        "description": "JSON Web Token (JWT) for authentication (e.g. bearer [token]) used alternatively to Service Key",
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
            "properties": {
              "deliverychannel": {
                "type": "string",
                "description": "Channel used to send the message i.e., AppleBusinessChat in this case.",
                "default": "AppleBusinessChat"
              },
              "appid": {
                "type": "string",
                "description": "The ID of the app asset that you can obtain from the Connect platform."
              },
              "destination": {
                "type": "array",
                "description": "User's Opaque ID that uniquely identifies a user and is specific to the business",
                "items": {
                  "properties": {
                    "abcUserID": {
                      "type": "array",
                      "description": "User's Opaque ID -Note: For more information [refer](https://register.apple.com/resources/messages/messaging-documentation/faq)_",
                      "default": [],
                      "items": {
                        "type": "string"
                      }
                    }
                  },
                  "type": "object"
                }
              },
              "channels": {
                "type": "object",
                "description": "Channels object used for messaging.",
                "properties": {
                  "AppleBusinessChat": {
                    "type": "object",
                    "description": "JSON object for AppleBusinessChat configuration.",
                    "properties": {
                      "type": {
                        "type": "string",
                        "description": "Type of the outbound event. It can be text, typing_start, typing_end, richLink, or interactive"
                      },
                      "interactiveData": {
                        "type": "object",
                        "description": "JSON object for interactiveData configuration",
                        "required": [
                          "appName",
                          "url",
                          "appIcon",
                          "useLiveLayout"
                        ],
                        "properties": {
                          "appStoreId": {
                            "type": "integer",
                            "description": "The App Store identifier of the iMessage app.",
                            "format": "int32"
                          },
                          "appName": {
                            "type": "string",
                            "description": "The name of the iMessage app."
                          },
                          "teamId": {
                            "type": "string",
                            "description": "AppStore team ID of the iMessage App"
                          },
                          "extensionId": {
                            "type": "string",
                            "description": "AppStore extension bundle ID of the iMessage App"
                          },
                          "url": {
                            "type": "string",
                            "description": "A URL query string containing data that the Messages app sends to the iMessage app."
                          },
                          "appIcon": {
                            "type": "string",
                            "description": "It’ll be an image URL, which we will convert to base64-encoded string. URL validation should be in place. Only .png files are accepted"
                          },
                          "sessionIdentifier": {
                            "type": "string",
                            "description": "uuid for this interaction"
                          },
                          "useLiveLayout": {
                            "type": "boolean",
                            "description": "A Boolean that determines whether the Messages app should use Live Layout. The default is true. Default: true"
                          },
                          "images": {
                            "type": "array",
                            "description": "An array of image dictionaries.",
                            "items": {
                              "properties": {
                                "url": {
                                  "type": "string",
                                  "description": "Publicly accessible URL that is a direct link to the media."
                                },
                                "identifier": {
                                  "type": "string",
                                  "description": "A string field identifying the time item that must be unique within the payload, if more than one exists."
                                }
                              },
                              "type": "object"
                            }
                          },
                          "receivedMessage": {
                            "type": "object",
                            "description": "JSON object for received message configuration",
                            "properties": {
                              "title": {
                                "type": "string",
                                "description": "The main title that the Messages app shows in the header of the received message bubble. Limited to 512 characters."
                              },
                              "subtitle": {
                                "type": "string",
                                "description": "The subtitle that appears under the main title in the received message bubble. Limited to 512 characters."
                              },
                              "imageTitle": {
                                "type": "string",
                                "description": "The attached image's title. Limited to 512 characters. Only custom interactive messages use this key."
                              },
                              "imageIdentifier": {
                                "type": "string",
                                "description": "The identifier for one of the images specified in data.images."
                              },
                              "imageSubtitle": {
                                "type": "string",
                                "description": "The attached image's subtitle. Limited to 512 characters. Only custom interactive messages use this key."
                              },
                              "secondarySubtitle": {
                                "type": "string",
                                "description": "A right-aligned title. Limited to 512 characters. Only custom interactive messages use this key."
                              },
                              "tertiarySubtitle": {
                                "type": "string",
                                "description": "A right-aligned subtitle. Limited to 512 characters. Only custom interactive messages use this key."
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              },
              "correlationid": {
                "type": "string",
                "description": "The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request."
              },
              "callbackData": {
                "type": "string",
                "description": "Data that you have configured to receive on the notify Url. This is configured as a part of the request."
              },
              "notifyurl": {
                "type": "string",
                "description": "Configure a URL to get notifications on delivery reports for a Apple message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries."
              },
              "notifyurlAuthId": {
                "type": "string",
                "description": "Unique Authentication ID.",
                "default": "No"
              }
            }
          },
          "examples": {
            "Request Example": {
              "value": {
                "deliverychannel": "AppleBusinessChat",
                "appid": "{{ambAppid}}",
                "destination": [
                  {
                    "abcUserId": [
                      "{{ambUserId}}"
                    ]
                  }
                ],
                "channels": {
                  "AppleBusinessChat": {
                    "type": "interactive",
                    "interactiveData": {
                      "appStoreId": 1065520552,
                      "appName": "API Explorer",
                      "teamId": "ADTJF9P7YB",
                      "extensionId": "com.imimobile.fcmconnect.MessagesExtension",
                      "url": "?name=samplepackage&extraCharge=1.5&deliveryDate=27-11-2022&destinationName=Home&street=1infiniteloop&state=CA&city=Hyderabad&country=IND&postalCode=500084&latitude=17.331686&longitude=78.030656&isMyLocation=false&isFinalDestination=false",
                      "appIcon": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg",
                      "sessionIdentifier": "76dbffd0-7f2b-4c92-a396-ae533d8a68e9",
                      "useLiveLayout": "true",
                      "images": [
                        {
                          "url": "https://media.croma.com/image/upload/v1663261950/Croma%20Assets/Small%20Appliances/Vacuum%20Cleaners/Images/259150_qs58bu.png",
                          "identifier": "vimg1"
                        },
                        {
                          "url": "https://media.croma.com/image/upload/v1632142476/Croma%20Assets/Small%20Appliances/Fryers%20and%20Grills/Images/243342_osqmdr.png",
                          "identifier": "vimg2"
                        },
                        {
                          "url": "https://res.cloudinary.com/jerrick/image/upload/f_jpg,fl_progressive,q_auto,w_1024/609a695d49932b001dce1ce5.jpg",
                          "identifier": "vimg3"
                        }
                      ],
                      "receivedMessage": {
                        "title": "Title of Bubble youtube",
                        "subtitle": "Subtitle to be displayed under title",
                        "imageTitle": "Title of image attachment",
                        "imageIdentifier": "vimg3",
                        "imageSubtitle": "Subtitle of the image attachment.",
                        "secondarySubtitle": "Title that is aligned right",
                        "tertiarySubtitle": "Subtitle that is aligned right"
                      }
                    }
                  }
                },
                "correlationid": "",
                "callbackData": "",
                "notifyurl": "",
                "notifyurlAuthId": "TNPBXKT09U"
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
