# Get User Messages

Source: https://developers.webexconnect.io/reference/user-messages-1
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:35:07+00:00

The following error code is displayed when the Server Side Inbox is disabled for your tenant.

```json
{
    "code": 67,
    "description": "This functionality is not available as Server Side Inbox is disabled for your app asset."
}
```

> 📘 Note
> 
> Only a tenant owner, full access user, or limited access user can enable or disable the Server Side Inbox for your tenant. To learn more, refer to [Server Side Inbox](https://help.webexconnect.io/docs/mobile-web#add-a-mobile-application) feature.

> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to Webex Connect , the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "apiSetting": "6a675233ec1c893d8a7f67ba",
  "examples": {
    "codes": [
      {
        "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads/{{threadid}}/messages\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n",
        "language": "curl",
        "name": ""
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages',\n          headers: {\n            'Content-Type': 'application/json',\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\",\n    :headers => {'Content-Type' => 'application/json',\n\t'secretKey ' => '{secretKey}’})\n# Print on console\nputs http\n\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);",
        "language": "javascript",
        "name": null
      },
      {
        "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\"\n\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}'}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      }
    ]
  },
  "results": {
    "codes": [
      {
        "code": "",
        "language": "text"
      },
      {
        "code": "{\n    \"total\": 1,\n    \"code\": \"0\",\n    \"count\": 1,\n    \"messages\": [\n        {\n            \"payload_type\": \"sentByUser\",\n            \"created_on\": \"2020-08-13T11:47:31.688Z\",\n            \"appid\": \"BA22091950\",\n            \"extras\": {},\n            \"read_at\": \"\",\n            \"media\": [],\n            \"thread\": {\n                \"id\": \"22110118-6352-4bbc-a53a-43b761ae18db\"\n            },\n            \"message\": \"hello\",\n            \"userId\": \"1420966801\",\n            \"delivered_at\": \"\",\n            \"tid\": \"Rbca18c81-ac37-4e0a-98ce-345b1c38fd11\",\n            \"status\": \"submited\"\n        }\n    ],\n    \"description\": \"success\"\n}",
        "language": "json",
        "status": 200
      }
    ]
  },
  "settings": "",
  "auth": "required",
  "params": [
    {
      "name": "Content-Type",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "application/json",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "5f51e7420f2307006f353a21",
      "id": "5f51e7420f2307006f353a21"
    },
    {
      "name": "secretKey",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Client key that can be accessed from your app asset configuration page on Webex Connect platform",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "5f51e7420f2307006f353a20",
      "id": "5f51e7420f2307006f353a20"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Specifies the ID of the app asset on Webex Connect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d6e33b34d8100600c068a",
      "id": "5f6d6e33b34d8100600c068a"
    },
    {
      "name": "userid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Unique ID for a mobile/web app user.",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d6e33b34d8100600c0689",
      "id": "5f6d6e33b34d8100600c0689"
    },
    {
      "name": "threadid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "The ID of the thread",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6dce2ac5a53700125195da",
      "id": "5f6dce2ac5a53700125195da"
    }
  ],
  "url": "/apps/{appid}/user/{userid}/threads/{threadid}/messages",
  "method": "get"
}
```

## OpenAPI operation and component schemas

Operation extraction: selected. Missing operation definitions must not be inferred from this cache.

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Thread API",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://rtm.imiconnect.io/rtmsAPI/api/v1/"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/apps/{appid}/user/{userid}/threads/{threadid}/messages",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get User Messages",
    "description": "This API retrieves a list of messages for a specified thread within a given app ID and user ID.",
    "operationId": "user-messages-1",
    "parameters": [
      {
        "name": "Content-Type",
        "in": "header",
        "description": "application/json",
        "schema": {
          "type": "string"
        }
      },
      {
        "name": "secretKey",
        "in": "header",
        "description": "Client key that can be accessed from your app asset configuration page on Webex Connect platform",
        "schema": {
          "type": "string"
        }
      },
      {
        "name": "appid",
        "in": "path",
        "description": "Specifies the ID of the app asset on Webex Connect platform",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "userid",
        "in": "path",
        "description": "Unique ID for a mobile/web app user.",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "threadid",
        "in": "path",
        "description": "The ID of the thread",
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
                "value": "{\n    \"total\": 1,\n    \"code\": \"0\",\n    \"count\": 1,\n    \"messages\": [\n        {\n            \"payload_type\": \"sentByUser\",\n            \"created_on\": \"2020-08-13T11:47:31.688Z\",\n            \"appid\": \"BA22091950\",\n            \"extras\": {},\n            \"read_at\": \"\",\n            \"media\": [],\n            \"thread\": {\n                \"id\": \"22110118-6352-4bbc-a53a-43b761ae18db\"\n            },\n            \"message\": \"hello\",\n            \"userId\": \"1420966801\",\n            \"delivered_at\": \"\",\n            \"tid\": \"Rbca18c81-ac37-4e0a-98ce-345b1c38fd11\",\n            \"status\": \"submited\"\n        }\n    ],\n    \"description\": \"success\"\n}"
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
                "code": {
                  "type": "string",
                  "example": "0"
                },
                "count": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                },
                "messages": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "payload_type": {
                        "type": "string",
                        "example": "sentByUser"
                      },
                      "created_on": {
                        "type": "string",
                        "example": "2020-08-13T11:47:31.688Z"
                      },
                      "appid": {
                        "type": "string",
                        "example": "BA22091950"
                      },
                      "extras": {
                        "type": "object",
                        "properties": {}
                      },
                      "read_at": {
                        "type": "string",
                        "example": ""
                      },
                      "media": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {}
                        }
                      },
                      "thread": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "example": "22110118-6352-4bbc-a53a-43b761ae18db"
                          }
                        }
                      },
                      "message": {
                        "type": "string",
                        "example": "hello"
                      },
                      "userId": {
                        "type": "string",
                        "example": "1420966801"
                      },
                      "delivered_at": {
                        "type": "string",
                        "example": ""
                      },
                      "tid": {
                        "type": "string",
                        "example": "Rbca18c81-ac37-4e0a-98ce-345b1c38fd11"
                      },
                      "status": {
                        "type": "string",
                        "example": "submited"
                      }
                    }
                  }
                },
                "description": {
                  "type": "string",
                  "example": "success"
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
          "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads/{{threadid}}/messages\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\",\n    :headers => {'Content-Type' => 'application/json',\n\t'secretKey ' => '{secretKey}’})\n# Print on console\nputs http\n\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\"\n\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}'}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n"
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
  },
  "operation_status": "selected"
}
```
