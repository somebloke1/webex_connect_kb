After you provision your Livechat channel asset on Webex Connect, you must register it with WxEngage to use it for your business’s contact center use case. WxEngage will require a Connect service to deliver outbound messages from your contact center. Therefore, you must create a service to register this Livechat asset with Engage. Refer to the procedure for [creating a WxConnect service](https://help.webexconnect.io/docs/create-a-service-on-imiconnect).

At the endof this provisioning step, WxEngage will provide you with an installation script that must be embedded into your website's code. Additionally, you will need to whitelist your website's domain in the Admin console. If you do not have a website yet or want to experiment with this on a test page, we recommend using [glitch.com](https://www.glitch.com) to try out the Livechat widget.

## Register Livechat asset

To register your Livechat asset with WxEngage, follow the below steps:

1. Navigate to Assets > Apps.
2. Click the Livechat channel asset you’d like to register from the Apps column.  
   The following screen appears.

   [block:image]{"images":[{"image":["https://files.readme.io/1528cb8bf16711f89ded3d3ff3c3bd9f62624c806e7bf40b8f344d2f75f88c83-image.png",null,"Screenshot of Configuring New Mobile & Web App Page "],"align":"center","border":true,"caption":"Screenshot of Configuring New Mobile & Web App Page "}]}[/block]
3. Click **Register to Webex Engage**.  
   The following pop-up window appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/19c168cc1c7deee1383390dc90bc2b5eb1688b4406f68df09a7e50df0a23e7af-image.png",
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

- Your channel asset will be linked to the Default Team on WxEngage by default. Suppose you want to change this setting or share the asset with multiple teams to facilitate transfers or enable agent-initiated outbound communications from different teams. In that case, you can manage these configurations in your Engage tenant's Admin console. For more information, refer to [managing your assets in Engage](https://docs.imi.chat/docs/livechat-channel).
- After viewing the success toast message on WxConnect, you can log in to your WxEngage tenant to confirm that your Livechat channel asset has been synced. Then, you can continue with further contact center configurations from the WxEngage Admin console (Admin console > Assets > Channel assets > Livechat (Tab) and click the Edit icon.).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d84a1bc88822b48af3cf699e9a9663348f1b5dd41c7f6b18f734b79cb31eaa82-image.png",
        null,
        "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped Mobile/Web Asset."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped Mobile/ Web Asset."
    }
  ]
}
[/block]


## **Configure Livechat widget**

In addition to registering Livechat assets on Webex Connect, you must whitelist your website’s domain on WxEngage.

To configure a Livechat widget, follow these steps:

1. Log in to Webex Engage as an Administrator.
2. Navigate to Assets > Channel assets > Livechat (Tab) and click **Edit **icon of the asset you just created.
3. Navigate to the **Websites **tab.
4. Click **Add website** on the top-right corner of the screen. 
5. Enter the mandatory fields as necessary.
6. In the **General settings** tab, ensure you configure your website’s domain without http (or) https\:// prefixes.  
   Example: \*.acme.com.
7. Configure the First message that you’d like your end customers to see on the Livechat widget. You will also need to use this subsequently when you configure your Connect flow to route messages.
8. Click Save changes.

You can refer to the Livechat website configuration guide to further customize the widget’s behavior on your website.

## **Deploy the widget on your website**

To deploy a widget on your website, follow these steps:

1. Log in to Webex Engage as the Administrator.
2. Navigate to Assets > Channel assets > Livechat (Tab) and click the **Edit** icon of the asset you just created.
3. Navigate to the **Installation** tab.
4. Click **Copy**.
5. Paste the code snippet before the closing tag in your website's HTML page and deploy  
   Voila! 

You should now see the Livechat widget appear on your website. Click the Launcher in the bottom-right corner to expand the Livechat widget.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c2a33a0772a2593399d24f8a23e56f5dc845c34593f2d1ea770dcead2e763f53-image.png",
        null,
        "Screenshot displaying the Livechat widget on the website."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Livechat widget on the website"
    }
  ]
}
[/block]


> 📘 Warning
> 
> - You cannot change the service mapping after successfully establishing it. Therefore, asset registration on Webex Engage should happen only after deciding on the service to be used.
> - Do not delete a Livechat asset after registering with Webex Engage, as you cannot restore the asset after deleting it. Doing so would lead to asset deletion within Webex Connect alone while the entry continues to be in Webex Engage.