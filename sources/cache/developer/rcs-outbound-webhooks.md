# RCS

Source: https://developers.webexconnect.io/reference/rcs-outbound-webhooks
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:45+00:00

Navigate to Integrations -> Outbound Webhooks 

## RCS Delivery Receipts

- Select the service you are sending the RCS messages from
- Select the channel as RCS

```json Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2019-10-17T14:14:30.495-04:00",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "rcs",
      "additionalInfo": "",
      "destination": "+1781XXXX832",
      "destinationType": "msisdn",
      "deliveryStatus": "Submitted"
    },
    "carrier": "8",
    "subtid": "c74fd072-7ed7-XXXX-XXXX-66a3b6f06dd6",
    "transid": "c74fd072-7ed7-XXXX-XXXX-66a3b6f06dd6",
    "callbackData": "",
    "serviceProvider": "GOOGLE",
    "correlationid": ""
  }
}
```
```json Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2019-10-17T14:14:35.981-04:00",
      "Description": "Delivered",
      "code": "7500",
      "deliveryChannel": "rcs",
      "additionalInfo": "",
      "destination": "+91XXXXXXXXXX",
      "destinationType": "",
      "deliveryStatus": "Delivered"
    },
    "carrier": "8",
    "subtid": "c74fd072-7ed7-XXXX-XXXX-66a3b6f06dd6",
    "transid": "c74fd072-7ed7-XXXX-XXXX-66a3b6f06dd6",
    "callbackData": "",
    "serviceProvider": "GOOGLE",
    "correlationid": ""
  }
}
```
```json Read
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2019-10-17T14:14:39.124-04:00",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "rcs",
      "additionalInfo": "",
      "destination": "+91XXXXXXXXXX",
      "destinationType": "",
      "deliveryStatus": "Read"
    },
    "carrier": "8",
    "subtid": "c74fd072-7ed7-XXXX-XXXX-66a3b6f06dd6",
    "transid": "c74fd072-7ed7-XXXX-XXXX-66a3b6f06dd6",
    "callbackData": "",
    "serviceProvider": "GOOGLE",
    "correlationid": ""
  }
}
```
```json Failed
{
    "deliveryInfoNotification": 
       {
          "deliveryInfo": 
             {
                "timeStamp": "2020-04-24T12:56:30.439Z",
                "Description": "Service provider exception.",
                "code": "7010",
                "deliveryChannel": "rcs",
                "additionalInfo": "Unable to determine service provider for recipient: +9163xxxxxxxx carrier: Reliance (JIO) and protocol:RCS",
                "destination": "XXXXXXXXXXX",
                "destinationType": "msisdn",
                "deliveryStatus": "Failed"
             },
          "subtid": "",
          "transid": "1ea5cd99-6cac-XXXX-XXXX-ffa42244842f",
          "callbackData": "",
          "correlationid": "40d93325-4651-XXXX-XXXX-fe9aff7dda3f"
       }
}
```

### RCS Incoming Messages & Events

- Select the app that you expect to receive messages or events from as the Entity

```json Incoming Message
{
   "channel":"rcs",
   "msisdn":"+91630XXXX252",
   "message":"RCS",
   "appId":"a_1570171XXXX6805250",
   "event":"MO",
   "ts":"2019-10-23T02:10:49.466-03:00",
   "tid":"42392840-09c2-XXXX-XXXX-8676413befe1",
   "serviceProvider":"GOOGLE",
   "carrier":"8",
   "messageid":"ndzkbkvuXXXXnjg3w424tyorja"
}
```
```json Incoming Attachment
{
    "channel": "rcs",
    "msisdn": "+91630XXXX252",
    "appId": "a_1570171XXXX6805250",
    "event": "ATTACHMENT",
    "ts": "2019-10-21T06:28:15.644-03:00",
    "tid": "471957e9-c5e8-XXXX-XXXX-2141e66acc35",
    "serviceProvider": "GOOGLE",
    "carrier": "N/A",
    "attachments": "[{\"payload\":{\"url\":\"https://rcs-user-content-us.storage.googleapis.com/407b434c-ea2a-4d24-9e73-d5c1dbf0f5f7/0f37f034c3764ac3400adc09b5307df91ca31a47b2ef229fc59588537902\"},\"type\":\"video\"}]",
    "messageid": "uo53ledr7fXXXXj7nfztguulse"  
}
```
```json Location
{
   "channel":"rcs",
   "msisdn":"+91630XXXX252",
   "appId":"a_1570171XXXX6805250",
   "event":"Location",
   "ts":"2019-10-17T14:34:58.808+03:00",
   "tid":"475794b6-8bdb-XXXX-XXXX-e20bae8c11a3",
   "serviceProvider":"GOOGLE",
   "carrier":"N/A",
   "latitude":"17.434679",
   "longitude":"78.3985752",
   "messageId": "zygwbhiu5zXXXX7bwluuhgkqn4"
}
```
```json Postback
{
    "channel": "rcs",
    "msisdn": "+91630XXXX252",
    "postback": "Yes",
    "appId": "a_1570171XXXX6805250",
    "event": "postback",
    "ts": "2020-08-05T04:44:17.179-05:00",
    "tid": "63736533-6312-XXXX-XXXX-1654c51af8a3",
    "serviceProvider": "GOOGLE",
    "carrier": "N/A",
    "messageId": "ty55gvyXXXXjjjj4wxzgoigzi"
}
```
```json Subscribe
{
"channel": "rcs",
"msisdn": "+9196XXXX269",
"appId": "a_172828XXXXX4801150",
"event": "SUBSCRIBE",
"ts": "2025-10-28T15:41:39.367+05:30",
"tid": "f610d8c1-4886-XXXX-XXXX-ca9502203251",
"serviceProvider": "GOOGLE",
"carrier": "573",
"messageId": "cskzaf7pkrcXXXXX4t75kgybru"
}
```
```json Unsubscribe
{
    "channel": "rcs",
    "msisdn": "+9196XXXX9269",
    "appId": "a_1728283XXXXX801150",
    "event": "UNSUBSCRIBE",
    "ts": "2025-10-28T15:41:36.257+05:30",
    "tid": "229211c0-0490-XXXX-XXXX-ca6fe0afbacb",
    "serviceProvider": "GOOGLE",
    "carrier": "573",
    "messageId": "nmdjaakztXXXXX3zfah5reqa3i"
}
```

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
