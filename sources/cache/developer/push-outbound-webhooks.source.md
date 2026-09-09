You can configure Outbound Webhooks to receive a copy of delivery notifications for Push Notifications sent via Webex Connect by navigating to 'Assets -> Integrations -> Outbound Webhooks' sections in the platform. 

## Outbound Webhook configuration for tracking message status

If you want to track message submission status, select the Webex Connect Service you are using to send the Push Notifications under 'Entity' dropdown. Once done, you will receive the following notifications on the configured webhook URL.

### Android

```json Submitted
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2024-02-07T14:52:10.281+05:30",
            "pushId": "ejS3Ao5XXXXtg2rDw9xQer:XXX91bXXl0kXHvdlPoTFOqNkfiKXzznnnQ2VGnp4lN20bJyzyRTaPHTiACkb41Fut9F193FrwPEU-28NSlRyY3Au3-m79ThKf5PEWRz3Z0oGUqXUWooEevBHZuYor5cV5JNPagQAtUIbE",
            "Description": "Submitted",
            "code": "7501",
            "deliveryChannel": "push",
            "destination": "ejS3Ao5XXXXtg2rDw9xQer:XXX91bXXl0kXHvdlPoTFOqNkfiKXzznnnQ2VGnp4lN20bJyzyRTaPHTiACkb41Fut9F193FrwPEU-28NSlRyY3Au3-m79ThKf5PEWRz3Z0oGUqXUWooEevBHZuYor5cV5JNPagQAtUIbE",
            "destinationType": "android_pushid", //The value of this field will be hms_pushid when sending notifications via Huawei Mobile Services instead of Firebase Cloud Messaging.
            "deviceid": "xxx0123456x78xxx",
            "deliveryStatus": "Submitted"
        },
        "subtid": "", //The sub transaction id is not relevant for API based transactions. It applies only for Send Node based transactions.
        "transid": "1baf584e-a059-XXXX-a1c1-e8391b08a16b",
        "callbackData": "callbackData",
        "correlationid": "correlationId"
    }
}
```
```json Delivered
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2024-02-07T14:52:10.725+05:30",
            "pushId": "ejS3Ao5XXX2tg2rDw9xQer:XXX91bERl0kHvdlPoXXOqNkfiXKXzznnnQ2XXnp4lN20bJyzyRTaPHTiACkb41Fut9F193FrwPEU-28NSlRyY3Au3-m79ThKf5PEWRz3Z0oGUqXUWooEevBHZuYor5cV5JNPagQAtUIbE",
            "Description": "Delivered",
            "code": "7500",
            "deliveryChannel": "push",
            "destination": "ejS3Ao5XXX2tg2rDw9xQer:XXX91bERl0kHvdlPoXXOqNkfiXKXzznnnQ2XXnp4lN20bJyzyRTaPHTiACkb41Fut9F193FrwPEU-28NSlRyY3Au3-m79ThKf5PEWRz3Z0oGUqXUWooEevBHZuYor5cV5JNPagQAtUIbE",
            "destinationType": "android_pushid", //The value of this field will be hms_pushid when sending notifications via Huawei Mobile Services instead of Firebase Cloud Messaging.
            "deviceid": "xxx0123456x78xxx",
            "deliveryStatus": "Delivered"
        },
        "subtid": "",
        "transid": "1baf584e-a059-XXXX-a1c1-e8391b08a16b",
        "callbackData": "callbackData",
        "correlationid": "correlationId"
    }
}
```
```json Read
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-14T21:37:38.512+05:30",
      "pushId": "xd3-XN8XXdTkSi62EIfGrweY:XXX91bFB6jxHPP7bFR5hnpwdgDuj_7Wqr5gtSG8ZQyChKW9O3hcAXogDRMVx_2hRnaXzlVUywJp-RyaMzlGVDCuF1XcihsYdRGeW8DsneIZj_0dzU9Kp8bU2Lb6RqTvR-oJR0tsvcZrJ",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "push",
      "destination": "xd3-XN8XXdTkSi62EIfGrweY:XXX91bFB6jxHPP7bFR5hnpwdgDuj_7Wqr5gtSG8ZQyChKW9O3hcAXogDRMVx_2hRnaXzlVUywJp-RyaMzlGVDCuF1XcihsYdRGeW8DsneIZj_0dzU9Kp8bU2Lb6RqTvR-oJR0tsvcZrJ",
      "destinationType": "android_pushid", //The value of this field will be hms_pushid when sending notifications via Huawei Mobile Services instead of Firebase Cloud Messaging.
      "deviceid": "xxx0123456x78xxx",
      "deliveryStatus": "Read"
    },
    "subtid": "",
    "transid": "ecbe2371-2634-XXXX-9f1b-15513c58708f",
    "callbackData": "callbackData",
    "correlationid": "correlationId"
  }
}
```
```json Read with Interaction
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-14T19:11:57.840+05:30",
      "pushId": "",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "push",
      "destination": "123456", //This field contains the user id of the customer.
      "interaction": {
        "Button_Pressed": "SUBSCRIBE", //This is an example where a button reading SUBSCRIBE has been clicked by the recipient.
        "pushref": "pushRef123"
      },
      "destinationType": "userid",
      "deviceid": "",
      "deliveryStatus": "Read"
    },
    "subtid": "",
    "transid": "ed661456-bdbc-XXXX-b8c1-4a206cb437e5",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Failed - Mandatory Paramaters Missing
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "timeStamp": "2024-02-09T15:25:35.194+01:00",
            "pushId": "",
            "Description": "Mandatory parameters missing.",
            "code": "7003",
            "deliveryChannel": "push",
            "destination": "12345",
            "destinationType": "android_pushid",
            "deviceid": "xxx0123456x78xxx",
            "deliveryStatus": "Failed"
        },
        "subtid": "",
        "transid": "28112e61-3d20-XXXX-bfd5-9f1cafe9184a",
        "callbackData": "callbackData",
        "correlationid": "correlationId"
    }
}
```
```json Failed - Customer Profile Not Found
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-14T21:38:39.110+05:30",
      "pushId": "",
      "Description": "Customer profile not found",
      "code": "7105",
      "deliveryChannel": "push",
      "destination": "1234567XX",
      "destinationType": "",
      "deviceid": "",
      "deliveryStatus": "Failed"
    },
    "subtid": "",
    "transid": "2e173d6e-b14d-XXXX-8679-bf76e65def61",
    "callbackData": "callbackData",
    "correlationid": "correlationId"
  }
}
```

#### Android Application States

Please note that an Android Mobile app can be in one of the below mentioned states at any given point in time, and some of delivery status notifications may be delayed depending on the state. 

[block:parameters]
{
  "data": {
    "h-0": "State",
    "h-1": "Description",
    "h-2": "Push Notification",
    "h-3": "Delivery Status",
    "0-0": "Foreground",
    "0-1": "The application is currently open, running in foreground, and is receiving events.",
    "0-2": "Received",
    "0-3": "Received",
    "1-0": "Background",
    "1-1": "The application is currently closed and running in background.",
    "1-2": "Received",
    "1-3": "Received",
    "2-0": "AppStandby",
    "2-1": "App Standby allows the system to determine that an application is idle when the user is not actively using it. The system makes this determination when the user does not touch the application for a certain period of time.",
    "2-2": "Delayed (High priority FCM messages are received immediately)",
    "2-3": "Delayed",
    "3-0": "Doze",
    "3-1": "If a user leaves a device unplugged and stationary over a period of time with the screen off, then the device enters Doze mode.  \nIn this mode, the system attempts to conserve battery by restricting apps access to network and CPU-intensive services.",
    "3-2": "Delayed (High priority FCM messages are received immediately)",
    "3-3": "Delayed",
    "4-0": "Idle",
    "4-1": "The application is idle when the user is not actively using it. Idle mode is triggered for both Doze and AppStandby.",
    "4-2": "Delayed (High priority FCM messages are received immediately)",
    "4-3": "Delayed"
  },
  "cols": 4,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


### iOS

```json Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:11:06.376+01:00",
      "pushId": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "push",
      "destination": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "destinationType": "ios_pushid",
      "deviceid": "XXXXXBE6306E417F90778E422532AEFC",
      "deliveryStatus": "Submitted"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:11:08.388+01:00",
      "pushId": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "Description": "Delivered",
      "code": "7500",
      "deliveryChannel": "push",
      "destination": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "destinationType": "ios_pushid",
      "deviceid": "XXXXXBE6306E417F90778E422532AEFC",
      "deliveryStatus": "Delivered"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Read
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:12:31.226+01:00",
      "pushId": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "push",
      "destination": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "destinationType": "ios_pushid",
      "deviceid": "XXXXXBE6306E417F90778E422532AEFC",
      "deliveryStatus": "Read"
    },
    "subtid": "",
    "transid": "x5xx1530-XXXX-4x0x-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Read with Interaction
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-03-01T11:37:05.125+05:30",
      "pushId": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "push",
      "destination": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "interaction": {
        "Button_Pressed": "SUBSCRIBE",
        "pushref": "ui"
      },
      "destinationType": "ios_pushid",
      "deviceid": "XXXXXBE6306E417F90778E422532AEFC",
      "deliveryStatus": "Read"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Failed
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:09:16.321+01:00",
      "pushId": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "Description": "Others",
      "code": "7404",
      "deliveryChannel": "push",
      "destination": "XXXXXf8dd3ca5bcca73f0519fefdb2ca9a246627aa2eaa1ac4a90a86667bf221",
      "destinationType": "ios_pushid",
      "deviceid": "XXXXXBE6306E417F90778E422532AEFC",
      "deliveryStatus": "Failed"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```

#### iOS Application States

The three application states for an iOS application are defined in the table below. These states determine whether the OS passes notification data to the app and, hence, whether a delivery receipt is sent by the SDK to the <<prodname>> platform.

[block:parameters]
{
  "data": {
    "h-0": "State",
    "h-1": "Description",
    "h-2": "Data passed to app",
    "0-0": "Active",
    "0-1": "The application is currently open, running in foreground, and is receiving events.",
    "0-2": "Yes",
    "1-0": "Background",
    "1-1": "The application is used in the background and is executing code. Most applications enter this state on their way to being suspended (that is, when user clicks on the button home/switch to another application). In this case, the app is still visible in the app switcher.",
    "1-2": "Yes",
    "2-0": "Terminated",
    "2-1": "The application is not launched after a reboot _or_ was running, but was terminated by the system.",
    "2-2": "Yes - If notification tapped.  \nNo - if notification dismissed."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Web

```json Chrome-Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:26:36.831+01:00",
      "pushId": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "push",
      "destination": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "destinationType": "chrome_pushid",
      "deviceid": "1009XXXX7733258337",
      "deliveryStatus": "Submitted"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Chrome-Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:26:38.729+01:00",
      "pushId": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "Description": "Delivered",
      "code": "7500",
      "deliveryChannel": "push",
      "destination": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "destinationType": "chrome_pushid",
      "deviceid": "1009XXXX7733258337",
      "deliveryStatus": "Delivered"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Chrome-Read
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:26:40.701+01:00",
      "pushId": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "push",
      "destination": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "destinationType": "chrome_pushid",
      "deviceid": "1009XXXX7733258337",
      "deliveryStatus": "Read"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Chrome - Failed
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:24:16.333+01:00",
      "pushId": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "Description": "Others",
      "code": "7404",
      "deliveryChannel": "push",
      "destination": "XXXXXXXXXXHP6XYu2V9AE2:APA91bHaq051NSXPiZh0raS6ZMkqga-LnrJyINdDhBHCaJ6y1g5NSIv_KlRhAR7sIxZcAub88ggjVQ3LFFqqYvhuYpzkdLz4K-RMyEDyOKeZKnMaTaVJlUEqiJq-ZDi-v1EaXKZFsHFw",
      "destinationType": "chrome_pushid",
      "deviceid": "1009XXXX7733258337",
      "deliveryStatus": "Failed"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Firefox-Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:29:26.589+01:00",
      "pushId": "XXXXXX2iRfVB8EW_ba9T50:APA91bEcKbz4VanqloI2papgaJ8i1ZTkBcog0BpLwOIrhcrOI8DXBr76fx-KsRENRYyoKzoN_kDY7ChoMsmkC1oxmkxXnl1D2GNlqXsIFDVaDle7aHDbnMozKMHFrl8mFLQSdHZ-UXix",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "push",
      "destination": "XXXXXX2iRfVB8EW_ba9T50:APA91bEcKbz4VanqloI2papgaJ8i1ZTkBcog0BpLwOIrhcrOI8DXBr76fx-KsRENRYyoKzoN_kDY7ChoMsmkC1oxmkxXnl1D2GNlqXsIFDVaDle7aHDbnMozKMHFrl8mFLQSdHZ-UXix",
      "destinationType": "firefox_pushid",
      "deviceid": "1090XXXX7733743479",
      "deliveryStatus": "Submitted"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Firefox-Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:29:27.063+01:00",
      "pushId": "XXXXXX2iRfVB8EW_ba9T50:APA91bEcKbz4VanqloI2papgaJ8i1ZTkBcog0BpLwOIrhcrOI8DXBr76fx-KsRENRYyoKzoN_kDY7ChoMsmkC1oxmkxXnl1D2GNlqXsIFDVaDle7aHDbnMozKMHFrl8mFLQSdHZ-UXix",
      "Description": "Delivered",
      "code": "7500",
      "deliveryChannel": "push",
      "destination": "XXXXXX2iRfVB8EW_ba9T50:APA91bEcKbz4VanqloI2papgaJ8i1ZTkBcog0BpLwOIrhcrOI8DXBr76fx-KsRENRYyoKzoN_kDY7ChoMsmkC1oxmkxXnl1D2GNlqXsIFDVaDle7aHDbnMozKMHFrl8mFLQSdHZ-UXix",
      "destinationType": "firefox_pushid",
      "deviceid": "1090XXXX7733743479",
      "deliveryStatus": "Delivered"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-XXXX-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Firefox-Read
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:29:51.405+01:00",
      "pushId": "XXXXXX2iRfVB8EW_ba9T50:APA91bEcKbz4VanqloI2papgaJ8i1ZTkBcog0BpLwOIrhcrOI8DXBr76fx-KsRENRYyoKzoN_kDY7ChoMsmkC1oxmkxXnl1D2GNlqXsIFDVaDle7aHDbnMozKMHFrl8mFLQSdHZ-UXix",
      "Description": "Read",
      "code": "7502",
      "deliveryChannel": "push",
      "destination": "XXXXXX2iRfVB8EW_ba9T50:APA91bEcKbz4VanqloI2papgaJ8i1ZTkBcog0BpLwOIrhcrOI8DXBr76fx-KsRENRYyoKzoN_kDY7ChoMsmkC1oxmkxXnl1D2GNlqXsIFDVaDle7aHDbnMozKMHFrl8mFLQSdHZ-UXix",
      "destinationType": "firefox_pushid",
      "deviceid": "1090XXXX7733743479",
      "deliveryStatus": "Read"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-4x0x-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Firefox - Failed
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-02-12T11:30:27.985+01:00",
      "pushId": "",
      "Description": "Customer profile not found",
      "code": "7105",
      "deliveryChannel": "push",
      "destination": "10999",
      "destinationType": "",
      "deviceid": "",
      "deliveryStatus": "Failed"
    },
    "subtid": "",
    "transid": "x5xx1530-34xx-4x0x-12xx-xxx30c236407",
    "callbackData": "",
    "correlationid": ""
  }
}
```