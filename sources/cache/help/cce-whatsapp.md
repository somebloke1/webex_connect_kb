# WhatsApp - CCE

Source: https://help.webexconnect.io/docs/cce-whatsapp
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:20+00:00

With more than 2 billion monthly users and counting, WhatsApp is arguably the most popular consumer messaging and communication app in the market today. This tutorial walks you through the process of configuring your WhatsApp Business Account on Webex Connect.

This tutorial is for Cisco Contact Center Enterprise (CCE) users who want to use WhatsApp as a channel of customer support with Webex Contact Center. The first procedure is configuring your WhatsApp Business Account on Webex Connect, and then registering your WhatsApp app on Webex Engage.

You may view the following sections:

- [Register for an Official Account on WhatsApp](https://help.webexconnect.io/docs/whatsapp-cce#register-for-an-official-account-on-whatsapp)
- [Configure WhatsApp App Asset on \<<prodname>](https://help.webexconnect.io/docs/whatsapp-cce#configure-whatsapp-app-asset-on-webex-connect)
  - [Embedded Sign-up](https://help.webexconnect.io/docs/whatsapp-cce#embedded-sign-up)
  - [Manual Sign-up](https://help.webexconnect.io/docs/whatsapp-cce#manual-sign-up)
- [Edit / Manage / Delete a WhatsApp App Asset](https://help.imiconnect.io/docs/whatsapp#editmanagedelete-the-whatsapp-app-asset)
- [Registering your WhatsApp App Asset with Webex Engage](https://help.webexconnect.io/docs/whatsapp-cce#registering-your-whatsapp-app-asset-with-webex-engage)
- [Business Account Settings](https://help.webexconnect.io/docs/whatsapp-cce#business-account-settings)

> 📘 WhatsApp Business Platform vs WhatsApp Business App
> 
> WhatsApp Business Platform allows enterprises with large customer bases to automate customer interactions such as notifications, customer self-service, and enable live-agent assistance using APIs. On the contrary, WhatsApp Business App is a mobile app for small businesses that enables them to build an official presence on WhatsApp and use it for interacting with customers manually.

Interested in our WhatsApp Business Platform? Answer a few short questions [in inquiry form](https://forms.office.com/Pages/ResponsePage.aspx?id=q1SMpQpW1kODQbRs5L6drpepR8VYYI5Lt08n_ihH9TNUN0szNDJSTTIyQkVXUDBVU0xOWkhSUEU3Sy4u) and we'll get in touch with you!

## Register for an Official Account on WhatsApp

> 📘 Embedded Sign-Up for WhatsApp Asset Creation
> 
> Please note that we now support and recommend WhatsApp Embedded Sign-Up for adding new WhatsApp assets on Webex Connect. Manual onboarding option that we supported previously is being phased out and may no longer be available in your tenant. If you need assistance in setting up a WABA, please reach out to the Support Team using the details mentioned in the ‘Contact Support’ section within your ”Webex Connect account.

You can use a phone number that is already registered in the Android, iPhone, or Business application versions of WhatsApp. However, in order to register this phone number with us, you need to follow the steps below to delete the WhatsApp account associated with that phone number mentioned in the [Migrate an Existing WhatsApp Number to a Business Account](https://help.webexconnect.io/v6.16.0/docs/migrate-an-existing-whatsapp-number-to-a-whatsapp-business-account) page.

## Configure WhatsApp App Asset on Webex Connect

1. To configure the WhatsApp app, sign in to the Webex Connect platform, go to **Assets** > **Apps **.  

   

![Assets - Apps navigation](https://files.readme.io/f0226cf-image.png)


2. On the Apps page, click the **Configure New App** button and choose WhatsApp from the drop-down list of apps.



![New app configuration - WhatsApp](https://files.readme.io/e2a2025-1.jpg)




3. Enter the name of the WhatsApp account in the **Name** field on the **Configure New App** page.
4. Select the Sign-up Method: **Sign-up with Facebook** or **Manual**.



![Sign-up with Facebook option](https://files.readme.io/9ffe22e-WxccWhatsApp.jpg)




If you selected **Sign-up with Facebook** in the step 4 above, follow the below embedded signup process.

> 📘 Note
> 
> Manual onboarding may be disabled for your tenant, please proceed with embedded signup to onboard your WhatsApp business.
> 
> The following is the screen for Embedded Sign-up.



![Screenshot for Embedded Sign-up ](https://files.readme.io/cb69885d369c709bb5e2f2f9e59cbbb72e9fa7aed31dc7600b39cc18bc7413be-b7537de-Screenshot_2024-06-13_at_4.35.47_PM.png)




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



![Sign-in with Facebook option](https://files.readme.io/1c2225e-WxccWhatsApp1.jpg)




2. Click **Add WhatsApp Business**. You can use the existing account or create a new account.



![Adding WhatsApp Business account](https://files.readme.io/afe318c-WhatsApp27.jpeg)




3. Click **Get Started**.



![Getting Started](https://files.readme.io/01a0ca2-WhatsApp28.jpeg)




4. Click **Continue**.
5. Select the existing **Meta Business Account** or **Create a new Meta business account**.



![Selecting an account](https://files.readme.io/4861103-WhatsApp29.jpeg)




6. Click **Continue**. 
7. Select the existing **WhatsApp Business account (WABA)** or **Create new WhatsApp Business account**.  
   Click **Continue**. A confirmation page appears.



![Selecting an existing account or creating a new one](https://files.readme.io/62bddb6-WhatsApp30.jpeg)




8. Click **Continue to Step2**.



![Account setup](https://files.readme.io/5c41c86-WhatsApp31.jpeg)




9. Select the existing **WhatsApp Business Profile** or **create a profile**.
10. Click **Continue**.



![Selecting or creating a profile](https://files.readme.io/cfc37ca-WhatsApp32.jpeg)




11. Select the existing WhatsApp number or create a number to integrate to your WhatsApp Business Account and click **Next**.



![Selecting a number or creating a new number](https://files.readme.io/97243eb-WhatsApp33.jpeg)




12. When prompted, enter the **OTP** to confirm the number.
13. The screen shows that the information is being processed.



![Integrating your WhatsApp Business account](https://files.readme.io/cea5adc-WhatsApp43.jpeg)




> 📘 Note
> 
> It is recommended to keep the duration of actions such as creating a business route or creating WABA to a maximum of 30 minutes. Exceeding this time limit may require you to repeat the entire process.

  If there is any delay in redirecting to Webex Connect, the following screen is displayed.



![Being Redirected to Webex Connect](https://files.readme.io/4f5d40c29659eab1609d79e394482955ac0afad661db433de364bfcaeca6cff6-image.png)




14. Once the process is done, **Steps to verify your business** screen appears.



![Steps to verify your business](https://files.readme.io/cdfcb35-WhatsApp34.jpeg)




15. Click one of the following:

- **Verify in Facebook**: a new tab opens with the verification screen. Complete the verification. To know more about the process, refer to the [WhatsApp Business verification](https://help.imiconnect.io/docs/whatsapp#business-verification-and-display-name-review) instructions.
- **Done with Verification? Proceed**: takes you to Step 20.
- **Skip Verification**: displays the following screen. Click Proceed.
  > 📘 Note
  > 
  > If you skip the verification, you can only send notifications to two numbers and have 10 customer -initiated conversations. Once you submit the documents for verification, you will be allowed for 1500 customer -initiated conversations.



!['Let's get started' screen](https://files.readme.io/6795a2b-WhatsApp35.jpeg)




16. The **Setup process for your WhatsApp Business Account** starts.



![Setup process screen](https://files.readme.io/70bd74c-WhatsApp36.jpeg)




17. On the Fetched WABA ID’s screen, click **Integrate with Webex Connect** associated with the account you would like to integrate.



![Integrate with Webex Connect option](https://files.readme.io/baf0467a6921ec5d698922ea5fd53fd38c8492c46bf3fc7a42b820fc6b6eb8a6-ES_doc_-_2.png)




18. Once the permission to manage account is received, the phone numbers associated with the WABA are fetched. Select the number you want to integrate and click **Integrate with Webex Connect**.



![Selecting a phone number](https://files.readme.io/565de74700f0c51e65762a6d55e6699fec0729d866f9835f2cc557583e397b39-ES_doc_-_1.png)




19. Once the pre-approved templates are added and the shared Webex Connet’s credit line with WABA is set up, the screen shows a Ready for Setup message.
    > 📘 Note
    > 
    > Credit line cannot be changed after being attached to a WABA. If you have integrated with a different credit line in the past, you must create a new WABA to use Webex Connect's credit line and then migrate the phone numbers to the new WABA if needed.
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

Display names should be related to your business and must not violate WhatsApp Commerce and Business policies. In addition, the display name must comply with formatting guidelines. Refer to [Display name guidelines](https://www.facebook.com/business/help/757569725593362) for comprehensive guidelines.

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

If you selected **Manual** in the step 4 of the procedure above, follow the below procedure:

1. Enter the name of the WhatsApp account in the **Name** field on the **Configure New App** page.
2. Choose **Manual signup** from Select **Sign Up Method** option.{"images":\[{"image":["https://files.readme.io/9b9a9fc-Assets_WhatsApp_Configure_New_WhatsApp_App.png","Assets WhatsApp Configure New WhatsApp App.png",1609],"align":"center","border":true,"caption":"Configure New WhatsApp App"}]}
3. Enter the WhatsApp Business Account ID (**WABA ID**) obtained from the support team/your account manager.
   > 📘 Note
   > 
   > You can create your own template via tools -> templates section in the platform, which needs to be approved by the WhatsApp. Once approved it will be available in the send node. In other words, every template message should be registered in business manager to be send to the customers.
   > 
   > You don't need to manually refresh WhatsApp template registration status.  
   > The status will be refreshed automatically on the UI as soon as WhatsApp provides an update.  
   > You can also view the reason for rejection in case a WhatsApp template is rejected.
4. You can either select the phone number in the **Phone Number** field or **Add a number**.

   

![Credentials Section Select the Phone Number](https://files.readme.io/97ae9a6-image.png)


5. If the selected phone number is not verified, you can verify it by choosing **SMS** or **Voice **as the **Verification Method **.Click the **Verify Number** button to verify your account and complete the configuration. The OTP initiates few minutes after clicking **Verify Number** and is valid within 24 hours after it is initiated. Once the verification is complete, a notification will be displayed on the top of the screen.

   > 🚧 Alert
   > 
   > **Verification OTP on Virtual numbers - WhatsApp**
   > 
   > You may often face issues while receiving authentication OTP from WhatsApp when using virtual numbers. See the following recommendations:
   > 
   > - Use voice call to get your service authenticated for WhatsApp.
   > - Use your own mobile numbers that support both voice and SMS services.
   > - In the United States and Canada, your virtual numbers must be on-boarded as a 10DLC number with a brand and campaign ID before it can be enabled for WhatsApp for Business.
   > - You may experience issues receiving OTPs when using virtual numbers with European country codes. Please confirm with your support contact for further assistance.

   

![Verify WhatsApp Number](https://files.readme.io/7961f31-image.png)


6. Click **Add Number** to add WhatsApp number to the list. **Add Phone number** that can be seen by people when they chat with you. Enter your **WhatsApp Business Display Name** which should match your business name and adhere to [WhatsApp Business’s display name guidelines](https://help.webexconnect.io/docs/display-name-guidelines) and click Save to capture the WhatsApp number.

   

![Add WhatsApp Number](https://files.readme.io/88e994a-image.png)


7. Toggle on **Data Streams **to choose from available integrations to receive data for events enabled by admin.
8. Click **Create**. You can see your WhatsApp app on the Apps page.

> 📘 Template API usage
> 
> The template should be registered and approved from **Tools -> Templates** section within Webex Connect platform, before it can be used to send notification messages. You can also use interactive message templates like **Call-To-Action** buttons or **Quick Replies** buttons. You can also use authentication templates for OTP and Auto-fill features.

## Local Storage

To enable Local Storage, please refer to [Local Storage setup instructions](https://help.webexconnect.io/docs/whatsapp-local-storage) and follow the steps provided.

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

- [How to Change Your WhatsApp Business Display Name](https://help.imiconnect.io/docs/how-to-change-your-whatsapp-business-display-name) 

- [Display Name and Formatting Guideline](https://help.imiconnect.io/docs/display-name-guidelines) 

- [Start Messaging Customers on WhatsApp Business Platform](https://help.imiconnect.io/docs/start-messaging-customers-on-whatsapp-business-platform)

- [About Your WhatsApp Business Phone Number’s Quality Rating](https://help.imiconnect.io/docs/about-your-whatsapp-business-phone-numbers-quality-rating) 

- [Capacity, Quality Rating, and Messaging Limits ](https://help.imiconnect.io/docs/messaging-limits)

## Registering your WhatsApp App Asset with Webex Engage

1. Go to **Assets** > **Apps** > **WhatsApp**.
2. Select the required **WhatsApp** app asset for which you want to register with Webex Engage.
3. Click **Manage** under **Actions**.  
   The **Manage - WhatsApp** page displays.



![Screenshot of Managing the WhatsApp Page](https://files.readme.io/2be596a-WhatsAppWXCC_Register.jpg)




5. Click **Register to Webex Engage**.
6. Select the required service (this should be the Webex Connect service that would be used for configuring WhatsApp flows for Webex Contact Center) and click **Register**.



![Screenshot of Register to Webex Engage](https://files.readme.io/3f1d584-WhatsAppWXCC_Register1.jpeg)




A message displays “Asset registered successfully”. This completes the asset registration for Webex Engage.



![Screenshot displaying the Webex Engage icon and PCI check enabled flag next to a mapped WhatsApp asset.](https://files.readme.io/910d6f5-WhatsAppWXCC_Register2.jpg)




As shown above, you will see a Webex Engage icon and a PCI check-enabled flag next to the App name once it's been successfully mapped with Webex Contact Center.

> 📘 Note
> 
> This should be the Webex Connect service that would be used for configuring WhatsApp flows for Webex Contact Center.



![Register to Webex Engage screen](https://files.readme.io/2663634-WA5.jpg)




A message displays “Asset registered successfully”. This completes the asset registration for Webex Contact Center.



![Successful mapping of asset](https://files.readme.io/0fa275a-WA6.jpg)




As shown above, you will see a Cisco Webex Contact Center icon and a PCI check enabled flag next to the number once it's been successfully mapped with Webex Contact Center.

> 📘 Entrypoint Configuration
> 
> Once the asset is registered on Webex Connect, the entry point mapping should be done on the Cisco Webex Contact Center portal as well.

## Start messaging immediately

You can start messaging customers immediately and only need to complete Business Verification when you are ready to scale business-initiated conversations or request to become an Official Business Account (OBA).

After completing Embedded Signup or the Manual onboarding (OBO model) processes, businesses can immediately:

- Respond to **unlimited customer-initiated conversations **(24-hour messaging windows).
- Send **business-initiated conversations to 250 unique customers** in a rolling 24-hour period.
- Register up to **two (2) phone numbers.**

## Edit/Manage/Delete the WhatsApp App Asset

1. Go to **Assets** > **Apps**.
2. Search for the WhatsApp that you want to edit and click **Manage** in the drop-down list box at the right to manage the settings of this app.



![Screenshot of Manage WhatsApp asset](https://files.readme.io/8655ba2-WhatsApp16.jpg)




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



![Screenshot of Deleting WhatsApp app asset](https://files.readme.io/f1854661bc4dfba2a2aa06730bf736ac62bc7c30e2b304898dc3893bdae5135d-WhatsApp_app_asset.png)




#### **Disable the two-factor authentication PIN from WhatsApp Manager**

1. Login to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/phone_numbers) and select your WABA from the WABA drop-down on the top right corner.

   

![WhatsApp Manager>Phone numbers](https://files.readme.io/27a16e1-d2464bcc-e8f2-4cab-95ba-e424fa7887b2.png)


2. Search your phone number, and click **Settings** **> Two-Step Verification**.

   

![Two Step Verification process](https://files.readme.io/df82d84-ed0224ab-4f45-401f-b25d-fa6b9595b205.png)


3. Click **Turn off two-step verification** to disable the PIN. A mail will be sent to your registered email.

   

![Turn off two-step verification](https://files.readme.io/bf50d3b-27889480-eef3-4ad7-97b0-9b48134e8b83.png)



   

![Turn off the two-step verification Email Notification](https://files.readme.io/463fe75-64f8508a-518a-48e9-b786-60f504ae52bc.png)



### WABA Account/number updates

You can view the WABA Status, Number Status, Quality Rating and Messaging Limit metrics as part of the WhatsApp app manage screen.

Following are the parameters of the WABA Account/number updates:

- **WABA Status**: This tracks your WhatsApp Business Account's review status. Status property can have one of the following values: PENDING, APPROVED, or REJECTED.
- **[Name Status](https://help.imiconnect.io/docs/whatsapp#business-verification-and-display-name-review)**: This tracks your WhatsApp Business phone number display name status.
- **[Quality Rating](https://help.imiconnect.io/docs/about-your-whatsapp-business-phone-numbers-quality-rating)**: Quality rating is based on how recipients have received messages over the past seven days and is weighted by recency. A combination of quality signals from conversations between your business and users determines it. Examples include user feedback signals such as blocks, reports, and the reasons users provide when they block a business.
- **Message Throughput**: This field indicates the number of inbound and outbound messages that can be sent and received on your WhatsApp business number in a second. Please note this limit is subject to the allocated throughput limit for your account, please reach out to your support contact for more information.



![Manage WhatsApp](https://files.readme.io/2776f26686f9d73fca213c39e0ca21d6370b784a78307221d2fa148c25a19376-image.png)




### Learn more

- [How to Change Your WhatsApp Business Display Name](https://www.facebook.com/business/help/378834799515077)
- [Display Name and Formatting Guideline](https://www.facebook.com/business/help/757569725593362)
- [Start Messaging Customers on WhatsApp Business Platform](https://www.facebook.com/business/help/2640149499569241)
- [About Your WhatsApp Business Phone Number’s Quality Rating](https://www.facebook.com/business/help/896873687365001)
- [Capacity, Quality Rating, and Messaging Limits](https://developers.facebook.com/docs/whatsapp/api/rate-limits)

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



![The business account details](https://files.readme.io/2621d5c-WhatsApp_app_Edit_2.2.PNG)




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
> If Webex Connect tries to send a message after the user has selected to 'stop' marketing messages, the message will fail with the following error code: 131050.
> 
> User preferences from Meta don’t support Interested/Not Interested user actions as webhook events.

- If the user chooses to Stop marketing messages, attempts to send a marketing template to a WhatsApp user from your business, the API will process the request but not send the message. A webhook triggers when a WhatsApp user stops or resumes marketing messages.

  

![User Prefernce Feature](https://files.readme.io/6443fbbe980a57b22021e56fbee29767bdfde0b4302d7f5d6481af9315448ef8-23225bb4-d738-4347-8a89-ea8f1cc2ccc5.png)



### Configuring Outbound Webhook for WhatsApp

To configure a Outbound Webhook for WhatsApp:

1. Go to Assets → Apps.
2. Select WhatsApp from the App Type drop-down.
3. Click the number for which you want to enable the Outbound Webhook.



![Configuring Outbound Webhooks](https://files.readme.io/e8df4a8-WhatsApp19.jpg)




4. Click Configure Outbound Webhooks.  
   Configure New Integration - Outbound Webhook is displayed.



![Configuring Outbound Webhooks](https://files.readme.io/e0b2fef-WhatsApp20.jpg)




5. Enter the **Name** for the webhook.
6. Entity is automatically populated.
7. Select the notifications you want to receive – **Incoming Message**, **Postback**, **List Message**, and/or **Reply Buttons Message**.
8. Enter the webhook URL for the **Endpoint Configuration**.
9. Select **Enable Hub Signature** if you want to enable the hub signature and enter all the relevant details.
10. Click **Save**.