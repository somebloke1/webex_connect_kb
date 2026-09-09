Webex Engage users who want to use Email as a channel of customer support with Webex Contact Center can configure an email asset. We support the following email service providers:

- Gmail
- Microsoft 365  
  For the above service providers, we have two authentication methods:
- Username and Password
- OAuth 2.0  
  You can map your support email addresses with <<prodname>> by following the steps below:

> 📘 Note
> 
> The following Email App Configuration instructions are applicable only for Webex Contact Center and <<prodname>> integration. If you have a standalone <<prodname>> tenant please refer to [Email App](https://help.imiconnect.io/docs/email) configuration for instructions.

## Configuring Email channel asset on Webex Connect

Follow the below steps to map your support email addresses with <<prodname>>:

1. Log in to <<prodname>> platform.
2. Go to Assets → Apps.
3. Click Configure New App and then select Email.  
   Configure New Application - Email page displays.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4535305-CCE1.jpeg",
        "Configure_Email_Asset1.jpg",
        "Screenshot of Creating the New Email App Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Creating the New Email App Page"
    }
  ]
}
[/block]


4. Enter a user-friendly name for the Asset.
5. Enter a valid Email address (such as support@<<CLIENT-DOMAIN>>). 
6. Copy the forwarding email address and configure an email forwarding rule in your email client to forward emails sent to your support email id (i.e., same as the email id mentioned in step 6) to this email address.

> 📘 Receiving Inbound Emails
> 
> - Please note that you’d need to mandatorily configure an auto-forwarding rule to forward the emails received on the email address configured in ‘EMAIL ID' field to the email address available in the ‘FORWARDING ADDRESS’ field. <<prodname>> won’t receive the inbound emails unless this step is completed. Please note that Email via SMTP has a 25MB size limitation on the inbound email attachments. Due to this limitation, if an inbound Email fails, customer gets a delivery failure email and is expected to resend the email with smaller attachment.
> - In the case of Gmail, you must verify the email forwarding address by either confirming through the URL provided or entering the OTP sent to the provided address as applicable. You can retrieve the URL or OTP as applicable either looking up the Outbound Webhook payload (requires configuring Outbound Webhook for inbound email) or decrypting the Debug Logs for the Email asset. It is found in the full email body of the logs. Earlier, the OTP was found in the subject of the email in the downloaded Export Logs.

> 📘 Note
> 
> Please note that for email sent via SMTP channel, <<prodname>> does not support delivery tracking and also does not receive delivery failure notification emails even if the auto-forwarding rule is set up No Delivery Failure Notifications

<InboundEmailWithInlineImages />

<br />

7. Enter the domain name for the SMTP Server.

8. Follow one of the two authentication protocol below based on your use case:

- Username Password 
- OAuth 2.0 (Recommended)

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a773e44-CCE2.jpeg",
        "Gmail OAuth 2.0 for Outbound Emails.jpeg",
        "Screenshot displaying to select the Authentication Type"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying to select the Authentication Type"
    }
  ]
}
[/block]


> 📘 
> 
> Based on your selection in step 8 in the procedure above, follow one of the two procedures below for authentication.

## Authentication using Username and Password

1. Enter a valid Username and Password to be used to authenticate the SMTP server connection.
2. Enter the Port number to which you want to configure your email asset.
3. Select the Security type as SSL or STARTTLS if required, otherwise leave it as None.
4. Click Test Connection. 

If the connection is successful, you will receive a confirmation message.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ca81ef4-email-image2.png",
        "email-image2.png",
        "Screenshot of Toast Message Displaying SMTP Connection Established Successfully."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Toast Message Displaying SMTP Connection Established Successfully."
    }
  ]
}
[/block]


## Authentication using OAuth 2.0

Follow the below steps to configure OAuth 2.0:

1. Enter the SMTP Server, Username, Port , Client ID, Client Secret, Authorization URL, Scope, Access Token URL, Validity and Refresh Token URL.
2. Select Use different email address than the asset email ID for generating tokens if you want to configure a shared mailbox as email app asset and enter the user ID to generate the access token in the **Login ID For Generating Token** field.
   > 📘 Note
   > 
   > Use the Copy icon to copy and enter the same user ID in the Login pop-up, when you click **Generate Token**.
3. Click **Generate Token**.
4. Click **Save **to complete email channel asset creation.

> 📘 Note
> 
> To get details such as Client ID, Client Secret, Authorization URL, Scope, Access Token URL, Validity and Refresh Token URL, based on your email provider, follow one of the following procedures.

<SharedMailbox />

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/083dd98f9a3b73f447a8fc97e62ee59863a6014cf42ebfdd9f488812280ce535-eu.webexconnect.io_apps_email-smtp_4.png",
        null,
        "Screenshot of Configuring New Email App."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring New Email App."
    }
  ]
}
[/block]


If your administrator restricts the users from providing consent for applications by choosing the option “Do not allow user consent“ or a similar option in the user consent settings of the email service provider, please make sure that you clear the option “I would like to explicitly review before providing consent for authentication“, when you are trying to create an email asset. Selecting the option may result in authentication failure as you might not have permission to provide consent for application, but the authentication request expects you to provide consent.

> ❗️ Missing Incoming Attachments
> 
> Incoming emails with .msg and .eml attachments sent from Microsoft Outlook might be received without the attachments due to a limitation from Microsoft Outlook.

> 📘 User Consent Settings
> 
> In case of Microsoft 365, if the user consent settings on Azure Active Directory are recently changed, please make sure that the new settings have taken effect, before adding an email asset on Webex Connect platform.

> 📘 Access Token
> 
> The Access Token, Refresh Token, and Validity are auto populated after a token is generated.
> 
> In some cases, Refresh Token needs to be generated manually. Email is sent by connect to the tenant owners email ID. Clients will receive an automated email. They must navigate to the Email asset page and must re-generate the token.
> 
> In some cases, Gmail might not provide a Refresh Token. In such scenarios, the asset owner will have to re-generate tokens after selecting the checkbox "I would like to explicitly review before providing consent for authentication".
> 
> Token has a fixed expiry time and the backend application automatically calls the API to regenerate token before that.

## Registering  on Google Cloud

1. Login to your <https://console.cloud.google.com/>
2. Create a new project or select an existing project.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fd844b8-2.jpg",
        "Picture 1.png",
        "Screenshot of Create a new project or select an existing project."
      ],
      "align": "center",
      "border": true,
      "caption": "Create a new project or select an existing project."
    }
  ]
}
[/block]


3. Hover over the left-hand side menu and click APIs & Services.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3dc8798-3.jpg",
        "Picture 2.png",
        "Screenshot of API and Services."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of API and Services."
    }
  ]
}
[/block]


The APIs & Services page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/90ab0ca-4.jpg",
        "Picture 3.png",
        "Screenshot of API and Services Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of API and Services Page."
    }
  ]
}
[/block]


4. Click OAuth consent screen. The page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/18dc882-5.jpg",
        "Picture 4.png",
        "Screenshot of OAuth consent screen."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of OAuth consent screen."
    }
  ]
}
[/block]


5. Select External and click Create.  
   The Edit app registration page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b666b3-6.jpg",
        "Picture 5.png",
        "Screenshot of Edit App Registration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Edit App Registration Page."
    }
  ]
}
[/block]


6. Enter the  App name, User support email  in App Information and email address under Developers Contact information.
7. Click **Save and Continue**. The Scopes page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1c1c8c8-7.jpg",
        "Picture 6.png",
        "Screenshot of Add or Remove Scopes."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Add or Remove Scopes."
    }
  ]
}
[/block]


> 📘 Note
> 
> Click **Learn more** option shown in the above image to get the appropriate value of the Scope based on your use-case. Alternatively, you can find the required information [here](https://developers.google.com/identity/protocols/oauth2/scopes#gmail)

8. Click **Save and Continue**. The Test users page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/32e7fb2-8.jpg",
        "Picture 7.png",
        "Screenshot of Test users page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Test users page."
    }
  ]
}
[/block]


9. To add test users, click **+ Add Users**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/022a618-9.jpg",
        "Picture 8.png",
        "Screenshot of Add users page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Add users page."
    }
  ]
}
[/block]


> 📘 Note
> 
> A project can have only 100 test users at max.

10. Enter the test user email address and click **Add**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/822a2d3-10.jpg",
        "Picture 9.png",
        "Screenshot of Add users page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Add users page."
    }
  ]
}
[/block]


11. Click **Save and Continue**.  
     The Summary page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f4febb0-11.jpg",
        "Picture 10.png",
        "Screenshot of Edit App Registration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Edit App Registration page."
    }
  ]
}
[/block]


## Adding Test Users

To add test users to an existing project.

1. Navigate to OAuth Consent Screen

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3cd0c50-12.jpg",
        "Picture 11.png",
        "Screenshot of OAuth Consent Screen page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of OAuth Consent Screen page."
    }
  ]
}
[/block]


2. Click **+Add Users** to add test users.

> 📘 Note
> 
> A project can have only 100 test users. It is mandatory to add the test users email address in your tenant asset creation page.

3. Add the callback URL in the ‘Credentials’ section (can be found on connect platform’s OAuth email asset creation page)

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d50efdd-CCE9.png",
        "Picture 13.png",
        "Screenshot of Adding the callback URL."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding the callback URL."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f7e1919-2.jpg",
        "Picture 14.png",
        "Screenshot of Adding the callback URL."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding the callback URL."
    }
  ]
}
[/block]


4. The **Client ID** and **Client Secret** values are available in the Credentials page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9ebadfe-Wxcc22.png",
        "Picture 15.png",
        "Screenshot Displaying the Client ID and Client Secrets."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Displaying the Client ID and Client Secrets."
    }
  ]
}
[/block]


5. Select **Use different email address than the asset email ID for generating tokens** if you want to configure a shared mailbox as email app asset and enter the user ID to generate the access token in the **Login ID For Generating Token** field.
   > 📘 Note
   > 
   > Use the Copy icon to copy and enter the same user ID in the Login pop-up, when you click **Generate Token**.
6. Click **Generate Token**. Access Token and Refresh Token are generated.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9278be0-Email3.jpg",
        "Picture 16.png",
        "Screenshot of Manage Email Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage Email Page."
    }
  ]
}
[/block]


6. Click **Save**.

> 📘 Note
> 
> Please note that, the app is still in Testing state on Gcloud. To publish the app, click "PUBLISH APP" under Publishing Status on the OAuth consent screen Dashboard as shown below.
> 
> Unless published, the authorizations by test users will expire 7 days from the time of consent.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/25efa9dcb1ce5062b3f4b9e16680d35943febb4072f83fb05cff7136795e6d93-0948c81-image001.png",
        "",
        "Screenshot for Highlighting Publish App"
      ],
      "align": "center",
      "border": true,
      "caption": "Highlighting Publish App"
    }
  ]
}
[/block]


## Configure a rule in Gmail to forward incoming emails to Webex Connect

1. Configure an Outbound Webhook in <<prodname>> under 'Assets->Integrations' to track incoming emails. This would require you to select the email channel asset configured newly in the Entity dropdown. Refer this link for more details.
2. Navigate to the email channel app asset configuration screen again and copy the value of the Forwarding Address.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a867bee-Wxcc4.jpeg",
        "MO OAuth.jpg",
        "Screenshot Highlighting the Forwarding Address."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Highlighting the Forwarding Address."
    }
  ]
}
[/block]


3. Now, navigate to the Settings page in your Gmail account and click Forwarding and POP/IMAP tab and paste the Forwarding Address in that field and then click Add. Gmail will send an verification URL or OTP to this forwarding address at this stage.
4. You can retrieve the verification URL or OTP by either looking up the Outbound Webhook payload (requires configuring Outbound Webhook for inbound email) or decrypting the Debug Logs for the Email asset. It is found in the full email body. Earlier, the OTP was found in the subject of the email in the downloaded Export Logs.
5. Select Forward a copy of Incoming mail to radio button in Gmail and click **Save** changes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/547f4d7-WxCC2.jpeg",
        "Gmail OAuth.png",
        "Screenshot of Select Forward a copy of Incoming mail."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Select Forward a copy of Incoming mail."
    }
  ]
}
[/block]


## Registering on Microsoft 365

1. Create app in Azure portal.  
   Please check on how to [create app on Microsoft 365](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).  
   a. Enter the **App Name**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f4d0661-Wxcc3.png",
        "App Name OAuth SMTP.png",
        "Screenshot of Brand and Properties Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Brand and Properties Page."
    }
  ]
}
[/block]


b. Click Authentication on the left panel, to add the Redirect URLs. This value should be taken from your app asset

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c8d961b-Wxcc5.png",
        "Redirect URLs OAuth SMTP.png",
        "Screenshot of Authentication Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Authentication Page."
    }
  ]
}
[/block]


c. Select the required Tokens and types for authentication from Authentication page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2840497601ccb024a4c81188e0b88429a3858b211517c57d3ee43eb444f7b88e-Email.png",
        "Tokens and types for authentication OAuth SMTP.png",
        "Authentication"
      ],
      "align": "center",
      "border": true,
      "caption": "Authentication"
    }
  ]
}
[/block]


d. Click **Certificates & secrets **on the left panel and click Client secrets tab to generate and copy the value under the **Value** field.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/934330647f88f3ca143936f5c1a1ac728b173a6717c6fc41eb25fe06ac3cb293-Value_Image.png",
        "Generate and copy client secret OAuth SMTP.png",
        "Screenshot of Certificates & secrets Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Certificates & secrets Page."
    }
  ]
}
[/block]


e. Click API Permissions on the left panel to add and grant permissions to send mail through SMTP. After clicking 'Add a permission', you will need to click on 'APIs my organization uses', search for 'Office 365 Exchange Online', choose 'Application permissions' (not 'Delegated permissions'), and add 'Mail.Send' permission.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/243323e-Wxcc8.png",
        "Permissions and grant to send mail through smtp.png",
        "Screenshot of API Permissions"
      ],
      "align": "center",
      "border": true,
      "caption": "API Permissions"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/727727d021d2d36760cb2797ae76c64cfe8acea3a76133f98d14732a78eea006-API_Permissions_1.png",
        "",
        "Screenshot of Request API Permissions - Office 365"
      ],
      "align": "center",
      "border": true,
      "caption": "Request API Permissions - Office 365"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fe36fbfc439bb0d6899b03243b94f253399ecd9e818aff67a192a28e4f5e142d-API_Permissions_2.png",
        "",
        "Screenshot of Granting Application Permissions"
      ],
      "align": "center",
      "border": true,
      "caption": "Granting Application Permissions"
    }
  ]
}
[/block]


2. Enabling SMTP authentication for User - Login as admin and enable SMTP for a user for which the above app has been created.

Use the Microsoft 365 admin center to enable or disable SMTP AUTH for specific mailboxes

a. Open the Microsoft 365 admin center and go to **Users** > **Active users**.  
b. Select the user, and a flyout appears, click **Mail**.  
c. In the Email apps section, click **Manage** email apps.  
d. Verify the Authenticated SMTP setting: unchecked = disabled, checked = enabled.  
e. When you're finished, click **Save changes**.

3. Once app is created ,you can find Tenant ID, Client ID and other details. Capture tenant id

   In the below screenshot Tenant id is “7f5XXX-e6XX-4aXX-bdXX-9fXXXXXXXX”.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5c9f5df-Wxcc9.png",
        "Tenant ID SMTP.png",
        "Screenshot of Overview Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Overview Page."
    }
  ]
}
[/block]


4. Create Email asset in <<prodname>> with above details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b838dacd1711b0ffe191af046c2cf02faa7fc5c2493f3e96e9717ce14d19d9de-staging.webexconnect.io_apps_email-smtp_17262.png",
        null,
        "Screenshot of Manage Email App Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage Email App Page."
    }
  ]
}
[/block]


 a. Replace respective Tenant ID in authorization, Access Token and Refresh Token urls. For example if tenant id is “tenant_abcd_123” then below are the urls to be configured

- Authorization URL: <https://login.microsoftonline.com/tenant_abcd_123/oauth2/v2.0/authorize>
- Scope: offline_access <https://outlook.office.com/SMTP.Send>
- Access Token URL: <https://login.microsoftonline.com/tenant_abcd_123/oauth2/v2.0/token>
- Refresh Token URL: <https://login.microsoftonline.com/tenant_abcd_123/oauth2/v2.0/token>

5. Select **Use different email address than the asset email ID for generating tokens** if you want to configure a shared mailbox as email app asset and enter the user ID to generate the access token in the **Login ID For Generating Token** field.
   > 📘 Note
   > 
   > Use the Copy icon to copy and enter the same user ID in the Login pop-up, when you click Generate Token.
6. Click **Generate Token** to authorize and save the asset.

## To enable SMTP authentication for an Active User

1. Login to the Admin.microsoft.com
2. Click the three horizontal lines on the left-hand side menu and click **Users**.
3. Under Users, click **Active Users**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ca18b75-Active_Users.jpg",
        "Active Users.jpg",
        "Screenshot Highlighting Active Users."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Highlighting Active Users."
    }
  ]
}
[/block]


 Active Users page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cde508d-Active_Users_Page.jpg",
        "Active Users Page.jpg",
        "Screenshot of Active Users Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Active Users Page."
    }
  ]
}
[/block]


4. Select the required user from the list and click **Manage product licenses** under settings.  
   A pop-up appears to the right-hand side menu of the window.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f2f4a45-Manage_Product_Licenses.jpg",
        "Manage Product Licenses.jpg",
        "Screenshot of Manage product licenses."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage product licenses."
    }
  ]
}
[/block]


5. Click **Mail** tab and click **Manage email apps** under Email apps.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/89bba4b-Mail.jpg",
        "Mail.jpg",
        "Screenshot of Mail Tab."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Mail Tab."
    }
  ]
}
[/block]


A pop-up appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6f9cd42-Manage_Email_Apps.jpg",
        "Manage Email Apps.jpg",
        "Screenshot of Manage email apps popup."
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Manage email apps popup."
    }
  ]
}
[/block]


6. Select all the fields and click **Save changes**.

## Configure Anti-spam policies

1. Click the three horizontal lines on the left-hand side menu and under Show all --> click **Settings**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8c92045-Policy1.jpg",
        "Policy1.jpg",
        "Screenshot highlighting Show all in Menu."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot highlighting Show all in Menu."
    }
  ]
}
[/block]


 Welcome to Microsoft 365 Defender page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bff5e69-Policies_and_Rules.jpg",
        "Policies and Rules.jpg",
        "Screenshot highlighting Policies & rules in Menu."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot highlighting Policies & rules in Menu."
    }
  ]
}
[/block]


2. Click **Policies & rules** on the left-hand side menu
3. Click **Threat policies** and click **Anti-spam** under Threat Policies.  
   Anti-spam policies page appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8d3efd0-Anti-spam.jpg",
        "Anti-spam.jpg",
        "Screenshot highlighting Threat policies Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot highlighting Threat policies Page."
    }
  ]
}
[/block]


4. Click + Create policy and select Outbound from the drop-down.  
   Name your policy page appears.
5. Enter the Name, Description and click Next.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c07cb72-Name_your_Policy.jpg",
        "Name your Policy.jpg",
        "Screenshot of Name Your Policy Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Name Your Policy Page."
    }
  ]
}
[/block]


6. Enter the username in Users field and select the required user from the suggested contacts in User, groups, and domains page. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4859986-User_and_Groups.jpg",
        "User and Groups.jpg",
        "Screenshot of User, groups, and domains page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of User, groups, and domains page."
    }
  ]
}
[/block]


7. Click **Next**.
8. Enter values in the **Set an external message limit**, **Set an internal message**, and **Set a daily messages**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eb37e1b-Protection_Settings.jpg",
        "Protection Settings.jpg",
        "Screenshot of Protection settings page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Protection settings page."
    }
  ]
}
[/block]


9. Select **Restrict the user from sending the mail until the following day** from Restriction placed on users who reach the message limit drop-down.
10. Select **On - Forwarding is enabled** from Automatic forwarding rules. 
11. Select **Notify these users and groups if a sender is blocked due to sending outbound spam** from Notifications and enter the email address of the user.
12. Click **Next** and click **Create**.  
    A New anti-spam policy created page is displayed with a message “Your anti-spam policy OutboundEmail has been created. It will go into effect immediately”.

## Registering your Webex Connect Email App Asset with Webex Engage

Once you’ve successfully configured your Email asset with <<prodname>> and saved it, you can register it with Webex Engage by following the below steps:

1. Go to Assets →Apps.
2. Select Email in the App Type drop-down list box.
3. Click the required Email.
4. Click Register To Webex Engage.  
   The Register To Webex Engage pop-up displays.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a1064cb-5.jpg",
        "Register_Webex_Engage.PNG",
        "Screenshot of Register To Webex Engage Page."
      ],
      "align": "center",
      "sizing": "450px",
      "border": true,
      "caption": "Screenshot of Register To Webex Engage Page."
    }
  ]
}
[/block]


5. Select the required service (Note: this should be the <<prodname>> service that would be used for configuring Email flows for Webex Contact Center integration and click Register. 

> 🚧 
> 
> - You cannot change the service mapping once done. Hence, the asset registration on Webex Contact Center should be done after the service to be used has been decided.
> 
>   - Do not delete an Email asset once it's been registered with Webex Contact Center. Once deleted it cannot be restored. Doing so would lead to asset deletion within Webex Connect alone while the entry continues to be in Webex Contact Center and Webex Engage.

A message displays “Asset registered successfully”. This completes the asset registration for Webex Contact Center integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3df427e-CCE_App_Asset_Configure.PNG",
        "CCE_App_Asset_Configure.PNG",
        "Screenshot of Email App Displaying Webex Engage icon and PCI check enabled flag."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Email App Displaying Webex Engage icon and PCI check enabled flag."
    }
  ]
}
[/block]


As shown above, you will see a Webex Engage icon and a PCI check enabled flag next to the email asset once it's been successfully mapped with Webex Contact Center.