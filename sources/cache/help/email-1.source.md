After you provision your Business mailbox as a channel asset on Webex Connect, you need to register it with WxEngage to use it for your business’s contact center use case. In addition, Webex Engage requires a Connect service to deliver outbound emails from your contact center, so kindly ensure you have created a service to register this Business mailbox with Engage. Refer to the procedure for [creating a WxConnect service](https://help.webexconnect.io/docs/create-a-service-on-imiconnect).

> 📘 Note:
> 
> Webex Connect supports the following email service providers for the Live Agent Add-on:
> 
> - Gmail
> - Microsoft 365

To register your Business mail server with WxEngage, follow the below steps:

1. Navigate to Assets > Apps.
2. Click the Email channel asset you’d like to register from the Apps column.

The following screen appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6edecc70882d9330713702e3e8fb9725c504975a77887b3b9d548675f90f20ee-image.png",
        null,
        "Screenshot of Managing the Email App Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing the Email App Page"
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
        "https://files.readme.io/e6f5db4318bcb089bb9eb2ed5f682101a505b1acf3f7995c64ab8145ddb4b960-image.png",
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

- Your channel asset will be linked to the Default Team on WxEngage by default. Suppose you want to change this setting or share the asset with multiple teams to facilitate transfers or enable agent-initiated outbound communications from different teams. In that case, ybook             ou can manage these configurations in your Engage tenant's Admin console. For more information on managing your assets in Engage, please refer to the provided link.
- After seeing the success toast message on WxConnect, you can log in to your WxEngage tenant to confirm that your Email channel asset has been synced. Then, you can continue with further contact center configurations from the WxEngage Admin console.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/693bd295a98295e232685dc986d01e41cc457527f87f72f16abb88caeeff3202-image.png",
        null,
        "Screenshot displaying the list of Email Assets"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the list of Email Assets"
    }
  ]
}
[/block]


Once the Email asset is mapped with the Webex Contact Center, you will view a Webex Contact Center (TBC) icon and a PCI check enabled flag next to it.

> 📘 Warning
> 
> - You cannot change the service mapping after successfully establishing it. Therefore, asset registration on Webex Engage should happen only after deciding on the service to be used.
> - Do not delete an Email asset after registering with Webex Engage, as you cannot restore the asset after deleting it. Doing so would lead to asset deletion within Webex Connect alone while the entry continues to be in Webex Engage.