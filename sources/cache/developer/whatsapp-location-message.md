# WhatsApp Location Message

Source: https://developers.webexconnect.io/reference/whatsapp-location-message
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
      "_id": "6453a588fb07fe11759bd55b",
      "id": "6453a588fb07fe11759bd55b"
    },
    {
      "name": "deliverychannel",
      "type": "string",
      "enumValues": "",
      "default": "whatsapp",
      "desc": "Channel used to send the message i.e., whatsapp in this case.",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "6453a588fb07fe11759bd55a",
      "id": "6453a588fb07fe11759bd55a"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Contains the applicationid",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "6453a588fb07fe11759bd559",
      "id": "6453a588fb07fe11759bd559"
    },
    {
      "name": "destination",
      "type": "array_object",
      "enumValues": "",
      "default": "",
      "desc": "Unique user id for the recipient of the message on whatsapp.",
      "required": true,
      "in": "body",
      "ref": "bsuid",
      "_id": "6453a588fb07fe11759bd558",
      "id": "6453a588fb07fe11759bd558"
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
      "_id": "6453a588fb07fe11759bd555",
      "id": "6453a588fb07fe11759bd555"
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
      "_id": "6453a588fb07fe11759bd554",
      "id": "6453a588fb07fe11759bd554"
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
      "_id": "6453a588fb07fe11759bd553",
      "id": "6453a588fb07fe11759bd553"
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
      "_id": "6453a588fb07fe11759bd552",
      "id": "6453a588fb07fe11759bd552"
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
      "_id": "64646d063324540034584569",
      "id": "64646d063324540034584569"
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
      "_id": "68c10c14ecc2d04c8c2a0031",
      "id": "68c10c14ecc2d04c8c2a0031"
    }
  ],
  "examples": {
    "codes": [
      {
        "code": "{\n    \"deliverychannel\": \"whatsapp\", //Mandatory. Channel used to send the message i.e., whatsapp in this case.\n    \"appid\": \"{{WAAppid}}\", //Mandatory. Contains the applicationid\n    \"destination\": [\n        {\n            \"waid\": [\n                \"{{waid}}\" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.\n            ]\n        }\n    ],\n    \"channels\": {\n        \"OTT-Messaging\": {\n            \"wa\": {\n                \"type\": \"location\", //Mandatory. Specifies the message type. The value needs to be 'location' for sending location messages.\n                \"location\": {\n                    \"longitude\": 0.0, //Mandatory. Longitude of the location\n                    \"latitude\": 0.0, //Mandatory. Latitude of the location\n                    \"name\": \"\", //Optional. Name of the location\n                    \"address\": \"\" //Optional. Address of the location. Only displayed if name is present.\n                },\n                \"identity_key_hash\": \"<identity-key-hash-value>\" //Optional. Pass this value to validate the identity of your customer.\n            }\n        }\n    },\n    \"correlationid\": \"\", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.\n    \"callbackData\": \"\", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.\n    \"notifyurl\": \"\" //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.\n    \"notifyurlAuthId\": \"TNPBXKT09U\" //Optional.\n}",
        "language": "json",
        "name": "WhatsApp Location"
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67f4"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "WhatsApp Location Message",
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
    "summary": "WhatsApp Location Message",
    "description": "Share location as a message on WhatsApp to your customers. This message type can be sent within 24 hour window after a customer initiated message. _Note: Modify YourRegion in the URL to the right to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints)._",
    "operationId": "whatsapp-location-message",
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
              "deliverychannel",
              "appid",
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
                "description": "Unique user id for the recipient of the message on whatsapp.",
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
                    "description": "JSON object for social channel message configuration",
                    "properties": {
                      "wa": {
                        "type": "object",
                        "description": "JSON object for WhatsApp message configuration",
                        "required": [
                          "type"
                        ],
                        "properties": {
                          "type": {
                            "type": "string",
                            "description": "Specifies the message type. The value needs to be 'location' for sending location messages.",
                            "default": "location"
                          },
                          "location": {
                            "type": "object",
                            "description": "Configure location details as part of location JSON object.",
                            "required": [
                              "longitude",
                              "latitude"
                            ],
                            "properties": {
                              "longitude": {
                                "type": "string",
                                "description": "Longitude of the location"
                              },
                              "latitude": {
                                "type": "string",
                                "description": "Latitude of the location"
                              },
                              "name": {
                                "type": "string",
                                "description": "Name of the location"
                              },
                              "address": {
                                "type": "string",
                                "description": "Address of the location. Only displayed if name is present."
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
