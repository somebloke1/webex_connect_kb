The Push node enables you to send rich and interactive notifications to mobile and web apps that use <<prodname>> SDKs. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/84ccdc2-Push.jpg",
        "Push.jpg",
        "Screenshot of Push Node."
      ],
      "align": "center",
      "caption": "Push Node"
    }
  ]
}
[/block]


## Prerequisites

1. An **[App Asset](https://developers.imiconnect.io/docs/create-mobile-application-on-imiconnect-platform#create-a-mobile-app-asset-in-webex-connect)** created on <<prodname>>.  
2. **<<prodname>>'s SDK** integrated within your app, with appropriate App ID and Client Key corresponding to the Mobile/Web App Asset configured in <<prodname>>.

> 📘 Note
> 
> The app should have at least one registered user, whose User-ID or Device-ID can be used as a destination.

## Node Configuration

All the parameters and input fields that you need to define within the node window are explained below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b714ffe-Push.jpg",
        "Push Node Window.png",
        "Screenshot of Push Node Configuration Window."
      ],
      "align": "center",
      "border": true,
      "caption": "Push Node Configuration Window."
    }
  ]
}
[/block]


### Destination Type

There are different types of identifiers supported in <<prodname>>, namely: 

- **Customer Id** is a master ID that is linked to all different channel-specific user IDs of a user within the customer profile. <<prodname>>'s customer profile is used to store multiple channel identifiers and customer communication preferences for various customers. It is useful in cross channel communication. For e.g: You want to send an exclusive promo code to a user’s app because of previous positive feedback that they have given via Messenger. If you have the customer profile configured with details of both Facebook Messenger PSID and user Id linked with the same customer Id, you can use the Customer-ID of the user since it will remain constant across both the channels. 
- **UserId** is the identifier specific to Push and In-App channels. This is generally created when a user registers on your mobile/web app. It is stored in the application profile. E.g. $(userid).
- **AndroidPushId** is the identifier for the Android application. E.g. $(android_pushid).
- **iOSPushId** is the identifier for the iOS application. E.g. $(ios_pushid).
- **ChromePushId** is the identifier for the Chrome application. E.g. $(chrome_pushid).
- **FirefoxPushId**  is the identifier for the Firefox application. E.g. $(firefox_pushid).
- **SafariPushId** is the identifier for the Safari application.
- **Topic** is used to broadcast notifications that come under a particular section of interest. Any user who subscribes to a topic starts receiving notifications published to that topic.

> 📘 Note
> 
> The destination type **Topic** is not visible in the list, if the Topic Messaging option is disabled for your tenant.

- **Segment** comes into picture when you want to target users that have subscribed to a specific combination of topics. You can create a segment containing the desired combination of topics and publish notifications to that segment.

> 📘 Note
> 
> The destination type **Segment** is not visible in the list, if the Segment Messaging option is disabled for your tenant

- **HMSPushId** is the identifier for the HMS application

### Destination

This field contains the destination value corresponding to the selected Destination Type. The value can be static or dynamic. For E.g: If the destination type is Customer-ID, the Destination can be kept dynamic by declaring it as $(customerID). 

### Message Configuration

This section explains the elements used to orchestrate the notification:

**Notification Title**

A heading displayed above the top of the notification text to summarize its content or purpose. The message configuration varies for Android, iOS and Web Browsers. Here are the details for each of these.

**Android**

These are Android-specific configurations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0f9211a-9.jpg",
        "",
        "Screenshot of Android Specific Configurations."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Android Specific Configurations."
    }
  ]
}
[/block]


- Notification Body: Enter the text for the notification body for Android. Eg: Hello this is a test push notifications.

- Notification Action: There are five types of actions that can be executed when a user taps on the notification:

  - OPEN_URL - When you select an Open_URL, it requires a URL as action value.  
    Eg: [www.webexconnect.com](http://www.webexconnect.com).
  - OPENWEBVIEW - When you select an OpenWebView, it requires a URL as action value.  
    Eg: [www.webexconnect.com](http://www.webexconnect.com).
  - DEEPLINK - When you select DeepLink, it Requires a deeplink URL as action value.  
    Eg: {{inappid}}://command/Notifications
  - OPEN_HTML - When you select an Open_HTML, it requires an html code to render as action value.  
    Eg: <marquee>WebexConnect</marquee>
  - OPEN_APP - Does not require an action value.

- Sound File (Discontinued): Enter the url of the sound file that must be played during the notification. 

- Collapse Key: Enter Collapse key. For example, Cricket score.  
  If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in the FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide. This parameter would only work if you use FCM as the Push provider.

- Time To Live: Enter the value for time to live in seconds. E.g. 100 seconds.  
  You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), FCM will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,419,200 seconds (0 to 28 days). If you don't set a limit, FCM will keep trying to deliver your message for up to 4 weeks.

- Delay While Idle (Deprecated): In-case when a notification is received, the device is in idle state, you can choose to wait for the user to be active before you display the notification on the device. E.g. 10 seconds.

- Priority: You can define the priority of a notification by assigning an integer from ranging 1 to 5, 5 being the highest. E.g. 4.

- Image URL: Enter the url of the image which is used to send images in the notification. E.g. <https://www.webexconnect.io/image_1>.

- Notification Icon: Enter the URL for the notification icon. Adding an icon for the push notifications creates a unique, branded experience. E.g. <https://www.webexconnect.io/image.svg>

- Notification Channel ID: Enter the channel ID for devices that run on Android Oreo or above. Each notification must be assigned with a channel ID, for example, WebexConnect_Channel.  
  Starting from Android 8.0 (API level 26), all notifications must be assigned to a notification channel; otherwise, they will not appear for the user. Instead of disabling all notifications, users have the option to control notifications by disabling a specific channel within the app. This allows for more granular control over the types of notifications they want to receive. For more information on the Notification Channel, refer to the [Android official documentation](https://developer.android.com/reference/android/app/NotificationChannel).

> 📘 Note
> 
> If a Notification Channel ID is not explicitly passed, the SDK will automatically use the default channel ID. It is mandatory to create a notification channel with the default channel ID within the app so that the notifications sent without any channel ID are displayed using the default channel. Refer to [Push Messaging Guide](https://developers.webexconnect.io/docs/push-messaging-guide#to-register-notification-channel)to know more about how to create a notification channel with the default channel ID.

**iOS**

These are iOS specific configurations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2c6b1fc-10.jpg",
        "",
        "Screenshot of iOS Specific Configurations."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of iOS Specific Configurations."
    }
  ]
}
[/block]


- Attachment Type - Select the required type (Image, Audio, and Video) from the dropdown.
- Attachment URL - Enter the attachment URL. It is used for sending images, audio, and videos with notifications.
- Collapse ID - Enter the unique key. E.g. Cricket score.  
  If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in the FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide. This parameter would only work if you use FCM as the Push provider.
- Notification Body - Enter the text for the notification body for iOS. Eg: Hello this is a test push notifications.
- Notification Action: Select one of the following from dropdown. There are five types of actions that can be executed when a user taps on the notification:
  - OPEN_URL - When you select an Open_URL, it requires a URL as action value.  
    Eg: [www.Webexconnect.com](http://www.Webexconnect.com).
  - OPENWEBVIEW - When you select an OpenWebView, it requires a URL as action value.  
    Eg: [www.webexconnect.com](http://www.webexconnect.com).
  - DEEPLINK - When you select DeepLink, it Requires a deeplink URL as action value.  
    Eg: {{inappid}}://command/Notifications
  - OPEN_HTML - When you select an Open_HTML, it requires an html code to render as action value.  
    Eg: <marquee>WebexConnect</marquee>
  - OPEN_APP - Does not require an action value.
- Notification Value - Enter the URL to be navigated to when the notification is clicked.
- Sound File - Enter the name of the sound file that must be played during the notification. You can pass either 'default' for the standard sound or specify a custom sound. To use the default sound, pass the value 'default,' and the system's default notification sound will be used. To add custom sounds, add the audio files to the Xcode project root. Make sure Add to targets is selected when adding files so that they are automatically added to the bundle resources. External URLs are not supported. You can pass the filename with the extension (newsound.mp3) of the sound file. Custom sounds enhance your app's experience by adding a unique touch to your notifications. You can set a specific sound for all notifications or just for certain ones, depending on the action.
- Badge - Enter the value to be displayed as a badge of the app icon. E.g. 10.
- Silent Push - Set this parameter value to True, then user will not receive a notification of the delivered message, although the app will receive the pushed message. Currently, this feature is not available. Any values passed as True or False will not be considered.
- Time to live: Enter the value for time to live in seconds. The period of time for which a notification would reside in the notification tray. E.g. 100 seconds.  
  You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), APNs will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,592,000 seconds (0 to 30 days). If you don't set a limit, APNS will keep trying to deliver your message for up to 30 days.

**Webpush**

These are Web-specific configurations. For Webpush, you first need to select all the browsers to be targeted. Following are the available options: 

- Firefox and Chrome
- Safari

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f25d183-11.jpg",
        "",
        "Screenshot of Web Specific Configurations."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Web Specific Configurations."
    }
  ]
}
[/block]


- For Firefox and Chrome:
  - Notification Body: Enter the text for the notification body for Webpush. Eg: Hello this is a test push notifications.
  - Notification Title: Enter the title for the notification. A heading displayed above the top of the notification text to summarize its content or purpose. Eg: Seasonal Sale
  - Time To Live: Enter the value for time to live in seconds. The period of time for which a notification would reside in the notification tray. E.g. 100 seconds.  
    You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), APNs will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,592,000 seconds (0 to 30 days). If you don't set a limit, APNS will keep trying to deliver your message for up to 30 days.
  - On Click URL: Enter the URL to navigate when clicked on notification.
  - Collapse Key: Enter Collapse key. E.g. Cricket score.  
    If you send multiple push notifications to a device with the same collapse key, and all of them are waiting in the FCM server to be delivered to the device, FCM will only send the latest push notification for the collapse key you provide. This parameter would only work if you use FCM as the Push provider.
- For Safari: 
  - Notification Body: Enter the text for the notification body for Webpush. Eg: Hello this is a test push notifications.
  - Notification title: Enter the title for the notification. A heading displayed above the top of the notification text to summarize its content or purpose. Eg: Seasonal Sale.
  - Time to live: Enter the value for time to live in seconds. The period of time for which a notification would reside in the notification tray. E.g: 100 seconds.  
    You can specify the lifespan of a message. If your message can't be delivered right away (like if a phone is off or offline), APNs will hold onto it and try again later. But some messages, like video call alerts or event invites, are only useful for a short time. For those, you can set a time limit from 0 to 2,592,000 seconds (0 to 30 days). If you don't set a limit, APNS will keep trying to deliver your message for up to 30 days.
  - On Click URL: Enter the URL to navigate when clicked on notification. Eg: [www.webexconnect.com](http://www.webexconnect.com).
  - Action Text: Enter the action text. It is the customizable label for the button that users can click to interact with the notification. The label provides a better context of the URL to which the user will be redirected. E.g. A notification asking user to create a new account can have a button with the label - 'Sign-Up'.

> 📘 Note
> 
> Currently, Web Push notifications are supported only for Chrome and Firefox.

**Interactions**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/55d43fa-12.jpg",
        "",
        "Screenshot of Interactions Configurations."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Interactions Configurations."
    }
  ]
}
[/block]


- OS - the operating system for the interactions. You can select iOS, Android, or All.
- Push Reference - Enter the unique value to make interaction result available as a trigger.
- Interactions - Select single button or two buttons. For more information refer the below table.
- Category - Based on the Category selected, the actions for the buttons vary. The available category for interactions are Single button and Two buttons. For more information refer the below table.
- Button Actions - Select the appropriate action. Based on the action selected, the Action Parameter field is displayed. For more information refer the below table.
  - Following are the available button actions for both single button and two buttons. Here are some examples of the Action parameter.
    - OPENURL - When you select an Open_URL, it requires a URL as action value.  
      Eg: [www.Webexconnect.com](http://www.Webexconnect.com).
    - OPENAPP - Does not require an action value.
    - DEEPLINK - When you select DeepLink, it requires a deeplink URL as action value.  
      Eg: {{inappid}}://command/Notifications
    - OPENWEBVIEW - When you select an OpenWebView, it requires a URL as action value.  
      Eg: [www.webexconnect.com](http://www.webexconnect.com).
    - SHARE - When you select Share, it requires the content intended for sharing to be specified.
    - TRIVIAL_REPLIES
    - DISMISS -  When you select Dismiss, it dismisses the notification. Does not require an action value.

The following table contains the information about the Category and Actions when a Single button or Two buttons interactions are selected:

[block:parameters]
{
  "data": {
    "h-0": "Interactions",
    "h-1": "Category",
    "h-2": "Button Action 1",
    "h-3": "Button Action 2",
    "0-0": "Single button ",
    "0-1": "Single button - Open  \nSingle button - Share  \nSingle button - Unsubscribe  \nSingle button - Subscribe  ",
    "0-2": "OPENURL  \nOPENAPP  \nDEEPLINK  \nOPENWEBVIEW  \nSHARE  \nTRIVIAL_REPLIES",
    "0-3": "Not Applicable ",
    "1-0": "Single button",
    "1-1": "Single button - Dismiss",
    "1-2": "DISMISS",
    "1-3": "Not Applicable",
    "2-0": "Two buttons",
    "2-1": "Two button - Like or Share  \nTwo button - Ok or Learn More  \nTwo button - Yes or No  \nTwo button - Subscribe or Unsubscribe",
    "2-2": "OPENURL  \nOPENAPP  \nDEEPLINK  \nOPENWEBVIEW  \nSHARE  \nTRIVIAL_REPLIES",
    "2-3": "OPENURL  \nOPENAPP  \nDEEPLINK  \nOPENWEBVIEW  \nSHARE  \nTRIVIAL_REPLIES",
    "3-0": "Two buttons",
    "3-1": "Two button - Buy Now or Buy Later  \nTwo button - Play now or PlayLater  \nTwo button - Later or Now  \nTwo button - Shopnow or Cancel  \nTwo button - Share or Cancel  \nTwo button - Accept or Cancel",
    "3-2": "OPENURL  \nOPENAPP  \nDEEPLINK  \nOPENWEBVIEW  \nSHARE  \nTRIVIAL_REPLIES",
    "3-3": "DISMISS"
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


### Extra Parameters

Along with the message, you can send additional information like some user-specific property, or any custom parameter that is required to display the message in a certain fashion within the app. This information can be sent in the form of extra parameters.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/abee70a-Push.jpg",
        null,
        "Screenshot of Extra Parameters."
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Screenshot of Extra Parameters."
    }
  ]
}
[/block]


**Correlation ID**

You can assign a unique ID of your choice to each Push message. This ID is returned to the platform with the delivery report and can be used to identify the message.

**Callback Data**

In case there is additional data to be sent along with the delivery reports to the URL, you must specify that here.

**Validations forCallback Data & Correlation ID**:

1. Callback Data, Correlation Id fields are optional for all the channels. Send node can be saved without providing these fields.
2. All characters, Alphabets, Numbers, and special characters are accepted.
3. Variables can be added.
4. Hard coded values are accepted.
5. On Platform side, there is no Max or Min length validation for these fields.

**Notify URL**

You can choose to notify a URL with the delivery report for the Push message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.

**Validations for Notify URL**:

- It is an optional field for all the channels. Send node can be executed without including these values.
- The notify URL should be updated with the proper URL format. The system returns the error message when the Notify URL field is not updated correctly as ‘Invalid URL: field accepts only valid URL or variable.’
- When you provide a space in front of the URL, the system displays the 'Invalid URL: field accepts only valid URLs or variables' error message.
- When you provide space at the end of the URL, the system trims and ignores the space, and the URL receives delivery receipts (DRs).
- Select the **Enable Notify URL Auth** checkbox to activate the authentication of the notify URL.
- There is no maximum length validation defined for this field.
- Variables can be added to this field.

> 📘 Note:
> 
> Notify URLs track the status of delivery receipts (DRs) for sent messages.
> 
> If Enable Notify URL Auth is enabled for your node and an Auth ID that is random, invalid, or deleted is used, the payload will be parked in <<prodname>> and not forwarded to the receiver's server. However, this does not impact the delivery of the message.
> 
> If Enable Notify URL Auth is not enabled, the payload is forwarded to the receiver's server regardless of any invalid Auth ID used.

### Advanced Options

**Wait For**

The life-cycle of push notification has three stages. You can wait for a callback at any of the stages before proceeding further in the flow by selecting any one of the following:

1. Gateway Submit: The first stage where the configured message along with the destination is submitted to the gateway for delivery.

2. Delivery Report: The second stage, in which the message is delivered to the targeted device.

3. Success Delivery Receipt: The third stage or option, when selected, the flow execution will only wait for a success Delivery Receipt. It will ignore the failures. If there are no Success Delivery Receipts returned before the expiry, the node will execute from Ontimeout edge.
   > 📘 Note
   > 
   > Success Delivery Receipt is only available as an option if the Destination Type is set as 'UserId'.

4. Read Report: The last stage is when the target user actually reads the message.

**Expiry**

Time in seconds or UTC, after which node session will <<prodname>> and the flow would proceed to the next node.

## Output Variables

You can see the data that this node generates as output variables.

| Output Variable                | Description                                                  | Example                                                                                   |
| :----------------------------- | :----------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| send.sentDateTime              | The date and time on which the message is sent.              | 2019-06-02T17:17:15.575Z                                                                  |
| send.gatewayTid                | The system generated transaction Id received from gateway.   | [{"code":"1001","transid":"48ceebcb-8035-40d0-8f22-3608b915e2b6","description":"Queued"}] |
| send.deliveryStatusDescription | Status of the delivery.                                      | Submitted/Delivered/Read.                                                                 |
| send.deliveryStatusCode        | The status code of the delivery message.                     | 101                                                                                       |
| send.response_data             | The response data received from the user.                    | [{"code":"1001","transid":"48ceebcb-8035-40d0-8f22-3608b915e2b6","description":"Queued"}] |
| send.response_interactive      | Captures if the interactive button in the message is tapped. |                                                                                           |

## Node Outcomes

- onsuccess: Node executed successfully.  
- onsubmit: Submitted to a gateway.  
- ondrsuccess: Received DR for the transaction.  
- Onread: Received RR for the transaction.  
- onpolicyfail: the flow exits through this node outcome when the expiry condition cannot be met.
- ondrfail: Failed to receive DR.
- onerror: the flow exits through this node outcome when there is an error.
- Ontimeout: Session <<prodname>>