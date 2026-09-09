# Live Chat - WXCC

Source: https://help.webexconnect.io/docs/livechat-asset-creation-wxcc
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:12+00:00

Cisco Webex Contact Center users who want to use Live Chat as a channel of customer support with Webex Contact Center can configure a Live Chat asset with Webex Connect by following the below steps:

## Configuring Live Chat channel asset on Webex Connect

> 📘 
> 
> Please note that In-App messaging on Android and iOS is not available for Webex CC integrated Connect tenants at the moment. The below configuration steps are applicable for Live Chat over websites/web browsers alone.

You can create a Live Chat asset in Webex Connect (for enabling customer support over Live Chat in combination with Webex Contact Centre) by following the below steps:

1. Log in to the Webex Connect platform.
2. Go to **Assets** → **Apps** section.
3. Click **Configure New App** and click **Mobile / Web**. 
4. Enter a user-friendly name for your Live Chat asset.
5. Toggle the Live Chat to enable the configuration section.

   

![Screenshot of Configuring New Mobile & Web App Page](https://files.readme.io/8faf5bb4145436a1154438d2fa72672be9d3d424ab955391bb9d77e2fe62ab85-image.png)


6. Select **MQTT** or **Web Socket** from the Primary Transfer Protocol. Message delivery is attempted via a primary protocol and in case of failure, the delivery falls back on the secondary protocol.
7. Select **MQTT** or **Web Socket** from the Secondary Transfer Protocol. E.g., if you selected MQTT as the primary protocol, select Web Socket as the secondary protocol.
8. Select **'Use Secured Port' ** checkbox. This is mandatory for Webex Connect and Cisco Webex Contact Center integration.
9. Do not select **'Enable payload encryption'** checkbox. This setting is not applicable for Webex Connect and Cisco Webex Contact Center integration.



![Screenshot of Enabling Use Secured Port in Configuring New Mobile & Web App Page](https://files.readme.io/2cf2d41-2.jpeg)






![Screenshot of enabling Server Side Inbox in Configuring New Mobile & Web App Page.](https://files.readme.io/8ef152f-3.png)




10. Click 'Save'. The 'Register To Webex Contact Center' action button becomes available once you've completed this step.

## Registering your Live Chat App Asset with Webex Contact Center

Once you’ve successfully configured your Live Chat asset with Webex Connect, you can register it with Webex Engage by following the below steps:

1. Go to Assets > Apps.
2. Select Mobile / Web option in the ‘App Type’ drop-down list box.
3. Click the required Live Chat asset.
4. Click 'Register to Webex Engage'.  
   The Register to Webex Engage pop-up displays.



![Screenshot of Register to Webex Engage.](https://files.readme.io/bf8784b-4.jpg)




5. Select the required service and click Register (Note: this should be the Webex Connect service that would be used for configuring Live Chat flows for Webex Contact Center).
6. Click Register.

> 🚧 
> 
> - You cannot change the service mapping once done. Hence, the asset registration on Webex Engage should be done after the service to be used has been decided. 
> - Do not delete a Live Chat asset once it's been registered with Webex Engage. Once deleted it cannot be restored. Doing so would lead to asset deletion within Webex Connect alone while the entry continues to be in Webex Contact Center and Webex Engage.

A message displays “Asset registered successfully”. This completes the asset registration for Webex Contact Center.



![Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped Mobile/ Web Asset.](https://files.readme.io/b903f56-5.jpg)




As shown above, you will see a Cisco Webex Contact Center icon and a PCI check enabled flag next to the Live Chat asset once it's been successfully mapped with Webex Contact Center.

> 📘 
> 
> Once the asset is registered, this asset will be available for entry point mapping in the Cisco  Webex Contact Center portal.
> 
> The Live Chat widget design configuration needs to be done within Webex Engage. The code for embedding a live chat widget on your website also is available within Webex Engage.