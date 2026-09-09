# SMS - CCE

Source: https://help.webexconnect.io/docs/cce-sms
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:19+00:00

You are required to have access to a long code or a short code for receiving incoming messages from customers and sending responses to their messages. Please contact your Webex Connect account manager for number provisioning requests.

Once a number has been provisioned to your tenant, it is visible under 'Assets -> Numbers' screen.

Once a number has been provisioned to your Webex Connect tenant for supporting SMS as a channel for customer service, you would need to register it on Cisco Contact Center Enterprise (CCE) to complete the asset configuration process. 

## Registering your Webex Connect Phone Number with Webex Engage

1. Go to **Assets** -> **Numbers**.
2. Select **Phone Number** from the Number Type.
3. Select the required **Phone Number** which you want to register with Webex Engage.
4. Click **Manage**.
5. The **Manage Phone Number** page displays.



![Screenshot of Manage Phone Number Page](https://files.readme.io/751110b-1.jpg)






![Screenshot of Register to Webex Engage](https://files.readme.io/b506999-2.jpg)




6. Click **Register to Webex Engage**.
7. Select the required service (Note: This should be the Webex Connect service that would be used for configuring SMS flows for Cisco Contact Center Enterprise integration and click Register.)



![Screenshot of registering the asset successfully with Webex Engage](https://files.readme.io/e50c831-3.jpg)




A message displays “Asset registered successfully”. This completes the asset registration for Cisco Contact Center Enterprise integration.



![Screenshot displaying the Webex Engage icon and PCI check enabled flag next to a mapped number.](https://files.readme.io/99b301f-4.jpg)




As shown above, you will see a Webex Engage icon and a PCI check enabled flag next to the number once it's been successfully mapped with Contact Center Enterprise.

> ❗️ 
> 
> 1. Please note, the service mapping cannot be changed once done. Hence, the asset registration on Webex Engage should be done after the service to be used has been decided.
> 
> 2. Do not release a number that you are using for providing customer support over SMS as a channel as it will cause disruptions to live services. Released numbers are delinked from your Webex Connect and cannot be restored.