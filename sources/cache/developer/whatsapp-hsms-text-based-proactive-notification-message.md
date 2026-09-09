# WhatsApp HSMs-Text based proactive notification message(Deprecated)

Source: https://developers.webexconnect.io/reference/whatsapp-hsms-text-based-proactive-notification-message
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




> ❗️ HSM Message Deprecation Alert
> 
> WhatsApp has announced that they will be deprecating the HSM message type sometime in early 2022. We recommend you to use Template message type instead of HSM messages, and migrate any existing HSMs to Template Message type. Unlike HSM which was meant to be used only for text messages, Template message type can be used to configure template messages of multiple components including text.

> 🚧 Some of the below values such as namespace, element_name, etc. are not available on imiconnect platform UI and need to be taken from WhatsApp Business Manager by reaching out to your regional support team. However, you wouldn't need it as we now recommend you to use Template message type instead of HSM.

> ❗️ WhatsApp Language Policy Change
> 
> Please note that the fallback language policy has been deprecated and the deterministic language policy is now the default policy. Do not use 'fallback' language policy while sending HSMs as it may lead to message delivery failures.

**_Localizable Parameters_**

When sending a Message Template, the hsm object is required. To define Message Templates, you specify a namespace and an element_name pair that identify a template. Templates have parameters that will be dynamically incorporated into the message. For the example used in this document, the Message Template looks like this:

| Parameters | Type             | Mandatory | Description                                                                                    |
| :--------- | :--------------- | :-------- | :--------------------------------------------------------------------------------------------- |
| default    | String           | Yes       | Default text if localization fails                                                             |
| currency   | currency object  | No        | If the currency object is used, it contains required parameters currency_code and amount_1000. |
| date_time  | date_time object | No        | If the date_time object is used, further definition of the date and time is required.          |

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
      "desc": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your Webex Connect tenant.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "6454be330d456709e6852188",
      "id": "6454be330d456709e6852188"
    },
    {
      "name": "deliverychannel",
      "type": "string",
      "enumValues": "",
      "default": "whatsapp",
      "desc": "Channel used to send the message i.e., WhatsApp in this case.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454be330d456709e6852187",
      "id": "6454be330d456709e6852187"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Contains the application ID",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6454be330d456709e6852186",
      "id": "6454be330d456709e6852186"
    },
    {
      "name": "destination",
      "type": "array_object",
      "enumValues": "",
      "default": "",
      "desc": "Unique user id for the recipient of the message on Apple Messages for Business.",
      "required": true,
      "in": "body",
      "ref": "bsuid",
      "_id": "6454be330d456709e6852185",
      "id": "6454be330d456709e6852185"
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
      "_id": "6454be330d456709e6852184",
      "id": "6454be330d456709e6852184"
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
      "_id": "6454be330d456709e6852183",
      "id": "6454be330d456709e6852183"
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
      "_id": "6454be330d456709e6852182",
      "id": "6454be330d456709e6852182"
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
      "_id": "6454be330d456709e6852181",
      "id": "6454be330d456709e6852181"
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
      "_id": "64647024aeab92083cb17880",
      "id": "64647024aeab92083cb17880"
    },
    {
      "name": "notifyurlAuthId",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "68c04aebb80e706ea3246c45",
      "id": "68c04aebb80e706ea3246c45"
    }
  ],
  "examples": {
    "codes": [
      {
        "code": "{  \n   \"deliverychannel\":\"whatsapp\",\n   \"appid\":\"<WAAppid>\",\n    \"destination\":[  \n      {  \n         \"waid\":[  \n            \"<waid>\"\n         ]\n      }\n   ],\n    \"channels\":{\n        \"OTT-Messaging\":{\n            \"wa\":{\n                \"type\":\"hsm\",\n                \"hsm\":{\n                    \"namespace\":\"\",\n                    \"element_name\":\"\",\n                    \"language\":{\n                        \"code\":\"en_gb\",\n                        \"policy\":\"deterministic\"\n                    },\n                    \"localizable_params\":[\n                        {\n                            \"default\":\"$10\"\n                        },\n                        {\n                            \"default\":\"1234\"\n                        }\n                    ]\n                }\n            }\n        }\n    },\n    \"correlationid\": \"\",\n\t\"callbackData\": \"\",\n  \"notifyurl\": \"\",\n  \"notifyurlAuthId\": \"TNPBXKT09U\" //Optional.\n}",
        "language": "json"
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67f8"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "WhatsApp HSMs - Text based proactive notification message",
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
    "summary": "WhatsApp HSMs-Text based proactive notification message(Deprecated)",
    "description": "Send business initiated messages using message templates beyond the 24 hour window to your customers. This message type includes text based templates without a header, footer or buttons.  _Note: Modify YourRegion in the URL to the right to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints)._",
    "operationId": "whatsapp-hsms-text-based-proactive-notification-message",
    "parameters": [
      {
        "name": "key",
        "in": "header",
        "description": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your Webex Connect tenant.",
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
                "description": "Channel used to send the message i.e., WhatsApp in this case.",
                "default": "whatsapp"
              },
              "appid": {
                "type": "string",
                "description": "Contains the application ID"
              },
              "destination": {
                "type": "array",
                "description": "Unique user id for the recipient of the message on Apple Messages for Business.",
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
                            "description": "Identifies WhatsApp message type",
                            "default": "hsm"
                          },
                          "hsm": {
                            "type": "object",
                            "description": "JSON object for hsm configuration",
                            "required": [
                              "namespace",
                              "element_name"
                            ],
                            "properties": {
                              "namespace": {
                                "type": "string",
                                "description": "The namespace that will be used."
                              },
                              "element_name": {
                                "type": "string",
                                "description": "The element name that indicates which template to use within the namespace."
                              },
                              "language": {
                                "type": "object",
                                "description": "JSON object for language configuration",
                                "required": [
                                  "code",
                                  "policy"
                                ],
                                "properties": {
                                  "code": {
                                    "type": "string",
                                    "description": "The code of the language or locale to use — Accepts both language and language_locale formats (e.g., en and en_US)."
                                  },
                                  "policy": {
                                    "type": "string",
                                    "description": "Options:  deterministic — Deliver the Message Template in exactly the language and locale asked for.  fallback (Deprecated) — Deliver the Message Template in the language that matches the user's language/locale setting on the device. If one can't be found, deliver using the specified fallback language."
                                  }
                                }
                              },
                              "localizable_params": {
                                "type": "object",
                                "description": "JSON object for localizable_params configuration",
                                "properties": {
                                  "default": {
                                    "type": "string",
                                    "description": "default value of the parameters"
                                  }
                                }
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
                "description": "Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries."
              },
              "notifyurlAuthId": {
                "type": "string"
              }
            }
          },
          "examples": {
            "Request Example": {
              "value": {
                "deliverychannel": "whatsapp",
                "appid": "<WAAppid>",
                "destination": [
                  {
                    "waid": [
                      "<waid>"
                    ]
                  }
                ],
                "channels": {
                  "OTT-Messaging": {
                    "wa": {
                      "type": "hsm",
                      "hsm": {
                        "namespace": "",
                        "element_name": "",
                        "language": {
                          "code": "en_gb",
                          "policy": "deterministic"
                        },
                        "localizable_params": [
                          {
                            "default": "$10"
                          },
                          {
                            "default": "1234"
                          }
                        ]
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
