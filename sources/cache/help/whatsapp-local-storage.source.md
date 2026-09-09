## WhatsApp Data Localization

WhatsApp Cloud API Local Storage allows you to control where your message data is stored at rest. Suppose your company is in a regulated industry such as finance, government, or healthcare. In that case, you may prefer to have your message data stored in a specific country when at rest because of regulatory or company policies.

WhatsApp Cloud API provides such an extra layer of data protection by implementing additional data management controls. The local Storage feature comprises of two additional constraints in Cloud API runtime environment:

- **Data-in-use TTL (Time-to-Live):** Whatsapp has been implemented, enforcing how long message content is accessible to Cloud API outside the target jurisdiction while being processed. Cloud API will automatically delete message content from its “data in use” storage (e.g. cache, queues) after 60 minutes. There will be no sensitive message content on the Cloud API US servers after TTL.
- **Data-at-rest location:** WhatsApp has implemented, enforcing which physical location Cloud API is allowed to use as a persistent storage for sensitive message content. Text and media payload of both incoming and outgoing messages will be stored in the Cloud API in-country (non-US) data stores.

You can enable local storage for your phone number during the time of WhatsApp app creation or by browsing to manage app for existing WhatsApp apps and enabling local storage. With such a setting enabled, Cloud API uses a localized storage in the specified country for persisting message content, instead of using its default storage based in the US.

WhatsApp Local Storage feature supplements other Cloud API privacy and security controls, and allows customers to ensure a higher level of compliance with local data protection regulations.

### Localized Data

WhatsApp Cloud API implements localization for message content. The following message flows are covered by Local Storage feature:

- **Outgoing messages:** messages you are sending to recipients with Cloud API
- **Incoming messages:** messages you are receiving back via Cloud API

The Local Storage feature covers the following message types:

- **Text messages:** textual payload (message body) is localized
- **Media messages:** media (audio, document image or video) payload is localized
- **Template messages:** Components with text/media payload are localized

WhatsApp includes a limited set of metadata attributes in the localized data set, in order to correctly associate encrypted localized message payload with the originally processed message and to audit the fact of localization. Metadata is protected with tokenization and encryption by WhatsApp.

The goal of the Local Storage feature is to allow your business to control where your sensitive data-at-rest is stored directly.

### Updating Local Storage

This feature is available for both embedded signup-based WABAs and OBO i.e. manually onboarded WABAs.

**Prerequisites**

- The phone number needs to be verified.

#### **Updating Local Storage for New Asset**

Steps to update local storage for a new asset:

1. Navigate to **Assets** **> Configure New App > WhatsApp **page.
2. Upon verifying the phone number, you can choose toggle on **Local Storage**.
3. Select your preferred **locale** from the drop-down.
4. Click **Save**.

#### ** Updating local storage of an Existing Asset**

Steps to update the local storage of an existing asset:

1. Navigate to **Assets** > **Configure New App** > **WhatsApp **page.
2. If the selected phone number is not verified, you can verify it by choosing **SMS** or **Voice **as the **Verification Method **. Click the **Verify Number **button to verify your account and complete the configuration. The OTP initiates a few minutes after clicking **Verify Number** and is valid within 24 hours after it is initiated. Once the verification is complete, a notification will be displayed on the top of the screen.

   > 🚧 Alert
   > 
   > Verification OTP on Virtual numbers - WhatsApp
   > 
   > If you are using a virtual number, you can face issues receiving verification SMS/Voice OTP. Please contact your regional support contact/account manager for assistance with verifying your number.

   [block:image]{"images":[{"image":["https://files.readme.io/69e56d4eec115169566c170d012397464e7717393cf17a135aff8320c2307672-image.png",null,"Screenshot of the number is not verified."],"align":"center","border":true,"caption":"The number is not verified."}]}[/block]
3. You can toggle **Local Storage **to disable or update the locale only when the phone number is verified successfully. 
4. Click **Save**.
   > 📘 Note
   > 
   > Downtime for the localization update is less then 5 mins.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1e88ec2f28d0d552fbddf6fe12ebe56c841aaa2796aa9cb519a75f1aaf3b714a-image.png",
        null,
        "Screenshot of Localization using Embedded Sign-up "
      ],
      "align": "center",
      "border": true,
      "caption": "Localization using Embedded Sign-up "
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c816b35022aca598ff029352ba23c7bc94dffc07d2a67a9eb65c9140602cb417-image.png",
        null,
        "Screenshot of Localization using Manual Sign-up"
      ],
      "align": "center",
      "border": true,
      "caption": "Localization using Manual Sign-up"
    }
  ]
}
[/block]