**Email - Inbound Message**

The following are the Email inbound message payloads.

```json Inbound Email
{
  "textMessage": "Sent with [Proton Mail](https:\\/\\/proton.me\\/mail\\/home) secure email.",
  "attachments": "[{\"name\":\"Audio_MP3_700kb.mp3\",\"contentType\":\"audio/mpeg\",\"url\":\"https://s3.amazonaws.com/stagingappleattachment/bcd95580-3ea5-49a7-a47f-353ce70fe04a_Audio_MP3_700kb.mp3\"},{\"name\":\"Audio_OGG.ogg\",\"contentType\":\"audio/ogg\",\"url\":\"https://s3.amazonaws.com/stagingappleattachment/f99b20e7-5113-482b-8f7f-5be99205263d_Audio_OGG.ogg\"},{\"name\":\"sample_3gp.3gp\",\"contentType\":\"video/3gpp\",\"url\":\"https://s3.amazonaws.com/stagingappleattachment/ca48ad35-63fc-4859-9b8d-19e01d386378_sample_3gp.3gp\"}]",
  "subject": "Send mail with multiple Attachments",
  "transid": "9c973908-a814-XXXX-a4be-1cd2fcbed08d",
  "channel": "Email",
  "htmlMessage": "<div style=\\\"font-family: Arial, sans-serif; font-size: 14px;\\\"><br><\\/div><div style=\\\"font-family: Arial, sans-serif; font-size: 14px;\\\"><br><\\/div>\\r\\n<div class=\\\"protonmail_signature_block\\\" style=\\\"font-family: Arial, sans-serif; font-size: 14px;\\\">\\r\\n    <div class=\\\"protonmail_signature_block-user protonmail_signature_block-empty\\\">\\r\\n        \\r\\n            <\\/div>\\r\\n    \\r\\n            <div class=\\\"protonmail_signature_block-proton\\\">\\r\\n        Sent with <a target=\\\"_blank\\\" href=\\\"https:\\/\\/proton.me\\/mail\\/home\\\">Proton Mail<\\/a> secure email.\\r\\n    <\\/div>\\r\\n<\\/div>\\r\\n",
  "dataIntegration": [
    {
      "prebuiltId": 51052,
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
      "dataIntegrationid": 50528
    }
  ],
  "appContext": {
    },
  "event_identifier": "MO",
  "userId": "",
  "tid": "9c973908-a814-XXXX-a4be-1cd2fcbed08d",
  "clientUUID": "0d41b41a-a8e8-XXXX-a9fb-24ce5334e18f",
  "x-wx-gtrid": "",
  "channel_identifier": "EMAIL",
  "appId": "a_638651XXXX99190000",
  "tenantId": 8129,
  "from": "testautocisco@protonmail.com",
  "to": "[\"\\\"pavanqa@bayone.webexconnect.in.net\\\" <pavanqa@bayone.webexconnect.in.net>\"]",
  "event": "Inbound Message",
  "ts": "2025-03-25T11:41:42.601+05:30"
}
```
```json Unsubscribe
{
  "transid": "97bc71e9-XXXX-XXXX-ad66-1384a0b2d533",
  "channel": "Email",
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
  "tid": "97bc71e9-29e2-XXXX-XXXX-1384a0b2d533",
  "clientUUID": "0d41b41a-XXXX-XXXX-a9fb-24ce5334e18f",
  "x-wx-gtrid": "",
  "senderId": "jack@smith.webexconnect.in.net",
  "appId": "a_638651XXXX99190000",
  "from": "xyz@yahoo.com",
  "correlationId": "",
  "event": "Unsubscribe",
  "ts": "2025-04-04T12:30:10.340+05:30"
}
```
```json Subscribe
{
  "transid": "a4ca548d-X774-XXX5-XXX7-17386a31e98",
  "channel": "Email",
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
  "tid": "a4ca548d-XXX4-XXX5-XXX7-17386a31e985",
  "clientUUID": "0d41b41a-a8e8-XXXX-XXXX-24ce5334e18f",
  "x-wx-gtrid": "",
  "senderId": "jack@smith.webexconnect.in.net",
  "appId": "a_63865XXXXXX9190000",
  "from": "xyz@yahoo.com",
  "correlationId": "",
  "event": "Subscribe",
  "ts": "2025-04-04T12:30:12.652+05:30"
}
```

**Email - Inbound Message Descriptions**

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Descriptions",
    "h-2": "Example",
    "0-0": "textMessage",
    "0-1": "Contains the text message sent by the user.",
    "0-2": "Hello Customer,  \n  \nThank you for using our services. For any further assistance, please reach us at [support@abc.tld]  \n  \nThanks,  \nTeam ABC",
    "1-0": "attachments",
    "1-1": "Contains the file attachment sent by the user.",
    "1-2": "Audio_MP3_700kb.mp3",
    "2-0": "subject",
    "2-1": "Email subject",
    "2-2": "Send mail with multiple Attachments",
    "3-0": "transid",
    "3-1": "Unique transaction reference id of the request.",
    "3-2": "a4ca548d-X774-XXX5-XXX7-17386a31e985",
    "4-0": "channel",
    "4-1": "Refers to the channel name.\"Email” in this case.",
    "4-2": "Email",
    "5-0": "htmlMessage",
    "5-1": "Email HTML Content",
    "5-2": "\"\\<html xmlns:v=\\\"urn:schemas-microsoft-com:vml\\\" xmlns:o=\\\"urn:schemas-microsoft-com:office:office\\\" \\\\r\\\\n \\***\\*REMOVED FOR READABILITY\\*\\***\"",
    "6-0": "dataIntegration",
    "6-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "6-2": "\"dataIntegration\": {    \"context\":  \n{  \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"  \n},  \n“appContext”: {  \n}  \n}",
    "7-0": "context",
    "7-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "7-2": "\"context\": {  \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"  \n}",
    "8-0": "serviceId",
    "8-1": "Contains the unique reference ID of the service.",
    "8-2": "12345",
    "9-0": "serviceName",
    "9-1": "Contains the name of the service.",
    "9-2": "New Service",
    "10-0": "flowId",
    "10-1": "Contains the unique ID for the flow.",
    "10-2": "54321",
    "11-0": "flowName",
    "11-1": "Contains the name of the flow.",
    "11-2": "Sample Flow",
    "12-0": "messagingAPI",
    "12-1": "Indicates whether the request is sent through messaging API.",
    "12-2": "true/false",
    "13-0": "appContext",
    "13-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "13-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "14-0": "event_identifier",
    "14-1": "Unique Identifier for an event as given by the client.",
    "14-2": "SampleInbound",
    "15-0": "userId",
    "15-1": "Unique customer ID that identifies a customer profile. Populated if used in the flow.",
    "15-2": "",
    "16-0": "tid",
    "16-1": "Transaction Id.",
    "16-2": "a4ca548d-XXX4-XXX5-XXX7-17386a31e985",
    "17-0": "clientUUID",
    "17-1": "Contains the clients unique identification number.",
    "17-2": "0d41b41a-a8e8-XXXX-XXXX-24ce5334e18f",
    "18-0": "senderId",
    "18-1": "Email address used to send the concerned email to the recipient.",
    "18-2": "[jack@smith.webexconnect.in.net]",
    "19-0": "x-wx-gtrid",
    "19-1": "Contains the global transaction ID between cross-products for a given request.",
    "19-2": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
    "20-0": "channel_identifier",
    "20-1": "Unique Identifier for a channel as given by the client.",
    "20-2": "EMAIL",
    "21-0": "appId",
    "21-1": "Contains the application ID.",
    "21-2": "a_63865XXXXXX9190000",
    "22-0": "tenantId",
    "22-1": "Unique tenant ID.",
    "22-2": "",
    "23-0": "from",
    "23-1": "Email ID of the sender.",
    "23-2": "[sender@protonmail.com]",
    "24-0": "to",
    "24-1": "Email ID of the receipent",
    "24-2": "[destination@jack.webexconnect.in.net]",
    "25-0": "event",
    "25-1": "Contains the incoming event type.",
    "25-2": "Subscribe",
    "26-0": "ts",
    "26-1": "Timestamp when MO received to <<prodname>>",
    "26-2": "2025-04-04T12:30:12.652+05:30",
    "27-0": "correlationId",
    "27-1": "The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
    "27-2": "12XXXX7e-5XXb-4XX9-9XXf-3bXXXXXXX90"
  },
  "cols": 3,
  "rows": 28,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Email - Delivery Receipt**

```json Submitted
{
  "x-wx-gtrid": "7c55322b-a0bd-XXXX-XXXX-f4a78b641feb",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2025-03-06T16:45:01.481+05:30",
      "Description": "Submitted",
      "code": "1234",
      "deliveryChannel": "email",
      "additionalInfo": "",
      "destination": "xyz@yahoo.com",
      "destinationType": "email",
      "deliveryStatus": "Submitted"
    },
    "subtid": "",
    "transid": "a00be223-XXXX-XXXX-a602-daaacca5c363",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "serviceId": "54321",
      "serviceName": "New Service",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
    }
  }
}
```
```json Delivered
{
	"x-wx-gtrid": "7c55322b-a0bd-XXXX-XXXX-f4a78b641feb",
	"deliveryInfoNotification": {
		"deliveryInfo": {
			"timeStamp": "2025-03-06T16:45:02.810+05:30",
			"Description": "Delivered",
			"code": "1234",
			"deliveryChannel": "email",
			"additionalInfo": "",
			"destination": "xyz@yahoo.com",
			"destinationType": "email",
			"deliveryStatus": "Delivered"
		},
		"subtid": "",
		"transid": "a00be223-bf3c-XXXX-XXXX-daaacca5c363",
		"callbackData": "",
		"correlationid": ""
	},
	"dataIntegration": {
		"context": {
			"serviceId": "54321",
			"serviceName": "NewService",
			"flowId": "",
			"flowName": "",
			"messagingAPI": "true"
		},
		"appContext": {}
	}
}
```
```json Read
{
	"x-wx-gtrid": "7c55322b-a0bd-XXXX-XXXX-f4a78b641feb",
	"deliveryInfoNotification": {
		"deliveryInfo": {
			"timeStamp": "2025-03-06T16:45:14.928+05:30",
			"Description": "Read",
			"code": "1234",
			"deliveryChannel": "email",
			"additionalInfo": "",
			"destination": "xyz@yahoo.com",
			"destinationType": "email",
			"deliveryStatus": "Read"
		},
		"subtid": "",
		"transid": "a00be223-bf3c-XXXX-XXXX-daaacca5c363",
		"callbackData": "",
		"correlationid": ""
	},
	"dataIntegration": {
		"context": {
			"serviceId": "54321",
			"serviceName": "NewService",
			"flowId": "",
			"flowName": "",
			"messagingAPI": "true"
		},
		"appContext": {}
	}
}
```
```json Clicked
{
  "x-wx-gtrid": "7c55322b-a0bd-XXXX-XXXX-f4a78b641feb",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2025-03-06T16:45:16.911+05:30",
      "Description": "http://www.w3schools.com|72.163.220.5",
      "code": "1234",
      "deliveryChannel": "email",
      "additionalInfo": "Mozilla\\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\\/537.36 (KHTML, like Gecko) Chrome\\/133.0.0.0 Safari\\/537.36",
      "destination": "xyz@yahoo.com",
      "destinationType": "email",
      "deliveryStatus": "Clicked"
    },
    "subtid": "",
    "transid": "a00be223-bf3c-XXXX-XXXX-daaacca5c363",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "serviceId": "54321",
      "serviceName": "NewService",
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
  "x-wx-gtrid": "698c6b7e-572b-XXXX-XXXX-97894550d172",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2025-04-09T17:21:43.514+05:30",
      "Description": "already bounced : bounce@simulator.amazonses.com",
      "code": "1234",
      "deliveryChannel": "email",
      "additionalInfo": "",
      "destination": "bounce@simulator.amazonses.com",
      "destinationType": "email",
      "deliveryStatus": "Failed"
    },
    "subtid": "",
    "transid": "8a97075b-52c0-XXXX-ade4-39e7ac7af43b",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "serviceId": "54321",
      "serviceName": "NewService",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
          }
  }
}
```
```json Complaint
{
  "x-wx-gtrid": "148bf1fd-1746-XXXX-89d9-a0dc032e965a",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2025-04-09T17:25:19.724+05:30",
      "Description": "",
      "code": "7521",
      "deliveryChannel": "email",
      "additionalInfo": "",
      "destination": "complaint@simulator.amazonses.com",
      "destinationType": "email",
      "deliveryStatus": "Complaint"
    },
    "subtid": "",
    "transid": "18480103-bc36-XXXX-bab3-59eb20b346b3",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "serviceId": "31410",
      "serviceName": "BayOneAkTest",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
      "tenant_identifier": "BayOneTestAutomation",
      "Topic": "BayOneDSAutomation",
      "URL": "b-1.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-3.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-2.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096",
      "webhookurl": "https://integrations.imiconnect.co/v1/integration/"
    }
  }
}
```
```json Bounced
{
	"deliveryInfoNotification": {
		"deliveryInfo": {
			"deliveryChannel": "email",
			"Description": "Permanent_General/Permanent_NoEmail/Permanent_Suppressed/Transient_General/Transient_MailboxFull/Transient_MessageTooLarge/Transient_ContentRejected/Transient_AttachmentRejected",
			"destinationType": "email",
			"timeStamp": "2023-02-07T03:51:52.322+05:30",
			"code": "7520",
			"deliveryStatus": "Bounce",
			"destination": "destination@domain.tld",
			"additionalInfo": "5.1.1|failed|smtp; 550-5.1.1 The email account that you tried to reach does not exist. Please try\\n550-5.1.1 double-checking the recipient's email address for typos or\\n550-5.1.1 unnecessary spaces. For more information, go to\\n550 5.1.1  https:\\/\\/support.google.com\\/mail\\/?p=NoSuchUser e16-20020a056402089000b0056023119210si1660773edy.317 - gsmtp"
		},
		"subtid": "",
		"transid": "8a97075b-52c0-XXXX-ade4-39e7ac7af43b",
		"callbackData": "",
		"correlationid": ""
	},
	"dataIntegration": {
		"context": {
			"serviceId": "54321",
			"serviceName": "NewService",
			"flowId": "",
			"flowName": "",
			"messagingAPI": "true"
		},
		"appContext": {}
	}
}
```
```json Not Verified
{
	"deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "email",
            "Description": "Account in sandbox mode. Destination email address is not verified",
            "destinationType": "emailid",
            "timeStamp": "2016-07-21T12:44:23.644",
            "code": "7522",
            "deliveryStatus": "Not Verified",
            "destination": "destination@domain.tld"
		},
		"subtid": "",
		"transid": "8a97075b-52c0-XXXX-ade4-39e7ac7af43b",
		"callbackData": "",
		"correlationid": ""
	},
	"dataIntegration": {
		"context": {
			"serviceId": "54321",
			"serviceName": "NewService",
			"flowId": "",
			"flowName": "",
			"messagingAPI": "true"
		},
		"appContext": {}
	}
}
```
```json Invalid
{
	"deliveryInfoNotification": {
		"deliveryInfo": {
			"timeStamp": "2021-03-04T17:00:07.538Z",
			"Description": "Invalid email address",
			"code": "7523",
			"deliveryChannel": "email",
			"additionalInfo": "",
			"destination": "destination@invalid",
			"destinationType": "email",
			"deliveryStatus": "Failed"
		},
		"subtid": "",
		"transid": "8a97075b-52c0-XXXX-ade4-39e7ac7af43b",
		"callbackData": "",
		"correlationid": ""
	},
	"dataIntegration": {
		"context": {
			"serviceId": "54321",
			"serviceName": "NewService",
			"flowId": "",
			"flowName": "",
			"messagingAPI": "true"
		},
		"appContext": {}
	}
}
```

> 📘 Note
> 
> All the Delivery receipts except “Submitted” are applicable only to Email via Amazon SES and not to Email via SMTP.

**Email - Delivery Receipt Descriptions **

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "x-wx-gtrid",
    "0-1": "Contains the global transaction ID between cross-products for a given request.",
    "0-2": "d7XXXX76-3XXa-4XXe  \n-9XX3-d6XXXXXXXXf9",
    "1-0": "deliveryInfoNotification",
    "1-1": "Delivery info parent object",
    "1-2": "NA",
    "2-0": "deliveryInfo",
    "2-1": "Delivery info child object",
    "2-2": "NA",
    "3-0": "timeStamp",
    "3-1": "Timestamp of the event. The timestamp mentioned in the outbound webhook is as per the timezone of the tenant and not UTC as a standard.",
    "3-2": "2023-03-06T17:53:02.270+05:30",
    "4-0": "Description",
    "4-1": "Detailed description of the delivery status.",
    "4-2": "Submitted",
    "5-0": "code",
    "5-1": "Status code as mentioned in the documentation.",
    "5-2": "1234",
    "6-0": "deliveryChannel",
    "6-1": "Channel used to send the message, i.e., email in this case.",
    "6-2": "email",
    "7-0": "additionalInfo",
    "7-1": "This field contains additional contextual information for certain receipts. For example, it captures the details of device where the email has been clicked at in case of 'Clicked' event. Let's say the click event is received from a user who is using Chrome Browser version 125.0.6422.140 on a 64-bit Windows machine using the WebKit rendering engine, this field may have information like: \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.140 Safari/537.36\".  \n  \nAlternatively, it contains the granular details about the reason behind an email getting bounced in case of bounced emails. Another example is when an email is bounced/rejected by the recipient email service provider such as Gmail because the sender is unauthenticated, additionalInfo field in such cases would contain details about 5.7.26 email errors.",
    "7-2": "Status Code 410",
    "8-0": "destination",
    "8-1": "Unique email ID for the recipient of the message on email",
    "8-2": "[xyz@yahoo.com]",
    "9-0": "destinationType",
    "9-1": "This is always email for Email",
    "9-2": "Email",
    "10-0": "deliveryStatus",
    "10-1": "Status of messages once sent.",
    "10-2": "Submitted",
    "11-0": "subtid",
    "11-1": "A unique transaction id will be generated as subtid for the flow level transactions (or node tid)",
    "11-2": "12XXXX3-fXXe-4XX4-aXX5-a6XXXXXXXXc",
    "12-0": "transid",
    "12-1": "Unique transaction reference id of the request.",
    "12-2": "a00be223-XXXX-XXXX-a602-daaacca5c363",
    "13-0": "callbackData",
    "13-1": "Data that you have configured to receive on the notify Url. This is configured as a part of the request.",
    "13-2": "This is callback data.",
    "14-0": "correlationid",
    "14-1": "The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.",
    "14-2": "12XXXX3e-4XXb-5XX6-7XXf-8bXXXXXXX90",
    "15-0": "dataIntegration",
    "15-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "15-2": "\"dataIntegration\": {    \"context\":  \n{  \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"  \n},  \n“appContext”: {  \n}  \n}",
    "16-0": "context",
    "16-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "16-2": "\"context\": {  \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"  \n}",
    "17-0": "serviceId",
    "17-1": "Contains the unique reference id of the service.",
    "17-2": "54321",
    "18-0": "serviceName",
    "18-1": "Contains the name of the service.",
    "18-2": "NewService",
    "19-0": "flowId",
    "19-1": "Contains the unique ID for the flow.",
    "19-2": "54321",
    "20-0": "messagingAPI",
    "20-1": "It is a boolean parameter. If the value is True, the message was sent using messaging API. If the value is False, the message was sent using either flow or rule.",
    "20-2": "true/false",
    "21-0": "appContext",
    "21-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "21-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}"
  },
  "cols": 3,
  "rows": 22,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Email - Outbound Message**

```json Outbound Email
{
  "attachments": [
    {
      "duration": 5,
      "disposition": "attachment",
      "mediaUrl": "https://www.fileformat.info/format/png/sample/40a6e65ed7fb44bc91a8a52aab47fdd4/MARBLE8.PNG",
      "attachmentType": 2,
      "name": "ImageAttachment",
      "mimeType": "image/png"
    }
  ],
  "subject": "Sample Subject",
  "transid": "5e53b019-14e3-XXXX-XXXX-45c3f6e06202",
  "validateDestination": false,
  "dataIntegration": {
    "context": {
      "Key1": "value 1",
      "Key2": "value 2"
    },
    "appContext": {
    }
  },
  "body": "Hi this is Jack Smith",
  "tid": "5e53b019-14e3-XXXX-XXXX-45c3f6e06202",
  "clientUUID": "0a4a1900-98ef-XXXX-XXXX-5ef0927d6683",
  "smtpHeaders": {
    },
  "appId": "a_637903XXXXX4180000",
  "fromName": "Jack Smith",
  "replyTo": "",
  "from": "sender@gmail.com",
  "x_msg_seq": 0,
  "to": [
    "destination@gmail.com"
  ],
  "serviceKey": "78970095-XXXX-XXX-XXXX-12dae3d9be6b",
  "serviceId": 67891
}
```

**Email - Outbound Message Descriptions **

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "attachments",
    "0-1": "Email attachment details",
    "0-2": "disposition and mediaUrl",
    "1-0": "disposition",
    "1-1": "It is present for email with attachments",
    "1-2": "attachment",
    "2-0": "mediaUrl",
    "2-1": "Direct URL pointing to the media file.",
    "2-2": "\"<https://www.fileformat.info/format/png/sample/40a6e65ed>  \n7fb44bc91a8a52aab47fdd4/MARBLE8.PNG\"",
    "3-0": "name",
    "3-1": "Name of the attachments",
    "3-2": "ImageAttachment",
    "4-0": "mimeType",
    "4-1": "Mime type of the attachment that is being sent. For example, \"image/png\".",
    "4-2": "image/png",
    "5-0": "subject",
    "5-1": "Subject of the email.",
    "5-2": "Sample Subject",
    "6-0": "transid",
    "6-1": "Unique transaction reference ID of the request.",
    "6-2": "5e53b019-14e3-XXXX-XXXX-45c3f6e06202",
    "7-0": "validateDestination",
    "7-1": "System variable.",
    "7-2": "False",
    "8-0": "dataIntegration",
    "8-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "8-2": "\"dataIntegration\": {    \"context\":  \n{  \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"  \n},  \n“appContext”: {  \n}  \n}",
    "9-0": "context",
    "9-1": "The object contains key-value pairs which are added either by Data Stream admin or in flow.",
    "9-2": "\"context\": {  \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"  \n}",
    "10-0": "appcontext",
    "10-1": "The object is added as key-value pair either by Data Stream admin or in flow.",
    "10-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "11-0": "body",
    "11-1": "Contains the information sent by the user.",
    "11-2": "Hi this is Jack Smith",
    "12-0": "tid",
    "12-1": "Transaction I",
    "12-2": "5e53b019-14e3-XXXX-XXXX-45c3f6e06202",
    "13-0": "clientUUID",
    "13-1": "Contains the clients unique identification number.",
    "13-2": "0a4a1900-98ef-XXXX-XXXX-5ef0927d6683",
    "14-0": "smtpHeaders",
    "14-1": "Includes SMTP header parameters and values at the time of sending email.",
    "14-2": "In-Reply-To",
    "15-0": "appId",
    "15-1": "Contains the application ID.",
    "15-2": "a_637903XXXXX4180000",
    "16-0": "fromName",
    "16-1": "Name of the sender. A string that will appear next to the from address in most email inboxes.",
    "16-2": "Jack Smith",
    "17-0": "replyTo",
    "17-1": "Reply path for the email when the customer responds",
    "17-2": "[operations@domain.tld]",
    "18-0": "from",
    "18-1": " Email ID of the sender",
    "18-2": "[sender@gmail.com]",
    "19-0": "x_msg_seq",
    "19-1": "This parameter represents whether the request should process sequence or not",
    "19-2": "0",
    "20-0": "to",
    "20-1": "Recipient's Email ID",
    "20-2": "[destination@gmail.com]",
    "21-0": "serviceKey",
    "21-1": "Unique identification number for the service.",
    "21-2": "78970095-XXXX-XXX-XXXX-12dae3d9be6b",
    "22-0": "serviceId",
    "22-1": "Contains the unique reference ID of the service.",
    "22-2": "12345"
  },
  "cols": 3,
  "rows": 23,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]