# Mobile & Web

Source: https://help.webexconnect.io/docs/mobile-web
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:03+00:00

The Webex Connect iOS and Android SDKs provide a messaging framework for mobile app developers to integrate Webex Connect's Push and Live Chat/InApp messaging services into their mobile applications.

## Push Notifications

A notification alerts a user about relevant and timely events. Notifications are of two types - local notifications and remote notifications.

- A local notification is scheduled by an app and delivered by the platform on the same device, regardless of whether the app is currently running in the foreground. 
- A remote notification is also known as push notification is sent by an app’s remote server to the Push Notification service, which pushes the notification to all devices that have the app installed. For example, a news app that alerts its users with important events as they happen.

> 📘 
> 
> Webex Connect does not support local notifications.

## **Interactive Notifications**

A notification can be interactive or non-interactive. A notification that supports actions is known as an interactive notification. Traditional notifications alert you when a message is received by your device. The notification does not allow you to do anything with the message after reading it.  
To respond to a traditional notification, you have to open the message box and then open the message you received. Finally, click the reply button. <br>

Interactive notifications let you respond without switching between the apps. When you receive a message, you will have one or two buttons configured along with the message. You can click one of the buttons to respond. Interactive notifications are secure and cannot be used to spread malicious activity from one app to another.

## Web Push Notifications

Webex Connect Web Push Notification feature allows you to send notifications to your customers' browsers, even when they are not on your website. The user must 'opt-in' and agree to receive notifications from your website. Once opted to receive notifications, your customers can receive notifications even when the browser is closed. Web Push notifications are supported only on HTTPS sites.

Some advantages of Web Push Notification:

- You can send push notifications to your customers without having any contact details.
- Your customers can receive push notifications even when the website is closed.
- You can send push notifications to those customers that are not on your website.

Web push notification examples:

- A bank can notify customers about their payments.
- A notification can be sent when a particular request or process is complete.
- A sports or news website can send timely updates to its subscribers.

> 📘 Note:
> 
> Web push notifications are not supported in _private browsing mode_.

## SDK Configuration Files

To initialize the SDK, use the appropriate configuration file that includes essential details such as the app ID, client key, and environment. These details uniquely identify your app when communicating with Webex Connect. For seamless integration, refer to the quick start guides available for the [Android](https://developers.webexconnect.io/docs/android-modularization-sdk-quick-start-guide), [iOS](https://developers.webexconnect.io/docs/ios-quick-start-guide), and [JavaScript](https://developers.webexconnect.io/docs/javascript-sdk-quickstart-guide) SDKs.

You can download the corresponding configuration files for Android, iOS and Web SDKs from SDK Configures files section independently from the Push Notifications configuration.



![Screenshot of SDK Configuration Files](https://files.readme.io/a1b46cd3277b194581919cc5211d9b099875870b9a054265d0d666c479adafb6-image.png)




When you click the download icon the SDK file for example,`WebexConnectConfig.plist` gets downloaded onto your local system to the selected folder. 

> 📘 Enabling Web Push Notifications generates updated imi-environment.js
> 
> Android and iOS configuration files do not change based on Push or In-App Messaging settings and require only a one-time download. For Web, the default imi-environment.js supports Live Chat Messaging, but enabling Web Push Notifications generates updated imi-environment.js and manifest.json files, which must be re-downloaded and integrated into your JavaScript SDK.



![Enabling Web Push Notifications generates updated imi-environment.js](https://files.readme.io/e691d0dcc19a0bfbab09f071db35d8db4296dde472cf16282f261ed3decaf6ab-image.png)




The app asset configuration page has been updated to allow downloading the complete config file required for initializing Webex Connect mobile SDKs (Android, iOS and Web SDKs). App developers can now directly embed the downloaded config file in their app code.

## **OS and Browser Support**

Web push notifications are supported on the following OS and browsers:

| OS                                     | Chrome | Firefox | Safari (Not Supported) |
| :------------------------------------- | :----- | :------ | :--------------------- |
| **Windows Desktop (Version 7, 8, 10)** | Yes    | Yes     | No                     |
| **Mac OS X 10.11 (EI Captain)**        | Yes    | Yes     | No                     |
| **Linux (Fedora 24)**                  | Yes    | Yes     | No                     |
| **iOS (9.x)**                          | No     | No      | No                     |
| **Android (5.x)**                      | Yes    | No      | No                     |

> 📘 Note
> 
> At this time, Safari web push notifications are not supported. Our development team is aware of this issue and is actively working on a solution to enable push notifications in Safari. Please stay tuned for updates in the upcoming releases.

## Add a Mobile Application

Before you add a mobile application, the following pre-configuration steps must be completed. The keys that are obtained from these steps are used to configure iOS, Android, and Web platforms.



| iOS | Android |
| --- | --- |
| _ [Setup Your Project](https://developers.imiconnect.io/docs/quickstart-guide-2)  <br>_ [Setup APNs](https://developers.imiconnect.io/docs/setup-apns-for-safari-browser) | [Setup Google Cloud Messaging (FCM)](https://developers.imiconnect.io/docs/setup-fcm-for-chrome-and-firefox-browsers) |




To add a mobile/web application in Webex Connect:

1. On the sidebar, hover your mouse on **Assets** (icon) and click **Apps** The Application screen appears.
2. On the **Apps** dashboard, click **Configure New App**  and select **Mobile/Web**.  
   The **Configure New App - Mobile & Web** allows you to configure push notifications over mobile and web.



| Field | Description |
| --- | --- |
| Name  | Enter a name for the mobile application. |
| Access Credentials | Access credential is used to uniquely identify the app while communicating with Webex Connect. |
| Client Key | The client key is auto-populated. This key along with _App ID_ is used to initialize the SDK. |
| Push Notifications | Configure your push provider's credentials here to allow Webex Connect to send notifications to your app users. Read our SDK quick start guides to know more.  <br>  <br>  _ [**iOS**](#section-apple-firebase-cloud-messaging-fcm)  <br>  _ [**Android**](#section-android-configure-push-notifications)  <br>  _ [**Chrome and Firefox**](#section-chrome-and-firefox-web-configure-push-notifications)  <br>  _ [**Safari**](#section-safari-web-configure-safari-push-notifications) |
| Live Chat/ In App Messaging | Configure Live Chat / InApp messaging |
| **Advanced Settings** |  |
| JWT Authorization | Configure JWT authorization to provide JWT secret key |
| Server Side Inbox | Allows the storage of data on server of Webex Connect. By default it is enabled for all the existing tenants. Only a tenant owner, a full access user, or a limited access user can enable or disable the option.  <br>  <br>Whenever you try to disable this option, a popup with the following message is displayed. You must click **confirm** to enable.  <br>  <br>  \_ Once server side inbox is enabled, all new messages will have a server side copy for future downloads.  <br>  <br>Whenever you try to disable this option, a popup with the following message is displayed. You must click **confirm** to disable.  <br>  <br>  \_ Once Server Side Inbox is disabled, new messages are not stored on server side. These messages will be delivered only once and post that, you must maintain a copy of these messages on your server for future reference.  <br>  <br>The Server Side Inbox option is disabled by default. You must enable the option if you want to use the capability. |
| Allow Multi User Registrations on Same Device | Allows multiple users on the same device for the application |
| Single Device Per User | Restricts access to the application to one user per device. If you register on a new device, you will stop receiving push notifications on the older device.  <br>  <br>You can enable this feature at an app asset level from mobile/web app asset configuration screen. |






![Enabling Single Device Per User](https://files.readme.io/c6bb2e5-3.jpg)






![Enabling Multi User Registrations on Same Device](https://files.readme.io/637158f-2.jpg)




## Configuration for Mobile Push Notifications

Hover the mouse pointer over the platform you want to configure and click the corresponding  **Configure**  next to the Status column.

### iOS

The following configurations are applicable for iOS mobile applications.

> 📘 Note
> 
> Based on the expiry date (Valid Till date), an email is sent to (the owner, full access and limited access users of the tenant) remind you 30, 15, 7, 3, 2, and 1 day(s) before expiry. If you do not upload a valid certificate after the expiry date, another email is sent 1 and 7 days after expiry

### Firebase Cloud Messaging (FCM)

| Field                                | Description                                                                                                                    |
| :----------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Upload Firebase Service Account JSON | You can download the Firebase Service Account JSON file from under the Service accounts tab in the Firebase Developer Console. |
| Permissions                          | Set of permissions that you need to add to the iOS app.                                                                        |

### Apple Push Notification Service (APNS)

For more information, you can refer [iOS SDK Quickstart Guide](https://developers.imiconnect.io/docs/ios-sdk-quickstart-guide).



| Field | Description |
| --- | --- |
| Certificate Password | Certificate password of the APNS. |
| APNS Type | Select the Gateway (production/sandbox).  <br>If you have created Apple Push Notification service SSL for Sandbox, then select Sandbox from the drop-down.  <br>If you have created Apple Push Notification service SSL for Production, then select Production from the drop-down. |
| Drag-and-drop or choose the APNS Certificate file | Select the APNS file you have created. |
| Permissions | Set of permissions that you need to add to the app. |




### Token-based Authentication for APNS

For more information, you can refer [iOS SDK Quickstart Guide](https://developers.imiconnect.io/docs/ios-sdk-quickstart-guide).

The token-based notifications mechanism does not have an expiry as opposed to the certificate-based mechanism.



| Field | Description |
| --- | --- |
| Key ID | The Key ID from Apple Developer Account |
| Team ID | The Team ID from Apple Developer Account |
| Package | An identifier of the topic of the app to which the notifications will be pushed |
| Gateway | The gateway to use for push notifications:  <br>   _ Sandbox  <br>   _ Production |
| Drag and drop or choose the APNS Certificate file | Select the APNS private key file specific to the app. |
| Permissions | Set of permissions that you need to add to the app. |




## Android

The following configurations are applicable for Android mobile applications.

### Configure Push Notifications

For more information, you can refer [Android SDK Quickstart Guide](https://developers.imiconnect.io/docs/quickstart-guide-2).

| Field                                | Description                                                                                                                                                                                                                                                                                |
| :----------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upload Firebase Service Account JSON | You can download the Firebase Service Account JSON file from under the Service accounts tab in the Firebase Developer Console. For more information, refer to [Quickstart guide](https://developers.imiconnect.io/docs/quickstart-guide-2#capture-the-firebase-service-account-json-file). |
| HMS                                  | Huawei Mobile Services (HMS) App ID and App secret allow Webex Connect to submit push notifications to your application. For more information, refer to [Quickstart guide](https://developers.imiconnect.io/docs/quickstart-guide-2#capture-the-huawei-app-id-and-app-secret).              |
| Permissions                          | Set of permissions that you need to add to the app.                                                                                                                                                                                                                                        |

## Web

The following configurations are applicable for Android and iOS web applications:

### Chrome and Firefox (web) - Configure Push Notifications

For more information, you can refer [Javascript SDK Quickstart Guide](https://developers.imiconnect.io/docs/javascript-sdk-quickstart-guide).

| Field                                 | Description                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Website URL                           | Website URL to push the notification.                                                                                                                                                                                                                                                                                                |
| Notification Icon URL                 | URL to fetch the notification icon.                                                                                                                                                                                                                                                                                                  |
| **Firebase cloud messaging settings** | Setting required to configure FCM for Firefox and Chrome.                                                                                                                                                                                                                                                                            |
| Upload Firebase Service Account JSON  | You can download the Firebase Service Account JSON file from under the Service accounts tab in the Firebase Developer Console. For more information, refer to the guide on [setting up FCM on Chrome and Firefox browsers](https://developers.imiconnect.io/docs/quickstart-guide-2#capture-the-firebase-service-account-json-file). |
| Firebase SDK Snippet                  | Under the General settings tab, navigate to Your apps section > SDK setup and configuration section, select **Config** in the Firebase Developer Console. For more information, refer to [Quickstart guide](https://developers.imiconnect.io/docs/setup-fcm-for-chrome-and-firefox-browsers).                                        |

App developers can copy the complete ‘Firebase SDK setup and configuration’ JSON object and re-use it directly instead of filling the individual fields.



![Screenshot of Configure Chrome and Firefox Push Notifications.](https://files.readme.io/21b84d3-4.jpg)




### Safari (web) - Configure Safari Push Notifications

| Field                                             | Description                                                                                          |
| :------------------------------------------------ | :--------------------------------------------------------------------------------------------------- |
| Site Name                                         | Title of the website                                                                                 |
| Site URL                                          | URL of the website                                                                                   |
| Notification Icons                                | Upload notification icons in each placeholder as per the resolution described.                       |
| APNS Credentials                                  | Certificate from the Apple developer account                                                         |
| Drag and drop or choose the APNS Certificate file | A placeholder for the APNS file. When you select the certificate file, it is uploaded to the server. |

## Global  Configuration

## In-App Messaging

In-app messages are notifications displayed while the user is active within the app itself – it can be triggered messages based on user interactions. Examples include popups, yes/no prompts, interstitials, and more.

In-app messaging provides a fast, secure and bi-directional channel of communication on mobile and Web Apps. Push notifications are mandatory for using In-app messaging on mobile platforms to display Push Notification for the messages delivered.

Message delivery is attempted via the primary protocol and in case of failure, the delivery falls back on a lower level of preferences. 



| Field | Description |
| --- | --- |
| Primary Transport Protocol | Message delivery primary transport protocol  <br>_ MQTT  <br>_ Web Socket |
| Secondary Transport Protocol | Message delivery secondary transport protocol. This protocol is used when the primary protocol fails to deliver the message.  <br>_ MQTT  <br>_ Web Socket |
| Use Secured Port | Secured ports to ensure RTM connections are established over a secured protocol for better security.  <br>If enabled, <code>8883</code> is used for MQTT and <code>8884</code> for Web Socket. |
| Enable Payload Encryption | Choose to use AES encryption to encrypt the in-app messaging payload for enhanced security. |




## JWT Authorization

When enabled, all communication from the SDK will be authorized by a valid JWT token. If a JWT token is updated or newly added once an application is live, users who don't update their apps will not be able to receive their messages until they update to the latest version of an application.

| Field          | Description                                                                                        |
| :------------- | :------------------------------------------------------------------------------------------------- |
| JWT Secret Key | When enabled, the gateway calls a third-party JWT API and generates a security token for the user. |

## Multi User Support

You can allow multiple user registrations on the same device by enabling the **Allow Multi User Registrations on Same Device** option. There is no limit on the maximum number of users that you can register on the same device. For the best experience, the maximum number of users registered on the same device simultaneously must be less than 100.<br>

When you allow multiple users on the same device, only one user is active at any given point of time and all other users are in an inactive state. The user states are as defined below:

- Active - The userId for which the `register` method was called last. Both in-app messages and push notifications sent to this **userId** will be received by the user.
- Inactive - All the users registered to a device prior to the last registered user are treated as inactive users unless they are unregistered by calling the `unregister` method. All push notifications sent to these users will be received on the device but in-app messages won't be received unless they register again and come to active mode. For example, if there are 50 users registered on the same device simultaneously, 49 of them will be in _inactive_ mode and 1 will be in _active_ mode. Push notifications sent to all the 50 users will be received, but in-app messages will be received only for the 50th user. 

> 📘 Push Notifications for Multiple Users
> 
> If `n` number of users are registered to a device and push notification is sent to all the `n` users, the device will receive the same push notification `n` times.

> 👍 Delivery of Notifications
> 
> Push notifications are delivered to both active and inactive users, whereas In-app notifications are delivered only to active users. For inactive users, the In-app notifications are delivered when the users become active.

> 📘 Applicable OS
> 
> The multi-user support is available only on **iOS** and **Android**.

## API

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection:Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download](https://www.getpostman.com/) Postman from official site.

## FAQs

You can refer to the [Mobile & Web channels FAQs](https://developers.imiconnect.io/reference/push-and-in-app-messaging-faqs) for contextual information.