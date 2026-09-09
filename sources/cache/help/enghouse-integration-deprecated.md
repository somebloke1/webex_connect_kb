# Enghouse Integration-Deprecated

Source: https://help.webexconnect.io/docs/enghouse-integration-deprecated
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:11+00:00

> 📘 Deprecation Alert
> 
> Please note that this integration has been deprecated and is no longer available. This doesn't impact any of your existing live services however the integration won't be available for newer Webex Connect tenants.

The integration enables Enghouse to support chat with their end customers on multiple channels (Example: Facebook Messenger, Real-Time Messaging) along with their own primary channel like web chat.

With Enghouse integration with Webex Connect, Enghouse chat agents will be able to receive messages from multiple channels using the same interface. 

**Note: You have to source Enghouse connection parameters to configure in Webex Connect, which are specific to a customer.**



![Screenshot of Enghouse Integration](https://files.readme.io/2c0f40d-Enghouse.png)




## Configure Enghouse

1. Log on to Webex Connect with your credentials.
2. On the left navigation bar, click ASSETS > **INTEGRATIONS**. 
3. Click **ADD INTEGRATION** > **Enghouse** to add new integration. 
4. Enter the connection parameters and save the details.



| Parameter | Description |
| --- | --- |
| NAME | Name of the Enghouse integration on Webex Connect. |
| **Configuration** | Parameters required to configure  Enghouse on Webex Connect |
| CALL CENTER ADDRESS | Call center address to route the incoming messages.  <br>E.g: webchat.ngcc.bt.com |
| CALL CENTER PORT | Port address of the call center. |
| TENANT ID | Unique Tenant ID provided by Enghouse. |
| APPLICATION ID |  |
| SERVER URL | Server URL of the hosted tenant.  <br>E.g: demotrial3 |
| API VERSION | API version in use to access Enghouse. |
| ACCOUNT ID | Account ID provided by Enghouse. |
| **Saved replies** | Message configured for automated replies. |
| WELCOME MESSAGE | The welcome message for first time user. |
| GOODBYE MESSAGE | Message displayed when a user end the chat conversation. |
| **System replies** | Codes send to users when error occurs while replying to message. |
| STATUS CODE |  |
| ERROR CODE |  |
| REPLY MESSAGE |  |
| **+ ADD MORE** |  |




_Note: This integration is available only in the cloud version of Webex Connect._