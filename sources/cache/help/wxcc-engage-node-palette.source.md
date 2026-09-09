<<prodname>> offers the following nodes for <<WebexCC>> integration. The node authorization configuration details are available in the next section.

## Node and Methods

| Node Name                                        | Description                                                                                                                            | Methods              | Recommended Node Version |
| :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :------------------- | :----------------------- |
| [Search Conversation](doc:search-conversation)   | Calls Webex Engage Conversation Search API to search for an existing conversation using the customer identifier                        | Search Chat          | v1.0, v1.1, and v1.3     |
| [Append Message](doc:append-conversation)        | Calls Webex Engage Append Conversation API to append a message to an existing conversation                                             | Append Message       | v1.0, v1.3, and v1.4     |
| [Create Conversation](doc:create-conversation)   | Calls Webex Engage Create Conversation API to create a new conversation on Webex Engage with the channel and customer details          | Create Conversation  | v1.0, v1.2, and v1.3     |
| [Update  Conversation](doc:update-conversation)  | Calls Webex Engage Update Conversation API to update a new conversation on Webex Engage with the channel and customer details          | Update  Conversation | v1.0                     |
| [Add Participant](doc:add-participant)           | Calls Webex Engage API to add a participant to a conversation                                                                          | Add Participant      | v1.0                     |
| [Remove Participant](doc:remove-participant)     | Calls Webex Engage API to remove a participant from a conversation                                                                     | Remove Participant   | v1.0                     |
| [Close conversation](doc:close-conversation)     | Calls Webex Engage API to close the conversation                                                                                       | Close conversation   | v1.0                     |
| [Re-open Conversation](doc:re-open-conversation) | Calls Webex Engage Update Conversation API to Re-open and queue a conversation which is in closed state                                | Re-open Conversation | v1.0                     |
| [Business Hours](doc:business-hours)             | Calls Webex Engage's Business Hour API to validate point in time whether the business is in working hours, on a holiday or an override | Business Hours       | v1.0                     |

## Node Authorization

Client applications (in this case <<prodname>>) are required to provide a valid access token for using various <<WebexCC>> and imiengage APIs. The access token is generated using the authorization details configured within the ‘Node Runtime Authorization’ field that <<WebexCC>> users are required to provide during flow configuration. 

> 📘 Note
> 
> For all the Authorization that is being accessed by Webex Connect, if the authorizing credentials are updated in the integrating system, the Webex Connect will loose access to the integration and the users will have to re-authorize the node.
> 
> Example of Authorization Credentials are: Username, Password, Client ID, Client Secret Key, Access Key etc.

## Node Authorization for <<WebexCC>> Engage nodes

For Webex CC Engage nodes (Engage nodes are Search Conversation, Append Conversation, Create Conversation, Update Conversation, Add Participant, Remove Participant, Close Conversation, and Re-open Conversation), you’ll be asked to provide the following details on clicking **+ ADD NEW AUTHORIZATION **option:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d3d19cd-43b05b1-Wxcc_engage.jpeg",
        "",
        "Screenshot of Node Authorization for Webex CC Engage Nodes"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Node Authorization for Webex CC Engage Nodes"
    }
  ]
}
[/block]


Here’re a brief description of the details that you need to provide: 

- Authorization Name - A unique name for identifying this authorization. 

> 📘 
> 
> Please note that the above details are provided to the requestor during the tenant provisioning process.

Click **AUTHORIZE **after configuring the above details. You will be redirected to Cisco Webex CC user login, where you to provide the username and password to login. You will see the confirmation message that the authorization is successfully added on the successful authorization. 

Once you have successfully configured the authorization details for a node, you will be able to reuse it every time to use the same node. If you delete a node authorization, you will need to go and update the authorization configuration wherever you’d used the same node with the same authorization. 

## Node Outcomes

Nodes in <<prodname>> have one or more outcome edges (that can be used to configure transitions to the next logical node based on the requirements) corresponding to various success or error cases. Some of the standard node outcomes include:  

- onError – Request processing failed due to an error. 
- onInvalidData – Request processing failed due to missing data. 
- onInvalidChoice – Request processing failed but there is no outcome configured for the concerned scenario. 
- onTimeout – Request processing timed out. 
- onAuthorizationFailure – Request could not be processed due to authorization failure. 

Apart from the standard outcomes, each node may have one or more node-specific outcomes. Descriptions for those are given below.

## Webex Engage Streaming

The Webex Engage Streaming is used for sharing channel event payloads with Webex Engage. It is a machine-to-machine streaming and is pre-authorized.

### Prerequisites

Your tenant must be a Contact-Center-linked <<prodname>> tenant.

You must have access to the Webex Engage Prebuilt node. For more information, refer to [Webex Engage Nodes and Node Authorizations](https://help.imiconnect.io/docs/webex-engage-nodes-and-node-authorizations).

> 📘 Note
> 
> The Webex Engage Streaming data stream is a pre-authorized streaming. The streaming is enabled by default for all channel incoming events. The data stream by default streams incoming events of all channels to Webex Engage.

### Viewing and Editing Webex Engage Streaming Data Stream on <<prodname>> Tenant

To view or edit the Webex Engage Streaming Data Stream:

1. Login to the <<prodname>> platform.
2. Navigate to Assets > Integrations.
3. In the search bar, search for Webex Engage Streaming.  
   You will be able to view the services where the node was used as the last entry.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b5a687d-Integrations.png",
        "",
        "Screenshot of Integrations page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Integrations page."
    }
  ]
}
[/block]


4. Under **Actions**, click **Manage**.  
   In the **Manage Integration - Data Streams** page, under Data Streams, you should be able to view Webex Engage Streaming.
5. The default configuration for Webex Engage Streaming allows to stream data for all channels incoming events.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d13bbe8-Integrations1.png",
        "",
        "Screenshot of Default Webex Engage Streaming configuration."
      ],
      "align": "center",
      "border": true,
      "caption": "Default Webex Engage Streaming configuration"
    }
  ]
}
[/block]


6. Select one of the following for Assets:
   1. Enable by default for all assets - This is the default configuration for the streaming. It allows Webex Engage to receive streaming for all assets created in the tenant. We recommend keeping the configuration as is.
   2. Choose to enable at an asset level - Use this option if you want to enable the streaming at an asset-level. You can choose the streaming for each asset/app in the corresponding app configuration page. Below is a screenshot which shows the configuration for Apple Messages for Business. The other apps also have similar configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5521fa9-Integrations2.webp",
        "",
        "Screenshot of Apple Messages for Business Manage App Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Apple Messages for Business - Manage App Page"
    }
  ]
}
[/block]


7. Select the required channels under Channels. By default all the channels are selected, however optionally channels can be disabled from platform UI. This will disable the streaming service for un-selected channels. We recommend to have at least the Apple Business Messaging option selected for Webex Engage streaming. 
8. **Incoming events & Messages** is selected by default for **Events**. 

> 📘 Note
> 
> The streaming only supports Incoming events & Messages. Do not disable this option.

9. Click **Save**.