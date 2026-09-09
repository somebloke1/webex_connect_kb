# Get User Messages v2

Source: https://developers.webexconnect.io/reference/user-messages-2
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:35:07+00:00

> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to Webex Connect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

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

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "settings": "",
  "results": {
    "codes": [
      {
        "code": "{\n\t\"total\": 1,\n\t\"code\": \"0\",\n\t\"count\": 1,\n\t\"messages\": [\n\t\t{\n\t\t\t\"payload_type\": \"sentByUser\",\n\t\t\t\"extras\": {},\n\t\t\t\"media\": [],\n\t\t\t\"thread\":{\n\t\t\t\t\t\t\"id\": \"5acb5fa7e4b04b585f09434d_0_f3f3cac48f810645875f97466b36993b522167ea\"\n\t\t\t\t}\n\t\t\t\"message\": \"Test2\",\n\t\t\t\"userId\": \"WwopGfVlcgKxbI2egTiT/Q==/Z8WPLM\",\n\t\t\t\"tid\": \"RDF5856B2-5197-4956-9809-CE68C9A446B9\",\n\t\t\t\"created_on\": \"2018-04-20T06:18:54.058Z\",\n\t\t\t\"appid\": \"R209113055\",\n\t\t\t\"read_at\": \"\",\n\t\t\t\"delivered_at\": \"\",\n\t\t\t\"status\": \"submited\"\n\t\t}\n\t],\n\t\"description\": \"success\"\n}\n",
        "language": "json",
        "status": 200
      }
    ]
  },
  "examples": {
    "codes": [
      {
        "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{{appid}}/user/{userid}/threads/{threadid}/messages\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n",
        "language": "curl",
        "name": ""
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages',\n          headers: {\n            'Content-Type': 'application/json',\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\",\n    :headers => {'Content-Type' => 'application/json',\n\t'secretKey ' => '{secretKey}’})\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\"\n\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}'}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      }
    ]
  },
  "apiSetting": "6a675233ec1c893d8a7f67bd",
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
      "_id": "5f51e8451d9c99002b2815a6",
      "id": "5f51e8451d9c99002b2815a6"
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
      "_id": "5f51e8451d9c99002b2815a5",
      "id": "5f51e8451d9c99002b2815a5"
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
      "_id": "5f6d6f450f002800358bc6db",
      "id": "5f6d6f450f002800358bc6db"
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
      "_id": "5f6d6f450f002800358bc6da",
      "id": "5f6d6f450f002800358bc6da"
    },
    {
      "name": "threadid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Unique ID of a thread.",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "67acd576ce8b49005ddb186f",
      "id": "67acd576ce8b49005ddb186f"
    }
  ],
  "url": "/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{threadid}/messages",
  "method": "get"
}
```

## OpenAPI operation and component schemas

Operation extraction: selected. Missing operation definitions must not be inferred from this cache.

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Thread API v2",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://rtm.imiconnect.io"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{threadid}/messages",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get User Messages v2",
    "description": "This API retrieves a list of messages for a specified thread within a given app ID and user ID.",
    "operationId": "user-messages-2",
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
        "description": "Unique ID for a mobile/web app user",
        "schema": {
          "type": "string"
        },
        "required": true
      },
      {
        "name": "threadid",
        "in": "path",
        "description": "Unique ID of a thread.",
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
                "value": "{\n\t\"total\": 1,\n\t\"code\": \"0\",\n\t\"count\": 1,\n\t\"messages\": [\n\t\t{\n\t\t\t\"payload_type\": \"sentByUser\",\n\t\t\t\"extras\": {},\n\t\t\t\"media\": [],\n\t\t\t\"thread\":{\n\t\t\t\t\t\t\"id\": \"5acb5fa7e4b04b585f09434d_0_f3f3cac48f810645875f97466b36993b522167ea\"\n\t\t\t\t}\n\t\t\t\"message\": \"Test2\",\n\t\t\t\"userId\": \"WwopGfVlcgKxbI2egTiT/Q==/Z8WPLM\",\n\t\t\t\"tid\": \"RDF5856B2-5197-4956-9809-CE68C9A446B9\",\n\t\t\t\"created_on\": \"2018-04-20T06:18:54.058Z\",\n\t\t\t\"appid\": \"R209113055\",\n\t\t\t\"read_at\": \"\",\n\t\t\t\"delivered_at\": \"\",\n\t\t\t\"status\": \"submited\"\n\t\t}\n\t],\n\t\"description\": \"success\"\n}\n"
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
          "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{{appid}}/user/{userid}/threads/{threadid}/messages\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\",\n    :headers => {'Content-Type' => 'application/json',\n\t'secretKey ' => '{secretKey}’})\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v2/apps/{appid}/user/{userid}/threads/{{threadid}}/messages\"\n\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}'}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n"
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
