# Search conversation - WxEngage standalone

Source: https://help.webexconnect.io/docs/search-conversation-1
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:29+00:00

When setting up flows in Webex Connect, you may use this node to search for an existing conversation based on the customer's channel identity and the business's channel asset. Some channels may need extra context to accurately resolve a message, such as including the subject line in email conversations. This node utilizes the "**Search Conversation**" API from Webex Engage. A detailed guide is available in the table below:

| Channel                     | Customer Address (customerAddress) | Business Address (bizAddress) | Additional context                                        |
| :-------------------------- | :--------------------------------- | :---------------------------- | :-------------------------------------------------------- |
| SMS                         | Customer Mobile Number             | Business Longcode             | -                                                         |
| Facebook Messenger          | Page Scoped ID                     | Page ID                       | -                                                         |
| Livechat                    | User ID                            | App ID                        | Thread ID, User ID and Browserfingerprint                 |
| Email                       | Email ID                           | Business Mailbox              | Subject, To Recipients, Cc Recipients, In Reply To Header |
| Apple Messages for Business | AMB User ID                        | AMB Account ID                | -                                                         |
| WhatsApp Business           | WhatsApp Mobile Number             | WhatsApp Business Longcode    | -                                                         |
| API                         | User ID                            | Business ID                   | Business ID can be fetched from New Admin console.        |

> 📘 Configuring API channel
> 
> The Business Identity for the API channel is displayed only on the New Admin Console. If this option is not visible on your Webex Engage Tenant, contact our Support Team.

## Configuration

To configure a search conversation node, follow these steps:

1. Drag and drop the **Search conversation** node from the Node palette from the left side of the screen.
2. Double-click the Search conversation node to view the configuration settings.



![Screenshot displaying the Configuration Settings for Search conversation node](https://files.readme.io/f955350ecbd74321200d510368f6a3aa3dea10fe77f2c88bd37e75ac4cf3352e-image.png)




3. Choose **Search conversation** from the Method Name drop-down list.
4. Choose **Authorization** from the Node Runtime Authorization drop-down list.  
   We recommend you set Authorization to a Default Authentication configured in [WxEngage's Integrations](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) screen under WxConnect's Integrations. Once you re-authenticate from the Integrations screen, all your nodes across flows will pick up the updated token.
5. Choose a channel from the **Channel** drop-down list.

- **SMS** - If you choose SMS channel, you will view following settings:
  - **Business Longcode / Shortcode** - Choose your Business Longcode / Shortcode from the Assets drop-down list.
  - **Customer Mobile Number** - In general the value is set to **$(n2.sms.msisdn**).  
    MSISDN from the output variables of the start node is the customer mobile number.
- **Facebook Messenger** - If you choose Facebook Messenger channel, you will view following settings:
  - **Page ID** - Choose your Facebook Messenger Page from the Facebook Page drop-down list.
  - **Facebook Page Scoped ID (PS ID)** - **$(n2.messenger.psId)**  
    PS ID from the output variables of the start node is the Facebook PS ID.
- **Livechat** - If you choose Livechat channel, you will view following settings:
  - **Livechat App** - Choose your Livechat App from the Livechat Apps drop-down list.
  - **Livechat Thread ID** - In general the value is set to **$(n2.inappmessaging.threadId)**.  
      threadId from the output variables of the start node is the Thread ID.  
    OR
  - **Livechat User ID** -  In general the value is set to **$(n2.inappmessaging.userId)**  
    userId from the output variables of the start node is the Customer Address.
  - **Livechat Browser Fingerprint** - In general the value is set to **$(n2.inappmessaging.userId)**.  
      userId from the output variables of the start node is the Livechat Browser Fingerprint.  
    <br />
- **Email** - If you choose Email channel, you will view following settings:
  - **Business Mailbox** - Choose your Business Mailbox from the drop-down list.
  - **From Address** - In general the value is set to **$(n2.email.emailId)**.  
    emailId in the output variables of the start node is From Address.
  - **In Reply To** - In general the value is set to **$(n2.email.inReplyTo)**.  
    InReplyTo in the output variables of the start node is the In Reply To.
  - **To Recipients** - In general the value is set to **$(n2.email.toAddresses)**.  
    toAddresses in the output variables of the start node is the To Recipients.
  - **Cc Recipients** - In general the value is set to **$(n2.email.ccRecipients)**.  
    ccRecipients in the output variables of the start node is the Cc Recipients.
  - **Email Subject** - In general the value is set to **$(n2.email.subject)**.  
    subject in the output variables of the start node is the Subject.
- **WhatsApp** - If you choose WhatsApp channel, you will view following settings:
  - **WhatsApp Business Longcode** - Choose your WhatsApp Business Longcode from the Assets drop-down list.
  - **WhatsApp Mobile Number** - In general the value is set to **$(n2.whatsapp.waId)**.  
    waId in the output variables of the start node is the WhatsApp Mobile Number.
- **Apple Messages for Business (AMB)** - If you choose AMB channel, you will view following settings:
  - **AMB Account ID** - Choose your Account from the AMB Account ID drop-down list.
  - **AMB User ID** - In general the value is set to **$(n2.abc.userId)**.  
    userId in the output variables of the start node is from AMB User ID.
- **API** - If you choose API channel, you will view following settings:
  - **Business Address** - Choose your address from the Business Address drop-down list.
  - **Customer Address** - Enter the Customer Address.  
    Unique identifier of the customer as per the channel in context.

6. Click **Save**.

## Output variables

| Variable           | Description                                                                                                                                                                                                                                        |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| conversationId     | System generated unique identifier of the conversation that needs to be used subsequently in the Flow downstream                                                                                                                                   |
| aliasId            | Auxiliary reference identifier mapped to the conversation                                                                                                                                                                                          |
| conversationExists | Boolean value that denotes whether an open conversation exists against the customer                                                                                                                                                                |
| status             | Status enum - success/failed                                                                                                                                                                                                                       |
| teamId             | Team ID (GUID) that the conversation resides in currently                                                                                                                                                                                          |
| userId             | Login ID of the user to whom the conversation is assigned. If the conversation is still in the queue, the userId will return null. However, if the customer is returning, the system will return the Login ID of the last agent who assisted them. |
| apiStatus          | HTTP status code from the underlying response received from WxEngage's REST API                                                                                                                                                                    |
| code               | Numeric code received from WxEngage's API response                                                                                                                                                                                                 |
| description        | Description received from WxEngage's API response                                                                                                                                                                                                  |
| responsePayload    | Raw WxEngage's API response payload (JSON string)                                                                                                                                                                                                  |

## Node outcomes

| Category | Outcome             | Description                                                                                                                                                                                                                |
| :------- | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success  | noConversationFound | New customer who has never interacted with the Business before                                                                                                                                                             |
|          | conversationInQueue | Existing conversation found in the status: queued. Message to be resolved subsequently using the Append message node                                                                                                       |
|          | conversationActive  | Existing conversation found in the status: active. Message to be resolved subsequently using the Append message node                                                                                                       |
|          | conversationOnHold  | Existing conversation found in the status: on hold. Message to be resolved subsequently using the Append message node                                                                                                      |
|          | conversationClosed  | Existing conversation found in the status: closed. Message to be resolved subsequently by re-opening the last conversation or creating a new conversation as per the required business logic                               |
| Errors   | onTimeout           | Could not receive an API response from WxEngage within the agreed time-out                                                                                                                                                 |
|          | onInvalidData       | Invalid data configured in WxConnect node                                                                                                                                                                                  |
|          | onError             | Error in WxConnect's middleware services                                                                                                                                                                                   |
|          | onInvalidChoice     | Invalid choice                                                                                                                                                                                                             |
|          | onauthorizationfail | Failed to Authorize successfully. We recommend you to recheck your Node Authorization configurations in the [Authorize Integration](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) section |
|          | Failure             | Any other run time failures                                                                                                                                                                                                |