<<prodname>> offers the following Task nodes for Contact Center Enterprise (CCE) integration. The node authorization configuration details are available in the next section.

## Node and Methods

[block:parameters]
{
  "data": {
    "h-0": "Node Name",
    "h-1": "Description",
    "h-2": "Methods",
    "h-3": "Recommended Node Version",
    "0-0": "[Create Task](https://help.imiconnect.io/docs/create-task-1)",
    "0-1": "Calls Contact Center Enterprise (CCE) Task API to Create a new Task at Contact Center Enterprise using a unique identifier",
    "0-2": "Create Task",
    "0-3": "v1.2",
    "1-0": "[Get Task Details (Task Node)](https://help.imiconnect.io/docs/get-task-details) ]",
    "1-1": "",
    "1-2": "",
    "1-3": "",
    "2-0": "[End Task](https://help.imiconnect.io/docs/close-task-1)",
    "2-1": "Calls Contact Center Enterprise (CCE) Task API to close task directly on Contact Center Enterprise",
    "2-2": "Closed Task on Contact Center Enterprise",
    "2-3": "v1.0",
    "3-0": "",
    "3-1": "Calls Contact Center Enterprise  \n Task API to notify Contact Center Enterprise on close task accept",
    "3-2": "Close Task Accept",
    "3-3": "v1.0",
    "4-0": "",
    "4-1": "Calls Contact Center Enterprise Task API to notify Contact Center Enterprise on close task reject",
    "4-2": "Close Task Reject",
    "4-3": "v1.0"
  },
  "cols": 4,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## Node Authorization

Client applications (in this case <<prodname>>) are required to provide a valid access token for using various Cisco Contact Center Enterprise and Webex Engage APIs. The access token is generated using the authorization details configured within the ‘Node Runtime Authorization’ field that Cisco Contact Center Enterprise users are required to provide during flow configuration. 

## Node Authorization for Cisco Contact Center Enterprise Task nodes

For Cisco Contact Center Enterprise Task nodes (Task nodes are Create Task, End Task, and Get Task Details).

To authorize a pre-built integration:

1. Go to Assets > Integrations.
2. Select Pre-built Integrations under Integration Type, to display the list of all pre-built integrations.  
   The integrations which are not yet authorized show the status as Pending Authorization.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cf44793-WebexCCE_Authorized.PNG",
        "WebexCCE_Authorized.PNG",
        "Screenshot of Integrations page showing pre-built integrations with pending authorization status."
      ],
      "align": "center",
      "border": true,
      "caption": "Viewing pre-built integrations pending authorization."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/46839cf-WebexCCE_Auth_Pending_2.PNG",
        "WebexCCE_Auth_Pending_2.PNG",
        "Screenshot of Integrations page showing pre-built integrations with pending authorization status."
      ],
      "align": "center",
      "border": true,
      "caption": "Viewing pre-built integrations pending authorization."
    }
  ]
}
[/block]


3. Click Actions → Manage associated with the integration you want to authorize.
4. On the Manage Integrations page, scroll down to the Node Authorizations section. This section lists all the authorizations mapped to this integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ceb78ab-Prebuild_Integration_Manage_Integration.PNG",
        "Prebuild_Integration_Manage_Integration.PNG",
        "Screenshot of Manage Integrations page with Node Authorizations section displaying mapped authorizations for the integration."
      ],
      "align": "center",
      "border": true,
      "caption": " Viewing node authorizations for the integration."
    }
  ]
}
[/block]


> 📘 Note
> 
> If the integration nodes have no auth required, then it is not shown in the list.

5. Click Action → Add Authorization associated with the authorization, where Auth Type is oauth2 and Status is Authorization Pending.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0ca30e3-wxcc_1.jpg",
        "wxcc_1.jpg",
        "Screenshot of Adding OAuth2 authorization."
      ],
      "align": "center",
      "border": true,
      "caption": "Adding OAuth2 authorization."
    }
  ]
}
[/block]


6. Enter the Authorization Name
7. Click Authorize.  
   A pop-up appears. 
8. Enter your Cisco email address and click **Sign in**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a15ce6c-wxcc_sso.jpg",
        "wxcc_sso.jpg",
        "Pop-up window prompting user to enter Cisco email address and click Sign in for authorization."
      ],
      "align": "center",
      "border": true,
      "caption": "Authorizing integration with Cisco account."
    }
  ]
}
[/block]


The status of the authorization will change to Authorized and all the nodes under this authorization are authorized and ready for use.  
Once authorized, you can perform the following actions on the authorization.

- View - allows you to view the authorization.
- Update - allows you to update the authorization details.
- Make it as default - allows you to make a particular authorization default for that node.
- Remove - allows you to delete the authorization.

> 📘 Note
> 
> If an OAuth 2.0 type authorization is edited in the Admin portal, you will be prompted to re-authorize the authorization.

You are not allowed to delete the authorization if it is mapped/used in flow assets.