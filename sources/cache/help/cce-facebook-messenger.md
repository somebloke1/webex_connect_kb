# Facebook Messenger - CCE

Source: https://help.webexconnect.io/docs/cce-facebook-messenger
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:20+00:00

Cisco Contact Center Enterprise (CCE) users who want to use Facebook Messenger as a channel of customer support with Webex Contact Center can use the first procedure for connecting their Facebook pages with Webex Connect, and then registering their Messenger app on Webex Engage.

## Configuring your Messenger App on Webex Connect

> 📘 Messenger Usage
> 
> Messenger as a channel is supported in the Canada region as well.

You can register your Facebook Messenger page with Webex Connect from 'Assets -> Apps' section. Here are the steps for registering:

1. Select **Messenger ** from **Configure New App** dropdown. 
2. Provide a name for your Messenger app asset and click **Add Messenger Page**. You must be the admin of the Facebook page to integrate Facebook Messenger with Webex Connect . You will be redirected to your Facebook login page.



![Screenshot of Creating the New Messenger App Page](https://files.readme.io/ad279d1-FB1.jpg)




3. Provide the login credentials. You may not see this step if you're already logged in.
4. Select the page that you want to register on the **What pages do you want to use with Webex Connect** pop-up.
5. Provide the requested access permissions, and click **Done**.  
   At this stage, you will be redirected to Webex Connect. If you have selected multiple pages in the previous step, you will be asked to choose the page that you want to use for the asset you are configuring. Select the required page. Once done, you'll see the following screen.

   

![Screenshot of Managing the Facebook Messenger App](https://files.readme.io/883e862-Facebook_Messenger_-_Configure_New_App.jpeg)



   > 📘 Note
   > 
   > Only the Tenant with the user role 'Owner' will be allowed to make changes to Facebook Messenger page after it is configured, to avoid accidental / unintended changes by other platform users.
6. Click **Save**. This completes the association of your Facebook Messenger page with Webex Connect. We do support advanced settings such as Welcome Screen, Persistent Menu, etc. but those are optional. Refer to the last section for information on the advanced settings.



![Screenshot of Facebook Messenger and platform association](https://files.readme.io/ccc3787-Facebook_login_flow.png)




## Configuring Welcome Screen, Persistent Menu, etc.

### Welcome Screen

You can optionally choose to configure the welcome screen for your Facebook Messenger customers. Switch the Welcome Screen toggle to Enabled, and provide a greeting message for the Welcome Screen (minimum three characters long).



![Welcome Screen](https://files.readme.io/f04763c-14302685_243106819419381_1314180151_n.png)




> 📘 
> 
> We recommend you to not enable the **Get Started** button on the Facebook Messenger app configuration screen under Assets --> Apps section when using Webex Connect for supporting Facebook Messenger for Webex Contact Center.

### Persistent Menu

The Persistent Menu allows you to have an always-on user interface element inside conversations. This is an easy way to help people discover and access the core functionality at any point in the conversation. You have to enable the 'Get Started' button in the welcome screen to configure Persistent Menu.



![Persistent Menu](https://files.readme.io/0c817c8-Messenger_Persistent_Menu.jpg)




You can refer to the [Messenger documentation on Persistent Menus](https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu/) topic to know more about this feature such as best practices, limitations, etc.

## Allowed List Domains

Add the web domains that need to be accessible from Facebook Messenger.

### Subscription Messaging

Enable this feature to allow Facebook page to send non-promotional content through Messenger channel. This feature is available only for clients who have Facebook's permission to use it.

### Page Discovery Plugins

The Page Discovery plugins allow you to integrate Facebook Messenger chat experience directly onto a website/webpage for a personalized experience. This allows your customers to interact with your business anytime with a click of a button.

To use the below plugins, you should include the code snippet provided on your webpage along with Facebook's JavaScript SDK. The website domain must also be in the allowed list on which you wish to use this plugin.



![Send to Messenger](https://files.readme.io/ad6844e-21477992_1945714059029979_5620422387120996352_n.png)




| Name       | Description                                                                                                            |
| :--------- | :--------------------------------------------------------------------------------------------------------------------- |
| Message Us | Renders a button when clicked on, redirects the users to Facebook Messenger and opens a conversation within your page. |



![Checkbox Plugin](https://files.readme.io/5b81fd6-13679808_631224743722018_2016203957_n.png)




> 🚧 Opt-In plugins
> 
> Support for Opt-ins received through Send to Messenger and Check box plugins is not available at the moment. We are currently working to restore these features and will continue to update this document and the release notes section with the details as they are available.

For more information on detailed information about Messenger app configuration, refer to the [Messenger ](https://help.imiconnect.io/docs/facebook-messenger) chapter in the Assets section.

## Registering your Facebook Messenger App with Webex Engage

Once the asset has been saved, you will see a 'Register to Webex Engage' action button on top (ref: below screen).



![Screenshot of Managing the Messenger App Page - Register to Webex Engage](https://files.readme.io/af823a7-Register_Messenger_with_Webex_Engage.png)




1. Click **Register to Webex Engage**. A pop-up appears.



![Screenshot of Register to Webex Engage](https://files.readme.io/503db5c-Register_Messenger_with_Webex_Engage_Snippet.jpeg)




2. Select the required service (this should be the Webex Connect service that would be used for configuring Facebook Messenger flows for Webex Contact Center).
3. Click **Register**. 

> 🚧 
> 
> - Please note, the service mapping cannot be changed once done. Hence, the asset registration on Webex Contact Center should be done after the service to be used has been decided. 
> - Do not delete the Facebook Messenger asset once it's been registered with Webex CC. Once deleted, it cannot be restored. Doing so would lead to asset deletion within Webex Connect alone, while the entry continues to be in Webex CC and Webex Engage.



![Screenshot of Asset Registration Page](https://files.readme.io/3f8611e-Register_Messenger_with_Webex_Engage.png)




A message displays 'Asset registered successfully'. This completes the asset registration for Webex Contact Center.



![Asset registration completion](https://files.readme.io/387180d-PCI-enabled.jpeg)




As shown above, you will see a Cisco Webex Contact Center icon and a PCI check enabled flag next to the Facebook Messenger asset once it's been successfully mapped with Webex Contact Center.

Once the asset is registered, this asset will be available for entry point mapping in Cisco Webex Contact Center portal.

## Edit/Manage/Delete the Facebook Messenger App Asset

1. Go to **Assets** > **Apps**.
2. Search for the Messenger app asset that you want to edit and click **Manage** in the drop-down list box at the right to manage the settings of this app.  
   You see the **Manage – Messenger** page, where you can manage the settings of the app.



![Manage Facebook Messenger app asset](https://files.readme.io/913190353ebfe01ac7ce64fc05e9c86c6e275cecc1ef087ae49379caab323da3-Facebook_Messenger_-_Manage_app.png)




### Delete Facebook Messenger App Asset

1. Go to Assets > Apps.
2. Search for the Facebook Messenger app asset that you want to edit and click **Delete** in the drop-down list box at the right to delete the app.



![Deleting Facebook Messenger app asset](https://files.readme.io/378f7d9deeea8ca8519b98ab88a342d90eca5d7623076dd605b45b8bdac64005-Facebook_Messenger_app_asset.png)




## Facebook Messenger Authorization Expiry

The following is a list of scenarios in which the authorization of your Messenger app will expire:

1. When you change your Facebook/Messenger login password.
2. If the user who requested the token no longer has a role on the page
3. If you deselect any of the integrated pages when adding a new page in the Webex Connect platform. Make sure to include all the integrated pages.

> 📘 Authorization Expiry
> 
> While adding a new page, please make sure to select all the pages that have been integrated with Webex Connect platform previously in the Facebook login flow.



![Screenshot of delinking the Facebook Messenger page from Webex Connect platform](https://files.readme.io/ccc3787-Facebook_login_flow.png)




4. You can delink the messenger page from the Webex Connect platform from messenger page settings.