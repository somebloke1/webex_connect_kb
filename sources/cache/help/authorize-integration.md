# Authorize Integration - WxEngage standalone

Source: https://help.webexconnect.io/docs/authorize-integration
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:29+00:00

Webex Engage’s Integration services are provided as Nodes within Webex Connect’s Flow Builder. You must authorize the integration before using these nodes to design your contact center journey. Webex Engage uses the OAuth 2.0 - Client Credentials Grant type for this authorization process. 

To complete the authorize the nodes, follow these steps:

1. Navigate to Assets > Integrations.
2. Choose **Pre-built Integrations** from the **Integration Type** drop-down list, to display the list of all Pre-built Integrations.



![Screenshot displaying the selection of Pre-built Integrations from the Integration Type drop-down list](https://files.readme.io/25a021c46388e1acb035fbc6578fd30cd2ac5f776c7f9ccbf9ab46b39cc18c4d-image.png)




Check for the Webex Engage Live Agent. The integration status will display as **Auth Pending** if you have not authorized it.



![Screenshot displaying the option to select the Manage Integrations page](https://files.readme.io/cd777712186b6f0f6445fe38d483c7056e7f719083599b89c32589b4db2ed6d8-image.png)




On the Manage Integrations page, navigate to the Node Authorizations section. You can view the list of Authorizations mapped to this integration.



![Screenshot displaying to Add authentication](https://files.readme.io/45085ce88bee41544087f627f1de0a0f174638a9f1fc73b7d411f7bb01361289-image.png)




3. Click **Action**.
4. Click **Add **authentication and enter an **Authentication Name.**
5. Click **Authenticate**.

A success message appears on the screen.

** Managing node authorisations Centrally**

If you have added multiple authentications, you can mark one as default by choosing Mark as default from the Actions drop-down list. Unless explicitly modified, it will ensure that these Auth credentials apply for all instances of Webex Engage Nodes within the tenant.

Once marked as default, you will view a Default tag adjacent to the Auth Name.