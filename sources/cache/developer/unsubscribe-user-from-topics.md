# Unsubscribe a User from Topics

Source: https://developers.webexconnect.io/reference/unsubscribe-user-from-topics
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:52+00:00



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
        "code": "{\n//This API does not require any params in the request body\n}",
        "language": "json"
      }
    ]
  },
  "settings": "",
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n\t\"trans_id\" : \"f2cc5fca-715e-4a86-b457-574bb7ba48d4\",\n\t\"description\" : \"Failed\",\n\t\"code\" : 1,\n\t\"success_topics\" : [\"591d3af1e4b0be20f3fc3eb9\"],\n\t\"fail_topics\" : [\"591d44c3e4b09eee109c1541\"]\n}",
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
      "_id": "5f571387650fba006c1f7919",
      "id": "5f571387650fba006c1f7919"
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
      "_id": "5f571387650fba006c1f7918",
      "id": "5f571387650fba006c1f7918"
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
      "_id": "601975b14d35fb0050397369",
      "id": "601975b14d35fb0050397369"
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
      "_id": "601975b14d35fb0050397368",
      "id": "601975b14d35fb0050397368"
    },
    {
      "name": "topicid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Specifies the ID of the topic",
      "required": false,
      "in": "query",
      "ref": "",
      "_id": "601976083625f4007a0c1988",
      "id": "601976083625f4007a0c1988"
    }
  ],
  "url": "/apps/$(appid)/user/$(userid)/topics?topics=$(topicid)",
  "method": "delete",
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
  "path": "/apps/$(appid)/user/$(userid)/topics?topics=$(topicid)",
  "method": "delete",
  "path_parameters": [],
  "operation": {
    "summary": "Unsubscribe a User from Topics",
    "description": "",
    "operationId": "unsubscribe-user-from-topics",
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
        "name": "userid",
        "in": "path",
        "description": "Unique ID for a mobile/web app user",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "topicid",
        "in": "query",
        "description": "Specifies the ID of the topic",
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
                "value": "{\n\t\"trans_id\" : \"f2cc5fca-715e-4a86-b457-574bb7ba48d4\",\n\t\"description\" : \"Failed\",\n\t\"code\" : 1,\n\t\"success_topics\" : [\"591d3af1e4b0be20f3fc3eb9\"],\n\t\"fail_topics\" : [\"591d44c3e4b09eee109c1541\"]\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "trans_id": {
                  "type": "string",
                  "example": "f2cc5fca-715e-4a86-b457-574bb7ba48d4"
                },
                "description": {
                  "type": "string",
                  "example": "Failed"
                },
                "code": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                },
                "success_topics": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "example": "591d3af1e4b0be20f3fc3eb9"
                  }
                },
                "fail_topics": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "example": "591d44c3e4b09eee109c1541"
                  }
                }
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
