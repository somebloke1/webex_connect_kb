# Get User Threads

Source: https://developers.webexconnect.io/reference/thread-apis-user-threads
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:35:07+00:00



> **Know Your Endpoint**
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.



## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "apiSetting": "6a675233ec1c893d8a7f67ba",
  "examples": {
    "codes": [
      {
        "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n\n\n",
        "language": "curl",
        "name": "cURL"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads',\n          headers: {\n            'Content-Type': 'application/json',\n\t'secretKey': '{secretKey}'\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n\n\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads\",\n    :headers => {'Content-Type' => 'application/json',\n\t'secretKey ' => '{secretKey}’})\n# Print on console\nputs http\n\n\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n\n\n",
        "language": "javascript"
      },
      {
        "code": "import requests\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads\"\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}'}\nresponse = requests.request(\"GET\", url, headers=headers)\nprint(response.text)\n",
        "language": "python"
      }
    ]
  },
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"total\": 2,\n    \"code\": \"0\",\n    \"count\": 2,\n    \"threads\": [\n        {\n            \"updated_on\": \"2020-08-13T11:47:31.688Z\",\n            \"created_on\": \"2020-08-13T11:47:26.568Z\",\n            \"extras\": {\n                \"icFirstName\": \"John\",\n                \"icEmailId\": \"john@doe.com\",\n                \"icLastName\": \"Doe\"\n            },\n            \"id\": \"22110118-6352-4bbc-a53a-43b761ae18db\",\n            \"title\": \"Enquiry-[2020-08-13T17:17:25.747Z]\",\n            \"type\": \"Conversation\",\n            \"category\": \"Enquiry\",\n            \"status\": \"Active\"\n        },\n        {\n            \"updated_on\": \"2020-08-13T11:46:27.878Z\",\n            \"created_on\": \"2020-08-13T11:46:20.664Z\",\n            \"extras\": {\n                \"icFirstName\": \"John\",\n                \"icEmailId\": \"john@doe.com\",\n                \"icLastName\": \"Doe\"\n            },\n            \"id\": \"a88233f1-57b5-4cd7-8d85-1f689c690958\",\n            \"title\": \"Account-[2020-08-13T17:16:19.850Z]\",\n            \"type\": \"Conversation\",\n            \"category\": \"Account\",\n            \"status\": \"Active\"\n        }\n    ],\n    \"description\": \"success\"\n}",
        "status": 200
      }
    ]
  },
  "auth": "never",
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
      "_id": "5f51e5d22aabb800187f5120",
      "id": "5f51e5d22aabb800187f5120"
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
      "_id": "5f51e5d22aabb800187f511f",
      "id": "5f51e5d22aabb800187f511f"
    },
    {
      "name": "appid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "App ID is the unique ID for an app asset configured within the Webex Connect platform",
      "required": false,
      "in": "path",
      "ref": "",
      "_id": "5f6d6d65f5be080037f14ae2",
      "id": "5f6d6d65f5be080037f14ae2"
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
      "_id": "5f6d6d65f5be080037f14ae1",
      "id": "5f6d6d65f5be080037f14ae1"
    },
    {
      "name": "start",
      "type": "int",
      "enumValues": "",
      "default": "0",
      "desc": "Specifies the index of the first thread entry to return. This parameter is zero-based, meaning that if you set start=0, the response will include the first thread entry. For example, setting start=9 will return the 10th thread entry in the list, as indexing begins at 0.",
      "required": false,
      "in": "query",
      "ref": "",
      "_id": "67ad25bc6233020011520dc5",
      "id": "67ad25bc6233020011520dc5"
    },
    {
      "name": "limit",
      "type": "int",
      "enumValues": "",
      "default": "",
      "desc": "Defines the maximum number of thread entries to return in the response. This parameter helps to control the size of the dataset returned by the API. For example, if you set limit=1, the response will include only one thread entry starting from the index specified by the start parameter.",
      "required": false,
      "in": "query",
      "ref": "",
      "_id": "67ad25bc6233020011520dc4",
      "id": "67ad25bc6233020011520dc4"
    }
  ],
  "url": "/apps/{appid}/user/{userid}/threads",
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
  "path": "/apps/{appid}/user/{userid}/threads",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get User Threads",
    "description": "This API is used to retrieve a list of threads associated with a specific combination of app ID and user ID.",
    "operationId": "thread-apis-user-threads",
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
        "description": "App ID is the unique ID for an app asset configured within the Webex Connect platform",
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
        "name": "start",
        "in": "query",
        "description": "Specifies the index of the first thread entry to return. This parameter is zero-based, meaning that if you set start=0, the response will include the first thread entry. For example, setting start=9 will return the 10th thread entry in the list, as indexing begins at 0.",
        "schema": {
          "type": "integer",
          "format": "int32",
          "default": 0
        }
      },
      {
        "name": "limit",
        "in": "query",
        "description": "Defines the maximum number of thread entries to return in the response. This parameter helps to control the size of the dataset returned by the API. For example, if you set limit=1, the response will include only one thread entry starting from the index specified by the start parameter.",
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
                "value": "{\n    \"total\": 2,\n    \"code\": \"0\",\n    \"count\": 2,\n    \"threads\": [\n        {\n            \"updated_on\": \"2020-08-13T11:47:31.688Z\",\n            \"created_on\": \"2020-08-13T11:47:26.568Z\",\n            \"extras\": {\n                \"icFirstName\": \"John\",\n                \"icEmailId\": \"john@doe.com\",\n                \"icLastName\": \"Doe\"\n            },\n            \"id\": \"22110118-6352-4bbc-a53a-43b761ae18db\",\n            \"title\": \"Enquiry-[2020-08-13T17:17:25.747Z]\",\n            \"type\": \"Conversation\",\n            \"category\": \"Enquiry\",\n            \"status\": \"Active\"\n        },\n        {\n            \"updated_on\": \"2020-08-13T11:46:27.878Z\",\n            \"created_on\": \"2020-08-13T11:46:20.664Z\",\n            \"extras\": {\n                \"icFirstName\": \"John\",\n                \"icEmailId\": \"john@doe.com\",\n                \"icLastName\": \"Doe\"\n            },\n            \"id\": \"a88233f1-57b5-4cd7-8d85-1f689c690958\",\n            \"title\": \"Account-[2020-08-13T17:16:19.850Z]\",\n            \"type\": \"Conversation\",\n            \"category\": \"Account\",\n            \"status\": \"Active\"\n        }\n    ],\n    \"description\": \"success\"\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "total": {
                  "type": "integer",
                  "example": 2,
                  "default": 0
                },
                "code": {
                  "type": "string",
                  "example": "0"
                },
                "count": {
                  "type": "integer",
                  "example": 2,
                  "default": 0
                },
                "threads": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "updated_on": {
                        "type": "string",
                        "example": "2020-08-13T11:47:31.688Z"
                      },
                      "created_on": {
                        "type": "string",
                        "example": "2020-08-13T11:47:26.568Z"
                      },
                      "extras": {
                        "type": "object",
                        "properties": {
                          "icFirstName": {
                            "type": "string",
                            "example": "John"
                          },
                          "icEmailId": {
                            "type": "string",
                            "example": "john@doe.com"
                          },
                          "icLastName": {
                            "type": "string",
                            "example": "Doe"
                          }
                        }
                      },
                      "id": {
                        "type": "string",
                        "example": "22110118-6352-4bbc-a53a-43b761ae18db"
                      },
                      "title": {
                        "type": "string",
                        "example": "Enquiry-[2020-08-13T17:17:25.747Z]"
                      },
                      "type": {
                        "type": "string",
                        "example": "Conversation"
                      },
                      "category": {
                        "type": "string",
                        "example": "Enquiry"
                      },
                      "status": {
                        "type": "string",
                        "example": "Active"
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
    "security": [],
    "x-readme": {
      "code-samples": [
        {
          "language": "curl",
          "code": "-X GET https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads\n-H \"Content-Type : application/json\"\n-H \"secretKey: {secretKey}\"\n\n\n",
          "name": "cURL"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads\",\n    :headers => {'Content-Type' => 'application/json',\n\t'secretKey ' => '{secretKey}’})\n# Print on console\nputs http\n\n\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{{appid}}/user/{{userid}}/threads\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"secretKey\", \"{secretKey}\");\nxhr.send(data);\n\n\n"
        },
        {
          "language": "python",
          "code": "import requests\nurl = \" https://rtm.imiconnect.io/rtmsAPI/api/v1/apps/{appid}/user/{userid}/threads\"\nheaders = {'Content-Type': 'application/json', 'secretKey': '{secretKey}'}\nresponse = requests.request(\"GET\", url, headers=headers)\nprint(response.text)\n"
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
