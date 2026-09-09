Webex Engage users who want to use Live Chat as a channel of customer support with Cisco Contact Center Enterprise can configure a Live Chat asset with <<prodname>> by following the below steps:

## Configuring Live Chat channel asset on Webex Connect

> 📘 
> 
> Please note that In-App messaging on Android and iOS is not available for <<CCE>> integrated - <<prodname>> tenants at the moment. The below configuration steps are applicable for Live Chat over websites/web browsers alone.

You can create a Live Chat asset in <<prodname>> (for enabling customer support over Live Chat in combination with Cisco Contact Center Enterprise) by following the below steps:

1. Log in to the <<prodname>> platform.
2. Go to **Assets** → **Apps** section.
3. Click Configure New App and select Mobile/Web.
4. Enter a user-friendly name for your Live Chat asset.
5. Enable Live Chat Messaging configuration section.

   [block:image]{"images":[{"image":["https://files.readme.io/c5f7e86e054b39ad657e949c71bb734dcbb233508a29c77a90bad30b13ebd67a-image.png",null,null],"align":"center","border":true,"caption":"Screenshot of Configuring a New Mobile & Web App Page"}]}[/block]
6. Select the Primary Transfer Protocol - MQTT or Web Socket. Message delivery is attempted via a primary protocol and in case of failure, the delivery falls back on the secondary protocol.
7. Select the Secondary Transfer Protocol - MQTT or Web Socket. E.g., if you selected MQTT as the primary protocol, select Web Socket as the secondary protocol.
8. **Select 'Use Secured Port' checkbox.** This is a must have for <<prodname>> and Cisco Contact Center Enterprise integration.
9. **Do not select 'Enable payload encryption' checkbox**. This setting is not applicable for <<prodname>> and Contact Center Enterprise integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6dd5dc6-7.jpg",
        "CCE_Live_Chat_Configure_2.png",
        "Screenshot displaying to enable Use Secured Port"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying to enable Use Secured Port"
    }
  ]
}
[/block]


10. Click 'Save'. The 'Register To Webex Engage' action button becomes available once you've completed this step.

## Registering your Live Chat App Asset with Webex Engage

Once you’ve successfully configured your Live Chat asset with <<prodname>>, you can register it with Webex Engage by following the below steps:

1. Go to Assets ->Apps.
2. Select Mobile/Web option in the ‘App Type’ drop-down list box.
3. Click the required Live Chat asset.
4. Click 'Register to Webex Engage'.  
   The Register to Webex Engage page displays.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0dae2a7-1.jpg",
        "Register_Webex_Engage.PNG",
        "Screenshot of Register to Webex Engage"
      ],
      "align": "center",
      "sizing": "450px",
      "border": true,
      "caption": "Screenshot of Register to Webex Engage"
    }
  ]
}
[/block]


5. Select the required service and click Register (Note: this should be the <<prodname>> service that would be used for configuring Live Chat flows for Cisco Contact Center Enterprise integration and click Register).

> 🚧 
> 
> - You cannot change the service mapping once done. Hence, the asset registration on Webex Engage should be done after the service to be used has been decided. 
> 
>   - Do not delete a Live Chat asset once it's been registered with Webex Engage. Once deleted it cannot be restored. Doing so would lead to asset deletion within <<prodname>> alone while the entry continues to be in Webex Engage.

A message displays “Asset registered successfully”. This completes the asset registration for Cisco Contact Center Enterprise integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b330cc7-3.jpg",
        "Post_Registration_Engage.png",
        "Screenshot displaying the Webex Engage icon and PCI check enabled flag next to a mapped Mobile/Web Asset."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Webex Engage icon and PCI check enabled flag next to a mapped Mobile/Web Asset."
    }
  ]
}
[/block]


As shown above, you will see a Webex Engage icon and a PCI check enabled flag next to the Live Chat asset once it's been successfully mapped with Cisco Contact Center Enterprise.

> 📘 
> 
> The Live Chat widget design configuration needs to be done within Webex Engage. The code for embedding a live chat widget on your website also is available within Webex Engage.