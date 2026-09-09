# Create a Topic

Source: https://developers.webexconnect.io/reference/createtopic
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
      "_id": "5f521648f1623d0029a7a5cc",
      "id": "5f521648f1623d0029a7a5cc"
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
      "_id": "5f521648f1623d0029a7a5cb",
      "id": "5f521648f1623d0029a7a5cb"
    },
    {
      "name": "name",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Specifies the name of the topic",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "5f521648f1623d0029a7a5ca",
      "id": "5f521648f1623d0029a7a5ca"
    },
    {
      "name": "ref",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Used to store input data",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "5f521648f1623d0029a7a5c9",
      "id": "5f521648f1623d0029a7a5c9"
    },
    {
      "name": "topic_group",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Used to define the group of the topic",
      "required": false,
      "in": "body",
      "ref": "",
      "_id": "5f521648f1623d0029a7a5c8",
      "id": "5f521648f1623d0029a7a5c8"
    },
    {
      "name": "description",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Used to add a comprehensive description",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "5f521648f1623d0029a7a5c7",
      "id": "5f521648f1623d0029a7a5c7"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The ID of the app asset that you can obtain from IMIconnect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d861f4d72eb006fb47997",
      "id": "5f6d861f4d72eb006fb47997"
    }
  ],
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n\t\"id\" : \"591d7f04e4b09e0d95d4f73f\",\n\t\"trans_id\" : \"22a23dbc-af31-4c65-925e-8e74e115ef27\",\n\t\"description\" : \"success\",\n\t\"code\" : 0\n}",
        "status": 200
      }
    ]
  },
  "settings": "",
  "url": "/apps/$(appid)/topics",
  "auth": "never",
  "examples": {
    "codes": [
      {
        "code": "{\n\t\"name\" : \"offers\",\n\t\"ref\" : \"offer ref\",\n\t\"topic_group\" : \"Extra Benefits\",\n\t\"description\" : \"Get Benefits from this topic\"\n}",
        "language": "json"
      },
      {
        "code": "-X POST https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n",
        "language": "curl",
        "name": ""
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'POST',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{inappid}}/topics',\n          headers: {\n            'Content-Type': 'application/json',\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.post(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\",\n    :headers => {'Content-Type' => 'application/json',\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\"\n\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"POST\", url, headers=headers)\n\nprint(response.text)\n\n",
        "language": "python"
      }
    ]
  },
  "method": "post",
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
  "path": "/apps/$(appid)/topics",
  "method": "post",
  "path_parameters": [],
  "operation": {
    "summary": "Create a Topic",
    "description": "This API is used to create topics for a specific appId.",
    "operationId": "createtopic",
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
        "description": "The ID of the app asset that you can obtain from IMIconnect platform",
        "schema": {
          "type": "string"
        },
        "required": true
      }
    ],
    "requestBody": {
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "required": [
              "name",
              "description"
            ],
            "properties": {
              "name": {
                "type": "string",
                "description": "Specifies the name of the topic"
              },
              "ref": {
                "type": "string",
                "description": "Used to store input data"
              },
              "topic_group": {
                "type": "string",
                "description": "Used to define the group of the topic"
              },
              "description": {
                "type": "string",
                "description": "Used to add a comprehensive description"
              }
            }
          },
          "examples": {
            "Request Example": {
              "value": {
                "name": "offers",
                "ref": "offer ref",
                "topic_group": "Extra Benefits",
                "description": "Get Benefits from this topic"
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
                "value": "{\n\t\"id\" : \"591d7f04e4b09e0d95d4f73f\",\n\t\"trans_id\" : \"22a23dbc-af31-4c65-925e-8e74e115ef27\",\n\t\"description\" : \"success\",\n\t\"code\" : 0\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string",
                  "example": "591d7f04e4b09e0d95d4f73f"
                },
                "trans_id": {
                  "type": "string",
                  "example": "22a23dbc-af31-4c65-925e-8e74e115ef27"
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
      }
    },
    "deprecated": false,
    "security": [],
    "x-readme": {
      "code-samples": [
        {
          "language": "curl",
          "code": "-X POST https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.post(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\",\n    :headers => {'Content-Type' => 'application/json',\n                          'secretKey ' => '{secretKey}’\n            }\n)\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{inappid}/topics\"\n\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}’}\n\nresponse = requests.request(\"POST\", url, headers=headers)\n\nprint(response.text)\n\n"
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
