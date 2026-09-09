# WhatsApp Contacts Messages

Source: https://developers.webexconnect.io/reference/whatsapp-contacts-messages
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
      "name": "deliverychannel",
      "type": "string",
      "enumValues": "",
      "default": "whatsapp",
      "desc": "Channel used to send the message i.e., WhatsApp in this case.",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "6453ce70c44a64000aff1585",
      "id": "6453ce70c44a64000aff1585"
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
      "_id": "6453ce70c44a64000aff1584",
      "id": "6453ce70c44a64000aff1584"
    },
    {
      "name": "destination",
      "type": "array_object",
      "enumValues": "",
      "default": "",
      "desc": "Unique user id for the recipient of the message on WhatsApp.",
      "required": true,
      "in": "body",
      "ref": "bsuid",
      "_id": "6453ce70c44a64000aff1583",
      "id": "6453ce70c44a64000aff1583"
    },
    {
      "name": "channels",
      "type": "object",
      "enumValues": "",
      "default": "",
      "desc": "Channels used for incoming messages.",
      "required": false,
      "in": "body",
      "ref": "channels",
      "_id": "6453ce70c44a64000aff1581",
      "id": "6453ce70c44a64000aff1581"
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
      "_id": "6453ce70c44a64000aff1580",
      "id": "6453ce70c44a64000aff1580"
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
      "_id": "6453ce70c44a64000aff157f",
      "id": "6453ce70c44a64000aff157f"
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
      "_id": "6453ce70c44a64000aff157e",
      "id": "6453ce70c44a64000aff157e"
    },
    {
      "name": "key",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Applicable when you want to use service key for API authentication. Available under API tab within a service in your WebexConnect tenant.",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "6453ce70c44a64000aff157d",
      "id": "6453ce70c44a64000aff157d"
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
      "_id": "64647147fc5bbe00447b4ef5",
      "id": "64647147fc5bbe00447b4ef5"
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
      "_id": "68c043243138060f4ff2483b",
      "id": "68c043243138060f4ff2483b"
    }
  ],
  "examples": {
    "codes": [
      {
        "code": "{\n    \"deliverychannel\": \"whatsapp\", //Mandatory. Channel used to send the message i.e., WhatsApp in this case.\n    \"appid\": \"{{WAAppid}}\", //Mandatory. Contains the applicationid\n    \"destination\": [\n        {\n            \"waid\": [\n                \"{{waid}}\" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.\n            ]\n        }\n    ],\n    \"channels\": {\n        \"OTT-Messaging\": {\n            \"wa\": {\n                \"type\": \"contacts\", //Mandatory. Specify the message type\n                \"contacts\": [\n                    {\n                        \"addresses\": [ //Optional.\n                            {\n                                \"city\": \"\", //City name\n                                \"country\": \"\", //Full country name\n                                \"country_code\": \"\", //Two-letter country abbreviation\n                                \"state\": \"\", //State abbreviation\n                                \"street\": \"\", //Street number and name\n                                \"type\": \"\", //Standard Values: HOME, WORK\n                                \"zip\": \"\" //ZIP code\n                            }\n                        ],\n                        \"birthday\": \"\", //Optional. YYYY-MM-DD formatted string\n                        \"emails\": [ //Optional.\n                            {\n                                \"email\": \"\", //Email address\n                                \"type\": \"\" //Standard Values: HOME, WORK\n                            }\n                        ],\n                        \"name\": { //Mandatory. At least one of the optional parameters needs to be included along with the formatted_name parameter.\n                            \"first_name\": \"\", //First name\n                            \"formatted_name\": \"\", //Mandatory. Full name as it normally appears.\n                            \"last_name\": \"\", //Last name\n                            \"middle_name\": \"\", //Middle name\n                            \"prefix\": \"\", //Name prefix\n                            \"suffix\": \"\" //Name suffix\n                        },\n                        \"org\": { //Optional.\n                            \"company\": \"\", //Name of the contact's company\n                            \"department\": \"\", //Name of the contact's department\n                            \"title\": \"\" //Contact's business title\n                        },\n                        \"phones\": [ //Optional.\n                            {\n                                \"phone\": \"\", //Contact phone number\n                                \"type\": \"\" //Standard Values: CELL, MAIN, IPHONE, HOME, WORK\n                            }\n                        ],\n                        \"urls\": [ //Optional.\n                            {\n                                \"url\": \"\", //URL\n                                \"type\": \"\" //Standard Values: HOME, WORK\n                            }\n                        ]\n                    }\n                ],\n                \"identity_key_hash\": \"<identity-key-hash-value>\" //Optional. Pass this value to validate the identity of your customer.\n            }\n        }\n    },\n    \"correlationid\": \"\", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.\n    \"callbackData\": \"\", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.\n     \"notifyurl\": \"\" //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.\n     \"notifyurlAuthId\": \"TNPBXKT09U\" //Optional.\n}",
        "language": "json",
        "name": "WhatsApp Contact"
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67f5"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "WhatsApp Contacts Message",
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
    "summary": "WhatsApp Contacts Messages",
    "description": "Share contacts on WhatsApp to your customers. This message type can be sent within 24 hour window after a customer initiated message.   _Note: Modify YourRegion in the URL to the right to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints)._",
    "operationId": "whatsapp-contacts-messages",
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
                "description": "Channel used to send the message i.e., WhatsApp in this case.",
                "default": "whatsapp"
              },
              "appid": {
                "type": "string",
                "description": "Contains the applicationid"
              },
              "destination": {
                "type": "array",
                "description": "Unique user id for the recipient of the message on WhatsApp.",
                "items": {
                  "properties": {}
                }
              },
              "channels": {
                "type": "object",
                "description": "Channels used for incoming messages.",
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
                            "description": "Specify the message type",
                            "default": "contacts"
                          },
                          "identity_key_hash": {
                            "type": "string",
                            "description": "Unique identity hash key to track the messages sent to the authorized customer."
                          },
                          "contacts": {
                            "type": "array",
                            "description": "JSON object for contact details configuration",
                            "items": {
                              "properties": {
                                "addresses": {
                                  "type": "array",
                                  "description": "JSON Object for Address configuration",
                                  "items": {
                                    "properties": {
                                      "city": {
                                        "type": "string",
                                        "description": "City name"
                                      },
                                      "country": {
                                        "type": "string",
                                        "description": "Full country name"
                                      },
                                      "country_code": {
                                        "type": "string",
                                        "description": "Two-letter country abbreviation"
                                      },
                                      "state": {
                                        "type": "string",
                                        "description": "State abbreviation"
                                      },
                                      "street": {
                                        "type": "string",
                                        "description": "Street number and name"
                                      },
                                      "type": {
                                        "type": "string",
                                        "description": "Standard Values: HOME, WORK"
                                      },
                                      "zip": {
                                        "type": "string",
                                        "description": "ZIP code"
                                      }
                                    },
                                    "type": "object"
                                  }
                                },
                                "birthday": {
                                  "type": "string",
                                  "description": "YYYY-MM-DD formatted string"
                                },
                                "emails": {
                                  "type": "array",
                                  "description": "Contact email address(es)",
                                  "items": {
                                    "properties": {
                                      "email": {
                                        "type": "string",
                                        "description": "Email address"
                                      },
                                      "type": {
                                        "type": "string",
                                        "description": "Standard Values: HOME, WORK"
                                      }
                                    },
                                    "type": "object"
                                  }
                                },
                                "name": {
                                  "type": "object",
                                  "description": "Full contact name",
                                  "required": [
                                    "formatted_name"
                                  ],
                                  "properties": {
                                    "first_name": {
                                      "type": "string",
                                      "description": "First name"
                                    },
                                    "formatted_name": {
                                      "type": "string",
                                      "description": "Full name as it normally appears. At least one of the optional parameters needs to be included along with the formatted_name parameter."
                                    },
                                    "last_name": {
                                      "type": "string",
                                      "description": "Last name"
                                    }
                                  }
                                },
                                "org": {
                                  "type": "object",
                                  "description": "Contact organization information",
                                  "properties": {
                                    "company": {
                                      "type": "string",
                                      "description": "Name of the contact's company"
                                    },
                                    "department": {
                                      "type": "string",
                                      "description": "Name of the contact's department"
                                    },
                                    "title": {
                                      "type": "string",
                                      "description": "Contact's business title"
                                    }
                                  }
                                },
                                "phone": {
                                  "type": "array",
                                  "description": "Contact phone number(s)",
                                  "items": {
                                    "properties": {
                                      "phone": {
                                        "type": "string",
                                        "description": "Contact phone number"
                                      },
                                      "type": {
                                        "type": "string",
                                        "description": "Standard Values: CELL, MAIN, IPHONE, HOME, WORK"
                                      },
                                      "wa_id": {
                                        "type": "string",
                                        "description": "WhatsApp ID"
                                      }
                                    },
                                    "type": "object"
                                  }
                                },
                                "urls": {
                                  "type": "array",
                                  "description": "Contact URL(s)",
                                  "items": {
                                    "properties": {
                                      "url": {
                                        "type": "string",
                                        "description": "URL"
                                      },
                                      "type": {
                                        "type": "string",
                                        "description": "Standard Values: HOME, WORK"
                                      }
                                    },
                                    "type": "object"
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
