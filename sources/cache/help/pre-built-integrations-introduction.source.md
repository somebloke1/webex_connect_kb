<<prodname>> contains a growing list of prebuilt integrations created, tested, and maintained by expert teams for out of box functionality. Prebuilt integrations are available as nodes and events in the low-code-builder and include support for popular systems like CRM, payment service providers, etc., 

When a pre-built integration is enabled for your tenant, you can view it along with other pre-built integrations enabled for your tenant in the <<prodname>> portal. These integrations will be listed in the Integrations section of the portal. You can also view all the events and nodes associated with the available pre-built integrations.

## Types of Integration

- [Nodes](https://help.imiconnect.io/docs/introduction-1#nodes)
- [Inbound Events](https://help.imiconnect.io/docs/introduction-1#inbound-events)

## Getting Started

These integrations need to be enabled for your account and are not available by default. Please contact your account manager in case you wish to enable it for your account.

Upon enabling them, below are the steps to start using them:

To view a pre-built integration:

1. Login to the <<prodname>> portal.
2. Navigate to Assets → Integrations.
3. Use the filter to select Pre-built Integrations as Integration Type.  
   The list of all the pre-built integrations available for your tenant are displayed.
4. Select Manage/View under Actions for the integration you want to view.

## Authorization

To authorize a pre-built integration:

1. Navigate to Assets → Integrations.
2. Select Pre-built Integrations under Integration Type, to display the list of all pre-built integrations.  
   The integrations which are not yet authorized show the status as Pending Authorization.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d396211-image.png",
        null,
        "Screenshot displaying a list of pre-built integrations"
      ],
      "align": "center",
      "caption": "Screenshot displaying a list of pre-built integrations."
    }
  ]
}
[/block]


<br />

3. Click Actions → Manage associated with the integration you want to authorize.
4. On the Manage Integrations page, scroll down to the Node Authorizations section. This section lists all the authorizations mapped to this integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5222af4-image.png",
        null,
        "Screenshot of Node Authorizations."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node Authorizations"
    }
  ]
}
[/block]


5. Click **Action** → **Add Authorization** associated with the authorization, where Auth Type is oauth2 and Status is Authorization Pending.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e569f0a-Prebuilt_Integration.jpg",
        "Prebuilt Integration.jpg",
        "Screenshot of Adding New Authorization"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding New Authorization"
    }
  ]
}
[/block]


6. Enter all the required fields. The authorization configuration and the parameters/variables depend on the type of authorization.

7. Click Authorize.  
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

## Manage Integration

### Integration Details

You can view the integration's information, which includes the integration's Name, Description, Service, Flows, Rules, Tenant Identifier, and Validate Signature.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cc33fcd-image.png",
        null,
        "Screenshot of Manage Pre-built Integration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage Pre-built Integration Page"
    }
  ]
}
[/block]


### Nodes

#### Node Authorization

If an integration supports nodes, then the node authentication details can be accessed from this section. Please find the example mentioned below:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6201e9e-image.png",
        null,
        "Screenshot of Node Authorizations"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node Authorizations."
    }
  ]
}
[/block]


#### View Node List

If an integration supports nodes, you can view the node versions of a particular node by expanding the node.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1a77c88-image.png",
        null,
        "Screenshot of View Node List."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of View Node List"
    }
  ]
}
[/block]


> 📘 Note
> 
> Different node versions can have different authorizations configured. If multiple auth mechanism are added by admin for a node and the latest version of the node only requires one of the auth mechanisms, then even if you have authorized the latest auth, the status of the old auth mechanism will show as pending.

Persisting the field values for pre-built integration nodes

> 📘 
> 
> When the Authorization is changed, you will have to add a new Authorization. The previous relevant Authorization details will be retained in the new Authorization. 
> 
> If the node UI is directly calling an API for rendering the field values, the authorization details will not be retained.

### Inbound Events

#### Event Authorisation

If an integration supports events and has event authorisation enabled, then the authentication details can be accessed from this section. Please find the example mentioned below:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d1209c4-image.png",
        null,
        "Screenshot of Event Authorization"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Event Authorization"
    }
  ]
}
[/block]


#### View Event List

If an integration supports events, then you can view the event versions of a particular node.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/11ebeda-image.png",
        null,
        "Screenshot of View Event List."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of View Event List."
    }
  ]
}
[/block]


### Validating Signature while regenerating a Secret key for Prebuilt Integration

When signature validation is enabled for pre-built integration the platform user will be able to view that in enable state on manage integrations page. Creating and discarding a Secret Key is only allowed to the tenant owner and restricted for all other user roles.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7e161c6-image.png",
        null,
        "Screenshot of Manage Pre-built Integration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Manage Pre-built Integration Page."
    }
  ]
}
[/block]


<br />

> 📘 Note
> 
> We have launched a new Integrations Studio i.e., a portal for our partners to build & publish pre-built integrations for the Webex Connect platform. For the integrations built and published on the studio, the manage integrations page layout would be different. On the Node UI for the integrations, additional info would be provided.

The layout would be different for the following sections:

**Manage Integrations**: The change Logs section is newly introduced. It shows for integration enablement and subsequent version releases alongside the existing information on the Manage Integrations page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fe5405e-image.png",
        null,
        "Screenshot of Manage Integrations"
      ],
      "align": "center",
      "border": true,
      "caption": "Screen shot of Manage Integrations"
    }
  ]
}
[/block]


**Node Authorization and Node List**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/61ad9c3-image.png",
        null,
        "Screenshot of Node Authorization"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node Authorization"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6306eb8-image.png",
        null,
        "Screenshot of Node List"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node List"
    }
  ]
}
[/block]


**Event Authorization and Event List**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f8f5973-image.png",
        null,
        "Screenshot of Event Authorization"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Event Authorization"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0f3d754-image.png",
        null,
        "Screenshot of Event List"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Event List"
    }
  ]
}
[/block]


The additional information on Node UI includes change logs in manage integrations, support, a user guide, a privacy policy, the recommended version on the node configuration window, and a link to configure authentication from the flow builder.

**Node Configuration**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6bba58e-image.png",
        null,
        "Screenshot of Node Configuration"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node Configuration"
    }
  ]
}
[/block]


**Recommended Version**

This is the node's latest version, and we suggest using this node for building flows.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2d9164b-image.png",
        null,
        "Screenshot of Recommended Version"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Recommended Version"
    }
  ]
}
[/block]


## Live Integrations

Live integrations include the following nodes:

| Live Integrations                                                                                                        |
| :----------------------------------------------------------------------------------------------------------------------- |
| [Agile CRM](https://help.imiconnect.io/docs/agile-crm-1)                                                                 |
| [Salesforce](https://help.imiconnect.io/docs/salesforce-node-1)                                                          |
| [AI Agent Node](https://help.webexconnect.io/docs/ai-agent-node)                                                         |
| [Google Dialogflow CX](https://help.imiconnect.io/docs/google-dialogflow-1)                                              |
| [Google Dialogflow ES](https://help.imiconnect.io/docs/google-dialogflow)                                                |
| [ServiceNow Node](https://help.webexconnect.io/docs/servicenow-node)                                                     |
| [Customer Journey Data Node ](https://help.webexconnect.io/docs/customer-journey-data)                                   |
| [Zendesk](https://help.imiconnect.io/docs/zendesk-node-1)                                                                |
| [Freshdesk](https://help.webexconnect.io/docs/freshdesk-node-1)                                                          |
| [Zoho](https://help.imiconnect.io/docs/zoho-crm-1)                                                                       |
| [Link Shortener](https://help.webexconnect.io/docs/link-shortener)                                                       |
| [Epic](https://help.imiconnect.io/docs/epic)                                                                             |
| [Webex Chat/Webex Engage](https://help.webexconnect.io/docs/webex-chat-webex-engage)                                     |
| [Enghouse Integration-Deprecated](https://dash.readme.com/project/imiconnect1/v6.1.0/docs/webex-chatwebex-engage-1)      |
| [Webex Connect AppExchange App - Deprecated](https://help.imiconnect.io/docs/webex-connect-appexchange-app-deprecated)   |
| [Nice inContact - Deprecated](https://help.imiconnect.io/docs/nice-incontact-deprecated)                                 |
| [Cisco ECE Integration - Deprecated](https://help.imiconnect.io/docs/cisco-ece-integration-deprecated)                   |
| [Skype for Business Integration - Deprecated](https://help.imiconnect.io/docs/skype-for-business-integration-deprecated) |

## FAQ

## I want to use an Integration (Prebuilt/Custom/HTTP) node immediately after a Social Hour node. However, I'm experiencing failures such as HTTP 429 Status Code ("Too Many Requests") and my flow execution stops. What should I do?

The HTTP 429 "Too Many Requests" status code means that the downstream system configured in integration (Custom/HTTP/Prebuilt) node is receiving requests faster than it can process them. This often happens when a large number of requests are released simultaneously from a Delay Node, Social Hour Node, or Event Scheduler and sent to integration node.

To resolve this, we recommend to implement a retry mechanism in your flow. Introduce a loop around the Integration or HTTP node that retries the failed request three times before stopping. This approach helps smooth out request bursts and increases the chances of successful processing, even if the target system is temporarily overloaded. Note that this does not guarantee all requests will be accepted by the downstream system. 

**How to implement a retry:**

1. Add a loop around the Integration(Custom/HTTP/Prebuilt) node.
2. Set the loop to attempt the request up to three times before failing the transaction.
3. Include a delay between retries to avoid overwhelming the endpoint (for example: 60 seconds, 120 seconds, and 180 seconds).
4. Optionally, log failed transactions using Logbook or Flow Outcome for monitoring and troubleshooting.