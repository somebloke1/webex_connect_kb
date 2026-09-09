With more than 2 billion monthly users and counting, WhatsApp is arguably the most popular consumer messaging and communication app in the market today. This tutorial walks you through the process of configuring your WhatsApp Business Account on <<prodname>>.

## Register for an Official Account on WhatsApp

> 📘 Embedded Sign-Up for WhatsApp Asset Creation
> 
> Please note that we now support and recommend WhatsApp Embedded Sign-Up for adding new WhatsApp assets on <<prodname>>. Manual onboarding option that we supported previously is being phased out and may no longer be available in your tenant. If you need assistance in setting up a WABA, please reach out to the Support Team using the details mentioned in the ‘Contact Support’ section within your ”<<prodname>> account.

You can use a phone number that is already registered in the Android, iPhone, or Business application versions of WhatsApp. However, in order to register this phone number with us, you need to follow the steps below to delete the WhatsApp account associated with that phone number mentioned in the [Migrate an Existing WhatsApp Number to a Business Account](https://help.webexconnect.io/v6.16.0/docs/cce-migrate-an-existing-whatsapp-number-to-a-business-account) page.

## Configure WhatsApp App Asset on Webex Connect

1. To configure the WhatsApp app, sign in to the <<prodname>> platform, go to **Assets** > **Apps **.  

   [block:image]{"images":[{"image":["https://files.readme.io/f0226cf-image.png",null,"Screenshot of Selecting the Apps in the Assets Menu."],"align":"center","border":true,"caption":"Selecting the Apps in the Assets Menu"}]}[/block]
2. On the Apps page, click the **Configure New App** button and choose WhatsApp from the drop-down list of apps.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/68d8369-1.jpg",
        "WA2.jpg",
        "Screenshot of Selecting the WhatsApp Asset in the Configure New App Dropdown."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Selecting the WhatsApp Asset in the Configure New App Dropdown"
    }
  ]
}
[/block]


3. Enter the name of the WhatsApp account in the **Name** field on the **Configure New App** page.
4. Select the Sign-up Method: **[Sign-up with Facebook (Embedded Sign-up Onboarding)](https://help.webexconnect.io/docs/wxcc-whatsapp-asset-creation#embedded-sign-up-onboarding)** or **[Manual](https://help.webexconnect.io/docs/wxcc-whatsapp-asset-creation#manual-sign-up)**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d7913ad-WxccWhatsApp.jpg",
        "Configure WhatsApp.jpg",
        "Screenshot of Configure New WhatsApp App."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configure New WhatsApp App"
    }
  ]
}
[/block]


If you selected **Sign-up with Facebook** in the step 4 above, follow the below embedded signup process.

> 📘 Note
> 
> Manual onboarding may be disabled for your tenant, please proceed with embedded signup to onboard your WhatsApp business.
> 
> The following is the screen for Embedded Sign-up.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7064bc1ba01026098b1b2edab7f176b1aa2e2f7e549254b6a1ee6dbd9b2df10d-b7537de-Screenshot_2024-06-13_at_4.35.47_PM.png",
        "",
        "Screenshot for Embedded Sign-up"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot for Embedded Sign-up"
    }
  ]
}
[/block]


> 📘 Note
> 
> Please note that we do not support appending WhatsApp Location messages to conversations. As a workaround, you must extract the latitude and longitude and provide them as plain text by generating a map URL using Google Maps or a similar service.

## Embedded Sign-up

Using the embedded signup feature, the Business Providers can onboard their businesses directly from their websites to the WhatsApp Business Platform.  

### Prerequisites

The following are the prerequisites for WhatsApp onboarding using embedded signup method: 

- A valid Meta user account. 
- A valid phone number.
  1. You should not have any personal WhatsApp account or WhatsApp Business App associated with this number. To migrate a number, you must first delete that WhatsApp account. For more information, refer to this [Migrate an Existing WhatsApp Number to a Business Account](https://developers.facebook.com/docs/whatsapp/on-premises/get-started/migrate-existing-whatsapp-number-to-a-business-account) page. 
  2. You also must have this number handy, because you’ll receive an SMS or a voice call during the verification process.
     > 📘 WhatsApp Business Number Activity Requirements:
     > 
     > To prevent WhatsApp business numbers from being blocked or deactivated, ensure they remain active by sending at least 3 SMS each month. We recommend using the Event Scheduler to automate this process.  
     > If the business repeatedly violate the [WhatsApp Business Terms of Service](https://www.whatsapp.com/legal/business-terms), such as sending spam, template misclassifications, or high-risk policy categories such as adult content, sale of alcohol and tobacco, drugs, gambling and unsafe supplements, they may start seeing messaging restrictions and eventual block. Find more details on the [WhatsApp Business Platform Policy and Spam Enforcement ](https://developers.facebook.com/docs/whatsapp/overview/policy-enforcement)page.
  3. The number must not be a short code or a toll-free number incapable of receiving an OTP message.
     1. Registering 1-800 and Toll Free Numbers  
        Phone numbers behind an IVR system can be registered, but must be able to accept calls from international numbers and be able to redirect WhatsApp SMS message or voice call to a real person.  
        To register a phone number that is behind an IVR system:  
        If you need to create an allowlist of the WhatsApp number you will receive a call from on your phone number behind an IVR system, please reach out to your support contact.
- In addition, you should be ready with the following details: 
  1. Business Phone Number 
     > 📘 Business Numbers Support
     > 
     > Please note that WhatsApp-provided ‘555’ business numbers are not supported currently.
  2. Company Name 
  3. Representative’s Email Address 
  4. Address 
  5. City 
  6. State / Province / Region Country 
  7. Website 
  8. Business number Display Name 
  9. Business Category 
  10. Business Description

> 📘 Onboarding Government Entities:
> 
> If you intend to onboard a government entity, your WABA may be disabled during the process. Please contact your support representative to raise a manual request with Meta Trust and Safety.

### Embedded Sign-up Onboarding

1. If you select **Sign-in with Facebook**.  
   A pop-up appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1c2225e-WxccWhatsApp1.jpg",
        null,
        "Screenshot of Sign-in with Facebook Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Sign-in with Facebook Page"
    }
  ]
}
[/block]


2. Click **Add WhatsApp Business**. You can use the existing account or create a new account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c742bc10a39a01fffab7eb8249cec6c0dac3bc4e992f95dcb19fd314a1a01661-2.jpeg",
        null,
        "Screenshot of Get Started."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Get Started"
    }
  ]
}
[/block]


3. Click **Get Started**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/95ed1f0c04cb30085b8570754516e4cca17a581e41c7788b8b54a6e334c9ccb9-3.jpeg",
        null,
        "Screenshot of Creating New or Selecting WhatsApp Business account popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Creating New or Selecting WhatsApp Business account popup"
    }
  ]
}
[/block]


4. Click **Continue**.
5. Select the existing **Meta Business Account** or **Create a new Meta business account**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bbbddb3f9ab46933191650d15b7d49bbe24c919d4aeb7b724217a4a37f03e210-4.jpeg",
        null,
        "Screenshot of Creating New or Selecting WhatsApp Business account popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Creating New or Selecting WhatsApp Business account popup"
    }
  ]
}
[/block]


6. Click **Continue**. 
7. Select the existing **WhatsApp Business account (WABA)** or **Create new WhatsApp Business account**.  
   Click **Continue**. A confirmation page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/53d35925571ca14fdce2e7f7e62153dc67a9830d24daf0e9341a2b6a4b1c2837-6.jpeg",
        null,
        "Screenshot of Create new WhatsApp Business account popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Create new WhatsApp Business account popup"
    }
  ]
}
[/block]


8. Click **Continue to Step 2**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4ed7f584eac0354ecbf615fd8cee253594cd7970a595cf62958056cb27726a00-7.jpeg",
        null,
        "Screenshot of Accounts have been set up popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Accounts have been set up popup"
    }
  ]
}
[/block]


9. Select the existing **WhatsApp Business Profile** or **create a profile**.
10. Click **Continue**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bfffc034371c0fd6bb745cf5daed48f442f41e20cccfd06f7947d11569cc2106-10.jpeg",
        null,
        "Screenshot of Create your WhatsApp Business Profile popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Create your WhatsApp Business Profile popup"
    }
  ]
}
[/block]


11. Select the existing WhatsApp number or create a number to integrate to your WhatsApp Business Account and click **Next**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ea1a1b7f544be311d18914fa34e8493f29595bbb3ac71bab19d93f20931877f5-11.jpeg",
        null,
        "Screenshot of Login with Facebook popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Login with Facebook popup"
    }
  ]
}
[/block]


> 📘 Business Numbers Support
> 
> Please note that WhatsApp-provided ‘555’ business numbers are not supported currently.

12. When prompted, enter the **OTP** to confirm the number.
13. The screen shows that the information is being processed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1138197a40e77161029c3ad00eaad0842a82c934631e39bb7f80c81760e5184a-131.jpeg",
        null,
        "Screenshot of Let's get started."
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Let's get started"
    }
  ]
}
[/block]


> 📘 Note
> 
> It is recommended to keep the duration of actions such as creating a business route or creating WABA to a maximum of 30 minutes. Exceeding this time limit may require you to repeat the entire process.

 If there is any delay in redirecting to <<prodname>>, the following screen is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9618b5c36f3fe12c8378c01829e0ede6daef832f74fb079d26678142e3ba734e-image.png",
        null,
        "Screenshot of Being Redirected to Webex Connect."
      ],
      "align": "center",
      "border": true,
      "caption": "Being Redirected to Webex Connect"
    }
  ]
}
[/block]


14. Once the process is done, **Steps to verify your business** screen appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4066ce29c9b5269bc40d4f84ada1d96fdff2867d2ce1bd6f489c9f8a2c897fff-141.jpeg",
        null,
        "Screenshot of Steps to verify your business."
      ],
      "align": "center",
      "sizing": "350px",
      "border": true,
      "caption": "Screenshot of Steps to verify your business"
    }
  ]
}
[/block]


15. Click one of the following:

- **Verify in Facebook**: a new tab opens with the verification screen. Complete the verification. To know more about the process, refer to [WhatsApp Business verification](https://help.webexconnect.io/docs/wxcc-whatsapp-asset-creation#business-verification-and-display-name-review).
- **Done with Verification? Proceed**: takes you to Step 20.
- **Skip Verification**: displays the following screen. Click Proceed.

> 📘 Note
> 
> If you skip the verification, you can only send notifications to two numbers and have 10 customer -initiated conversations. Once you submit the documents for verification, you will be allowed for 1500 customer -initiated conversations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/443db7ab22069d18abc6f5ba1af0e61ba048293159552326edc7f2c1d4681c9d-151.jpeg",
        null,
        "Screenshot of Lets get started."
      ],
      "align": "center",
      "sizing": "450px",
      "border": true,
      "caption": "Screenshot of Lets get started"
    }
  ]
}
[/block]


16. The **Setup process for your WhatsApp Business Account** starts.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/510ceea83044b3097f9f3ba72f738b6ae6635431f53bceb98617cd6597a2111b-16.jpeg",
        null,
        "Screenshot of Getting Started with the Integration."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Getting Started with the Integration"
    }
  ]
}
[/block]


17. On the Fetched WABA ID’s screen, click **Integrate with Webex Connect** associated with the account you would like to integrate.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/99a59ccf21f19ef2f40a2569c1146396082d300ad61a7c83f66a59e7ec63472d-ES_doc_-_2.png",
        null,
        "Screenshot of Integrating WhatsApp Business Account."
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Integrating WhatsApp Business Account"
    }
  ]
}
[/block]


18. Once the permission to manage account is received, the phone numbers associated with the WABA are fetched. Select the number you want to integrate and click **Integrate with Webex Connect**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/48817d8158dd5518d603d55a72fabf43e80201d5cf706f27a8d91a4ccd9bb88f-ES_doc_-_1.png",
        null,
        "Screenshot of Selecting a Phone Number popup."
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Selecting a Phone Number popup"
    }
  ]
}
[/block]


19. Once the pre-approved templates are added and the shared Webex Connect's credit line with WABA is set up, the screen shows a Ready for Setup message.
    > 📘 Note
    > 
    > Credit line cannot be changed after being attached to a WABA. If you have integrated with a different credit line in the past, you must create a new WABA to use <<prodname>>'s credit line and then migrate the phone numbers to the new WABA if needed.
20. Go to your tenant and navigate to **Assets** → **Apps**. Select **WhatsApp** from App Type.
21. Select the WhatsApp number that is integrated using the above steps.
22. On the Mange WhatsApp page: 
    - The credentials that are approved show the **Approved** icon.
    - The credentials that are pending approval show the **Pending-approval** icon.
    - The credentials that are rejected show the **Rejected** icon.

> 📘 Note
> 
> WhatsApp allows you to use two numbers without having to verify, with limited conversations and limited number of transactions.

### What is Phone Number Display Name?

This is the display name which your customers see on your WhatsApp Business profile. Whenever you add a phone number to your WABA, you are prompted to add a display name for it as part of Embedded signup pop-up.

Display names should be related to your business and must not violate WhatsApp Commerce and Business policies.  In addition, the display name must comply with formatting guidelines. Refer to [Display name guidelines](https://www.facebook.com/business/help/757569725593362) for comprehensive guidelines.

> 📘 Note
> 
> The name status shows the status of the current display name.
> 
> Whenever there is a change in the display name, the display name approval happens automatically. Upon approval, the old name will transition to the current name.

### Business verification and Display Name review

Business verification and WhatsApp Business Display name review aren’t required now as a mandatory step to start messaging on WhatsApp. After signup an automated compliance check with the WhatsApp Business Platform Policy is conducted. Following which you can immediately start sending messages to customers but only to a limited number of recipients 

> 📘 When to initiate Business verification?
> 
> You are only required to initiate the business verification process when you’re ready to scale your business-initiated conversations or request to become a [WhatsApp Official Business Account.](https://help.imiconnect.io/docs/whatsapp#request-to-become-whatsapp-official-business-account)

After the business verification is complete, the display name review for all phone numbers associated with your account will be initiated. Once the display name review is initiated, any new display name change will have to be reviewed and approved before it can be used. 

Once the business verification is completed and the display names for all phone numbers are approved, your business can have increased messaging and phone number limits.

_Starting in April 2024_, businesses can scale with more phone numbers and daily conversations by demonstrating a record of quality messaging. This will also allow businesses to complete display name review without having to business verify

Follow [the tips](https://www.facebook.com/business/help/687938765816627?content_id=nYpTi7PjgbK9XvX) for driving high-quality conversations. Businesses can track progress in WhatsApp Manager and will be notified of the increased messaging and phone number limits within WhatsApp manager as well as on their Meta login email address used during Embedded signup Onboarding.

## Manual Sign-up

Using the manual configuration, the user will be able to add WhatsApp numbers to manually onboard WABAs and register assets using Cloud APIs for WhatsApp business messaging. Additionally, we have limited manual onboarding, by making this only available to tenants who have at-least one phone number live with manually onboarded WABA.

> 📘 Note
> 
> With this, we are announcing the deprecation of On-premises APIs for new assets. Existing assets using On-Premises will continue to function as before, but businesses are encouraged to promptly migrate to Cloud APIs to avoid future enforcement.

If you selected **Manual** in the step 4 of the procedure above, follow the below procedure:

1. Enter the name of the WhatsApp account in the **Name** field on the **Configure New App** page.
2. Choose **Manual signup** from Select **Sign Up Method** option.

   [block:image]{"images":[{"image":["https://files.readme.io/4158d92-image.png",null,"Screenshot of Selecting the Manual Sign-up Method."],"align":"center","sizing":"70% ","caption":"Screenshot of Selecting the Manual Sign-up Method"}]}[/block]

   <br />
3. Enter the WhatsApp Business Account ID (**WABA ID**) obtained from the support team/your account manager.
   > 📘 Note
   > 
   > You can create your own template via tools -> templates section in the platform, which needs to be approved by the WhatsApp. Once approved it will be available in the send node. In other words, every template message should be registered in business manager to be send to the customers.
   > 
   > You don't need to manually refresh WhatsApp template registration status.  
   > The status will be refreshed automatically on the UI as soon as WhatsApp provides an update.  
   > You can also view the reason for rejection in case a WhatsApp template is rejected.
4. You can either select the phone number in the **Phone Number** field or **Add a number**.

   [block:image]{"images":[{"image":["https://files.readme.io/97ae9a6-image.png",null,"Screenshot of Credentials Section Select the Phone Number"],"align":"center","sizing":"70% ","caption":"Credentials Section Select the Phone Number"}]}[/block]
5. If the selected phone number is not verified, you can verify it by choosing **SMS** or **Voice **as the **Verification Method **. Click the **Verify Number** button to verify your account and complete the configuration. The OTP initiates a few minutes after clicking **Verify Number** and is valid within 24 hours after it is initiated. Once the verification is complete, a notification will be displayed on the top of the screen.

   > 🚧 Alert
   > 
   > Verification OTP on Virtual numbers - WhatsApp
   > 
   > You may often face issues while receiving authentication OTP from WhatsApp when using virtual numbers. See the following recommendations:
   > 
   > - Use voice call to get your service authenticated for WhatsApp.
   > - Use your own mobile numbers that support both voice and SMS services.
   > - In the United States and Canada, your virtual numbers must be on-boarded as a 10DLC number with a brand and campaign ID before it can be enabled for WhatsApp for Business.
   > - You may experience issues receiving OTPs when using virtual numbers with European country codes. Please confirm with your support contact for further assistance.

   [block:image]{"images":[{"image":["https://files.readme.io/7961f31-image.png",null,"Screenshot of Verify WhatsApp Number"],"align":"center","sizing":"70% ","caption":"Verify WhatsApp Number"}]}[/block]
6. Click **Add Number** to add WhatsApp number to the list. **Add Phone number** that can be seen by people when they chat with you. Enter your **WhatsApp Business Display Name** which should match your business name and adhere to [WhatsApp Business’s display name guidelines](https://help.webexconnect.io/docs/display-name-guidelines) and click Save to capture the WhatsApp number.

   [block:image]{"images":[{"image":["https://files.readme.io/88e994a-image.png",null,"Screenshot of Add WhatsApp Number."],"align":"center","sizing":"70% ","caption":"Add WhatsApp Number"}]}[/block]
7. Toggle on **Data Streams **to choose from available integrations to receive data for events enabled by admin.
8. Click **Create**. You can see your WhatsApp app on the Apps page.

> 📘 Template API usage
> 
> The template should be registered and approved from **Tools -> Templates** section within <<prodname>> platform, before it can be used to send notification messages. You can also use interactive message templates like **Call-To-Action** buttons or **Quick Replies** buttons. You can also use authentication templates for OTP and Auto-fill features.

## Edit/Manage/Delete the WhatsApp App Asset

1. Go to **Assets** > **Apps**.
2. Search for the WhatsApp that you want to edit and click **Manage** in the drop-down list box at the right to manage the settings of this app.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8655ba2-WhatsApp16.jpg",
        "WhatsApp app Edit 1.1.png",
        "Screenshot Highlighting Manage Button for WhatsApp Asset."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Highlighting Manage Button for WhatsApp Asset"
    }
  ]
}
[/block]


You see the **Manage – WhatsApp** page, where you can manage the settings of the app. <br>

> 🚧 Managing WhatsApp account settings
> 
> Please use the Manage - WhatsApp page of the Webex Connect platform for updating the Business Account Settings. Although you can access your WABA from within the WhatsApp Manager portal if you have onboarded using the Embedded signup model, the following updates made from the WhatsApp Manager portal can impact your existing services -  Business Account Settings, Template content, or the two-factor authentication settings.

### Delete WhatsApp App

1. Go to Assets > Apps.
2. Search for the WhatsApp app asset that you want to edit and click **Delete** in the drop-down list box at the right to manage the settings of this app.

> 🚧 Alert
> 
> Please note deleting the phone number from within Connect will not automatically delete the number from WABA, the number will be listed and show up as offline. In order to delete the number and re-use you should disable the two-factor authentication PIN before registering the number again.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f1854661bc4dfba2a2aa06730bf736ac62bc7c30e2b304898dc3893bdae5135d-WhatsApp_app_asset.png",
        "",
        "Screenshot of Deleting WhatsApp app asset."
      ],
      "align": "center",
      "border": true,
      "caption": "Deleting WhatsApp app asset"
    }
  ]
}
[/block]


#### Disable the two-factor authentication PIN from WhatsApp Manager

1. Login to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/phone_numbers) and select your WABA from the WABA drop-down on the top right corner.

   [block:image]{"images":[{"image":["https://files.readme.io/27a16e1-d2464bcc-e8f2-4cab-95ba-e424fa7887b2.png","","Screenshot of Navigating to WhatsAppManager>Phone numbers section"],"align":"center","border":true,"caption":"WhatsApp Manager>Phone numbers"}]}[/block]
2. Search your phone number, and click **Settings** **> Two-Step Verification**.

   [block:image]{"images":[{"image":["https://files.readme.io/df82d84-ed0224ab-4f45-401f-b25d-fa6b9595b205.png","","Screenshot of Settings>Two Step Verification"],"align":"center","border":true,"caption":"Settings>Two Step Verification"}]}[/block]
3. Click **Turn off two-step verification** to disable the PIN. A mail will be sent to your registered email.

   [block:image]{"images":[{"image":["https://files.readme.io/bf50d3b-27889480-eef3-4ad7-97b0-9b48134e8b83.png","","Screenshot of Turn off the two-step verification"],"align":"center","border":true,"caption":"Turn off the two-step verification"}]}[/block]

   [block:image]{"images":[{"image":["https://files.readme.io/463fe75-64f8508a-518a-48e9-b786-60f504ae52bc.png","","Screenshot of Turn off the two-step verification Email Notification"],"align":"center","border":true,"caption":"Turn off the two-step verification Email Notification"}]}[/block]

### WABA Account/number updates

You can view the WABA Status, Number Status, Quality Rating and Messaging Limit metrics as part of the WhatsApp app manage screen.

Following are the parameters of the WABA Account/number updates:

- **WABA Status**: This tracks your WhatsApp Business Account's review status. Status property can have one of the following values: PENDING, APPROVED, or REJECTED.
- **[Name Status](https://help.webexconnect.io/docs/wxcc-whatsapp-asset-creation#business-verification-and-display-name-review)**: This tracks your WhatsApp Business phone number display name status.
- **[Quality Rating](https://help.webexconnect.io/docs/whatsapp-business-phone-number-quality-rating-wxcc)**: Quality rating is based on how recipients have received messages over the past seven days and is weighted by recency. A combination of quality signals from conversations between your business and users determines it. Examples include user feedback signals such as blocks, reports, and the reasons users provide when they block a business.
- **Message Throughput**: This field indicates the number of inbound and outbound messages that can be sent and received on your WhatsApp business number in a second. Please note this limit is subject to the allocated throughput limit for your account, please reach out to your support contact for more information.

  [block:image]{"images":[{"image":["https://files.readme.io/50b08b77af037b10545cecbb7ecb49fe73b18c4ad1dd626e710db031d1ba7b56-image.png",null,"Screenshot of Manage WhatsApp"],"align":"center","border":true,"caption":"Manage WhatsApp"}]}[/block]

### Learn more

- [How to Change Your WhatsApp Business Display Name](https://help.webexconnect.io/docs/how-to-change-your-whatsapp-business-display-name-wxcc) 

- [Display Name Guidelines](https://help.webexconnect.io/docs/display-name-guidelines-wxcc) 

- [Messaging Customers on WhatsApp Business Platform](https://help.webexconnect.io/docs/messaging-customers-on-whatsapp-business-platform-wxcc)

- [WhatsApp Business Phone Number Quality Rating](https://help.webexconnect.io/docs/whatsapp-business-phone-number-quality-rating-wxcc) 

- [Messaging Limits ](https://help.webexconnect.io/docs/messaging-limits-wxcc)

## Using the Channel

### User Preference

WhatsApp offers a feature called Offers and Announcements, which enables users to manage their preferences regarding marketing communications from businesses. Through this setting, WhatsApp users can indicate their level of interest in receiving promotional messages and may also apply a threshold over message delivery by choosing to either stop or resume receiving the marketing messages from businesses. You can capture user preferences through [outbound webhooks](https://developers.webexconnect.io/reference/whatsapp-outbound-webhooks).

> 📘 Note
> 
> Current support for user preference is limited to outbound webhooks only.

### Managing User Preferences for Marketing Messages on WhatsApp

WhatsApp users can use the Offers and announcements setting to express their interest in receiving marketing template messages from the business.

- If a user chooses Not interested, it can affect per-user [marketing template messaging limits](https://help.webexconnect.io/docs/templates-whatsapp#limitation-on-marketing-messages) between you and the user.
- When a user selects Not Interested, a second modal appears, offering them the option to stop delivery of marketing messages entirely. A webhook triggers when a WhatsApp user stops marketing messages.

> 📘 Note
> 
> If <<prodname>> tries to send a message after the user has selected to 'stop' marketing messages, the message will fail with the following error code: 131050.
> 
> User preferences from Meta don’t support Interested/Not Interested user actions as webhook events.

- If the user chooses to Stop marketing messages, attempts to send a marketing template to a WhatsApp user from your business, the API will process the request but not send the message. A webhook triggers when a WhatsApp user stops or resumes marketing messages.

  [block:image]{"images":[{"image":["https://files.readme.io/6443fbbe980a57b22021e56fbee29767bdfde0b4302d7f5d6481af9315448ef8-23225bb4-d738-4347-8a89-ea8f1cc2ccc5.png","","Screenshot of User Preferrence"],"align":"center","caption":"User Prefernce Feature"}]}[/block]

## WhatsApp Official Business Account (OBA) Eligibility and Application Process

If your business wishes to obtain a WhatsApp Official Business Account (OBA) or a blue tick against the business profile, please note that Meta has recently refined the eligibility and application process to make it more selective.

**Eligibility Criteria**

  A business may be considered eligible if it:

- Represents a well-known, reputable, and frequently searched-for brand, organization, or entity.
- Has completed Meta Business Verification
- Has an approved display name and two-step verification enabled for the phone number.
- Complies with the WhatsApp Business Messaging Policy.

**Application Pathway**

1. Through Cisco Support  
   • Cisco may submit OBA applications for a limited number of businesses.  
   • If you meet the above eligibility requirements, please reach out to your Cisco support contact to initiate your application. Cisco will validate eligibility with Meta before proceeding.
2. Government entities and large advertisers  
   • Government accounts or large advertisers with a long-standing relationship with Meta may directly apply for an OBA through WhatsApp Manager, where the option will be visible only for WABAs that are eligible.
3. Businesses with a direct commercial relationship with Meta  
   • Companies that work directly with Meta can contact their Meta point of contact (PoC) to request OBA approval.

**Learn more** 

- [How to Change Your WhatsApp Business Display Name](https://help.webexconnect.io/docs/how-to-change-your-whatsapp-business-display-name-wxcc) 

- [Display Name Guidelines](https://help.webexconnect.io/docs/display-name-guidelines-wxcc) 

- [Messaging Customers on WhatsApp Business Platform](https://help.webexconnect.io/docs/messaging-customers-on-whatsapp-business-platform-wxcc)

- [WhatsApp Business Phone Number Quality Rating](https://help.webexconnect.io/docs/whatsapp-business-phone-number-quality-rating-wxcc) 

- [Messaging Limits ](https://help.webexconnect.io/docs/messaging-limits-wxcc)

## Registering your WhatsApp App Asset with Webex Engage

1. Go to **Assets** > **Apps** > **WhatsApp**.
2. Select the required **WhatsApp** app asset for which you want to register with Webex Engage.
3. Click **Manage** under **Actions**.  
   The **Manage - WhatsApp** page displays.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2be596a-WhatsAppWXCC_Register.jpg",
        "WA4.jpg",
        "Screenshot of Registering your WhatsApp App Asset with Webex Engage."
      ],
      "align": "center",
      "border": true,
      "caption": "Registering your WhatsApp App Asset with Webex Engage"
    }
  ]
}
[/block]


5. Click **Register to Webex Engage**.
6. Select the required service (this should be the <<prodname>> service that would be used for configuring WhatsApp flows for Webex Contact Center) and click **Register**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3f1d584-WhatsAppWXCC_Register1.jpeg",
        "WA5.jpg",
        "Screenshot of Registering WhatsApp App Asset with Webex Engage popup"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Registering WhatsApp App Asset with Webex Engage popup"
    }
  ]
}
[/block]


A message displays “Asset registered successfully”. This completes the asset registration for Webex Engage.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/910d6f5-WhatsAppWXCC_Register2.jpg",
        "WA6.jpg",
        "Screenshot Displaying List of WhatsApp Assets"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Displaying List of WhatsApp Assets"
    }
  ]
}
[/block]


As shown above, you will see a Webex Engage icon and a PCI check-enabled flag next to the App name once it's been successfully mapped with Cisco Webex Contact Center.

> 📘 Entrypoint Configuration
> 
> Once the asset is registered on <<prodname>>, the entry point mapping should be done on the Cisco Webex Contact Center portal as well.

## Business Account Settings

You can register the details of the business account like the **About**, **Address**, **Business Category**, **Contact Email**, **Business Description**, **Website URL 1** (the primary website), and **Website URL 2** (the secondary website). Click the **Upload** button to browse and select an image that will be displayed as the logo. 

As per the WhatsApp guidelines, when you upload the image, the WhatsApp Business Platform Client will scale and crop the uploaded the profile pic and render it as a square image. Therefore, the image that you use for your business logo must comply with the following:

- Maximum size of 5 MB
- Image height or width not less than 192 px
- Image resolution of 640x640.

These business account settings appear to the users when they view your business profile on WhatsApp.

> 🚧 Managing Business Account Settings
> 
> Please use the Manage - WhatsApp page - Business Account Settings section of the Webex Connect platform to update any Business profile information. Although you can access your WABA from within the WhatsApp Manager portal if you have onboarded using the Embedded signup model, it may impact your existing services.

Refer to the screenshot below:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/671a448-WhatsApp42.jpeg",
        "WhatsApp app Edit 2.2.PNG",
        "Screenshot of Business Account Settings."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Business Account Settings"
    }
  ]
}
[/block]


### Configuring Outbound Webhook for WhatsApp

To configure a Outbound Webhook for WhatsApp:

1. Go to Assets → Apps.
2. Select WhatsApp from the App Type drop-down.
3. Click the number for which you want to enable the Outbound Webhook.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e8df4a8-WhatsApp19.jpg",
        "WhatsApp Outbound Webhooks.jpeg",
        "Screenshot highlighting the Configuring Outbound Webhook Button."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot highlighting the Configuring Outbound Webhook Button"
    }
  ]
}
[/block]


4. Click Configure Outbound Webhooks.  
   Configure New Integration - Outbound Webhook is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e0b2fef-WhatsApp20.jpg",
        "WhatsApp Outbound Webhooks1.jpeg",
        "Screenshot of Configuring New Outbound Webhook Integration."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring New Outbound Webhook Integration"
    }
  ]
}
[/block]


5. Enter the **Name** for the webhook.
6. Entity is automatically populated.
7. Select the notifications you want to receive – **Incoming Message**, **Postback**, **List Message**, and/or **Reply Buttons Message**.
8. Enter the webhook URL for the **Endpoint Configuration**.
9. Select **Enable Hub Signature** if you want to enable the hub signature and enter all the relevant details.
10. Click **Save**.