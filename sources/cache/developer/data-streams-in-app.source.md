**In-App - Inbound Message**

The following are the Live Chat / In-App inbound message payloads.

```json Incoming Message
{
   "attachments":"",
   "clientId":"EK20133633/xxxx/v2_610FA9CFEDBxxxxEAC82CF60759BB0C0",
   "transid":"d94ba95c-xxxx-4c4e-xxxx-7851028415f4",
   "channel":"Rtm",
   "extras":"",
   "dataIntegration":{
      "context":{
         "serviceId":"",
         "serviceName":"",
         "flowId":"",
         "flowName":"",
         "messagingAPI":"false"
      },
      "appContext":{
         
      }
   },
   "thread":"{\"updated_on\":\"2024-11-xxxx:52:55.947Z\",\"created_on\":\"2024-11-xxxx:52:40.801Z\",\"id\":\"fd321782-dc4c-4107-bb6a-ebfc473f9e0a\",\"title\":\"MyStore 483\",\"category\":\"MyStore 483\",\"type\":\"Conversation\",\"unread_msg_count\":0,\"status\":\"Active\"}",
   "message":"",
   "userId":"8686",
   "tid":"d94ba95c-xxxx-4c4e-xxxx-7851028415f4",
   "thread_title":"MyStore 483",
   "clientUUID":"9e911426-xxxx-4747-xxxx-d9499c7433bd",
   "x-wx-gtrid":"7528f6be-xxxx-4777-xxxx-548b879a61b7",
   "thread_id":"fd321782-xxxx-4107-xxxx-ebfc473f9e0a",
   "appId":"Exxxx33633",
   "replyTo":"",
   "event":"MO",
   "ts":"2024-11-xxxx:23:00.284+05:30"
}
```
```json Incoming Attachment
{
   "attachments":"[{\"preview\":\"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\",\"file\":\"https://qa-appleattachment.s3.amazonaws.com/dbd82a30-918e-4222-b799-c3879ae98eabd2d93f4c-293e-403a-8fdc-0db7cfb0d28f?keyUri=kms%3A%2F%2Fkms-us-int.wbx2.com%2Fkeys%2F3e42f5f1-5f82-4dcb-918d-b04f844aad2d&JWE=eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..LBIBZpjvxHhH9uIY.p3g7qG3xGIDpnBRLs5kY4jXB42Rzria6L8w_czkoxjjwQSnsKj87oQxH9ho9fohucIOB4_LZ6zifexvqXAbBCqvFfdHRDvIcfxMxyONzzYvZJJHgtoBuU3xFrR_aZ589MgiGNugeOXK7K0u29ToCZJmyDzSvd5tFsLbhPl9NdlcUheiAhnwZZTJR3Yhb4E3Cw9UbjRfdrqabW2oMbeeg6dZ2bli9UP3Mf4gTGp6cGPV59CLnlU4_8gpO26SHU8H-KSqVvreNcifLkM9n55DGWGtt54nHPXTcb-0xiwk0Ta0xZJgDol8etCEaZyVzX0b_N0Y0DulCLwT6lmkbcB510kD7GGJdsvGv2rUd8dgAkzucwzRsd94DTZ9C.nJlHRNZ41d0LcSxmF43jRw\",\"size\":75370,\"id\":\"302947189875262\",\"contentType\":\"image\"}]",
   "clientId":"EK20133633/xxxx/v2_610FA9CFEDBxxxxEAC82CF60759BB0C0",
   "transid":"defc578b-xxxx-4405-xxxx-09f9b67e1f52",
   "channel":"Rtm",
   "extras":"",
   "dataIntegration":{
      "context":{
         "serviceId":"",
         "serviceName":"",
         "flowId":"",
         "flowName":"",
         "messagingAPI":"false"
      },
      "appContext":{
         
      }
   },
   "thread":"{\"updated_on\":\"2024-11-xxxx:26:35.949Z\",\"id\":\"20fade24-xxxx-459f-xxxx-2415936ff3eb\",\"unread_msg_count\":0,\"title\":\"Thread1Test\",\"type\":\"Conversation\",\"status\":\"Active\"}",
   "message":"",
   "userId":"xxxx",
   "tid":"defc578b-xxxx-4405-xxxx-09f9b67e1f52",
   "thread_title":"Thread1Test",
   "clientUUID":"9e911426-xxxx-4747-xxxx-d9499c7433bd",
   "x-wx-gtrid":"fcb9c714-xxxx-4559-xxxx-f0b010ae773c",
   "thread_id":"20fade24-xxxx-459f-xxxx-2415936ff3eb",
   "appId":"EK2xxxx633",
   "replyTo":"",
   "event":"MO",
   "ts":"2024-11-xxxx:58:06.386+05:30"
}
```
```json Postback
{
    "attachments": "",
    "clientId": "EK20133633/xxxx/v2_610FA9CFEDB64xxxxC82CF60759BB0C0",
    "transid": "64475517-xxxx-445a-xxxx-d416d9ed9f0f",
    "channel": "Rtm",
    "interactiveData": "{\"reference\":\"postback\",\"identifier\":\"postback\",\"title\":\"postback\",\"type\":\"quickReplyPostback\"}",
    "extras": "",
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
    "thread": "{\"updated_on\":\"2024-11-xxxx:06:16.152Z\",\"created_on\":\"2024-11-xxxx:57:12.725Z\",\"id\":\"70f01690-xxxx-4cc7-xxxx-00ed1823dc43\",\"title\":\"iOS Test 776\",\"category\":\"iOS Test 776\",\"type\":\"Conversation\",\"unread_msg_count\":0,\"status\":\"Active\"}",
    "message": "postback",
    "userId": "xxxx",
    "tid": "64475517-xxxx-445a-xxxx-d416d9ed9f0f",
    "thread_title": "iOS Test 776",
    "clientUUID": "9e911426-xxxx-4747-xxxx-d9499c7433bd",
    "x-wx-gtrid": "822e9c85-xxxx-40bb-xxxx-cbff99c57e85",
    "thread_id": "70f01690-xxxx-4cc7-xxxx-00ed1823dc43",
    "appId": "EKxxxx3633",
    "replyTo": "",
    "event": "OnPostback",
    "ts": "2024-11-xxxx:36:17.510+05:30"
}
```
```json On Thread Close
{
    "origin": "gateway",
    "channel": "Rtm",
    "dataIntegration": {
        "context": {
            "serviceId": "76",
            "serviceName": "RegInApp",
            "flowId": "xxxx",
            "flowName": "Flow3Threadclosed",
            "messagingAPI": "false"
        },
        "appContext": {
            
        }
    },
    "type": "Conversation",
    "title": "FormtEstThread",
    "userId": "9897",
    "tid": "32a8bd14-xxxx-4e05-xxxx-75d112720035",
    "threadId": "99d56588-xxxx-4263-xxxx-b822c7b7b517",
    "x-wx-gtrid": "14d45a2a-xxxx-4d42-xxxx-cacf0a93915f",
    "datetime": "2024-11-xxxx:08:26.982+05:30",
    "appId": "EK20133633",
    "event": "OnThreadClosed",
    "status": "Closed",
    "ts": "2024-11-xxxx:08:26.982+05:30"
}
```
```json Custom Event
{
    "transid": "27075df0-xxxx-4929-xxxx-6dd6f1e436a3",
    "channel": "Rtm",
    "dataIntegration": [
        {
            "prebuiltId": xxxx,
            "outBoundEventNotificationEnabled": 1,
            "drEventNotificationEnabled": 1,
            "context": {
                "serviceId": "",
                "serviceName": "",
                "flowId": "",
                "flowName": "",
                "messagingAPI": "false"
            },
            "userAuditNotificationEnabled": 0,
            "assetLevel": 1,
            "isInboundEventNotificationEnabled": 1,
            "dataIntegrationid": 172
        }
    ],
    "thread": "{\"id\":\"99d56588-xxxx-4263-xxxx-b822c7b7b517\",\"title\":\"FormtEstThread\",\"type\":\"Conversation\",\"unread_msg_count\":0,\"status\":\"Closed\"}",
    "event_identifier": "MO",
    "userId": "9897",
    "deviceId": "05667xxxxa671eb3",
    "tid": "27075df0-xxxx-4929-xxxx-6dd6f1e436a3",
    "clientUUID": "9e911426-xxxx-4747-xxxx-d9499c7433bd",
    "x-wx-gtrid": "0f91c362-xxxx-4700-xxxx-99a573c5c74b",
    "channel_identifier": "RTM",
    "appId": "EKxxxx3633",
    "tenantId": 3,
    "event": "UpdateThreadACK",
    "ts": "2024-11-xxxx:08:28.713+05:30"
}
```
```json Typing Start
{
  "clientId": "NA18140011/XXXXXX/V2_41d0f523288c4591",
  "transid": "c7fa78a5-XXXX-XXXX-9350-c1324c00a00c",
  "channel": "Rtm",
  "extras": "",
  "dataIntegration": [
    {
      "prebuiltId": 50472,
      "outBoundEventNotificationEnabled": 1,
      "drEventNotificationEnabled": 1,
      "context": {
        "serviceId": "",
        "serviceName": "",
        "flowId": "",
        "flowName": "",
        "messagingAPI": "false"
      },
      "userAuditNotificationEnabled": 0,
      "assetLevel": 1,
      "isInboundEventNotificationEnabled": 1,
      "dataIntegrationid": 50297
    }
  ],
  "thread": "{\"updated_on\":\"2025-09-05T10:55:32.433Z\",\"created_on\":\"2025-07-29T08:49:56.513Z\",\"id\":\"4419bb31-1332-494a-9d2e-f018f5c8efa8\",\"title\":\"test\",\"type\":\"Conversation\",\"unread_msg_count\":0,\"status\":\"Active\"}",
  "type": "typingStart",
  "message": "",
  "event_identifier": "MO",
  "userId": "974090",
  "tid": "c7fa78a5-XXXX-XXXX-9350-c1324c00a00c",
  "thread_title": "test",
  "clientUUID": "0a4a1900-XXXX-XXXX-b9f9-5ef0927d6683",
  "x-wx-gtrid": "18c4e233-19e6-XXXX-9222-20412dcffbf2",
  "thread_id": "4419bb31-1332-XXXX-XXXX-f018f5c8efa8",
  "channel_identifier": "RTM",
  "appId": "NA1XXXX011",
  "tenantId": 3XX8,
  "event": "TypingIndicator",
  "ts": "2025-09-10T11:04:28.560Z"
} 
```
```json Typing Stop
{
  "clientId": "NA18140011/XXXX/V2_41d0f523288c4591",
  "transid": "c7fa78a5-0fd8-XXXX-9350-c1324c00a00c",
  "channel": "Rtm",
  "extras": "",
  "dataIntegration": [
    {
      "prebuiltId": 12345,
      "outBoundEventNotificationEnabled": 1,
      "drEventNotificationEnabled": 1,
      "context": {
        "serviceId": "",
        "serviceName": "",
        "flowId": "",
        "flowName": "",
        "messagingAPI": "false"
      },
      "userAuditNotificationEnabled": 0,
      "assetLevel": 1,
      "isInboundEventNotificationEnabled": 1,
      "dataIntegrationid": 50297
    }
  ],
  "thread": "{\"updated_on\":\"2025-09-05T10:55:32.433Z\",\"created_on\":\"2025-07-29T08:49:56.513Z\",\"id\":\"4419bb31-1332-494a-9d2e-f018f5c8efa8\",\"title\":\"test\",\"type\":\"Conversation\",\"unread_msg_count\":0,\"status\":\"Active\"}",
  "type": "typingStop",
  "message": "",
  "event_identifier": "MO",
  "userId": "97XX90",
  "tid": "c7fa78a5-0fd8-XXXX-9350-c1324c00a00c",
  "thread_title": "test",
  "clientUUID": "0a4a1900-98ef-XXXX-b9f9-5ef0927d6683",
  "x-wx-gtrid": "18c4e233-19e6-XXXX-9222-20412dcffbf2",
  "thread_id": "4419bb31-1332-XXXX-9d2e-f018f5c8efa8",
  "channel_identifier": "RTM",
  "appId": "NA1XXXX011",
  "tenantId": 3678,
  "event": "TypingIndicator",
  "ts": "2025-09-10T11:04:28.560Z"
} 
```

**Live Chat / In-App - Inbound Message Descriptions **

The following table contains the parameter descriptions of inbound messages.

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Descriptions",
    "h-2": "Example",
    "h-3": "Event Type",
    "0-0": "attachments",
    "0-1": "In-App attachment details",
    "0-2": "[{\\\"file\\\":\\\"https://stagingrtmedia.s3.amazonaws.com/ne05064134/97407654974538.doc\\\",\\\"size\\\":98304,\\\"id\\\":\\\"97407654974538\\\",\\\"contentType\\\":\\\"file\\\"}]",
    "0-3": "",
    "1-0": "clientId",
    "1-1": "Unique identification  number of the client.",
    "1-2": "POXXXX3801/3XX2/v2_fc50XXXXXXXXXX5a",
    "1-3": "",
    "2-0": "transid",
    "2-1": "Contains the transaction ID.",
    "2-2": "d94ba95c-xxxx-4c4e-xxxx-7851028415f4",
    "2-3": "",
    "3-0": "channel",
    "3-1": "This is “rt” in case of Live Chat and In-App Messaging.",
    "3-2": "RTM",
    "3-3": "Common parameter for all inbound event types.",
    "4-0": "extras",
    "4-1": "Contains the additional information like some user-specific property, or any custom parameter that is required to display the message in a certain fashion within the app",
    "4-2": "{       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n}",
    "4-3": "",
    "5-0": "dataIntegration",
    "5-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "5-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "5-3": "",
    "6-0": "context",
    "6-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "6-2": "\"context\": {   \n                     \"key1\": \"value1\",  \n                     \"key2\": \"value2\",  \n                     \"key3\": \"value3\"     \n}",
    "6-3": "Common parameter for all inbound event types.",
    "7-0": "serviceId",
    "7-1": "Contains the unique reference id of the service.",
    "7-2": "12345",
    "7-3": "Common parameter for all inbound event types.",
    "8-0": "serviceName",
    "8-1": "Contains the name of the service.",
    "8-2": "My New Service",
    "8-3": "Common parameter for all inbound event types.",
    "9-0": "flowId",
    "9-1": "Contains the unique ID for the flow.",
    "9-2": "54321",
    "9-3": "Common parameter for all inbound event types.",
    "10-0": "flowName",
    "10-1": "Contains the name of the flow.",
    "10-2": "Sample Flow",
    "10-3": "Common parameter for all inbound event types.",
    "11-0": "messagingAPI",
    "11-1": "Indicates whether the request is sent through messaging API",
    "11-2": "true/false",
    "11-3": "Common parameter for all delivery receipts.",
    "12-0": "appContext",
    "12-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "12-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "12-3": "Common parameter for all inbound event types.",
    "13-0": "thread",
    "13-1": "",
    "13-2": "",
    "13-3": "",
    "14-0": "message",
    "14-1": "Contains the text message sent by the user.",
    "14-2": "Hi this is a LiveChat message",
    "14-3": "",
    "15-0": "userId",
    "15-1": "Unique identification  number of the user.",
    "15-2": "12345",
    "15-3": "Common parameter for all inbound event types.",
    "16-0": "tid",
    "16-1": "Contains the transaction id.",
    "16-2": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
    "16-3": "Common parameter for all inbound event types.",
    "17-0": "thread_title",
    "17-1": "",
    "17-2": "",
    "17-3": "",
    "18-0": "client_UUID",
    "18-1": "",
    "18-2": "",
    "18-3": "",
    "19-0": "x-wx-gtrid",
    "19-1": "Contains the global transaction ID between cross-products for a given request.",
    "19-2": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
    "19-3": "Message and Attachments ",
    "20-0": "thread_id",
    "20-1": "The unique identification of the thread in which the message needs to be published.",
    "20-2": "\"fd321782-xxxx-4107-xxxx-ebfc473f9e0a\"",
    "20-3": "",
    "21-0": "appid",
    "21-1": "Contains the application ID.",
    "21-2": "a_63XXXXXXXXXXXXX000",
    "21-3": "Common parameter for all inbound event types.",
    "22-0": "reply_To",
    "22-1": "Contains the details of the user to whom the message is being sent.",
    "22-2": "User1",
    "22-3": "Message, Attachments and Postback",
    "23-0": "event",
    "23-1": "Contains the incoming event type.",
    "23-2": "Incoming Message  \nOnPostback  \nOnThreadClosed  \nCustom",
    "23-3": "",
    "24-0": "ts",
    "24-1": "Timestamp when MO received to <<prodname>>.",
    "24-2": "2022-01-17T10:59:51.945Z",
    "24-3": "Common parameter for all inbound event types.",
    "25-0": "datetime",
    "25-1": "Data and Time on which the message is received.",
    "25-2": "2020-02-25T12:40:45.051+05:30",
    "25-3": "Postback, OnThread Closed, and Custom Event",
    "26-0": "pciInfo",
    "26-1": "Contains the PCI information of the user.",
    "26-2": "droppedAttachmentCount",
    "26-3": "",
    "27-0": "deviceId",
    "27-1": "Unique identification  number of the device.",
    "27-2": "fc5XXXXXXXXX25a",
    "27-3": "",
    "28-0": "version",
    "28-1": "Version of the In-App REST API used for sending messages.",
    "28-2": "1",
    "28-3": "",
    "29-0": "Name",
    "29-1": "Contains the name of the user.",
    "29-2": "Tom",
    "29-3": "",
    "30-0": "status",
    "30-1": "Contains the status of the flow.",
    "30-2": "Closed",
    "30-3": "",
    "31-0": "title",
    "31-1": "Contains the title name",
    "31-2": "Buy Now",
    "31-3": ""
  },
  "cols": 4,
  "rows": 32,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Live Chat / In-App - Delivery Receipt**

The following are the Live Chat / In-App delivery receipts payloads.

```json Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-01-17T16:08:10.787+05:30",
      "pushId": "dummy_data",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "rt",
      "destination": "dummy_data",
      "destinationType": "customerid",
      "deviceid": "",
      "deliveryStatus": "Submitted"
    },
    "subtid": "dummy_data",
    "transid": "dummy_data",
    "callbackData": "",
    "correlationid": ""
  },
    "dataIntegration": {
      "context": {
        "Key": "Value",
        "Key2": "Value2"
      },
      "appContext": {
        "adminKey": "",
        "tenant_identifier": "dummyTenant"
      }
    }
  }
}
```
```json Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-01-17T16:08:10.896+05:30",
      "pushId": "",
      "Description": "Delivered",
      "code": "7500",
      "deliveryChannel": "rt",
      "destination": "dummy_data",
      "destinationType": "customerid",
      "deviceid": "dummy_data",
      "deliveryStatus": "Delivered"
    },
    "subtid": "dummy_data",
    "transid": "dummy_data",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "dataIntegration": {
      "context": {
        "Key": "Value",
        "Key2": "Value2"
      },
      "appContext": {
        "adminKey": "",
        "tenant_identifier": "dummyTenant"
      }
    }
  }
}
```
```json Read
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-01-17T16:08:10.927+05:30",
      "pushId": "",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "rt",
      "destination": "dummy_data",
      "destinationType": "customerid",
      "deviceid": "dummy_data",
      "deliveryStatus": "Read"
    },
    "subtid": "dummy_data",
    "transid": "dummy_data",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "dataIntegration": {
      "context": {
        "Key": "Value",
        "Key2": "Value2"
      },
      "appContext": {
        "adminKey": "",
        "tenant_identifier": "dummyTenant"
      }
    }
  }
}
```

**Live Chat / In-App - Delivery Receipt Descriptions **

The following table contains the parameter descriptions of delivery receipts.

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "h-2": "Example",
    "h-3": "Message Type",
    "0-0": "x-wx-gtrid",
    "0-1": "Contains the global transaction ID between cross-products for a given request.",
    "0-2": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
    "0-3": "Common parameter for all delivery receipts.",
    "1-0": "deliveryInfoNotification",
    "1-1": "System variable",
    "1-2": "N/A",
    "1-3": "Common parameter for all delivery receipts.",
    "2-0": "deliveryInfo",
    "2-1": "System variable",
    "2-2": "N/A",
    "2-3": "Common parameter for all delivery receipts.",
    "3-0": "timeStamp",
    "3-1": "Timestamp of the event",
    "3-2": "2024-03-04T16:08:52.860+05:30",
    "3-3": "Common parameter for all delivery receipts.",
    "4-0": "Description",
    "4-1": "Detailed description of the delivery status.",
    "4-2": "Message length exceeded",
    "4-3": "Common parameter for all delivery receipts.",
    "5-0": "code",
    "5-1": "Status code as mentioned in the documentation",
    "5-2": "7107",
    "5-3": "Common parameter for all delivery receipts.",
    "6-0": "deliveryChannel",
    "6-1": "Channel to be used to send message",
    "6-2": "In-App",
    "6-3": "Common parameter for all delivery receipts.",
    "7-0": "additionalinfo",
    "7-1": "Additional info such as details about the browser used to open a link in case of Click events.",
    "7-2": "",
    "7-3": "Common parameter for all delivery receipts.",
    "8-0": "destination",
    "8-1": "The mobile number to which message will be sent.",
    "8-2": "174XXXX6048",
    "8-3": "Common parameter for all delivery receipts.",
    "9-0": "destinationType",
    "9-1": "This is always msisdn for In-App.",
    "9-2": "customerid",
    "9-3": "Common parameter for all delivery receipts.",
    "10-0": "deliveryStatus",
    "10-1": "Status of messages once sent",
    "10-2": "Submitted",
    "10-3": "Common parameter for all delivery receipts.",
    "11-0": "subtid",
    "11-1": "A unique transaction id will be generated as subtid for the flow level transactions(or node tid).",
    "11-2": "27XXXX95-dXXb-4XXc-8XXc-61XXXXXXX8fa",
    "11-3": "Common parameter for all delivery receipts.",
    "12-0": "transid",
    "12-1": "Unique transaction reference id of the request.",
    "12-2": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
    "12-3": "Common parameter for all delivery receipts.",
    "13-0": "callbackData",
    "13-1": "Data that you have configured to receive on the notify Url. This is configured as a part of the request",
    "13-2": "CallBackdata",
    "13-3": "Common parameter for all delivery receipts.",
    "14-0": "correlationid",
    "14-1": "The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
    "14-2": "InAppMTusingmsisdn",
    "14-3": "Common parameter for all delivery receipts.",
    "15-0": "dataIntegration",
    "15-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "15-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "15-3": "Common parameter for all delivery receipts.",
    "16-0": "context",
    "16-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "16-2": "\"context\": {   \n                     \"key1\": \"value1\",  \n                     \"key2\": \"value2\",  \n                     \"key3\": \"value3\"     \n}",
    "16-3": "Common parameter for all delivery receipts.",
    "17-0": "serviceId",
    "17-1": "Contains the unique reference id of the service.",
    "17-2": "12345",
    "17-3": "Common parameter for all delivery receipts.",
    "18-0": "serviceName",
    "18-1": "Contains the name of the service.",
    "18-2": "My New Service",
    "18-3": "Common parameter for all delivery receipts.",
    "19-0": "flowId",
    "19-1": "Contains the unique ID for the flow.",
    "19-2": "54321",
    "19-3": "Common parameter for all delivery receipts.",
    "20-0": "flowName",
    "20-1": "Contains the name of the flow.",
    "20-2": "Sample Flow",
    "20-3": "Common parameter for all delivery receipts.",
    "21-0": "messagingAPI",
    "21-1": "Indicates whether the request is sent through messaging API",
    "21-2": "true/false",
    "21-3": "Common parameter for all delivery receipts.",
    "22-0": "appContext",
    "22-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "22-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "22-3": "Common parameter for all delivery receipts."
  },
  "cols": 4,
  "rows": 23,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Live Chat / In-App - Outbound Message**

The following are the Live Chat / In-App outbound message payloads.

```json Text
{
  "transid": "1cXXXXcd-7XX0-4XX2-9XX7-24XXXXXXXXa4",
  "channel": "RT",
  "extras": {
    
  },
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Data Stream Send Node",
      "serviceId": "12345",
      "serviceName": "My New Service",
      "flowId": "54321",
      "flowName": "Sample Flow",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "priority": 5,
  "message": "Send Node flow executed 01-04-2024",
  "userId": "2XX0",
  "tid": "1cXXXXcd-7XX0-4XX2-9XX7-249XXXXXXXXa4",
  "threadid": "b5XXXX01-c2ee-4XXc-aXX0-01XXXXXXXX0b",
  "clientUUID": "0aXXXX00-98ef-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "7aXXXXa6-bXX5-6XX0-aXX8-bcXXXXXXXX6f",
  "appId": "NEXXXXXX34",
  "x_msg_seq": 0,
  "serviceKey": "27XXXX75-eXX3-1XXe-aXX0-02XXXXXXXXd5"
}
```
```json File
{
"channel": "RT",
  "extras": {
    
  },
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Send Node with file",
      "serviceId": "12345",
      "serviceName": "Inapp_First",
      "flowId": "54321",
      "flowName": "DS2",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "priority": 5,
  "message": "Send Node with file",
  "userId": "2XX0",
  "tid": "1cXXXXcd-7XX0-4XX2-9XX7-249XXXXXXXXa4",
  "threadid": "b5XXXX01-c2ee-4XXc-aXX0-01XXXXXXXX0b",
  "clientUUID": "0aXXXX00-98ef-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "7aXXXXa6-bXX5-6XX0-aXX8-bcXXXXXXXX6f",
  "attachment": [
    {
      "preview": "https://sample-videos.com/img/Sample-jpg-image-50kb.jpg",
      "file": "https://sample-videos.com/img/Sample-jpg-image-50kb.jpg",
      "contentType": "image/jpg"
    }
  ],
  "appId": "NEXXXXXX34",
  "x_msg_seq": 0,
  "serviceKey": "27XXXX75-eXX3-1XXe-aXX0-02XXXXXXXXd5"
}
```
```json Postback
{
  "transid": "a3XXXX3c-5XX0-4XXe-aXXd-edXXXXXXXX12",
  "channel": "RT",
  "extras": {
    
  },
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "Check": "Post Back Send Node",
      "serviceId": "12345",
      "serviceName": "InappR_First",
      "flowId": "54321",
      "flowName": "DS3",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "priority": 5,
  "message": "Generic template",
  "userId": "2XX0",
  "tid": "1cXXXXcd-7XX0-4XX2-9XX7-249XXXXXXXXa4",
  "threadid": "b5XXXX01-c2ee-4XXc-aXX0-01XXXXXXXX0b",
  "clientUUID": "0aXXXX00-98ef-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "7aXXXXa6-bXX5-6XX0-aXX8-bcXXXXXXXX6f",
  "attachment": [
    {
      "templateType": "generic",
      "payload": {
        "reference": "Consent",
        "elements": [
          {
            "buttons": [
              {
                "identifier": "12124",
                "payload": "",
                "type": "templatePostback",
                "title": "Buy Now",
                "url": ""
              }
            ],
            "subtitle": "Subtitle",
            "imageUrls": [
              "https://www.fnordware.com/superpng/pnggrad16rgb.png"
            ],
            "title": "product"
          }
        ]
      },
      "contentType": "template"
    }
  ],
  "appId": "NEXXXXXX34",
  "x_msg_seq": 0,
  "serviceKey": "27XXXX75-eXX3-1XXe-aXX0-02XXXXXXXXd5"
}
```
```json Quick Replies
{
  "quickReplies": {
    "reference": "Consent",
    "options": [
      {
        "identifier": "12321",
        "payload": "",
        "imageUrl": "https://www.fnordware.com/superpng/pnggrad16rgb.png",
        "type": "quickReplyPostback",
        "title": "Yes"
      }
    ]
  },
  "transid": "2eXXXX09-1XX1-4XX9-9XX7-93XXXXXXXX25",
  "channel": "RT",
  "extras": {
    
  },
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Send Node Quick Reply",
      "serviceId": "12345",
      "serviceName": "Inapp_First",
      "flowId": "54321",
      "flowName": "DS3",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "priority": 5,
  "message": "Quick reply Post back",
  "userId": "2XX0",
  "tid": "1cXXXXcd-7XX0-4XX2-9XX7-249XXXXXXXXa4",
  "threadid": "b5XXXX01-c2ee-4XXc-aXX0-01XXXXXXXX0b",
  "clientUUID": "0aXXXX00-98ef-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "7aXXXXa6-bXX5-6XX0-aXX8-bcXXXXXXXX6f",
  "appId": "NEXXXXXX34",
  "x_msg_seq": 0,
  "serviceKey": "27XXXX75-eXX3-1XXe-aXX0-02XXXXXXXXd5"
}
```
```json Form  Message
{
  "transid": "2eXXXX09-1XX1-4XX9-9XX7-93XXXXXXXX25",
  "channel": "RT",
  "extras": {
    
  },
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "DS send node form",
      "serviceId": "12345",
      "serviceName": "Inapp_First",
      "flowId": "54321",
      "flowName": "DSFlow",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "priority": 1,
  "userId": "2XX0",
  "tid": "1cXXXXcd-7XX0-4XX2-9XX7-249XXXXXXXXa4",
  "threadid": "b5XXXX01-c2ee-4XXc-aXX0-01XXXXXXXX0b",
  "clientUUID": "0aXXXX00-98ef-4XX5-bXX9-5eXXXXXXXX83",
  "x-wx-gtrid": "7aXXXXa6-bXX5-6XX0-aXX8-bcXXXXXXXX6f",
  "attachment": [
    {
      "templateType": "form",
      "payload": {
        "fields": [
          {
            "name": "Name",
            "description": "enter name",
            "label": "Name",
            "type": "text",
            "mandatory": false
          },
          {
            "name": "Email",
            "description": "email",
            "label": "Email",
            "type": "email",
            "mandatory": false
          },
          {
            "name": "Gender",
            "options": [
              "Male",
              "Female"
            ],
            "description": "",
            "label": "Gender",
            "type": "dropdown",
            "mandatory": false
          }
        ],
        "title": "Student Form"
      },
      "templateId": "0W1XPWN2ND",
      "contentType": "template"
    }
  ],
  "appId": "NEXXXXXX34",
  "x_msg_seq": 0,
  "serviceKey": "27XXXX75-eXX3-1XXe-aXX0-02XXXXXXXXd5"

```

**Live Chat / In-App - Outbound Message Descriptions**

The following table contains the parameter descriptions of outbound messages.

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Descriptions",
    "h-2": "Example",
    "h-3": "Event Type",
    "0-0": "transid",
    "0-1": "Unique transaction reference id of the request.",
    "0-2": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
    "0-3": "Text, File, Postback, and Form Response",
    "1-0": "channel",
    "1-1": "This is “rt” in case of Live Chat and In-App Messaging.",
    "1-2": "RTM",
    "1-3": "Common parameter for all outbound message types.",
    "2-0": "extras",
    "2-1": "Contains the additional information like some user-specific property, or any custom parameter that is required to display the message in a certain fashion within the app",
    "2-2": "{       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n}",
    "2-3": "Common parameter for all outbound message types.",
    "3-0": "validateDestination",
    "3-1": "System Variable",
    "3-2": "true/false",
    "3-3": "Common parameter for all outbound message types.",
    "4-0": "dataIntegration",
    "4-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "4-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "4-3": "Common parameter for all outbound message types.",
    "5-0": "context",
    "5-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "5-2": "\"context\": {   \n                     \"key1\": \"value1\",  \n                     \"key2\": \"value2\",  \n                     \"key3\": \"value3\"     \n}",
    "5-3": "Common parameter for all outbound message types.",
    "6-0": "serviceId",
    "6-1": "Contains the unique reference id of the service.",
    "6-2": "12345",
    "6-3": "Common parameter for all outbound message types.",
    "7-0": "serviceName",
    "7-1": "Contains the name of the service.",
    "7-2": "My New Service",
    "7-3": "Common parameter for all outbound message types.",
    "8-0": "flowId",
    "8-1": "Contains the unique ID for the flow.",
    "8-2": "54321",
    "8-3": "Common parameter for all outbound message types.",
    "9-0": "flowName",
    "9-1": "Contains the name of the flow.",
    "9-2": "Sample Flow",
    "9-3": "Common parameter for all outbound message types.",
    "10-0": "messagingAPI",
    "10-1": "Indicates whether the request is sent through messaging API.",
    "10-2": "true/false",
    "10-3": "Common parameter for all outbound message types.",
    "11-0": "appContext",
    "11-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "11-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "11-3": "Common parameter for all outbound message types.",
    "12-0": "priority",
    "12-1": "This parameter is used to specify the message priority.",
    "12-2": "1",
    "12-3": "Common parameter for all outbound message types.",
    "13-0": "message",
    "13-1": "Contains the text message sent by the user.",
    "13-2": "Hi this is a LiveChat message",
    "13-3": "Common parameter for all outbound message types.",
    "14-0": "userId",
    "14-1": "Unique identification number of the user.",
    "14-2": "2480",
    "14-3": "Common parameter for all outbound message types.",
    "15-0": "tid",
    "15-1": "Transaction ID",
    "15-2": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
    "15-3": "Common parameter for all outbound message types.",
    "16-0": "threadid",
    "16-1": "Unique identification number of the thread.",
    "16-2": "12eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXX13",
    "16-3": "Common parameter for all outbound message types.",
    "17-0": "clientUUID",
    "17-1": "Contains the clients unique identification number.",
    "17-2": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
    "17-3": "Common parameter for all outbound message types.",
    "18-0": "x-wx-gtrid",
    "18-1": "Contains the global transaction ID between cross-products for a given request.",
    "18-2": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
    "18-3": "Common parameter for all outbound message types.",
    "19-0": "appId",
    "19-1": "Contains the application ID",
    "19-2": "a_63XXXXXXXXXXXXX000",
    "19-3": "Common parameter for all outbound message types.",
    "20-0": "x_msg_seq",
    "20-1": "This parameter represents whether the request should process sequence or not.",
    "20-2": "0",
    "20-3": "Common parameter for all outbound message types.",
    "21-0": "serviceKey",
    "21-1": "Unique identification number for the service.",
    "21-2": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d",
    "21-3": "Common parameter for all outbound message types.",
    "22-0": "templateType",
    "22-1": "Contains the information about the template type.  \nGeneric or Form",
    "22-2": "\"templateType\": \"form\",  \n  \n\"templateType\": \"generic\",",
    "22-3": "",
    "23-0": "payload",
    "23-1": "Contains the information about the payload.",
    "23-2": "payload\": { \"reference\": \"T-shirt options\", \"elements\": \\[ //Maximum of 8 elements can be added. { \"title\": \"Classic White T-Shirt\", \"subtitle\": \"Clothing\", \"imageUrls\": [ //Maximum of 5 images can be added. \"https://e7.pngegg.com/pngimages/464/597/png-clipart-logo-cisco-systems-router-network-switch-packet-tracer-logo-hmi-emblem-text-thumbnail.png\" ], \"buttons\": \\[ //Maximum of 3 buttons can be added. { \"type\": \"webUrl\", \"identifier\": \"21221-323232-231212\", \"url\": \"<https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png\">, \"title\": \"View Item\", \"payload\": {} }",
    "23-3": "",
    "24-0": "type",
    "24-1": "Defines the type of the button. In case of a quick reply, it should be quickReplyPostback.",
    "24-2": "quickReplyPostback",
    "24-3": "Quick Reply",
    "25-0": "title",
    "25-1": "Specifies the bubble title.",
    "25-2": "Student Form",
    "25-3": "Form Response "
  },
  "cols": 4,
  "rows": 26,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]