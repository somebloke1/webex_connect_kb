# Webex CC Task Integration Nodes and Node Authorizations

Source: https://help.webexconnect.io/docs/wxcc-task-integration-nodes-and-node-authorizations
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:14+00:00

Webex Connect offers the following nodes for Cisco Webex Contact Center integration. The node authorization configuration details are available in the next section.

## Node and Methods

| Node Name                                                                    | Description                                                                                                                                                            | When to use                                                                                                                                         | Methods              | Recommended Node Version   |
| :--------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- | :------------------------- |
| [Create Task](https://help.webexconnect.io/docs/wxcc-create-task)                                               | Calls Webex CC Task API to Create a new Task at WxCC using a unique identifier.                                                                                        | When a new conversation is initiated by an end customer, or an existing conversation is reopened.                                                   | Create Task          | v1.2 and v1.0              |
| [Set Variable](https://help.imiconnect.io/docs/set-variable)                 | Webex Contact Center supports use of global variables and custom flow variables (local variables) while building flows for the digital channels.                       |                                                                                                                                                     | Set Variable         |                            |
|                                                                              | Global variables are defined in the Webex CC Admin Portal.                                                                                                             |                                                                                                                                                     | Set Global Variable  | v1.7                       |
|                                                                              | Flow variables are defined in the flow.                                                                                                                                |                                                                                                                                                     | Set Flow Variable    | v1.7                       |
| [Queue Task](https://help.webexconnect.io/docs/wxcc-queue-task)                                                 | Calls Webex CC Task API to Queue a Task.                                                                                                                               | When you want to escalate a conversation to a customer service agent in Cisco Webex Contact Center                                                                 | Queue Task           | v1.0, v1.1, v1.2, and v1.3 |
| [PIQ and EWT](https://help.webexconnect.io/docs/wxcc-piq-and-ewt)                                               | Provides the caller's current Position in Queue (PIQ) and the Estimated Wait Time (EWT).                                                                               | When you want to inform a customer who is waiting to chat with an agent about the estimated wait time and there position in queue.                  | PIQ and EWT          | v1.1                       |
| [Routed Notification](https://help.webexconnect.io/docs/wxcc-routed-notification)                               | Calls Webex CC Task API to notify that that the task routed is accepted when the participant is added successfully.                                                    | After receiving a confirmation from Cisco Webex Contact Center on whether a routing request (i.e., addition of participant to a conversation) was accepted or not. | Routed Accepted      | v1.1                       |
|                                                                              | Calls Webex CC Task API to notify that that the task routed is rejected when adding the participant failed.                                                            | After receiving a confirmation from Cisco Webex Contact Center on whether a routing request (i.e., addition of participant to a conversation) was rejected or not. | Routed Rejected      | v1.1                       |
| [Modify Notification](https://help.webexconnect.io/docs/wxcc-modify-notification)                               | Calls Webex CC Task API to notify that that the task modified accepted when the participant is added/removed successfully based on the context.                        | After receiving a confirmation from Cisco Webex Contact Center on whether a task modification request (such as conversation transfer) was accepted or not.         | Modified Accepted    | v1.1                       |
|                                                                              | Calls Webex CC Task API to notify that that the task modified rejected when adding/removing the participant failed based on the context.                               | After receiving a confirmation from Cisco Webex Contact Center on whether a task modification request (such as conversation transfer) was rejected or not.         | Modified Rejected    | v1.1                       |
| [Screen Pop](https://help.webexconnect.io/docs/wxcc-screen-pop)                                                 | Calls Webex CC Screen pop API. While configuring flows in Webex Connect, you’d need to use this node for sending a screen pop message to the agent contact on Webex CC. | When sending a pop-up message to the agent contact on Cisco Webex Contact Center.                                                                                  | Screen Pop           | v1.1                       |
| [Close Task](https://help.webexconnect.io/docs/wxcc-close-task)                                                 | Calls Webex CC Task API to close task directly on Webex CC.                                                                                                            | For closing a Task when an agent closes a conversation, or a conversation gets closed due to some unexpected failure.                               | Closed Task on WxCC  | v1.0                       |
|                                                                              | Calls Webex CC Task API to notify Webex CC on close task accept.                                                                                                       | Received from Cisco Webex Contact Center when an agent accepts a conversation.                                                                      | Close Task Accept    | v1.0                       |
|                                                                              | Calls Webex CC Task API to notify Webex CC on close task reject.                                                                                                       | Received from Cisco Webex Contact Center when an agent rejects a conversation.                                                                      | Close Task Reject    | v1.0                       |
| [Resolve Conversation](https://help.imiconnect.io/docs/resolve-conversation) | Calls Webex Engage Resolve Conversation API to resolve conversation on Webex Engage.                                                                                   |                                                                                                                                                     | Resolve Conversation | v1.1 and v1.0              |

## Node Authorization

Client applications (in this case Webex Connect) are required to provide a valid access token for using various Cisco Webex Contact Center and imiengage APIs. The access token is generated using the authorization details configured within the ‘Node Runtime Authorization’ field that Cisco Webex Contact Center users are required to provide during flow configuration. 

> 📘 Note
> 
> For all the Authorization that is being accessed by Webex Connect, if the authorizing credentials are updated in the integrating system, the Webex Connect will loose access to the integration and the users will have to re-authorize the node.
> 
> Example of Authorization Credentials are: Username, Password, Client ID, Client Secret Key, Access Key etc.

## Node Authorization for Cisco Webex Contact Center Task nodes

For Cisco Webex Contact Center Task nodes  (Task nodes are Create Task, Set Variable, Queue Task, PIQ and EWT, Routed Notification, Modified Notification, Screen Pop, Close Task, and Resolve Conversation).

To authorize a pre-built integration:

1. Go to Assets → Integrations.
2. Select Pre-built Integrations under Integration Type, to display the list of all pre-built integrations.  
   The integrations which are not yet authorized show the status as Pending Authorization.



![Screenshot of Integrations Page.](https://files.readme.io/31de8c2-Integrations.jpg)




3. Click Actions → Manage associated with the integration you want to authorize.
4. On the Manage Integrations page, scroll down to the Node Authorizations section. This section lists all the authorizations mapped to this integration.



![Screenshot of Manage Prebuilt Integration Page.](https://files.readme.io/c1a9cfb-Integrations1.jpg)




> 📘 Note
> 
> If the integration nodes have no auth required, then it is not shown in the list.

5. Click Action → Add Authorization associated with the authorization, where Auth Type is oauth2 and Status is Authorization Pending.



![Adding OAuth2 authorization.](https://files.readme.io/0ca30e3-wxcc_1.jpg)




6. Enter the Authorization Name
7. Click Authorize.  
   A pop-up appears. 
8. Enter your Cisco email address and click **Sign in**.

> 🚧 **Note:**
> 
> The user credentials used to authorize the integration must have a **Contact Center License** mapped to them with an **Admin role** (_Full Admin_ or _Contact Center Admin_) in Control Hub as a pre-requisite.
> 
> It is recommended to use dedicated user credentials, as any changes to these credentials or the user may cause the authorization node to fail, which could impact other nodes in IMI.



![Authorizing integration with Cisco account.](https://files.readme.io/a15ce6c-wxcc_sso.jpg)




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