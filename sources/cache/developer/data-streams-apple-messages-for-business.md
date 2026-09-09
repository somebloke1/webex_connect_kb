# Data Streams - Apple Messages for Business

Source: https://developers.webexconnect.io/reference/data-streams-apple-messages-for-business
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:49+00:00

**Apple Messages for Business - Inbound Message**

The following are the Apple Messages for Business inbound message payloads.

```json Invitation Response
{
  "abcUserId": "urn:mbid:AQAAY+DpsEOs4wkistDRF80rdtsT9hNu/3iQpHFkpep5b5sKRWOHzHCHW0YS5JXiPGy64qaVuBUckNu0B4jzKJwOV5zHC4ybjx6pOZ4tpLlMYCd/DLyUI4GxHRMbmv25gpJ8KVpaOufbKlqwaNZ35n2tPZaqviM=",
  "channel": "AppleBusinessChat",
  "abcAccountId": "59a5c4a6-ad9a-4ead-904a-c0ad04ae67ee",
  "dataIntegration": {
    "context": {
      "serviceId": "12345",
      "serviceName": "My New Service",
      "flowId": "54321",
      "flowName": "Sample Flow",
      "messagingAPI": "false"
    },
    "appContext": {}
  },
  "appId": "a_638899722384450000",
  "event": "InvitationResponse",
  "ts": "2026-06-11T13:03:25.668+05:30",
  "tid": "98ad3ea0-918f-f2e4-8e9e-1f92bc37fa36",
  "msisdn": "+91807663XXXX",
  "requestIdentifier": "tel:+91807663XXXX",
  "invitationAccepted": "true",
  "invitationResponse": "{\"notification\":{\"displayContent\":{\"determinateResponse\":{\"subtitle\":\"You are now connected with WebExConnect.\",\"type\":{\"yes\":{}},\"title\":\"Yes\"}},\"id\":\"yes\"},\"requestIdentifier\":\"tel:+91807663XXXX\",\"version\":\"1\",\"referenceId\":\"{ caseNumber : cb2eadcc-9d46-435e-b319-47a4efc07a61 }\"}",
  "locale": "en_IN",
  "bizGroupId": "",
  "bizIntentId": "",
  "timestamp": "",
  "capabilities": "",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Text
{
  "attachments": "",
  "capabilities": "",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "serviceId": “12345”,
      "serviceName": "My New Service",
      "flowId": “54321”,
      "flowName": “Sample Flow",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "bizIntentId": "",
  "type": "text",
  "message": "AMB start node Data stream checks ",
  "locale": "en_IN",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": "urn:mbidTc=",
  "datetime": "2024-03-28T21:21:03.763+05:30",
  "bizGroupId": "",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "requestIdentifier": "",
  "event": "MO",
  "ts": "2024-03-28T21:21:03.763+05:30",
  "timestamp": "2024-03-28T15:51:03.763Z"
}
```
```json List Picker
{
  "attachments": "[{\"size\":\"27654\",\"name\":\"ms-6BPndN.jpeg\",\"mimeType\":\"image/jpeg\",\"type\":\"image\",\"url\":\"https://s3.amazonaws.com/stagingappleattachment/db132fd4-89d6-4a5b-ac72-bbba5b6ae4a5.jpeg\"}]",
  "capabilities": "",
  "timezone": "",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "datePicker": "",
  "dataIntegration": {
    "context": {
      "check": "Data stream LP/TP start node",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMB_ListpickerResponseMultipleUser",
      "messagingAPI": "false"
    },
    "appContext": {
    }
  },
  "bizIntentId": "",
  "type": "text",
  "message": " ",
  "locale": "en_IN",
  "listPicker": "",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": "Dummy Data",
  "datetime": "2024-03-28T21:21:03.763+05:30",
  "bizGroupId": "",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "requestIdentifier": "",
  "event": "InteractiveResponse",
  "ts": "2024-03-28T21:21:03.763+05:30",
  "timestamp": "2024-03-28T15:51:03.763Z"
}
```
```json Time Picker
{
  "attachments": "",
  "capabilities": "",
  "timezone": "",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "datePicker": "",
  "dataIntegration": {
    "context": {
      "check": "Data stream LP/TP start node",
      "serviceId": "32763",
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “12345”,
      "flowName": "AMB_TimepickerResponseMultipleUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "bizIntentId": "",
  "type": "time_picker_response",
  "message": "",
  "locale": "en_IN",
  "listPicker": "",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": “Dummy Data”,
  "datetime": "2024-03-28T22:00:40.004+05:30",
  "bizGroupId": "",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX26",
  "requestIdentifier": "21XXXXc4-3XXc-bXX5-4XX1-36XXXXXXXXd21",
  "event": "INTERACTIVERESPONSE",
  "ts": "2024-03-28T22:00:40.004+05:30"
}
```
```json Classical Authentication
{
  "capabilities": "",
  "authenticateStatus": "",
  "timezone": "",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "send node1": "send node1 value",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBClassicalAuth",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "classical_auth_response",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": “Dummy Data“,
  "abcUserId": "Dummy Data",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "authenticateToken": "",
  "requestIdentifier": "21XXXXc4-3XXc-bXX5-4XX1-36XXXXXXXXd21",
  "event": "AuthenticationResponse",
  "ts": "2024-04-26T12:30:20.234+05:30"
}
```
```json New Authentication
{
  "authenticateStatus": "success",
  "timezone": "2024-04-01T16:07:33.485Z",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "check": "DS start node Auth",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBAuthentcation",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "new_auth_response",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
 "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data,
  "datetime": "2024-04-01T21:37:33.485+05:30",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260", 
  "authenticateToken": "AQWLx",
  "requestIdentifier": "21XXXXc4-3XXc-bXX5-4XX1-36XXXXXXXXd21",
  "event": "NewAuthenticationResponse",
  "ts": "2024-04-01T21:37:33.485+05:30"
}
```
```json Quick Reply
{
  "capabilities": "",
  "timezone": "",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "check": "Data stream check in start node AMB  QR",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMB_QRResponseMultipleUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "bizIntentId": "",
  "type": "interactive",
  "locale": "en_IN",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
 "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "datetime": "2024-04-01T14:58:57.070+05:30",
  "bizGroupId": "",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "requestIdentifier": "21XXXXc4-3XXc-bXX5-4XX1-36XXXXXXXXd21",
  "quickreplies": "",
  "event": "QuickReplyResponse",
  "ts": "2024-04-01T14:58:57.070+05:30"
}

```
```json Form Reponse
{
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "check": "AMB Form Response Start node",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBFormResponseMultipleUsers",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "form_response",
  "locale": "en_IN",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
 "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "datetime": "2024-04-01T16:05:03.001+05:30",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "requestIdentifier": "21XXXXc4-3XXc-bXX5-4XX1-36XXXXXXXXd21",
  "event": "FormResponse",
  "ts": "2024-04-01T16:05:03.001+05:30",
  "formResponse": ""
}
```
```json iMessage
{
  "attachments": "",
  "timezone": "2024-04-01T15:24:50.581Z",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "check": "Data stream Start node iMessage",
      "serviceId": “12345,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBiMessageResponseMultiUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "imessage_app_response",
  "tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data,
  "datetime": "2024-04-01T20:54:50.581+05:30",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "event": "iMessageAppResponse",
  "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:XB45D9TT4D:com.imimobile.fcmconnect.MessagesExtension",
  "ts": "2024-04-01T20:54:50.581+05:30"
}

```
```json Typing Indicator
{
  "capabilities": "",
  "timezone": "2024-04-25T18:52:33.947Z",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "send node1": "send node1 value",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “5”4321,
      "flowName": "AMBTyping",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "typing_start",
  ""tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data,
  "datetime": "2024-04-26T00:22:33.947+05:30",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "requestIdentifier": "",
  "event": "TYPINGINDICATOR",
  "ts": "2024-04-26T00:22:33.947+05:30"
}

```
```json Conversation Closed
{
  "capabilities": "",
  "timezone": "2024-04-25T19:04:03.770Z",
  "channel": "AppleBusinessChat",
  "abcAccountId": "93XXXX0b-0XX0-4XXb-aXXd-37fXXXXXXX4d",
  "dataIntegration": {
    "context": {
      "send node1": "send node1 value",
      "serviceId": “12345”,
      "serviceName": "AMB650_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBConvClosed",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "close",
  ""tid": "234XXXXX-dXXX-4XXX-9XXX-c4bXXXXXXX20",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data,
  "datetime": "2024-04-26T00:22:33.947+05:30",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2",
  "appId": "a_15984XXXXXXXXXX260",
  "requestIdentifier": "",
  "event": "CONVERSATIONCLOSED",
  "ts": "2024-04-26T00:34:03.770+05:30"
}

```

The following table contains the parameter descriptions of Inbound Events.



| Field Name | Descriptions | Example | Message Type |
| --- | --- | --- | --- |
| attachments | Contains the attachment sent by the user | [www.webexconnect.com](http://www.webexconnect.com) | Text with attachments, List Picker, Time Picker, iMessage |
| capabilities | This field has been deprecated by Apple Messages for Business in March 2022 and no longer contains any value. Refer to capabilityList field instead. | NA | Text, List Picker, Time Picker, Classical Authentication, Quick Reply, Conversation Closed |
| channel | Name of the channel. | Apple Business Chat | Common parameter for all inbound event types. |
| abcAccountId | Contains the unique Apple Messages for Business account ID. | 31XXXX96-fXXe-4XX4  <br>-aXX8-a6XXXXXXXXca | Common parameter for all inbound event types. |
| dataIntegration | The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.. | "dataIntegration": {    "context":  <br> {       <br>"key1": "value1",  <br>"key2": "value2",  <br>"key3": "value3"     <br>},  <br>“appContext”: {  <br>}  <br>} | Common parameter for all inbound event types. |
| context | The object contains  key-value pairs which are added either by Data Stream admin or in flow. | "context": {   <br>                     "key1": "value1",  <br>                     "key2": "value2",  <br>                     "key3": "value3"     <br>} | Common parameter for all inbound event types. |
| serviceId | Contains the unique reference id of the service. | 12345 | Common parameter for all inbound event types. |
| serviceName | Contains the name of the service. | My New Service | Common parameter for all inbound event types. |
| flowId | Contains the unique ID for the flow. | 54321 | Common parameter for all inbound event types. |
| flowName | Contains the name of the flow. | Sample Flow | Common parameter for all inbound event types. |
| messagingAPI | It is a boolean parameter. If the value is True, the message was sent using messaging API. If the value is False, the message was sent using either flow or rule. | true/false | Common parameter for all inbound event types. |
| appContext | The object is added as key-value pair either by Data Stream admin or in flow. | “appContext“: {  <br>                           “key1”: “value1“,  <br>                          “key2”: “value2“  <br>} | Common parameter for all inbound event types. |
| bizIntentId | The intention, or purpose, of the chat as specified by the business, such as account_question. | account_question | Text, List Picker, Time Picker, and Quick Reply. |
| type | Contains the details of event type. | text | Common parameter for all inbound event types. |
| message | Contains the text message sent by the user. | This is a test message. | Common parameter for all inbound event types. |
| locale | Contains the location-based language setting | en_US | Common parameter for all inbound event types. |
| tid | Transaction ID | 9fXXXX4e-fXXb-dXXb  <br>-3XX0-9eXXXXXXXX4c | Common parameter for all inbound event types. |
| x-wx-gtrid | Contains the global transaction ID between cross-products for a given request. | d7XXXX76-3XXa-4XXe  <br>-9XX3-d6XXXXXXXXf9 | Common parameter for all inbound event types. |
| abcUserId | Contains the unique Apple Messages for Business user ID | urn:mbidTc= | Common parameter for all inbound event types. |
| datetime | Data and Time on which the message is received. | 2020-02-25T12:40:45.051+05:30 | Common parameter for all inbound event types. |
| bizGroupId | Contains the business group ID. | Sales | Text, List Picker, Time Picker, Quick Reply |
| deviceAgent | This field has been deprecated by Apple Messages for Business in March 2022 and no longer contains any value. | NA | Common parameter for all inbound event types. |
| capabilityList | A string list that identifies Messages for Business features supported by the customer’s device. The list items are case insensitive and separated by commas. When a customer sends a message, this field allows you to understand the customer device capabilities to compose an appropriate response for that device. | AUTH%2CLIST%2CTIME  <br>%2CQUICK%2CAUTH2 | Common parameter for all inbound event types. |
| appId | Contains the application ID. | a_63XXXXXXXXXXXXX000 | Common parameter for all inbound event types. |
| requestIdentifier | Applicable for responses to interactive message types such as Quick Replies and Invitation Response. It can be used to correlate the user response to a previously sent interactive message or invitation message. | `fcb5e9ca-0ddc-4a07-bf9b-7fcbd044aeeb` | Quick Reply, List Picker, Time Picker, Classical Authentication, New Authentication, Form Response, and Invitation Response |
| event | Contains the incoming event type. For invitation responses, this value is `InvitationResponse`. | `InvitationResponse` | Common parameter for all inbound event types. |
| ts | Timestamp when MO received to Webex Connect | 2023-03-06T17:21:41.488+05:30 | Common parameter for all inbound event types. |
| timestamp | Timestamp when MO received to connect. This is an old field. This info is now available in the 'ts' field. | 2023-03-06T17:21:41.488+05:30 | Text and List Picker event type. |
| listPicker | Contains the JSON payload of    list picker response as selected by the customer. | "{\"otherItemCount\":0,\"selectedItemCount\":3,  <br>\"selectedItems\":[{\"identifier\":\"0\",\"style\":\"default\",  <br>\"title\":\"iPhone X\",\"order\":\"0\"},]}", | List Picker and Time Picker event type. |
| datePicker | Contains the JSON payload of    time picker response as selected by the customer. | "{\"identifier\":\"fdXXXX99-6XX1-4XX6-aXX8-aeXXXXXXXX9c\",  <br>\"timezoneOffset\":\"-100\",\"location\":{},  <br>\"title\":\"NHS Appointments\",  <br>\"timeslots\":[{\"duration\":\"1800\",\"identifier\":\"3\",  <br>\"startTime\":\"2023-03-22T12:30+0000\"}]}", | List Picker and Time Picker event type. |
| bid | The bundle ID relevant to the message type. For iMessage App extension, it’s the app specific bundle ID. For all the other messages, it’s the default. | "com.apple.messages.MSMessage  <br>ExtensionBalloonPlugin:0000000000:com.  <br>apple.icloud.apps.messages.business.extension" | iMessage event type. |
| type | Contains the details of event type. | text | Common parameter for all inbound event types. |
| quickreplies | Allows the customer with a single tap to make a choice. | "{\"selectedIdentifier\":\"345345\",\"items\":[{\"identifier\":\"2323\",\"title\":\"TestCloudQA\"},{\"identifier\":\"345345\",\"title\":\"No 👎\"}],\"selectedIndex\":1}", | Quick Reply |
| formResponse | Allows the customer to create  interactive flows. | "formResponse": "{\"template\":\"messageForms"}" | Form Response |
| msisdn | Customer mobile number used for the invitation, when available. | `+4477362XXXX` | Invitation Response |
| invitationAccepted | Indicates whether the customer accepted the invitation. | `true` | Invitation Response |
| invitationResponse | Invitation response payload returned as an escaped JSON string. | `{"notification":{"id":"yes"}}` | Invitation Response |
| interactiveData.sessionIdentifier | Apple session identifier received in the invitation response payload, when available. | `de82fd8a-bcb4-3b2c-b14c-f52e63f40940` | Invitation Response |




**Apple Messages for Business - Outbound Message**

The following are the Apple Messages for Business outbound message payloads.

```json Invitation Message
{
  "sourceId": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "type": "invitation",
  "destinationId": "tel:+4477362XXXX",
  "msisdn": "+4477362XXXX",
  "withImage": true,
  "brandName": "Delta",
  "requestIdentifier": "fcb5e9ca-0ddc-4a07-bf9b-7fcbd044aeeb",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "abcUserId": "",
  "v": 1,
  "appId": "a_63XXXXXXXXXXXX0000",
  "ts": "1778584727566"
}
```
```json Text
{
  "sourceId": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "serviceId": “12345”,
      "serviceName": "My New Service",
      "flowId": “54321”,
      "flowName": "Sample Flow",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "text",
  "body": "This is AMB text message -AMBMultipleUsersFix650  -Clientstaging\nhttps://www.apple.com/",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": "urn:mbidTc=",
  "v": 1,
  "sendTypingIndicator": true,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 1,
  "text": "This is AMB text message -AMBMultipleUsersFix650  -Clientstaging\nhttps://www.apple.com/",
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d",
  "ts": "1711641065642"
}
```
```json Text with Attachments
{
  "sourceId": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
  "attachments": [
    {
      "size": 0,
      "mimeType": "image/jpeg",
      "url": "https://s3.amazonaws.com/stagingappleattachment/db322c0b-6c5f-430a-ae65-6373eadb1dd1.jpeg"
    }
  ],
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "serviceId": “12345”,
      "serviceName": "AMB6_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBIncmingMessageEvent",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "text",
  "body": "Text with Attachment DSï¿¼",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "text": "Text with Attachment DS",
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"
}
```
```json Quick Reply
{
  "sourceId": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "interactiveData": {
    "data": {
      "requestIdentifier": "RQR123456",
      "version": "1.0",
      "quick-reply": {
        "summaryText": "This is QR Summary Text",
        "items": [
          {
            "identifier": "OptionA",
            "title": "Confirm"
          },
          {
            "identifier": "Confirm",
            "title": "Cancel"
          }
        ],
        "selectedIndex": 0
      }
    },
    "useLiveLayout": true,
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Data stream check in strat node AMB  QR",
      "serviceId": “12345”,
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBQRResponseMultipleUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
   "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"
}
```
```json List Picker
{
  "sourceId": "db73f591-1e2f-4af9-8ebf-6ba866808caa",
  "transid": "2b865cc5-3c11-47f9-a08e-e266ad49a73f",
  "interactiveData": {
    "receivedMessage": {
      "imageIdentifier": "807b3124-c7d4-67dc-4708-4c9ebda001f5",
      "subtitle": "ReceiveSubtitle_Start",
      "style": "small",
      "title": "ReceiveTitle_Start"
    },
    "data": {
      "images": [
        {
          "identifier": "807b3124-c7d4-67dc-4708-4c9ebda001f5",
          "url": "https://www.gstatic.com/webp/gallery3/1.png"
        },
        {
          "identifier": "d9525ebe-4b9f-258d-e64e-723774fa9cbd",
          "url": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg"
        },
        {
          "identifier": "4956555a-ceac-c77d-2a9a-3e49eecad76a",
          "url": "https://www.lens-rumors.com/wp-content/uploads/2014/10/Nikon-AF-S-DX-Nikkor-18-140mm-f3.5-5.6G-ED-VR-sample-images1.jpg"
        }
      ],
      "requestIdentifier": "Req12121212",
      "version": "1.0",
      "listPicker": {
        "sections": [
          {
            "title": "S1",
            "items": [
              {
                "identifier": "a232323",
                "imageIdentifier": "d9525ebe-4b9f-258d-e64e-723774fa9cbd",
                "subtitle": "I1Subtitle",
                "style": "default",
                "title": "I1",
                "order": 1
              }
            ],
            "multipleSelection": true,
            "order": 1
          },
          {
            "title": "S2",
            "items": [
              {
                "identifier": "b232323",
                "imageIdentifier": "",
                "subtitle": "I2Subtitle",
                "style": "default",
                "title": "I2",
                "order": 1
              }
            ],
            "multipleSelection": true,
            "order": 2
          },
          {
            "title": "S3",
            "items": [
              {
                "identifier": "c232323",
                "imageIdentifier": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
                "subtitle": "I3Subtitle",
                "style": "default",
                "title": "I3",
                "order": 1
              },
              {
                "identifier": "d232323",
                "imageIdentifier": "",
                "subtitle": "I4Subtitle",
                "style": "default",
                "title": "I4",
                "order": 2
              }
            ],
            "multipleSelection": true,
            "order": 3
          }
        ]
      }
    },
    "useLiveLayout": true,
    "replyMessage": {
      "style": "icon",
      "alternateTitle": "ReplySubtitle",
      "title": "ReplyTitle"
    },
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Data stream LP/TP start node",
      "serviceId": “12345”,
      "serviceName": "AMB650_MultipleUsersAsset",
      "flowId": “54321”,
      "flowName": "AMBListpickerResponseMultipleUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"}

```
```json Time Picker
{
  "sourceId": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "interactiveData": {
    "receivedMessage": {
      "imageIdentifier": "132XXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
      "subtitle": "Pickitout",
      "style": "large",
      "title": "SamplePicker"
    },
    "data": {
      "images": [
        {
          "identifier": "132XXX81-2XXe-4XX5-9XXd-36XXXXXXXX3",
          "url": "https://www.gstatic.com/webp/gallery3/1.png"
        }
      ],
      "requestIdentifier": "DP12345",
      "event": {
        "identifier": "Date123",
        "timezoneOffset": 330,
        "location": {
          "latitude": 51.5505,
          "title": "Wembly",
          "radius": 10,
          "longitude": 0.3048
        },
        "title": "BookAppointment",
        "timeslots": [
          {
            "duration": 1800,
            "identifier": "slot123",
            "startTime": "2024-12-28T06:30Z"
          },
          {
            "duration": 3000,
            "identifier": "slot345",
            "startTime": "2024-08-28T16:00Z"
          }
        ]
      },
      "version": "1.0"
    },
    "useLiveLayout": true,
    "replyMessage": {
      "style": "icon",
      "title": "Chosen Date"
    },
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Data stream LP/TP start node",
      "serviceId": "32763",
      "serviceName": "AMB650_MultipleUsersAsset",
      "flowId": "33607",
      "flowName": "AMBListpickerResponseMultipleUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"
}

```
```json Form Response
{
  "sourceId": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "interactiveData": {
    "receivedMessage": {
      "imageIdentifier": "551a9527-e8c1-XXXX-9431-885c7e8615f2",
      "subtitle": "Please fill out the following dispute form",
      "style": "icon",
      "title": "Send node executed with For Response"
    },
    "data": {
      "images": [
        {
          "identifier": "55XXXX81-2XXe-4XX5-9XXd-36XXXXXXXXf2",
          "url": "https://sample-videos.com/img/Sample-png-image-100kb.png"
        }
      ],
      "requestIdentifier": "66dbffd0-7f2b-XXXX-a396-ae533d8a68e7",
      "dynamic": {
        "template": "messageForms",
        "private": false,
        "data": {
          "showSummary": true,
          "pages": [
            {
              "submitForm": false,
              "pageIdentifier": "0",
              "subtitle": "Was the merchandise you received defective or not as the merchant described?",
              "nextPageIdentifier": "1",
              "type": "select",
              "title": "Type of Product",
              "items": [
                {
                  "identifier": "001",
                  "imageIdentifier": "1",
                  "title": "Option 1",
                  "value": "option1"
                },
                {
                  "identifier": "002",
                  "imageIdentifier": "2",
                  "title": "Option 2",
                  "value": "option2"
                }
              ],
              "multipleSelection": true
            },
            {
              "submitForm": false,
              "pageIdentifier": "1",
              "subtitle": "Was the merchandise you received defective or not as the merchant described?",
              "nextPageIdentifier": "2",
              "type": "select",
              "title": "Item Condition",
              "items": [
                {
                  "identifier": "101",
                  "imageIdentifier": "1",
                  "nextPageIdentifier": "2",
                  "title": "Defective",
                  "value": "defective"
                },
                {
                  "identifier": "102",
                  "imageIdentifier": "2",
                  "nextPageIdentifier": "3",
                  "title": "Non defective",
                  "value": "non defective"
                }
              ],
              "multipleSelection": false
            },
            {
              "submitForm": false,
              "pageIdentifier": "2",
              "subtitle": "Do you have any supporting documents that demonstrate that the product quality was not sufficient?",
              "nextPageIdentifier": "3",
              "type": "select",
              "title": "Supporting Documents",
              "items": [
                {
                  "identifier": "201",
                  "imageIdentifier": "1",
                  "nextPageIdentifier": "3",
                  "title": "Yes",
                  "value": "yes"
                },
                {
                  "identifier": "202",
                  "imageIdentifier": "2",
                  "nextPageIdentifier": "3",
                  "title": "No",
                  "value": "no"
                }
              ],
              "multipleSelection": false
            },
            {
              "submitForm": false,
              "pageIdentifier": "3",
              "subtitle": "Select Your Region",
              "nextPageIdentifier": "4",
              "pickerTitle": "Select Your Region",
              "type": "picker",
              "items": [
                {
                  "identifier": "301",
                  "title": "APAC",
                  "value": "apac"
                }              ],
              "multipleSelection": false,
              "selectedItemIndex": "2"
            },
            {
              "submitForm": false,
              "pageIdentifier": "4",
              "subtitle": "What date did you receive, or expect to receive the product?",
              "options": {
                "dateFormat": "MM/dd/yyyy",
                "labelText": "Select Delivery Date",
                "maximumDate": "02/13/2020",
                "minimumDate": "01/01/2020",
                "startDate": "01/12/2020"
              },
              "nextPageIdentifier": "5",
              "type": "datePicker",
              "title": "Delivery Date",
              "multipleSelection": false
            },
            {
              "submitForm": false,
              "pageIdentifier": "5",
              "subtitle": "Please provide details about remaining issue",
              "options": {
                "regex": "",
                "maximumCharacterCount": 10,
                "keyboardType": "UIKeyboardTypeEmailAddress",
                "inputType": "multiline",
                "placeholder": "Please enter issues",
                "required": true
              },
              "nextPageIdentifier": "6",
              "type": "input",
              "title": "Remaining Issues",
              "multipleSelection": false
            },
            {
              "submitForm": true,
              "pageIdentifier": "6",
              "subtitle": "Please provide name of the product",
              "options": {
                "regex": "^d+$",
                "prefixText": "$",
                "maximumCharacterCount": 10,
                "keyboardType": "numberPad",
                "labelText": "Name",
                "inputType": "singleline",
                "placeholder": "Please enter product name",
                "required": false
              },
              "type": "input",
              "title": "Product name",
              "multipleSelection": false
            }
          ],
          "splash": {
            "splashtext": "Kindly answer the following questions to help us dispute this transaction",
            "imageIdentifier": "551a9527-e8c1-XXXX-9431-885c7e8615f1",
            "buttonTitle": "Continue-123",
            "header": "Hello Apple Card-Send Node Kindly answer the following questions"
          },
          "startPageIdentifier": "1"
        }
      },
      "version": "1.0"
    },
    "useLiveLayout": true,
    "replyMessage": {
      "imageIdentifier": "551a9527-e8c1-XXXX-9431-885c7e8615f2",
      "subtitle": "This is Subtitle",
      "style": "small",
      "title": "Tap to view your response."
    },
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "AMB Form Response Start node",
      "serviceId": "32763",
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": "33453",
      "flowName": "AMBFormResponseMultipleUsers",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"
}

```
```json Classical Authentication
{
  "sourceId": "db73f591-1e2f-XXXX-8ebf-6ba866808caa",
  "transid": "2b865cc5-3c11-XXXX-a08e-e266ad49a73f",
  "interactiveData": {
    "receivedMessage": {
      "imageIdentifier": "328cb84e-df8e-XXXX-bddd-8eabc60f8c38",
      "subtitle": "ReceiveMessage_subtitle",
      "title": "ReceiveMessage_Old"
    },
    "data": {
      "images": [
        {
          "identifier": "f1e899bd-9edc-XXXX-ffb7-debda068ad0d",
          "url": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg"
        },
        {
          "identifier": "55XXXX81-2XXe-4XX5-9XXd-36XXXXXXXXf2",
          "url": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg"
        }
      ],
      "authenticate": {
        "error_code": 0,
        "oauth2": {
          "responseType": "code",
          "scope": [
            "r_liteprofile"
          ],
          "state": "eca7edc7-e5aa-XXXX-a787-5c9f6b08512d"
        }
      },
      "requestIdentifier": "oldauth2122",
      "version": "1.0"
    },
    "useLiveLayout": true,
    "replyMessage": {
      "imageIdentifier": "f1XXXX81-2XXe-4XX5-9XXd-36XXXXXXXX0d",
      "subtitle": "ReplyMessageSubtitle",
      "title": "ReplyMessage_New"
    },
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "send node1": "send node1 value",
      "serviceId": "32763",
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": "38792",
      "flowName": "AMBClassicalAuth",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"
}

```
```json New Authentication
{
  "sourceId": "db73f591-1e2f-XXXX-8ebf-6ba866808caa",
  "transid": "2b865cc5-3c11-XXXX-a08e-e266ad49a73f",
  "interactiveData": {
    "receivedMessage": {
      "imageIdentifier": "bd1883d0-fa6a-XXXX-94d1-fe3ba4b25ce8",
      "subtitle": "ReceiveMessageSubtitle",
      "title": "ReceiveMessage_New"
    },
    "data": {
      "images": [
        {
          "identifier": "81XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXX82",
          "url": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg"
        },
        {
          "identifier": "bdXXXX81-2XXe-4XX5-9XXd-36XXXXXXXXe8",
          "url": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg"
        }
      ],
      "newAuthenticate": {
        "oauth2": {
          "scope": [
            "r_liteprofile",
            "r_emailaddress"
          ],
          "additionalParameters": ""
        }
      },
      "requestIdentifier": "newauth12344",
      "version": "2.0"
    },
    "useLiveLayout": true,
    "replyMessage": {
      "imageIdentifier": "81XXXX81-2XXe-4XX5-9XXd-36XXXXXXXX82",
      "subtitle": "ReplyMessageSubtitle",
      "title": "ReplyMessage_New"
    },
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "DS start node Auth",
      "serviceId": "32763",
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": "33850",
      "flowName": "AMBAuthentcation",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d"}


```
```json iMessage
{
  "sourceId": "db73f591-1e2f-XXXX-8ebf-6ba866808caa",
  "transid": "2b865cc5-3c11-XXXX-a08e-e266ad49a73f",  "interactiveData": {
    "receivedMessage": {
      "subtitle": "Receive Message Subtitle",
      "title": "Receive Message title"
    },
    "appIcon": "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg",
    "useLiveLayout": true,
    "replyMessage": {
      "imageIdentifier": "cfXXXX26-9XX1-4XX7-bXXa-d9XXXXXXX40",
      "subtitle": "Reply Message Subtitle",
      "title": "Reply Message title"
    },
    "appName": "API Explorer",
    "teamId": "ADTXXXX7YB",
    "appStoreId": "106XXXX552",
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
    "extensionId": "com.imimobile.fcmconnect.MessagesExtension",
    "url": "?name=samplepackage&extraCharge=1.5&deliveryDate=27-11-2022&destinationName=Home&street=1infiniteloop&state=CA&city=Hyderabad&country=IND&postalCode=500084&latitude=17.331686&longitude=78.030656&isMyLocation=false&isFinalDestination=false"
  },
  "channel": "AppleBusinessChat",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "check": "Data stream Start node iMessage",
      "serviceId": "32763",
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": "33667",
      "flowName": "AMBiMessageResponseMultiUser",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "type": "interactive",
  "tid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "abcUserId": “Dummy Data”,
  "v": 1,
  "sendTypingIndicator": false,
  "appId": "a_63XXXXXXXXXXXX0000",
  "attachmentCount": 0,
  "x_msg_seq": 0,
  "serviceKey": "02XXXXd0-5XX7-1XXd-bXX8-12XXXXXXXX6d""
}
```
```json Rich Link
"{
  ""sourceId"": ""db73f591-1e2f-XXXX-8ebf-6ba866808caa"",
  ""transid"": ""95aa2197-928a-XXXX-a4d0-00b3c0677723"",
  ""channel"": ""AppleBusinessChat"",
  ""validateDestination"": false,
  ""dataIntegration"": {
    ""context"": {
      ""check"": ""DScheck630Start"",
      ""serviceId"": ""32763"",
      ""serviceName"": ""AMB650_MultipleUsersAsset"",
      ""flowId"": ""33699"",
      ""flowName"": ""AMBRichLink"",
      ""messagingAPI"": ""false""
    },
    ""appContext"": {
      
    }
  },
  ""type"": ""richLink"",
  ""tid"": ""95aa2197-928a-XXXX-a4d0-00b3c0677723"",
  ""clientUUID"": ""0a4a1900-98ef-XXXX-b9f9-5ef0927d6683"",
  ""x-wx-gtrid"": ""839999e9-256f-XXXX-5fbd-31b87468accd"",
  ""abcUserId"": ""urn:mbid:AQAAY60qTheTNgzRXmhGzC2PgVQvER1zlijKpna+OVr9LqhBpnFDZUtFJtss3pzF/RvxaK+iuxkOwqXXMaoQIufgbbJefToGl8980MHiUUCBkOsOWTMmVvs0pRbZ57ernMjoe4A8wKo14amNwiYRYOpyvFJ6YTc="",
  ""v"": 1,
  ""sendTypingIndicator"": false,
  ""appId"": ""a_6384126XXXX7140000"",
  ""attachmentCount"": 0,
  ""x_msg_seq"": 0,
  ""serviceKey"": ""95f74f99-bf45-XXXX-87be-12ec8b0d9009"",
  ""richLinkData"": {
    ""assets"": {
      ""image"": {
        ""mimeType"": ""image/jpeg"",
        ""url"": ""https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg""
      },
      ""video"": {
        ""mimeType"": ""video/mp4"",
        ""url"": ""https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4""
      }
    },
    ""title"": ""Google"",
    ""url"": ""https://www.google.com/""
  }
}"
```

The following table contains the parameter descriptions of Outbound Events.



| Field Name | Descriptions | Examples | Message Type |
| --- | --- | --- | --- |
| sourceId | The Apple Messages business ID of the client. | 31XXXX6-fXXe-4XX4-  <br>aXX8-a6XXXXXXXXca | Common parameter for all outbound message types. |
| transid | Unique transaction reference id of the request. | cfXXXX81-2XXe-  <br>4XX5-9XXd-36XXXXXXXX3a | Common parameter for all outbound message types. |
| channel | Channel is AppleBusinessChat always for incoming chats on Apple Messages for Business. | AppleBusinessChat | Common parameter for all outbound message types. |
| validateDestination | System variable. | False | Common parameter for all outbound message types. |
| dataIntegration | The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object. | "dataIntegration": {    "context":  <br> {       <br>"key1": "value1",  <br>"key2": "value2",  <br>"key3": "value3"     <br>},  <br>“appContext”: {  <br>}  <br>} | Common parameter for all outbound message types. |
| imageIdentifier | Unique Identifier for an image as given by the client. | a9XXXX98-9XX2-4XX5  <br>-bXXa-6aXXXXXXXX93 | List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage |
| context | The object contains key-value pairs which are added either by Data Stream admin or in flow. | "context": {   <br>                     "key1": "value1",  <br>                     "key2": "value2",  <br>                     "key3": "value3"     <br>} | Common parameter for all outbound message types. |
| serviceId | Contains the unique reference id of the service. | 12345 | Common parameter for all outbound message types. |
| serviceName | Contains the name of the service. | My New Service | Common parameter for all outbound message types. |
| flowId | Contains the unique ID for the flow. | 54321 | Common parameter for all outbound message types. |
| flowName | Contains the name of the flow | Sample Flow | Common parameter for all outbound message types. |
| messagingAPI | Indicates whether the request is sent through messaging API | true/false | Common parameter for all outbound message types. |
| appContext | The object is added as key-value pair either by Data Stream admin or in flow. | “appContext“: {  <br>“key1”: “value1“,  <br>“key2”: “value2“  <br>} | Common parameter for all outbound message types. |
| type | Contains the details of the event type. For invitation messages, this value is `invitation`. | `invitation` | Common parameter for all outbound message types. |
| body | Contains the information sent by the user. | simple text | Text and Text with Attachments. |
| tid | Transaction ID. | cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a | Common parameter for all outbound message types. |
| clientUUID | Contains the clients unique identification number. | 9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd | Common parameter for all outbound message types. |
| x-wx-gtrid | Contains the global transaction ID between cross-products for a given request. | d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9 | Common parameter for all outbound message types. |
| abcUserId | Contains the unique Apple Messages for Business user ID. For invitation messages, this value may be empty before the customer responds and the AMB user ID is resolved. | `urn:mbidTc=` | Common parameter for all outbound message types. |
| v | Version of the AMB REST API used for sending messages. | 1 | Common parameter for all outbound message types. |
| sendTypingIndicator | Indicates whether to send typing indicator before sending the actual message to customer. | false | Common parameter for all outbound message types. |
| appId | Contains the application ID. | a_63XXXXXXXXXXXX0000 | Common parameter for all outbound message types. |
| attachmentCount | Contains the total attachment count by the user. | 0 | Common parameter for all outbound message types. |
| x_msg_seq | This parameter represents whether the request should process sequence or not | 0 | Common parameter for all outbound message types. |
| text | Contains the text message sent by the user. | This is a AMB Message | Common parameter for all outbound message types. |
| serviceKey | Unique identification number for the service. | 02XXXXd0-5XX7-1XXd  <br>-bXX8-12XXXXXXXX6d | Common parameter for all outbound message types. |
| Ts | Timestamp when MO received to Webex Connect. | 2023-03-06T17:21:41.488+05:30 | Common parameter for all outbound message types. |
| richLinkData | Contains the details of rich link object | {  <br>    ""assets"": {  <br>      ""image"": {  <br>        ""mimeType"": ""image/jpeg"",  <br>        ""url"": ""  <br>      }, | Rich Link. |
| assets | Contains image or video asset. | NA | Rich Link. |
| images | Contains the details of the image. | NA | List Picker, Time Picker, Form Response, Classical Authentication, and New Authentication. |
| mimeType | Contains the format of the file. | image/jpg | Text with Attachments and Rich Link. |
| Url | Contains data that the app sends to the iMessage app. | Dummy Data | Text with Attachments, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, iMessage, and Rich Link. |
| title | Title name. | Online Shopping | Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, iMessage, and Rich Link. |
| ts | Timestamp when MO received to Webex Connect. | 1678104966670 | Text. |
| interactiveData | Contains the list/Time Picker (Date Picker) and Quick Reply data. | NA | Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage. |
| receivedMessage | A dictionary with information telling the Messages app how and what content to display the received message bubble. | NA | List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage. |
| subtitle | Subtitle name. | Upgrade to new phone. | List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage. |
| style | A style that controls the size of the view rendered by Live Layout. The default is icon. The other possible values are small, large. | Small | List Picker, Time Picker, and Form Response. |
| listPicker | Array that contains the list picker item(s) selected by the customer. | Dummy Data | List Picker. |
| items | Array that contains the list picker item(s) selected by the customer. | NA | Quick Reply, List Picker, and Form Response. |
| multipleSelection | A Bool value that defaults to false or singleSelect. Set to true to enable multipleSelection on the page. | true | List Picker and Form Response. |
| useLiveLayout | A Boolean that determines whether the Messages app should use Live Layout. | true | Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage. |
| bid | The bundle ID relevant to the message type. For iMessage App extension, it’s the app specific bundle ID. For all the other messages, it’s the default | "com.apple.messages.  <br>MSMessageExtensionBalloonPlugin:  <br>0000000000:com.apple.icloud.apps.  <br>messages.business.extension" | Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage. |
| data | A collection of name and values used for interactive message types. | NA | Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, and New Authentication. |
| timezoneOffset | Determines whether the startTime is in a specific time zone or in the customer's current time zone. | 330 | Time Picker. |
| location | Contains the geographical location of the user. | NA | Time Picker. |
| latitude | Contains the location of the date picker event. | 17.331686 | Time Picker. |
| radius | A number (data type: double) representing the location radius, in meters. Apple Messages for Business ignores this field when latitude and longitude are missing or empty. | 10 | Time Picker. |
| longitude | Contains the location details of the business. | 0.3048 | Time Picker. |
| timeslots | Array that contains the time slot selected by the customer. | NA | Time Picker. |
| startTime | Displays the time at which the event has started. | 2024-12-28T06:30Z | Time Picker. |
| alternateTitle | Alternate name for the title. | ReplySubtitle | List Picker. |
| quick-reply | Allows the customer with a single tap to make a choice. | NA | Quick Reply. |
| summaryText | Summary text that will be used for device notification but will also shown in the transcript after the end user selects one of the quick reply options. | This is QR Summary Text. | Quick Reply. |
| selectedIndex | The selected item number from top order. | 0 | Quick Reply. |
| dynamic | JSON object that contains entire data of the dynamic message types such as Form message. | NA | Form Response. |
| template | Name of the template | messageForms | Form Response. |
| showSummary | Displays the summary. | true | Form Response. |
| pages | An array of different pages to be shown in the form. Every page object has following common objects. | NA | Form Response. |
| submitForm | A Bool value placed on the pages to denote the end page of the form. Since multiple pages can act as an end page, this object can be set on multiple pages. | false | Form Response. |
| nextPageIdentifier | Contains the details of single select option page, where you specify the nextPageIdentifier within each of the item objects. | 1 | Form Response. |
| multipleSelection | A Bool value that defaults to false or singleSelect. Set to true to enable multipleSelection on the page. | true | List Picker and Form Response. |
| dateFormat | A string representing the date format on the page. | mm/dd/yyyy | Form Response. |
| labelText | A string representing the text string to be shown next to date field. Defaults to text 'Date'. | Select Delivery Date | Form Response. |
| maximumDate | A string representing the maximum date that a date picker can show. Defaults to current date. | 02/13/2020 | Form Response. |
| minimumDate | A string representing the minimum date that a date picker can show. | 01/01/2020 | Form Response. |
| startDate | A string representing the date displayed by the date picker. Defaults to current date. | 01/01/2020 | Form Response. |
| regex | A string representing a JSON encoded regular expression (regex) string to limit the type of input for input field to use | ^\\w+$ | Form Response. |
| maximumCharacterCount | Maximum number of characters allowed. | 10 | Form Response. |
| keyboardType | Type of keyboard to be shown. Possible values: -default: Default value. | IKeyboardTypeEmailAddress | Form Response. |
| inputType | A string value that defaults to singleline. Other values are multiline or singleline. | multiline | Form Response. |
| placeholder | A text string used when there is no other text in the input text field. Default value are Required or Optional. | Please enter issues. | Form Response. |
| splash | The object that contains the splash parameters and values. Splash is shown at the start of the form. |  | Form Response. |
| splashtext | Displays the body copy for the page. | Kindly fill the form | Form Response. |
| buttonTitle | Contains the  title for the button. | Continue | Form Response. |
| Header | Displays in bold the title on the page underneath the image. | Apple Card | Form Response. |
| destinationId | Destination used for the outbound invitation message. For invitation messages, this value is the customer mobile number in `tel:+E.164` format. | `tel:+4477362XXXX` | Invitation Message |
| msisdn | Customer mobile number used for the invitation. | `+4477362XXXX` | Invitation Message |
| withImage | Indicates whether the invitation message is sent with the business image or brand logo. | `true` | Invitation Message |
| brandName | Brand name displayed in the invitation message. | `Delta` | Invitation Message |
| requestIdentifier | Identifier associated with the invitation request and response. | `fcb5e9ca-0ddc-4a07-bf9b-7fcbd044aeeb` | Invitation Message |




**Apple Messages for Business Delivery Receipts**

The following are the Apple Messages for Business delivery receipts payloads.

```json Submitted
{
  "deliveryInfoNotification": {
    "subtid": "85c4aea8-66f0-XXXX-8045-c443f7d1a178",
    "deliveryInfo": {
      "deliveryChannel": "applebusinesschat",
      "Description": "Submitted",
      "destinationType": "msisdn",
      "timeStamp": "2026-05-12T06:52:59.311Z",
      "code": "7501",
      "additionalInfo": "",
      "deliveryStatus": "Submitted",
      "destination": "4477362XXXX"
    },
    "correlationid": "corr-12345",
    "callbackData": "customer-context",
    "transid": "00dff89a-4feb-XXXX-8742-3847933492bb"
  }
}
```
```json Failed
{
  "x-wx-gtrid": "effdc4a6-f9af-XXXX-98fe-a4102f550090",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-04-02T11:05:06.066+05:30",
      "Description": "Service provider exception.",
      "code": "7010",
      "deliveryChannel": "applebusinesschat",
      "additionalInfo": "Status Code 410, Resp:410 Gone : Session not found",
      "destination": "Dummy Data",
      "destinationType": "applebusinesschat",
      "deliveryStatus": "Failed"
    },
    "subtid": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXc",
    "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a,
    "callbackData": "This is callbackdata",
    "correlationid": "3eXXXX81-2XXe-4XX5-9XXd-36XXXXXXXXd9"
  },
  "dataIntegration": {
    "context": {
      "serviceId": "32763",
      "serviceName": "AMB_MultipleUsersAsset",
      "flowId": "54321",
      "flowName": "AMBIncmingMessageEvent",
      "messagingAPI": "true"
    },
    "appContext": {
      
    }
  }
}
```
```json Invitation Message - Submitted
{
  "x-wx-gtrid": "11XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXX22",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2026-05-12T11:21:14.971+05:30",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "applebusinesschat",
      "additionalInfo": "",
      "destination": "4477362XXXX",
      "destinationType": "msisdn",
      "deliveryStatus": "Submitted"
    },
    "subtid": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXca",
    "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
    "callbackData": "This is callbackdata",
    "correlationid": "3eXXXX81-2XXe-4XX5-9XXd-36XXXXXXXXd9"
  }
}
```
```json Invitation Message - Failed
{
  "deliveryInfoNotification": {
    "subtid": "85c4aea8-66f0-XXXX-8045-c443f7d1a178",
    "deliveryInfo": {
      "deliveryChannel": "applebusinesschat",
      "Description": "Internal server error",
      "destinationType": "msisdn",
      "timeStamp": "2026-05-12T14:20:09.383Z",
      "code": "7006",
      "additionalInfo": "404 Not Found : No device registrations for user",
      "deliveryStatus": "Failed",
      "destination": "4477362XXXX"
    },
    "correlationid": "corr-12345",
    "callbackData": "customer-context",
    "transid": "f7a31230-dd19-XXXX-b60b-983a094bd70d"
  }
}
```

The following table contains the parameter descriptions of Delivery Receipts .



| Field Name | Descriptions | Example | Message Type |
| --- | --- | --- | --- |
| x-wx-gtrid | Contains the global transaction ID between cross-products for a given request. | d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9 | Common parameter for all delivery receipts. |
| deliveryInfoNotification | System variable | NA | Common parameter for all delivery receipts. |
| deliveryInfo | System variable | NA | Common parameter for all delivery receipts. |
| timeStamp | Timestamp of the event. The timestamp mentioned in the outbound webhook is as per the timezone of the tenant and not UTC as a standard. | 2023-03-06T17:53:02.270+05:30 | Common parameter for all delivery receipts. |
| Description | Detailed description of the delivery status. | Submitted | Common parameter for all event types. |
| code | Status code as mentioned in the documentation. | 1011 | Common parameter for all delivery receipts. |
| deliveryChannel | Channel used to send the message i.e., Apple Messages for Business in this case. | Apple Messages for Business | Common parameter for all delivery receipts. |
| additionalInfo | Additional information about the transaction. | Status Code 410 | Common parameter for all delivery receipts. |
| destination | For standard Apple Messages for Business messages, this contains the unique user ID for the recipient. For invitation message delivery receipts, this contains the invited customer's mobile number, when available. | `4477362XXXX` | Common parameter for all delivery receipts. |
| destinationType | For standard Apple Messages for Business messages, this value is `applebusinesschat`. For invitation message delivery receipts, this value is `msisdn`. | `msisdn` | Common parameter for all delivery receipts. |
| deliveryStatus | Status of messages once sent. For invitation messages, supported values include `Submitted` and `Failed`. Apple does not provide delivery or read status events for invitation messages. | `Submitted` | Common parameter for all delivery receipts. |
| subtid | A unique transaction id will be generated as subtid for the flow level transactions(or node tid) | 31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXc | Common parameter for all delivery receipts. |
| transid | Unique transaction reference id of the request. | f4XXXX7e-5XXb-4XX9-9XXf-3bXXXXXXXf3d | Common parameter for all delivery receipts. |
| callbackData | Data that you have configured to receive on the notify Url. This is configured as a part of the request. | This is callback data. | Common parameter for all delivery receipts. |
| correlationid | The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request. | 12XXXX7e-5XXb-4XX9-9XXf-3bXXXXXXX90 | Common parameter for all delivery receipts. |
| dataIntegration | The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object. | "dataIntegration": {    "context":  <br> {       <br>"key1": "value1",  <br>"key2": "value2",  <br>"key3": "value3"     <br>},  <br>“appContext”: {  <br>}  <br>} | Common parameter for all delivery receipts. |
| context | The object contains  key-value pairs which are added either by Data Stream admin or in flow. | "context": {   <br>                     "key1": "value1",  <br>                     "key2": "value2",  <br>                     "key3": "value3"     <br>} | Common parameter for all delivery receipts. |
| serviceId | Contains the unique reference id of the service. | 12345 | Common parameter for all delivery receipts. |
| serviceName | Contains the name of the service. | My New Service | Common parameter for all delivery receipts. |
| flowId | Contains the unique ID for the flow. | 54321 | Common parameter for all delivery receipts. |
| flowName | Contains the name of the flow | Sample Flow | Common parameter for all delivery receipts. |
| messagingAPI | It is a boolean parameter. If the value is True, the message was sent using messaging API. If the value is False, the message was sent using either flow or rule. | true/false | Common parameter for all delivery receipts. |
| appContext | The object is added as key-value pair either by Data Stream admin or in flow. | “appContext“: {  <br>                           “key1”: “value1“,  <br>                          “key2”: “value2“  <br>} | Common parameter for all delivery receipts. |



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
