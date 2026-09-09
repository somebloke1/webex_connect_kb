After you provision your Facebook Messenger page as a channel asset on Webex Connect, you need to register it with WxEngage to use it for your business’s contact center use case. In addition, Webex Engage requires a Connect service to deliver outbound messages from your contact center, so kindly ensure you have created a service to register this Messenger page with Engage. Refer to the procedure for [creating a WxConnect service](https://help.webexconnect.io/docs/create-a-service-on-imiconnect).

To register your Facebook Messenger page with WxEngage, follow the below steps:

1. Navigate to Assets > Apps.
2. Click the Facebook Messenger channel asset you’d like to register from the Apps column.

The following screen appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/076f6350f3c8ad07be399936318c3702bd9eba1ec0d3f8cd672654f7dd449f67-image.png",
        null,
        "Screenshot of Managing the Messenger App Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing the Messenger App Page"
    }
  ]
}
[/block]


3. Click **Register to Webex Engage**.  
   The following pop-up window appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ff4b128fc0fef5f0ce0620276b9b9dff49e0d52e2767b04fc579ccf6c54375b5-image.png",
        null,
        "Screenshot of Register to Webex Engage"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Register to Webex Engage"
    }
  ]
}
[/block]


4. Choose a Service that you created in the pre-requisite step from the **Select Service** drop-down and click **Register**.

- Your channel asset will be linked to the Default Team on WxEngage by default. Suppose you want to change this setting or share the asset with multiple teams to facilitate transfers or enable agent-initiated outbound communications from different teams. In that case, you can manage these configurations in your Engage tenant's Admin console. For more information on managing your assets in Engage, please refer to the provided link.
- After seeing the success toast message on WxConnect, you can log in to your WxEngage tenant to confirm that your Facebook Messenger channel asset has been synced. Then, you can continue with further contact center configurations from the WxEngage Admin console.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/50408897e12abed5e81d75a55347e36f4a53faf56b9881bd283bed70f92db186-image.png",
        null,
        "Screenshot of registering the asset successfully with Webex Engage."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of registering the asset successfully with Webex Engage"
    }
  ]
}
[/block]


Once the Facebook Messenger asset is mapped with the Webex Contact Center, you will view a Webex Contact Center (TBC) icon and a PCI check enabled flag next to it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/814e535346d1c5262a3d3754ac0c2fd8ca48c3a7a7bfc8f246bd3f916ccd32ee-image.png",
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


> 📘 Warning
> 
> - You cannot change the service mapping after successfully establishing it. Therefore, asset registration on Webex Engage should happen only after deciding on the service to be used.
> - Do not delete an Facebook Messenger asset after registering with Webex Engage, as you cannot restore the asset after deleting it. Doing so would lead to asset deletion within Webex Connect alone while the entry continues to be in Webex Engage.