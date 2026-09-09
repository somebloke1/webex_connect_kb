# Accessing Webex Connect

Source: https://help.webexconnect.io/docs/accessing-the-product
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:47+00:00

## Accessing the Product

To access Webex Connect, use the directions below.

- Enter your tenant URL in the browser address bar (e.g., [https://<tenantname>.<region>.webexconnect.io]). Refer to [Know Your API Endpoints](https://developers.webexconnect.io/reference/endpoints) for guidance on selecting the relevant API endpoint.
- Based on your tenant’s configuration, you will see one of the following login options:

  - Both Webex SSO and Webex Connect username and password-based login / Webex Connect SSO.

    

![Logging into Webex Connect](https://files.readme.io/5123ea5-SSO_User.png)


  - Only Webex Connect username and password based login / Webex Connect SSO.

    

![Logging to Webex Connect using Username and Password](https://files.readme.io/10c3b7d-User.png)


  - Only Webex SSO.

    

![Logging into Webex Connect using Webex Single Sign On (SSO)](https://files.readme.io/ba0408d-SSO.png)



> 📘 Note
> 
> The Login Using Webex SSO option is available only for users whose organization is linked with Control Hub and who have signed up for the Webex account.

- After you successfully log in, the dashboard appears with the Services tab in view as shown below.

### Session Timeout

For your security, Webex Connect automatically ends your session after a period of inactivity. If you do not interact with the platform for 30 minutes, you will be logged out and required to sign in again to continue your work. This helps protect your account and sensitive data from unauthorized access.

- The default session timeout is 30 minutes of inactivity.
- There is currently no warning notification before the session expires.
- After timeout, you will be redirected to the login page and prompted to sign in again.

If you are working on important tasks, be sure to save your progress regularly to avoid losing any unsaved changes when your session times out.

## Navigation

When you log into Webex Connect, you reach the Services page by default. You can start off by creating a new workspace or service, or you can move on to exploring other functionalities.



![Navigating Webex Connect](https://files.readme.io/3730aac-imiconnect_page.png)






![Navigating to various sections of Webex Connect](https://files.readme.io/5fad71d-1.jpg)




### Services

A service is a named workspace to manage a given customer interaction use case. Each service provides you with a unique service key that's needed for using Webex Connect communication APIs, event APIs, and inbound webhooks. Refer to the [Services Documentation](https://help.imiconnect.io/docs/introduction) for more information.

### Reports

The Reports section helps you view and analyze your messaging and flow traffic across various services. Webex Connect provides reporting at three levels - platform level summary, channel asset level summary, and service level summary. Refer to the [Reports Documentation](https://help.imiconnect.io/docs/service-reports) for more information.

### Assets

Assets is where you manage the numbers, apps (3rd party messaging platform connections), and integrations associated with your account. In the developer sandbox, you are not able to add new numbers or apps as these are preconfigured for you. Refer to the [Assets Documentation](https://help.imiconnect.io/docs/inbound-webhooks) for more information.

### Tools

As part of tools, you can access [Voice Media](https://help.imiconnect.io/docs/voice-media), [Voice Recordings](https://help.imiconnect.io/docs/voice-recordings), [Smart Links](https://help.imiconnect.io/docs/smart-links), [Templates](https://help.imiconnect.io/docs/templates), [Export Logs](https://help.webexconnect.io/docs/export-logs-overview), and [Media Manager](https://help.imiconnect.io/docs/media-manager).

### Debug

View transaction details and troubleshoot issues using a Transaction ID or a Destination ID or a date range. Refer to the [Debug Console Documentation](https://help.imiconnect.io/docs/console) for more information.

### Reports and Analytics

View and export reports for various services and assets within your account. Refer to the [Reports](https://help.imiconnect.io/docs/service-reports) section for more information.

### Help

View information on the product documentation, [Changelogs](https://help.imiconnect.io/changelog), [API Reference](https://developers.imiconnect.io/reference#apioverview), [Platform Documentation](https://help.imiconnect.io/docs), and the Knowledge Base.

### App Tray

View and access tools such as App Trays, [Bot Builder](https://help.imiconnect.io/docs/bot-builder), [Contact Policy](https://help.imiconnect.io/docs/contact-policy), and [Event Scheduler](https://help.imiconnect.io/docs/event-scheduler).

### Profile Settings

Navigate to change profile and tenant settings, switch groups or teams, contact support, view teammates, or view brands and campaigns.