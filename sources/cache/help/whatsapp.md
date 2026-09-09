# WhatsApp

Source: https://help.webexconnect.io/docs/whatsapp
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:04+00:00

With more than 2 billion monthly users and counting, WhatsApp is arguably the most popular consumer messaging and communication app in the market today. This tutorial walks you through the process of configuring your WhatsApp Business Account on Webex Connect.

## Register for an Official Account on WhatsApp

> 📘 Embedded Sign-Up for WhatsApp Asset Creation
> 
> Please note that we now support and recommend WhatsApp Embedded Sign-Up for adding new WhatsApp assets on Webex Connect. Manual onboarding option that we supported previously is being phased out and may no longer be available in your tenant. If you need assistance in setting up a WABA, please reach out to the Support Team using the details mentioned in the ‘Contact Support’ section within your ”Webex Connect account.

You can use a phone number that is already registered in the Android, iPhone, or Business application versions of WhatsApp. However, in order to register this phone number with us, you need to follow the steps below to delete the WhatsApp account associated with that phone number mentioned in the [Migrate an Existing WhatsApp Number to a Business Account](https://help.webexconnect.io/docs/migrate-an-existing-whatsapp-number-to-a-whatsapp-business-account)  page. 

## Configure WhatsApp App Asset on Webex Connect

1. To configure the WhatsApp app, sign in to the Webex Connect platform, go to **Assets** > **Apps **.  



![Selecting the Apps in the Assets Menu](https://files.readme.io/e731cf4-RCS.png)




2. On the Apps page, click the **Configure New App** button and choose WhatsApp from the drop-down list of apps.

   

![Screenshot of Selecting the WhatsApp Asset in the Configure New App Dropdown.](https://files.readme.io/68d8369-1.jpg)


3. Enter the name of the WhatsApp account in the **Name** field on the **Configure New App** page.
4. Select the Sign-up Method: **[Sign-up with Facebook (Embedded Sign-up Onboarding)](https://help.imiconnect.io/docs/whatsapp#embedded-sign-up-onboarding)** or **[Manual](https://help.imiconnect.io/docs/whatsapp#manual-sign-up)**.



![Screenshot of Configure New WhatsApp App.](https://files.readme.io/d9a2421-WxccWhatsApp.jpg)




If you selected** Sign-up with Facebook** in the step 4 above, follow the below embedded signup process.

> 📘 Disabled Manual Onboarding
> 
> Manual onboarding may be disabled for your tenant, please proceed with embedded signup to onboard your WhatsApp business.

The following is the screen for tenants with disabled manual onboarding.



![Screenshot of Configure New WhatsApp App.](https://files.readme.io/b7537de-Screenshot_2024-06-13_at_4.35.47_PM.png)




## Embedded Sign-up

Using the embedded signup feature, the Business can onboard to the WhatsApp Business Platform directly from the Webex Connect WhatsApp App Creation page.  

Embedded Signup reduces onboarding time from days to minutes by simplifying the process and having all the steps (i.e., connecting WhatsApp Business Manager accounts, creating WhatsApp Business Accounts (WABAs), verifying phone numbers) in a single flow.

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
     1. Registering 1-800 and Toll Free Numbers: Phone numbers behind an IVR system can be registered, but must be able to accept calls from international numbers and be able to redirect the OTP message on SMS or Voice to a real person.  
        To register a phone number that is behind an IVR system you will need to create an allowlist of the WhatsApp number you will receive a call from on your phone number behind an IVR system, please reach out to your support contact for more information. 
        > 📘 Using 10DLC Numbers for WhatsApp Business
        > 
        > Businesses seeking a '+1' Country Code business number can utilize a 10DLC number and configure inbound routing capabilities such as Debug Logs, Outbound Webhooks, etc. within Webex Connect to capture OTPs and complete the WhatsApp Embedded Signup onboarding process.
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

1. Select **Sign-in with Facebook** on Select Sign-up Method within the WhatsApp apps page to start with the onboarding process. If Manual Onboarding is disabled you can directly click on Add WhatsApp Business option as mentioned in step 2. 



![Screenshot of Sign-in with Facebook Page.](https://files.readme.io/5e7c96e-WxccWhatsApp1.jpg)




2. Click **Add WhatsApp Business**. You can use the existing account or create a new account.



![Screenshot of Get Started.](https://files.readme.io/0ecb2cefc5db534ef9f728f5d31c613eb8d244a2c0e4c9504dfd1bd89bb18c21-2.jpeg)




3. Click **Get Started**.



![Screenshot of Creating New or Selecting WhatsApp Business account popup.](https://files.readme.io/44e284df84ad5f5579cb0f048d88a2fb8f4dc075028eb9f454ec76ae259f5373-4.jpeg)




4. Click **Continue**.
5. Select the existing **Meta Business Account** or **Create a new Meta business account**.



![Screenshot of Creating New or Selecting WhatsApp Business account popup.](https://files.readme.io/997c129158ca54aa2033d5b91595c5453747c813d3a72f6a8e6e8fd035f4cd5c-5.jpeg)




6. Click **Continue**. 
7. Select the existing **WhatsApp Business account (WABA)** or **Create new WhatsApp Business account**.  
   Click **Continue**. 



![Screenshot of Create new WhatsApp Business account popup.](https://files.readme.io/8282711dab73723b95c4c40dd98b5e0fa39fc9a7f14989705831edb7cb5ab677-6.jpeg)




8. Click **Continue to Step2** to proceed to create or select the WhatsApp Business profile i.e., your WhatsApp Business number specifications. 



![Screenshot of Accounts have been set up popup.](https://files.readme.io/4a6346de2ff044d99da4212ace83b861f331c7a7151392b60e2569255290e534-7.jpeg)




9. Select the existing **WhatsApp Business Profile** or **create a profile**.
10. Click **Continue**.



![Screenshot of Create your WhatsApp Business Profile popup.](https://files.readme.io/b9107f5-3.jpeg)




11. Select the existing WhatsApp number or create a number to integrate to your WhatsApp Business Account and click **Next**. To know more about phone number display name, refer to the [What is Phone Number Display Name?](https://help.imiconnect.io/docs/whatsapp#what-is-phone-number-display-name) section.



![Screenshot of Login with Facebook popup.](https://files.readme.io/81d8806f3639ab4445b226c9d65fb9c0f3264141a5e8b282bc0b657019e56798-11.jpeg)




> 📘 Business Numbers Support
> 
> Please note that WhatsApp-provided ‘555’ business numbers are not supported currently.

12. When prompted, trigger the OTP on SMS or Voice and enter the **OTP** to confirm the number.
13. Permission Acknowledgement: At the end of the flow, review the list of permissions requested by Webex Connect. The permissions cannot be edited. Tap on Continue to acknowledge the permissions and complete Embedded Signup flow. 



![Screenshot of Requesting Permission.](https://files.readme.io/044fe74c67740231fff11097d0e746c39a5ff16db27d558f9ed29009589c0f0a-13.png)




> 📘 Note
> 
> It is recommended to keep the duration of actions such as creating a business route or creating WABA to a maximum of 30 minutes. Exceeding this time limit may require you to repeat the entire process.

  If there is any delay in redirecting to Webex Connect, the following screen is displayed.



![Being Redirected to Webex Connect](https://files.readme.io/25987a9bfb8ffe2166d8ed21d4488dad157ce8ae83345b16c837407dc8029728-image.png)




14. Once the Facebook Login flow is complete, you should see **Steps to verify your business** screen.



![Screenshot of Steps to verify your business.](https://files.readme.io/83c07c10a3bfd4474bb97510fbef563a224534230090a5b893144d8d4a05d9b0-14.jpeg)




15. Click one of the following:

- **Verify in Facebook**: a new tab opens with the verification screen. Complete the verification. To know more about WhatsApp Business verification, refer to the [Business verification and Display Name review](https://help.imiconnect.io/docs/whatsapp#business-verification-and-display-name-review) section.
- **Done with Verification? Proceed**: takes you to Step 20.
- **Skip Verification**: displays the following screen. Click Proceed.
  > 📘 Note
  > 
  > If you skip the verification, you can only add upto 2 phone numbers and your phone numbers will be limited to 250 business-initiated conversations in a 24-hour moving period and unlimited customer-initiated conversations. In-order to [increase your messaging limit](https://help.imiconnect.io/docs/whatsapp-messaging-limits)  please verify your business.

16. The **Setup process for your WhatsApp Business Account** starts.



![Screenshot of Getting Started with the Integration.](https://files.readme.io/7aed5f88c8ae3c4aaf7bd00809dae9e6c8effc3c4cbffa5c9856a48e39a952f5-16.jpeg)




17. On the Fetched WABA ID’s screen, click **Integrate with Webex Connect** associated with the account you would like to integrate.



![Screenshot of Integrating WhatsApp Business Account.](https://files.readme.io/7edea393bff5f55bae40930736201f98c3f85ef483e8f510c2cdfc0290115f81-ES_doc_-_2.png)




18. Once the permission to manage account is received, the phone numbers associated with the WABA are fetched. Select the number you want to integrate and click **Integrate with Webex Connect**.



![Screenshot of Selecting a Phone Number popup.](https://files.readme.io/86a3b5a82b49100e4e0de857a88bb0cdc7c153f5e8d9912526adc24d5efa31cf-ES_doc_-_1.png)




19. We will share Webex Connect Credit line with your WABA to complete the set up, the screen shows a prompt to register the app. Clicking on Create will register your app with Cloud APIs. 
    > 📘 Note
    > 
    > Credit line cannot be changed after being attached to a WABA. If you have integrated with a different credit line in the past, you must create a new WABA to use Webex Connect's credit line and then migrate the phone numbers to the new WABA if needed.

### What is Phone Number Display Name?

This is the display name which your customers see on your WhatsApp Business profile. Whenever you add a phone number to your WABA, you are prompted to add a display name for it as part of Embedded signup pop-up or Manual Sign up.

Display names should be related to your business and must not violate WhatsApp Commerce and Business policies.  In addition, the display name must comply with formatting guidelines. Refer to [Display Name Guidelines](https://help.webexconnect.io/docs/display-name-guidelines) for comprehensive guidelines.

> 🚧 Name Status limitation
> 
> The name status within the Account/Number updates section shows the status of the current display name. Please note this doesn't track the status of the new or updated display name. 
> 
> Whenever there is a change in the display name, the display name is applied automatically after WhatsApp's approval. Please reach out to your support contact if the display name is not updated in WhatsApp mobile application even after approval.

### Business verification and Display Name review

Business verification and WhatsApp Business Display name review aren’t required now as a mandatory step to start messaging on WhatsApp. After signup an automated compliance check with the WhatsApp Business Platform Policy is conducted. Following which you can immediately start sending messages to customers but only to a limited number of recipients.

> 📘 When to initiate Business verification?
> 
> You are only required to initiate the business verification process when you’re ready to scale your business-initiated conversations or request to become a [WhatsApp Official Business Account.](https://help.imiconnect.io/docs/whatsapp#request-to-become-whatsapp-official-business-account)

After the business verification is complete, the display name review for all phone numbers associated with your account will be initiated. Once the display name review is initiated, any new display name change will have to be reviewed and approved before it can be used. 

Once the business verification is completed and the display names for all phone numbers are approved, your business can have increased messaging and phone number limits. For more details, refer to [Messaging Limits](https://help.imiconnect.io/docs/whatsapp-messaging-limits).

_Starting April 2024_, businesses can scale with more phone numbers and daily conversations by demonstrating a record of quality messaging. This will also allow businesses to complete display name review without having to business verify.

Follow [the tips](https://help.webexconnect.io/docs/about-your-whatsapp-business-phone-numbers-quality-rating#improve-your-quality-rating) for driving high-quality conversations. Businesses can track progress in WhatsApp Manager and will be notified of the increased messaging and phone number limits within WhatsApp manager as well as on their Meta login email address used during Embedded signup Onboarding. 

## Manual Sign-up

Using the manual configuration, the user will be able to add WhatsApp numbers to manually onboard WABAs and register assets using Cloud APIs for WhatsApp business messaging. Additionally, we have limited manual onboarding, by making this only available to tenants who have at-least one phone number live with manually onboarded WABA.

If you selected **Manual** in the step 4 of the procedure above, follow the below procedure:

1. Enter the name of the WhatsApp account in the **Name** field on the **Configure New App** page.
2. Choose **Manual signup** from the Select **Sign Up Method** option.
3. Enter the WhatsApp Business Account ID (**WABA ID**) obtained from the support team/your account manager. 
4. You can either select the phone number in the **Phone Number** field or **Add a number**.



![Credentials Section Select the Phone Number](https://files.readme.io/97ae9a6-image.png)




5. If the selected phone number is not verified, you can verify it by choosing **SMS** or **Voice **as the **Verification Method **. Click the **Verify Number** button to verify your account and complete the configuration. The OTP initiates few minutes after clicking **Verify Number** and is valid within 24 hours after it is initiated. Once the verification is complete, a notification will be displayed on the top of the screen.

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

6. Click **Add Number** to add WhatsApp number to the list. **Add Phone number** that can be seen by people when they chat with you. Enter your **[WhatsApp Business Display Name](https://help.imiconnect.io/docs/whatsapp#what-is-phone-number-display-name)** which should match your business name and adhere to [WhatsApp Business’s display name guidelines](https://help.imiconnect.io/docs/display-name-guidelines) and click Save to capture the WhatsApp number.



![Add WhatsApp Number](https://files.readme.io/88e994a-image.png)




7. Toggle on **Data Streams **to choose from available integrations to receive data for events enabled by admin.
8. Click **Create**. You can see your WhatsApp app on the Apps page.

## Local Storage

To enable Local Storage, please refer to this [Local Storage setup guide](https://help.webexconnect.io/docs/whatsapp-local-storage) and follow the steps provided.

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

- [Display Name Guidelines](https://help.imiconnect.io/docs/display-name-guidelines) 

- [Messaging Customers on WhatsApp Business Platform](https://help.imiconnect.io/docs/start-messaging-customers-on-whatsapp-business-platform)

- [WhatsApp Business Phone Number’s Quality Rating](https://help.imiconnect.io/docs/about-your-whatsapp-business-phone-numbers-quality-rating)

- [Messaging Limits ](https://help.imiconnect.io/docs/whatsapp-messaging-limits) 

## Start messaging immediately

You can start messaging customers immediately and only need to complete Business Verification when you are ready to scale business-initiated conversations or request to become an Official Business Account (OBA).

After completing Embedded Signup or the Manual onboarding (OBO model) processes, businesses can immediately:

- Respond to **unlimited customer-initiated conversations **(24-hour messaging windows).
- Send **business-initiated conversations to 250 unique customers** in a rolling 24-hour period.
- Register up to **two (2) phone numbers.**

## Edit/Manage/Delete the WhatsApp App Asset

1. Go to **Assets** > **Apps**.
2. Search for the WhatsApp that you want to edit and click **Manage** in the drop-down list box at the right side of the page, to manage the settings of this app.



![Screenshot Highlighting Manage Button for WhatsApp Asset.](https://files.readme.io/8655ba2-WhatsApp16.jpg)




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



![Deleting WhatsApp app asset](https://files.readme.io/f1854661bc4dfba2a2aa06730bf736ac62bc7c30e2b304898dc3893bdae5135d-WhatsApp_app_asset.png)




#### **Disable the two-factor authentication PIN from WhatsApp Manager**

1. Login to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/phone_numbers) and select your WABA from the WABA drop-down on the top right corner.

   

![WhatsApp Manager>Phone numbers](https://files.readme.io/27a16e1-d2464bcc-e8f2-4cab-95ba-e424fa7887b2.png)


2. Search your phone number, and click **Settings** **> Two-Step Verification**.

   

![Settings>Two Step Verification](https://files.readme.io/df82d84-ed0224ab-4f45-401f-b25d-fa6b9595b205.png)


3. Click **Turn off two-step verification** to disable the PIN. A mail will be sent to your registered email.

   

![Turn off the two-step verification](https://files.readme.io/bf50d3b-27889480-eef3-4ad7-97b0-9b48134e8b83.png)



   

![Turn off the two-step verification Email Notification](https://files.readme.io/463fe75-64f8508a-518a-48e9-b786-60f504ae52bc.png)



### WABA Account/number updates

You can view the WABA Status, Number Status, Quality Rating and Messaging Limit metrics as part of the WhatsApp app manage screen.

Following are the parameters of the WABA Account/number updates:

- **WABA Status**: This tracks your WhatsApp Business Account's review status. Status property can have one of the following values: PENDING, APPROVED, or REJECTED.
- **[Name Status](https://help.imiconnect.io/docs/whatsapp#business-verification-and-display-name-review)**: This tracks your WhatsApp Business phone number display name status.
- **[Quality Rating](https://help.imiconnect.io/docs/about-your-whatsapp-business-phone-numbers-quality-rating)**: Quality rating is based on how recipients have received messages over the past seven days and is weighted by recency. A combination of quality signals from conversations between your business and users determines it. Examples include user feedback signals such as blocks, reports, and the reasons users provide when they block a business.
- **Message Throughput**: This field indicates the number of inbound and outbound messages that can be sent and received on your WhatsApp business number in a second. Please note this limit is subject to the allocated throughput limit for your account, please reach out to your support contact for more information.

  

![Manage WhatsApp](https://files.readme.io/9dddbbd68d677a114309619346c48a693bf7c202c7e429ebfa86fe02e8e5c89a-image.png)



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

Refer to the screenshot below:



![Screenshot of Business Account Settings.](https://files.readme.io/ca0b017-WhatsApp17.jpg)




> 🚧 Managing Business Account Settings
> 
> Please use the Manage - WhatsApp page - Business Account Settings section of the Webex Connect platform to update any Business profile information. Although you can access your WABA from within the WhatsApp Manager portal if you have onboarded using the Embedded signup model, it may impact your existing services.

### Message Us Plugin

The _Message Us_ plugin renders a **Message Us** button on your WhatsApp business profile page. This button, when clicked by the users, enables the users to open a conversation with the business on the configured WhatsApp Business Account. Use the following code sample on your website to allow users to contact you on your configured WhatsApp Business Account through the **Message Us** button.

The below HTML code shows different possible values available for color, size, border radius, etc.

```java Message Us
<div class="wa-message-us" number="<YOUR_WHATSAPP_NUMBER>"
    label="<CUSTOM_BUTTON_LABEL>"
    pre_filled_message="<CUSTOM_PREFILLED_MESSAGE>"
    color="<teal | green | white>"
    size="<standard | compact>"
    border_radius="<VALUE_IN_PX_OR_%>"
    <script src="https://apptray-uk.imiconnect.io/WhatsApp/WhatsAppPlugin.js" type="text/javascript">
    </script>
    </div>
```



![Message Us Plugin](https://files.readme.io/9880d85-WhatsApp18.png)




For e.g. use the following code to generate a standard size WhatsApp Message Us button in green color:

```json Sample
<div class="wa-message-us" number="9180xxxxxxxx"
    label="Message Us"
    pre_filled_message="Hi there"
    color="green"
    size="standard"
    border_radius="5px">
</div>
    <script src="https://apptray-uk.imiconnect.io/WhatsApp/WhatsAppPlugin.js" type="text/javascript">
    </script>
```



![Message Us Button.](https://files.readme.io/cb565fd-WA_MUGreenStandard.PNG)




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



### User Identity

To message users on WhatsApp you will need the users **WA ID**. This is the MSISDN that the customer uses on WhatsApp. The BSUID (Business-scoped User ID) can also be used as the user identity.

### Getting Opt-Ins

You are required to obtain opt-in before opening marketing, utility, and authentication conversations with customers outside the 24-hour window. You can obtain opt-in in a multitude of ways, both on and off WhatsApp.

The following are examples of supported opt-in methods:

- SMS
- Website
- In a WhatsApp thread
- By phone (using an interactive voice response (IVR) flow)
- In person or on paper (customers can sign a physical document to opt in)

We strongly recommend that businesses continue to optimize for the user experience when designing opt-in flows.

### API

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download Postman from here](https://www.getpostman.com/)

### Message Types

WhatsApp supports the following message types:

1. Text
2. Media (Image, Video, Document and Sticker)
3. Location
4. Contact
5. Templates
6. List Messages
7. Reply Buttons 

### Rules

You can configure based on Trigger events to activate the WhatsApp node.



| Trigger event | Action |
| --- | --- |
| Incoming Message | Send WhatsApp Message  <br>Forward to BOT |




### Flow

In a flow, you can configure the [Receive](https://help.imiconnect.io/docs/receive) node to receive messages from WhatsApp users and the [WhatsApp](https://help.imiconnect.io/docs/whatsapp) node enables you to deliver messages to the WhatsApp user.

### Configuring Outbound Webhook for WhatsApp

To configure a Outbound Webhook for WhatsApp:

1. Go to Assets → Apps.
2. Select WhatsApp from the App Type drop-down.
3. Click the number for which you want to enable the Outbound Webhook.



![Screenshot highlighting the Configuring Outbound Webhook Button.](https://files.readme.io/e8df4a8-WhatsApp19.jpg)




4. Click Configure Outbound Webhooks.  
   Configure New Integration - Outbound Webhook is displayed.



![Screenshot of Configuring New Outbound Webhook Integration.](https://files.readme.io/e0b2fef-WhatsApp20.jpg)




5. Enter the **Name** for the webhook.
6. Entity is automatically populated.
7. Select the notifications you want to receive – **Incoming Message**, **Postback**, **List Message**, and/or **Reply Buttons Message**.
8. Enter the webhook URL for the **Endpoint Configuration**.
9. Select **Enable Hub Signature** if you want to enable the hub signature and enter all the relevant details.
10. Click **Save**.

## WhatsApp User Identity Change

WhatsApp enables you to authenticate the identity of the customer to make sure you are communicating with the intended person. For this, WhatsApp uses a unique cryptographic identity hash key for the customer’s phone number.

If there is a change in the customer’s phone number or device (due to theft or change to a new device), WhatsApp considers it as an identity change and updates their Identity Hash. This will change the BSUID of the customer.

When you send a WhatsApp message to that customer including the old hash in the message, the delivery of the message fails because the hashes do not match. An error code is sent to notify you that the delivery has failed. This indicates that the customer’s phone number can no longer be authenticated. To re-authenticate, contact the customer using any of the non-WhatsApp channels and verify the customer’s identity.

After re-authenticating the customer, you can get the new hash key:

- By sending a message to the new identity (if any) without including the hash. You will receive the updated hash as part of the delivery receipt.
- As part of incoming message payload within Outbound webhooks, Export Logs, Debug logs, Start Node, and Receive Node, when the customer messages you.

You can save it for future use and include the new hash in the messages going forward.

## FAQs

You can refer to the [WhatsApp channel FAQs](https://developers.imiconnect.io/reference/whatsapp-faqs) for contextual information.