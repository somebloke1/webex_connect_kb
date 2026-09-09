# Event Authorization - CCE

Source: https://help.webexconnect.io/docs/cce-event-authorization
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:22+00:00

## Prerequisites

- The redirection or Access Token URLs need to be configured in the Unified Contact Center Enterprise Management portal under the Digital Channel Settings, before activating the Authorizations on the Webex Connect Tenant. This will ensure that the inbound webhook authorization functions correctly.

| Access Token URLs                                                                      | Regions     |
| :------------------------------------------------------------------------------------- | :---------- |
| <https://keycloak-authservice.imiconnect.eu/auth/realms/imiconnect_ln_prod/token>      | London      |
| <https://keycloak-authservice.imiconnect.com.au/auth/realms/imiconnect_syd_prod/token> | Sydney      |
| <https://keycloak-authservice.imiconnect.ca/auth/realms/imiconnect_cn_prod/token>      | Canada      |
| <https://keycloak-authservice-us.imiconnect.io/auth/realms/imiconnect_us_prod/token>   | Oregon (US) |
| <https://keycloak-authservice.imiconnect.io/auth/realms/imiconnect_uk_prod/token>      | Ireland     |
| <https://keycloak-authservice.imiconnect.in/auth/realms/imiconnect_ind_prod/token>     | Mumbai      |
| <https://keycloak-authservice.sg.webexconnect.io/auth/realms/imiconnect_sg_prod/token> | Singapore   |

- For more information on configuration details, refer to [Unified Contact Center Enterprise Management (UCCE) Documentation Portal](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html).

## Activating Authorizations at the Webex Connect Tenant

1. Login to Webex Connect tenant using your login credentials.
2. Click **Assets** > **Integrations**.



![Navigating to the Integrations section under Assets.](https://files.readme.io/740b258-CCE_Services_Integration.PNG)




   The Integrations listing page is displayed.



![View of the Integrations listing page.](https://files.readme.io/7c72071-CCE_Integrations_Page.PNG)




3. Search for the pre-built integration that you have configured. The integration is displayed.

4. In the **Actions** drop-down menu, click **Manage**.



![Accessing the Manage option from the Actions drop-down menu.](https://files.readme.io/0400eab-CCE_Integrations_Manage.PNG)




5. In the **Manage Integration - Prebuilt Integration** page, click the **Activate** button.



![Activating a prebuilt integration from the Manage Integration page.](https://files.readme.io/7e0de41-CC_Activate.PNG)




The activation success message is displayed, and the status is changed to **Activated**.



![Integration successfully activated.](https://files.readme.io/8e7805f-CCE_Authorization_successful.PNG)






![Screenshot highlighting the section displaying the Client ID and Client Secret.](https://files.readme.io/22f3531-CCE_Activated.PNG)




6. Copy your **Client ID** and **Client Secret** and save it on your system for reference.

The same credentials used in step 6 are to be used at the Contact Centre Enterprise side in ‘Unified Contact Center Enterprise Management’ for configuring OAuth 2.0 to post async events to Webex Connect.