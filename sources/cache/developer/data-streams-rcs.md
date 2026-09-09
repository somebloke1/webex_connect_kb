# Data Streams - RCS

Source: https://developers.webexconnect.io/reference/data-streams-rcs
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:48+00:00

**RCS - Inbound Message**

The following are the RCS inbound message payloads.

```json Incoming Message
{
"transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
"channel": "rcs",
"messageId": "12344321",
"dataIntegration": {
  "context": {
    "serviceId": "",
    "serviceName": "",
    "flowId": "",
    "flowName": "",
    "messagingAPI": "false"
    },
    "appContext": {
    }
  },
  "message": "hello",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "clientUUID ": "0a4a1900-98ef-4385-b9f9-5ef0927d6683",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "carrier": "8",
  "appId": "a_15984XXXXXXXXXX260",
  "serviceProvider": "ABC”,
  "msisdn": "+178XXXXXX32",
  "event": "MO",
  "ts": "2024-04-01T14:55:38.135+05:30"
  }
```
```json Incoming Attachment
{
"attachments": "[{\"payload\":{\"url\":\"https://rcs-user-content-us.storage.googleapis.com/d5d1fa92-19d8-467d-bbef-0aba94e5bf79/4b53d3803d5077a8031575e0f4b3a99610dfa851c8b0e8edc66b31134384\"},\"type\":\"image\"}]",
"transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
"channel": "rcs",
"messageId": "12344321",
"dataIntegration": {
  "context": {
    "serviceId": "",
    "serviceName": "",
    "flowId": "",
    "flowName": "",
    "messagingAPI": "false"
    },
    "appContext": {
    }
  },
  "message": "hello",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "clientUUID ": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "carrier": "8",
  "appId": "a_15984XXXXXXXXXX260",
  "serviceProvider": "ABC”,
  "msisdn": "+178XXXXXX32",
  "event": "MO",
  "ts": "2024-04-01T14:55:38.135+05:30"
  }
```
```json Postback
{
"postback": "Welcome",
"transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
"channel": "rcs",
"messageId": "12344321",
"dataIntegration": {
  "context": {
    "serviceId": "",
    "serviceName": "",
    "flowId": "",
    "flowName": "",
    "messagingAPI": "false"
    },
    "appContext": {
    }
  },
  "message": "hello",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "clientUUID ": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "carrier": "8",
  "appId": "a_15984XXXXXXXXXX260",
  "serviceProvider": "ABC”,
  "msisdn": "+178XXXXXX32",
  "event": "MO",
  "ts": "2024-04-01T14:55:38.135+05:30"
  }
```
```json Location Response
{
"transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
"latitude": "42.629926",
"channel": "rcs",
"messageId": "12344321",
"dataIntegration": {
  "context": {
    "serviceId": "",
    "serviceName": "",
    "flowId": "",
    "flowName": "",
    "messagingAPI": "false"
    },
    "appContext": {
    }
  },
  "message": "hello",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "clientUUID ": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "carrier": "8",
  "appId": "a_15984XXXXXXXXXX260",
  "serviceProvider": "ABC”,
  "msisdn": "+178XXXXXX32",
  "event": "MO",
  "ts": "2024-04-01T14:55:38.135+05:30",
  "longitude": "-71.3052476"
  }
```
```json Unsubscribe
{
"transid": "f88055de-e362-XXXX-XXXX-07d392964e1c",
"channel": "rcs",
"messageId": "ew7zkxlhqrXXXXXqddfyitnepi",
"dataIntegration": {
"context": {
"serviceId": "",
"serviceName": "",
"flowId": "",
"flowName": "",
"messagingAPI": "false"
},
"appContext": {
"tenant_identifier": "R6XXXXXMS",
"Topic": "bayonetenantTopic",
"URL": "b-1.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-3.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-2.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096",
"webhookurl": "https://integrations.imiconnect.co/v1/integration/"
}
},
"tid": "f88055de-e362-XXXX-XXXX-07d392964e1c",
"clientUUID": "0d41b41a-XXXX-XXXX-a9fb-24ce5334e18f",
"x-wx-gtrid": "5b973242-XXXX-XXXX-8e2a-5f1ff69f6b01",
"carrier": "8",
"appId": "a_1728283XXXXX801150",
"serviceProvider": "GOOGLE",
"msisdn": "+178XXXXX319",
"event": "UNSUBSCRIBE",
"ts": "2025-10-28T12:08:11.798+05:30"
}
```
```json Subscribe
{
"transid": "fe59b6a3-XXXX-XXXX-add1-74cb46cb8264",
"channel": "rcs",
"messageId": "dvspu3khzja4XXXXXasn6msocy",
"dataIntegration": {
"context": {
"serviceId": "",
"serviceName": "",
"flowId": "",
"flowName": "",
"messagingAPI": "false"
},
"appContext": {
"tenant_identifier": "R6XXXXXMS",
"Topic": "bayonetenantTopic",
"URL": "b-1.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-3.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-2.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096",
"webhookurl": "https://integrations.imiconnect.co/v1/integration/"
}
},
"tid": "fe59b6a3-368f-XXXX-XXXX-74cb46cb8264",
"clientUUID": "0d41b41a-XXXX-XXXX-a9fb-24ce5334e18f",
"x-wx-gtrid": "ce9229c3-XXXX-XXXX-93a1-8e16f4165d79",
"carrier": "573",
"appId": "a_1728283XXXXX801150",
"serviceProvider": "GOOGLE",
"msisdn": "+9196XXXXX269",
"event": "SUBSCRIBE",
"ts": "2025-10-28T13:24:29.411+05:30"
}
```

**RCS - Delivery Receipt**

The following are the RCS delivery receipts payloads.

```json Delivered
{
  "x-wx-gtrid": "rcsgtrid",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-04-01T15:11:16.792+05:30",
      "Description": "Delivered",
      "code": "7501",
      "deliveryChannel": "rcs",
      "additionalInfo": "",
      "destination": "+178XXXXXX32",
      "destinationType": "msisdn",
      "deliveryStatus": "Delivered"
    },
    "carrier": "8",
    "subtid": "",
    "transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d,
    "callbackData": "",
    "serviceProvider": "GOOGLE",
    "correlationid": "XXXXXXXXX"
  },
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
      
    }
  }
}

```
```json Read
{
  "x-wx-gtrid": "rcsgtrid",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-04-01T15:11:16.792+05:30",
      "Description": "Read",
      "code": "7501",
      "deliveryChannel": "rcs",
      "additionalInfo": "",
      "destination": "+178XXXXXX32",
      "destinationType": "msisdn",
      "deliveryStatus": "Read"
    },
    "carrier": "8",
    "subtid": "",
    "transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d,
    "callbackData": "",
    "serviceProvider": "GOOGLE",
    "correlationid": "XXXXXXXXX"
  },
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
      
    }
  }
}

```
```json Submitted
{
  "x-wx-gtrid": "rcsgtrid",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-04-01T15:11:16.792+05:30",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "rcs",
      "additionalInfo": "",
      "destination": "+178XXXXXX32",
      "destinationType": "msisdn",
      "deliveryStatus": "Submitted"
    },
    "carrier": "8",
    "subtid": "",
    "transid": "6dXXXX28-bXX8-4XXb-aXX0-ecXXXXXXXX05",
    "callbackData": "",
    "serviceProvider": "GOOGLE",
    "correlationid": "XXXXXXXXX"
  },
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
      
    }
  }
}
```
```json Failed
{
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-03-04T16:23:11.086+05:30",
      "Description": "Invalid media details",
      "code": "7740",
      "deliveryChannel": "rcs",
      "additionalInfo": "Invalid media URL",
      "destination": "+178XXXXXX32",
      "destinationType": "msisdn",
      "deliveryStatus": "Failed"
    },
    "carrier": "",
    "subtid": "13XXXX81-2XXe-4XX5-9XXd-36XXXXXXXX62",
    "transid": "cqXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
    "callbackData": "",
    "serviceProvider": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "Message type": "Dynamic Carousel",
      "serviceId": "6360",
      "serviceName": "RCS_1",
      "flowId": "4166",
      "flowName": "RCS Flow",
      "messagingAPI": "false"
    },
    "appContext": {}
  }
}
```

**RCS - Outbound Message**

The following are the RCS outbound message payloads.

```json Text Message
{
  "transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d,
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {}
  },
  "priority": 3,
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "content": {
    "fileSize": 0,
    "text": "RCS test in AWS staging qa sanity- 6.6",
    "type": "text"
  },
  "clientUUID": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "rcsgtrid",
  "appId": "a_15984XXXXXXXXXX260",
  "x_msg_seq": 0,
  "serviceKey": "dfXXXX26-fXX9-1XXc-bXXf-12XXXXXXX6b",
  "msisdn": "+178XXXXXX32",
  "carrierId": 0
}
```
```json File
{
  "transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d ",
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": { 
    }
  },
  "priority": 1,
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "content": {
    "fileSize": 342434,
    "suggestions": [
      {
        "displayText": "Yes",
        "postbackData": "dummy data",
        "type": "reply"
      },
      {
        "displayText": "Impact Mobile Office",
        "address": +178XXXXXX32",
        "postbackData": "dummy data",
        "latitude": "43.649269",
        "type": "viewLocation",
        "longitude": "-79.378423"
      },
      {
        "displayText": "Share location",
        "postbackData": "dummy data",
        "type": "shareLocation"
      },
      {
        "displayText": "Impact Mobile",
        "postbackData": " dummy data ",
        "type": "openUrl",
        "url": "http://www.impactmobile.com "
      },
      {
        "displayText": "Impact Mobile",
        "postbackData": " dummy data ",
        "meetingDescription": "http://www.impactmobile.com ",
        "startTime": "2017-03-14T00:00:00Z",
        "meetingTitle": "http://www.impactmobile.com ",
        "endTime": "2017-03-21T00:00:00Z",
        "type": "calendarEvent"
      },
      {
        "displayText": "Call Us!",
        "postbackData": " dummy data ",
        "phone": "+178XXXXXX32",
        "type": "dialPhone"
      }
    ],
    "mediaContentUrl": "https://file-examples.com/storage/fe0275ec7165ef4cb9b4af6/2017/10/file-example_PDF_500_kB.pdf",
    "type": "media"
  },
  "clientUUID": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "rcsgtrid",
  "appId": "a_15984XXXXXXXXXX260",
  "x_msg_seq": 0,
  "serviceKey": "dfXXXX26-fXX9-1XXc-bXXf-12XXXXXXX6b",
  "msisdn": "+178XXXXXX32",
  "carrierId": 0
}

```
```json Rich Card
{
  "transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d ",
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": { 
    }
  },
  "priority": 3,
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "content": {
    "richCard": {
      "orientation": "HORIZONTAL",
      "thumbnail": {
        "fileSize": 12864,
        "url": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/5476/5476500_sd.jpg;canvasHeight=442;canvasWidth=1034"
      },
      "thumbnailAlignment": "RIGHT",
      "description": "The description\" in AWS\\Staging",
      "media": {
        "fileSize": 0,
        "url": "https://file-examples.com/storage/fe17d655216606dd89d5226/2017/04/file_example_MP4_640_3MG.mp4",
        "height": "MEDIUM"
      },
      "title": "The Card Title\" R\rich card chk"
    },
    "fileSize": 0,
    "suggestions": [
      {
        "displayText": "Yes",
        "postbackData": "usr_msg_yes",
        "type": "reply"
      }
    ],
    "type": "standalone"
  },
  "clientUUID": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "rcsgtrid",
  "appId": "a_15984XXXXXXXXXX260",
  "x_msg_seq": 0,
  "serviceKey": "dfXXXX26-fXX9-1XXc-bXXf-12XXXXXXX6b",
  "msisdn": "+178XXXXXX32",
  "carrierId": 0
}
```
```json Carousel Card
{	
"transid": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d ",
  "dataIntegration": {
    "context": {
      "serviceId": "20824",
      "serviceName": "RCS6_1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": { 
    }
  },
  "priority": 3,
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "content": {
    "cards": [
      {
        "description": "Carousle card new from rule\rs Enter\n carriage check in AWS NV",
        "suggestions": [
          {
            "displayText": "Yes",
            "postbackData": "dummy data",
            "type": "reply"
          }
        ],
        "media": {
          "fileSize": 12053,
          "url": "https://file-examples.com/storage/fe1b802e1565fe057a1d758/2017/04/file_example_MP4_480_1_5MG.mp4",
          "height": "MEDIUM"
        },
        "title": "Carousel card\t check from API in QA\t with enter carriage"
      },
      {
        "description": "Carousel card",
        "suggestions": [
        ],
        "media": {
          "fileSize": 15860,
          "url": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/5476/5476500_sd.jpg;canvasHeight=442;canvasWidth=1034",
          "height": "MEDIUM"
        },
        "title": "Carousel card 2\t check from messaging API"
      }
    ],
    "fileSize": 0,
    "width": "MEDIUM",
    "suggestions": [
      {
        "displayText": "Yes",
        "postbackData": "dummy data",
        "type": "reply"
      },
      {
        "displayText": "Impact",
        "address": "+141XXXXXXXX34",
        "postbackData": "dummy data",
        "latitude": "43.649269",
        "type": "viewLocation",
        "longitude": "-79.378423"
      },
      {
        "displayText": "Share location",
        "postbackData": "e460dd65-e69b-XXXX-a5af-458683248f2d_url_google",
        "type": "shareLocation"
      }
    ],
    "type": "carousel"
  },
  "clientUUID": "0aXXXX00-9XXf-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "rcsgtrid",
  "appId": "a_15984XXXXXXXXXX260",
  "x_msg_seq": 0,
  "serviceKey": "dfXXXX26-fXX9-1XXc-bXXf-12XXXXXXX6b",
  "msisdn": "+178XXXXXX32",
  "carrierId": 0
}
```

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [],
  "examples": {
    "codes": []
  }
}
```
