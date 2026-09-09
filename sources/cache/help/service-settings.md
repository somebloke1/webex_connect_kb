# Locking, Deleting, and Other Settings

Source: https://help.webexconnect.io/docs/service-settings
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:51+00:00

You can perform the following tasks under the **Service Settings** section:

a. **Change/update the name and description** for your service  
b. **Lock the service** to prevent other users from making any changes to the service (e.g. flow, rules, etc.), if required.  A locked service does not allow other users, apart from the owner, to make any changes to the service. Other users can view the locked services in a read-only mode.

> 📘 SMS Routes
> 
> When you send outbound message requests to the Webex Connect platform, we send it to the destination device through pre-configured SMS routes to ensure optimal delivery performance and latency.
> 
> Every Webex Connect tenant has an SMS route configured based on various parameters. If a custom route has been configured for your tenant based on specific requirements, you will see an SMS Route dropdown option to select the preferred SMS route for the SMS traffic, sent via the concerned Webex ConnectService. Please reach out to your account manager if you have any custom routing requirements.



![Service Settings](https://files.readme.io/017653a-Locking_n_Deleting.jpg)




> 📘 Note
> 
> If Branded text is enabled for your client, the '**Fallback Wait Time**' appears on the **Service Settings** page. To enable Branded text for your number, please refer to the [Branded Text](https://help.webexconnect.io/docs/rcs-branded-text) page for more information.



![Fallback Wait Time when Branded Text is Enabled](https://files.readme.io/99a9fb417d07a5ebaca1256a8bfa8cac1abd1dbdd5f94f09f8b715dc0a89029a-image-20250723-110826.png)




The fallback wait time field defines how long a request should wait before it falls back to SMS, and you can configure it for each service level. The minimum fallback wait time is 20 seconds, the maximum fallback wait time is 60 minutes, and the default fallback wait time is 60 seconds.  
If you send an SMS request with an expiry, and if the current time plus 20 seconds (minimum fallback time) is greater than or equal to the expiry, the system sends Branded Text. Otherwise, the system initiates a fallback.

c. **Delete the service** if it's no longer needed. Once deleted, a service cannot be restored. Full access users are advised to lock their services to prevent accidental deletion by other users. When you delete a service, you are prompted to enter the password. If you are logged in with Webex SSO, enter the text **Confirm** to delete the service.



![Screenshot of Delete Service pop-up](https://files.readme.io/30509f4-delete_a_service.png)




> ❗️ Service Deletion
> 
> When you delete a service, all the reports and flows associated with that service are lost forever and cannot be restored. It will adversely impact the functioning of any integrated systems or apps that use the service key/JSON Web Tokens of this service for sending/receiving messages or calls.