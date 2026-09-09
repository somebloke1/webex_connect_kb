## Prerequisites

- The redirection or Access Token URLs need to be configured in the Unified Contact Center Enterprise Management portal under the Digital Channel Settings, before activating the Authorizations on the <<prodname>> Tenant. This will ensure that the inbound webhook authorization functions correctly.

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

1. Login to <<prodname>> tenant using your login credentials.
2. Click **Assets** > **Integrations**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/740b258-CCE_Services_Integration.PNG",
        "CCE_Services_Integration.PNG",
        "Screenshot showing the user interface with the highlighted path: Assets menu expanded to reveal the Integrations option."
      ],
      "align": "center",
      "border": true,
      "caption": "Navigating to the Integrations section under Assets."
    }
  ]
}
[/block]


   The Integrations listing page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7c72071-CCE_Integrations_Page.PNG",
        "CCE_Integrations_Page.PNG",
        "Screenshot of the Integrations listing page, displaying a list of available integrations."
      ],
      "align": "center",
      "border": true,
      "caption": "View of the Integrations listing page."
    }
  ]
}
[/block]


3. Search for the pre-built integration that you have configured. The integration is displayed.

4. In the **Actions** drop-down menu, click **Manage**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0400eab-CCE_Integrations_Manage.PNG",
        "CCE_Integrations_Manage.PNG",
        "Screenshot showing the Actions drop-down menu opened with the Manage option highlighted, allowing users to manage selected integrations."
      ],
      "align": "center",
      "border": true,
      "caption": "Accessing the Manage option from the Actions drop-down menu."
    }
  ]
}
[/block]


5. In the **Manage Integration - Prebuilt Integration** page, click the **Activate** button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7e0de41-CC_Activate.PNG",
        "CC_Activate.PNG",
        "Screenshot of the Manage Integration - Prebuilt Integration page with the Activate button highlighted, enabling the activation of the selected integration."
      ],
      "align": "center",
      "border": true,
      "caption": "Activating a prebuilt integration from the Manage Integration page."
    }
  ]
}
[/block]


The activation success message is displayed, and the status is changed to **Activated**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8e7805f-CCE_Authorization_successful.PNG",
        "CCE_Authorization_successful.PNG",
        "Screenshot showing the activation success message displayed on the Manage Integration page, with the integration status updated to Activated."
      ],
      "align": "center",
      "border": true,
      "caption": "Integration successfully activated."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/22f3531-CCE_Activated.PNG",
        "CCE_Activated.PNG",
        "Screenshot highlighting the section displaying the Client ID and Client Secret."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot highlighting the section displaying the Client ID and Client Secret."
    }
  ]
}
[/block]


6. Copy your **Client ID** and **Client Secret** and save it on your system for reference.

The same credentials used in step 6 are to be used at the Contact Centre Enterprise side in ‘Unified Contact Center Enterprise Management’ for configuring OAuth 2.0 to post async events to <<prodname>>.