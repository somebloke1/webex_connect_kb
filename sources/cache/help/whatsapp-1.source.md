After you provision your WhatsApp longcode on Webex Connect, you must register it with WxEngage to use it for your business’s contact center use case. In addition, Webex Engage requires a Connect service to deliver outbound messages from your contact center, so kindly ensure you have created a service to register WhatsApp Business Longcode with Engage. Refer to the procedure for [creating a WxConnect service](https://help.webexconnect.io/docs/create-a-service-on-imiconnect).

To register your WhatsApp Business Longcode with WxEngage, follow the below steps:

1. Navigate to Assets > Numbers.
2. Click the WhatsApp channel asset you’d like to register from the Apps column.  
   The following screen appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f931b18b018575a575beff74bd98090a0bce3985a61217c9ba70253e6adad759-image.png",
        null,
        "Screenshot of Managing the WhatsApp Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Managing the WhatsApp Page"
    }
  ]
}
[/block]


3. Click **Register to Webex Engage** on the top-right corner of the screen.

The following pop-up window appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f6d7aa344febbeb3054a4c2377472e774526977d4abd8a8a694f3c1e0dab121f-image.png",
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


4. Choose the Service that you created in the pre-requisite step from the **Select Service** drop-down and click **Register**.

- Your channel asset will be linked to the Default Team on WxEngage by default. Suppose you want to change this setting or share the asset with multiple teams to facilitate transfers or enable agent-initiated outbound communications from different teams. In that case, you can manage these configurations in your Engage tenant's Admin console. 
- Once the number is mapped with the Webex Contact Center, you will view a Webex Contact Center (TBC) icon and a PCI check enabled flag next to the number.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fe6c13c5418bdf23fb4ee85952c513837c4b3e1d0c9d78ed549593d8799e1765-image.png",
        null,
        "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number."
    }
  ]
}
[/block]


> 📘 Warning
> 
> - You cannot change the service mapping after successfully establishing it. Therefore, asset registration on Webex Engage should happen only after deciding on the service to be used.
> - Do not release a number you are using to provide customer support over WhatsApp as a channel, as it will cause disruptions to live services. Released numbers are delinked from your Webex Connect and cannot be restored.