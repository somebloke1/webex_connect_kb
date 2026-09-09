# Apple Messages for Business

Source: https://help.webexconnect.io/docs/apple-messages-for-business-setup
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:02+00:00

## Creating an Apple Messages for Business application

A Messages for Business application is automatically created within Webex Connect when you register on the [Apple Business Register](https://register.apple.com/business-chat) to create a Messages for Business account and choose Webex Connect as your messaging service provider (MSP).

> 📘 Note
> 
> Please note that Apple Messages for Business commercial accounts that have not registered any activity in the past three months could be scheduled for deactivation by Apple.

## Registering on Apple Messages for Business Register

Before you can offer Messages for Business to your customers, you must register with Apple. You will then need to select an approved Messaging Service Provider (MSP) during registration to use Messages for Business.

To register for a new business account, follow these guides by Apple:

1. [Introduction to Messages for Business](https://register.apple.com/resources/messages/messaging-documentation/)
2. [Onboarding your account](https://register.apple.com/resources/business-chat/BC-OnboardingYourBCA.pdf) 

Once your business account is approved, choose Webex Connect as your MSP platform



![Customer Service Platform Configuration on Apple Business Register](https://files.readme.io/fe4b166-2024-01-10_13-54-57.jpg)




You need an Webex Connect account to complete the linking process. Once successfully linked, you will find your business account under Apps in your Webex Connect account.

> 📘 Note
> 
> - If you do not have an Webex Connect account, register for a free trial on [our website](https://imimobile.com/products/imiconnect) and wait for the approval which takes about 2 hours on a business day.
> - If you are configuring Internal Test Account, and you try the option, 'Test your Messaging Service Provider connection', the Client Landing Page that opens may be invalid due to a limitation from Apple Messages for Business as mentioned [Apple Messages for Business documentation](https://register.apple.com/resources/messages/msp-rest-api/channel-settings#client-landing-page). You will be required to add the text [**&name=<<YourAppName>>**] to the URL at the end.

## Using the channel

### User Identity

To message users on Apple Messages for Business (AMB), you will need the <code>abcId</code> of the users. You will receive this when the customer messages the business account for the first time.

<code>abcId</code> is the Opaque ID unique to the relationship between the customer's Apple ID and the business's business ID.

### Message Types

Apple Messages for Business on Webex Connect supports the following message types -

- Invitation Messages
- Text
- Attachments
- Rich Links
- List Pickers
- Time Pickers
- Text with Attachment
- Form Message
- iMessage App
- Agent Typing Indicators
- Payment Message
- New Authentication Message
- Classical Authentication Message (Please note that this message type has been deprecated by Apple and is no longer supported. Use New Authentication Message type instead). 
- Quick Replies

### Apple Payment Configuration (Optional)

Apple Messages for Business enables you to provide customers with the option to buy products and services using Apple Pay without leaving the conversation. Customers can respond to the payment request using their preferred Apple Pay payment methods. 

#### **Prerequisites**

1. You must have an [ <<Apple Messages for Business>> account](https://developers.imiconnect.io/reference/apple-business-chat-faqs).
2. You must have an Apple Developer account in order to create an Apple Pay Merchant account. If you do not have an Apple Developer account, please set one up at [Apple Developers](https://developer.apple.com/). The approval time may take several days. You will need to get your Merchant ID and Certificate from here.
3. Access to the payment processing endpoint.

#### **Register your Merchant ID on Apple Business Register**

Use the following steps to verify that your Merchant ID is registered with Apple Business Register: 

1. Go to [register.apple.com](http://register.apple.com/) and sign in with your Apple ID as the administrator or technical contact for the business that owns your Apple Pay credentials. 
2. Go to your company’s Business Chat Accounts and find the appropriate business account. If your company has multiple accounts, ensure that you enter the merchant information into the Business Chat account corresponding to your company’s Apple Pay capability. 
3. Edit the Apple Pay section of your Business Chat Account and update your merchant ID. 

#### **Generate the PEM File required by the payment session**

Use the following steps to generate the PEM file required by the payment session: 

1. Download the Merchant Identity Certificate from your Apple Pay developer account to your local file system. 
2. In the Applications folder on Mac, open the Utilities folder and launch Keychain Access. 
3. Add the Merchant Identity Certificate to Keychain Access by opening the certificate file. 
4. In the Keychain Access, find the certificate, and then expand it. You should see a private key. 
5. Hold down the command key and select both the certificate and the private key. 
6. From the Mac Menu select File > Export Items.
7. Select “Personal Information Exchange (.p12)” as File Format and save the .p12 file. 
8. Convert the .p12 file to a .pem file using the following command: 
   ```
   openssl pkcs12 -in <CERT_FROM_KEYCHAIN_EXPORT.p12> -out OUTPUT.pem / -nodes -clcerts
   ```

#### **Configure the App on Webex Connect Platform**

Use the following steps to configure the App on Webex Connect Platform: 

1. Go to the **Assets**>**Apps** page. 
2. Select **Apple Messages for Business** from the **App Type **dropdown.
3. Select the required app and click **Manage ** under **Actions**. 
4. Enable **Payment** toggle and provide the following details that you have obtained here: _Merchant ID_, _Merchant Name_, _Domain Name_  as shown below.

   

![Enable Payment](https://files.readme.io/92b7074-2024-06-06_16h06_55.png)


5. Choose the payment networks allowed by the business in _Supported Networks_. Selection of at least one network is mandatory. 
6. Upload the PEM File that you downloaded. This is the certificate for your business. 
7. The Payment Gateway URL directs the money to your account.  

Optionally, provide values for the following Endpoints. These are a set of URLs used in the payment process. 

1. Shipping Contact Update URL - URL for the customer to update any changes in the shipping address. 
2. Payment Method Update URL – URL to change the payment method. 
3. Fallback URL – a URL to complete the purchase transaction in case of a failed payment.  
4. Order Tracking URL – URL to update the order information after completing the order. 
5. Shipping Method Update URL – URL to change or update the shipping method. 

Once the above steps are configured, you can start using flow nodes to send Apple Pay requests and wait for payment responses to configure your customer journeys. For more information, refer to [Configuring a Payment](https://help.imiconnect.io/docs/apple-messages-for-business#configuring-a-payment).

### Business Logo for Invitation Messages

Apple Messages for Business invitation messages can be sent with or without a brand logo. If you send an invitation message with a brand logo, configure a business logo on the Apple Messages for Business app asset.

Webex Connect uses the configured business logo when you send invitation messages with **Send along with Brand Logo** enabled, or when `withImage` is set to `true` in the API request. If `withImage` is set to `true` and the selected Apple Messages for Business app asset does not have a business logo configured, the invitation message transaction fails.

#### Prerequisites

- You must have an Apple Messages for Business account.
- You must have an Apple Messages for Business app configured in Webex Connect.
- The app asset must be associated with the service used to send Apple Messages for Business invitation messages.

#### Configure the Business Logo

Use the following steps to configure the business logo on the Apple Messages for Business app asset:

1. Go to **Assets** > **Apps**.
2. Select **Apple Messages for Business** from the **App Type** dropdown.
3. Select the required app and click **Manage** under **Actions**.
4. In the **Business Logo (Optional)** section, upload the business logo.
5. Select the PNG file to be used as the business logo.
6. Click **Save**.

After the business logo is saved, you can use the app asset to send invitation messages with a brand logo.

> 📘 Note
> 
> - Only PNG files are supported for the business logo.
> - A square business logo is recommended.
> - The business logo is required only when you send an Apple Messages for Business invitation message with a brand logo.
> - The business logo is not required when you send an invitation message without a brand logo.

### Apple Authentication Configuration (Optional)

Enterprises can send an _authentication_ type message on Apple Messages for Business to prompt the user to login with their credentials right within the message window. This level of authentication opens up a whole new set of sensitive customer support use-cases seamlessly possible.



![Apple Business Register](https://files.readme.io/b2dd215-apple_business_register.png)




#### ** Prerequisites**

- You must have an [Apple Messages for Business account](https://developers.imiconnect.io/reference/apple-business-chat-faqs#registration-for-apple-messages-for-business).

- **OAuth authorization endpoint, OAuth token endpoint, OAuth client ID -** These details need to be entered on your Apple Messages for Business account within Apple Business Register. These details will be provided by you OAuth provider. Below is an example that we setup using LinkedIn’s OAuth service.

- **OAuth client secret -** This needs to be entered on the ‘Manage App’ section of Apple Messages for Business app on Webex Connect UI.



![Enable Authentication](https://files.readme.io/873a5dc-1.jpeg)




Once your authentication configuration is setup on both Apple Business Register and Webex Connect, you can start using it in a flow. For more information, refer to [Configuring a New Authentication](https://help.imiconnect.io/docs/apple-messages-for-business#configuring-a-new-authentication).

### Rich Link Previews for Domains (Optional)

If a Text messages contain links, they are auto-converted to Rich Links.

When converting hyperlinks in text messages to rich links, if a webpage doesn’t have a preview-quality image, the platform uses default preview image. You can control what preview image should be used by default for such web pages, by using this feature. You can add one default preview image per domain for up to 25 domains. You should use this feature only if the hyperlinks you want to send to customers do not have preview-quality images. You can figure out whether a particular webpage has a preview-quality image by sending yourself the hyperlink as an iMessage from any Apple device. If the webpage has a preview quality image, it’ll show up on the iMessages console.

To upload preview images:

1. Click **Add Preview For Domain**.



![Add Preview For Domain](https://files.readme.io/10c0cac-AMB_Rich_Links.jpg)




2. Enter a valid **Domain** name.



![Domain Name](https://files.readme.io/1a79aa2-AMB_Rich_Links1.jpg)




3. Click **Choose File** to upload the image for the domain.



![Choose File to upload the image](https://files.readme.io/f5a28e6-AMB_Rich_Links3.png)




> 📘 Note:
> 
> 1. You can add up to only 25 domains per asset. Once you reach the limit, the “Add Preview for Domain” button will be disabled.
> 2. You can upload only .jpeg, .jpg, and .png images.
> 3. Images must not exceed 5 MB and must be of at least 50 pixels in height and width.
> 4. Make sure to provide only domains, not URLs. i.e., avoid entering https or http. 
> 5. Domains with sub-category or sub-domains are allowed.
> 6. If you enter www. at the beginning of a domain, it is ignored and the rest of the domain is considered.

<br />

## API

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections) 

[Download](https://www.getpostman.com/) Postman from official site.

## Webhooks

You can configure Outbound Webhooks by choosing the Apple Messages for Business app from the entity dropdown to receive incoming messages and events from your customers.

Once you have registered and configured on the Apple Messages for Business and selected Webex Connect as your preferred service provider.

## FAQs

You can refer to the [Apple Messages for Business channel FAQs](https://developers.imiconnect.io/reference/apple-business-chat-faqs) for contextual information.