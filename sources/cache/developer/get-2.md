# Get a Topic

Source: https://developers.webexconnect.io/reference/get-2
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
        "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{inappid}}/topics/\n-H \"secretKey: {secretKey}\"\n",
        "language": "curl"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/',\n          headers: {\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      }
    ]
  },
  "settings": "",
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"code\": \"0\",\n    \"topics\": [\n        {\n            \"ref\": \"yes\",\n            \"topic_group\": \"Testing\",\n            \"created_on\": \"2020-08-24T05:00:47.264Z\",\n            \"name\": \"JWTSanityUK1\",\n            \"description\": \"Cordova\",\n            \"id\": \"5f43497fe4b0eae4f99c0f6e\"\n        }\n    ],\n    \"description\": \"success\",\n    \"trans_id\": \"d13b5c1c-96ba-478a-84e5-25b86f2de5b7\"\n}\n",
        "status": 200
      }
    ]
  },
  "auth": "required",
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
      "_id": "5f6d87a7c839e5005f194f1e",
      "id": "5f6d87a7c839e5005f194f1e"
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
      "_id": "5f6d87a7c839e5005f194f1d",
      "id": "5f6d87a7c839e5005f194f1d"
    }
  ],
  "url": "/apps/$(appid)/topics/$(topicid)",
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
  "path": "/apps/$(appid)/topics/$(topicid)",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get a Topic",
    "description": "This API should return the topic information for a specific topicId.",
    "operationId": "get-2",
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
        "name": "topicid",
        "in": "path",
        "description": "Specifies the ID of the topic",
        "schema": {
          "type": "string"
        },
        "required": true
      }
    ],
    "responses": {
      "200": {
        "description": "200",
        "content": {
          "application/json": {
            "examples": {
              "Result": {
                "value": "{\n    \"code\": \"0\",\n    \"topics\": [\n        {\n            \"ref\": \"yes\",\n            \"topic_group\": \"Testing\",\n            \"created_on\": \"2020-08-24T05:00:47.264Z\",\n            \"name\": \"JWTSanityUK1\",\n            \"description\": \"Cordova\",\n            \"id\": \"5f43497fe4b0eae4f99c0f6e\"\n        }\n    ],\n    \"description\": \"success\",\n    \"trans_id\": \"d13b5c1c-96ba-478a-84e5-25b86f2de5b7\"\n}\n"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "string",
                  "example": "0"
                },
                "topics": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "ref": {
                        "type": "string",
                        "example": "yes"
                      },
                      "topic_group": {
                        "type": "string",
                        "example": "Testing"
                      },
                      "created_on": {
                        "type": "string",
                        "example": "2020-08-24T05:00:47.264Z"
                      },
                      "name": {
                        "type": "string",
                        "example": "JWTSanityUK1"
                      },
                      "description": {
                        "type": "string",
                        "example": "Cordova"
                      },
                      "id": {
                        "type": "string",
                        "example": "5f43497fe4b0eae4f99c0f6e"
                      }
                    }
                  }
                },
                "description": {
                  "type": "string",
                  "example": "success"
                },
                "trans_id": {
                  "type": "string",
                  "example": "d13b5c1c-96ba-478a-84e5-25b86f2de5b7"
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
          "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{inappid}}/topics/\n-H \"secretKey: {secretKey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\",\n    :headers => {\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics/\"\n\nheaders = {'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n"
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
