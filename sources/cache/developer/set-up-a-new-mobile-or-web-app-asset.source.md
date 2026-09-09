To leverage our SDKs within your application, you must first create an app asset within the <<prodname>> platform. The asset configuration determines which SDK features are enabled and available for you to use.

When an app asset is configured the platform will assign an **App ID** and **Client Key**. These credentials must be provided to the SDK by your app and form part of the authentication process with the <<prodname>> platform.

> 🚧 Important!
> 
> For enhanced security you should consider implementing JWT authentication.

In order to send Push Notifications or Live Chat /  In-App messages to your app, the asset must be mapped to a [service](https://help.imiconnect.io/docs/introduction).

> 📘 Note
> 
> Your account administrator should have been provided a URL to the <<prodname>> Portal, this URL is unique to your account. If you do not have your account URL, please contact your account administrator.

## Create a Mobile App Asset in Webex Connect

1. Log in to your <<prodname>> Portal account using your unique account URL.
2. Navigate to **Assets** > **Apps**. The Apps page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/17fd152a08d25c0c9cb5cc7f34ed22ce609ba258354091d54964a5062863d0aa-Apps.png",
        "",
        "Screenshot displaying the Assets Menu."
      ],
      "align": "center",
      "sizing": "800px",
      "border": true,
      "caption": "Screenshot displaying the Assets Menu."
    }
  ]
}
[/block]


3. Click **Configure New App > Mobile / Web.**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5ed464cbc7c5454f01544d877849f5cc70f21afdd2361b918eff446612114786-Configure.jpg",
        "",
        "Screenshot of selecting the Mobile / Web App."
      ],
      "align": "center",
      "sizing": "200em",
      "caption": "Screenshot of selecting the Mobile / Web App."
    }
  ]
}
[/block]


4. In the app configuration screen, enter a name for your app and make a note of **CLIENT KEY** provided within the **Access Credentials** section.

   [block:image]{"images":[{"image":["https://files.readme.io/9938c430e563f7ee8b2f17589c899feffac16a43ae8b512033d3b320a5dc309a-New_assets_step5.png",null,"Screenshot of Configuring New Mobile & Web App Page"],"align":"center","border":true,"caption":"Screenshot of Configuring New Mobile & Web App Page"}]}[/block]
5. In Channels, select one of the following:

   1. **Mobile Push and/or In-App Messaging**
   2. **Web Push and/or Live Chat**
6. Select one of the following:

   1. **Push Notifications**
   2. **Live Chat / In-App Messaging**
7. To initialize the SDK, please use the appropriate configuration file that includes essential details such as the app ID, client key, and environment. Download the corresponding configuration files for Android, iOS and Web SDKs from SDK Configures files section.

   [block:image]{"images":[{"image":["https://files.readme.io/79620aee5f83e23c12fa1097119ed5139184a035e9b3376d9eff9d3a787471be-SDK_Configuration_Files.png",null,"Screenshot of SDK Configuration Files"],"align":"center","border":true,"caption":"Screenshot of SDK Configuration Files"}]}[/block]
8. Configure **Push Notifications** Within the Push Notifications section, hover over the Platform Type and click Configure to configure OS-specific Push Notification settings.
   1. [Configure Push-Notification channel for Android](https://developers.imiconnect.io/docs/configure-push-notification-channel-for-android)
   2. [Configure Push-Notification channel for iOS](https://developers.imiconnect.io/docs/configure-push-notification-for-ios-channel)
   3. [Configure Push-Notification channel for Web-browser](https://developers.imiconnect.io/docs/configure-push-notification-channel-for-web-browser)

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a5cc1757544cc4c7dbd037c0146b1f1287a27d4cdf53e4aea4423d5aab0c49cc-SDK_Configuration_Files_-_Both_options.png",
        "",
        "Screenshot of Push Notifications Section."
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Screenshot of Push and Live Chat / In App Messaging Notifications Section."
    }
  ]
}
[/block]


> 📘 Note
> 
> The information required to configure push notifications for each platform will vary as it is specific to each platform.

9. Configure **Live Chat / In-App Messaging**

| No. | Live Chat / In-App Messaging Settings | Mandatory / Optional | Description                                                                                                                                                                                                                                                                                                  |
| :-- | :------------------------------------ | :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.  | **Transport protocols**               | Mandatory            | Two transport protocols are available for establishing Live Chat / In-App Messaging connection with <<prodname>>. They are Web Socket and MQTT. You can configure them as primary and secondary. In case the connection is not established on the primary protocol, it will fall back to secondary protocol. |
| 2.  | **Use Secured Port**                  | Mandatory            | Enable secured ports to establish Live Chat / In-App Messaging connection on the secured port for MQTT and WebSocket as an extra layer of security.                                                                                                                                                          |
| 3.  | **Enable Payload Encryption**         | Optional             | Enable Live Chat / In-App Messaging payload encryption to encrypt the Live Chat / In-App Messaging payload in transit.                                                                                                                                                                                       |

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c0dfed5e6f38ab397c36d2af94f4a6db4deaec272a133f5c18ed121e7d2d4464-Screenshot_2025-04-16_at_2.00.48_PM.png",
        "",
        "Screenshot of Live Chat / In-App Messaging Section."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Live Chat / In-App Messaging Section."
    }
  ]
}
[/block]


10. **Advanced Settings** You will see the following options under Advanced Settings. Select the required options as per your requirement.

> 📘 **Note**
> 
> Modular SDK for both Android and iOS does not support device attribute monitoring capability.

[block:parameters]
{
  "data": {
    "h-0": "No.",
    "h-1": "Advanced Settings",
    "h-2": "Mandatory/Optional",
    "h-3": "Description",
    "0-0": "1.",
    "0-1": "JWT Authorization -  \na. Symmetric  \nb. Asymmetric",
    "0-2": "Optional",
    "0-3": "a. Symmetric: Configure JWT authorization to provide JWT secret key.  \nb. Asymmetric: Upload the JWK keys.",
    "1-0": "2.",
    "1-1": "Allow Multi User Registrations on Same Device",
    "1-2": "Optional",
    "1-3": "Multi-User Registration allows you to have multiple users registered from a single device at the same time. This will ensure that push notification sent to any of the registered user will be delivered on the device. However if the notification is sent to all the users registered on a device parallelly, you would see duplicate push notifications on that given device.",
    "2-0": "3.",
    "2-1": "Single Device Per User",
    "2-2": "Optional",
    "2-3": "Restricts access to the application to one user per device. If you register on a new device, you will stop receiving push notifications on the older device.",
    "3-0": "4.",
    "3-1": "Server Side Inbox",
    "3-2": "Optional",
    "3-3": "Allows the storage of data on server of <<prodname>>.",
    "4-0": "5.",
    "4-1": "Data Stream",
    "4-2": "Optional",
    "4-3": ""
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


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/67bcc7587705d059073bab85c4aeb7aa0b0061ad41e466efdba58e141d3e4031-Screenshot_2025-04-16_at_2.15.52_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


### JWT Authorization

> 📘 Note
> 
> For existing App Assets, the Symmetric (Legacy) option is enabled by default, and for new App Assets, the Asymmetric option is enabled by default.

When JWT Authorization is enabled, you will see the option to enter the JWT Secret Key. Enter the JWT secret key.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/77bafdc4a187acb2d3a850a492e67d652a17ff82781cf662734fe81b8ac73384-Existing_assets_Standalone.png",
        "",
        "Screenshot of JWT Authorization Section."
      ],
      "align": "center",
      "sizing": "1000px",
      "border": true,
      "caption": "Screenshot of JWT Authorization Section."
    }
  ]
}
[/block]


  For more information, refer to the Public Key Upload Format section below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4c18583a1beea37e35faa65734cde0904c9040c1622a0f60e35ca99baa15128a-New_assets_Standalone.png",
        "",
        "Screenshot of Asymmetric JWT Authorization"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Asymmetric JWT Authorization"
    }
  ]
}
[/block]


#### Public Key Upload Format

The customer uploads the public key as a JSON Web Key (JWK). The following fields are validated by Webex Connect:

```json
{
  "alg": "RS256",
  "e": "AQAB",
  "key_ops": [
    "verify"
  ],
  "kty": "RSA",
  "n": "<base64url-encoded-rsa-modulus>",
  "use": "sig",
  "kid": "3d10c888f998970e70712bcca8e447fa"
}
```

JWK properties are defined in [RFC 7517, Section 4](http://datatracker.ietf.org/doc/html/rfc7517#section-4). Algorithm-specific properties are defined in [RFC 7518](https://datatracker.ietf.org/doc/html/rfc7518).

| Property name | Description                                                                                                                                                                                                                                                 |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alg           | The specific cryptographic algorithm used with the key.                                                                                                                                                                                                     |
| e             | The exponent for the [RSA public key](https://datatracker.ietf.org/doc/html/rfc7518#page-30), represented as a Base64urlUInt-encoded value.                                                                                                                 |
| key_ops       | Specifies the operation for which the key is intended to be used. The supported value is verify, which indicates that the key is used to verify digital signatures. See [RFC 7517, Section 4.3](https://datatracker.ietf.org/doc/html/rfc7517#section-4.3). |
| kty           | Identifies the cryptographic algorithm family used with the key. For this JWK, the value is RSA. See [RFC 7517, Section 4.1](https://datatracker.ietf.org/doc/html/rfc7517#section-4.1)                                                                     |
| n             | The modulus for the [RSA public key](https://datatracker.ietf.org/doc/html/rfc7518#page-30), represented as a Base64urlUInt-encoded value.                                                                                                                  |
| use           | Specifies the intended use of the public key. The value sig indicates that the key is intended for signature verification. See [RFC 7517, Section 4.2](https://datatracker.ietf.org/doc/html/rfc7517#section-4.2).                                          |
| kid           | The key identifier used to match a specific key, for example, during key rotation. See [RFC 7517, Section 4.5](https://datatracker.ietf.org/doc/html/rfc7517#section-4.5).                                                                                  |

10. Finally Click on **Save** to complete your app asset creation process and click the back button, to land on the apps page. You can now see your app listed with an App-ID.

You'll have to embed this APP ID in your app code. You can learn more about it in Quickstart guides available in each SDK documentation.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/710b0f0-Mobile11.jpeg",
        "appID.png",
        "Screenshot of Apps Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Apps Page."
    }
  ]
}
[/block]


To configure a project, visit [Project Setup](doc:quickstart-guide-2#section-project-setup)