# Get All Subscribers of a Topic

Source: https://developers.webexconnect.io/reference/get-all-subscribers
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
  "examples": {
    "codes": [
      {
        "code": "-X GET \nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{inappid}}/topics/{{topicid}}/users\n-H \"secretKey: {secretKey}\"",
        "language": "curl"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' \nhttps://rtm.imiconnect.io/rtmsAPI/api/v11/apps/{inappid}/topics/{topicid}/users',\n          headers: {\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"\nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/{topicid}/users\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" \nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/{topicid}/users\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" \nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/{topicid}/users\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      }
    ]
  },
  "settings": "",
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"total\": \"1\",\n    \"code\": 0,\n    \"count\": \"50\",\n    \"description\": \"success\",\n    \"trans_id\": \"a1c40090-8fc0-45f9-bb4b-dbf3d5413d63\",\n    \"users\": [\n        \"1420966801\"\n    ]\n}\n",
        "status": 200
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
      "_id": "5f521eb90e8470001152131b",
      "id": "5f521eb90e8470001152131b"
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
      "_id": "5f521eb90e8470001152131a",
      "id": "5f521eb90e8470001152131a"
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
      "_id": "5f6d88f1eaed2d001f78aec3",
      "id": "5f6d88f1eaed2d001f78aec3"
    },
    {
      "name": "topicid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Specifies the ID of the topic",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d88f1eaed2d001f78aec2",
      "id": "5f6d88f1eaed2d001f78aec2"
    },
    {
      "name": "start",
      "type": "int",
      "enumValues": "",
      "default": "",
      "desc": "The record pointer that defines where to start in the subscriber list. A maximum of 50 subscribers can be returned (if available).",
      "required": false,
      "in": "query",
      "ref": "",
      "_id": "601973724243d400188ee59f",
      "id": "601973724243d400188ee59f"
    }
  ],
  "url": "/apps/$(appid)/topics/$(topicid)/users?start=0",
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
  "path": "/apps/$(appid)/topics/$(topicid)/users?start=0",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get All Subscribers of a Topic",
    "description": "This API will get all the subscribers of a topic.",
    "operationId": "get-all-subscribers",
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
        "name": "topicid",
        "in": "path",
        "description": "Specifies the ID of the topic",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "start",
        "in": "query",
        "description": "The record pointer that defines where to start in the subscriber list. A maximum of 50 subscribers can be returned (if available).",
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
                "value": "{\n    \"total\": \"1\",\n    \"code\": 0,\n    \"count\": \"50\",\n    \"description\": \"success\",\n    \"trans_id\": \"a1c40090-8fc0-45f9-bb4b-dbf3d5413d63\",\n    \"users\": [\n        \"1420966801\"\n    ]\n}\n"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "total": {
                  "type": "string",
                  "example": "1"
                },
                "code": {
                  "type": "integer",
                  "example": 0,
                  "default": 0
                },
                "count": {
                  "type": "string",
                  "example": "50"
                },
                "description": {
                  "type": "string",
                  "example": "success"
                },
                "trans_id": {
                  "type": "string",
                  "example": "a1c40090-8fc0-45f9-bb4b-dbf3d5413d63"
                },
                "users": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "example": "1420966801"
                  }
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
          "code": "-X GET \nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{inappid}}/topics/{{topicid}}/users\n-H \"secretKey: {secretKey}\""
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"\nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/{topicid}/users\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" \nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/{topicid}/users\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" \nhttps://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/{topicid}/users\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n"
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
