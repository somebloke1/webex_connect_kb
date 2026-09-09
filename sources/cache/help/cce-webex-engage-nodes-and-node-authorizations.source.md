<<prodname>> offers the following Webex Engage nodes for Cisco Contact Center Enterprise integration. The node authorization configuration details are available in the next section.

## Node and Methods

| Node Name                                        | Description                                                                                                                | Methods              | Recommended Node Version |
| :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------- | :----------------------- |
| [Search Conversation](doc:search-conversation)   | Calls Webex Engage Conversation Search API to search for an existing conversation using the customer identifier            | Search Conversation  | v1.1                     |
| [Append Message](doc:append-conversation)        | Calls Webex Engage Append Conversation API to append a message to an existing conversation                                 | Append Message       | v1.0 and v1.3            |
| [Create Conversation](doc:create-conversation)   | Calls Webex Engage Create Conversation API to create a new conversation on imiengage with the channel and customer details | Create Conversation  | v1.0 and v1.2            |
| [Update  Conversation](doc:update-conversation)  | Calls Webex Engage Update Conversation API to update a new conversation on imiengage with the channel and customer details | Update  Conversation | v1.0                     |
| [Add Participant](doc:add-participant)           | Calls Webex Engage API to add a participant to a conversation                                                              | Add Participant      | v1.0                     |
| [Remove Participant](doc:remove-participant)     | Calls Webex Engage API to remove a participant from a conversation                                                         | Remove Participant   | v1.0                     |
| [Close conversation](doc:close-conversation)     | Calls Webex Engage API to close the conversation                                                                           | Close conversation   | v1.0                     |
| [Re-open Conversation](doc:re-open-conversation) | Calls Webex Engage Update Conversation API to Re-open and queue a conversation which is in closed state                    | Re-open Conversation | v1.0                     |
| Business Hours                                   | Calls Webex Engage Business Hours API to check the agents availability during business hours.                              | Business Hours       | v1.0                     |

## Node Authorization

Client applications (in this case <<prodname>> ) are required to provide a valid access token for using various Webex Engage APIs. The access token is generated using the authorization details configured within the ‘Node Runtime Authorization’ field that Cisco Contact Center Enterprise users are required to provide during flow configuration. 

## Node Authorization for Webex Engage nodes

Webex Engage nodes (Search Conversation, Create Conversation, Append Conversation, Re-open Conversation, Add Participant, Remove Participant, Close Conversation).

To authorize a pre-built integration:

1. Go to Assets > Integrations.
2. Select Pre-built Integrations under Integration Type, to display the list of all pre-built integrations.  
   The integrations which are not yet authorized show the status as Pending Authorization.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/58dc375-WebexCCE_Engage_Authorized.PNG",
        "WebexCCE_Engage_Authorized.PNG",
        "Page showing a list of prebuilt integrations available for selection and configuration."
      ],
      "align": "center",
      "border": true,
      "caption": "List of Prebuilt Integrations."
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
        "https://files.readme.io/54f3a49-Prebuild_Integration_Manage_Integration.PNG",
        "Prebuild_Integration_Manage_Integration.PNG",
        "Screenshot of Manage Integrations page with Node Authorizations section displaying mapped authorizations for the integration."
      ],
      "align": "center",
      "border": true,
      "caption": "Viewing node authorizations for the integration."
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