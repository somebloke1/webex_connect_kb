# Get Streams - Legacy

Source: https://developers.webexconnect.io/reference/list-streams
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:50+00:00



> **Know Your Endpoint**
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.webexconnect.io/reference/know-your-api-endpoints) section to understand which endpoint to use for your domain.



## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "url": "/{rtmsdomain}/api/v1/apps/{appid}/streams",
  "method": "get",
  "examples": {
    "codes": [
      {
        "code": "{\n//This API does not require any params in the request body\n}",
        "language": "json"
      }
    ]
  },
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n  \"status\": \"success\",\n  \"streams\": [\n    {\n      \"id\": \"59197d9ee4b04a5c464d71f6\",\n      \"created_on\": \"2017-05-15T10:06:22.848Z\",\n      \"name\": \"APPUSERSTREAM\"\n    },\n    {\n      \"id\": \"59267828e4b0479ee69708bb\",\n      \"created_on\": \"2017-05-25T06:22:32.167Z\",\n      \"name\": \"BOT\"\n    },\n    ],\n  \"code\": 0\n}",
        "status": 200
      }
    ]
  },
  "settings": "",
  "auth": "required",
  "params": [
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Specifies the ID of app asset on IMIconnect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d679ba4febd003482113b",
      "id": "5f6d679ba4febd003482113b"
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
      "_id": "5f6d679ba4febd003482113a",
      "id": "5f6d679ba4febd003482113a"
    },
    {
      "name": "secretKey",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Client key that can be accessed from your app asset configuration page on IMIconnect platform",
      "required": false,
      "in": "header",
      "ref": "",
      "_id": "5f6d679ba4febd0034821139",
      "id": "5f6d679ba4febd0034821139"
    }
  ],
  "apiSetting": "6a675233ec1c893d8a7f67ba"
}
```

## OpenAPI operation and component schemas

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
  "path": "/{rtmsdomain}/api/v1/apps/{appid}/streams",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get Streams - Legacy",
    "description": "Streams are used to route the messages from customers to one service. One stream per service limits users to hold conversations on multiple threads from the same service. So, a thread ID should be generated first, for every new thread title with a combination of message type, stream ID and thread title as shown in the below combination:\n**<stream_id>_<message_type>_<thread_title>*.",
    "operationId": "list-streams",
    "parameters": [
      {
        "name": "appid",
        "in": "path",
        "description": "Specifies the ID of app asset on IMIconnect platform",
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
        "description": "Client key that can be accessed from your app asset configuration page on IMIconnect platform",
        "schema": {
          "type": "string"
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
                "value": "{\n  \"status\": \"success\",\n  \"streams\": [\n    {\n      \"id\": \"59197d9ee4b04a5c464d71f6\",\n      \"created_on\": \"2017-05-15T10:06:22.848Z\",\n      \"name\": \"APPUSERSTREAM\"\n    },\n    {\n      \"id\": \"59267828e4b0479ee69708bb\",\n      \"created_on\": \"2017-05-25T06:22:32.167Z\",\n      \"name\": \"BOT\"\n    },\n    ],\n  \"code\": 0\n}"
              }
            }
          }
        }
      }
    },
    "deprecated": false,
    "requestBody": {
      "content": {
        "application/json": {
          "schema": {},
          "examples": {
            "Request Example": {
              "value": {}
            }
          }
        }
      }
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
