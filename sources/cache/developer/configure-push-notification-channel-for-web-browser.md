# Configure Push-Notification channel for Web-browser

Source: https://developers.webexconnect.io/docs/configure-push-notification-channel-for-web-browser
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:39+00:00

## Configure Push-Notification channel for Web-browser

To add a web application in Webex Connect, follow these steps:

1. Select browser and click Configure. The Configure Chrome and Firefox Push Notifications pop-up appears.
2. Enter the following fields to configure Chrome and Firefox browsers:
   1. Website URL: Enter the URL of the website to configure Web Push notification.
   2. Notification Icon: Enter the path of the notification icon. The size of the icon should be 80x80.
   3. Upload Firebase Service Account JSON: Upload the JSON file that contains the private key to access the FCM HTTP v1 API. To generate a new private key, go to Service accounts in your Firebase project settings.
   4. Firebase SDK Snippet: Enter the Firebase SDK Snippet generated in the section [Setup FCM for Chrome and Firefox Browsers](https://developers.imiconnect.io/docs/setup-fcm-for-chrome-and-firefox-browsers)
   5. Click **Save**.



![Configure Chrome and Firefox Push Notifications](https://files.readme.io/908c979-Push5.jpeg)




3. Enter the following fields to configure Safari browser:
   1. Site Name: The name that is entered is displayed on the notification.
   2. Site URL: The URL that is used to validate the identity of the website requesting push notifications using your ID. Only the website that matches the URL can use your Webex Connect ID for push notifications.
   3. Notification Icons: It is mandatory to upload all five icons. Click the respective buttons to upload the icons.
   4. APNS Credentials: Enter the password that is set while generating the certificate in the section  **[Setup APNS for Safari Browser](https://developers.webexconnect.io/docs/setup-apns-for-safari-browser)**. Leave this field blank if the certificate was generated without a password.
   5. Name: Enter the name of the APNS file and click Validate. Once the file is validated, the Valid From, Valid Till, and Identifier are auto populated.
   6. Upload the **.p12** certificate .
   7. Click **Save**.



![Configure Safari Push Notification](https://files.readme.io/5073cbc-web_app_safari.png)




> 📘 Note
> 
> After your configure push notification for web browser, it generates a updated imi-environment.js and manifest.json files, which must be re-downloaded and integrated into your JavaScript SDK.



![Enabling Web Push Notifications generates updated imi-environment.js](https://files.readme.io/4a0175506c05a44f0c0537a3373bb10cc9f7e92787a704a99d416565383d18d4-image.png)

