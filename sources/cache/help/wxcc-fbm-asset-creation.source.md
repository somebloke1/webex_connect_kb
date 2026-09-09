<<WebexCC>> users who want to use Facebook Messenger as a channel of customer support with Webex Contact Center can easily connect their Facebook pages with <<prodname>> by following the below steps:

## Configuring your Messenger App on Webex Connect

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
        "Screenshot of Configuring the Messenger App Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Messenger App Page."
    }
  ]
}
[/block]


3. Provide the login credentials. You may not see this step if you're already logged in.
4. Select the page that you want to register on the **What pages do you want to use with <<prodname>>** pop-up.
5. Provide the requested access permissions, and click **Done**.  
   At this stage, you will be redirected to <<prodname>> . If you selected multiple pages in the previous step, you will be asked to choose the page that you want to use for the asset you are configuring. Select the required page. Once done, you'll see the following screen.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/01b2a03-6.jpeg",
        null,
        "Screenshot of Managing the Messenger App Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing the Messenger App Page."
    }
  ]
}
[/block]


6. Click 'Save'. This completes the association of your Facebook Messenger page with <<prodname>>. We do support advanced settings such as Welcome Screen, Persistent Menu, etc. but those are optional. Refer to the last section for info on the advanced settings.

## Registering your Facebook Messenger App Asset with Webex Engage

Once the asset has been saved, you will see a 'Register to Webex Engage' action button on top (ref: below screen).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e08a455-image.png",
        null,
        "Screenshot of Managing the Messenger App Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing the Messenger App Page."
    }
  ]
}
[/block]


1. Click **Register to Webex Engage**option. Once clicked, you will see the following pop-up.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b50bc23-8.jpg",
        "FB4.jpg",
        "Screenshot of Register to Webex Engage."
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Screenshot of Register to Webex Engage."
    }
  ]
}
[/block]


2. Select the required service (this should be the <<prodname>> service that would be used for configuring Facebook Messenger flows for Webex Contact Center).
3. Click **Register**. 

> 🚧 Note
> 
> - Please note, the service mapping cannot be changed once done. Hence, the asset registration on Webex Contact Center should be done after the service to be used has been decided. 
> - Do not delete the Facebook Messenger asset once it's been registered with Webex Contact Center. Once deleted it cannot be restored. Doing so would lead to asset deletion within <<prodname>> alone while the entry continues to be in Webex Contact Center and Webex Engage.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8b98695-image.png",
        null,
        "Screenshot of registering the asset successfully with Webex Engage."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of registering the asset successfully with Webex Engage."
    }
  ]
}
[/block]


A message displays “Asset registered successfully”. This completes the asset registration for Webex Contact Center.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8d430f8-2.jpg",
        null,
        "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped Messenger App."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped Messenger App."
    }
  ]
}
[/block]


As shown above, you will see a <<WebexCC>> icon and a PCI check enabled flag next to the Facebook Messenger asset once it's been successfully mapped with Webex Contact Center.

Once the asset is registered, this asset will be available for entry point mapping in Webex Contact Center portal.

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
        "Screentshot of Manage Facebook Messenger app asset"
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
        "https://files.readme.io/1c4e70bfa642d9a9c90137165760071653f67b6afa3c7df36d02846f67f44015-Facebook_Messenger_app_asset.png",
        "",
        "Screenshot of Deleting Facebook Messenger app asset"
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
        "https://files.readme.io/c518d5d-image.png",
        null,
        "Screenshot of Integrated Pages."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Integrated Pages."
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
> We recommend you to not enable the **Get Started** button on the Messenger app configuration screen under  Assets --> Apps section when using <<prodname>> for supporting Messenger for Webex Contact Center.

## Persistent Menu

The persistent menu allows you to have an always-on user interface element inside conversations. This is an easy way to help people discover and access the core functionality at any point in the conversation. You have to enable the "get started" button in the welcome screen to configure Persistent Menu.

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


You can refer [Messenger documentation on Persistent Menus](https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu/) to know more about this feature such as best practices, limitations, etc.

**Supported Buttons :**The persistent menu is composed of an array of [buttons](https://developers.facebook.com/docs/messenger-platform/send-messages/buttons). The following button types are supported in the persistent menu:

- [Open URL](https://developers.facebook.com/docs/messenger-platform/send-api-reference/url-button): Opens URL on Messenger webview
- Postback: Triggers the postback event

When a Messenger user clicks an item in the menu, a postback event notification is received as part of inbound notifications like in start node, receive node and outbound webhooks. The event notification contains information about what item was select and by whom. This item selection action opens the standard messaging window wherein the Business has 24 hours to respond to the Messenger user.

### Requirements

For the persistent menu to appear, the following must be true:

- The person must be running Messenger v106 or above on iOS or Android.
- The Facebook Page the Messenger bot is subscribe to must be published.

### Disable Free Text Input

You can choose to disable the messenger composer to make the persistent menu and inline messages like message postbacks and quick replies, the only way a person can interact with your page. This is useful when your page is used for very specific functions and you do not want to entertain a free text conversation.

## Best Practices

**Dos**

- Like buttons, menu items can produce a webview or postback. Keep in mind that a second-level menu is not supported.
- Use the menu for entry points into your Business page.
- Be descriptive: your menu lets people know what your Business page can do. It instantly lets users know how they can reach your Business in the future. 

**Donts**

- Be selective to represent the core functions of your Business page and try to limit menu items to 5.
- The menu is designed to contain Messenger user-specific data.
- Don't put a "Menu" button in the menu that sends the user a message containing a menu. 
- Don't put generic actions like "Restart" in the menu.
- Don't use prime menu real estate for secondary, "colophon"-style info like about, terms of service, privacy policy, or "powered by,"  neglecting to expose your Business page's main functionality.

## Allowed List Domains

Add the web domains that need to be accessible from Facebook Messenger.

## Subscription Messaging

Enable this feature to allow the Facebook page to send non-promotional content through the Messenger channel. This feature is available only for clients who have Facebook's permission to use it.

## Page Discovery Plugins

The Page Discovery plugins allow you to integrate the Facebook Messenger chat experience directly onto a website/webpage for a personalized experience. This allows your customers to interact with your business anytime with a click of a button.

To use the below plugins, you should include the code snippet provided on your webpage along with Facebook's JavaScript SDK. The website domain must also be in the allowed list on which you wish to use this plugin.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ad6844e-21477992_1945714059029979_5620422387120996352_n.png",
        "21477992_1945714059029979_5620422387120996352_n.png",
        "Screenshot of Send to Messenger."
      ],
      "align": "center",
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
        "Screenshot of Checkbox Plugin"
      ],
      "align": "center",
      "caption": "Checkbox Plugin"
    }
  ]
}
[/block]


> 🚧 Opt-In plugins
> 
> Support for Opt-ins received through Send to Messenger and Check box plugins is not available at the moment. We are currently working to restore these features and will continue to update this document and the release notes section with the details as they are available.