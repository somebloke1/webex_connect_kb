You are required to have access to a long code or a short code for receiving incoming messages from customers and sending responses to their messages. Number provisioning requests need to be sent to your Partner Success Manager(PSM) or Customer Success Manager(CSM). For Gold/Partner tenants, requests should be sent to the PSM team and, for Customer tenants, requests should be sent to CSM. Contact information is available on the Contact Support page within your <<prodname>>tenant.

Once a number has been provisioned to your tenant, it is visible under 'Assets -> Numbers' screen.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/52ea3a2-1.jpg",
        null,
        "Screenshot of Number Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Number Page."
    }
  ]
}
[/block]


Once a number has been provisioned to your <<prodname>> tenant for supporting SMS as a channel for customer service, you would need to register it on Cisco Webex Contact Center to complete the asset configuration process.

## Registering your <<prodname>> Phone Number with Webex Contact Center

1. Navigate to **Assets** -> **Numbers**.
2. Select **Phone Number** from the Number Type.
3. Select the required **Phone Number** which you want to register with Cisco Webex Contact Center.
4. Click **Manage**.  
   The **Manage Phone Number** page displays.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/daf1f62-2.jpg",
        null,
        "Screenshot of Manage Phone Number Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage Phone Number Page."
    }
  ]
}
[/block]


5. Click **Register to Webex Engage**.

   [block:image]{"images":[{"image":["https://files.readme.io/3b2d50d-3.jpg","SMS3.jpg","Screenshot of Register to Webex Engage."],"align":"center","sizing":"400px","border":true,"caption":"Screenshot of Register to Webex Engage."}]}[/block]
6. Select the required service (Note: This should be the <<prodname>> service that would be used for configuring SMS flows for Webex Contact Center) and click **Register**. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/deaabde-3.jpg",
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
        "https://files.readme.io/1c32a46-4.jpg",
        null,
        "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number"
    }
  ]
}
[/block]


As shown above, you will see a <<WebexCC>> icon and a PCI check enabled flag next to the number once it's been successfully mapped with Webex Contact Center.

> ❗️ 
> 
> 1. Please note, the service mapping cannot be changed once done. Hence, the asset registration on Webex Contact Center should be done after the service to be used has been decided.
> 
> 2. Do not release a number that you are using for providing customer support over SMS as a channel as it will cause disruptions to live services. Released numbers are delinked from your <<prodname>> and cannot be restored.

> 📘 Entrypoint Configuration
> 
> Once the asset is registered on <<prodname>>, the entry point mapping should be done on the Cisco Webex Contact Center portal as well.