After you provision your SMS longcode on Webex Connect, you must register it with WxEngage to use it for your business’s contact center use case. You need a number provisioned for messaging (SMS) to support bi-directional messaging. Ensure it is a longcode, not an alphanumeric sender ID, as they do not support bi-directional messaging. In addition to this, WxEngage will require a Connect service to deliver outbound messages from your contact center. Therefore, you must create a service to register this number with Engage. Refer to the procedure for [creating a WxConnect service](https://help.webexconnect.io/docs/create-a-service-on-imiconnect).

To register your SMS number with WxEngage, follow the below steps:

1. Navigate to Assets > Numbers.
2. Click the number from the Numbers column you’d like to register.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/601ea6e517ec70de6a7f5c007bdab865fe334e8951c053b5b4f3a154b98c0117-image.png",
        null,
        "Screenshot of Number Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Number Page"
    }
  ]
}
[/block]


The following screen appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/19d639abf6466bf7392053a70c3e0250ec9d112724aa1e4897c44ef66ee9dfd6-image.png",
        null,
        "Screenshot of Manage Phone Number Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage Phone Number Page"
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
        "https://files.readme.io/a64d8e47702bc5fcca7da8f2e5a28cea683c2bab8b92057b5ea3bb394ff41717-image.png",
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
- After seeing the success toast message on WxConnect, you can log in to your WxEngage tenant to confirm that your SMS channel asset has been synced. Then, you can continue with further contact center configurations from the WxEngage Admin console.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d684b79fa0b1cc97995c74825c966ebd80353196a1d2da2b105f653502e3504b-image.png",
        null,
        "Screenshot of registering the asset successfully with Webex Engage"
      ],
      "align": "center",
      "caption": "Screenshot of registering the asset successfully with Webex Engage"
    }
  ]
}
[/block]


Once the number is mapped with the Webex Contact Center, you will view a Webex Contact Center (TBC) icon and a PCI check enabled flag next to the number.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/92c2a678cf2d0d3d9e809992325919f89362dc637446af57ae24bfee1b3a2fa8-image.png",
        null,
        "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number."
      ],
      "align": "center",
      "caption": "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number"
    }
  ]
}
[/block]


> 📘 Warning
> 
> - You cannot change the service mapping after successfully establishing it. Therefore, asset registration on Webex Engage should happen only after deciding on the service to be used.
> - Do not delete an SMS asset after registering with Webex Engage, as you cannot restore the asset after deleting it. Doing so would lead to asset deletion within Webex Connect alone while the entry continues to be in Webex Engage.