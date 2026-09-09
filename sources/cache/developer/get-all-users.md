# Get All Users of  a Segment

Source: https://developers.webexconnect.io/reference/get-all-users
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:51+00:00

**For Segment**: 

The following is the error code displayed when the Segment messaging is disabled for your tenant.


```json
{

  "code": 70,

  "description": "Segment based messaging feature is not available for your tenant"

}
```





> **Note**
> 
> To enable the Segment messaging for your tenant, contact your account manager.




> **Know Your Endpoint**
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.



## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"code\": 0,\n    \"description\": \"Success\",\n    \"trans_id\": \"295e1d2e-b5a9-4d7d-8358-d1e0da803f94\",\n    \"users\": [\n        \"1420966801\",\n        \"1420966802\"\n    ]\n}",
        "status": 200
      }
    ]
  },
  "settings": "",
  "examples": {
    "codes": [
      {
        "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\n-H \"secretKey: {secretKey}\"",
        "language": "curl",
        "name": ""
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0',\n          headers: {\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)",
        "language": "python"
      }
    ]
  },
  "auth": "required",
  "params": [
    {
      "name": "inappid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The ID of the app asset that you can obtain from the imiconnect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d834d755de300133785ad",
      "id": "5f6d834d755de300133785ad"
    },
    {
      "name": "segmentid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Unique ID of the segment",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d834d755de300133785ac",
      "id": "5f6d834d755de300133785ac"
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
      "_id": "5f4139808ea31002da2fb269",
      "id": "5f4139808ea31002da2fb269"
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
      "_id": "5f4139808ea31002da2fb268",
      "id": "5f4139808ea31002da2fb268"
    },
    {
      "name": "start",
      "type": "int",
      "enumValues": "",
      "default": "",
      "desc": "The record pointer that defines where to start in the list. A maximum of 50 records can be returned (if available).",
      "required": false,
      "in": "query",
      "ref": "",
      "_id": "60194cb30d555b001da6bd0b",
      "id": "60194cb30d555b001da6bd0b"
    }
  ],
  "url": "/apps/{inappid}/segments/{segmentid}/users?start=0",
  "method": "get",
  "apiSetting": "6a675233ec1c893d8a7f67bb"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Segment APIs",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://rtm.imiconnect.io/rtmsAPI/api/v1"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/apps/{inappid}/segments/{segmentid}/users?start=0",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get All Users of  a Segment",
    "description": "This API is used to get all users of a segment",
    "operationId": "get-all-users",
    "parameters": [
      {
        "name": "inappid",
        "in": "path",
        "description": "The ID of the app asset that you can obtain from the imiconnect platform",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "segmentid",
        "in": "path",
        "description": "Unique ID of the segment",
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
      },
      {
        "name": "start",
        "in": "query",
        "description": "The record pointer that defines where to start in the list. A maximum of 50 records can be returned (if available).",
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
                "value": "{\n    \"code\": 0,\n    \"description\": \"Success\",\n    \"trans_id\": \"295e1d2e-b5a9-4d7d-8358-d1e0da803f94\",\n    \"users\": [\n        \"1420966801\",\n        \"1420966802\"\n    ]\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer",
                  "example": 0,
                  "default": 0
                },
                "description": {
                  "type": "string",
                  "example": "Success"
                },
                "trans_id": {
                  "type": "string",
                  "example": "295e1d2e-b5a9-4d7d-8358-d1e0da803f94"
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
          "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\n-H \"secretKey: {secretKey}\""
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/segments/{segmentid}/users?start=0\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)"
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
