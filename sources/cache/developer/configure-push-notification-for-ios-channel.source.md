## Configure Push-Notification for iOS channel

In the pop-up that appears, you can configure iOS push notifications in three different ways. To configure iOS push notifications for any of the three options, select the appropriate option: 

1. [Configure the Firebase Service Account JSON-based push](#firebase-service-account-json-based-push)
2. [APNs](#apple-push-notification-service-apns)
3. [APNs token based push](#apns-token-based-push)

### Firebase Service Account JSON-based push

For more information on obtaining the Firebase Service Account JSON, please refer to the "[Setup Firebase Cloud Messaging Project](https://developers.webexconnect.io/docs/set-up-firebase-cloud-messaging-project)" guide.

If you want to use Firebase Service Account JSON-based push, follow the steps below:

1. Select "Firebase Service Account JSON based push" as the type.
2. Click on "Choose file" and upload the JSON file downloaded from the Firebase Project.
3. Click on "Save".

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/db1622eb20d7ad79ec485ed7ec5e7a5fd8e755422411a49e8349a339e4d506a2-iOS_Push_Notifications.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


### Apple Push Notification Service (APNS)

If you want to use APNS as the Push Notification gateway, follow the steps below:

**Prerequisite**: To create to the certificate, refer to the [iOS SDK Quickstart Guide](https://developers.imiconnect.io/docs/ios-sdk-quickstart-guide#setup-apns) 

1. Enter the Certificate Password.
2. Select APNS Type gateway from dropdown for your project.
   1. Sandbox: Select the Sandbox option to target your development app.
   2. Production: Select the Production option when sending push message to your production ready app.
3. Upload the APNS Certificate file.
4. Enter the Name and click the Validate.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/caf478316d4ae8aa4e69f5b2cad73a15cdfcdc10ee306660e42343e3cbc96ac5-APNS.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


> 📘 Supported Certificate Format
> 
> Currently, `.p12` is the only certificate format supported.

### APNS token based push

**Prerequisite**: To create to the certificate, click the link: [iOS SDK Quickstart Guide](https://developers.imiconnect.io/docs/ios-sdk-quickstart-guide#configuring-ios-p8-key-for-token-based-connection-to-apns)

1. Enter the **KeyId** for the Authentication token.

2. Enter the **Team ID** for your Apple Account. You can find it from “View Account”.

3. Enter the **BundleId** of your **Package** project.

4. Select one of the Gateway from dropdown:
   - **Sandbox**: To target your development app select the Sandbox.
   - **Production**: Select the Production when sending push to your production ready app.

5. Upload the **Private Key** file.

6. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/49522942def1fab1bbe18a69ee198a804fef4334edfc4db6583431f88d781033-APNs_Token_Based.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]