# Live Chat / In-App Messages

Source: https://developers.webexconnect.io/reference/live-chat-in-app-messages-outbound-webhooks
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:44+00:00

You can configure Outbound Webhooks to receive a copy of delivery status notifications for Live Chat/In-App Messaging channel and for a copy of incoming messages/events by navigating to 'Assets -> Integrations -> Outbound Webhooks' sections in the platform. 

## Outbound Webhook configuration for tracking Live Chat/In-App message delivery status.

If you want to track message delivery status, select the Webex Connect Service you are sending the Live Chat/In-App Messages from under 'Entity' dropdown.

```json Submitted
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2024-02-12T06:38:46.939+01:00",
            "Description": "Submitted",
            "code": "7501",
            "deliveryChannel": "rt",
            "additionalInfo": "",
            "destination": "97XX90",
            "destinationType": "customerid",
            "deliveryStatus": "Submitted"
        },
        "subtid": "b8a3050d-xxxx-4ccf-9a99-853ac8386ccb",
        "transid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
        "callbackData": "",
        "correlationid": ""
    }
}
```
```json Delivered
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2024-02-12T06:38:48.519+01:00",
            "Description": "Delivered",
            "code": "7500",
            "deliveryChannel": "rt",
            "additionalInfo": "",
            "destination": "97XX90",
            "destinationType": "customerid",
            "deliveryStatus": "Delivered"
        },
        "subtid": "b8a3050d-xxxx-4ccf-9a99-853ac8386ccb",
        "transid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
        "callbackData": "",
        "correlationid": ""
    }
}
```
```json Read
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2024-02-12T06:38:49.101+01:00",
            "Description": "Read",
            "code": "7502",
            "deliveryChannel": "rt",
            "additionalInfo": "",
            "destination": "97XX90",
            "destinationType": "customerid",
            "deliveryStatus": "Read"
        },
        "subtid": "b8a3050d-xxxx-4ccf-9a99-853ac8386ccb",
        "transid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
        "callbackData": "",
        "correlationid": ""
    }
}
```
```json Failed
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-14T18:53:12.196+05:30",
      "pushId": "",
      "Description": "Invalid thread id",
      "code": "7312",
      "deliveryChannel": "rt",
      "destination": "97XX90",
      "destinationType": "userid",
      "deviceid": "",
      "deliveryStatus": "Failed"
    },
    "subtid": "b8a3050d-xxxx-4ccf-9a99-853ac8386ccb",
    "transid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Clicked
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-14T23:01:08.741+05:30",
      "Description": "Clicked",
      "code": "7528",
      "subtid": "b8a3050d-xxxx-4ccf-9a99-853ac8386ccb",
      "deliveryChannel": "rt",
      "transid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
      "callbackData": "",
      "destination": "97XX90",
      "interactiveData": {
        "identifier": "1",
        "type": "webUrl",
        "title": "View Item",
        "url": ""
      },
      "destinationType": "userid",
      "correlationid": "",
      "deliveryStatus": "Clicked"
    }
  }
}
```
```json Interactive-Read (Deprecated)
{
    
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "appmessaging",
            "Description": "Read",
            "destinationType": "customerid",
            "timeStamp": "2016-07-22T11:22:50.065",
            "code": "7502",
            "deliveryStatus": "Read",
            "deviceid": "355004057394234",
            "destination": "9876",
            "interaction": {
               "Button_Pressed": "SUBSCRIBE",
               "MessageRef": "123252445"
            }
        },
        "correlationid": "0322-4874-XXXX-560292c115cb-3f8e656c",
        "callbackData": "return callbackdata",
        "transid": "3f8e656c-0322-XXXX-96e8-560292c115cb"
    }
}
```

| Field Name      | Description                                                                                                                                                                          |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timeStamp       | Timestamp of the event                                                                                                                                                               |
| Description     | Detailed description of the delivery status                                                                                                                                          |
| code            | Message delivery status code                                                                                                                                                         |
| deliveryChannel | This is “rt” in case of Live Chat and In-App Messaging delivery receipts                                                                                                             |
| additionalInfo  | Additional contextual information                                                                                                                                                    |
| destination     | This contains the destination value. E.g., userid of the recipient the message was sent to.                                                                                          |
| destinationType | Describes the destination type used for sending the message. E.g., userid.                                                                                                           |
| deliveryStatus  | Message delivery status                                                                                                                                                              |
| subtid          | Transaction id of the node used for sending the message. Applies to messages sent using channel specific nodes in a flow. This value isn't populated for Messaging API transactions. |
| transid         | Unique transaction reference id of the request                                                                                                                                       |
| callbackData    | Data that you have configured to receive on the notify URL. This is configured as a part of the request                                                                              |
| correlationid   | The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request          |

## Outbound Webhook configuration for tracking incoming Live Chat/In-App Messages or Events

If you want to track incoming messages and events on Live Chat and In-App channels, select the app asset you are sending and receiving the Live Chat/In-App Messages from under 'Entity' dropdown.

```json Incoming Message
{
    "userId": "4657",
    "channel": "Rtm",
    "appId": "SD12xxxx50",
    "event": "MO",
    "message": "motext",
    "ts": "2024-09-xxxx:36:55.099+05:30",
    "tid": "74f09963-xxxx-4be5-bdc6-b3c952f5d081",
    "attachments": "",
    "replyTo": "",
    "clientId": "SD12xxxx50/xxxx/V2_00c82xxxx6b32aa9",
    "thread_id": "4b092634-a8eb-xxxx-996b-29ebaded4970",
    "thread_title": "Electronics",
    "thread": "{\"updated_on\":\"2024-09-1xxxxx:06:51.213Z\",\"created_on\":\"2024-09-1xxxxx:06:51.213Z\",\"extras\":{\"icFirstName\":\"John\",\"icLastName\":\"Doe\"},\"id\":\"4b092634-a8eb-xxxx-996b-29ebaded4970\",\"title\":\"Electronics\",\"type\":\"Conversation\",\"category\":\"Electronics\",\"unread_msg_count\":0,\"status\":\"Active\"}",
    "extras": "",
    "pciInfo": "{\"droppedAttachmentCount\":0,\"isPCICompliance\":true,\"isPCIValidationDone\":true,\"isAttachmentEnabled\":true,\"nonPCIComplianceReason\":{}}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
    "malwareinfo": "{\"isMalwareValidationDone\":\"NA\",\"droppedAttachmentCount\":\"NA\",\"isMalwareCompliance\":\"NA\",\"malwareFailedReason\":\"NA\"}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
    "securityscaninfo": "{\"droppedAttachmentCount\":0,\"isSecurityCompliance\":true,\"securityFailedReason\":{},\"isSecurityValidationDone\":true}" //Applicable only for Webex CC and CCE integrated Webex Connect tenants
}
```
```json Registration Request
{
  "userId": "97XX90",
  "channel": "Rtm",
  "appId": "MU20XX1001",
  "event": "OnProfileCreate",
  "ts": "2024-02-13T17:32:18.186+05:30",
  "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f"
}
```
```json Profile Update
{
  "userId": "",
  "channel": "Rtm",
  "appId": "MU20XX1001",
  "event": "OnProfileUpdate",
  "ts": "2024-02-15T15:32:28.288+05:30",
  "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f"
}
```
```json Form Response
{
    "relatedTid": "R4b07b11e-2c4b-4e25-b435-be5be8bc69e0",
    "userId": "97XX90",
    "channel": "Rtm",
    "appId": "MU20XX1001",
    "event": "OnFormResponse",
    "message": "",
    "ts": "2024-02-12T06:57:06.747+01:00",
    "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
    "attachments": "[{\"templateType\":\"form\",\"payload\":{\"fields\":[{\"name\":\"Name\",\"description\":\"enter name\",\"label\":\"Name\",\"type\":\"text\",\"value\":\"Naga\",\"mandatory\":false},{\"name\":\"Email\",\"description\":\"email\",\"label\":\"Email\",\"type\":\"email\",\"value\":\"enagarjun.1@gmail.com\",\"mandatory\":false},{\"name\":\"Gender\",\"label\":\"Gender\",\"type\":\"dropdown\",\"value\":\"Male\",\"mandatory\":false}],\"title\":\"Student Form\"},\"templateId\":\"0W1XPWN2ND\",\"contentType\":\"template\"}]",
    "replyTo": "",
    "pciInfo": "{\"droppedAttachmentCount\":0,\"isPCICompliance\":true,\"isPCIValidationDone\":true,\"isAttachmentEnabled\":true,\"nonPCIComplianceReason\":{}}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
    "malwareinfo": "{\"isMalwareValidationDone\":\"NA\",\"droppedAttachmentCount\":\"NA\",\"isMalwareCompliance\":\"NA\",\"malwareFailedReason\":\"NA\"}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
    "securityscaninfo": "{\"droppedAttachmentCount\":0,\"isSecurityCompliance\":true,\"securityFailedReason\":{},\"isSecurityValidationDone\":true}" //Applicable only for Webex CC and CCE integrated Webex Connect tenants

}
```
```json Postback for Quick Replies
{
  "userId": "97XX90",
  "channel": "Rtm",
  "appId": "MU20XX1001",
  "event": "OnPostback",
  "message": "Yes",
  "ts": "2024-02-13T18:55:12.126+05:30",
  "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
  "attachments": "",
  "replyTo": "",
  "interactiveData": "{\"reference\":\"Test\",\"identifier\":\"12345xxxxx987654\",\"type\":\"quickReplyPostback\",\"title\":\"Yes\"}",
  "clientId": "SD12xxxx50/xxxx/V2_00c82xxxx6b32aa9",
  "thread_id": "4b092634-a8eb-xxxx-996b-29ebaded4970",
  "thread_title": "Electronics",
  "thread": "{\"updated_on\":\"2024-09-1xxxxx:06:51.213Z\",\"created_on\":\"2024-09-1xxxxx:06:51.213Z\",\"extras\":{\"icFirstName\":\"John\",\"icLastName\":\"Doe\"},\"id\":\"4b092634-a8eb-xxxx-996b-29ebaded4970\",\"title\":\"Electronics\",\"type\":\"Conversation\",\"category\":\"Electronics\",\"unread_msg_count\":0,\"status\":\"Active\"}",
  "extras": "{\"customtags\":{\"key1\":\"value1\",\"key2\":\"value2\"}}",
  "pciInfo": "{\"droppedAttachmentCount\":0,\"isPCICompliance\":true,\"isPCIValidationDone\":true,\"isAttachmentEnabled\":true,\"nonPCIComplianceReason\":{}}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
  "malwareinfo": "{\"isMalwareValidationDone\":\"NA\",\"droppedAttachmentCount\":\"NA\",\"isMalwareCompliance\":\"NA\",\"malwareFailedReason\":\"NA\"}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
  "securityscaninfo": "{\"droppedAttachmentCount\":0,\"isSecurityCompliance\":true,\"securityFailedReason\":{},\"isSecurityValidationDone\":true}" //Applicable only for Webex CC and CCE integrated Webex Connect tenants
}
```
```json Postback for Generic Template
{
  "userId": "97XX90",
  "channel": "Rtm",
  "appId": "MU20XX1001",
  "event": "OnPostback",
  "message": "Buy Now",
  "ts": "2024-02-13T18:56:59.797+05:30",
  "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
  "attachments": "",
  "replyTo": "",
  "interactiveData": "{\"reference\":\"Test\",\"identifier\":\"1234567890\",\"type\":\"templatePostback\",\"title\":\"Buy Now\"}",
  "clientId": "SD12xxxx50/xxxx/V2_00c82xxxx6b32aa9",
  "thread_id": "4b092634-a8eb-xxxx-996b-29ebaded4970",
  "thread_title": "Electronics",
  "thread": "{\"updated_on\":\"2024-09-1xxxxx:06:51.213Z\",\"created_on\":\"2024-09-1xxxxx:06:51.213Z\",\"extras\":{\"icFirstName\":\"John\",\"icLastName\":\"Doe\"},\"id\":\"4b092634-a8eb-xxxx-996b-29ebaded4970\",\"title\":\"Electronics\",\"type\":\"Conversation\",\"category\":\"Electronics\",\"unread_msg_count\":0,\"status\":\"Active\"}",
  "extras": "{\"customtags\":{\"key1\":\"value1\",\"key2\":\"value2\"}}",
  "pciInfo": "{\"droppedAttachmentCount\":0,\"isPCICompliance\":true,\"isPCIValidationDone\":true,\"isAttachmentEnabled\":true,\"nonPCIComplianceReason\":{}}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
  "malwareinfo": "{\"isMalwareValidationDone\":\"NA\",\"droppedAttachmentCount\":\"NA\",\"isMalwareCompliance\":\"NA\",\"malwareFailedReason\":\"NA\"}", //Applicable only for Webex CC and CCE integrated Webex Connect tenants
  "securityscaninfo": "{\"droppedAttachmentCount\":0,\"isSecurityCompliance\":true,\"securityFailedReason\":{},\"isSecurityValidationDone\":true}" //Applicable only for Webex CC and CCE integrated Webex Connect tenants
}
```
```json Typing Start
{
  "userId": "97XX90",
  "channel": "Rtm",
  "appId": "MU20XX1001",
  "event": "TypingIndicator",
  "type": "typingStart",
  "message": "Typing Start",
  "ts": "2024-02-13T18:55:12.126+05:30",
  "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
  "clientId": "SD12xxxx50/xxxx/V2_00c82xxxx6b32aa9",
  "thread_id": "4b092634-a8eb-xxxx-996b-29ebaded4970",
  "thread_title": "Electronics",
  "thread": "{\"updated_on\":\"2024-09-1xxxxx:06:51.213Z\",\"created_on\":\"2024-09-1xxxxx:06:51.213Z\",\"extras\":{\"icFirstName\":\"John\",\"icLastName\":\"Doe\"},\"id\":\"4b092634-a8eb-xxxx-996b-29ebaded4970\",\"title\":\"Electronics\",\"type\":\"Conversation\",\"category\":\"Electronics\",\"unread_msg_count\":0,\"status\":\"Active\"}",
  "extras": "",
  }
```
```json Typing Stop
{
  "userId": "97XX90",
  "channel": "Rtm",
  "appId": "MU20XX1001",
  "event": "TypingIndicator",
  "type": "typingStop",
  "message": "Typing Start",
  "ts": "2024-02-13T18:55:12.126+05:30",
  "tid": "2054f89f-yyyy-40d5-b08f-2ae89e45a94f",
  "clientId": "SD12xxxx50/xxxx/V2_00c82xxxx6b32aa9",
  "thread_id": "4b092634-a8eb-xxxx-996b-29ebaded4970",
  "thread_title": "Electronics",
  "thread": "{\"updated_on\":\"2024-09-1xxxxx:06:51.213Z\",\"created_on\":\"2024-09-1xxxxx:06:51.213Z\",\"extras\":{\"icFirstName\":\"John\",\"icLastName\":\"Doe\"},\"id\":\"4b092634-a8eb-xxxx-996b-29ebaded4970\",\"title\":\"Electronics\",\"type\":\"Conversation\",\"category\":\"Electronics\",\"unread_msg_count\":0,\"status\":\"Active\"}",
  "extras": "",
  }
```

> 📘 Note
> 
> - Typing Indicator is not available as part of the Live Chat/In-App message node.
> - Typing Indicator are included in the TPS limits for the Messaging API.

| Field Name       | Description                                                                                                                                                                                                                                                        |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userId           | User ID of the sender of the incoming message                                                                                                                                                                                                                      |
| channel          | This is “Rtm” in case of Live Chat and In-App Messaging incoming messages.                                                                                                                                                                                         |
| appId            | App ID of the mobile/web asset configured in Webex Connect                                                                                                                                                                                                         |
| event            | Type of the event. E.g., MO for incoming message, and OnProfileCreate for profile creation.                                                                                                                                                                        |
| message          | Content of the incoming message or response to an interactive outbound message such as quick reply messages                                                                                                                                                        |
| ts               | Timestamp                                                                                                                                                                                                                                                          |
| tid              | Unique transaction id                                                                                                                                                                                                                                              |
| attachments      | Details of the attachments received                                                                                                                                                                                                                                |
| client_id        | The unique identifier of the client                                                                                                                                                                                                                                |
| thread_id        | The unique identifier created when creating a thread for a given app ID. It is a mandatory parameter to send messages to user(s).                                                                                                                                  |
| thread_title     | Specifies the title of the thread                                                                                                                                                                                                                                  |
| thread           | All relevant details pertaining to the thread creation.                                                                                                                                                                                                            |
| extras           | You can send additional information along with the message, such as some user-specific property, or any custom parameter that is required to display the message in a certain manner within the app. This information can be sent in the form of extra parameters. |
| pciInfo          | Captures the details of the PCI compliance checks applied to the incoming message and attachments. This is available only for Webex CC and CCE integrated Webex Connect tenants.                                                                                   |
| malwareinfo      | Captures the details of the Malware checks applied to the incoming message and attachments. This is available only for Webex CC and CCE integrated Webex Connect tenants.                                                                                          |
| securityscaninfo | Captures the details of the Security Scans applied to the incoming message and attachments. This is available only for Webex CC and CCE integrated Webex Connect tenants.                                                                                          |

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "results": {
    "codes": [
      {
        "status": 200,
        "language": "json",
        "code": "{}",
        "name": ""
      },
      {
        "status": 400,
        "language": "json",
        "code": "{}",
        "name": ""
      }
    ]
  },
  "auth": "required",
  "params": [],
  "url": "",
  "method": "get",
  "examples": {
    "codes": []
  }
}
```
