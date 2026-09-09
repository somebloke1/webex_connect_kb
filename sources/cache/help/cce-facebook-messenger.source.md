<<CCE>> users who want to use Facebook Messenger as a channel of customer support with Webex Contact Center can use the first procedure for connecting their Facebook pages with <<prodname>>, and then registering their Messenger app on Webex Engage.

## Configuring your Messenger App on <<prodname>>

> 📘 Messenger Usage
> 
> Messenger as a channel is supported in the Canada region as well.

You can register your Facebook Messenger page with <<prodname>> from 'Assets -> Apps' section. Here are the steps for registering:

1. Select **Messenger ** from **Configure New App** dropdown. 
2. Provide a name for your Messenger app asset and click **Add Messenger Page**. You must be the admin of the Facebook page to integrate Facebook Messenger with <<prodname>> . You will be redirected to your Facebook login page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ad279d1-FB1.jpg",
        "FB1.jpg",
        "Screenshot of Creating the New Messenger App Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Creating the New Messenger App Page"
    }
  ]
}
[/block]


3. Provide the login credentials. You may not see this step if you're already logged in.
4. Select the page that you want to register on the **What pages do you want to use with <<prodname>>** pop-up.
5. Provide the requested access permissions, and click **Done**.  
   At this stage, you will be redirected to <<prodname>>. If you have selected multiple pages in the previous step, you will be asked to choose the page that you want to use for the asset you are configuring. Select the required page. Once done, you'll see the following screen.

   [block:image]{"images":[{"image":["https://files.readme.io/883e862-Facebook_Messenger_-_Configure_New_App.jpeg","","Screenshot of Managing the Facebook Messenger App Page"],"align":"center","border":true,"caption":"Screenshot of Managing the Facebook Messenger App"}]}[/block]

   > 📘 Note
   > 
   > Only the Tenant with the user role 'Owner' will be allowed to make changes to Facebook Messenger page after it is configured, to avoid accidental / unintended changes by other platform users.
6. Click **Save**. This completes the association of your Facebook Messenger page with <<prodname>>. We do support advanced settings such as Welcome Screen, Persistent Menu, etc. but those are optional. Refer to the last section for information on the advanced settings.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ccc3787-Facebook_login_flow.png",
        "Facebook login flow.png",
        "Screenshot of Facebook Messenger and platform association"
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Screenshot of Facebook Messenger and platform association"
    }
  ]
}
[/block]


## Configuring Welcome Screen, Persistent Menu, etc.

### Welcome Screen

You can optionally choose to configure the welcome screen for your Facebook Messenger customers. Switch the Welcome Screen toggle to Enabled, and provide a greeting message for the Welcome Screen (minimum three characters long).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f04763c-14302685_243106819419381_1314180151_n.png",
        "14302685_243106819419381_1314180151_n.png",
        "Screenshot of Welcome Screen"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Welcome Screen"
    }
  ]
}
[/block]


> 📘 
> 
> We recommend you to not enable the **Get Started** button on the Facebook Messenger app configuration screen under Assets --> Apps section when using <<prodname>> for supporting Facebook Messenger for Webex Contact Center.

### Persistent Menu

The Persistent Menu allows you to have an always-on user interface element inside conversations. This is an easy way to help people discover and access the core functionality at any point in the conversation. You have to enable the 'Get Started' button in the welcome screen to configure Persistent Menu.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0c817c8-Messenger_Persistent_Menu.jpg",
        "Messenger Persistent Menu.jpg",
        "Screenshot of Persistent Menu"
      ],
      "align": "center",
      "sizing": "300rt",
      "border": true,
      "caption": "Persistent Menu"
    }
  ]
}
[/block]


You can refer to the [Messenger documentation on Persistent Menus](https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu/) topic to know more about this feature such as best practices, limitations, etc.

## Allowed List Domains

Add the web domains that need to be accessible from Facebook Messenger.

### Subscription Messaging

Enable this feature to allow Facebook page to send non-promotional content through Messenger channel. This feature is available only for clients who have Facebook's permission to use it.

### Page Discovery Plugins

The Page Discovery plugins allow you to integrate Facebook Messenger chat experience directly onto a website/webpage for a personalized experience. This allows your customers to interact with your business anytime with a click of a button.

To use the below plugins, you should include the code snippet provided on your webpage along with Facebook's JavaScript SDK. The website domain must also be in the allowed list on which you wish to use this plugin.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ad6844e-21477992_1945714059029979_5620422387120996352_n.png",
        "21477992_1945714059029979_5620422387120996352_n.png",
        "Screenshot of Send to Messenger"
      ],
      "align": "center",
      "border": true,
      "caption": "Send to Messenger"
    }
  ]
}
[/block]


| Name       | Description                                                                                                            |
| :--------- | :--------------------------------------------------------------------------------------------------------------------- |
| Message Us | Renders a button when clicked on, redirects the users to Facebook Messenger and opens a conversation within your page. |

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5b81fd6-13679808_631224743722018_2016203957_n.png",
        "13679808_631224743722018_2016203957_n.png",
        "Screenshot of checkbox plugin -Send to Messenger"
      ],
      "align": "center",
      "border": true,
      "caption": "Checkbox Plugin"
    }
  ]
}
[/block]


> 🚧 Opt-In plugins
> 
> Support for Opt-ins received through Send to Messenger and Check box plugins is not available at the moment. We are currently working to restore these features and will continue to update this document and the release notes section with the details as they are available.

For more information on detailed information about Messenger app configuration, refer to the [Messenger ](https://help.imiconnect.io/docs/facebook-messenger) chapter in the Assets section.

## Registering your Facebook Messenger App with Webex Engage

Once the asset has been saved, you will see a 'Register to Webex Engage' action button on top (ref: below screen).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/af823a7-Register_Messenger_with_Webex_Engage.png",
        "FB3.jpg",
        "Screenshot of Managing the Messenger App Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing the Messenger App Page - Register to Webex Engage"
    }
  ]
}
[/block]


1. Click **Register to Webex Engage**. A pop-up appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/503db5c-Register_Messenger_with_Webex_Engage_Snippet.jpeg",
        "FB4.jpg",
        "Screenshot of Register to Webex Engage"
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Screenshot of Register to Webex Engage"
    }
  ]
}
[/block]


2. Select the required service (this should be the <<prodname>> service that would be used for configuring Facebook Messenger flows for Webex Contact Center).
3. Click **Register**. 

> 🚧 
> 
> - Please note, the service mapping cannot be changed once done. Hence, the asset registration on Webex Contact Center should be done after the service to be used has been decided. 
> - Do not delete the Facebook Messenger asset once it's been registered with Webex CC. Once deleted, it cannot be restored. Doing so would lead to asset deletion within <<prodname>> alone, while the entry continues to be in Webex CC and Webex Engage.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3f8611e-Register_Messenger_with_Webex_Engage.png",
        "FB5.jpg",
        "Screenshot of Asset Registration Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Asset Registration Page"
    }
  ]
}
[/block]


A message displays 'Asset registered successfully'. This completes the asset registration for Webex Contact Center.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/387180d-PCI-enabled.jpeg",
        "FB6.jpg",
        "Asset Registration"
      ],
      "align": "center",
      "border": true,
      "caption": "Asset registration completion"
    }
  ]
}
[/block]


As shown above, you will see a <<WebexCC>> icon and a PCI check enabled flag next to the Facebook Messenger asset once it's been successfully mapped with Webex Contact Center.

Once the asset is registered, this asset will be available for entry point mapping in Cisco Webex Contact Center portal.

## Edit/Manage/Delete the Facebook Messenger App Asset

1. Go to **Assets** > **Apps**.
2. Search for the Messenger app asset that you want to edit and click **Manage** in the drop-down list box at the right to manage the settings of this app.  
   You see the **Manage – Messenger** page, where you can manage the settings of the app.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/913190353ebfe01ac7ce64fc05e9c86c6e275cecc1ef087ae49379caab323da3-Facebook_Messenger_-_Manage_app.png",
        "",
        "Manage Facebook Messenger app asset"
      ],
      "align": "center",
      "border": true,
      "caption": "Manage Facebook Messenger app asset"
    }
  ]
}
[/block]


### Delete Facebook Messenger App Asset

1. Go to Assets > Apps.
2. Search for the Facebook Messenger app asset that you want to edit and click **Delete** in the drop-down list box at the right to delete the app.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/378f7d9deeea8ca8519b98ab88a342d90eca5d7623076dd605b45b8bdac64005-Facebook_Messenger_app_asset.png",
        "",
        "Deleting Facebook Messenger app asset"
      ],
      "align": "center",
      "border": true,
      "caption": "Deleting Facebook Messenger app asset"
    }
  ]
}
[/block]


## Facebook Messenger Authorization Expiry

The following is a list of scenarios in which the authorization of your Messenger app will expire:

1. When you change your Facebook/Messenger login password.
2. If the user who requested the token no longer has a role on the page
3. If you deselect any of the integrated pages when adding a new page in the <<prodname>> platform. Make sure to include all the integrated pages.

> 📘 Authorization Expiry
> 
> While adding a new page, please make sure to select all the pages that have been integrated with <<prodname>> platform previously in the Facebook login flow.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ccc3787-Facebook_login_flow.png",
        "Facebook login flow.png",
        "Screenshot of delinking the Facebook Messenger page from Webex Connect platform"
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Screenshot of delinking the Facebook Messenger page from Webex Connect platform"
    }
  ]
}
[/block]


4. You can delink the messenger page from the Webex Connect platform from messenger page settings.