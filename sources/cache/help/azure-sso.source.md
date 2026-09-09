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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/025d920-1.jpg",
        null,
        ""
      ],
      "align": "center",
      "sizing": "0px",
      "border": true
    }
  ]
}
[/block]


3. On the left pane, click **Enterprise applications** under Manage.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b155f88-2.jpg",
        null,
        "Screenshot of selecting the Enterprise applications"
      ],
      "align": "center",
      "sizing": "200px",
      "border": true,
      "caption": "Screenshot of selecting the Enterprise applications"
    }
  ]
}
[/block]


4. Click **+ New application**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a16d912-3.jpg",
        null,
        "Image showing the interface to click the + New application button, highlighting its location for adding a new application."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot instructing to click + New application"
    }
  ]
}
[/block]


5. Click **+ Create your own application**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3969f48-4.jpg",
        null,
        "Image displaying the interface with guidance on how to create your own application"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot instructing to create your own application"
    }
  ]
}
[/block]


6. Do the following in the **Create your own application** section:
   1. Enter a valid name for your application.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cac2555-5.jpg",
        null,
        "Image showing the interface to enter the name for your app"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot instructing to enter the name for your app"
    }
  ]
}
[/block]


2. Select **Integrate any other application you don’t find in the gallery (Non-gallery)** under What are you looking to do with your application?
3. Click **Create**.  
   The Overview page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2f89e20-6.jpg",
        null,
        "Image showing the interface with instructions to select the Single Sign-on option"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the option to select Single Sign-on"
    }
  ]
}
[/block]


7. On the left pane, click **Single sign-on** and then click **SAML**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/87e7d3a-7.jpg",
        null,
        "Image showing the interface to select the SAML option"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot instructing to select the SAML option"
    }
  ]
}
[/block]


8. Click **Edit** in Basic SAML Configuration and enter/update the details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1f27477-8.jpg",
        null,
        "Image showing the interface with Basic SAML Configuration details"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Basic SAML Configuration details"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d09383d-8.jpg",
        null,
        ""
      ],
      "align": "center",
      "sizing": "0px"
    }
  ]
}
[/block]


> 📘 Note
> 
> Entity ID, Assertions Consumer Service URL are available on Webex Connect. It is available under Single Sign-On Settings.

## Setting up  SAML Configuration

1. Log in to your Webex tenant and click **Single Sign-On Settings**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/174e0e3-9.png",
        null,
        "Image showing the interface for Single Sign-On Settings in Webex Connect."
      ],
      "align": "center",
      "sizing": "200px",
      "border": true,
      "caption": "Screenshot displaying the Single Sign-On Settings in <<prodname>>"
    }
  ]
}
[/block]


2. In the Single Sign-On Settings page enter the Identifier (**Entity ID**).
   > 📘 Note
   > 
   > Please make sure the same Entity ID is configured in Azure and Webex Connect. We recommend using the Entity ID available in Connect.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/94714a2-5.jpg",
        null,
        "Screenshot of Single Sign-on Settings Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Single Sign-on Settings Page"
    }
  ]
}
[/block]


3. Copy the **Identifier** value from Webex Connect Service Provider Details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a3a1703-11.jpeg",
        null,
        "Screenshot of Configuring the Identifier Value."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Identifier value"
    }
  ]
}
[/block]


4. Click **Add Identifier** and paste the value.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4c10d1d-12.jpeg",
        null,
        "Screenshot of Identifier (Entity ID)."
      ],
      "align": "center",
      "caption": "Screenshot of Identifier (Entity ID)"
    }
  ]
}
[/block]


5. Enter the **Reply URL (Assertion Consumer Service URL)**. To get this value, login to your Webex Connect and navigate Single Sign-On Settings.
6. Copy the **Reply URL (Assertion Consumer Service URL)** value from Webex Connect Service Provider Details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1476910-13.jpeg",
        null,
        "Screenshot of ACS URL"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of ACS URL"
    }
  ]
}
[/block]


7. Click **Add reply URL** and paste the value.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4db001f-14.jpeg",
        null,
        "Screenshot of Adding Reply URL."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding Reply URL"
    }
  ]
}
[/block]


8. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3eb731c-15.jpeg",
        null,
        "Screenshot of saving the Basic SAML Configuration."
      ],
      "align": "center",
      "sizing": "250px",
      "border": true,
      "caption": "Screenshot of Saving the Basic SAML Configuration"
    }
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/37177cb-17.jpeg",
        null,
        "Screenshot of Managing claim page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing claim page"
    }
  ]
}
[/block]


- Select the required **Source**. 
- Select the required **Source attribute** from the drop-down.
- Click **Save**.

10. To download the SAML Certificates, click **Certificate (Base64 ) Download**.

## Configuring SSO on Webex Connect

1. Login to your Webex Connect and navigate to **Single Sign-On Settings**.
2. Enter the **Identity Provider Login URL** copied from the Azure portal.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8215034-18.jpg",
        null,
        "Screenshot of Configuring the SSO in Webex Connect"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring SSO in <<prodname>>"
    }
  ]
}
[/block]


3. Enter the **Entity ID**. Copy and Paste the **Entity ID** from Connect Single Sign-On page or Azure Single Sign-On page.
   > 📘 Note:
   > 
   > The Entity ID must be same in both the Webex Connect and Azure portals. We recommend using the Entity ID
4. Enter the **Remote Logout URL** copied from Azure Portal.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8641d84-19.jpg",
        null,
        "Screenshot of Configuring the Logout URL."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Logout URL."
    }
  ]
}
[/block]


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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b76fd32-20.jpg",
        null,
        "Screenshot of Testing the SSO Connection"
      ],
      "align": "center",
      "caption": "Screenshot of Testing the SSO Connection"
    }
  ]
}
[/block]


3. Click **Test**.