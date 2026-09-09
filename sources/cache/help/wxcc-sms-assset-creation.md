# SMS - WXCC

Source: https://help.webexconnect.io/docs/wxcc-sms-assset-creation
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:12+00:00

You are required to have access to a long code or a short code for receiving incoming messages from customers and sending responses to their messages. Number provisioning requests need to be sent to your Partner Success Manager(PSM) or Customer Success Manager(CSM). For Gold/Partner tenants, requests should be sent to the PSM team and, for Customer tenants, requests should be sent to CSM. Contact information is available on the Contact Support page within your Webex Connecttenant.

Once a number has been provisioned to your tenant, it is visible under 'Assets -> Numbers' screen.



![Screenshot of Number Page.](https://files.readme.io/52ea3a2-1.jpg)




Once a number has been provisioned to your Webex Connect tenant for supporting SMS as a channel for customer service, you would need to register it on Cisco Webex Contact Center to complete the asset configuration process.

## Registering your Webex Connect Phone Number with Webex Contact Center

1. Navigate to **Assets** -> **Numbers**.
2. Select **Phone Number** from the Number Type.
3. Select the required **Phone Number** which you want to register with Cisco Webex Contact Center.
4. Click **Manage**.  
   The **Manage Phone Number** page displays.



![Screenshot of Manage Phone Number Page.](https://files.readme.io/daf1f62-2.jpg)




5. Click **Register to Webex Engage**.

   

![Screenshot of Register to Webex Engage.](https://files.readme.io/3b2d50d-3.jpg)


6. Select the required service (Note: This should be the Webex Connect service that would be used for configuring SMS flows for Webex Contact Center) and click **Register**. 



![Screenshot of registering the asset successfully with Webex Engage.](https://files.readme.io/deaabde-3.jpg)




A message displays “Asset registered successfully”. This completes the asset registration for Webex Contact Center.



![Screenshot displaying the Webex Contact Center icon and PCI check enabled flag next to a mapped number](https://files.readme.io/1c32a46-4.jpg)




As shown above, you will see a Cisco Webex Contact Center icon and a PCI check enabled flag next to the number once it's been successfully mapped with Webex Contact Center.

> ❗️ 
> 
> 1. Please note, the service mapping cannot be changed once done. Hence, the asset registration on Webex Contact Center should be done after the service to be used has been decided.
> 
> 2. Do not release a number that you are using for providing customer support over SMS as a channel as it will cause disruptions to live services. Released numbers are delinked from your Webex Connect and cannot be restored.

> 📘 Entrypoint Configuration
> 
> Once the asset is registered on Webex Connect, the entry point mapping should be done on the Cisco Webex Contact Center portal as well.