# Get App Profile by User ID

Source: https://developers.webexconnect.io/reference/get-app-profile-by-user-id
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:49+00:00

> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

[block:textarea]
{
  "text": "### **Response Parameters**",
  "sidebar": true
}
[/block]


| Parameter                        | Type   | Description                                                                     |
| :------------------------------- | :----- | :------------------------------------------------------------------------------ |
| Status                           | Number | Zero indicates success response                                                 |
| Description                      | String | Describes the status of API call                                                |
| Records                          | Array  | An array of Outward links and Inward links                                      |
| Record\[].Attributes             | Array  | Outward links and Inward links                                                  |
| Attributes\[].Name               | String | Name of the column. For example, CustomerId -Column Name                        |
| Attributes\[].Value              | String | Value Contained with in the column Eg: CustomerId- 1234                         |
| Attributes\[].ID                 | Number | System generated unique Id for the column                                       |
| InwardLinks                      | Array  | Shows app profiles mapped  to the Customer Id                                   |
| OutwardLinks                     | Array  | Displays customer profile information on Get app profile call                   |
| OutwardLinks\[].ProfileId        | Number | Unique system Generated ID  on profile store creation                           |
| OutwardLinks\[].ProfileName      | String | Profile store Name                                                              |
| OutwardLinks\[].Records          | Array  | List of columns mapped to the profile store Eg: Customer Id,Name,Mobile No etc. |
| OutwardLinks\[].Records\[].Value | String | Value Contained with in the column Eg: CustomerId- 1234                         |
| OutwardLinks\[].Records\[].ID    | Number | System generated unique Id for the column                                       |
| OutwardLinks\[].Records\[].Name  | String | Name of the column Eg : CustomerId -Column Name                                 |
| code                             | String | Internal code handling by imiconnect                                            |
| transid                          | String | Unique system generated id for API call                                         |

## **Status Codes**

This API may return the following response codes:

| Response Code | Message                      | Description                                                                     |
| :------------ | :--------------------------- | :------------------------------------------------------------------------------ |
| 1000          | Success                      | Returned when the request is completed successfully                             |
| 7000          | Invalid JSON                 | Returned when an invalid JSON request is sent                                   |
| 7001          | Authentication failed        | Returned when the invalid service key or profile key is provided in the request |
| 7003          | Mandatory parameters missing | Returned when the mandatory parameters configured in custom event are missing   |

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "/customerappprofile/<appID>?identifier=<userID>",
  "auth": "required",
  "apiSetting": "6a675233ec1c893d8a7f67b8",
  "examples": {
    "codes": [
      {
        "code": "-X GET https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\n-H \"Content-Type : application/json\"\n-H \"key : {profilekey}\"\n",
        "language": "curl"
      },
      {
        "code": "var request=require(\"request\");\n var options = {\n          method: 'GET',\n          uri: ' https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}',\n          headers: {\n            'Content-Type': 'application/json',\n\t'key': ' Profile key present in tenant setting '\n            }\n        };\n  request(options, function(error, response, body) {\n               if(error){\n                  console.log(error);\n             }else{\n                  console.log(response);\n            }\n        });\n",
        "language": "json",
        "name": "Node"
      },
      {
        "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\",\n    :headers => {'Content-Type' => 'application/json',\n\t'key' => ' Profile key present in tenant setting’})\n# Print on console\nputs http\n",
        "language": "ruby"
      },
      {
        "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"key\", \"Profile key present in tenant setting\");\nxhr.send(data);\n",
        "language": "javascript"
      },
      {
        "code": "import requests\n\nurl = \" https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\");\"\n\nheaders = {'Content-Type': 'application/json', 'key': ' Profile key present in tenant setting '}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n",
        "language": "python"
      },
      {
        "code": "https://api.imiconnect.com/resources/v2/customerappprofile/a_636035705699961900/8953",
        "language": "json",
        "name": "Get Single App Profile"
      },
      {
        "code": "https://api.imiconnect.com/resources/v2/customerappprofile/BO20055029?customerId=8953&customerId=8954",
        "language": "json",
        "name": "Get Multiple App Profiles"
      }
    ]
  },
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
      "_id": "5f6df21a813dfd006b198b2e",
      "id": "5f6df21a813dfd006b198b2e"
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
      "_id": "5f6df21a813dfd006b198b2d",
      "id": "5f6df21a813dfd006b198b2d"
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
      "_id": "5f6df21a813dfd006b198b2c",
      "id": "5f6df21a813dfd006b198b2c"
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
      "_id": "5f6df21a813dfd006b198b2b",
      "id": "5f6df21a813dfd006b198b2b"
    }
  ],
  "results": {
    "codes": [
      {
        "language": "json",
        "code": "{\n    \"Status\": 0,\n    \"Description\": \"success\",\n    \"code\": \"1000\",\n    \"transid\": \"b15f6e15-26f8-4538-959f-326209a0c2e4\",\n    \"Records\": [\n        {\n            \"OutwardLinks\": [\n                {\n                    \"ProfileID\": 3030,\n                    \"ProfileName\": \"imi2828_cpms_1\",\n                    \"Records\": [\n                        [\n                            {\n                                \"Value\": \"777777\",\n                                \"ID\": 67007,\n                                \"Name\": \"customerid\"\n                            },\n                            {\n                                \"Value\": \"sainath.a@imimobile.com\",\n                                \"ID\": 67008,\n                                \"Name\": \"email\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 67009,\n                                \"Name\": \"msisdn\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 67010,\n                                \"Name\": \"name\"\n                            },\n                            {\n                                \"Value\": \"false\",\n                                \"ID\": 71641,\n                                \"Name\": \"channel_pref\"\n                            }\n                        ]\n                    ]\n                }\n            ],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 86910,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"777777\",\n                    \"ID\": 86911,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"Check123457\",\n                    \"ID\": 86912,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"checkdevice1\",\n                    \"ID\": 86913,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 86914,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"37bc5867465cb95124e5e03aad905100f8154cb4f1f5cb8c4a01eae8ee75831612\",\n                    \"ID\": 86915,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"fb89d255-15e5-4a24-b35b-5d88bb6df2b9\",\n                    \"ID\": 86916,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"2018-01-21T16:39:54+0530\",\n                    \"ID\": 86917,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86918,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86919,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86920,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86921,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 86922,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"1\",\n                    \"ID\": 86923,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2016-07-11 17:02:51\",\n                    \"ID\": 86924,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        }\n    ]\n}\n",
        "status": 200
      },
      {
        "code": "{\n    \"Status\": 0,\n    \"Description\": \"success\",\n    \"code\": \"1000\",\n    \"transid\": \"c20df4b3-1dbe-4554-9179-c31b614c88aa\",\n    \"Records\": [\n        {\n            \"OutwardLinks\": [\n                {\n                    \"ProfileID\": 1288,\n                    \"ProfileName\": \"Showcase_cpms_1\",\n                    \"Records\": [\n                        [\n                            {\n                                \"Value\": \"07522178657\",\n                                \"ID\": 27673,\n                                \"Name\": \"msisdn\"\n                            },\n                            {\n                                \"Value\": \"1518124524912406\",\n                                \"ID\": 27674,\n                                \"Name\": \"email\"\n                            },\n                            {\n                                \"Value\": \"fbm\",\n                                \"ID\": 27675,\n                                \"Name\": \"name\"\n                            },\n                            {\n                                \"Value\": \"1234\",\n                                \"ID\": 27676,\n                                \"Name\": \"customerId\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27677,\n                                \"Name\": \"sms\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27678,\n                                \"Name\": \"voice\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27679,\n                                \"Name\": \"rt\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27680,\n                                \"Name\": \"fb\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27681,\n                                \"Name\": \"twitter\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27682,\n                                \"Name\": \"wechat\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27683,\n                                \"Name\": \"wa\"\n                            }\n                        ]\n                    ]\n                }\n            ],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"43e42902e645d42f\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"eE7iXpDQTCKyhYSo0e01Lp:APA91bEXnGFQ6eFMGtthUj6N9Eysk5vjJblqIa8Qk4pp_yveX_3w0DKPp8H0SpsGzm1Dhzz_50cDvDx_-krWrHP2-dGCod4dyo6-Z2sw_1Gaw4rrCkUZH332I1qBJpu4gza7LdVjcOs7\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"a0a2c9fd-a146-416a-a115-f5c4243bd9bd\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-17 08:49:05\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        },\n        {\n            \"OutwardLinks\": [\n                {\n                    \"ProfileID\": 1288,\n                    \"ProfileName\": \"Showcase_cpms_1\",\n                    \"Records\": [\n                        [\n                            {\n                                \"Value\": \"07522178657\",\n                                \"ID\": 27673,\n                                \"Name\": \"msisdn\"\n                            },\n                            {\n                                \"Value\": \"1518124524912406\",\n                                \"ID\": 27674,\n                                \"Name\": \"email\"\n                            },\n                            {\n                                \"Value\": \"fbm\",\n                                \"ID\": 27675,\n                                \"Name\": \"name\"\n                            },\n                            {\n                                \"Value\": \"1234\",\n                                \"ID\": 27676,\n                                \"Name\": \"customerId\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27677,\n                                \"Name\": \"sms\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27678,\n                                \"Name\": \"voice\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27679,\n                                \"Name\": \"rt\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27680,\n                                \"Name\": \"fb\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27681,\n                                \"Name\": \"twitter\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27682,\n                                \"Name\": \"wechat\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27683,\n                                \"Name\": \"wa\"\n                            }\n                        ]\n                    ]\n                }\n            ],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"43e42902e645d42f\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"af40c06d-fd27-4791-b9d5-58d87f4e47e4\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-22 13:05:42\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        },\n        {\n            \"OutwardLinks\": [],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"54d9019674bc3578\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"176ed19d-da10-462c-83fd-1bdf2b273606\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-23 05:37:05\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        },\n        {\n            \"OutwardLinks\": [],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"a6cd9e8951d388ab\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"dUwl94H6RVSiqWJFBKu4QJ:APA91bGjjlG0OEA4fK_FU91-PyOt3ZI-KEH16ZRGZC9ar65a9SK1DKI1kk6zYu4y_Tr8blgxzT5i0O93ZEHDqprGe_Wz0jr-_CWS0I56AXhp1Mk3r9-hYJArF374kKtAyM5g7_P0SwME\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"2158ecc5-293c-4254-9f0f-a85f450daa25\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-23 07:25:13\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        }\n    ]\n}\n",
        "language": "json",
        "status": 200,
        "name": "Get Single App Profile"
      },
      {
        "code": "{\n  \"Status\": 0,\n  \"Description\": \"success\",\n  \"Records\": [\n    {\n      \"Attributes\": [\n        {\n          \"Name\": \"status\",\n          \"Value\": 0,\n          \"ID\": 6063\n        },\n        {\n          \"Name\": \"verified\",\n          \"Value\": \"0\",\n          \"ID\": 6064\n        },\n        {\n          \"Name\": \"customerId\",\n          \"Value\": \"8954\",\n          \"ID\": 6065\n        },\n        {\n          \"Name\": \"connectStatus\",\n          \"Value\": 0,\n          \"ID\": 6066\n        },\n        {\n          \"Name\": \"appId\",\n          \"Value\": \"\",\n          \"ID\": 6067\n        },\n        {\n          \"Name\": \"userId\",\n          \"Value\": \"8954\",\n          \"ID\": 6068\n        },\n        {\n          \"Name\": \"password\",\n          \"Value\": \"\",\n          \"ID\": 6069\n        },\n        {\n          \"Name\": \"deviceId\",\n          \"Value\": \"\",\n          \"ID\": 6070\n        },\n        {\n          \"Name\": \"batterylevel\",\n          \"Value\": \"11%\",\n          \"ID\": 6071\n        },\n        {\n          \"Name\": \"Bluetooth\",\n          \"Value\": \"1\",\n          \"ID\": 6072\n        },\n        {\n          \"Name\": \"cellid\",\n          \"Value\": \"\",\n          \"ID\": 6073\n        },\n        {\n          \"Name\": \"connectType\",\n          \"Value\": \"\",\n          \"ID\": 6074\n        },\n        {\n          \"Name\": \"email\",\n          \"Value\": \"\",\n          \"ID\": 6075\n        },\n        {\n          \"Name\": \"externalmemory\",\n          \"Value\": \"\",\n          \"ID\": 6076\n        },\n        {\n          \"Name\": \"foreground\",\n          \"Value\": \"0\",\n          \"ID\": 6077\n        },\n        {\n          \"Name\": \"foregroundapp\",\n          \"Value\": \"\",\n          \"ID\": 6078\n        },\n        {\n          \"Name\": \"idlescreen\",\n          \"Value\": \"\",\n          \"ID\": 6079\n        },\n        {\n          \"Name\": \"imei\",\n          \"Value\": \"\",\n          \"ID\": 6080\n        },\n        {\n          \"Name\": \"imsi\",\n          \"Value\": \"\",\n          \"ID\": 6081\n        },\n        {\n          \"Name\": \"internalmemory\",\n          \"Value\": \"11.85 GB\",\n          \"ID\": 6082\n        },\n        {\n          \"Name\": \"IP\",\n          \"Value\": \"192.168.1.2\",\n          \"ID\": 6083\n        },\n        {\n          \"Name\": \"language\",\n          \"Value\": \"English (en-IN)\",\n          \"ID\": 6084\n        },\n        {\n          \"Name\": \"oldlocation\",\n          \"Value\": \"[ { \\\"val\\\" : \\\"[17.40209177851416,78.48741864001678]\\\" , \\\"count\\\" : 1 , \\\"trans_date\\\" : { \\\"$date\\\" : \\\"2016-02-22T19:07:49.714Z\\\"}}]\",\n          \"ID\": 6085\n        },\n        {\n          \"Name\": \"location\",\n          \"Value\": \"[17.4026309524199,78.48846396756929]\",\n          \"ID\": 6086\n        },\n        {\n          \"Name\": \"MAC\",\n          \"Value\": \"\",\n          \"ID\": 6087\n        },\n        {\n          \"Name\": \"make\",\n          \"Value\": \"Apple\",\n          \"ID\": 6088\n        },\n        {\n          \"Name\": \"MCC\",\n          \"Value\": \"\",\n          \"ID\": 6089\n        },\n        {\n          \"Name\": \"MNC\",\n          \"Value\": \"\",\n          \"ID\": 6090\n        },\n        {\n          \"Name\": \"model\",\n          \"Value\": \"iPhone 6 (GSM+CDMA)\",\n          \"ID\": 6091\n        },\n        {\n          \"Name\": \"NFC\",\n          \"Value\": \"\",\n          \"ID\": 6092\n        },\n        {\n          \"Name\": \"os\",\n          \"Value\": \"ios\",\n          \"ID\": 6093\n        },\n        {\n          \"Name\": \"osversion\",\n          \"Value\": \"9.2.1\",\n          \"ID\": 6094\n        },\n        {\n          \"Name\": \"phonemode\",\n          \"Value\": \"\",\n          \"ID\": 6095\n        },\n        {\n          \"Name\": \"presence\",\n          \"Value\": \"\",\n          \"ID\": 6096\n        },\n        {\n          \"Name\": \"RAM\",\n          \"Value\": \"1.00 GB\",\n          \"ID\": 6097\n        },\n        {\n          \"Name\": \"resolution\",\n          \"Value\": \"750x1334\",\n          \"ID\": 6098\n        },\n        {\n          \"Name\": \"roaming\",\n          \"Value\": \"\",\n          \"ID\": 6099\n        },\n        {\n          \"Name\": \"serialnumber\",\n          \"Value\": \"\",\n          \"ID\": 6100\n        },\n        {\n          \"Name\": \"signalstrength\",\n          \"Value\": \"\",\n          \"ID\": 6101\n        },\n        {\n          \"Name\": \"teleco\",\n          \"Value\": \"\",\n          \"ID\": 6102\n        },\n        {\n          \"Name\": \"timespent\",\n          \"Value\": 385,\n          \"ID\": 6103\n        },\n        {\n          \"Name\": \"timezone\",\n          \"Value\": \"\",\n          \"ID\": 6104\n        },\n        {\n          \"Name\": \"useragent\",\n          \"Value\": \"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15\",\n          \"ID\": 6105\n        },\n        {\n          \"Name\": \"pushId\",\n          \"Value\": \"6682513c1a97730fb9b69e1358273571fa5181e930bc37b9f905adead18322d3\",\n          \"ID\": 6106\n        },\n        {\n          \"Name\": \"rtmId\",\n          \"Value\": \"8954_08519E2437BB40FEBDF694B5C88703DC\",\n          \"ID\": 6107\n        },\n        {\n          \"Name\": \"createdOn\",\n          \"Value\": \"2016-08-09 12:57:26\",\n          \"ID\": 6108\n        },\n        {\n          \"Name\": \"last_opened\",\n          \"Value\": \"2016-02-22T18:38:57+0530\",\n          \"ID\": 6109\n        },\n        {\n          \"Name\": \"last_upgraded\",\n          \"Value\": \"2016-02-18T20:24:11+0530\",\n          \"ID\": 6110\n        },\n        {\n          \"Name\": \"channel\",\n          \"Value\": \"rt\",\n          \"ID\": 6111\n        }\n      ],\n      \"InwardLinks\": [],\n      \"OutwardLinks\": [\n        {\n          \"Records\": [\n            [\n              {\n                \"Name\": \"msisdn\",\n                \"Value\": \"918019031470\",\n                \"ID\": 5950\n              },\n              {\n                \"Name\": \"email\",\n                \"Value\": \"abc.pqr@imimobile.com\",\n                \"ID\": 5951\n              },\n              {\n                \"Name\": \"name\",\n                \"Value\": \"IMI\",\n                \"ID\": 5952\n              },\n              {\n                \"Name\": \"customerId\",\n                \"Value\": \"8954\",\n                \"ID\": 5953\n              },\n              {\n                \"Name\": \"country\",\n                \"Value\": \"1\",\n                \"ID\": 5954\n              },\n              {\n                \"Name\": \"city\",\n                \"Value\": \"1\",\n                \"ID\": 5955\n              },\n              {\n                \"Name\": \"sms\",\n                \"Value\": \"1\",\n                \"ID\": 5956\n              },\n              {\n                \"Name\": \"voice\",\n                \"Value\": \"1\",\n                \"ID\": 5957\n              },\n              {\n                \"Name\": \"ussd\",\n                \"Value\": \"1\",\n                \"ID\": 5958\n              },\n              {\n                \"Name\": \"rt\",\n                \"Value\": \"1\",\n                \"ID\": 5959\n              },\n              {\n                \"Name\": \"fb\",\n                \"Value\": \"1\",\n                \"ID\": 5960\n              },\n              {\n                \"Name\": \"fbc\",\n                \"Value\": \"1\",\n                \"ID\": 5961\n              },\n              {\n                \"Name\": \"twitter\",\n                \"Value\": \"1\",\n                \"ID\": 5962\n              },\n              {\n                \"Name\": \"wechat\",\n                \"Value\": \"1\",\n                \"ID\": 5963\n              },\n              {\n                \"Name\": \"wa\",\n                \"Value\": \"1\",\n                \"ID\": 5964\n              }\n            ]\n          ],\n          \"ProfileID\": 239,\n          \"ProfileName\": \"UK412_cpms_1\"\n        }\n      ]\n    },\n    {\n      \"Attributes\": [\n        {\n          \"Name\": \"status\",\n          \"Value\": 0,\n          \"ID\": 6063\n        },\n        {\n          \"Name\": \"verified\",\n          \"Value\": \"0\",\n          \"ID\": 6064\n        },\n        {\n          \"Name\": \"customerId\",\n          \"Value\": \"8953\",\n          \"ID\": 6065\n        },\n        {\n          \"Name\": \"connectStatus\",\n          \"Value\": 0,\n          \"ID\": 6066\n        },\n        {\n          \"Name\": \"appId\",\n          \"Value\": \"\",\n          \"ID\": 6067\n        },\n        {\n          \"Name\": \"userId\",\n          \"Value\": \"8953\",\n          \"ID\": 6068\n        },\n        {\n          \"Name\": \"password\",\n          \"Value\": \"\",\n          \"ID\": 6069\n        },\n        {\n          \"Name\": \"deviceId\",\n          \"Value\": \"08519E2437BB40FEBDF694B5C88703DC\",\n          \"ID\": 6070\n        },\n        {\n          \"Name\": \"batterylevel\",\n          \"Value\": \"56%\",\n          \"ID\": 6071\n        },\n        {\n          \"Name\": \"Bluetooth\",\n          \"Value\": \"1\",\n          \"ID\": 6072\n        },\n        {\n          \"Name\": \"cellid\",\n          \"Value\": \"\",\n          \"ID\": 6073\n        },\n        {\n          \"Name\": \"connectType\",\n          \"Value\": \"\",\n          \"ID\": 6074\n        },\n        {\n          \"Name\": \"email\",\n          \"Value\": \"\",\n          \"ID\": 6075\n        },\n        {\n          \"Name\": \"externalmemory\",\n          \"Value\": \"\",\n          \"ID\": 6076\n        },\n        {\n          \"Name\": \"foreground\",\n          \"Value\": \"0\",\n          \"ID\": 6077\n        },\n        {\n          \"Name\": \"foregroundapp\",\n          \"Value\": \"\",\n          \"ID\": 6078\n        },\n        {\n          \"Name\": \"idlescreen\",\n          \"Value\": \"\",\n          \"ID\": 6079\n        },\n        {\n          \"Name\": \"imei\",\n          \"Value\": \"\",\n          \"ID\": 6080\n        },\n        {\n          \"Name\": \"imsi\",\n          \"Value\": \"\",\n          \"ID\": 6081\n        },\n        {\n          \"Name\": \"internalmemory\",\n          \"Value\": \"11.85 GB\",\n          \"ID\": 6082\n        },\n        {\n          \"Name\": \"IP\",\n          \"Value\": \"10.0.3.199\",\n          \"ID\": 6083\n        },\n        {\n          \"Name\": \"language\",\n          \"Value\": \"English (en-IN)\",\n          \"ID\": 6084\n        },\n        {\n          \"Name\": \"oldlocation\",\n          \"Value\": \"[ { \\\"val\\\" : \\\"[17.43485703226193,78.39852736587122]\\\" , \\\"count\\\" : 1 , \\\"trans_date\\\" : { \\\"$date\\\" : \\\"2016-03-02T06:10:57.449Z\\\"}}]\",\n          \"ID\": 6085\n        },\n        {\n          \"Name\": \"location\",\n          \"Value\": \"[17.43586970339053,78.39709874994861]\",\n          \"ID\": 6086\n        },\n        {\n          \"Name\": \"MAC\",\n          \"Value\": \"\",\n          \"ID\": 6087\n        },\n        {\n          \"Name\": \"make\",\n          \"Value\": \"Apple\",\n          \"ID\": 6088\n        },\n        {\n          \"Name\": \"MCC\",\n          \"Value\": \"404\",\n          \"ID\": 6089\n        },\n        {\n          \"Name\": \"MNC\",\n          \"Value\": \"49\",\n          \"ID\": 6090\n        },\n        {\n          \"Name\": \"model\",\n          \"Value\": \"iPhone 6 (GSM+CDMA)\",\n          \"ID\": 6091\n        },\n        {\n          \"Name\": \"NFC\",\n          \"Value\": \"\",\n          \"ID\": 6092\n        },\n        {\n          \"Name\": \"os\",\n          \"Value\": \"ios\",\n          \"ID\": 6093\n        },\n        {\n          \"Name\": \"osversion\",\n          \"Value\": \"9.2.1\",\n          \"ID\": 6094\n        },\n        {\n          \"Name\": \"phonemode\",\n          \"Value\": \"\",\n          \"ID\": 6095\n        },\n        {\n          \"Name\": \"presence\",\n          \"Value\": \"\",\n          \"ID\": 6096\n        },\n        {\n          \"Name\": \"RAM\",\n          \"Value\": \"1.00 GB\",\n          \"ID\": 6097\n        },\n        {\n          \"Name\": \"resolution\",\n          \"Value\": \"750x1334\",\n          \"ID\": 6098\n        },\n        {\n          \"Name\": \"roaming\",\n          \"Value\": \"0\",\n          \"ID\": 6099\n        },\n        {\n          \"Name\": \"serialnumber\",\n          \"Value\": \"\",\n          \"ID\": 6100\n        },\n        {\n          \"Name\": \"signalstrength\",\n          \"Value\": \"\",\n          \"ID\": 6101\n        },\n        {\n          \"Name\": \"teleco\",\n          \"Value\": \"AirTel\",\n          \"ID\": 6102\n        },\n        {\n          \"Name\": \"timespent\",\n          \"Value\": 4242,\n          \"ID\": 6103\n        },\n        {\n          \"Name\": \"timezone\",\n          \"Value\": \"Asia/Kolkata\",\n          \"ID\": 6104\n        },\n        {\n          \"Name\": \"useragent\",\n          \"Value\": \"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15\",\n          \"ID\": 6105\n        },\n        {\n          \"Name\": \"pushId\",\n          \"Value\": \"cf81c1b537de65fb26bc023f83008a6594fb74f9c8c96482a4427e9289bed217\",\n          \"ID\": 6106\n        },\n        {\n          \"Name\": \"rtmId\",\n          \"Value\": \"8953_08519E2437BB40FEBDF694B5C88703DC\",\n          \"ID\": 6107\n        },\n        {\n          \"Name\": \"createdOn\",\n          \"Value\": \"2016-08-09 12:57:26\",\n          \"ID\": 6108\n        },\n        {\n          \"Name\": \"last_opened\",\n          \"Value\": \"2016-03-02T11:12:09+0530\",\n          \"ID\": 6109\n        },\n        {\n          \"Name\": \"last_upgraded\",\n          \"Value\": \"2016-03-02T11:12:09+0530\",\n          \"ID\": 6110\n        },\n        {\n          \"Name\": \"channel\",\n          \"Value\": \"rt\",\n          \"ID\": 6111\n        }\n      ],\n      \"InwardLinks\": [],\n      \"OutwardLinks\": [\n        {\n          \"Records\": [\n            [\n              {\n                \"Name\": \"msisdn\",\n                \"Value\": \"919908505526\",\n                \"ID\": 5950\n              },\n              {\n                \"Name\": \"email\",\n                \"Value\": \"abc.lmnop@imimobile.com\",\n                \"ID\": 5951\n              },\n              {\n                \"Name\": \"name\",\n                \"Value\": \"LMNOP\",\n                \"ID\": 5952\n              },\n              {\n                \"Name\": \"customerId\",\n                \"Value\": \"8953\",\n                \"ID\": 5953\n              },\n              {\n                \"Name\": \"country\",\n                \"Value\": \"1\",\n                \"ID\": 5954\n              },\n              {\n                \"Name\": \"city\",\n                \"Value\": \"1\",\n                \"ID\": 5955\n              },\n              {\n                \"Name\": \"sms\",\n                \"Value\": \"1\",\n                \"ID\": 5956\n              },\n              {\n                \"Name\": \"voice\",\n                \"Value\": \"1\",\n                \"ID\": 5957\n              },\n              {\n                \"Name\": \"ussd\",\n                \"Value\": \"1\",\n                \"ID\": 5958\n              },\n              {\n                \"Name\": \"rt\",\n                \"Value\": \"1\",\n                \"ID\": 5959\n              },\n              {\n                \"Name\": \"fb\",\n                \"Value\": \"1\",\n                \"ID\": 5960\n              },\n              {\n                \"Name\": \"fbc\",\n                \"Value\": \"1\",\n                \"ID\": 5961\n              },\n              {\n                \"Name\": \"twitter\",\n                \"Value\": \"1\",\n                \"ID\": 5962\n              },\n              {\n                \"Name\": \"wechat\",\n                \"Value\": \"1\",\n                \"ID\": 5963\n              },\n              {\n                \"Name\": \"wa\",\n                \"Value\": \"1\",\n                \"ID\": 5964\n              }\n            ]\n          ],\n          \"ProfileID\": 239,\n          \"ProfileName\": \"UK412_cpms_1\"\n        }\n      ]\n    }\n  ],\n  \"code\": \"1000\",\n  \"transid\": \"67bcc0f8-6fef-4d1c-90e0-cfaaf3dafb63\"\n}",
        "language": "json",
        "status": 200,
        "name": "Get Multiple App Profiles"
      }
    ]
  },
  "settings": ""
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
  "path": "/customerappprofile/<appID>?identifier=<userID>",
  "method": "get",
  "path_parameters": [],
  "operation": {
    "summary": "Get App Profile by User ID",
    "description": "This API is used to retrieve a customer's application profile for a given *appid* and *user ID*.",
    "operationId": "get-app-profile-by-user-id",
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
        "name": "userid",
        "in": "path",
        "description": "Unique ID for a mobile/web app user",
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
    "responses": {
      "200": {
        "description": "200",
        "content": {
          "application/json": {
            "examples": {
              "Result": {
                "value": "{\n    \"Status\": 0,\n    \"Description\": \"success\",\n    \"code\": \"1000\",\n    \"transid\": \"b15f6e15-26f8-4538-959f-326209a0c2e4\",\n    \"Records\": [\n        {\n            \"OutwardLinks\": [\n                {\n                    \"ProfileID\": 3030,\n                    \"ProfileName\": \"imi2828_cpms_1\",\n                    \"Records\": [\n                        [\n                            {\n                                \"Value\": \"777777\",\n                                \"ID\": 67007,\n                                \"Name\": \"customerid\"\n                            },\n                            {\n                                \"Value\": \"sainath.a@imimobile.com\",\n                                \"ID\": 67008,\n                                \"Name\": \"email\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 67009,\n                                \"Name\": \"msisdn\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 67010,\n                                \"Name\": \"name\"\n                            },\n                            {\n                                \"Value\": \"false\",\n                                \"ID\": 71641,\n                                \"Name\": \"channel_pref\"\n                            }\n                        ]\n                    ]\n                }\n            ],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 86910,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"777777\",\n                    \"ID\": 86911,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"Check123457\",\n                    \"ID\": 86912,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"checkdevice1\",\n                    \"ID\": 86913,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 86914,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"37bc5867465cb95124e5e03aad905100f8154cb4f1f5cb8c4a01eae8ee75831612\",\n                    \"ID\": 86915,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"fb89d255-15e5-4a24-b35b-5d88bb6df2b9\",\n                    \"ID\": 86916,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"2018-01-21T16:39:54+0530\",\n                    \"ID\": 86917,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86918,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86919,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86920,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 86921,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 86922,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"1\",\n                    \"ID\": 86923,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2016-07-11 17:02:51\",\n                    \"ID\": 86924,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        }\n    ]\n}\n"
              },
              "Get Single App Profile": {
                "value": "{\n    \"Status\": 0,\n    \"Description\": \"success\",\n    \"code\": \"1000\",\n    \"transid\": \"c20df4b3-1dbe-4554-9179-c31b614c88aa\",\n    \"Records\": [\n        {\n            \"OutwardLinks\": [\n                {\n                    \"ProfileID\": 1288,\n                    \"ProfileName\": \"Showcase_cpms_1\",\n                    \"Records\": [\n                        [\n                            {\n                                \"Value\": \"07522178657\",\n                                \"ID\": 27673,\n                                \"Name\": \"msisdn\"\n                            },\n                            {\n                                \"Value\": \"1518124524912406\",\n                                \"ID\": 27674,\n                                \"Name\": \"email\"\n                            },\n                            {\n                                \"Value\": \"fbm\",\n                                \"ID\": 27675,\n                                \"Name\": \"name\"\n                            },\n                            {\n                                \"Value\": \"1234\",\n                                \"ID\": 27676,\n                                \"Name\": \"customerId\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27677,\n                                \"Name\": \"sms\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27678,\n                                \"Name\": \"voice\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27679,\n                                \"Name\": \"rt\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27680,\n                                \"Name\": \"fb\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27681,\n                                \"Name\": \"twitter\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27682,\n                                \"Name\": \"wechat\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27683,\n                                \"Name\": \"wa\"\n                            }\n                        ]\n                    ]\n                }\n            ],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"43e42902e645d42f\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"eE7iXpDQTCKyhYSo0e01Lp:APA91bEXnGFQ6eFMGtthUj6N9Eysk5vjJblqIa8Qk4pp_yveX_3w0DKPp8H0SpsGzm1Dhzz_50cDvDx_-krWrHP2-dGCod4dyo6-Z2sw_1Gaw4rrCkUZH332I1qBJpu4gza7LdVjcOs7\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"a0a2c9fd-a146-416a-a115-f5c4243bd9bd\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-17 08:49:05\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        },\n        {\n            \"OutwardLinks\": [\n                {\n                    \"ProfileID\": 1288,\n                    \"ProfileName\": \"Showcase_cpms_1\",\n                    \"Records\": [\n                        [\n                            {\n                                \"Value\": \"07522178657\",\n                                \"ID\": 27673,\n                                \"Name\": \"msisdn\"\n                            },\n                            {\n                                \"Value\": \"1518124524912406\",\n                                \"ID\": 27674,\n                                \"Name\": \"email\"\n                            },\n                            {\n                                \"Value\": \"fbm\",\n                                \"ID\": 27675,\n                                \"Name\": \"name\"\n                            },\n                            {\n                                \"Value\": \"1234\",\n                                \"ID\": 27676,\n                                \"Name\": \"customerId\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27677,\n                                \"Name\": \"sms\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27678,\n                                \"Name\": \"voice\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27679,\n                                \"Name\": \"rt\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27680,\n                                \"Name\": \"fb\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27681,\n                                \"Name\": \"twitter\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27682,\n                                \"Name\": \"wechat\"\n                            },\n                            {\n                                \"Value\": \"1\",\n                                \"ID\": 27683,\n                                \"Name\": \"wa\"\n                            }\n                        ]\n                    ]\n                }\n            ],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"43e42902e645d42f\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"af40c06d-fd27-4791-b9d5-58d87f4e47e4\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-22 13:05:42\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        },\n        {\n            \"OutwardLinks\": [],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"54d9019674bc3578\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"176ed19d-da10-462c-83fd-1bdf2b273606\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-23 05:37:05\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        },\n        {\n            \"OutwardLinks\": [],\n            \"Attributes\": [\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135193,\n                    \"Name\": \"verified\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135194,\n                    \"Name\": \"customerId\"\n                },\n                {\n                    \"Value\": \"1234\",\n                    \"ID\": 135195,\n                    \"Name\": \"userId\"\n                },\n                {\n                    \"Value\": \"a6cd9e8951d388ab\",\n                    \"ID\": 135196,\n                    \"Name\": \"deviceId\"\n                },\n                {\n                    \"Value\": \"Android\",\n                    \"ID\": 135197,\n                    \"Name\": \"os\"\n                },\n                {\n                    \"Value\": \"dUwl94H6RVSiqWJFBKu4QJ:APA91bGjjlG0OEA4fK_FU91-PyOt3ZI-KEH16ZRGZC9ar65a9SK1DKI1kk6zYu4y_Tr8blgxzT5i0O93ZEHDqprGe_Wz0jr-_CWS0I56AXhp1Mk3r9-hYJArF374kKtAyM5g7_P0SwME\",\n                    \"ID\": 135198,\n                    \"Name\": \"pushId\"\n                },\n                {\n                    \"Value\": \"2158ecc5-293c-4254-9f0f-a85f450daa25\",\n                    \"ID\": 135199,\n                    \"Name\": \"rtmId\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135200,\n                    \"Name\": \"last_opened\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135201,\n                    \"Name\": \"ios_fcmpushid\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135202,\n                    \"Name\": \"language\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135203,\n                    \"Name\": \"timezone\"\n                },\n                {\n                    \"Value\": \"\",\n                    \"ID\": 135204,\n                    \"Name\": \"foreground\"\n                },\n                {\n                    \"Value\": \"false\",\n                    \"ID\": 135205,\n                    \"Name\": \"guest\"\n                },\n                {\n                    \"Value\": \"0\",\n                    \"ID\": 135206,\n                    \"Name\": \"status\"\n                },\n                {\n                    \"Value\": \"2020-09-23 07:25:13\",\n                    \"ID\": 135207,\n                    \"Name\": \"createdOn\"\n                }\n            ],\n            \"InwardLinks\": []\n        }\n    ]\n}\n"
              },
              "Get Multiple App Profiles": {
                "value": "{\n  \"Status\": 0,\n  \"Description\": \"success\",\n  \"Records\": [\n    {\n      \"Attributes\": [\n        {\n          \"Name\": \"status\",\n          \"Value\": 0,\n          \"ID\": 6063\n        },\n        {\n          \"Name\": \"verified\",\n          \"Value\": \"0\",\n          \"ID\": 6064\n        },\n        {\n          \"Name\": \"customerId\",\n          \"Value\": \"8954\",\n          \"ID\": 6065\n        },\n        {\n          \"Name\": \"connectStatus\",\n          \"Value\": 0,\n          \"ID\": 6066\n        },\n        {\n          \"Name\": \"appId\",\n          \"Value\": \"\",\n          \"ID\": 6067\n        },\n        {\n          \"Name\": \"userId\",\n          \"Value\": \"8954\",\n          \"ID\": 6068\n        },\n        {\n          \"Name\": \"password\",\n          \"Value\": \"\",\n          \"ID\": 6069\n        },\n        {\n          \"Name\": \"deviceId\",\n          \"Value\": \"\",\n          \"ID\": 6070\n        },\n        {\n          \"Name\": \"batterylevel\",\n          \"Value\": \"11%\",\n          \"ID\": 6071\n        },\n        {\n          \"Name\": \"Bluetooth\",\n          \"Value\": \"1\",\n          \"ID\": 6072\n        },\n        {\n          \"Name\": \"cellid\",\n          \"Value\": \"\",\n          \"ID\": 6073\n        },\n        {\n          \"Name\": \"connectType\",\n          \"Value\": \"\",\n          \"ID\": 6074\n        },\n        {\n          \"Name\": \"email\",\n          \"Value\": \"\",\n          \"ID\": 6075\n        },\n        {\n          \"Name\": \"externalmemory\",\n          \"Value\": \"\",\n          \"ID\": 6076\n        },\n        {\n          \"Name\": \"foreground\",\n          \"Value\": \"0\",\n          \"ID\": 6077\n        },\n        {\n          \"Name\": \"foregroundapp\",\n          \"Value\": \"\",\n          \"ID\": 6078\n        },\n        {\n          \"Name\": \"idlescreen\",\n          \"Value\": \"\",\n          \"ID\": 6079\n        },\n        {\n          \"Name\": \"imei\",\n          \"Value\": \"\",\n          \"ID\": 6080\n        },\n        {\n          \"Name\": \"imsi\",\n          \"Value\": \"\",\n          \"ID\": 6081\n        },\n        {\n          \"Name\": \"internalmemory\",\n          \"Value\": \"11.85 GB\",\n          \"ID\": 6082\n        },\n        {\n          \"Name\": \"IP\",\n          \"Value\": \"192.168.1.2\",\n          \"ID\": 6083\n        },\n        {\n          \"Name\": \"language\",\n          \"Value\": \"English (en-IN)\",\n          \"ID\": 6084\n        },\n        {\n          \"Name\": \"oldlocation\",\n          \"Value\": \"[ { \\\"val\\\" : \\\"[17.40209177851416,78.48741864001678]\\\" , \\\"count\\\" : 1 , \\\"trans_date\\\" : { \\\"$date\\\" : \\\"2016-02-22T19:07:49.714Z\\\"}}]\",\n          \"ID\": 6085\n        },\n        {\n          \"Name\": \"location\",\n          \"Value\": \"[17.4026309524199,78.48846396756929]\",\n          \"ID\": 6086\n        },\n        {\n          \"Name\": \"MAC\",\n          \"Value\": \"\",\n          \"ID\": 6087\n        },\n        {\n          \"Name\": \"make\",\n          \"Value\": \"Apple\",\n          \"ID\": 6088\n        },\n        {\n          \"Name\": \"MCC\",\n          \"Value\": \"\",\n          \"ID\": 6089\n        },\n        {\n          \"Name\": \"MNC\",\n          \"Value\": \"\",\n          \"ID\": 6090\n        },\n        {\n          \"Name\": \"model\",\n          \"Value\": \"iPhone 6 (GSM+CDMA)\",\n          \"ID\": 6091\n        },\n        {\n          \"Name\": \"NFC\",\n          \"Value\": \"\",\n          \"ID\": 6092\n        },\n        {\n          \"Name\": \"os\",\n          \"Value\": \"ios\",\n          \"ID\": 6093\n        },\n        {\n          \"Name\": \"osversion\",\n          \"Value\": \"9.2.1\",\n          \"ID\": 6094\n        },\n        {\n          \"Name\": \"phonemode\",\n          \"Value\": \"\",\n          \"ID\": 6095\n        },\n        {\n          \"Name\": \"presence\",\n          \"Value\": \"\",\n          \"ID\": 6096\n        },\n        {\n          \"Name\": \"RAM\",\n          \"Value\": \"1.00 GB\",\n          \"ID\": 6097\n        },\n        {\n          \"Name\": \"resolution\",\n          \"Value\": \"750x1334\",\n          \"ID\": 6098\n        },\n        {\n          \"Name\": \"roaming\",\n          \"Value\": \"\",\n          \"ID\": 6099\n        },\n        {\n          \"Name\": \"serialnumber\",\n          \"Value\": \"\",\n          \"ID\": 6100\n        },\n        {\n          \"Name\": \"signalstrength\",\n          \"Value\": \"\",\n          \"ID\": 6101\n        },\n        {\n          \"Name\": \"teleco\",\n          \"Value\": \"\",\n          \"ID\": 6102\n        },\n        {\n          \"Name\": \"timespent\",\n          \"Value\": 385,\n          \"ID\": 6103\n        },\n        {\n          \"Name\": \"timezone\",\n          \"Value\": \"\",\n          \"ID\": 6104\n        },\n        {\n          \"Name\": \"useragent\",\n          \"Value\": \"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15\",\n          \"ID\": 6105\n        },\n        {\n          \"Name\": \"pushId\",\n          \"Value\": \"6682513c1a97730fb9b69e1358273571fa5181e930bc37b9f905adead18322d3\",\n          \"ID\": 6106\n        },\n        {\n          \"Name\": \"rtmId\",\n          \"Value\": \"8954_08519E2437BB40FEBDF694B5C88703DC\",\n          \"ID\": 6107\n        },\n        {\n          \"Name\": \"createdOn\",\n          \"Value\": \"2016-08-09 12:57:26\",\n          \"ID\": 6108\n        },\n        {\n          \"Name\": \"last_opened\",\n          \"Value\": \"2016-02-22T18:38:57+0530\",\n          \"ID\": 6109\n        },\n        {\n          \"Name\": \"last_upgraded\",\n          \"Value\": \"2016-02-18T20:24:11+0530\",\n          \"ID\": 6110\n        },\n        {\n          \"Name\": \"channel\",\n          \"Value\": \"rt\",\n          \"ID\": 6111\n        }\n      ],\n      \"InwardLinks\": [],\n      \"OutwardLinks\": [\n        {\n          \"Records\": [\n            [\n              {\n                \"Name\": \"msisdn\",\n                \"Value\": \"918019031470\",\n                \"ID\": 5950\n              },\n              {\n                \"Name\": \"email\",\n                \"Value\": \"abc.pqr@imimobile.com\",\n                \"ID\": 5951\n              },\n              {\n                \"Name\": \"name\",\n                \"Value\": \"IMI\",\n                \"ID\": 5952\n              },\n              {\n                \"Name\": \"customerId\",\n                \"Value\": \"8954\",\n                \"ID\": 5953\n              },\n              {\n                \"Name\": \"country\",\n                \"Value\": \"1\",\n                \"ID\": 5954\n              },\n              {\n                \"Name\": \"city\",\n                \"Value\": \"1\",\n                \"ID\": 5955\n              },\n              {\n                \"Name\": \"sms\",\n                \"Value\": \"1\",\n                \"ID\": 5956\n              },\n              {\n                \"Name\": \"voice\",\n                \"Value\": \"1\",\n                \"ID\": 5957\n              },\n              {\n                \"Name\": \"ussd\",\n                \"Value\": \"1\",\n                \"ID\": 5958\n              },\n              {\n                \"Name\": \"rt\",\n                \"Value\": \"1\",\n                \"ID\": 5959\n              },\n              {\n                \"Name\": \"fb\",\n                \"Value\": \"1\",\n                \"ID\": 5960\n              },\n              {\n                \"Name\": \"fbc\",\n                \"Value\": \"1\",\n                \"ID\": 5961\n              },\n              {\n                \"Name\": \"twitter\",\n                \"Value\": \"1\",\n                \"ID\": 5962\n              },\n              {\n                \"Name\": \"wechat\",\n                \"Value\": \"1\",\n                \"ID\": 5963\n              },\n              {\n                \"Name\": \"wa\",\n                \"Value\": \"1\",\n                \"ID\": 5964\n              }\n            ]\n          ],\n          \"ProfileID\": 239,\n          \"ProfileName\": \"UK412_cpms_1\"\n        }\n      ]\n    },\n    {\n      \"Attributes\": [\n        {\n          \"Name\": \"status\",\n          \"Value\": 0,\n          \"ID\": 6063\n        },\n        {\n          \"Name\": \"verified\",\n          \"Value\": \"0\",\n          \"ID\": 6064\n        },\n        {\n          \"Name\": \"customerId\",\n          \"Value\": \"8953\",\n          \"ID\": 6065\n        },\n        {\n          \"Name\": \"connectStatus\",\n          \"Value\": 0,\n          \"ID\": 6066\n        },\n        {\n          \"Name\": \"appId\",\n          \"Value\": \"\",\n          \"ID\": 6067\n        },\n        {\n          \"Name\": \"userId\",\n          \"Value\": \"8953\",\n          \"ID\": 6068\n        },\n        {\n          \"Name\": \"password\",\n          \"Value\": \"\",\n          \"ID\": 6069\n        },\n        {\n          \"Name\": \"deviceId\",\n          \"Value\": \"08519E2437BB40FEBDF694B5C88703DC\",\n          \"ID\": 6070\n        },\n        {\n          \"Name\": \"batterylevel\",\n          \"Value\": \"56%\",\n          \"ID\": 6071\n        },\n        {\n          \"Name\": \"Bluetooth\",\n          \"Value\": \"1\",\n          \"ID\": 6072\n        },\n        {\n          \"Name\": \"cellid\",\n          \"Value\": \"\",\n          \"ID\": 6073\n        },\n        {\n          \"Name\": \"connectType\",\n          \"Value\": \"\",\n          \"ID\": 6074\n        },\n        {\n          \"Name\": \"email\",\n          \"Value\": \"\",\n          \"ID\": 6075\n        },\n        {\n          \"Name\": \"externalmemory\",\n          \"Value\": \"\",\n          \"ID\": 6076\n        },\n        {\n          \"Name\": \"foreground\",\n          \"Value\": \"0\",\n          \"ID\": 6077\n        },\n        {\n          \"Name\": \"foregroundapp\",\n          \"Value\": \"\",\n          \"ID\": 6078\n        },\n        {\n          \"Name\": \"idlescreen\",\n          \"Value\": \"\",\n          \"ID\": 6079\n        },\n        {\n          \"Name\": \"imei\",\n          \"Value\": \"\",\n          \"ID\": 6080\n        },\n        {\n          \"Name\": \"imsi\",\n          \"Value\": \"\",\n          \"ID\": 6081\n        },\n        {\n          \"Name\": \"internalmemory\",\n          \"Value\": \"11.85 GB\",\n          \"ID\": 6082\n        },\n        {\n          \"Name\": \"IP\",\n          \"Value\": \"10.0.3.199\",\n          \"ID\": 6083\n        },\n        {\n          \"Name\": \"language\",\n          \"Value\": \"English (en-IN)\",\n          \"ID\": 6084\n        },\n        {\n          \"Name\": \"oldlocation\",\n          \"Value\": \"[ { \\\"val\\\" : \\\"[17.43485703226193,78.39852736587122]\\\" , \\\"count\\\" : 1 , \\\"trans_date\\\" : { \\\"$date\\\" : \\\"2016-03-02T06:10:57.449Z\\\"}}]\",\n          \"ID\": 6085\n        },\n        {\n          \"Name\": \"location\",\n          \"Value\": \"[17.43586970339053,78.39709874994861]\",\n          \"ID\": 6086\n        },\n        {\n          \"Name\": \"MAC\",\n          \"Value\": \"\",\n          \"ID\": 6087\n        },\n        {\n          \"Name\": \"make\",\n          \"Value\": \"Apple\",\n          \"ID\": 6088\n        },\n        {\n          \"Name\": \"MCC\",\n          \"Value\": \"404\",\n          \"ID\": 6089\n        },\n        {\n          \"Name\": \"MNC\",\n          \"Value\": \"49\",\n          \"ID\": 6090\n        },\n        {\n          \"Name\": \"model\",\n          \"Value\": \"iPhone 6 (GSM+CDMA)\",\n          \"ID\": 6091\n        },\n        {\n          \"Name\": \"NFC\",\n          \"Value\": \"\",\n          \"ID\": 6092\n        },\n        {\n          \"Name\": \"os\",\n          \"Value\": \"ios\",\n          \"ID\": 6093\n        },\n        {\n          \"Name\": \"osversion\",\n          \"Value\": \"9.2.1\",\n          \"ID\": 6094\n        },\n        {\n          \"Name\": \"phonemode\",\n          \"Value\": \"\",\n          \"ID\": 6095\n        },\n        {\n          \"Name\": \"presence\",\n          \"Value\": \"\",\n          \"ID\": 6096\n        },\n        {\n          \"Name\": \"RAM\",\n          \"Value\": \"1.00 GB\",\n          \"ID\": 6097\n        },\n        {\n          \"Name\": \"resolution\",\n          \"Value\": \"750x1334\",\n          \"ID\": 6098\n        },\n        {\n          \"Name\": \"roaming\",\n          \"Value\": \"0\",\n          \"ID\": 6099\n        },\n        {\n          \"Name\": \"serialnumber\",\n          \"Value\": \"\",\n          \"ID\": 6100\n        },\n        {\n          \"Name\": \"signalstrength\",\n          \"Value\": \"\",\n          \"ID\": 6101\n        },\n        {\n          \"Name\": \"teleco\",\n          \"Value\": \"AirTel\",\n          \"ID\": 6102\n        },\n        {\n          \"Name\": \"timespent\",\n          \"Value\": 4242,\n          \"ID\": 6103\n        },\n        {\n          \"Name\": \"timezone\",\n          \"Value\": \"Asia/Kolkata\",\n          \"ID\": 6104\n        },\n        {\n          \"Name\": \"useragent\",\n          \"Value\": \"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15\",\n          \"ID\": 6105\n        },\n        {\n          \"Name\": \"pushId\",\n          \"Value\": \"cf81c1b537de65fb26bc023f83008a6594fb74f9c8c96482a4427e9289bed217\",\n          \"ID\": 6106\n        },\n        {\n          \"Name\": \"rtmId\",\n          \"Value\": \"8953_08519E2437BB40FEBDF694B5C88703DC\",\n          \"ID\": 6107\n        },\n        {\n          \"Name\": \"createdOn\",\n          \"Value\": \"2016-08-09 12:57:26\",\n          \"ID\": 6108\n        },\n        {\n          \"Name\": \"last_opened\",\n          \"Value\": \"2016-03-02T11:12:09+0530\",\n          \"ID\": 6109\n        },\n        {\n          \"Name\": \"last_upgraded\",\n          \"Value\": \"2016-03-02T11:12:09+0530\",\n          \"ID\": 6110\n        },\n        {\n          \"Name\": \"channel\",\n          \"Value\": \"rt\",\n          \"ID\": 6111\n        }\n      ],\n      \"InwardLinks\": [],\n      \"OutwardLinks\": [\n        {\n          \"Records\": [\n            [\n              {\n                \"Name\": \"msisdn\",\n                \"Value\": \"919908505526\",\n                \"ID\": 5950\n              },\n              {\n                \"Name\": \"email\",\n                \"Value\": \"abc.lmnop@imimobile.com\",\n                \"ID\": 5951\n              },\n              {\n                \"Name\": \"name\",\n                \"Value\": \"LMNOP\",\n                \"ID\": 5952\n              },\n              {\n                \"Name\": \"customerId\",\n                \"Value\": \"8953\",\n                \"ID\": 5953\n              },\n              {\n                \"Name\": \"country\",\n                \"Value\": \"1\",\n                \"ID\": 5954\n              },\n              {\n                \"Name\": \"city\",\n                \"Value\": \"1\",\n                \"ID\": 5955\n              },\n              {\n                \"Name\": \"sms\",\n                \"Value\": \"1\",\n                \"ID\": 5956\n              },\n              {\n                \"Name\": \"voice\",\n                \"Value\": \"1\",\n                \"ID\": 5957\n              },\n              {\n                \"Name\": \"ussd\",\n                \"Value\": \"1\",\n                \"ID\": 5958\n              },\n              {\n                \"Name\": \"rt\",\n                \"Value\": \"1\",\n                \"ID\": 5959\n              },\n              {\n                \"Name\": \"fb\",\n                \"Value\": \"1\",\n                \"ID\": 5960\n              },\n              {\n                \"Name\": \"fbc\",\n                \"Value\": \"1\",\n                \"ID\": 5961\n              },\n              {\n                \"Name\": \"twitter\",\n                \"Value\": \"1\",\n                \"ID\": 5962\n              },\n              {\n                \"Name\": \"wechat\",\n                \"Value\": \"1\",\n                \"ID\": 5963\n              },\n              {\n                \"Name\": \"wa\",\n                \"Value\": \"1\",\n                \"ID\": 5964\n              }\n            ]\n          ],\n          \"ProfileID\": 239,\n          \"ProfileName\": \"UK412_cpms_1\"\n        }\n      ]\n    }\n  ],\n  \"code\": \"1000\",\n  \"transid\": \"67bcc0f8-6fef-4d1c-90e0-cfaaf3dafb63\"\n}"
              }
            },
            "schema": {
              "oneOf": [
                {
                  "type": "object",
                  "properties": {
                    "Status": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "Description": {
                      "type": "string",
                      "example": "success"
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "transid": {
                      "type": "string",
                      "example": "b15f6e15-26f8-4538-959f-326209a0c2e4"
                    },
                    "Records": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "OutwardLinks": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "ProfileID": {
                                  "type": "integer",
                                  "example": 3030,
                                  "default": 0
                                },
                                "ProfileName": {
                                  "type": "string",
                                  "example": "imi2828_cpms_1"
                                },
                                "Records": {
                                  "type": "array",
                                  "items": {
                                    "type": "array",
                                    "items": {
                                      "type": "object",
                                      "properties": {
                                        "Value": {
                                          "type": "string",
                                          "example": "777777"
                                        },
                                        "ID": {
                                          "type": "integer",
                                          "example": 67007,
                                          "default": 0
                                        },
                                        "Name": {
                                          "type": "string",
                                          "example": "customerid"
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          },
                          "Attributes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "Value": {
                                  "type": "string",
                                  "example": "0"
                                },
                                "ID": {
                                  "type": "integer",
                                  "example": 86910,
                                  "default": 0
                                },
                                "Name": {
                                  "type": "string",
                                  "example": "verified"
                                }
                              }
                            }
                          },
                          "InwardLinks": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {}
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "title": "Get Single App Profile",
                  "type": "object",
                  "properties": {
                    "Status": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "Description": {
                      "type": "string",
                      "example": "success"
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "transid": {
                      "type": "string",
                      "example": "c20df4b3-1dbe-4554-9179-c31b614c88aa"
                    },
                    "Records": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "OutwardLinks": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "ProfileID": {
                                  "type": "integer",
                                  "example": 1288,
                                  "default": 0
                                },
                                "ProfileName": {
                                  "type": "string",
                                  "example": "Showcase_cpms_1"
                                },
                                "Records": {
                                  "type": "array",
                                  "items": {
                                    "type": "array",
                                    "items": {
                                      "type": "object",
                                      "properties": {
                                        "Value": {
                                          "type": "string",
                                          "example": "07522178657"
                                        },
                                        "ID": {
                                          "type": "integer",
                                          "example": 27673,
                                          "default": 0
                                        },
                                        "Name": {
                                          "type": "string",
                                          "example": "msisdn"
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          },
                          "Attributes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "Value": {
                                  "type": "string",
                                  "example": "0"
                                },
                                "ID": {
                                  "type": "integer",
                                  "example": 135193,
                                  "default": 0
                                },
                                "Name": {
                                  "type": "string",
                                  "example": "verified"
                                }
                              }
                            }
                          },
                          "InwardLinks": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {}
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "title": "Get Multiple App Profiles",
                  "type": "object",
                  "properties": {
                    "Status": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "Description": {
                      "type": "string",
                      "example": "success"
                    },
                    "Records": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "Attributes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "Name": {
                                  "type": "string",
                                  "example": "status"
                                },
                                "Value": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "ID": {
                                  "type": "integer",
                                  "example": 6063,
                                  "default": 0
                                }
                              }
                            }
                          },
                          "InwardLinks": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {}
                            }
                          },
                          "OutwardLinks": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "Records": {
                                  "type": "array",
                                  "items": {
                                    "type": "array",
                                    "items": {
                                      "type": "object",
                                      "properties": {
                                        "Name": {
                                          "type": "string",
                                          "example": "msisdn"
                                        },
                                        "Value": {
                                          "type": "string",
                                          "example": "918019031470"
                                        },
                                        "ID": {
                                          "type": "integer",
                                          "example": 5950,
                                          "default": 0
                                        }
                                      }
                                    }
                                  }
                                },
                                "ProfileID": {
                                  "type": "integer",
                                  "example": 239,
                                  "default": 0
                                },
                                "ProfileName": {
                                  "type": "string",
                                  "example": "UK412_cpms_1"
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    "code": {
                      "type": "string",
                      "example": "1000"
                    },
                    "transid": {
                      "type": "string",
                      "example": "67bcc0f8-6fef-4d1c-90e0-cfaaf3dafb63"
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
          "code": "-X GET https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\n-H \"Content-Type : application/json\"\n-H \"key : {profilekey}\"\n"
        },
        {
          "language": "ruby",
          "code": "require 'httparty'\n# Create the HTTP objects and post request\nhttp = HTTParty.get(\"https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\",\n    :headers => {'Content-Type' => 'application/json',\n\t'key' => ' Profile key present in tenant setting’})\n# Print on console\nputs http\n"
        },
        {
          "language": "javascript",
          "code": "var data = null;\n\nvar xhr = new XMLHttpRequest();\n\nxhr.addEventListener(\"readystatechange\", function () {\n  if (this.readyState === this.DONE) {\n    console.log(this.responseText);\n  }\n});\n\nxhr.open(\"GET\", \" https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\");\nxhr.setRequestHeader(\"Content-Type\", \"application/json\");\nxhr.setRequestHeader(\"key\", \"Profile key present in tenant setting\");\nxhr.send(data);\n"
        },
        {
          "language": "python",
          "code": "import requests\n\nurl = \" https://api.imiconnect.io/resources/v2/customerappprofile/{inappid}?identifier={userId}\");\"\n\nheaders = {'Content-Type': 'application/json', 'key': ' Profile key present in tenant setting '}\n\nresponse = requests.request(\"GET\", url, headers=headers)\n\nprint(response.text)\n"
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
