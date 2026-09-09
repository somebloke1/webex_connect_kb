> 📘 Please Note
> 
> Push channel is supported via <<prodname>> Messaging API v1. The endpoint for it is:
> 
> [https://api.{YourRegion}.webexconnect.io/resources/v1/messaging].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying various types of push notifications supported by <<prodname>>.

## Request Body for Push Notification

```json
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory. App ID of the mobile/web asset configured in <<prodname>>.
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "title": "Notification Title", //Optional
                "text": "Android specific text message.", //Mandatory for Android Push notification
                "extras": { //Optional. Refer the Android extras section below.
                    "collapse_key": "{{collapse_key}}", //Optional. If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide.
                    "time_to_live": "1000", //Optional. You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), FCM will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit  from 0 to 2,419,200 seconds (0 to 28 days). If you don't set a limit, FCM will keep trying to deliver your message for up to 4 weeks.
                    "customtags": { // Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                        "imageurl": "{{imageurl}}", // Custom tags object includes a reserved parameter called “imageurl”. This accepts a URL as a string and this parameter is used for sending images with notifications.
                        "Key1": "Value1" //Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                    },
                    "iconurl": "{{iconurl}}", //Optional, This accepts a URL as a string. Adding an icon for the push notifications can help create a unique, branded experience."
                    "notificationChannelId": "{{notificationChannelId}}", //Optional. Starting on Android 8.0, all notifications must be assigned to a Notification channel or it will not appear. Instead of disabling all the notifications, user can control notification by disabling a specific channel on the app.
                    "notificationaction": { //Optional. Define this object to specify an action to be taken when the notification is clicked. Please refer 'Android - notificationaction' section for different types of actions supported in the Webex Connect.
                        "action": "OPEN_URL", //Opens the respective link in your browser. 
                        "value": "{{url}}" //Accepts a URL as a string when the action is selected as 'OPEN_URL'.
                    }
                }
            },
            "ios": {
                "title": "Notification Title", //Optional
                "text": "iOS specific text message.", //Mandatory for iOS push notification
                "extras": { //Optiona. Refer the iOS extras section below.
                    "badge": "10", //Accepts integer, The number to be displayed as badge of the app icon.
                    "sound": "default", //You can pass either 'default' for the standard sound or specify a custom sound. To use the default sound, pass the value 'default,' and the system's default notification sound will be used. To add custom sounds, add files to the Xcode project root. Make sure Add to targets is selected when adding files so that they are automatically add to the bundle resources. External URLs are not supported and you need to pass the filename with extension (newsound.mp3) of the sound file.
                    "time_to_live": "1000", //Optional. You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), APNs will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit upto 30days.
                    "customtags": {
                        "key1": "value1" // Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                    },
                    "collapse_key": "{{collapse_key}}", //Optional. An arbitrary string that is used to replace the older message with new message when the older message did not reach the destination.
                    "attachmenturl": "{{attachmenturl}}", //Optional. This accepts a URL as a string and this parameter is used for sending images with notifications.
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked. Please refer 'iOS - notificationaction' section for different types of actions supported in the Webex Connect.
                        "action": "OPEN_URL", //Opens the respective link in your browser.
                        "value": "{{url}}" //Accepts a URL as a string when the action is selected as 'OPEN_URL'.
                    }
                }
            },
            "web": {
                "platform_types": [
                    "chrome",
                    "safari",
                    "firefox"
                ], //Mandatory for web push notification,
                "title": "<title text for web browser push message>", //Optional.
                "text": "<push message text for Web browser>", //Mandatory for web push notification
                "actiontext": "<Specifies the text of the button for safari browsers only>",
                "url": "<URL that opens when message is clicked>",
                "extras": {
                    "collapse_key": "<Alpha numeric key>", //Optional. If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide.
                    "time_to_live": "<integer value>", //Number of seconds that a message may be stored if the user is not immediately available. Max of 51840000.  
                    "customtags": {
                        "key1": "object1",
                        "key2": {
                            "object2": "val"
                        },
                        "key3": [
                            "object3",
                            "object4"
                        ] //Optional, Refer the web extras section below.
                    }
                }
            },
            "interactive": { //Optional. Refer the interactive section below for different types of actions supported by Webex Connect.
                "category": "DOUBLE_YES_NO",
                "pushref": "ui", //Optional.
                "device_types": [
                    "ios",
                    "android"
                ],
                "actions": [
                    {
                        "action": "OPEN_URL",
                        "value": "https://www.cisco.com",
                        "identifier": "YES", //The identifier depends on the action.
                        "pos": 1 // Specifies the position or sequence of the button. Pass either 1 or 2.
                    },
                    {
                        "action": "OPEN_APP",
                        "identifier": "NO", //The identifier depends on the action.
                        "pos": 2 //Specifies the position or sequence of the button. Pass either 1 or 2.
                    }
                ]
            }
        }
    },
    "expiry": "{{expiry}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. 
    "callbackData": "{{callbackData}}", //Optional.
    "notifyurl": "{{webhookurl}}", //Optional.
    "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

## Push Messaging Parameters

The following are the parameters of the request body:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "deliverychannel",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "Set the value to 'push' for the push notification channel.",
    "1-0": "appid",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "App ID of the mobile/web asset configured in <<prodname>>.",
    "2-0": "channels",
    "2-1": "JSONObject",
    "2-2": "yes",
    "2-3": "Contains a push object as defined in the next row.",
    "3-0": "push",
    "3-1": "JSONObject",
    "3-2": "yes",
    "3-3": "Contains [android](https://imiconnect-apis-group.readme.io/reference/push#android), [ios](https://imiconnect-apis-group.readme.io/reference/push#ios), [web ](https://imiconnect-apis-group.readme.io/reference/push#web)and [interactive](https://imiconnect-apis-group.readme.io/reference/push#interactive) objects. At least one of the three objects, i.e. the Android, iOS, or _web_ object is mandatory.",
    "4-0": "android",
    "4-1": "JSONObject",
    "4-2": "No",
    "4-3": "This object is for Android-specific push settings. For more information, see [android](https://imiconnect-apis-group.readme.io/reference/push#android).",
    "5-0": "ios",
    "5-1": "JSONObject",
    "5-2": "No",
    "5-3": "This object is for iOS-specific push settings. For more information, see [iOS](https://imiconnect-apis-group.readme.io/reference/push#ios).",
    "6-0": "web",
    "6-1": "JSONObject",
    "6-2": "No",
    "6-3": "This object is for web browser-specific push settings. For more information, see [web](https://imiconnect-apis-group.readme.io/reference/push#web).",
    "7-0": "interactive",
    "7-1": "JSONObject",
    "7-2": "No",
    "7-3": "This object contains the information of buttons and their actions in an interactive push notification. For more information, see [interactive](https://imiconnect-apis-group.readme.io/reference/push#interactive).",
    "8-0": "correlationid",
    "8-1": "string",
    "8-2": "No",
    "8-3": "A unique identifier that can be used to correlate requests and their subsequent responses. The correlation-id is sent as part of delivery updates to outbound webhooks and notify URLs. It can be up to 50 bytes long.",
    "9-0": "notifyurl",
    "9-1": "string",
    "9-2": "No",
    "9-3": "<<prodname>> will send delivery updates to the URL specified in the notifyurl parameter. The notifyurl can also be configured while creating a service. If the URL is specified in both the service and the messaging API, preference will be given to the messaging API request.",
    "10-0": "notifyurlAuthId",
    "10-1": "string",
    "10-2": "",
    "10-3": "Unique Authentication ID.",
    "11-0": "callbackData",
    "11-1": "string",
    "11-2": "No",
    "11-3": "Any metadata that needs to be sent alongside delivery updates to the notiyurl.",
    "12-0": "expiry",
    "12-1": "string",
    "12-2": "No",
    "12-3": "If the expiry time provided is crossed by the time the API request is processed,<<prodname>> will not attempt delivery of the message. The expiry time is in UTC format. For example, 2015-04-12T13:00:19.456Z or 2015-04-12T18:30:19.456+5:30.",
    "13-0": "message template",
    "13-1": "JSONObject",
    "13-2": "No",
    "13-3": "The message block references a template via the template ID which is created within the <<prodname>> platform. Along with the template ID, you can pass a JSON object called ‘parameters'. You can send a key-value pair in the 'parameters’ object  \n  \nThese key-value pairs are supplied to the template for substitution in the final message.  \n  \n{  \n\"message\": {  \n\"template\": \"TEMPLATE ID\",  \n\"parameters\": {  \n\"parameter1\": \"VALUE\",  \n\"parameter2\": \"VALUE\",  \n\"parameter3\": \"VALUE\"  \n}  \n}  \n}  \n  \n_**Note:** If you use message templates, then the parameter name of the key-value pair should match the parameter name specified in the template. The parameters in this message block are overridden if a channel-specific parameter block is also used._",
    "14-0": "destination",
    "14-1": "JSONArray",
    "14-2": "Yes",
    "14-3": "The destination parameter holds the user ID or push ID of the targeted customer. It is an array that can be up to 1,000 entries.  \n  \nHere are the syntaxes for various ID types:  \n  \n\"userid\": [\"userid\"]  \n\"android_pushid\": [\"android_pushid\"]  \n\"hms_pushid\": [\"hms_pushid\"]  \n\"ios_pushid\": [\"ios_pushid\"]  \n\"chrome_pushid\": [\"chrome_pushid\"]  \n\"firefox_pushid\": [\"firefox_pushid\"]"
  },
  "cols": 4,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

> 📘 Note
> 
> The overall payload limit for the messaging API for Push notification is 4KB.

## **Components of Push Object**

A push object comprises the following components:

- [Android](https://imiconnect-apis-group.readme.io/reference/push#android)
- [iOS](https://imiconnect-apis-group.readme.io/reference/push#ios) 
- [Web ](https://imiconnect-apis-group.readme.io/reference/push#web)
- [Interactive](https://imiconnect-apis-group.readme.io/reference/push#interactive)

### Android

To send push notifications to AndroidA devices

```json Android Push
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "", //Mandatory, for Android Push Notifications.
                "title": "Notification Title", //Optional
                "extras": {
                    //Please refer to the extras section
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
"notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

| Parameter | Type       | Mandatory | Description                                                                                                                                                                |
| :-------- | :--------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| title     | String     | No        | A heading displayed above the top of the notification text to summarize its content or purpose.                                                                            |
| text      | String     | Yes       | The text for the notification body for Android.                                                                                                                            |
| extras    | JSONObject | No        | Please refer to the [extras](https://developers.imiconnect.io/reference/push#android:~:text=push%20%3E%20android%20%3E%20Android%20extras) section right below this table. |

#### **push > android > Android extras**

To change the appearance of your push notifications, such as sending images, icons, etc., and managing notification delivery use the extras object.

```json extras - Definition
"extras": {
        "collapse_key": "<Alpha numeric key>",
        "time_to_live": "<integer value>",
        "customtags": {
            "key1": "object1",
            "key2": {
                "object2": "val"
            },
            "key3": [
                "object3",
                "object4"
            ]
        },
        "notificationaction": {
            "action": "OPEN_URL",
            "value": "www.cisco.com"
        },
        "iconurl": "{{iconurl}}", //Optional. This accepts a URL as a string. Adding an icon for the push notifications creates a unique, branded experience."
        "notificationChannelId":"{{notificationChannelId}}" //Optional. Starting with Android 8.0, all notifications must be assigned to a Notification channel or it will not appear. Instead of disabling all the notifications, user can control notification by disabling a specific channel on the app.
    }
```
```json Android push with image
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Mandatory
                "extras": {
                    "sound": "default", //Optional
                    "customtags": { // Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                        "imageurl": "https://file-examples.com/wp-content/storage/2017/10/file_example_JPG_100kB.jpg" // customtags object contains a reserved parameter: imageurl: It accepts a URL as string. This parameter is used to send images in notification.
                    },
                    "notificationChannelId": "" //Optional. Starting on Android 8.0, all notifications must be assigned to a Notification channel or it will not appear. Instead of disabling all the notifications, user can control notification by disabling a specific channel on the app.
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json Android push with extras
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "collapse_key": "{{collapse_key}}", //Optional. If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide.
                    "time_to_live": "1000", //Optional. You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), FCM will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit  from 0 to 2,419,200 seconds (0 to 28 days). If you don't set a limit, FCM will keep trying to deliver your message for up to 4 weeks.
                    "customtags": { // Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                        "imageurl": "{{imageurl}}", // Custom tags object includes a reserved parameter called “imageurl”. This accepts a URL as a string and this parameter is used for sending images with notifications.
                        "Key1": "Value1" //Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                    },
                    "iconurl": "{{iconurl}}", //Optional, This accepts a URL as a string. Adding an icon for the push notifications creates a unique, branded experience."
                    "notificationChannelId": "" //Optional. Starting on Android 8.0, all notifications must be assigned to a Notification channel or it will not appear. Instead of disabling all the notifications, user can control notification by disabling a specific channel on the app.
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "collapse_key",
    "0-1": "String",
    "0-2": "No",
    "0-3": "If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in the FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide.",
    "1-0": "time_to_live",
    "1-1": "String",
    "1-2": "No",
    "1-3": "You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), FCM will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,419,200 seconds (0 to 28 days). If you don't set a limit, FCM will keep trying to deliver your message for up to 4 weeks.  \n  \n_**Note: **If the value is set to 0 seconds, the message will expire immediately, and FCM will not store the notification or attempt to redeliver it._",
    "2-0": "sound (Discontinued)",
    "2-1": "String",
    "2-2": "No",
    "2-3": "_**Note:** This parameter is no longer supported. It will get ignored even if we pass any value._  \nA Default / Custom sound will be played when the notification is delivered.  \n  \nThe options are:  \n  \n  \\_ default  \n  \n  \\_ custom sound",
    "3-0": "delay_while_idle (Deprecated)",
    "3-1": "String",
    "3-2": "No",
    "3-3": "If true, the message delivery is delayed when the customer’s device is idle.  \n  \nOptions are:  \n  \n  \\_ true  \n  \n  \\_ false",
    "4-0": "customtags",
    "4-1": "JSONObject",
    "4-2": "No",
    "4-3": "Custom tags are flexible and can be crafted to match the specific needs and logic of your business. Simply pass a key-value pair, where the value can be a string, a JSON object, or a JSON array depending on your requirement.  \n  \n_**Note:** Custom tags object includes a reserved parameter called “imageurl”. This accepts a URL as a string and this parameter is used for sending images with notifications on Android devices only._",
    "5-0": "notificationaction",
    "5-1": "JSONObject",
    "5-2": "No",
    "5-3": "Define this object to add an action when the notification is clicked. The sub-parameters of this block are:  \n  \n\\_ action  \n  \n\\_ value  \nPlease refer to the [notificationaction](https://imiconnect-apis-group.readme.io/reference/push#android:~:text=notification%20channel.-,Android%20%2D%20notificationaction,-Traditionally%2C%20tapping%20a) section right below this table.",
    "6-0": "iconurl",
    "6-1": "String",
    "6-2": "No",
    "6-3": "This accepts a URL as a string. Adding an icon for the push notifications creates a unique, branded experience.",
    "7-0": "notificationChannelId",
    "7-1": "String",
    "7-2": "No",
    "7-3": "Starting with Android 8.0 (API level 26), all notifications must be assigned to a notification channel; otherwise, they will not appear to the user. Rather than disabling all notifications, users have the option to control notifications by disabling a specific channel within the app. This allows for more granular control over the types of notifications they wish to receive. For more info on the Notification Channel, refer to the [Android official documentation on the notification channel](https://developer.android.com/reference/android/app/NotificationChannel).  \n  \n**Note:**  If a notificationChannelId is not explicitly passed, the SDK will automatically use the default channel ID. It is mandatory to create a notification channel with the default channel ID within the app so that the notifications sent without any channel ID are displayed using the default channel. Refer to [Push Messaging Guide](https://developers.webexconnect.io/docs/push-messaging-guide#to-register-notification-channel)  to know more about how to create a notification channel with the default channel ID."
  },
  "cols": 4,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Android - notificationaction**

Traditionally, tapping a push notification simply opens an app. However, modern notifications can offer users much more. With just a tap, you can now provide up to five distinct actions, allowing for immediate and varied responses to notifications without ever opening the app.

Following are the sample codes for various notification actions supported in <<prodname>>:

```json Android Push with Notification action - OPEN_URL
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Optioanl
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPEN_URL", //Opens the respective link in your browser.
                        "value": "{{url}}" //Accepts a URL as a string when the action is selected as 'OPEN_URL'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyurl": "{{webhookurl}}", //Optional.
    "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json Android Push with Notification action - OPENWEBVIEW
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{inappid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPENWEBVIEW", // launches a web view inside your app.
                        "value": "https://www.cisco.com" //Accepts a URL as a string when the action is selected as 'OPENWEBVIEW'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
"notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json Android Push with Notification action - DEEPLINK
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{inappid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "DEEPLINK", //will take you to destination defined in the link.
                        "value": "MU20051001://command/Notifications"
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json Android Push with Notification action - OPEN_HTML
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{inappid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPEN_HTML", // Renders the HTML payload within the app.
                        "value": "<a href=https://www.cisco.com>Click on it for Cisco</a>" // Accpets HTML tags, when the action is selected as 'OPEN_HTML'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json Android Push with Notification action - OPEN_APP
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{inappid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPEN_APP" //Simply opens the app corresponding to the notification. Does not require value for 'Open_Action'.
                    }
                }
            }
        }
    },
    "expiry": "", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

The following parameters are part of the **notification action **object which in turn is part of the **extras **object.

<NotificationActionTable />

> 📘 Note
> 
> It is not mandatory to define _notificationaction_. But if you set an _action_, you must specify a \_value \_that is used to complete the configured action. By default Open App is the notificationaction set by android for all notification.

### iOS

Following are the sample request bodies to send iOS Push notifications:

```json iOS Push
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "iOS specific text message.", //Mandatory
                "title": "Notification Title", //Optional
              	"extras": {
                    //Optional.Please refer extras section.
                }
            }
        },
        "expiry": "{{expirytime}}", //Optional. UTC time format.
        "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
      "notifyurl": "{{webhookurl}}", //Optional.
     "notifyurlAuthId": "TNPXXXT09U" //Optional.
    }
}
```
```json iOS Push with Image
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "iOS specific text message.", //Mandatory
                "title": "Notification Title", //Mandatory
                "extras": {
                    "attachmenturl": "{{attachmenturl}}" ////Optional. This accepts a URL as a string and this parameter is used for sending images with notifications.
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

To send push notifications to iOS devices, the following are the parameters required:

| Parameter | Type       | Mandatory | Description                                                                                                                                                                            |
| :-------- | :--------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| title     | String     | No        | A heading is displayed above the top of the notification text to summarize its content or purpose.                                                                                     |
| text      | String     | Yes       | The text for the notification body for iOS.                                                                                                                                            |
| extras    | JSONObject | No        | Please refer to the [extras](https://imiconnect-apis-group.readme.io/reference/push#ios:~:text=google.com%22%0A%20%20%20%20%7D%0A%7D-,Parameter,-Type) section right below this table. |

#### **push > ios > ios extras**

To change the appearance of your iOS push notifications, such as sending images, icons, etc., and managing notification delivery use the extras object.

Following are the sample request bodies for the extra object.

```json extras - Definition
{
    "badge": "<badge number>",
    "sound": "<default/custom sound>",//For custom sound you need to pass the file name with extension.
    "time_to_live": "<integer value>",
    
    "customtags": {
        "key1": "object1",
        "key2": {
            "object2": "val"
        },
        "key3": ["object3", "object4"]
    },
    "notificationaction": {
        "action": "OPEN_URL",
        "value": "www.google.com"
    }
}
```
```json iOS Push notification with extras
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "iOS specific text message.", //Mandatory
                "title": "Notification Title", //Mandatory
                "extras": {
                    "badge": "10", //Accepts integer, The number to be displayed as badge of the app icon.
                    "sound": "default", //You can pass either 'default' for the standard sound or specify a custom sound. To use the default sound, pass the value 'default,' and the system's default notification sound will be used. To add custom sounds, add files to the Xcode project root. Make sure Add to targets is selected when adding files so that they are automatically add to the bundle resources. External URLs are not supported and you need to pass the filename with extension (newsound.mp3) of the sound file.
                    "time_to_live": "1000", //Optional. You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), APNs will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit upto 30day
                    "customtags": {
                        "key1": "value1" // Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                    },
                    "collapse_key": "{{collapse_key}}", //Optional. An arbitrary string that is used to replace the older message with new message when the older message did not reach the destination.
                    "attachmenturl": "{{attachmenturl}}" //Optional. This accepts a URL as a string and this parameter is used for sending images with notifications.
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "badge",
    "0-1": "String",
    "0-2": "No",
    "0-3": "The number to be displayed as a badge of the app icon.",
    "1-0": "sound",
    "1-1": "String",
    "1-2": "No",
    "1-3": "Default or Custom sound that should be played when the notification is delivered.  \n  \nThe options are:  \n  \n  \\_ default  \n  \n  \\_ file name of custom sound  \n  \nYou can pass either 'default' for the standard sound or specify a custom sound. To use the default sound, pass the value 'default,' and the system's default notification sound will be used. To add custom sounds, add the audio files to the Xcode project root. Make sure **Add to targets **is selected when adding files so that they are automatically added to the bundle resources. External URLs are not supported. You need to pass the filename with the extension (newsound.mp3) of the sound file.  \nCustom sounds enhance your app's experience by adding a unique touch to your notifications. You can set a specific sound for all notifications or just for certain ones, depending on the action.  \n  \n**For example:** for emergency alerts, \"Hospital Emergency\" might play an ambulance siren sound, making the notifications more attention-grabbing. Meanwhile, social networking apps might use custom sounds exclusively for messages, allowing users to instantly recognize personal interactions and distinguish these alerts from regular system notifications.",
    "2-0": "time_to_live",
    "2-1": "String",
    "2-2": "No",
    "2-3": "You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), APNs will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,592,000 seconds (0 to 30 days). If you don't set a limit, APNS will keep trying to deliver your message for up to 30 days.  \n_**Note**: If the value is set to 0 seconds, the message will expire immediately, and APNs will not store the notification or attempt to redeliver it._",
    "3-0": "customtags",
    "3-1": "JSONObject",
    "3-2": "No",
    "3-3": "Custom tags are flexible and can be crafted to match the specific needs and logic of your business. Simply pass a key-value pair, where the value can be a string, a JSON object, or a JSON array depending on your requirement.",
    "4-0": "collapse_key",
    "4-1": "String",
    "4-2": "No",
    "4-3": "If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in the FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide. This parameter would only work if you use FCM as the Push provider.",
    "5-0": "attachmenturl",
    "5-1": "String",
    "5-2": "No",
    "5-3": "This accepts a URL as a string and this parameter is used for sending images with notifications.",
    "6-0": "notificationaction",
    "6-1": "JSONObject",
    "6-2": "No",
    "6-3": "Define this object to add an action when the notification is clicked. The sub-parameters of this block are:  \n  \n\\_ action  \n  \n\\_ value  \nPlease refer [notificationaction](https://imiconnect-apis-group.readme.io/reference/push#android:~:text=below%20this%20table.-,iOS%20%2D%20notificationaction,-Traditionally%2C%20tapping%20a) section right below this table."
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**iOS - notificationaction**

Traditionally, tapping a push notification simply opens an app. However, modern notifications can offer users much more. With just a tap, you can now provide up to five distinct actions, allowing for immediate and varied responses to notifications without ever opening the app.

```json iOS Push with Notification action - OPEN_URL
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "iOS specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPEN_URL", //Opens the respective link in your browser.
                        "value": "{{url}}" //Accepts a URL as a string when the action is selected as 'OPEN_URL'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json iOS Push with Notification action - OPENWEBVIEW
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{appid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "ios specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPENWEBVIEW", // launches a web view inside your app.
                        "value": "https://www.cisco.com" //Accepts a URL as a string when the action is selected as 'OPENWEBVIEW'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json iOS Push with Notification action - DEEPLINK
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{appid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "ios specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "DEEPLINK", //will take you to destination defined in the link.
                        "value": "{{inappid}}://command/Notifications"
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
"notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json iOS Push with Notification action - OPEN_HTML
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{appid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "ios specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPEN_HTML", // Renders the HTML payload within the app.
                        "value": "<a href=https://www.cisco.com>Click on it for Cisco</a>" // Accpets HTML tags, when the action is selected as 'OPEN_HTML'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```
```json Push with Notification action - OPEN_APP
{
    "deliverychannel": "push", //Mandatory.
    "appid": "{{appid}}", //Mandatory.
    "destination": [
        {
            "userid": [ // You can pass either userid or customerid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "ios": {
                "text": "ios specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "extras": {
                    "notificationaction": { //Define this object to specify an action to be taken when the notification is clicked.
                        "action": "OPEN_APP" //Simply opens the app corresponding to the notification. Does not require value for 'Open_App'.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

The following parameters are part of the **notification action **object, which in turn is part of the **extras **object.

<NotificationActionTable />

<br />

> 📘 Note
> 
> It is not mandatory to define _notification action_. But if you set an _action_, you must specify a \_value \_that is used to complete the configured action. By default Open App is the notificationaction set by iOS for all notification.

### Web

Following are the sample request bodies to send Web Push notifications:

> 📘 Note
> 
> Currently, Web Push notifications are supported only for Chrome and Firefox.

```json Definition
// Web browser notification
{
    "web": {
        "title": "<title text for web browser push message>",
        "text": "<push message text for Web browser>",
        "url": "<URL that opens when message is clicked>",
        "actiontext": "<Specifies the text of the button for safari browsers only>",
        "platorm_types": [
            "chrome",
            "safari",
            "firefox"
        ],
        "extras": {
            "collapse_key": "<Alpha numeric key>", //If two messages have same collapse key, older message is discarded on the end device.
            "time_to_live": "<integer value>", //Number of seconds that a message may be stored if the user is not immediately available. Max of 51840000.
            "customtags": {
                "key1": "object1",
                "key2": {
                    "object2": "val"
                },
                "key3": [
                    "object3",
                    "object4"
                ]
            }
        }
    }
}
```
```json Web Push (Chrome and Firefox)
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "web": {
                "platform_types": [ //This parameter is mandatory; you can specify "Chrome", "Firefox", or any combination of these two to indicate the browser(s) to which the push message will be sent.
                    "firefox",
                    "chrome"
                ],
                "text": "Web Browser specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "url": "https://www.cisco.com" // Specifies the URL that opens when the message is clicked.
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

To send push notifications to web browsers, the following are the parameters in the request body of the Web Push notification:

| Parameter      | Type       | Mandatory | Description                                                                                                                                                                                                                                                                                   |
| :------------- | :--------- | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| platform_types | JSONArray  | Yes       | Specify "Chrome", "Firefox", "Safari", or any combination of these three to indicate the browser(s) to which the message will be sent.                                                                                                                                                        |
| title          | String     | Yes       | A heading is displayed above the top of the notification text to summarize its content or purpose.                                                                                                                                                                                            |
| text           | String     | Yes       | The text for the notification body for a Web browser.                                                                                                                                                                                                                                         |
| url            | String     | No        | URL of the webpage to which a user is redirected upon clicking the notification.                                                                                                                                                                                                              |
| actiontext     | String     | Yes       | It is the customizable label for the button that users can click to interact with the notification. The label provides a better context of the URL to which the user will be redirected. E.g. A notification asking user to create a new account can have a button with the label - 'Sign-Up' |
| extras         | JSONObject | No        | Please refer to the [extras](https://developers.imiconnect.io/reference/push#push--web--extras)                                                                                                                                                                                               |

<br />

#### **push > web > extras**

To manage notification delivery, use the extras object.

```json Web Push (Chrome and Firefox) with extras
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "web": {
                "platform_types": [ //This parameter is mandatory; you can specify "Chrome", "Firefox", or any combination of these two to indicate the browser(s) to which the push message will be sent.
                    "firefox",
                    "chrome"
                ],
                "text": "Web Browser specific text message.", //Mandatory
                "title": "Notification Title", //Optional
                "url": "https://www.cisco.com", // Specifies the URL that opens when the message is clicked.
                "extras": {
                    "collapse_key": "{{collapse_key}}", //Optional. If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide.
                    "time_to_live": "1000", //Optional. You can specify the lifespan of a message. If your message can't be delivered right away (like if a device is off or offline), FCM will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit  from 0 to 2,419,200 seconds (0 to 28 days). If you don't set a limit, FCM will keep trying to deliver your message for up to 4 weeks.
                    "customtags": {
                        "key1": "Value1" // Optional. A user defined key-value pair. The value can be a string or JSON object, or a JSON array.
                    }
                }
            }
        }
    },
    "expiry": "{{expirytime}}", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

<br />

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "collapse_key",
    "0-1": "String",
    "0-2": "No",
    "0-3": "If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in the FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide.  \n  \n_**Note**:The parameter collapse_key does not apply to the Safari browser._",
    "1-0": "time_to_live",
    "1-1": "String",
    "1-2": "No",
    "1-3": "You can specify the lifespan of a message. If your message can't be delivered right away (like if a device is off or offline), FCM will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,419,200 seconds (0 to 28 days). If you don't set a limit, FCM will keep trying to deliver your message for up to 4 weeks.  \n_**Note**: If the value is set to 0 seconds, the message will expire immediately, and FCM will not store the notification or attempt to redeliver it._",
    "2-0": "customtags",
    "2-1": "JSONObject",
    "2-2": "No",
    "2-3": "Custom tags are flexible and can be crafted to match the specific needs and logic of your business. Simply pass a key-value pair, where the value can be a string, a JSON object, or a JSON array depending on your requirement."
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


### interactive

Interactive Notifications are notifications with buttons for additional actions. Users can interact with these notifications without opening the app, allowing them to take immediate and specific actions.<<prodname>> provides a collection of 17 predefined interactive notification types, each designed to address the most commonly observed use cases. Please refer to the [table ](https://imiconnect-apis-group.readme.io/reference/push#interactive:~:text=interactive%3Eactions-,Parameter,-Type), for detailed information on the interactive notification types.

> 📘 Note
> 
> Interactive Push Notifications are supported exclusively for mobile apps and are not available for web push.

Following are the sample request bodies to send interactive push notifications:

```json Push Interactive
{
    "deliverychannel": "push", //Mandatory
    "appid": "{{inappid}}", //Mandatory
    "destination": [
        {
            "userid": [ // You can pass either userid or pushid as a destination.
                "{{userid}}" //Mandatory.
            ]
        }
    ],
    "channels": {
        "push": {
            "android": {
                "text": "Android specific text message 1.", //Mandatory
                "title": "Notification Title" //Optional
            },
            "ios": {
                "text": "Android specific text message.", //Mandatory
                "title": "Notification Title" //Optional
            },
            "interactive": {
                "category": "DOUBLE_YES_NO",
                "pushref": "ui",
                "device_types": [
                    "ios",
                    "android"
                ],
                "actions": [
                    {
                        "action": "OPEN_URL",
                        "value": "https://www.cisco.com",
                        "identifier": "YES",
                        "pos": 1
                    },
                    {
                        "action": "OPEN_APP",
                        "identifier": "NO",
                        "pos": 2
                    }
                ]
            }
        }
    },
    "expiry": "", //Optional. UTC time format.
    "correlationid": "{{correlationid}}", //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "{{callbackData}}", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "{{webhookurl}}", //Optional.
  "notifyurlAuthId": "TNPXXXT09U" //Optional.
}
```

The following parameters are part of the **interactive** parameter block which in turn is part of the **push** block.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "device_types",
    "0-1": "JSONArray",
    "0-2": "Yes, at least one",
    "0-3": "The device types that should receive the interactive notifications. You can pass \"android,\" \"ios,\" or both.  \n  \n  \\_ android  \n  \n  \\_ ios",
    "1-0": "pushref",
    "1-1": "String",
    "1-2": "No",
    "1-3": "This is an optional parameter that can be passed in the interactive object to pass additional context along with the interactive buttons. This parameter is returned as part of the outbound webhook payload of Read Receipts.",
    "2-0": "category",
    "2-1": "String",
    "2-2": "Yes",
    "2-3": "There are 17 predefined interactive notification types, and selecting at least one is mandatory for sending an interactive notification.  \n  \n  \\_     SINGLE_DISMISS  \n  \n  \\_     SINGLE_OPEN  \n  \n  \\_     SINGLE_SUBSCRIBE  \n  \n  \\_     SINGLE_UNSUBSCRIBE  \n  \n  \\_     SINGLE_SHARE  \n  \n  \\_     SINGLE_DEEPLINK  \n  \n  \\_     SINGLE_REPLY  \n  \n  \\_ (   DOUBLE_YES_NO  \n  \n  \\_     DOUBLE_ACCEPT_CANCEL  \n  \n  \\_     DOUBLE_SHARE_CANCEL  \n  \n  \\_     DOUBLE_SHOPNOW_CANCEL  \n  \n  \\_ DOUBLE_LATER_NOW  \n  \n  \\_ DOUBLE_PLAY_NOW_PLAY_LATER  \n  \n  \\_ DOUBLE_OK_LEARN_MORE  \n  \n  \\_ DOUBLE_SUBSCRIBE_UNSUBSCRIBE  \n  \n  \\_ DOUBLE_BUY_NOW_BUY_LATER  \n  \n  \\* DOUBLE_LIKE_SHARE",
    "3-0": "actions",
    "3-1": "JSONArray",
    "3-2": "Yes",
    "3-3": "This is a mandatory JSONArray that varies depending on the selected category. Based on the category chosen, the identifiers, values, and actions may differ. Please refer to the [actions](https://developers.imiconnect.io/reference/push#interactive:~:text=interactive%3Eactions-,Parameter,-Type)."
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**interactive>actions**

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "pos",
    "0-1": "String",
    "0-2": "Yes",
    "0-3": "The button's position or sequence is specified by either 1 or 2.",
    "1-0": "action",
    "1-1": "String",
    "1-2": "No",
    "1-3": "Actions available for the notification buttons are  \n  \n  \\_     DISMISS (Dismisses the notification).  \n  \n  \\_     OPEN_URL (Opens a specified URL, requires a URL to be provided in the value parameter).  \n  \n  \\_     OPEN_APP (Launches the application).  \n  \n  \\_     DEEPLINK (Navigates to a specific page within the app, requires the destination page to be specified in the value parameter).  \n  \n  \\_     OPENWEBVIEW (Opens a URL within an in-app web view, requires a URL to be provided in the value parameter).  \n  \n  \\_     SHARE (Initiates a sharing operation, requires the content intended for sharing to be specified).",
    "2-0": "identifier",
    "2-1": "String",
    "2-2": "No",
    "2-3": "The \"identifier\" depends on the action chosen. For example, if the action is \\_DOUBLE_SHOPNOW_CANCEL_, then identifier 1 corresponds to SHOPNOW, and identifier 2 corresponds to CANCEL. Refer to the description of the category parameter in the [interactive](https://imiconnect-apis-group.readme.io/reference/push#interactive)  section for a detailed list of all identifiers.",
    "3-0": "value",
    "3-1": "String",
    "3-2": "No, unless action is OPEN_URL,  DEEPLINK, OPENWEBVIEW or SHARE",
    "3-3": "The \"value\" specifies the necessary information for the action. For example, if you configure the action as OPEN_URL, then you have to configure the value with a URL such as [www.cisco.com](http://www.cisco.com).  \n_**Note:** If the action is set to  **OPENAPP**, value is not required.\\_"
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]