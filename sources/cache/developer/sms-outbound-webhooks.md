# SMS

Source: https://developers.webexconnect.io/reference/sms-outbound-webhooks
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:45+00:00

Navigate to Integrations -> Outbound Webhooks 

## **SMS Delivery Receipts**

- Select the service you are sending the SMS from
- Select the channel as SMS

```json Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Invalid address",
      "code": "7102",
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189XXXXXXXX",
      "destinationType": "msisdn",
      "deliveryStatus": "Submitted"
    },
    "subtid": "",
    "transid": "7f3af32c-8d6a-XXXX-b1c8-4805135ada71",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Failed (sample 1)
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Invalid Sender ID",
      "code": "7101",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards. 
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Failed"
    },
    "carrier": "", 
    "subtid": "",
    "transid": "3bf586f4-XXXX-4272-8da2-a7161644cebc",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Failed (sample 2)
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Invalid address",
      "code": "7102",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards.
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Failed"
    },
    "carrier": "", 
    "subtid": "",
    "transid": "dba07fc1-0d68-XXXX-ae9f-d7ec539ac832",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Failed (sample 3)
{
 "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Message length exceeded",
      "code": "7107",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards. 
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "91891xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Failed"
    },
    "carrier": "", 
    "subtid": "",
    "transid": "4daf1851-eca4-XXXX-a231-9be44a0f60ce",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Un-Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "<dynamic response>",
      "code": "<dynamic code>",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards.	
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Un-Delivered"
    },
    "carrier": "USTMO",
    "subtid": "",
    "transid": "f7541551-0d9d-XXXX-b68d-1499168e24fb",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Clicked (only for v2)
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "sms",
            "Description": "http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html|192.0.2.1",
            "destinationType": "msisdn",
            "timeStamp": "2022-10-10T13:53:13.749+01:00",
            "additionalInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "code": "7528",
            "deliveryStatus": "Clicked",
            "destination": "4475xxxxxxxx"
        },
        "correlationid": "3bd8edf31c81-4b72d8a2-XXXX-49e2-993e",
        "callbackData": "return callbackdata",
        "transid": "4b72d8a2-290d-XXXX-993e-3bd8edf31c81"
    }
}
```
```json Delivered
{
 "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Delivered",
      "code": "7500",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards. 
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Delivered"
    },
    "carrier": "USTMO", 
    "subtid": "",
    "transid": "7f3af32c-8d6a-XXXX-b1c8-4805135ada71",
    "callbackData": "",
    "correlationid": ""
  }
}
```

**Delivery Receipts Descriptions** 



| Field Name | Description |
| --- | --- |
| timeStamp | Timestamp of the event |
| description | Detailed description of the delivery status. |
| code | Status code as mentioned in the documentation |
| messageCount |  The number of segments in the SMS message. This value will only be returned for Delivered and Failed delivery receipts. _Note: This field will not be available in Canada and India regions_ |
| deliveryChannel | Channel to be used to send message |
| destination | The mobile number to which message will be sent |
| destinationType | This is always msisdn for SMS |
| additionalinfo | Additional info such as details about the browser used to open a link in case of Click events. Please note that Clicked events are tracked only when using shortenLinks with trackClicks set to true via Messaging API v2. Click tracking isn't available for Smart Links at the moment. |
| deliveryStatus | Status of messages once sent |
| carrier | A unique identifier for the carrier. See [SMS Carrier Mapping](https://developers.webexconnect.io/reference/sms-carrier-mapping) for the mapping to the carrier name and country ISO code.  <br>**Note**: The `carrier` field contains the carrier ID where available. |
| subtid | A unique transaction id will be generated as subtid for the flow level transactions(or node tid) |
| transid | Unique transaction reference id of the request |
| callbackData | Data that you have configured to receive on the notify Url. This is configured as a part of the request |
| correlationid | The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request. |
| Submitted | When a message is submitted to the Webex Connect gateway |
| Delivered | Returned when the delivery is completed successfully |
| Un-Delivered | We have different reasons for the un-delivered in the document |
| Failed | We have multiple reasons for the failure of a message  <br>Eg: When the sender ID is invalid.  <br>When the address is invalid more details and error codes are already covered in the document |




> 📘 Note
> 
> If Branded Text is enabled for your client, the  ‘**Attempted Upgrade to**’ and ‘**Upgrade Result**,’ parameters on the SMS Delivered payload will appear as shown below. To enable Branded Text for your number, please refer to the [Branded Text](https://help.webexconnect.io/docs/rcs-branded-text) page for more information.

## **SMS Incoming Messages**

- Navigate to Integrations -> Outbound Webhooks 
- Select the short-code/number that you expect to receive messages on as the 'Entity'
- Select Incoming Message checkbox under 'Which notifications do you want to receive' section
- Configure the URL you would like to receive a notification for incoming messages on under 'Endpoint Configuration' section
- Optionally configure Hub Signature details 
- Click Save

Once done, you'll be notified on the configured URL whenever an incoming message is received on the configured Webex Connect phone number/short code.

```json Incoming Message
{
  "userld": "8765",
  "Channel": "SMS",
  "da": "56263",
  "message_source": "SMS",
  "oa": "XXXXXXXXXX",
  "message": "Incoming Text Message",
  "messageCount": "2",
  "tid": "0044_7826374XXXX",
  "datetime": "2024-01-07T14:36:09.266Z",
  "ts": "2024-01-07T14:36:09.266Z",
  "x_networkid": "USTMO"
}
```

**Incoming Messages Descriptions** 



| Field Name | Descriptions |
| --- | --- |
| channel | Channel is SMS always for incoming SMS |
| oa | Phone number on which the SMS has been received on |
| da | End user phone number from which the message was sent from |
| message_source | Message type |
| message | Message content |
| messageCount | The number of segments in the incoming SMS message. |
| tid | Unique transaction reference id of the request |
| datetime | Timestamp when this message was received on Webex Connect |
| ts | Timestamp when this message was received on Webex Connect |
| x_networkid | A unique identifier for the carrier. See [SMS Carrier Mapping](https://developers.webexconnect.io/reference/sms-carrier-mapping)  for the mapping to the carrier name and country ISO code.  <br>**Note**: The `x_networkid` field contains the carrier ID where available. |




## **Error Codes**

| Error Code | Description                                                   | Status       |
| :--------- | :------------------------------------------------------------ | :----------- |
| 7500       | Returned when the delivery is completed successfully          | Delivered    |
| 7501       | Returned when message is submitted to the gateway             | Submitted    |
| 7004       | Returned when an invalid value or parameters are provided     | Un-Delivered |
| 7006       | Returned when an error occurs in server                       | Un-Delivered |
| 7101       | Returned when the sender ID is invalid                        | Un-Delivered |
| 7102       | Returned when the address is invalid                          | Un-Delivered |
| 7107       | Returned when the message length exceeded 4000 characters     | Un-Delivered |
| 7109       | Returned when the user is registered on Do Not Disturb list   | Un-Delivered |
| 7201       | Returned when the delivery failed at operator                 | Un-Delivered |
| 7202       | Returned when the delivery failed at platform                 | Un-Delivered |
| 7203       | Returned when the subscriber address is not known             | Un-Delivered |
| 7204       | Returned when the subscriber account has insufficient credits | Un-Delivered |
| 7205       | Returned when there is an error in binary message             | Un-Delivered |
| 7206       | Returned when the subscribers SIM is full                     | Un-Delivered |
| 7207       | Returned when the subscriber is out of coverage area          | Un-Delivered |
| 7208       | Returned when message is expired                              | Un-Delivered |
| 7209       | Returned when unable to deliver multi-part message            | Un-Delivered |
| 7210       | Returned when there is an error in billing configuration      | Un-Delivered |
| 7211       | Returned when an error occurs at operator                     | Un-Delivered |

> 📘 Note
> 
> Refer to [SMS - Channel ](https://developers.webexconnect.io/reference/channel-specific-status-codes-1)codes for more information.

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
