# Azure SSO

Source: https://help.webexconnect.io/docs/azure-sso
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:36+00:00

## Configure an Azure AD Identity Provider

Configure Microsoft Azure Active Directory (AD) as an identity provider to let users log in to your Connect tenant using their Azure AD credentials.

Follow the below steps to configure Azure AD as an identity provider.

1. Set up an Azure AD application.
2. Setup your an Azure AD SSO on Webex Connect.
3. Test the connection.

## Configure SSO on Azure

To Configure SSO on Azure, follow the procedure below:

1. Log in to your Azure portal I.e., [Microsoft Azure](http://portal.azure.com/) 
2. Click **Azure Active Directory** under Azure services.



![Source screenshot](https://files.readme.io/025d920-1.jpg)




3. On the left pane, click **Enterprise applications** under Manage.



![Screenshot of selecting the Enterprise applications](https://files.readme.io/b155f88-2.jpg)




4. Click **+ New application**.



![Screenshot instructing to click + New application](https://files.readme.io/a16d912-3.jpg)




5. Click **+ Create your own application**.



![Screenshot instructing to create your own application](https://files.readme.io/3969f48-4.jpg)




6. Do the following in the **Create your own application** section:
   1. Enter a valid name for your application.



![Screenshot instructing to enter the name for your app](https://files.readme.io/cac2555-5.jpg)




2. Select **Integrate any other application you don’t find in the gallery (Non-gallery)** under What are you looking to do with your application?
3. Click **Create**.  
   The Overview page is displayed.



![Screenshot displaying the option to select Single Sign-on](https://files.readme.io/2f89e20-6.jpg)




7. On the left pane, click **Single sign-on** and then click **SAML**.



![Screenshot instructing to select the SAML option](https://files.readme.io/87e7d3a-7.jpg)




8. Click **Edit** in Basic SAML Configuration and enter/update the details.



![Screenshot displaying the Basic SAML Configuration details](https://files.readme.io/1f27477-8.jpg)






![Source screenshot](https://files.readme.io/d09383d-8.jpg)




> 📘 Note
> 
> Entity ID, Assertions Consumer Service URL are available on Webex Connect. It is available under Single Sign-On Settings.

## Setting up  SAML Configuration

1. Log in to your Webex tenant and click **Single Sign-On Settings**.



![Screenshot displaying the Single Sign-On Settings in Webex Connect](https://files.readme.io/174e0e3-9.png)




2. In the Single Sign-On Settings page enter the Identifier (**Entity ID**).
   > 📘 Note
   > 
   > Please make sure the same Entity ID is configured in Azure and Webex Connect. We recommend using the Entity ID available in Connect.



![Screenshot of Single Sign-on Settings Page](https://files.readme.io/94714a2-5.jpg)




3. Copy the **Identifier** value from Webex Connect Service Provider Details.



![Screenshot of Configuring the Identifier value](https://files.readme.io/a3a1703-11.jpeg)




4. Click **Add Identifier** and paste the value.



![Screenshot of Identifier (Entity ID)](https://files.readme.io/4c10d1d-12.jpeg)




5. Enter the **Reply URL (Assertion Consumer Service URL)**. To get this value, login to your Webex Connect and navigate Single Sign-On Settings.
6. Copy the **Reply URL (Assertion Consumer Service URL)** value from Webex Connect Service Provider Details.



![Screenshot of ACS URL](https://files.readme.io/1476910-13.jpeg)




7. Click **Add reply URL** and paste the value.



![Screenshot of Adding Reply URL](https://files.readme.io/4db001f-14.jpeg)




8. Click **Save**.



![Screenshot of Saving the Basic SAML Configuration](https://files.readme.io/3eb731c-15.jpeg)




9. Click **Edit** in Attributes & Claims and enter/update the details.

   | Attributes             | Values               | Description                      |
   | :--------------------- | :------------------- | :------------------------------- |
   | mobileno               | user.telephonenumber | The telephone number of the user |
   | loginid                | user.mail            | The email ID of the user         |
   | firstname              | user.displayname     | The first name of the user       |
   | Unique User Identifier | user.mail            | The email ID of the user         |

   > 📘 Attributes in assertion data
   > 
   > The attributes are case-sensitive and should be entered in the displayed cases above.

   - Steps to add an Attribute Enter **Name**, **Namespace** in Manage Claim.



![Screenshot of Managing claim page](https://files.readme.io/37177cb-17.jpeg)




- Select the required **Source**. 
- Select the required **Source attribute** from the drop-down.
- Click **Save**.

10. To download the SAML Certificates, click **Certificate (Base64 ) Download**.

## Configuring SSO on Webex Connect

1. Login to your Webex Connect and navigate to **Single Sign-On Settings**.
2. Enter the **Identity Provider Login URL** copied from the Azure portal.



![Screenshot of Configuring SSO in Webex Connect](https://files.readme.io/8215034-18.jpg)




3. Enter the **Entity ID**. Copy and Paste the **Entity ID** from Connect Single Sign-On page or Azure Single Sign-On page.
   > 📘 Note:
   > 
   > The Entity ID must be same in both the Webex Connect and Azure portals. We recommend using the Entity ID
4. Enter the **Remote Logout URL** copied from Azure Portal.



![Screenshot of Configuring the Logout URL.](https://files.readme.io/8641d84-19.jpg)




5. Upload the **Base 64 Certificate** (which is downloaded from the Azure) in the Identity Provider Certificate.
6. Select the Request Signature Method as **RSA-SHA256** from the drop-down.
7. Click **Save**.
8. Click **Confirm** on the pop-up.

## Testing the SSO Connection

1. On Single Sign-On Settings page click **Test**.
2. Enter the **Email Id**. 

> 📘 NOTE
> 
> Please make sure the email address used for testing is registered on Azure with SSO app, created during the configuration on SSO.



![Screenshot of Testing the SSO Connection](https://files.readme.io/b76fd32-20.jpg)




3. Click **Test**.