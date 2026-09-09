# Messenger

Source: https://help.webexconnect.io/docs/facebook-messenger
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:03+00:00

Facebook Messenger has over 1.3 billion active users and is one of the most feature-rich social platforms available for businesses to reach customers today.

Users can easily connect their Facebook pages with Webex Connect and build rich messaging experiences using messaging API and/or flow builder. We support various rich messaging features offered by Facebook Messenger such as carousels, quick replies, emojis, persistent menus, and templates.

> 📘 Messenger Graph API version upgrade
> 
> The Messenger version for Webex Connect v5.5.3 or below is v3.2 to v6.0. The Messenger version for Webex Connect v5.6.0 is v8.0 to v16.0.

## Configuring your Messenger App on Webex Connect

> 📘 Messenger Usage
> 
> Messenger as a channel is supported in the Canada region as well.

You can register your Facebook Messenger page with Webex Connect from 'Assets > Apps' section. Following are the steps for registering:

1. Select **Messenger ** from **Configure New App** dropdown. 
2. Provide a name for your Messenger app asset and click **Add Messenger Page**. You must be the admin of the Facebook page to integrate Facebook Messenger with Webex Connect. At this stage, you'll be redirected to your Facebook login page.



![Screenshot of Configure New Messenger App Page.](https://files.readme.io/dfbec0e-Assets_Messenger_Configuring_your_Messenger_App_on_imiconnect.png)




3. Provide the login credentials. You may not see this step if you're already logged in.
4. Select the page that you want to register on the **What Pages do you want to use with Webex Connect?**pop-up.
5. Provide the requested access permissions, and click **Done**.  
   At this stage, you'll be redirected to Webex Connect. If you selected multiple pages in the previous step, you'll be asked to choose the page that you want to use for the asset you are configuring. Select the required page.

> 📘 Note
> 
> Only the Tenant owner user role will be allowed to make changes to Facebook Messenger page after it is configured to avoid accidental / unintended changes by other platform users.

Once done, you'll see the following screen.



![Adding a Facebook page to Webex Connect - Assets -> Apps -> Configure New App](https://files.readme.io/2fc5ecc-1.jpg)




## Welcome Screen

You can optionally choose to configure the welcome screen for your Facebook Messenger customers. Switch the Welcome Screen toggle to Enabled, and provide a greeting message for the Welcome Screen (minimum three characters long).



![Welcome Screen](https://files.readme.io/f04763c-14302685_243106819419381_1314180151_n.png)




You can choose to enable a 'Get Started' button, which allows end customers to start a conversation with you. When a person taps the 'Get Started' button, the 'Get Started' message will be posted into the conversation (the configured 'Postback Payload' value is posted back to any associated Rule or relevant Flow Start Node or Receive Node when this event happens), and your flow is then granted permission to send messages.

## Persistent Menu

The persistent menu allows you to have an always-on user interface element inside conversations. This is an easy way to help people discover and access the core functionality at any point in the conversation. You have to enable the "get started" button in the welcome screen to configure Persistent Menu.



![Persistent Menu](https://files.readme.io/0c817c8-Messenger_Persistent_Menu.jpg)




You can refer [Messenger documentation on Persistent Menus](https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu/) to know more about this feature such as best practices, limitations, etc.

## Allowed List Domains

Add the web domains that need to be accessible from Facebook Messenger.

## Subscription Messaging

Enable this feature to allow Facebook page to send non-promotional content through Messenger channel.

## Page Discovery Plugins

The Page Discovery plugins allow you to integrate Facebook Messenger chat experience directly onto a website/webpage for a personalized experience. This allows your customers to interact with your business anytime with a click of a button.

To use the below plugins, you should include the code snippet provided on your webpage along with Facebook's JavaScript SDK. The website domain must also be in the allowed list on which you wish to use this plugin.



![Message Us](https://files.readme.io/c447f16-23423215_1791233210947700_2174958476483100672_n.png)






![Send to Messenger](https://files.readme.io/ad6844e-21477992_1945714059029979_5620422387120996352_n.png)






![Checkbox Plugin](https://files.readme.io/5b81fd6-13679808_631224743722018_2016203957_n.png)




> 🚧 Opt-In plugins
> 
> Support for Opt-ins received through Send to Messenger and Check box plugins is not available at the moment. We are currently working to restore these features and will continue to update this document and the release notes section with the details as they are available.

| Name       | Description                                                                                                            |
| :--------- | :--------------------------------------------------------------------------------------------------------------------- |
| Message Us | Renders a button when clicked on, redirects the users to Facebook Messenger and opens a conversation within your page. |

## Page Discovery Add-ons



![Messenger Code](https://files.readme.io/f1a185b-16685647_261975084241469_2329165888516784128_n.png)






![m.me Link](https://files.readme.io/9e2de0e-6a7978c-21274929_1469790786436315_8432829112128634880_n.png)




> 🚧 Messenger code deprecated
> 
> Starting August 15 2019, The Messenger camera no longer supports scanning Messenger Codes.
> 
> As an alternative, Messenger recommends businesses take advantage of the phone's native capabilities to scan QR codes with embedded m.me links. For more details, refer to the [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/discovery/m-me-links/#qr_codes) documentation.



| Name | Description |
| --- | --- |
| Messenger Code | You can make the QR codes of your webpage available on Facebook Messenger so that the users can directly scan the codes from the mobile app to start a conversation.  <br>  <br>**Image Size**:  the size of the QR code image in pixels  <br>  <br>**Add Referral Payload**: enable this to add a payload for the QR code. Enter the payload in the **Ref Payload** field. You can generate different messenger codes with different referral payload. The referral payload is part of the first message the user scans the code. You can use this to track referral code traction or you can use to activate different journey for different Messenger code scan. |
| Messenger Link | Your messenger link is a shortened URL that people can use to go directly into a Messenger conversation. |




## Authorization Expiry

The following is a list of scenarios in which the authorization of your Messenger app will expire:

1. When you change your Facebook/Messenger login password.
2. If the user who requested the token no longer has a role on the page
3. If you deselect any of the integrated pages when adding a new page in the Webex Connect platform. Make sure to include all the integrated pages.

   > 📘 Authorization Expiry
   > 
   > While adding a new page, please make sure to select all the pages that have been integrated with Webex Connect platform previously in the Facebook login flow.

   <br />

   

![Screenshot displaying of List of Messenger Page.](https://files.readme.io/ccc3787-Facebook_login_flow.png)


4. You can delink the messenger page from the Webex Connect platform from messenger page settings.

### Reauthorization of Messenger

If any time the user’s asset gets delinked by gaining any of the mentioned scenarios, you can reauthorize the same asset by following the  below steps:

1. Navigate to the **Assets** > **Apps **section. Select Messenger from the Apps dropdown.
2. Click **Reauthorize Page** to relink the page from the Webex Connect platform from the messenger page settings.

   

![Reauthorize Page](https://files.readme.io/e8439bf17e1f23198c6e2508532a87efbee0ddb2436fe74cd28a2b8c6a5d2a82-image.png)


3. Click **Reauthorize **to confirm the reauthorization of the Messenger page.

   

![Reauthorize- Messenger Page](https://files.readme.io/e19d3ab619b4068f9611d0e89b0ab4f052ad0881a9dd38183a4d3d3e1297c1c6-image.png)


4. Select Messenger Page, which appears with an auto-selected page from the list, and click **Next**.

   

![Select Messenger Page- Confirm](https://files.readme.io/090b549fc083c425fd9b8c04f5bc783e3cf17d8dc90afb314aa74bf660136d73-image.png)


5. Click **Confirm **to reauthorize successfully.

## Edit/Manage/Delete the Facebook Messenger App Asset

1. Go to **Assets** > **Apps**.
2. Search for the Messenger app asset that you want to edit and click **Manage** in the drop-down list box at the right to manage the settings of this app.  
   You see the **Manage – Messenger** page, where you can manage the settings of the app.



![Manage Facebook Messenger app asset](https://files.readme.io/913190353ebfe01ac7ce64fc05e9c86c6e275cecc1ef087ae49379caab323da3-Facebook_Messenger_-_Manage_app.png)




### Delete Facebook Messenger App Asset

1. Go to Assets > Apps.
2. Search for the Facebook Messenger app asset that you want to edit and click **Delete** in the drop-down list box at the right to delete the app.



![Deleting Facebook Messenger app asset](https://files.readme.io/4dad07ff7b5588d5b765c05d3842cc50a927bce387a195528695a72bafda66a3-Facebook_Messenger_app_asset.png)




## Using the Channel

### User Identity

To message users on Facebook Messenger you need the **PS ID** of the users. You receive this when a user messages the business for the first time.

### API

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download](https://www.getpostman.com/) Postman from official site.

### Webhooks

Once a Facebook Messenger app is configured, you can configure [Outbound Webhooks](https://help.webexconnect.io/docs/outbound-webhooks) by choosing the Facebook Messenger app from the entity dropdown to receive incoming messages and events from your customers.

```json Text
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "38b0b8da-c3ed-44cd-bc9e-2403bea529cd_0",
  "message": "Simple Text",
  "attachments": "",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Image attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "158828d0-9242-472b-bf25-e67026c69636_0",
  "message": "",
  "attachments": "[{\"payload\":{\"url\":\"https:\/\/scontent.xx.fbcdn.net\/v\/t35.0-12\/13682620_539022026303737_1111397419_o.jpg?_nc_ad=z-m&oh=5f15c5db7900be7a79ec5f7810a3d4be&oe=579C2B3D\"},\"type\":\"image\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Video attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "cd5c3fea-0169-4075-a50c-ddfd731d73eb_0",
  "message": "",
  "attachments": "[{\"payload\":{\"url\":\"https:\/\/video.xx.fbcdn.net\/v\/t42.3356-2\/13862946_539025056303434_1490024390_n.mp4\/video-1469713591.mp4?vabr=261485&oh=9046f1a7f78711f8c929df57620c6515&oe=579BBDDF\"},\"type\":\"video\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Audio attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "f4feefdc-f16c-4de2-887a-9b22bcbc4b9d_0",
  "message": "",
  "attachments": "[{\"payload\":{\"url\":\"https:\/\/cdn.fbsbx.com\/v\/t59.3654-21\/13691952_539021966303743_1334694100_n.aac\/audioclip-1471699879041-4420.aac?oh=b5c676bbf78b620559bcaeec790b2573&oe=579D2E33\"},\"type\":\"audio\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Sticker attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "3c131e54-1a3e-46d7-9a84-e9985a8e2f33_0",
  "message": "",
  "attachments": "[{\"payload\":{\"url\":\"https:\/\/scontent.xx.fbcdn.net\/t39.1997-6\/p100x100\/10333099_298592936987572_2124775027_n.png?_nc_ad=z-m\"},\"sticker_id\":\"298592933654239\",\"type\":\"sticker\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Location attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "6488520b-2f43-4d6d-98b2-65f7f9f087d8_0",
  "message": "",
  "attachments": "[{\"title\":\"Joe's Location\",\"payload\":{\"coordinates\":{\"long\":78.398511094914,\"lat\":17.434871564442}},\"type\":\"location\",\"url\":\"https:\/\/www.facebook.com\/l.php?u=https%3A%2F%2Fwww.bing.com%2Fmaps%2Fdefault.aspx%3Fv%3D2%26pc%3DFACEBK%26mid%3D8100%26where1%3D17.434871564442%252C%2B78.398511094914%26FORM%3DFBKPL1%26mkt%3Den-US&h=oAQGHo3bQ&s=1&enc=AZOWktitnAQChz53RmIFyV-Y-wNJKMktlhVDAeDSAA8fVi0nwdSIoAhQIxfYk8CbRft6rYKn5Ppp95-TFlIWzh-TPFRQBRRfx9jpLyjhjGqo2g\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json File attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "66a810e7-7800-4567-9316-f2f580e9e6c4_0",
  "message": "",
  "attachments": "[{\"payload\":{\"url\":\"https:\/\/cdn.fbsbx.com\/v\/t59.2708-21\/11645068_10207285897933930_1035858644_n.doc\/sample.doc?oh=9a50be5da6b06c60f76410d2d8973972&oe=579C0291\"},\"type\":\"file\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Link attachment
{
  "userId": "8953",
  "channel": "Facebook",
  "appId": "a_636035637428953782",
  "event": "MO",
  "psid": "1037878796267914",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "9aef3e3c-6fa0-431d-9ab4-17dd57cde2c5_0",
  "message": "https://www.goal.com",
  "attachments": "[{\"title\":\"Goal.com\",\"payload\":null,\"type\":\"link\",\"url\":\"https%3A%2F%2Fwww.goal.com%2F\"}]",
  "locale": "en_US",
  "gender": "male",
  "timezone": "5.5"
}
```
```json Authentication - Opt-In
{
  "userId": "",
  "channel": "Facebook",
  "psid": "1635633030094183",
  "appId": "a_635984672401175940",
  "event": "OnOptin",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "0db0a903-aa44-4b6b-8851-8e0f068b5608_0",
  "name": "Jack Suraj",
  "profile_pic": "https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/11988450_1499437227047098_59962553964862977_n.jpg?oh=657d5460db724d720780dd9cf2a014af&oe=5818524C",
  "optin": "{\"ref\":\"prod26\"}"
}
```
```json Postback
{
  "userId": "8953",
  "channel": "Facebook",
  "psid": "1037878796267914",
  "appId": "a_636035637428953782",
  "event": "OnPostback",
  "ts": "2015-04-12T13:00:19.456Z",
  "timeStamp" : "2015-04-12T13:00:19.456Z",
  "tid": "20cbc7d1-be4e-416b-8250-d8bd4f303d0f_0",
  "name": "Joe James",
  "profile_pic": "https://scontent.xx.fbcdn.net/v/t1.0-1/s200x200/10354686_10150004552801856_220367501106153455_n.jpg?oh=afdc2c35d5b7230522ee0353a8aff5e8&oe=5824CE50",
  "postback": "{\"payload\":\"1232\"}"
}
```

To receive delivery receipts of the messages you sent out, configure [Outbound Webhooks](https://help.webexconnect.io/docs/outbound-webhooks) on the service from which you sent the message.

```json Submitted
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "fb",
            "Description": "Submited",
            "destinationType": "psid",
            "timeStamp": "2016-07-21T12:44:23.644",
            "code": "7501",
            "deliveryStatus": "Submited",
            "destination": "1368028456544331"
        },
        "correlationid": "3bd8edf31c81-4b72d8a2-290d-49e2-993e",
        "callbackData": "return callbackdata",
        "transid": "4b72d8a2-290d-49e2-993e-3bd8edf31c81"
    }
}
```
```json Delivered
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "fb",
            "Description": "Delivered",
            "destinationType": "psid",
            "timeStamp": "2016-08-12T07:00:15.537",
            "code": "7500",
            "deliveryStatus": "Delivered",
            "destination": "1107152119374928"
        },
        "correlationid": "cid",
        "callbackData": "",
        "transid": "e389acdf-f751-45c1-90da-2262bd252ee6"
    }
}
```
```json Read
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "fb",
            "Description": "End point not reachable(FB is not reachable)",
            "destinationType": "psid",
            "timeStamp": "2017-08-29T23:00:22.961Z",
            "additional_info" : {
               "error" : {
                   "message" : "Errorvalidatingaccesstoken:ThesessionhasbeeninvalidatedbecausetheuserchangedtheirpasswordorFacebookhaschangedthesessionforsecurityreasons.",
                   "error_subcode" : 460,
                   "fbtrace_id" : "HV9WpzzqdS8",
                   "code" : 190,
                   "type" : "OAuthException"
               }
            },
            "code": "7010",
            "additionalInfo" : "",
            "deliveryStatus": "Failed",
            "destination": "110715211937428"
        },
        "correlationid": "",
        "callbackData": "",
        "transid": "a454423a-722d-4c40-9af9-56cd3696da8a"
    }
}
```
```json Failed
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "fb",
            "Description": "Read",
            "destinationType": "psid",
            "timeStamp": "2016-10-25T06:20:59.753",
            "code": "7502",
            "deliveryStatus": "Read",
            "destination": "1277069878990108"
        },
        "correlationid": "",
        "callbackData": "",
        "transid": "df7d2dc8-e3dd-4fa4-a593-6679b59dc6ab"
    }
}
```

## Message Types

Facebook Messenger DM supports the following message types:

1. Text
2. Attachments (Image, Audio, Video, and File)
3. Generic Template



![Generic Template](https://files.readme.io/8507c37-facebook-generic-template.png)




4. Button Template



![Button Template](https://files.readme.io/65ddf3a-dd93a72-facebook-button-template.png)




5. Receipt Template



![Receipt Template](https://files.readme.io/6a5258e-68747470733a2f2f636c61756469616a732e636f6d2f6173736574732f66616365626f6f6b2f726563656970742e706e67.png)




All the messages support quick replies.



![Quick Replies](https://files.readme.io/dd68181-Xbb3k.png)




## Rules

When you select Facebook Messenger as the channel, the following events and actions are available for configuration:



| Channel Events | Actions |
| --- | --- |
| _ Incoming message  <br>  _ On link click  <br>  _ Postback  <br>  _ Profile creation  <br>  \* Profile update | _ Send Messenger Message  <br>_ Invoke a Flow  <br>\* Forward to BOT |




## Flows

In flow, you can configure the [Receive](https://help.imiconnect.io/docs/receive) node to receive messages from a Facebook page and the [Messenger](https://help.webexconnect.io/docs/messenger) node enables you to send messages on to Facebook end-user.

## FAQs

You can refer to the [Messenger channel FAQs](https://developers.imiconnect.io/reference/facebook-messenger-faqs) for contextual information.