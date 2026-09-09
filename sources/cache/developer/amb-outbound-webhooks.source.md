You can configure Outbound Webhooks to receive a copy of submission notifications for Apple Messages and for a copy of incoming Apple Messages/Events by navigating to 'Assets -> Integrations -> Outbound Webhooks' sections in the platform.

Apple Messages for Business invitation messages support outbound webhook notifications for invitation submission status and invitation response events. For invitation message submissions, Webex Connect sends submission success or failure notifications using the existing `deliveryInfoNotification` payload. For invitation responses, Webex Connect sends an invitation response event when the customer responds to the invitation.

## Outbound Webhook configuration for tracking message status

If you want to track message submission status, select the <<prodname>> Service you are sending the Apple messages from under 'Entity' dropdown. 

> 📘 Note
> 
> Apple Messages for Business invitation messages do not support delivery or read status events. Webex Connect provides submission success or failure notifications.  
> Hence, the DRs are limited to confirmed successful submission of message from Webex Connect to Apple Messages for Business platform.

```json Submitted
{
    "deliveryInfoNotification": {
        "subtid": "85c4aea8-66f0-XXXX-8045-c443f7d1a178",
        "deliveryInfo": {
            "deliveryChannel": "applebusinesschat",
            "Description": "Submitted",
            "destinationType": "applebusinesschat",
            "timeStamp": "2019-03-03T06:52:59.311Z",
            "code": "7501",
            "additionalInfo": "",
            "deliveryStatus": "Submitted",
            "destination": "urn:mbid:AQAAY45PVG4jg/ni/q6rWSYuu9d7Ga6K22bxp0iUmPkdOwxr3yAbisjOmtYFzw6LjDqhABFFHD/nFz6S2U5rBEcSqO7Eg0B5ikXukFD/x+6hPeOuR0Bvb3JDbU24DLlT/E5Yj9aBzFVASwfwStWnuGMX/+FXmAs="
        },
        "correlationid": "",
        "callbackData": "",
        "transid": "00dff89a-4feb-XXXX-8742-3847933492bb"
    }
}
```
```json Failed
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2023-03-14T14:20:09.383+05:30",
            "Description": "Invalid application details",
            "code": "7314",
            "deliveryChannel": "applebusinesschat",
            "additionalInfo": "Please enable new authentication in the Manage Asset Screen",
            "destination": "urn:mbid:AQAAY0qk7se2RMvKV9a/SriP43hSxnu5x2037uBBwERxxYGcZre87nQA41kRlQ+XLPwZUMINkCPa1G1CDesG8kyZNJ+LtyuIBgsn3BHypDNTnV1rn66cO6OuJOnGMfgGnqVDt8bdKJ9UQdwtG5CSBaQwANJjvCI=",
            "destinationType": "applebusinesschat",
            "deliveryStatus": "Failed"
        },
        "subtid": "",
        "transid": "f7a31230-dd19-XXXX-b60b-983a094bd70d",
        "callbackData": "callback4322",
        "correlationid": "correl123"
    }
  )
```

## Invitation Message Submission Notifications

For Apple Messages for Business invitation messages, Webex Connect sends submission success or failure notifications using the existing `deliveryInfoNotification` structure. The `destination` field contains the invited customer's mobile number when available.

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
  "deliveryInfoNotification": {
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
    "subtid": "85c4aea8-66f0-XXXX-8045-c443f7d1a178",
    "transid": "f7a31230-dd19-XXXX-b60b-983a094bd70d",
    "callbackData": "customer-context",
    "correlationid": "corr-12345"
  }
}
```

| Field Name      | Description                                                                                                                                                                                                    |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| subtid          | A unique transaction id will be generated as subtid for the flow level transactions(or node tid)                                                                                                               |
| deliveryChannel | Channel used to send the message i.e., Apple Messages for Business in this case.                                                                                                                               |
| Description     | Detailed description of the delivery status                                                                                                                                                                    |
| destinationType | For standard Apple Messages for Business messages, this value is `applebusinesschat`. For invitation message submissions, this value is `msisdn`.                                                              |
| timeStamp:      | Timestamp of the event. The timestamp mentioned in the outbound webhook is as per the timezone of the tenant and not UTC as a standard.                                                                        |
| code            | Status code as mentioned in the documentation                                                                                                                                                                  |
| additionalInfo  | Additional information about the transaction.                                                                                                                                                                  |
| deliveryStatus  | Status of messages once sent.                                                                                                                                                                                  |
| destination     | For standard Apple Messages for Business messages, this contains the unique user ID for the recipient. For invitation message submissions, this contains the invited customer's mobile number, when available. |
| correlationid   | The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.                                   |
| callbackData    | Data that you have configured to receive on the notify Url. This is configured as a part of the request.                                                                                                       |
| transid         | Unique transaction reference id of the request.                                                                                                                                                                |

## Outbound Webhook configuration for tracking incoming messages and events

If you want to track incoming messages or responses, select the Apple Messages for Business asset you are sending and receiving the Apple messages from under 'Entity' dropdown.

> 📘 
> 
> The samples below are split into 2 blocks in the interest of space and not categories.

> 📘 List Picker Responses
> 
> Please note that you may receive duplicate responses for the List Picker, if the customer responds through non-iOS Apple devices such as the MacBook.

```json Incoming Text Message
{
  "abcUserId": "urn:mbid:SAMPLeFy8He+XuETx+Z52eprTnbIwCPwO/vlXMYKQuJNKJy7SefjtHMetEmlg9jA18Bg5tjdng92D7xHLPyw56R5XCl8fdIjRxtkPkeC7nt6h7aB3kgIOO1FFOpbVHpIHilAxN0R5NkyLFNKku4mb2O4AncxU30=",
  "channel": "AppleBusinessChat",
  "abcAccountId": "00f67e37-e26a-XXXX-8f1b-a73608a976cf",
  "appId": "a_637818908588360000",
  "event": "MO",
  "ts": "2022-07-26T19:56:51.809+01:00",
  "tid": "d38ba2f4-f81a-XXXX-37f5-882ddb350ce0",
  "message": "Hey",
  "attachments": "",
  "locale": "en_IN",
  "bizGroupId": "",
  "bizIntentId": "",
  "requestIdentifier": "",
  "timestamp": "",
  "capabilities": "",
  "deviceAgent": "",
  "capabilityList": "AUTH%2CLIST%2CTIME%2CQUICK"
}
```
```json Image
{
    "abcUserId": "urn:mbid:AQAAY+muaCxppiRFbNZFEiuJAGjZM9I6qRiQqkXVB2gPRPev57AgWIpx431qaDe/JajE2gtnC861/rnOaYWwHUDv7s/lEjgaXYQw0WINUOeouvEY9xOoRqdIwD1c+PkU/8JsPtlLSZupUty4vjT/LYXhya/nyPM=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "137f8c97-8e00-XXXX-ad8f-56051e485e35",
    "appId": "a_636779XXXX21130000",
    "event": "MO",
    "ts": "2018-11-17T12:23:08.407Z",
    "tid": "f18b67ec-1b11-XXXX-5237-7e56619b1fe1",
    "message": "\ufffc",
    "attachments": "[{\"size\":\"148861\",\"name\":\"5E57E087-5C6B-4FD2-8B06-03F0BB17D188.jpeg\",\"mimeType\":\"image/jpeg\",\"type\":\"image\",\"url\":\"https://s3.amazonaws.com/appleattachment/5E57E087-5C6B-4FD2-8B06-03F0BB17D188.jpeg\"}]",
    "locale": "en_IN",
    "bizGroupId": "",
    "bizIntentId": "",
    "requestIdentifier": "",
    "timestamp": "",
    "capabilities": "",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CQUICK"
}
```
```json Video
{
    "abcUserId": "urn:mbid:AQAAY+muaCxppiRFbNZFEiuJAGjZM9I6qRiQqkXVB2gPRPev57AgWIpx431qaDe/JajE2gtnC861/rnOaYWwHUDv7s/lEjgaXYQw0WINUOeouvEY9xOoRqdIwD1c+PkU/8JsPtlLSZupUty4vjT/LYXhya/nyPM=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "137f8c97-8e00-XXXX-ad8f-56051e485e35",
    "appId": "a_636779XXXX21130000",
    "event": "MO",
    "ts": "2018-11-17T12:19:43.815Z",
    "tid": "59493791-95b8-89f5-XXXX-fd4f3163e3e4",
    "message": "\ufffc",
    "attachments": "[{\"size\":\"8588423\",\"name\":\"IMG_0028.mov\",\"mimeType\":\"video/quicktime\",\"type\":\"video\",\"url\":\"https://s3.amazonaws.com/appleattachment/IMG_0028.mov\"}]",
    "locale": "en_IN",
    "bizGroupId": "",
    "bizIntentId": "",
    "requestIdentifier": "",
    "timestamp": "",
    "capabilities": "",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CQUICK"
}
```
```json Listpicker
{
    "abcUserId": "urn:mbid:AQAAY+muaCxppiRFbNZFEiuJAGjZM9I6qRiQqkXVB2gPRPev57AgWIpx431qaDe/JajE2gtnC861/rnOaYWwHUDv7s/lEjgaXYQw0WINUOeouvEY9xOoRqdIwD1c+PkU/8JsPtlLSZupUty4vjT/LYXhya/nyPM=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "137f8c97-8e00-XXXX-ad8f-56051e485e35",
    "appId": "a_63677951XXXX130000",
    "event": "INTERACTIVERESPONSE",
    "ts": "2018-11-17T12:40:27.185Z",
    "tid": "ce7524f7-bbea-XXXX-15d1-4247c5cb785a",
    "message": "",
    "attachments": "[{\"size\":\"27344\",\"name\":\"jpeg-image-8iEic2.jpeg\",\"mimeType\":\"image/jpeg\",\"type\":\"image\",\"url\":\"https://s3.amazonaws.com/appleattachment/jpeg-image-8iEic2.jpeg\"}]",
    "datePicker": "",
    "listPicker": "{\"otherItemCount\":2,\"selectedItemCount\":1,\"otherItems\":[{\"identifier\":\"1\",\"style\":\"default\",\"title\":\"iPhone 8\",\"url\":\"https://s3.amazonaws.com/appleattachment/f3dee919-4ebe-4a93-92e6-b4da8eab3a68.jpeg\",\"order\":\"1\"},{\"identifier\":\"2\",\"style\":\"default\",\"title\":\"iPhone SE\",\"url\":\"https://s3.amazonaws.com/appleattachment/06ade50d-5195-4e0a-88c7-315130ba6703.jpeg\",\"order\":\"2\"}],\"selectedItems\":[{\"identifier\":\"0\",\"style\":\"default\",\"title\":\"iPhone X\",\"url\":\"https://s3.amazonaws.com/appleattachment/3566bd31-d031-4bfe-9d1d-36b4b2c3d646.jpeg\",\"order\":\"0\"}]}",
    "locale": "",
    "bizGroupId": "",
    "bizIntentId": "",
    "requestIdentifier": "21d4a1c4-327c-XXXX-45b1-36a050b15ad2",
    "timezone": "",
    "capabilities": "",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CQUICK"
}
```
```json Timepicker (Date Picker)
{
    "abcUserId": "urn:mbid:AQAAY+muaCxppiRFbNZFEiuJAGjZM9I6qRiQqkXVB2gPRPev57AgWIpx431qaDe/JajE2gtnC861/rnOaYWwHUDv7s/lEjgaXYQw0WINUOeouvEY9xOoRqdIwD1c+PkU/8JsPtlLSZupUty4vjT/LYXhya/nyPM=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "137f8c97-8e00-XXXX-ad8f-56051e485e35",
    "appId": "a_63677951XXXX130000",
    "event": "INTERACTIVERESPONSE",
    "ts": "2018-11-17T12:49:56.989Z",
    "tid": "0d2f7154-87ac-XXXX-5927-156bb2ade6e3",
    "message": "",
    "attachments": "",
    "datePicker": "{\"identifier\":\"fd296699-6ad1-4c96-af78-ae10dee1f19c\",\"timezoneOffset\":\"-100\",\"location\":{},\"title\":\"NHS Appointments\",\"timeslots\":[{\"duration\":\"1800\",\"identifier\":\"0\",\"startTime\":\"2019-01-18T15:30+0000\"}]}",
    "listPicker": "",
    "locale": "",
    "bizGroupId": "",
    "bizIntentId": "",
    "requestIdentifier": "b0291fd1-d2ac-XXXX-bd53-9258d6748619",
    "timezone": "",
    "capabilities": "",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CQUICK"
}
```
```json QuickReply
{
"abcUserId": "urn:mbid:AQAAY1cYZy/EMyGTtdo8Hn5/hmvhF9EAzi0briUvglmQ2T4OGaIUXqK/BV+bUNosaolxurhgVhyzPn24nIb6bHAlajJeNfHlQNENNL2m6zCOxBRz5bvVH6JoUmPOGCh1bFOHjF1WOQZd+jS7jG+Zh78clXae8D8=",
"channel": "AppleBusinessChat",
"abcAccountId": "00f67e37-e26a-47c7-XXXX-a73608a976cf",
"appId": "a_637818XXXX88360000",
"event": "QuickReplyResponse",
"ts": "2022-12-08T14:59:15.930Z",
"tid": "1aaf25ff-5401-4d7e-XXXX-2bea0a82b069",
"quickreplies": "{\"selectedIdentifier\":\"Complaint\",\"items\":[{\"identifier\":\"Appointment\",\"title\":\"Book an Appointment\"},{\"identifier\":\"Order\",\"title\":\"Track Order\"},{\"identifier\":\"Complaint\",\"title\":\"Raise a Complaint\"},{\"identifier\":\"Authentication\",\"title\":\"Test Classic Auth\"}],\"selectedIndex\":2}",
"locale": "en_US",
"bizGroupId": "",
"bizIntentId": "",
"requestIdentifier": "NewReq01",
"timezone": "",
"capabilities": "",
"deviceAgent": "",
"capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Classical Authentication
{
    "abcUserId": "urn:mbid:AQAAY70GM+x7gX8NkVOGzgGSqRnQW0YSGkrOV0c6vrKx6iI3nWFDEoxmy80TGcz7ve5/OE7siVVphKDlO+jfNXW2yCDpnGOaryVCkiW+Y8zMM0TxsJUVC92vvgbSULMIc6XqviL7BrVmSa8Oc5XySIFAsbeOLrI=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "5564aa28-66b0-XXXX-bc1c-795867da2241",
    "appId": "a_637438XXXX47650000",
    "event": "AuthenticationResponse",
    "ts": "2022-12-07T22:31:15.402+05:30",
    "tid": "4f6d32ba-e0ce-XXXX-253e-2670f9ae571f",
    "authenticateStatus": "authenticated",
    "authenticateToken": "AQVs-Z2u2TudcFeIPJSiXiqyIGBefBS-4rkHgaGj-1IRxfatFKWGj0gmrXKYZ1wZcdbDtKA8NJzjYQsZKxPvscD1rqhyQeMHvQkqIz_Nr_jr7-Ypwrh3f163EE-RsKH5JKg-HBtlmNMDk9_MwoKn4RTA0TNAHXCRwFdXMIMQktvBkR4EjgfcifWtlItfLYp60MTFW-Sd4duzrFB-vYPxhDHMxbECtH2jM26XQ2IIMud6uwsS9NcbZ7avGRkfsB2lIZvly3TPC3DhOVx8y808vdWTzi0eS1OPKA8SJM8pHkCezXZbk201t2oH2uoSzooPMVwOG_azBuKTkhJcQzmkEn4j6J3L5g",
    "requestIdentifier": "abcd4343",
    "capabilities": "",
    "timezone": "2022-12-07T22:31:15.402+05:30",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```

```json Form Response
{
    "abcUserId": "urn:mbid:AQAAY+5Ero4MNdcGgggjGnuXUThT95YZwW1qHyS6A3Lq0wpJbvftD36jZM4LVUzxyrh/jOuvZTwJYAs5qmxiAE0Wj1ECz/4Wy/M+GmaYf3ZQ/I7VfIW1SsXTpLpfFwEWzBGRX54bswgwMXBByDQZy+HV2hD8D0Q=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "5564aa28-66b0-XXXX-bc1c-795867da2241",
    "appId": "a_63743XXXX447650000",
    "event": "FormResponse",
    "ts": "2023-01-20T13:24:50.861+05:30",
    "tid": "8567392a-10a3-XXXX-fd44-159fa6e7ca95",
    "formResponse": "{\"template\":\"messageForms\",\"version\":\"1.1\",\"private\":true,\"selections\":[{\"pageIdentifier\":\"0\",\"items\":[{\"identifier\":\"0\",\"value\":\"abc@gmail.com\",\"type\":\"input\",\"title\":\"abc@gmail.com\"}],\"subtitle\":\"Please provide new email address\",\"title\":\"New Email Address\"}]}",
    "locale": "en_US",
    "requestIdentifier": "76dbffd0-7f2b-XXXX-a396-ae533d8a68e7",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json iMessage App Response
{
    "abcUserId": "urn:mbid:AQAAY70GM+x7gX8NkVOGzgGSqRnQW0YSGkrOV0c6vrKx6iI3nWFDEoxmy80TGcz7ve5/OE7siVVphKDlO+jfNXW2yCDpnGOaryVCkiW+Y8zMM0TxsJUVC92vvgbSULMIc6XqviL7BrVmSa8Oc5XySIFAsbeOLrI=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "5564aa28-66b0-XXXX-bc1c-795867da2241",
    "appId": "a_637438XXXX47650000",
    "event": "iMessageAppResponse",
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:EQHXZ8M8AV:com.google.ios.youtube.MessagesExtension",
    "attachments": "[{\"size\":\"112407\",\"name\":\"jpeg-image-VrGZee.jpeg\",\"mimeType\":\"image/jpeg\",\"type\":\"image\",\"url\":\"https://s3.amazonaws.com/stagingappleattachment/c1912c9d-1cc9-445d-af33-a1195e498504.jpeg\"}]",
    "ts": "2023-01-12T19:26:44.930+05:30",
    "tid": "78e196ac-b642-1eec-XXXX-8709f67077da",
    "timezone": "2023-01-12T19:26:44.930+05:30",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Authentication Response (New)
{
    "abcUserId": "urn:mbid:AQAAY6Y97JCdel6GzV4bfOZ5t4BxTK+02NQkz8fR7W7LU4O5vaj2xse1ZAMcsdRX1KdDYmyHdNzqzrTZlaTGV7JLlFYGWkAZ5dQgCPq/QhBuri9OR1f22yWxrDxxk+2zNEIgjU22mJNlb+0OaJgpiMg8MdRpjkE=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "5564aa28-66b0-XXXX-bc1c-795867da2241",
    "appId": "a_63743870XXXX650000",
    "event": "NewAuthenticationResponse",
    "ts": "2023-01-09T19:19:01.913+01:00",
    "tid": "0bf841d7-ad7a-XXXX-0585-03b04ac0e9e8",
    "authenticateStatus": "success",
    "authenticateToken": "ABCozws5ygDs1yjaTBuNzq9uJ0xbt9zA0dk1NabcdLoIK3NjXoX08N1JAjExvN9IrrKfvL3cwvHtTpa6cNwsQ_3tMM7a-2ed-SQhCykmqsgWShyWvc_NhnXlbpeeFCzbm2vO5gLJmkTT_9R4bKFFiZLVP5o3TidQV09eacPKrzkIzASnbKTCHDC6L4vkIdVVuBUtf7v0HVpcRN9sJt_wYQUpzY0Wz1vgKF7_EB69bDu4zF-S7-sfnGhkvOeDkUw0SVY9-7-07DhJq872p6w-cAi4T9L9PFgFBKCjV3t39n3a5rmdjA0-ikmjPgLAJTO9MQ-HYuvhfNbYSHMVEuwQBAKi0HYHTw",
    "requestIdentifier": "5de6a59c-846f-45d8-a1d7-24382d9919d33",
    "timezone": "2023-01-09T19:19:01.913+01:00",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Typing Indicator Start
{
    "abcUserId": "urn:mbid:AQAAY+WXd2wHkkzPXBkPZYTkrIupSkanlb1MWd8rM8rXvC5Kudtd/8kaZ2987fp7iLMqssG3l1RR0QPMTP7jlxB97Vm3R4LuiWofF/X3CtH86ApMuSRobNuxZiVtaR25cjyKjNP28g4ax8Q06DlK1bx1NsxhP6c=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "c3f71555-5c42-XXXX-bb65-db3d76322094",
    "appId": "a_63808XXXX336480000",
    "event": "TYPINGINDICATOR",
    "type": "typing_start",
    "ts": "2023-01-09T18:08:41.543+01:00",
    "tid": "4f37e399-942a-XXXX-1f95-e64dfaca7352",
    "requestIdentifier": "",
    "capabilities": "",
    "timezone": "2023-01-09T18:08:41.543+01:00",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Typing Indicator End
{
    "abcUserId": "urn:mbid:AQAAY+WXd2wHkkzPXBkPZYTkrIupSkanlb1MWd8rM8rXvC5Kudtd/8kaZ2987fp7iLMqssG3l1RR0QPMTP7jlxB97Vm3R4LuiWofF/X3CtH86ApMuSRobNuxZiVtaR25cjyKjNP28g4ax8Q06DlK1bx1NsxhP6c=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "c3f71555-5c42-XXXX-bb65-db3d76322094",
    "appId": "a_638085880336480000",
    "event": "TYPINGINDICATOR",
    "type": "typing_end",
    "ts": "2023-01-09T18:21:23.224+01:00",
    "tid": "392345a0-0633-XXXX-aaa4-a83fcb8c111a",
    "requestIdentifier": "",
    "capabilities": "",
    "timezone": "2023-01-09T18:21:23.224+01:00",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Conversation Closed
{
    "abcUserId": "urn:mbid:AQAAY70GM+x7gX8NkVOGzgGSqRnQW0YSGkrOV0c6vrKx6iI3nWFDEoxmy80TGcz7ve5/OE7siVVphKDlO+jfNXW2yCDpnGOaryVCkiW+Y8zMM0TxsJUVC92vvgbSULMIc6XqviL7BrVmSa8Oc5XySIFAsbeOLrI=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "5564aa28-66b0-XXXX-bc1c-795867da2241",
    "appId": "a_637438XXXX47650000",
    "event": "CONVERSATIONCLOSED",
    "type": "close",
    "ts": "2023-01-09T20:16:49.362+01:00",
    "tid": "a556ec33-f312-XXXX-59ab-6fa2e317609b",
    "requestIdentifier": "",
    "capabilities": "",
    "timezone": "2023-01-09T20:16:49.362+01:00",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```
```json Payment Response
{
    "abcUserId": "urn:mbid:AQAAY7Ef830oIja+D072cC0kG/zc+XahQLl/3xHNEtTscvAAwPpn3DE0EA9fVUGQlAzyMj2Ns2phzB7KmR5aWatkVb+Qos8Yam4BC/xUzW+kk1n+hkPbqS6GJnEVGZqTvr5DtNrCfmzwxKqHVtYtbs169Os4W60=",
    "channel": "AppleBusinessChat",
    "abcAccountId": "5564aa28-66b0-XXXX-bc1c-795867da2241",
    "appId": "a_637438XXXX47650000",
    "event": "PaymentResponse",
    "ts": "2023-03-07T10:37:25.224+01:00",
    "tid": "55af2508-5bf6-XXXX-8ea9-9afd12db9822",
    "paymentStatus": "paid",
    "merchantSessionIdentifier": "PSHF8B5E74545DE45149385C0E04E7FAAA3_CCE257A9D27B42513B2C3CA67DB49F602F3450D996C0811ED462EDCA0D7477FD",
    "merchantIdentifier": "B8B2110F393F4A39401E7654321A1234FXXXXC3122704C8AC0FC19BDAF13790",
    "paymentRequest": {
        "lineItems": [
            {
                "amount": "3.5",
                "label": "Adoption fee",
                "type": "Final"
            },
            {
                "amount": "2.5",
                "label": "tution fee",
                "type": "Final"
            },
            {
                "amount": "14",
                "label": "Your Total",
                "type": "Final"
            }
        ],
        "total": {
            "amount": "14",
            "label": "Your Total",
            "type": "Final"
        },
        "countryCode": "US",
        "currencyCode": "USD",
        "requiredBillingContactFields": [
            "name",
            "phone"
        ],
        "shippingMethods": [
            {
                "identifier": "b3062736-e911-XXXX-b7a2-b5c603805858",
                "amount": "8",
                "label": "shipping charges (Optional)",
                "detail": "fast delivery (Optional)"
            }
        ]
    },
    "requestIdentifier": "21d4a1c4-327c-XXXX-45b1-36a050b15ad2",
    "capabilities": "",
    "timezone": "2023-03-07T10:37:25.224+01:00",
    "deviceAgent": "",
    "capabilityList": "AUTH%2CLIST%2CTIME%2CFORM%2CQUICK%2CAUTH2"
}
```

## Invitation Response

When a customer responds to an Apple Messages for Business invitation message, Webex Connect emits an invitation response event if the event is enabled in the outbound webhook configuration.

The invitation response payload includes the resolved Apple Messages for Business user ID when available, `msisdn` when available, `invitationAccepted`, `requestIdentifier`, and the raw or normalized invitation response payload.

```json Invitation Response - Yes
{
  "abcUserId": "urn:mbid:AQAAY+DpsEOs4wkistDRF80rdtsT9hNu/3iQpHFkpep5b5sKRWOHzHCHW0YS5JXiPGy64qaVuBUckNu0B4jzKJwOV5zHC4ybjx6pOZ4tpLlMYCd/DLyUI4GxHRMbmv25gpJ8KVpaOufbKlqwaNZ35n2tPZaqviM=",
  "channel": "AppleBusinessChat",
  "abcAccountId": "59a5c4a6-ad9a-4ead-904a-c0ad04ae67ee",
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

<br />

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "0-0": "abcUserId",
    "0-1": "Contains the unique Apple Messages for Business user ID",
    "1-0": "channel",
    "1-1": "Channel is AppleBusinessChat always for incoming chats on Apple Messages for Business",
    "2-0": "abcAccountId",
    "2-1": "Contains the unique Apple Messages for Business account ID",
    "3-0": "appId",
    "3-1": "Contains the application ID",
    "4-0": "ts",
    "4-1": "Timestamp when MO received to connect",
    "5-0": "tid",
    "5-1": "Transaction ID",
    "6-0": "message",
    "6-1": "Contains the text message sent by the user",
    "7-0": "attachments",
    "7-1": "Contains the attachments sent by the user",
    "8-0": "locale",
    "8-1": "Contains the geographical location of the user",
    "9-0": "bizGroupId",
    "9-1": "Contains the business group ID",
    "10-0": "bizIntentId",
    "10-1": "The intention, or purpose, of the chat as specified by the business, such as account_question.",
    "11-0": "requestIdentifier",
    "11-1": "Applicable for responses to interactive message types such as Quick Replies and Invitation Response. It can be used to correlate the user response to a previously sent interactive message or invitation message.",
    "12-0": "timestamp",
    "12-1": "Timestamp when MO received to connect. This is an old field. This info is now available in the 'ts' field.",
    "13-0": "capabilities",
    "13-1": "This field has been deprecated by Apple Messages for Business in March 2022 and no longer contains any value. Refer to capabilityList field instead.",
    "14-0": "deviceAgent",
    "14-1": "This field has been deprecated by Apple Messages for Business in March 2022 and no longer contains any value.",
    "15-0": "capabilityList",
    "15-1": "A string list that identifies Messages for Business features supported by the customer’s device. The list items are case insensitive and separated by commas. When a customer sends a message, this field allows you to understand the customer device capabilities to compose an appropriate response for that device.  \n  \nSample values are:  \n  \n- QUICK for Quick Reply Message support\n- LIST for List Picker Message support\n- TIME for Time Picker Message support\n- AUTH for Authenticate Message support. Refer to [Common Specifications](https://register.apple.com/resources/messages/msp-rest-api/common-specs#common-specifications)  for full list. Apple Pay, Rich Links are supported on all devices type and version.",
    "16-0": "msisdn",
    "16-1": "Customer mobile number used for the invitation, when available.",
    "17-0": "invitationAccepted",
    "17-1": "`true` if the customer selected **Yes**. `false` if the customer selected **No**.",
    "18-0": "interactiveData.sessionIdentifier",
    "18-1": "Apple session identifier received in the invitation response.",
    "19-0": "invitationResponse",
    "19-1": "Invitation response payload returned as an escaped JSON string."
  },
  "cols": 2,
  "rows": 20,
  "align": [
    "left",
    "left"
  ]
}
[/block]