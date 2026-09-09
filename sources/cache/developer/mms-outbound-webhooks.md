# MMS

Source: https://developers.webexconnect.io/reference/mms-outbound-webhooks
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:44+00:00

You can configure Outbound Webhooks to receive a copy of delivery notifications for MMS and for a copy of incoming MMS messages by navigating to 'Assets -> Integrations -> Outbound Webhooks' sections in the platform.

## Outbound Webhook configuration for tracking message delivery status

If you want to track message delivery status, select the Webex Connect Service you are sending the MMS messages from under 'Entity' dropdown. Select the channel as MMS.

```json Submitted
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2021-07-28T05:37:56.583Z",
            "Description": "Submitted",
            "code": "7501",
            "deliveryChannel": "mms",
            "additionalInfo": "",
            "destination": "+1650XXXX091",
            "destinationType": "msisdn",
            "sentAs": "MMS",
            "deliveryStatus": "Submitted"
        },
        "subtid": "",
        "transid": "9d257966-11ee-XXXX-984c-3ea6d3970897",
        "callbackData": "mmstest",
        "correlationid": "na1b2b1i1"
    }
}
```
```json Delivered
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2021-07-28T05:39:02.673Z",
            "Description": "Delivered",
            "code": "7500",
            "deliveryChannel": "mms",
            "additionalInfo": "",
            "destination": "+1650XXXX091",
            "destinationType": "msisdn",
            "sentAs": "MMS",
            "deliveryStatus": "Delivered"
        },
        "subtid": "",
        "transid": "9d257966-11ee-XXXX-984c-3ea6d3970897",
        "callbackData": "mmstest",
        "correlationid": "na1b2b1i1"
    }
}
```
```json Failed
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2021-07-28T05:45:28.761Z",
            "Description": "Message failed at vendor",
            "code": "7267",
            "deliveryChannel": "mms",
            "additionalInfo": "",
            "destination": "+16508635091",
            "destinationType": "msisdn",
            "sentAs": "MMS",
            "deliveryStatus": "Failed"
        },
        "subtid": "",
        "transid": "996c998b-c83a-XXXX-86e3-c6942ce34718",
        "callbackData": "suneelmmstest",
        "correlationid": "na1b2b1i1"
    }
}
```

## Outbound Webhook configuration for tracking incoming MMS messages

If you want to track incoming messages, select the MMS asset you are receiving the messages on under 'Entity' dropdown. 

```json Incoming Message
{
   "channel": "MMS",
   "da": "34343",
   "oa": "16502813641",
   "message": "[{\"file\":\"http://qa-sfeui.imimobile.net/dvp-cfdforms/link/34343/d166a619-2e17-4791-8216-819dca0b9b27/EXyTXJQo.jpg\"},{\"file\":\"http://qa-sfeui.imimobile.net/dvp-cfdforms/link/34343/da77ed72-2d91-45a3-9c23-4550d9ef7794/EXyTXJQo.smil\"}]",
   "tid": "8731ca89-d9a6-4a78-835c-7b7957dd0883",
   "ts": "2021-03-22T05:09:23.925Z"
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
