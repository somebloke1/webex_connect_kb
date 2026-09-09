# Create App Profile

Source: https://developers.webexconnect.io/reference/createappprofile
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:49+00:00

> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

> 📘 
> 
> Profile details are encapsulated within the Attributes section. Additional key-value pairs may be added as required.

## **Status Codes**

This API may return the following response codes:

| Response Code | Message                                                         | Description                                                                                    |
| :------------ | :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| 1000          | Queued                                                          | Returned when the request is queued                                                            |
| 1002          | Partial success                                                 | Returned when at least one app profile could not be created successfully                       |
| 7000          | Invalid JSON                                                    | Returned when an invalid JSON request is sent                                                  |
| 7001          | Authentication failed                                           | Returned when the invalid service key or profile key is provided in the request                |
| 7002          | Service Key Missing                                             | Returned when the parameter _key_ is missing in the message request                            |
| 7003          | Mandatory parameters missing                                    | Returned when the mandatory parameters configured in the custom event are missing              |
| 7006          | Internal error occurred                                         | Returned when an internal error occurs                                                         |
| 7010          | Source IP is not in the allowed list                            | Returned when a request is sent from an IP that is not in the allowed list in Webex Connect     |
| 7011          | Invalid Attribute Value                                         | Returned when an invalid value is provided for the customer or app profile _Attributes_ object |
| 7018          | invalid app profile or app profile is not linked to this client | Returned when an application master profile does not exists                                    |

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "auth": "required",
  "examples": {
    "codes": [
      {
        "code": "-X POST https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}\n-H \"Content-Type : application/json\"\n-H \"key : {profilekey}\"\n",
        "language": "curl"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'POST',\n          uri: ' https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}} ',\n          headers: {\n            'Content-Type': 'application/json',\n\t'key': ' Profile key present in tenant setting '\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.post(\"https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\",\n    :headers => {'Content-Type' => 'application/json',\n\t'key' => ' Profile key present in tenant setting’})\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"key\", \"Profile key present in tenant setting\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\"\n\nheaders = {'Content-Type': 'application/json', 'key': ' Profile key present in tenant setting '}\n\nresponse = requests.request(\"POST\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"8955\",\n        \"Attributes\": {\n            \"status\": \"1\",\n\t\t\t\t\t\t\"verified\": \"1\",\n\t\t\t\t\t\t\"psid\": \"1652750724851329\",\n\t\t\t\t\t\t\"createdOn\": \"2018-08-26 12:26:03\",\n\t\t\t\t\t\t\"customerId\": \"1842\"\n\t\t\t\t\t\t\"name\": \"Ravipudi Durgaprasad\",\n\t\t\t\t\t\t\"profile_pic\": \"https://platform-lookaside.fbsbx.com/platform/profilepic/?\t\t\t\t\t\t\t psid=1652750724851329&width=1024&ext=1537878362&hash=AeQ6XJBhDeMC7RUN\",\n\t\t\t\t\t\t\"gender\": \"male\",\n\t\t\t\t\t\t\"locale\": \"en_US\",\n\t\t\t\t\t\t\"timezone\": \"5.5\",\n\t\t\t\t\t\t\"channel\": \"fb\",\n\t\t\t\t\t\t\"updatedOn\": \"2018-09-19 07:13:50\"\n\n        }\n    },\n                {\n        \"customerId\": \"8956\",\n        \"Attributes\": {\n            \"status\": \"1\",\n\t\t\t\t\t\t\"verified\": \"1\",\n\t\t\t\t\t\t\"psid\": \"1652750724851134\",\n\t\t\t\t\t\t\"createdOn\": \"2018-08-26 12:26:03\",\n\t\t\t\t\t\t\"customerId\": \"1845\"\n\t\t\t\t\t\t\"name\": \"Anil Dhar\",\n\t\t\t\t\t\t\"profile_pic\": \"https://platform-lookaside.fbsbx.com/platform/profilepic/?\t\t\t\t\t\t\t psid=1652750724851329&width=1024&ext=1537878362&hash=AeQ6XJBhDeMC7RUN\",\n\t\t\t\t\t\t\"gender\": \"male\",\n\t\t\t\t\t\t\"locale\": \"en_US\",\n\t\t\t\t\t\t\"timezone\": \"5.5\",\n\t\t\t\t\t\t\"channel\": \"fb\",\n\t\t\t\t\t\t\"updatedOn\": \"2018-09-25 07:14:35\"        }\n    }]\n}",
        "language": "json",
        "name": "Create App Profile - Facebook"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"8957\",\n        \"Attributes\": {\n            \"status\": \"1\",\n\t\t\t\t\t\t\"verified\": \"1\",\n\t\t\t\t\t\t\"twitterid\": \"3424284794\",\n\t\t\t\t\t\t\"twitter_handle\": \"BalajiSatuluri\",\n\t\t\t\t\t\t\"twitter_name\": \"Balaji Satuluri\",\n\t\t\t\t\t\t\"customerId\": \"3330\",\n\t\t\t\t\t\t\"geolocation\": \"\",\n\t\t\t\t\t\t\"timezone\": \"\",\n\t\t\t\t\t\t\"channel\": \"twitter\",\n\t\t\t\t\t\t\"createdOn\": \"2016-10-14 05:27:50\",\n\t\t\t\t\t\t\"updatedOn\": \"2018-09-19 07:07:29\"\n\n        }\n    }]",
        "language": "json",
        "name": "Create App Profile - Twitter"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"9876\",\n        \"Attributes\": {\n            \"created_on\": ISODate('2018-04-02T07:09:30.395Z'),\n\t\t\t\t\t\t\"updated_on\": ISODate('2018-04-02T07:25:22.660Z'),\n\t\t\t\t\t\t\"customerId\": \"8953\",\n\t\t\t\t\t\t\"city\": \"\",\n\t\t\t\t\t\t\"verified\": \"2018-04-02T07:25:22.660Z\",\n\t\t\t\t\t\t\"createdOn\": \"2018-04-02T06:09:30.611Z\",\n\t\t\t\t\t\t\"nick\": \"cogniti\",\n\t\t\t\t\t\t\"status\": \"1\",\n\t\t\t\t\t\t\"gender\": \"Female\",\n\t\t\t\t\t\t\"province\": \"\",\n\t\t\t\t\t\t\"language\": \"en\",\n\t\t\t\t\t\t\"country\": \"India\"\n        } \n    },\n               {\n        \"customerId\": \"9877\",\n        \"Attributes\": {\n            \"created_on\": ISODate('2018-04-02T07:10:30.395Z'),\n\t\t\t\t\t\t\"updated_on\": ISODate('2018-04-02T08:26:22.660Z'),\n\t\t\t\t\t\t\"customerId\": \"8954\",\n\t\t\t\t\t\t\"city\": \"\",\n\t\t\t\t\t\t\"verified\": \"2018-05-02T07:25:23.660Z\",\n\t\t\t\t\t\t\"createdOn\": \"2018-05-02T06:09:30.611Z\",\n\t\t\t\t\t\t\"nick\": \"cogniti\",\n\t\t\t\t\t\t\"status\": \"1\",\n\t\t\t\t\t\t\"gender\": \"Female\",\n\t\t\t\t\t\t\"province\": \"\",\n\t\t\t\t\t\t\"language\": \"en\",\n\t\t\t\t\t\t\"country\": \"India\"\n        }\n    }\n               ]\n}",
        "language": "json",
        "name": "Create App Profile - WeChat"
      },
      {
        "code": "{\n    \"Records\": [{\n        \"customerId\": \"9879\",\n        \"Attributes\": {\n\t\t\t\t\t\t\"status\": \"\",\n\t\t\t\t\t\t\"verified\": \"0\",\n\t\t\t\t\t\t\"customerId\": \"0774943838490264760\"\n          \t\"connectStatus\": \"1\",\n\t\t\t\t\t\t\"appId\": \"\",\n\t\t\t\t\t\t\"userId\": \"30774943838490264760\",\n\t\t\t\t\t\t\"password\": \"\",\n            \"deviceId\": \"HT59TBE00192\",\n            \"batterylevel\": \"\",\n            \"Bluetooth\": \"\",\n            \"cellid\": \"\",\n            \"connectType\": \"\",\n            \"email\": \"\",\n            \"externalmemory\": \"\",\n            \"foreground\": \"\",\n            \"foregroundapp\": \"\",\n            \"idlescreen\": \"\",\n            \"imei\": \"\",\n            \"imsi\": \"\",\n            \"internalmemory\": \"\",\n            \"IP\": \"\",\n            \"language\": \"\",\n            \"oldlocation\": \"[]\",\n            \"location\": \"\",\n            \"MAC\": \"\",\n            \"make\": \"HTC\",\n            \"MCC\": \"\",\n            \"MNC\": \"\",\n            \"model\": \"HTC One A9\",\n            \"NFC\": \"\",\n            \"os\": \"Android\",\n            \"osversion\": \"6.0.1\",\n            \"phonemode\": \"\",\n            \"presence\": \"\",\n            \"RAM\": \"\",\n            \"resolution\": \"\",\n            \"roaming\": \"\",\n            \"serialnumber\": \"\",\n            \"signalstrength\": \"\",\n            \"teleco\": \"\",\n            \"timespent\": \"\",\n            \"timezone\": \"\",\n            \"useragent\": \"\",\n            \"pushId\": \"fwYj0eb9jmM:APA91bF3hHgNR51OgRJ64dC2bmHa3Hh6BWHjSnDCv4ZFfvSgEiCx0p6bqeB0Ij9DdAy41t275Hhd02TC6BufvakJimEuGw_68nyUA9JWZXGylmfSkcC_2RSsys3yR6HLvZgu8esif_jd\",\n            \"rtmId\": \"30774943838490264760_HT59TBE00192\",\n            \"createdOn\": \"2018-09-11 15:37:28\",\n            \"last_opened\": \"2018-09-12T10:24:59.907Z\",\n            \"last_upgraded\": \"2018-09-11T15:37:29.067Z\",\n            \"channel\": \"rt\",\n            \"accounts\": \"\",\n            \"sdkversion\": \"\",\n        }\n    }]\n}",
        "language": "json",
        "name": "Create App Profile - In-app"
      },
      {
        "code": "{\n    \"Records\": [\n        {\n            \"customerId\": \"70993\",\n            \"Attributes\": {\n                \"status\": \"1\",\n                \"connectStatus\": \"1\",\n                \"rtmId\": \"1100333\",\n                \"userId\":\"112200\",\n                \"deviceId\": \"3304401\",\n                \"make\": \"nokia\",\n                \"model\": \"GM1901\",\n                \"os\": \"Android\",\n                \"osversion\": \"10\", \n                \"pushId\":\"5437bc5867465cb9\",\n                \"createdOn\": \"2016-07-11 17:02:51\",\n                \"last_opened\": \"2018-01-21T16:39:54+0530\",\n                \"last_upgraded\": \"2016-01-21T16:39:54+0530\"\n            }\n        }\n    ]\n}",
        "language": "json",
        "name": "Create App Profile - Push"
      }
    ]
  },
  "method": "post",
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
      "_id": "5f6ded51240f6d0032c41722",
      "id": "5f6ded51240f6d0032c41722"
    },
    {
      "name": "customerid",
      "type": "string",
      "enumValues": "",
      "default": "",
      "desc": "Customer ID is a Client specific ID (such as CRN) to uniquely identify a customer",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "5f6ded51240f6d0032c41721",
      "id": "5f6ded51240f6d0032c41721"
    },
    {
      "name": "attributes",
      "type": "object",
      "enumValues": "",
      "default": "",
      "desc": "Key value pairs to add",
      "required": true,
      "in": "body",
      "ref": "",
      "_id": "5f6ded51240f6d0032c41720",
      "id": "5f6ded51240f6d0032c41720"
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
      "_id": "5fd7012b57bcb8002ee86483",
      "id": "5fd7012b57bcb8002ee86483"
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
      "_id": "5fd7012b57bcb8002ee86482",
      "id": "5fd7012b57bcb8002ee86482"
    }
  ],
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"TotalCount\": 1,\n    \"FailureCount\": 0,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"code\": \"1000\",\n            \"customerId\": \"70993\",\n            \"description\": \"SUCCESS\"\n        }\n    ],\n    \"transid\": \"bd86e517-18b0-4189-a38c-64ba50c14728\",\n    \"description\": \"SUCCESS\",\n    \"SuccessCount\": 1\n}",
        "status": 200
      },
      {
        "code": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"8955\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        },\n      {\n            \"customerId\": \"8956\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}",
        "language": "json",
        "status": 202,
        "name": "Create App Profile - Facebook"
      },
      {
        "code": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"8957\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}",
        "language": "json",
        "status": 202,
        "name": "Create App Profile - Twitter"
      },
      {
        "code": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"9876\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        },\n       {\n            \"customerId\": \"9877\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}",
        "language": "json",
        "status": 202,
        "name": "Create App Profile - WeChat"
      },
      {
        "code": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"9879\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}",
        "language": "json",
        "status": 202,
        "name": "Create App Profile - In-app"
      }
    ]
  },
  "settings": "",
  "url": "/customerappprofile/{inappid}",
  "apiSetting": "6a675233ec1c893d8a7f67b8"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Profile API v2",
    "version": "6.20.0"
  },
  "servers": [
    {
      "url": "https://api.imiconnect.io/resources/v2"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "path": "/customerappprofile/{inappid}",
  "method": "post",
  "path_parameters": [],
  "operation": {
    "summary": "Create App Profile",
    "description": "This API is used to create customer's application profile.",
    "operationId": "createappprofile",
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
      }
    ],
    "requestBody": {
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "required": [
              "customerid",
              "attributes"
            ],
            "properties": {
              "customerid": {
                "type": "string",
                "description": "Customer ID is a Client specific ID (such as CRN) to uniquely identify a customer"
              },
              "attributes": {
                "type": "object",
                "description": "Key value pairs to add",
                "properties": {}
              }
            }
          },
          "examples": {
            "Create App Profile - Push": {
              "value": {
                "Records": [
                  {
                    "customerId": "70993",
                    "Attributes": {
                      "status": "1",
                      "connectStatus": "1",
                      "rtmId": "1100333",
                      "userId": "112200",
                      "deviceId": "3304401",
                      "make": "nokia",
                      "model": "GM1901",
                      "os": "Android",
                      "osversion": "10",
                      "pushId": "5437bc5867465cb9",
                      "createdOn": "2016-07-11 17:02:51",
                      "last_opened": "2018-01-21T16:39:54+0530",
                      "last_upgraded": "2016-01-21T16:39:54+0530"
                    }
                  }
                ]
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
                "value": "{\n    \"TotalCount\": 1,\n    \"FailureCount\": 0,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"code\": \"1000\",\n            \"customerId\": \"70993\",\n            \"description\": \"SUCCESS\"\n        }\n    ],\n    \"transid\": \"bd86e517-18b0-4189-a38c-64ba50c14728\",\n    \"description\": \"SUCCESS\",\n    \"SuccessCount\": 1\n}"
              }
            },
            "schema": {
              "type": "object",
              "properties": {
                "TotalCount": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                },
                "FailureCount": {
                  "type": "integer",
                  "example": 0,
                  "default": 0
                },
                "code": {
                  "type": "string",
                  "example": "1000"
                },
                "Results": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "code": {
                        "type": "string",
                        "example": "1000"
                      },
                      "customerId": {
                        "type": "string",
                        "example": "70993"
                      },
                      "description": {
                        "type": "string",
                        "example": "SUCCESS"
                      }
                    }
                  }
                },
                "transid": {
                  "type": "string",
                  "example": "bd86e517-18b0-4189-a38c-64ba50c14728"
                },
                "description": {
                  "type": "string",
                  "example": "SUCCESS"
                },
                "SuccessCount": {
                  "type": "integer",
                  "example": 1,
                  "default": 0
                }
              }
            }
          }
        }
      },
      "202": {
        "description": "202",
        "content": {
          "application/json": {
            "examples": {
              "Create App Profile - Facebook": {
                "value": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"8955\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        },\n      {\n            \"customerId\": \"8956\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}"
              },
              "Create App Profile - Twitter": {
                "value": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"8957\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}"
              },
              "Create App Profile - WeChat": {
                "value": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"9876\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        },\n       {\n            \"customerId\": \"9877\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}"
              },
              "Create App Profile - In-app": {
                "value": "{\n    \"FailureCount\": 1,\n    \"TotalCount\": 1,\n    \"description\": \"QUEUED\",\n    \"SuccessCount\": 1,\n    \"code\": \"1000\",\n    \"Results\": [\n        {\n            \"customerId\": \"9879\",\n            \"description\": \"QUEUED\",\n            \"code\": \"1000\"\n        }\n    ],\n    \"transid\": \"29a70681-43ea-44c0-9423-5fe4567f5cbb\"\n}"
              }
            },
            "schema": {
              "oneOf": [
                {
                  "title": "Create App Profile - Facebook",
                  "type": "object",
                  "properties": {
                    "FailureCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "TotalCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "description": {
                      "type": "string",
                      "example": "QUEUED"
                    },
                    "SuccessCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "Results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "customerId": {
                            "type": "string",
                            "example": "8955"
                          },
                          "description": {
                            "type": "string",
                            "example": "QUEUED"
                          },
                          "code": {
                            "type": "string",
                            "example": "1000"
                          }
                        }
                      }
                    },
                    "transid": {
                      "type": "string",
                      "example": "29a70681-43ea-44c0-9423-5fe4567f5cbb"
                    }
                  }
                },
                {
                  "title": "Create App Profile - Twitter",
                  "type": "object",
                  "properties": {
                    "FailureCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "TotalCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "description": {
                      "type": "string",
                      "example": "QUEUED"
                    },
                    "SuccessCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "Results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "customerId": {
                            "type": "string",
                            "example": "8957"
                          },
                          "description": {
                            "type": "string",
                            "example": "QUEUED"
                          },
                          "code": {
                            "type": "string",
                            "example": "1000"
                          }
                        }
                      }
                    },
                    "transid": {
                      "type": "string",
                      "example": "29a70681-43ea-44c0-9423-5fe4567f5cbb"
                    }
                  }
                },
                {
                  "title": "Create App Profile - WeChat",
                  "type": "object",
                  "properties": {
                    "FailureCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "TotalCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "description": {
                      "type": "string",
                      "example": "QUEUED"
                    },
                    "SuccessCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "Results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "customerId": {
                            "type": "string",
                            "example": "9876"
                          },
                          "description": {
                            "type": "string",
                            "example": "QUEUED"
                          },
                          "code": {
                            "type": "string",
                            "example": "1000"
                          }
                        }
                      }
                    },
                    "transid": {
                      "type": "string",
                      "example": "29a70681-43ea-44c0-9423-5fe4567f5cbb"
                    }
                  }
                },
                {
                  "title": "Create App Profile - In-app",
                  "type": "object",
                  "properties": {
                    "FailureCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "TotalCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "description": {
                      "type": "string",
                      "example": "QUEUED"
                    },
                    "SuccessCount": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "Results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "customerId": {
                            "type": "string",
                            "example": "9879"
                          },
                          "description": {
                            "type": "string",
                            "example": "QUEUED"
                          },
                          "code": {
                            "type": "string",
                            "example": "1000"
                          }
                        }
                      }
                    },
                    "transid": {
                      "type": "string",
                      "example": "29a70681-43ea-44c0-9423-5fe4567f5cbb"
                    }
                  }
                }
              ]
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
          "code": "-X POST https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}\n-H \"Content-Type : application/json\"\n-H \"key : {profilekey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.post(\"https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\",\n    :headers => {'Content-Type' => 'application/json',\n\t'key' => ' Profile key present in tenant setting’})\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"POST\", \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"key\", \"Profile key present in tenant setting\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://api.imiconnect.io/resources/v2/customerappprofile/{{inappid}}\"\n\nheaders = {'Content-Type': 'application/json', 'key': ' Profile key present in tenant setting '}\n\nresponse = requests.request(\"POST\", url, headers=headers)\n\nprint(response.text)\n"
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
