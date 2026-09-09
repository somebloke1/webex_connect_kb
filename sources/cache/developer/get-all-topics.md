# Get All Topics of a Subscriber

Source: https://developers.webexconnect.io/reference/get-all-topics
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:51+00:00



> **Know Your Endpoint**
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.


**For Topic**: 

The following is the error code displayed when the Topic messaging is disabled for your tenant.


```json
{

"code": 69,

"description": "Topics based messaging feature is not available for your tenant"

}
```





> **Note**
> 
> To enable the Topic messaging for your tenant, contact your account manager.



## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "results": {
    "codes": [
      {
        "status": 200,
        "language": "json",
        "code": "{\n\t\"total\" : 1,\n\t\"count\" : 1,\n\t\"topics\" : [{\n\t\t\t\"id\" : \"591d7b7de4b09e0d95d4f73d\",\n\t\t\t\"ref\" : \"offer ref\",\n\t\t\t\"created_on\" : \"2017-05-26T18 12:22:51.001Z\",\n\t\t\t\"description\" : \"Get Lot of Benifits from this topic\",\n\t\t\t\"name\" : \"offers\",\n\t\t\t\"topic_group\" : \"Extra Benifits\",\n                                           \"subscribed\" : true\n\n\t\t}\n\t],\n\t\"trans_id\" : \"2b1142c3-b99e-4af4-befa-77b5451ad2af\",\n\t\"description\" : \"success\",\n\t\"code\" : 0\n}",
        "name": ""
      },
      {
        "name": "",
        "status": 400,
        "language": "json",
        "code": "{}"
      }
    ]
  },
  "settings": "",
  "examples": {
    "codes": [
      {
        "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\n-H \"secretKey: {secretKey}\"\n",
        "language": "curl"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0',\n          headers: {\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      }
    ]
  },
  "auth": "required",
  "params": [
    {
      "name": "Content-Type",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Application/JSON",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "5f521f59bf0a38006a06ad13",
      "id": "5f521f59bf0a38006a06ad13"
    },
    {
      "name": "secretKey",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Client key that can be accessed from your app asset configuration page on imiconnect platform",
      "required": true,
      "in": "header",
      "ref": "",
      "_id": "5a0eea7ec57106001c099547",
      "id": "5a0eea7ec57106001c099547"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The ID of the app asset that you can obtain from imiconnect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d8b84267dcc006b19e245",
      "id": "5f6d8b84267dcc006b19e245"
    },
    {
      "name": "userid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Unique ID for a mobile/web app user",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d8b84267dcc006b19e244",
      "id": "5f6d8b84267dcc006b19e244"
    },
    {
      "name": "start",
      "type": "int",
      "enumValues": "",
      "default": "",
      "desc": "The record pointer which defines where to start in the list. A maximum of 50 records can be returned (if available).",
      "required": false,
      "in": "query",
      "ref": "",
      "_id": "601973c4ec9d15005dc41b02",
      "id": "601973c4ec9d15005dc41b02"
    }
  ],
  "url": "/apps/$(appid)/users/$(userid)/topics?start=0&subscribed=true/false/both",
  "method": "get",
  "apiSetting": "6a675233ec1c893d8a7f67bc"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Topic APIs",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://rtm.imiconnect.io/"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/apps/$(appid)/users/$(userid)/topics?start=0&subscribed=true/false/both",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get All Topics of a Subscriber",
    "description": "This API is used to get all the topics of a subscriber.",
    "operationId": "get-all-topics",
    "parameters": [
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
        "required": true,
        "schema": {
          "type": "string"
        }
      },
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
        "name": "userid",
        "in": "path",
        "description": "Unique ID for a mobile/web app user",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "start",
        "in": "query",
        "description": "The record pointer which defines where to start in the list. A maximum of 50 records can be returned (if available).",
        "schema": {
          "type": "integer",
          "format": "int32"
        }
      }
    ],
    "responses": {
      "200": {
        "description": "200",
        "content": {
          "application/json": {
            "examples": {
              "Result": {
                "value": "{\n\t\"total\" : 1,\n\t\"count\" : 1,\n\t\"topics\" : [{\n\t\t\t\"id\" : \"591d7b7de4b09e0d95d4f73d\",\n\t\t\t\"ref\" : \"offer ref\",\n\t\t\t\"created_on\" : \"2017-05-26T18 12:22:51.001Z\",\n\t\t\t\"description\" : \"Get Lot of Benifits from this topic\",\n\t\t\t\"name\" : \"offers\",\n\t\t\t\"topic_group\" : \"Extra Benifits\",\n                                           \"subscribed\" : true\n\n\t\t}\n\t],\n\t\"trans_id\" : \"2b1142c3-b99e-4af4-befa-77b5451ad2af\",\n\t\"description\" : \"success\",\n\t\"code\" : 0\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "total": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                },
                "count": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                },
                "topics": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "example": "591d7b7de4b09e0d95d4f73d"
                      },
                      "ref": {
                        "type": "string",
                        "example": "offer ref"
                      },
                      "created_on": {
                        "type": "string",
                        "example": "2017-05-26T18 12:22:51.001Z"
                      },
                      "description": {
                        "type": "string",
                        "example": "Get Lot of Benifits from this topic"
                      },
                      "name": {
                        "type": "string",
                        "example": "offers"
                      },
                      "topic_group": {
                        "type": "string",
                        "example": "Extra Benifits"
                      },
                      "subscribed": {
                        "type": "boolean",
                        "example": true,
                        "default": true
                      }
                    }
                  }
                },
                "trans_id": {
                  "type": "string",
                  "example": "2b1142c3-b99e-4af4-befa-77b5451ad2af"
                },
                "description": {
                  "type": "string",
                  "example": "success"
                },
                "code": {
                  "type": "integer",
                  "example": 0,
                  "default": 0
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
                "value": "{}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {}
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
          "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\n-H \"secretKey: {secretKey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/user/{userid}/topics?start=0\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n"
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
