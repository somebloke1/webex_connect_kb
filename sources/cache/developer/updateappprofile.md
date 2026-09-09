# Update App Profile

Source: https://developers.webexconnect.io/reference/updateappprofile
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:50+00:00

> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

> 📘 
> 
> For data privacy and security reasons, the REST API is served over encrypted HTTPS. The standard HTTP is not supported.

## **Status Codes**

This API may return the following response codes:

| Response Code | Message                                                       | Description                                                                                    |
| :------------ | :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------- |
| 1000          | Queued                                                        | Returned when the request is queued                                                            |
| 1002          | Partial success                                               | Returned when one or more sub-transactions within a batch request fail                         |
| 7000          | Invalid JSON                                                  | Returned when an invalid JSON request is sent                                                  |
| 7001          | Authentication failed                                         | Returned when an invalid service key or profile key is provided in the request                 |
| 7002          | Service Key Missing                                           | Returned when the parameter key is missing in the message request                              |
| 7003          | Mandatory parameters missing                                  | Returned when the mandatory parameters configured in the custom event are missing              |
| 7006          | Internal error occurred                                       | Returned when an internal error occurs                                                         |
| 7010          | Source IP is not in the allowed list                          | Returned when a request is sent from an IP that is not n the allowed list in Webex Connect      |
| 7011          | Invalid Attribute Value                                       | Returned when an invalid value is provided for the customer or app profile _Attributes_ object |
| 7018          | Invalid app profile or app profile not linked to this client. | Returned when an application master profile does not exist                                     |

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "settings": "",
  "url": "/customerappprofile/<app ID>",
  "auth": "required",
  "examples": {
    "codes": [
      {
        "code": "-X PUT https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\n-H \"Content-Type : application/json\"\n-H \"key : {profilekey}\"\n",
        "language": "curl"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'PUT',\n          uri: ' https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}',\n          headers: {\n            'Content-Type': 'application/json',\n\t'key': ' Profile key present in tenant setting '\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.put(\"https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\",\n    :headers => {'Content-Type' => 'application/json',\n\t'key' => ' Profile key present in tenant setting’})\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"key\", \"Profile key present in tenant setting\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\"\n\nheaders = {'Content-Type': 'application/json', 'key': ' Profile key present in tenant setting '}\n\nresponse = requests.request(\"PUT\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"9876\",\n        \"Attributes\": {\n            \"verified\": \"1\",\n            \"status\": \"1\",\n            \"createdOn\": \"2016-07-11 17:02:51\",\n            \"channel\": \"fb\",\n            \"name\": \"Joe James1\",\n            \"profile_pic\": \"https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/v/t1.0-1/s200x200/10354686_10150004552801856_220367501106153455_n.jpg?oh=246adb8e3d7dc948f4d8025495fbf8dd&oe=57FD4150&__gda__=1476209436_66628acd9a55e42920bb3f0a823e1eac\",\n            \"psid\": \"1223275837725015\",\n            \"updatedOn\": \"2016-07-11 17:17:06\"\n        }\n    }]\n}",
        "language": "json",
        "name": "Facebook"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"9876\",\n        \"Attributes\": {\n            \"verified\": \"1\",\n            \"status\": \"1\",\n            \"channel\": \"twitter\",\n            \"twitter_handle\": \"Vamsi_Rayudu\",\n            \"twitter_name\": \"Vamsi_Rayudu1\",\n            \"geolocation\": \"\",\n            \"timezone\": \"\",\n            \"twitterid\": \"755652926081761280\",\n            \"createdOn\": \"2016-07-11 17:02:51\",\n            \"updatedOn\": \"2016-07-11 17:17:06\"\n        }\n    }]\n}",
        "language": "json",
        "name": "Twitter"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"9876\",\n        \"Attributes\": {\n            \"verified\": \"1\",\n            \"status\": \"1\",\n            \"channel\": \"wechat\",\n            \"nick\": \"vamsi punnam1\",\n            \"language\": \"en\",\n            \"wechat_user_id\": \"o8E7mwaZqY3Q9eaxeftj7TyD5EiE\",\n            \"createdOn\": \"2016-07-11 17:02:51\",\n            \"updatedOn\": \"2016-07-11 17:17:06\"\n        }\n    }]\n}",
        "language": "json",
        "name": "WeChat"
      },
      {
        "code": "    {\n        \"Records\": [{\n            \"customerId\": \"9876\",\n            \"Attributes\": {\n                \"verified\": \"0\",\n                \"status\": \"1\",\n                \"connectStatus\": \"1\",\n                \"userId\": \"9876\",\n                \"channel\": \"rt\",\n                \"deviceId\": \"355004057394235\",\n                \"rtmId\": \"9876_355004057394235\",\n                \"make\": \"Apple\",\n                \"model\": \"iPad 3(GSM)\",\n                \"os\": \"ios\",\n                \"osversion\": \"9.3.1\",\n                \"pushId\": \"37bc5867465cb95124e5e03aad905100f8154cb4f1f5cb8c4a01eae8ee758316\",\n                \"createdOn\": \"2016-07-11 17:02:51\",\n                \"last_opened\": \"2016-07-25T16:39:54+0530\",\n                \"last_upgraded\": \"2016-07-25T16:39:54+0530\"\n            }\n        }]\n    }",
        "language": "json",
        "name": "In-app"
      }
    ]
  },
  "method": "put",
  "params": [
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The ID of the app asset that you can obtain from imiconnect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6df593fa51ca0016b017f8",
      "id": "5f6df593fa51ca0016b017f8"
    },
    {
      "name": "Content-Type",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Application/JSON",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "5f6df593fa51ca0016b017f7",
      "id": "5f6df593fa51ca0016b017f7"
    },
    {
      "name": "secretKey",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Client key that can be accessed from your app asset configuration page on imiconnect platform",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "5f6df593fa51ca0016b017f6",
      "id": "5f6df593fa51ca0016b017f6"
    },
    {
      "name": "attributes",
      "type": "array_string",
      "enumValues": "",
      "default": "",
      "desc": "String of key/value pairs to update",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "5f6df62459c8f10052483030",
      "id": "5f6df62459c8f10052483030"
    }
  ],
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"TotalCount\": 1,\n    \"FailureCount\": 0,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"code\": \"1000\",\n            \"customerId\": \"777777\",\n            \"description\": \"SUCCESS\"\n        }\n    ],\n    \"transid\": \"b9d2aeea-6f08-4b81-bc01-68b042481e47\",\n    \"description\": \"SUCCESS\",\n    \"SuccessCount\": 1\n}\n",
        "status": 200
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67b8"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Profile API v2",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://api.imiconnect.io/resources/v2"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/customerappprofile/<app ID>",
  "method": "put",
  "path_parameters": [],
  "operation": {
    "summary": "Update App Profile",
    "description": "This API is used to update application profile of a customer.",
    "operationId": "updateappprofile",
    "parameters": [
      {
        "name": "appid",
        "in": "path",
        "description": "The ID of the app asset that you can obtain from imiconnect platform",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "Content-Type",
        "in": "header",
        "description": "Application/JSON",
        "schema": {
          "type": "string"
        }
      },
      {
        "name": "secretKey",
        "in": "header",
        "description": "Client key that can be accessed from your app asset configuration page on imiconnect platform",
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
              "attributes"
            ],
            "properties": {
              "attributes": {
                "type": "array",
                "description": "String of key/value pairs to update",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "examples": {
            "Facebook": {
              "value": {
                "Records": [
                  {
                    "customerId": "9876",
                    "Attributes": {
                      "verified": "1",
                      "status": "1",
                      "createdOn": "2016-07-11 17:02:51",
                      "channel": "fb",
                      "name": "Joe James1",
                      "profile_pic": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfa1/v/t1.0-1/s200x200/10354686_10150004552801856_220367501106153455_n.jpg?oh=246adb8e3d7dc948f4d8025495fbf8dd&oe=57FD4150&__gda__=1476209436_66628acd9a55e42920bb3f0a823e1eac",
                      "psid": "1223275837725015",
                      "updatedOn": "2016-07-11 17:17:06"
                    }
                  }
                ]
              }
            },
            "Twitter": {
              "value": {
                "Records": [
                  {
                    "customerId": "9876",
                    "Attributes": {
                      "verified": "1",
                      "status": "1",
                      "channel": "twitter",
                      "twitter_handle": "Vamsi_Rayudu",
                      "twitter_name": "Vamsi_Rayudu1",
                      "geolocation": "",
                      "timezone": "",
                      "twitterid": "755652926081761280",
                      "createdOn": "2016-07-11 17:02:51",
                      "updatedOn": "2016-07-11 17:17:06"
                    }
                  }
                ]
              }
            },
            "WeChat": {
              "value": {
                "Records": [
                  {
                    "customerId": "9876",
                    "Attributes": {
                      "verified": "1",
                      "status": "1",
                      "channel": "wechat",
                      "nick": "vamsi punnam1",
                      "language": "en",
                      "wechat_user_id": "o8E7mwaZqY3Q9eaxeftj7TyD5EiE",
                      "createdOn": "2016-07-11 17:02:51",
                      "updatedOn": "2016-07-11 17:17:06"
                    }
                  }
                ]
              }
            },
            "In-app": {
              "value": {
                "Records": [
                  {
                    "customerId": "9876",
                    "Attributes": {
                      "verified": "0",
                      "status": "1",
                      "connectStatus": "1",
                      "userId": "9876",
                      "channel": "rt",
                      "deviceId": "355004057394235",
                      "rtmId": "9876_355004057394235",
                      "make": "Apple",
                      "model": "iPad 3(GSM)",
                      "os": "ios",
                      "osversion": "9.3.1",
                      "pushId": "37bc5867465cb95124e5e03aad905100f8154cb4f1f5cb8c4a01eae8ee758316",
                      "createdOn": "2016-07-11 17:02:51",
                      "last_opened": "2016-07-25T16:39:54+0530",
                      "last_upgraded": "2016-07-25T16:39:54+0530"
                    }
                  }
                ]
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
                "value": "{\n    \"TotalCount\": 1,\n    \"FailureCount\": 0,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"code\": \"1000\",\n            \"customerId\": \"777777\",\n            \"description\": \"SUCCESS\"\n        }\n    ],\n    \"transid\": \"b9d2aeea-6f08-4b81-bc01-68b042481e47\",\n    \"description\": \"SUCCESS\",\n    \"SuccessCount\": 1\n}\n"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "TotalCount": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                },
                "FailureCount": {
                  "type": "integer",
                  "example": 0,
                  "default": 0
                },
                "code": {
                  "type": "string",
                  "example": "1000"
                },
                "Results": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "code": {
                        "type": "string",
                        "example": "1000"
                      },
                      "customerId": {
                        "type": "string",
                        "example": "777777"
                      },
                      "description": {
                        "type": "string",
                        "example": "SUCCESS"
                      }
                    }
                  }
                },
                "transid": {
                  "type": "string",
                  "example": "b9d2aeea-6f08-4b81-bc01-68b042481e47"
                },
                "description": {
                  "type": "string",
                  "example": "SUCCESS"
                },
                "SuccessCount": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                }
              }
            }
          }
        }
      }
    },
    "deprecated": false,
    "x-readme": {
      "code-samples": [
        {
          "language": "curl",
          "code": "-X PUT https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\n-H \"Content-Type : application/json\"\n-H \"key : {profilekey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.put(\"https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\",\n    :headers => {'Content-Type' => 'application/json',\n\t'key' => ' Profile key present in tenant setting’})\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"PUT\", \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"key\", \"Profile key present in tenant setting\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\"\n\nheaders = {'Content-Type': 'application/json', 'key': ' Profile key present in tenant setting '}\n\nresponse = requests.request(\"PUT\", url, headers=headers)\n\nprint(response.text)\n"
        }
      ],
      "samples-languages": [
        "curl",
        "ruby",
        "javascript",
        "python"
      ]
    }
  },
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "key"
      }
    }
  }
}
```
