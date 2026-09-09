**<<AMB>> - Inbound Message**

The following are the <<AMB>> inbound message payloads.

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

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Descriptions",
    "h-2": "Example",
    "h-3": "Message Type",
    "0-0": "attachments",
    "0-1": "Contains the attachment sent by the user",
    "0-2": "[www.webexconnect.com](http://www.webexconnect.com)",
    "0-3": "Text with attachments, List Picker, Time Picker, iMessage",
    "1-0": "capabilities",
    "1-1": "This field has been deprecated by Apple Messages for Business in March 2022 and no longer contains any value. Refer to capabilityList field instead.",
    "1-2": "NA",
    "1-3": "Text, List Picker, Time Picker, Classical Authentication, Quick Reply, Conversation Closed",
    "2-0": "channel",
    "2-1": "Name of the channel.",
    "2-2": "Apple Business Chat",
    "2-3": "Common parameter for all inbound event types.",
    "3-0": "abcAccountId",
    "3-1": "Contains the unique Apple Messages for Business account ID.",
    "3-2": "31XXXX96-fXXe-4XX4  \n-aXX8-a6XXXXXXXXca",
    "3-3": "Common parameter for all inbound event types.",
    "4-0": "dataIntegration",
    "4-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object..",
    "4-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "4-3": "Common parameter for all inbound event types.",
    "5-0": "context",
    "5-1": "The object contains  key-value pairs which are added either by Data Stream admin or in flow.",
    "5-2": "\"context\": {   \n                     \"key1\": \"value1\",  \n                     \"key2\": \"value2\",  \n                     \"key3\": \"value3\"     \n}",
    "5-3": "Common parameter for all inbound event types.",
    "6-0": "serviceId",
    "6-1": "Contains the unique reference id of the service.",
    "6-2": "12345",
    "6-3": "Common parameter for all inbound event types.",
    "7-0": "serviceName",
    "7-1": "Contains the name of the service.",
    "7-2": "My New Service",
    "7-3": "Common parameter for all inbound event types.",
    "8-0": "flowId",
    "8-1": "Contains the unique ID for the flow.",
    "8-2": "54321",
    "8-3": "Common parameter for all inbound event types.",
    "9-0": "flowName",
    "9-1": "Contains the name of the flow.",
    "9-2": "Sample Flow",
    "9-3": "Common parameter for all inbound event types.",
    "10-0": "messagingAPI",
    "10-1": "It is a boolean parameter. If the value is True, the message was sent using messaging API. If the value is False, the message was sent using either flow or rule.",
    "10-2": "true/false",
    "10-3": "Common parameter for all inbound event types.",
    "11-0": "appContext",
    "11-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "11-2": "“appContext“: {  \n                           “key1”: “value1“,  \n                          “key2”: “value2“  \n}",
    "11-3": "Common parameter for all inbound event types.",
    "12-0": "bizIntentId",
    "12-1": "The intention, or purpose, of the chat as specified by the business, such as account_question.",
    "12-2": "account_question",
    "12-3": "Text, List Picker, Time Picker, and Quick Reply.",
    "13-0": "type",
    "13-1": "Contains the details of event type.",
    "13-2": "text",
    "13-3": "Common parameter for all inbound event types.",
    "14-0": "message",
    "14-1": "Contains the text message sent by the user.",
    "14-2": "This is a test message.",
    "14-3": "Common parameter for all inbound event types.",
    "15-0": "locale",
    "15-1": "Contains the location-based language setting",
    "15-2": "en_US",
    "15-3": "Common parameter for all inbound event types.",
    "16-0": "tid",
    "16-1": "Transaction ID",
    "16-2": "9fXXXX4e-fXXb-dXXb  \n-3XX0-9eXXXXXXXX4c",
    "16-3": "Common parameter for all inbound event types.",
    "17-0": "x-wx-gtrid",
    "17-1": "Contains the global transaction ID between cross-products for a given request.",
    "17-2": "d7XXXX76-3XXa-4XXe  \n-9XX3-d6XXXXXXXXf9",
    "17-3": "Common parameter for all inbound event types.",
    "18-0": "abcUserId",
    "18-1": "Contains the unique Apple Messages for Business user ID",
    "18-2": "urn:mbidTc=",
    "18-3": "Common parameter for all inbound event types.",
    "19-0": "datetime",
    "19-1": "Data and Time on which the message is received.",
    "19-2": "2020-02-25T12:40:45.051+05:30",
    "19-3": "Common parameter for all inbound event types.",
    "20-0": "bizGroupId",
    "20-1": "Contains the business group ID.",
    "20-2": "Sales",
    "20-3": "Text, List Picker, Time Picker, Quick Reply",
    "21-0": "deviceAgent",
    "21-1": "This field has been deprecated by Apple Messages for Business in March 2022 and no longer contains any value.",
    "21-2": "NA",
    "21-3": "Common parameter for all inbound event types.",
    "22-0": "capabilityList",
    "22-1": "A string list that identifies Messages for Business features supported by the customer’s device. The list items are case insensitive and separated by commas. When a customer sends a message, this field allows you to understand the customer device capabilities to compose an appropriate response for that device.",
    "22-2": "AUTH%2CLIST%2CTIME  \n%2CQUICK%2CAUTH2",
    "22-3": "Common parameter for all inbound event types.",
    "23-0": "appId",
    "23-1": "Contains the application ID.",
    "23-2": "a_63XXXXXXXXXXXXX000",
    "23-3": "Common parameter for all inbound event types.",
    "24-0": "requestIdentifier",
    "24-1": "Applicable for responses to interactive message types such as Quick Replies and Invitation Response. It can be used to correlate the user response to a previously sent interactive message or invitation message.",
    "24-2": "`fcb5e9ca-0ddc-4a07-bf9b-7fcbd044aeeb`",
    "24-3": "Quick Reply, List Picker, Time Picker, Classical Authentication, New Authentication, Form Response, and Invitation Response",
    "25-0": "event",
    "25-1": "Contains the incoming event type. For invitation responses, this value is `InvitationResponse`.",
    "25-2": "`InvitationResponse`",
    "25-3": "Common parameter for all inbound event types.",
    "26-0": "ts",
    "26-1": "Timestamp when MO received to <<prodname>>",
    "26-2": "2023-03-06T17:21:41.488+05:30",
    "26-3": "Common parameter for all inbound event types.",
    "27-0": "timestamp",
    "27-1": "Timestamp when MO received to connect. This is an old field. This info is now available in the 'ts' field.",
    "27-2": "2023-03-06T17:21:41.488+05:30",
    "27-3": "Text and List Picker event type.",
    "28-0": "listPicker",
    "28-1": "Contains the JSON payload of    list picker response as selected by the customer.",
    "28-2": "\"{\\\"otherItemCount\\\":0,\\\"selectedItemCount\\\":3,  \n\\\"selectedItems\\\":[{\\\"identifier\\\":\\\"0\\\",\\\"style\\\":\\\"default\\\",  \n\\\"title\\\":\\\"iPhone X\\\",\\\"order\\\":\\\"0\\\"},]}\",",
    "28-3": "List Picker and Time Picker event type.",
    "29-0": "datePicker",
    "29-1": "Contains the JSON payload of    time picker response as selected by the customer.",
    "29-2": "\"{\\\"identifier\\\":\\\"fdXXXX99-6XX1-4XX6-aXX8-aeXXXXXXXX9c\\\",  \n\\\"timezoneOffset\\\":\\\"-100\\\",\\\"location\\\":{},  \n\\\"title\\\":\\\"NHS Appointments\\\",  \n\\\"timeslots\\\":[{\\\"duration\\\":\\\"1800\\\",\\\"identifier\\\":\\\"3\\\",  \n\\\"startTime\\\":\\\"2023-03-22T12:30+0000\\\"}]}\",",
    "29-3": "List Picker and Time Picker event type.",
    "30-0": "bid",
    "30-1": "The bundle ID relevant to the message type. For iMessage App extension, it’s the app specific bundle ID. For all the other messages, it’s the default.",
    "30-2": "\"com.apple.messages.MSMessage  \nExtensionBalloonPlugin:0000000000:com.  \napple.icloud.apps.messages.business.extension\"",
    "30-3": "iMessage event type.",
    "31-0": "type",
    "31-1": "Contains the details of event type.",
    "31-2": "text",
    "31-3": "Common parameter for all inbound event types.",
    "32-0": "quickreplies",
    "32-1": "Allows the customer with a single tap to make a choice.",
    "32-2": "\"{\\\"selectedIdentifier\\\":\\\"345345\\\",\\\"items\\\":[{\\\"identifier\\\":\\\"2323\\\",\\\"title\\\":\\\"TestCloudQA\\\"},{\\\"identifier\\\":\\\"345345\\\",\\\"title\\\":\\\"No 👎\\\"}],\\\"selectedIndex\\\":1}\",",
    "32-3": "Quick Reply",
    "33-0": "formResponse",
    "33-1": "Allows the customer to create  interactive flows.",
    "33-2": "\"formResponse\": \"{\\\"template\\\":\\\"messageForms\"}\"",
    "33-3": "Form Response",
    "34-0": "msisdn",
    "34-1": "Customer mobile number used for the invitation, when available.",
    "34-2": "`+4477362XXXX`",
    "34-3": "Invitation Response",
    "35-0": "invitationAccepted",
    "35-1": "Indicates whether the customer accepted the invitation.",
    "35-2": "`true`",
    "35-3": "Invitation Response",
    "36-0": "invitationResponse",
    "36-1": "Invitation response payload returned as an escaped JSON string.",
    "36-2": "`{\"notification\":{\"id\":\"yes\"}}`",
    "36-3": "Invitation Response",
    "37-0": "interactiveData.sessionIdentifier",
    "37-1": "Apple session identifier received in the invitation response payload, when available.",
    "37-2": "`de82fd8a-bcb4-3b2c-b14c-f52e63f40940`",
    "37-3": "Invitation Response"
  },
  "cols": 4,
  "rows": 38,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**<<AMB>> - Outbound Message**

The following are the <<AMB>> outbound message payloads.

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

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Descriptions",
    "h-2": "Examples",
    "h-3": "Message Type",
    "0-0": "sourceId",
    "0-1": "The Apple Messages business ID of the client.",
    "0-2": "31XXXX6-fXXe-4XX4-  \naXX8-a6XXXXXXXXca",
    "0-3": "Common parameter for all outbound message types.",
    "1-0": "transid",
    "1-1": "Unique transaction reference id of the request.",
    "1-2": "cfXXXX81-2XXe-  \n4XX5-9XXd-36XXXXXXXX3a",
    "1-3": "Common parameter for all outbound message types.",
    "2-0": "channel",
    "2-1": "Channel is AppleBusinessChat always for incoming chats on Apple Messages for Business.",
    "2-2": "AppleBusinessChat",
    "2-3": "Common parameter for all outbound message types.",
    "3-0": "validateDestination",
    "3-1": "System variable.",
    "3-2": "False",
    "3-3": "Common parameter for all outbound message types.",
    "4-0": "dataIntegration",
    "4-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "4-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "4-3": "Common parameter for all outbound message types.",
    "5-0": "imageIdentifier",
    "5-1": "Unique Identifier for an image as given by the client.",
    "5-2": "a9XXXX98-9XX2-4XX5  \n-bXXa-6aXXXXXXXX93",
    "5-3": "List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage",
    "6-0": "context",
    "6-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "6-2": "\"context\": {   \n                     \"key1\": \"value1\",  \n                     \"key2\": \"value2\",  \n                     \"key3\": \"value3\"     \n}",
    "6-3": "Common parameter for all outbound message types.",
    "7-0": "serviceId",
    "7-1": "Contains the unique reference id of the service.",
    "7-2": "12345",
    "7-3": "Common parameter for all outbound message types.",
    "8-0": "serviceName",
    "8-1": "Contains the name of the service.",
    "8-2": "My New Service",
    "8-3": "Common parameter for all outbound message types.",
    "9-0": "flowId",
    "9-1": "Contains the unique ID for the flow.",
    "9-2": "54321",
    "9-3": "Common parameter for all outbound message types.",
    "10-0": "flowName",
    "10-1": "Contains the name of the flow",
    "10-2": "Sample Flow",
    "10-3": "Common parameter for all outbound message types.",
    "11-0": "messagingAPI",
    "11-1": "Indicates whether the request is sent through messaging API",
    "11-2": "true/false",
    "11-3": "Common parameter for all outbound message types.",
    "12-0": "appContext",
    "12-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "12-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "12-3": "Common parameter for all outbound message types.",
    "13-0": "type",
    "13-1": "Contains the details of the event type. For invitation messages, this value is `invitation`.",
    "13-2": "`invitation`",
    "13-3": "Common parameter for all outbound message types.",
    "14-0": "body",
    "14-1": "Contains the information sent by the user.",
    "14-2": "simple text",
    "14-3": "Text and Text with Attachments.",
    "15-0": "tid",
    "15-1": "Transaction ID.",
    "15-2": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
    "15-3": "Common parameter for all outbound message types.",
    "16-0": "clientUUID",
    "16-1": "Contains the clients unique identification number.",
    "16-2": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
    "16-3": "Common parameter for all outbound message types.",
    "17-0": "x-wx-gtrid",
    "17-1": "Contains the global transaction ID between cross-products for a given request.",
    "17-2": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
    "17-3": "Common parameter for all outbound message types.",
    "18-0": "abcUserId",
    "18-1": "Contains the unique Apple Messages for Business user ID. For invitation messages, this value may be empty before the customer responds and the AMB user ID is resolved.",
    "18-2": "`urn:mbidTc=`",
    "18-3": "Common parameter for all outbound message types.",
    "19-0": "v",
    "19-1": "Version of the AMB REST API used for sending messages.",
    "19-2": "1",
    "19-3": "Common parameter for all outbound message types.",
    "20-0": "sendTypingIndicator",
    "20-1": "Indicates whether to send typing indicator before sending the actual message to customer.",
    "20-2": "false",
    "20-3": "Common parameter for all outbound message types.",
    "21-0": "appId",
    "21-1": "Contains the application ID.",
    "21-2": "a_63XXXXXXXXXXXX0000",
    "21-3": "Common parameter for all outbound message types.",
    "22-0": "attachmentCount",
    "22-1": "Contains the total attachment count by the user.",
    "22-2": "0",
    "22-3": "Common parameter for all outbound message types.",
    "23-0": "x_msg_seq",
    "23-1": "This parameter represents whether the request should process sequence or not",
    "23-2": "0",
    "23-3": "Common parameter for all outbound message types.",
    "24-0": "text",
    "24-1": "Contains the text message sent by the user.",
    "24-2": "This is a AMB Message",
    "24-3": "Common parameter for all outbound message types.",
    "25-0": "serviceKey",
    "25-1": "Unique identification number for the service.",
    "25-2": "02XXXXd0-5XX7-1XXd  \n-bXX8-12XXXXXXXX6d",
    "25-3": "Common parameter for all outbound message types.",
    "26-0": "Ts",
    "26-1": "Timestamp when MO received to <<prodname>>.",
    "26-2": "2023-03-06T17:21:41.488+05:30",
    "26-3": "Common parameter for all outbound message types.",
    "27-0": "richLinkData",
    "27-1": "Contains the details of rich link object",
    "27-2": "{  \n    \"\"assets\"\": {  \n      \"\"image\"\": {  \n        \"\"mimeType\"\": \"\"image/jpeg\"\",  \n        \"\"url\"\": \"\"  \n      },",
    "27-3": "Rich Link.",
    "28-0": "assets",
    "28-1": "Contains image or video asset.",
    "28-2": "NA",
    "28-3": "Rich Link.",
    "29-0": "images",
    "29-1": "Contains the details of the image.",
    "29-2": "NA",
    "29-3": "List Picker, Time Picker, Form Response, Classical Authentication, and New Authentication.",
    "30-0": "mimeType",
    "30-1": "Contains the format of the file.",
    "30-2": "image/jpg",
    "30-3": "Text with Attachments and Rich Link.",
    "31-0": "Url",
    "31-1": "Contains data that the app sends to the iMessage app.",
    "31-2": "Dummy Data",
    "31-3": "Text with Attachments, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, iMessage, and Rich Link.",
    "32-0": "title",
    "32-1": "Title name.",
    "32-2": "Online Shopping",
    "32-3": "Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, iMessage, and Rich Link.",
    "33-0": "ts",
    "33-1": "Timestamp when MO received to <<prodname>>.",
    "33-2": "1678104966670",
    "33-3": "Text.",
    "34-0": "interactiveData",
    "34-1": "Contains the list/Time Picker (Date Picker) and Quick Reply data.",
    "34-2": "NA",
    "34-3": "Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage.",
    "35-0": "receivedMessage",
    "35-1": "A dictionary with information telling the Messages app how and what content to display the received message bubble.",
    "35-2": "NA",
    "35-3": "List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage.",
    "36-0": "subtitle",
    "36-1": "Subtitle name.",
    "36-2": "Upgrade to new phone.",
    "36-3": "List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage.",
    "37-0": "style",
    "37-1": "A style that controls the size of the view rendered by Live Layout. The default is icon. The other possible values are small, large.",
    "37-2": "Small",
    "37-3": "List Picker, Time Picker, and Form Response.",
    "38-0": "listPicker",
    "38-1": "Array that contains the list picker item(s) selected by the customer.",
    "38-2": "Dummy Data",
    "38-3": "List Picker.",
    "39-0": "items",
    "39-1": "Array that contains the list picker item(s) selected by the customer.",
    "39-2": "NA",
    "39-3": "Quick Reply, List Picker, and Form Response.",
    "40-0": "multipleSelection",
    "40-1": "A Bool value that defaults to false or singleSelect. Set to true to enable multipleSelection on the page.",
    "40-2": "true",
    "40-3": "List Picker and Form Response.",
    "41-0": "useLiveLayout",
    "41-1": "A Boolean that determines whether the Messages app should use Live Layout.",
    "41-2": "true",
    "41-3": "Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage.",
    "42-0": "bid",
    "42-1": "The bundle ID relevant to the message type. For iMessage App extension, it’s the app specific bundle ID. For all the other messages, it’s the default",
    "42-2": "\"com.apple.messages.  \nMSMessageExtensionBalloonPlugin:  \n0000000000:com.apple.icloud.apps.  \nmessages.business.extension\"",
    "42-3": "Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, New Authentication, and iMessage.",
    "43-0": "data",
    "43-1": "A collection of name and values used for interactive message types.",
    "43-2": "NA",
    "43-3": "Quick Reply, List Picker, Time Picker, Form Response, Classical Authentication, and New Authentication.",
    "44-0": "timezoneOffset",
    "44-1": "Determines whether the startTime is in a specific time zone or in the customer's current time zone.",
    "44-2": "330",
    "44-3": "Time Picker.",
    "45-0": "location",
    "45-1": "Contains the geographical location of the user.",
    "45-2": "NA",
    "45-3": "Time Picker.",
    "46-0": "latitude",
    "46-1": "Contains the location of the date picker event.",
    "46-2": "17.331686",
    "46-3": "Time Picker.",
    "47-0": "radius",
    "47-1": "A number (data type: double) representing the location radius, in meters. Apple Messages for Business ignores this field when latitude and longitude are missing or empty.",
    "47-2": "10",
    "47-3": "Time Picker.",
    "48-0": "longitude",
    "48-1": "Contains the location details of the business.",
    "48-2": "0.3048",
    "48-3": "Time Picker.",
    "49-0": "timeslots",
    "49-1": "Array that contains the time slot selected by the customer.",
    "49-2": "NA",
    "49-3": "Time Picker.",
    "50-0": "startTime",
    "50-1": "Displays the time at which the event has started.",
    "50-2": "2024-12-28T06:30Z",
    "50-3": "Time Picker.",
    "51-0": "alternateTitle",
    "51-1": "Alternate name for the title.",
    "51-2": "ReplySubtitle",
    "51-3": "List Picker.",
    "52-0": "quick-reply",
    "52-1": "Allows the customer with a single tap to make a choice.",
    "52-2": "NA",
    "52-3": "Quick Reply.",
    "53-0": "summaryText",
    "53-1": "Summary text that will be used for device notification but will also shown in the transcript after the end user selects one of the quick reply options.",
    "53-2": "This is QR Summary Text.",
    "53-3": "Quick Reply.",
    "54-0": "selectedIndex",
    "54-1": "The selected item number from top order.",
    "54-2": "0",
    "54-3": "Quick Reply.",
    "55-0": "dynamic",
    "55-1": "JSON object that contains entire data of the dynamic message types such as Form message.",
    "55-2": "NA",
    "55-3": "Form Response.",
    "56-0": "template",
    "56-1": "Name of the template",
    "56-2": "messageForms",
    "56-3": "Form Response.",
    "57-0": "showSummary",
    "57-1": "Displays the summary.",
    "57-2": "true",
    "57-3": "Form Response.",
    "58-0": "pages",
    "58-1": "An array of different pages to be shown in the form. Every page object has following common objects.",
    "58-2": "NA",
    "58-3": "Form Response.",
    "59-0": "submitForm",
    "59-1": "A Bool value placed on the pages to denote the end page of the form. Since multiple pages can act as an end page, this object can be set on multiple pages.",
    "59-2": "false",
    "59-3": "Form Response.",
    "60-0": "nextPageIdentifier",
    "60-1": "Contains the details of single select option page, where you specify the nextPageIdentifier within each of the item objects.",
    "60-2": "1",
    "60-3": "Form Response.",
    "61-0": "multipleSelection",
    "61-1": "A Bool value that defaults to false or singleSelect. Set to true to enable multipleSelection on the page.",
    "61-2": "true",
    "61-3": "List Picker and Form Response.",
    "62-0": "dateFormat",
    "62-1": "A string representing the date format on the page.",
    "62-2": "mm/dd/yyyy",
    "62-3": "Form Response.",
    "63-0": "labelText",
    "63-1": "A string representing the text string to be shown next to date field. Defaults to text 'Date'.",
    "63-2": "Select Delivery Date",
    "63-3": "Form Response.",
    "64-0": "maximumDate",
    "64-1": "A string representing the maximum date that a date picker can show. Defaults to current date.",
    "64-2": "02/13/2020",
    "64-3": "Form Response.",
    "65-0": "minimumDate",
    "65-1": "A string representing the minimum date that a date picker can show.",
    "65-2": "01/01/2020",
    "65-3": "Form Response.",
    "66-0": "startDate",
    "66-1": "A string representing the date displayed by the date picker. Defaults to current date.",
    "66-2": "01/01/2020",
    "66-3": "Form Response.",
    "67-0": "regex",
    "67-1": "A string representing a JSON encoded regular expression (regex) string to limit the type of input for input field to use",
    "67-2": "^\\\\w+$",
    "67-3": "Form Response.",
    "68-0": "maximumCharacterCount",
    "68-1": "Maximum number of characters allowed.",
    "68-2": "10",
    "68-3": "Form Response.",
    "69-0": "keyboardType",
    "69-1": "Type of keyboard to be shown. Possible values: -default: Default value.",
    "69-2": "IKeyboardTypeEmailAddress",
    "69-3": "Form Response.",
    "70-0": "inputType",
    "70-1": "A string value that defaults to singleline. Other values are multiline or singleline.",
    "70-2": "multiline",
    "70-3": "Form Response.",
    "71-0": "placeholder",
    "71-1": "A text string used when there is no other text in the input text field. Default value are Required or Optional.",
    "71-2": "Please enter issues.",
    "71-3": "Form Response.",
    "72-0": "splash",
    "72-1": "The object that contains the splash parameters and values. Splash is shown at the start of the form.",
    "72-2": "",
    "72-3": "Form Response.",
    "73-0": "splashtext",
    "73-1": "Displays the body copy for the page.",
    "73-2": "Kindly fill the form",
    "73-3": "Form Response.",
    "74-0": "buttonTitle",
    "74-1": "Contains the  title for the button.",
    "74-2": "Continue",
    "74-3": "Form Response.",
    "75-0": "Header",
    "75-1": "Displays in bold the title on the page underneath the image.",
    "75-2": "Apple Card",
    "75-3": "Form Response.",
    "76-0": "destinationId",
    "76-1": "Destination used for the outbound invitation message. For invitation messages, this value is the customer mobile number in `tel:+E.164` format.",
    "76-2": "`tel:+4477362XXXX`",
    "76-3": "Invitation Message",
    "77-0": "msisdn",
    "77-1": "Customer mobile number used for the invitation.",
    "77-2": "`+4477362XXXX`",
    "77-3": "Invitation Message",
    "78-0": "withImage",
    "78-1": "Indicates whether the invitation message is sent with the business image or brand logo.",
    "78-2": "`true`",
    "78-3": "Invitation Message",
    "79-0": "brandName",
    "79-1": "Brand name displayed in the invitation message.",
    "79-2": "`Delta`",
    "79-3": "Invitation Message",
    "80-0": "requestIdentifier",
    "80-1": "Identifier associated with the invitation request and response.",
    "80-2": "`fcb5e9ca-0ddc-4a07-bf9b-7fcbd044aeeb`",
    "80-3": "Invitation Message"
  },
  "cols": 4,
  "rows": 81,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**<<AMB>> Delivery Receipts**

The following are the <<AMB>> delivery receipts payloads.

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

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Descriptions",
    "h-2": "Example",
    "h-3": "Message Type",
    "0-0": "x-wx-gtrid",
    "0-1": "Contains the global transaction ID between cross-products for a given request.",
    "0-2": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
    "0-3": "Common parameter for all delivery receipts.",
    "1-0": "deliveryInfoNotification",
    "1-1": "System variable",
    "1-2": "NA",
    "1-3": "Common parameter for all delivery receipts.",
    "2-0": "deliveryInfo",
    "2-1": "System variable",
    "2-2": "NA",
    "2-3": "Common parameter for all delivery receipts.",
    "3-0": "timeStamp",
    "3-1": "Timestamp of the event. The timestamp mentioned in the outbound webhook is as per the timezone of the tenant and not UTC as a standard.",
    "3-2": "2023-03-06T17:53:02.270+05:30",
    "3-3": "Common parameter for all delivery receipts.",
    "4-0": "Description",
    "4-1": "Detailed description of the delivery status.",
    "4-2": "Submitted",
    "4-3": "Common parameter for all event types.",
    "5-0": "code",
    "5-1": "Status code as mentioned in the documentation.",
    "5-2": "1011",
    "5-3": "Common parameter for all delivery receipts.",
    "6-0": "deliveryChannel",
    "6-1": "Channel used to send the message i.e., Apple Messages for Business in this case.",
    "6-2": "Apple Messages for Business",
    "6-3": "Common parameter for all delivery receipts.",
    "7-0": "additionalInfo",
    "7-1": "Additional information about the transaction.",
    "7-2": "Status Code 410",
    "7-3": "Common parameter for all delivery receipts.",
    "8-0": "destination",
    "8-1": "For standard Apple Messages for Business messages, this contains the unique user ID for the recipient. For invitation message delivery receipts, this contains the invited customer's mobile number, when available.",
    "8-2": "`4477362XXXX`",
    "8-3": "Common parameter for all delivery receipts.",
    "9-0": "destinationType",
    "9-1": "For standard Apple Messages for Business messages, this value is `applebusinesschat`. For invitation message delivery receipts, this value is `msisdn`.",
    "9-2": "`msisdn`",
    "9-3": "Common parameter for all delivery receipts.",
    "10-0": "deliveryStatus",
    "10-1": "Status of messages once sent. For invitation messages, supported values include `Submitted` and `Failed`. Apple does not provide delivery or read status events for invitation messages.",
    "10-2": "`Submitted`",
    "10-3": "Common parameter for all delivery receipts.",
    "11-0": "subtid",
    "11-1": "A unique transaction id will be generated as subtid for the flow level transactions(or node tid)",
    "11-2": "31XXXX6-fXXe-4XX4-aXX8-a6XXXXXXXXc",
    "11-3": "Common parameter for all delivery receipts.",
    "12-0": "transid",
    "12-1": "Unique transaction reference id of the request.",
    "12-2": "f4XXXX7e-5XXb-4XX9-9XXf-3bXXXXXXXf3d",
    "12-3": "Common parameter for all delivery receipts.",
    "13-0": "callbackData",
    "13-1": "Data that you have configured to receive on the notify Url. This is configured as a part of the request.",
    "13-2": "This is callback data.",
    "13-3": "Common parameter for all delivery receipts.",
    "14-0": "correlationid",
    "14-1": "The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
    "14-2": "12XXXX7e-5XXb-4XX9-9XXf-3bXXXXXXX90",
    "14-3": "Common parameter for all delivery receipts.",
    "15-0": "dataIntegration",
    "15-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "15-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "15-3": "Common parameter for all delivery receipts.",
    "16-0": "context",
    "16-1": "The object contains  key-value pairs which are added either by Data Stream admin or in flow.",
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
    "20-1": "Contains the name of the flow",
    "20-2": "Sample Flow",
    "20-3": "Common parameter for all delivery receipts.",
    "21-0": "messagingAPI",
    "21-1": "It is a boolean parameter. If the value is True, the message was sent using messaging API. If the value is False, the message was sent using either flow or rule.",
    "21-2": "true/false",
    "21-3": "Common parameter for all delivery receipts.",
    "22-0": "appContext",
    "22-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "22-2": "“appContext“: {  \n                           “key1”: “value1“,  \n                          “key2”: “value2“  \n}",
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