While you can always configure your own flows for handling incoming inquiries over digital messaging channels (such as SMS, Live Chat, WhatsApp, Apple Messages for Business, Facebook Messenger, Email, etc.) supported by <<prodname>> and <<CCE>> in combination, we have provided some representative flows to provide you with a reference on how to configure such flows.

These flows are available for [download](https://software.cisco.com/download/home/268439622/type/286332149/release/12.6(2)).

There are a total of 15 representative flows as listed below:

[block:parameters]
{
  "data": {
    "h-0": "Flow Name",
    "h-1": "Description",
    "h-2": "Additional context",
    "0-0": "SMS Inbound Flow",
    "0-1": "Used to handle incoming messages from end customers over SMS. This flow includes a welcome message and provides options for customers to escalate to an agent or drop out of a conversation using intent keywords.",
    "0-2": "This flow needs to be configured separately for each SMS number/Sender ID.",
    "1-0": "Email Inbound Flow",
    "1-1": "Used to handle emails from end customers and escalates the task to CCE to assign an agent.",
    "1-2": "This flow evaluates for any sensitive data / PCI compliance in the email text or attachments and notifies the sender if any sensitive data is detected.  \nThis flow needs to be configured separately for each Email asset.",
    "2-0": "Live Chat Inbound Flow",
    "2-1": "Used to handle incoming messages from end customers over live chat.",
    "2-2": "This flow needs to be configured separately for each Live Chat asset. This flow evaluates for any sensitive data / PCI compliance in the text messages or attachments from end customers and notifies them, if any sensitive data is detected.",
    "3-0": "Live Chat Customer Close",
    "3-1": "Used to handle live chat sessions that are closed or abandoned by end customers and informs the agent that the chat is closed or abandoned.",
    "3-2": "This flow needs to be configured separately for each Live Chat asset. This flow also handles chats that are abandoned in CCE queue before an agent gets assigned.",
    "4-0": "Live Chat with WebCallback Flow",
    "4-1": "Similar to Live Chat Inbound Flow, but in addition to regular Live Chat, it checks if the task is queued for a certain threshold (1 min, which is configurable) and then prompts the customer if they'd like to be called back instead.",
    "4-2": "This flow demonstrates how a Live Chat can be turned into a Web Callback and employs the Agent Request feature of CCE under the hood. If Customer opts to be called back, the existing Live Chat request is cancelled, and a Web Callback request is placed instead. These channels / media types are handled through different queues and as soon as an Agent is found, a call is placed to the Customer's phone number.  \nWhile all the other flows for Web Callback, can be same as that for other channels, there is some special handling that is required to switch media from chat to Voice. A separate flow for CLOSED_Webhook processing which closes the cancelled Live Chat request, and also handles the Closed webhook notification from Digital Routing service as soon as an Agent gets assigned for the Web Callback, is required which needs to be used in conjunction with this flow. It is named Live Chat with WebCallback Flow.",
    "5-0": "WebCallback CLOSED",
    "5-1": "Used in conjunction with Live_Chat_Inbound_With_Web_Callback_Flow to provide special handling when switching media from Live Chat to Voice.",
    "5-2": "This flow is triggered when an asynchronous CLOSED Webhook notification is sent from the Digital Routing service when:  \n  \n- The customer stays on and completes the conversation over the Live Chat channel, which may include connecting to an Agent or the task being abandoned while in queue.\n- The customer opts to cancel the Live Chat channel request, and instead receive a Web Callback. A Closed webhook event will be sent indicating the chat request being cancelled.\n- When CCE assigns an agent for the Voice / Web Callback request and initiates a call to the customer's phone number.",
    "6-0": "Facebook Inbound Flow",
    "6-1": "Used to handle incoming messages posted on a Facebook Page integrated into <<prodname>>, by end customers who employ the Facebook Messenger as a channel for communicating with a business. This flow includes a welcome message and options for customers to escalate to an agent or drop out of a conversation using intent keywords. It also showcases and includes rich media controls like a carousel message and quick reply that one can employ while interacting with a customer over the Messenger channel.",
    "6-2": "This flow needs to be configured separately for each Messenger asset. The flow evaluates for any sensitive data / PCI compliance in the text messages or attachments from end customers and notifies them, if any sensitive data is detected.",
    "7-0": "WhatsApp Inbound Flow",
    "7-1": "Used to handle incoming messages sent to a WhatsApp Business account (WABA).  This flow includes a welcome message and options for customers to escalate to an agent or drop out of a conversation using intent keywords. It also showcases and includes rich media controls like an embedded image message and quick reply that one can employ while interacting with a customer over the WhatsApp channel.",
    "7-2": "This flow needs to be configured separately for each WhatsApp asset. The flow evaluates for any sensitive data / PCI compliance in the text messages or attachments from end customers and notifies them, if any sensitive data is detected.",
    "8-0": "AppleMessages_Inbound_Flow",
    "8-1": "Used to handle incoming messages posted on a Apple Messages for Business account (AMB) integrated into <<prodname>>, by end customers who employ Apple Messages for Business as a channel for communicating with a business. This flow includes a 'Welcome' message and options for customers to escalate to an agent, or drop out of a conversation using intent keywords. It also showcases and includes rich media controls like a Carousel message and Quick Reply that one can employ while interacting with a customer over the Apple Messages for Business channel.",
    "8-2": "This flow needs to be configured separately for each Apple Messages for Business asset. The flow evaluates for any sensitive data / PCI compliance in the text messages or attachments from end customers and notifies them, if any sensitive data is detected.",
    "9-0": "AppleMessages_CustomerClose",
    "9-1": "Used to handle Apple Messages sessions that are closed / blocked by end customers, which then informs the agent that the chat has been closed or abandoned.",
    "9-2": "This flow is triggered based on a specific event generated on the Apple Messages for Business channel (Conversation Closed) which is when an end customer chooses not to receive any more messages / contact from a messaging service provider. An agent, if already engaged, or the self service flow is prevented from sending any message to the end customer once this event has been triggered, and until the conversation is unblocked by the end customer. Any existing conversation in Webex Engage or a task in CCE will be terminated on receipt of this event and the corresponding flow being triggered.",
    "10-0": "CREATED Flow",
    "10-1": "Used to send the notification message to the end customer over SMS, live chat, and email media channels when a task is created in CCE.",
    "10-2": "This flow is triggered when an asynchronous CREATED webhook notification from the Digital Routing service is sent owing to the create task request being accepted by the service. These tasks will be subsequently submitted to the CCE router for queueing and routing. On receipt of the notification from the Digital Routing service, the flow sends the notification message to the end customer over the respective channels of communication.",
    "11-0": "QUEUED Flow",
    "11-1": "Used to send the notification message to the end customer over SMS and live chat when there is an update to the Estimated Wait Time (EWT) for a task.",
    "11-2": "This flow is triggered because of an asynchronous QUEUED webhook notification from the Digital Routing service when:  \n_ A task is submitted to CCE for queuing or routing.  \n_ A notification is sent when there are updates to the Estimated Wait Time (EWT) or updates to the task context variables. This requires the RunExternalScript node to be set up in the CCE scripts.  \nNote: When the Digital Routing service submits tasks to CCE, the first queued task will not have any EWT, or the EWT value will be -1. In this scenario, the flow will not send any message to the end customer.  \nThe flow sends messages to end customers only if you've set the call.EstimatedWaitTime and use the RunExternalScript node to notify the Digital Routing service of the EWT.",
    "12-0": "ROUTED Flow",
    "12-1": "Used to add an agent participant to a conversation when <<prodname>> receives the Task Routed event from Contact Center Enterprise. This flow sends a message to the end customer over SMS or Live Chat, notifying that an agent is about to be added to the conversation.",
    "12-2": "This flow is triggered when an asynchronous ROUTED webhook notification is sent from the Digital Routing service after CCE assigns an agent to a task. For the conversation to be loaded on the Agent desktop, the Agent should get added as a participant in Webex Engage, which is what this flow is primarily meant for.",
    "13-0": "CLOSED Flow",
    "13-1": "Used to close a conversation in Webex Engage and send a message to the end customer over SMS or Live Chat, notifying that the conversation has been marked as closed.",
    "13-2": "This flow is triggered when an asynchronous CLOSED webhook notification is sent from the Digital Routing service after agent closes or ends the task on the Agent desktop or when the task is automatically closed by the system due to queuing / routing failures, after being accepted.",
    "14-0": "TRANSFERRED Flow",
    "14-1": "Used to send a message to the end customer over SMS or Live Chat when a conversation is being transferred to another queue by an Agent or when a RONA (Redirect on No Answer) gets triggered owing to No answer or when Agent logs out from the desktop while still having active tasks.",
    "14-2": "The flow is triggered when an asynchronous TRANSFERRED webhook notification is sent from the Digital Routing service owing to an Agent or system-initiated transfer. It removes the transferring Agent as a participant of the Conversation in Webex Engage, before reinjecting the task into the Digital Routing service for the next agent to be assigned as part of the transfer, by invoking the “CCE Create Task” node with the same CCE taskID as the task being transferred.  \n  \nIf the transfer fails, the flow sends a notification message to the end customer over SMS, Live Chat or Email depending on the channel on which the task was created, stating that the conversation will be closed, and the customer must reinitiate it."
  },
  "cols": 3,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


There are some task context variables that get passed along from <<prodname>> while creating a task in CCE that are essential for end to end call flow. The task context can comprise of Call Variables, Expanded Call Context (ECC) variables or Extension Variables:-

1. Call Variables - There are up to 10 Call Variables of 40 bytes each, that can carry task context data. They translate to Peripheral Variables 1 to 10 in CCE, and are prefixed with the string "cv\_" in the Digital Routing API payloads.
2. ECC Variables - ECC variables can be up to 210 bytes each and are identified with a prefix "user" in the API payload. These need to be defined in CCE and added to the "Digital Channel Settings" page in CCE Web Administration tool to ensure task context variables can be sent and retained in Digital Routing Service, and in turn available to <<prodname>> via Webhook notifications.
3. Extension Variables - Extension variables neither have the the ECC variable nor the Call Variable prefix in their names. These are stored in Digital Routing service along with the task and do not get sent as a Call variable in CCE. They are used to store metadata about the task and are used by the <<prodname>> flows to communicate with the end customer on a given channel.  
   <<prodname>> automatically populates the following ECC (Expanded Call Context) and Extension variables while invoking the "CCE Create Task" node:

| Channel                     | Field Name in Create Task node | Underlying ECC/Extension variable populated in Task payload |
| :-------------------------- | :----------------------------- | :---------------------------------------------------------- |
| SMS                         | Conversation Id                | user_DR_MediaResourceID                                     |
| SMS                         | Customer Name                  | user_DR_CustomerName                                        |
| Live Chat                   | Conversation Id                | user_DR_MediaResourceID                                     |
| Live Chat                   | Customer Name                  | user_DR_CustomerName                                        |
| Live Chat                   | Live Chat Thread Id            | ChatThreadID                                                |
| Email                       | Conversation Id                | user_DR_MediaResourceID                                     |
| Email                       | Customer Name                  | user_DR_CustomerName                                        |
| Email                       | Email Message Id               | EmailMessageID                                              |
| Email                       | Subject                        | EmailSubject                                                |
| Email                       | Email CC                       | EmailCCRecipients                                           |
| Email                       | Email BCC                      | EmailBCCRecipients                                          |
| Web Callback                | Conversation Id                | user_DR_MediaResourceID                                     |
| Web Callback                | Customer Name                  | user_DR_CustomerName                                        |
| Web Callback                | LiveChatUserID                 | LiveChatUserID                                              |
| Web Callback                | LiveChatThreadID               | LiveChatThreadID                                            |
| Web Callback                | LiveChatAppID                  | LiveChatAppID                                               |
| Facebook Messenger          | Conversation Id                | user_DR_MediaResourceID                                     |
| Facebook Messenger          | Customer Name                  | user_DR_CustomerName                                        |
| WhatsApp                    | Conversation Id                | user_DR_MediaResourceID                                     |
| WhatsApp                    | Customer Name                  | user_DR_CustomerName                                        |
| Apple Messages for Business | Conversation Id                | user_DR_MediaResourceID                                     |

You can use these flows to create flows in your <<prodname>> account by using the 'Create Flow -> Upload a Flow' method under Flows Tab within a service. These need to be sent as additional Extension variables as part of the Web Callback request. They contain details of the chat channel, through which customer initiated the callback request. It is useful if messages need to be relayed to end customers, while Web Callback is being processed by CCE, or when the Agent gets assigned.  
The Live Chat extension variables (the ones that contain LiveChat\* in the name without the "user underscore" prefix) need to be sent as additional Extension variables as part of Web Callback request. They contain details of the chat channel, through which customer initiated the callback request. This is useful if messages need to be relayed to end customers while Web Callback is being processed by CCE, or when Agent gets assigned.  
The ECC variables (the ones prefixed with "user underscore") need to be defined in CCE, prior to importing the flows and trying out the end to end call flow.

## Creating Flows

To create a flow using upload a flow option:

1. Create a Service (it should be the same as the service that you mapped with <<CCE>> for the Messenger asset) and create a flow by importing the representative flow named _FBM Inbound Message_.
2. Click the service and navigate to Service Dashboard.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ec33205-1.png",
        "service_dashboard.png",
        "Flows tab interface with the Create Flow button highlighted."
      ],
      "align": "center",
      "border": true,
      "caption": " Creating a new flow in the Flows tab."
    }
  ]
}
[/block]


3. Go to the **Flows** tab.
4. Click **Create Flow**.
5. Provide a name for the flow.
6. Select **Upload a flow** in the Method drop-down.
7. Click **Choose File** to upload the required file.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7d8477c-CISCO_WEBEX_CONTACT_CENTER__IMICONNECT_INTEGRATION_Flow_Configuration_using_Sample_Templates_Choose_File.png",
        "CISCO WEBEX CONTACT CENTER & IMICONNECT INTEGRATION Flow Configuration using Sample Templates Choose File.png",
        "Screenshot of the interface with the Method drop-down menu expanded to select \"Upload a flow,\" followed by the Choose File button highlighted, enabling users to browse and upload the required file for the flow."
      ],
      "align": "center",
      "caption": "Uploading a flow via file selection."
    }
  ]
}
[/block]


8. Click Create.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/81f5f9a-CISCO_WEBEX_CONTACT_CENTER__IMICONNECT_INTEGRATION_Flow_Configuration_using_Sample_Templates_Create.png",
        "CISCO WEBEX CONTACT CENTER & IMICONNECT INTEGRATION Flow Configuration using Sample Templates Create.png",
        "Screenshot of the interface with the Method drop-down menu expanded to select \"Upload a flow,\" followed by the Choose File button highlighted, enabling users to browse and upload the required file for the flow."
      ],
      "align": "center",
      "caption": "Uploading a flow via file selection."
    }
  ]
}
[/block]


> 📘 Note
> 
> When a flow is created using an Upload Flow method, it is mandatory to **Save** the flow before proceeding further. This is required to ensure that configurations are saved correctly. As a known limitation missing this step can lead to Evaluate node script formatting getting lost.

## Configure Flows

1. Open the required flow in the flow editor.
2. Double click the pre-built<<CCE>>nodes one at a time and provide authorization for the concerned node.
3. Keep the Method Name as is.
4. Select Add New Authorization in the Node Runtime Authorization drop-down.  
   a. The Add new authorization pop-up window opens.  
   b. Provide a name for the authorization that appears in the Node Runtime Authorization drop-down. Click Authorize. The Cisco Webex Contact Center Enterprise login page appears and you need to provide valid credentials to add the authorization.
5. Refer to the pre-built integration node documentation to configure other fields in the node. 
6. For SMS flow, click the Start Node and select incoming message as the flow trigger option. This step doesn't apply to other channels.

Repeat this process for all of the pre-built integration nodes within the flow. 

Publish your flow once you've made all the changes.

Repeat the above steps for the remaining flows.

> 📘 Note
> 
> If you create a flow or edit an existing flow it is recommended to use the "securityscaninfo variable. The securityscaninfo variables displays a combined result of PCI and malware scans.The securityscaninfo variable is backward compatible with PCI info variable. If PCI and malware are enabled for the tenant, <<prodname>> first performs a PCI scan, then a malware scan, and stores the combined result in the securityscaninfo variable. The combined result is also updated in the PCI variables, so that all existing flows that were using PCI can have malware scan enabled for them without requiring any changes to the flow.

## Understanding Representative Flows

Here's a high level overview of the logic configured in each of the representative flows. The flow comprises of Conversation nodes that interact with the Webex Engage platform and the Task nodes that interact with the Digital Routing service in CCE.

The representative / template flow bundle contains a flow specific to handling Inbound messages (including attachments) per channel, and additionally a couple of flows for closing conversations in the case of Live Chat and Apple Messages for Business, apart from the common CCE webhook event triggered flows for routing, transferring and closing conversations.

The <<prodname>> platform uses Webex Engage as a conversation store and for maintaining chat transcripts as well as any attachments that are sent during an interaction. Every inbound flow defined in the CCE flow template broadly employs a similar mechanism to search for an existing conversation in Webex Engage based on a channel specific identifier, to then decide a flow path on whether a new conversation needs to be created, or an existing conversation needs to be reopened, or the incoming message (or attachment) needs to be appended to the existing conversation, so that the message sent to the customer is seen by the agent (This is also how the chat transcript can capture all the messages and attachments sent by a customer).

The Webex Engage 'Search Conversation' node can have one of the following outcomes, based on the state of the task:

1. noConversationFound - This would be the case for new customer interactions that have no record of previously engaging with the Webex Contact Center on this Media Channel.
2. conversationInQueue - The task is currently in Created (or Queued) state in CCE waiting for an Agent to get assigned.
3. conversationActive - The task is in Routed state with an agent assigned, and the customer is currently interacting with the Agent in an active session.
4. conversationClosed - The task is in Closed state or there is no active conversation in the system. The system does recognize the customer though, based on previous interaction history on this specific media channel using the channel specific identifier. For example, in the case of SMS, this is the Customer's phone number.
5. conversationOnHold - This is currently not applicable for CCE, but it is one of the responses that Webex Engage can return for the Search Conversation API.

### Anti-Malware Scan for Attachments

Today's malware targets organizations for financial gain by infiltrating systems, replicating, laying dormant, and evading detection. Advanced malware protection is crucial to prevent operational disruptions.

<<prodname>> now provides enhanced malware protection for CCE digital channels by continuously monitoring file activity for faster threat identification. This default detection feature protects agents and customers across all digital channels, helping organizations prevent potential breaches.

#### Setting Up <<prodname>> Workflow to Process Anti-Malware Scan Results

By default, this feature is automatically enabled for attachments received across all digital channels via <<prodname>>. All file attachments undergo a malware scan, and only those that pass will be scanned for PCI compliance before being sent to an agent. Files detected as malware are not stored on the <<prodname>> platform, ensuring your Webex Contact Center is protected from potential threats.

The latest <<prodname>> flows are equipped to automatically detect malware files present in attachments and notify agents as well as end customers about the file being dropped because of malicious content. The template flow uses prefilled, channel-specific flow variables that contain the result of the malware scan that were performed on the attachment. Customers can customize or build the malware detection logic in their existing <<prodname>>  flow as per the business requirements by referring to the template flow. If you create a flow or edit an existing flow, it is recommended to use the `securityscaninfo` variable.

> 📘 
> 
> It's important to note that these values pertain to the combined outcomes of both PCI scans and malware scans. For example, when`securityscaninfo.isSecurityCompliance` is set to false, it indicates that either the attachment is malicious or the PCI scan has detected sensitive card information being shared.

#### Parameters and values of the securityscaninfo variable

The parameters and values of the `securityscaninfo` variable are detailed in the table below.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "securityscaninfo.isSecurityValidationDone",
    "0-1": "Values are True or False.  \nDenotes whether the anti-malware scan is enabled for your tenant.",
    "1-0": "securityscaninfo.isSecurityCompliance",
    "1-1": "Values are True, False, or NA.  \nVerifies if the attachment is malware free or not.  \n'NA' denotes that the received message was a plain text with no attachments.",
    "2-0": "securityscaninfo.droppedAttachmentCount",
    "2-1": "Can be a integer or NA.  \nDenotes the total number of attachments that were either dropped or flagged as malicious. If no malicious attachments are detected, this parameter is set to zero.  \n'NA' denotes the received message was a plain text with no attachments.",
    "3-0": "securityscaninfo.securityFailedReason",
    "3-1": "`securityFailedReason` is a JSON object which contains the actual reason the compliance was marked as failed.  \nThe JSON object format is as follows: securityscaninfo.securityFailedReason\": \"{\"text\":\"\"}\"  \nIn cases where malicious content is detected in the attachments, the 'Text' field will begin with the prefix 'Malware: Failed:', followed by the specific reason. If an error occurs during scanning or the file exceeds the size limit for malware scans, the text field will start with the prefix 'System Alert', followed by the relevant reason."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


#### Anti-Malware Notifications Sent to End Customers and Agents via Template Flows

The <<prodname>> platform automatically runs a malware check for all inbound and outbound attachments for all digital channels.  
If any malware is detected in chats, the infected attachment is dropped in both directions. If the attachment the customer sent is infected, the message "The attachment you sent was dropped as it contains malicious data" is displayed to the customer, while the Agent Desktop displays the infected attachment as a "blocked or dropped" file and doesn't provide an option to download the same.  
The same applies to emails, where the email content is sent to the agent, but without any detected malicious attachments. The malicious attachments are displayed as "blocked or dropped."

**Considerations**:  
If a customer sends an attachment that exceeds 25 MB, the file is not sent to the agent, and the customer receives the notification: "The attachment(s) you sent could not be processed at the moment." Simultaneously, the Agent Desktop marks the file as "The attachment(s) sent by the customer could not be scanned for Malware and so was dropped," and the agent will have no option to download it.  
Not all digital channels can display the file name when files are rejected, either because they are flagged as malicious or contain sensitive PCI data. For details, see the table below.

| Digital Channel             | Filename Displayed |
| :-------------------------- | :----------------- |
| Email                       | Yes                |
| Live Chat                   | No                 |
| SMS                         | No                 |
| Facebook Messenger          | No                 |
| WhatsApp                    | Yes                |
| Apple Messages for Business | No                 |

> 📘 Flows
> 
> If you are building new flows using the CCE template flows, the message relayed to the agent and customer will include the filename that was dropped. However, if you are using custom flows or updating existing flows to process malware scan results, one can find the logic used to populate the filename of the dropped files in the "Evaluate MalwareScan Compliance" node of the CCE template flow.

For more details about the security scan including PCI scan service, one can refer to the CCE Features Guide available here: <https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/ucce_b_1501_features-guide/rcct_m_150_digital-channels-integration-using-webex-connect.html#_e0442e2e-6a35-43c0-b0bb-9ec0531ad3e8>

## CCE Flows

### SMS Inbound Flow

When an inbound message is received over SMS channel, <<prodname>> searches for the conversation in Webex Engage. If the conversation already exists, then the incoming message is appended to the existing conversation, else a new conversation is created. Alternately an existing conversation that was previously closed, can also be reopened. Reopening a conversation has the advantage of retaining interaction history with the customer when the conversation lands on the Agent desktop, including all past interactions. The downside is that a new interaction for a completely different service request may get appended to the same conversation, based on Customer's phone number.

The Search Conversation node can have one of the following outcomes, based on the state of the task:-

- noConversationFound - This would be the case for new customer interactions that have no record of previously engaging with the Contact Center on this Media Channel.
- conversationInQueue - The task is currently in Created (or Queued) state in CCE waiting for an Agent to get assigned.  
- conversationActive - The task is in Routed state, and the customer is currently interacting with the Agent in an active session.
- conversationClosed - The task is in Closed state or there is no active conversation in the system. The system does recognize the customer though, based on previous interaction history on this specific media channel using the channel specific identifier, which in the case of SMS is Customer's phone number.
- conversationOnHold - This is currently not applicable for CCE, but is one of the responses that Webex Engage can return for the Search Conversation API.  
  In the representative flow, a new conversation gets created if an existing conversation is found to be closed. Once a new conversation is created, a welcome message is sent to the end customer followed by a couple of options to choose from, so as to determine what service is being requested. Depending on the customer's input, a task would be created in CCE with the corresponding Script Selector being passed in the Create Task API request. Script Selectors determine which CCE script gets executed for the task, which in turn determines which Skill Groups and Precisions Queues should be targeted for the task. One may pass additional call context data to take appropriate routing decisions or determine task priority in CCE scripts.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0a365725e25bcdc4ecb91ad3a7475e031436b9073f2555e8de18e8f6a849df88-SMS_Inbound_Flow.jpg",
        "SMS Inbound Flow.jpg",
        "Screenshot of SMS Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "SMS Inbound Message Flow"
    }
  ]
}
[/block]


Search Conversation, Append Conversation, Create Conversation and Close Conversation nodes are designed for conversation handling in Webex Engage.

The flow also allows for and checks whether a customer wants to end an interaction by searching for the "End Conversation" phrase in the text message. This allows the customer to start a new interaction all over again, starting with the welcome message. If the task was already submitted to CCE, the flow invokes the "CCE End Task" node to close or abandon the task, depending on whether the Agent was already assigned to it.

The flow inherently also checks for PCI compliance in the message sent by end customer and informs the end user if sensitive information has been detected. The sensitive data is automatically masked before it gets appended to the Conversation to be sent to the Agent, or recorded as response during self service.

The SMS Inbound flow ends when a task has been created and the CCE taskId has been updated in the Conversation object in Webex Engage.

The following custom variables are used in the flow:-

- errorTechnicalIssue
- errorSendingMessage
- errorServiceNotAvailable
- automatedResponse
- actual_message_content
- TaskID
- customer_response
- ScriptSelector
- ClosedMessage
- isPCICompliance
- isPCIValidationDone
- senderNumber
- status
- userId

You can view these configurations by clicking on the setting icon on the top right side of the flow canvas.

### Email Inbound Flow

This flow is triggered when an email message is received by the <<prodname>> platform on an Email asset uniquely identified by the asset Email ID. It is very similar to Live Chat where PCI compliance is checked for, in the email body as well as in any attachments looking for sensitive data.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5ff6048b2be3228a0ee09b2a0d2d6afb506d5dbe50a2a0b09218ffc153981326-Email_Inbound_Flow.jpg",
        "Email Inbound Flow.jpg",
        "Screenshot of Email Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Email Inbound Message Flow"
    }
  ]
}
[/block]


The flow ends when the CCE taskID gets updated in Engage using the Update Conversation node.

### Live Chat Inbound Flow

The sequence and logic of the flow is similar to that of the SMS Inbound Flow, where every message sent by the end user triggers a Search Conversation node to determine if a previous interaction is already in progress. If it is, then an Append Conversation node is invoked to append the incoming message to the existing conversation. else a new conversation is created in Webex Engage. A Pre-Chat form which employs a form template to obtain customer details like Name, Email address and service requested (Or query regarding which, the interaction was initiated), is used to get end user inputs. The same details are used to create a Task in CCE by mapping the form input to determine a Script Selector for the task. Additional ECC or call variables may also be sent as needed to CCE while creating the task.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/699c7d89bec6cb021cce9a3b1b8c31498a43e48922653de3acc0457f15100377-Live_Chat_Inbound_Flow.jpg",
        "Live Chat Inbound Flow.jpg",
        "Screenshot of Livechat Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Live Chat Inbound Message Flow"
    }
  ]
}
[/block]


The flow also checks for incoming messages and attachments sent by end customer for PCI compliance, and warns the user of sensitive data having been detected. The sensitive data detected is redacted in messages, and attachments containing sensitive data are dropped.

Following are the custom variables used in this flow:-

- appid
- message
- inappPayloadObject
- nonPCIComplianceReasonObject
- messagetext
- domain
- conversationId
- errorTechnicalIssue
- errorSendingMessage
- liveChatDomain
- err_msg_toomanyrequests
- parseDataAttachment
- isPCICompliance
- isPCIValidationDone

> 📘 
> 
> The liveChatDomain variable should contain the URL of the website (without specifying the protocol like HTTPS) hosting the chat. Eg. support.my-company.com

> 📘 
> 
> The following variables are subject to change and are used for internal reasons to handle integrations between solution components. We do not encourage <<CCE>> flow developers to use these variables (OR) if you do, please acknowledge the risks in doing so. We cannot undertake responsibility if your flows break due to changes in the values stored in these variables.
> 
> - inappmessaging.threadTitle
> - inappmessaging.threadStatus
> - inappmessaging.os
> - inappmessaging.tid
> - inappmessaging.version
> - inappmessaging.deviceId
> - inappmessaging.customtags
> - inappmessaging.extras
> - inappmessaging.message.extras

The flow ends when the CCE taskID gets updated in Engage using the Update Conversation node.

### Live Chat Customer Close Flow

This flow is invoked when the customer ends a chat session by closing the chat window or the browser. The flow invokes the CCE End Task node or an Append Conversation depending on whether the Conversation is in Active state (meaning already assigned to an Agent) or if it is still waiting for Agent assignment, which is akin to abandoning the task in queue. If the Agent was handling the task, then the Append Conversation node lets the Agent know that the customer has left the chat session, so that the Agent can finish wrapping up the task before marking it complete.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/03678d98cc1490b6cec6d35ec273c536ead5863860e49c2b1dc9255f51021b69-Live_Chat_Closed_Flow.jpg",
        "Live Chat Closed Flow.jpg",
        "Screenshot of Live Chat Close Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Live Chat Close Flow"
    }
  ]
}
[/block]


The custom variables used in this flow are:-

- status
- userId

### Live Chat with WebCallback Flow

This flow is similar to the Live Chat Inbound flow, but also offers an option to place a Web Callback / Voice Callback request to the customer instead of waiting for an Agent on the chat medium.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c464bc06ed203162347be4473daa5c2c3a54ac23af09a760b70779473e97006f-Live_Chat_Inbound_With_Web_Callback.jpg",
        null,
        "Screenshot of Live Chat with WebCallback Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Live Chat with WebCallback Flow - Part 1"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3e4930cfa6881d7c09af517ffd760ea9df56699174303f86721e9789e8d5018a-Live_Chat_Inbound_With_Web_Callback_-_Part_2.jpg",
        null,
        "Screenshot of Live Chat with WebCallback Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Live Chat with WebCallback Flow - Part 2"
    }
  ]
}
[/block]


To increase readability, there is a separate page / tab in the same flow that provides the logic which deals with cancelling the chat request and then placing a Web Callback request for a call to be placed to the customer's phone number that was received as input in a Pre-Chat form.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2695d2567a4a012c811cc000cdc59bb4505b9299fc95753be4ef05a5affdde42-Live_Chat_Inbound_With_Web_Callback_-_Web_Callback_Tab_3.jpg",
        null,
        "Screenshot of Live Chat with WebCallback Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Live Chat with WebCallback Flow - Part 3"
    }
  ]
}
[/block]


The custom variables used in this flow are:-

- appid
- message
- inappPayloadObject
- nonPCIComplianceReasonObject
- messagetext
- domain
- conversationId
- errorTechnicalIssue
- errorSendingMessage
- liveChatDomain
- err_msg_toomanyrequests
- parseDataAttachment
- isPCICompliance
- isPCIValidationDone
- currentTaskState
- CallbackRequested
- CustomerPhoneNumber
- CustomerName
- CustomerID
- ScriptSelector
- ChatThreadID
- ChatUserID
- errorCallbackFailed
- errorEndTaskFailed

### WebCallback CLOSED

This flow is used in conjunction with the Live Chat with Web Callback flow to handle Closed webhook events received from Digital Routing service and message appropriately to end customers who initiated the interaction using Live Chat as a medium. Since there is a possible switch in media, based on customer input, the Closed Webhook event needs to be handled differently. The flow aims at showcasing how this can be achieved in general when switching a digital channel task to a voice based callback from the Contact Center.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/24aae1ad516ba61f3f4ccafcf332d1138d860feea57302f90e15a080d27fde80-Closed_Webhook_Flow_WebCallback.jpg",
        null,
        "Screenshot of WebCallback CLOSED"
      ],
      "align": "center",
      "border": true,
      "caption": "WebCallback CLOSED"
    }
  ]
}
[/block]


The custom variables used in this flow are:-

- TaskContextVariables
- ClosedMessage
- mediaResourceID
- LiveChatThreadID
- LiveChatAppID
- LiveChatUserID
- WebCallbackMessage
- IsWebCallbackRequested
- WebCallbackAgentFound

### Facebook Inbound Message Flow

The sequence and logic of the flow is similar to that of the SMS Inbound Flow, where every message sent by the end user using the Facebook Messenger triggers a Search Conversation node to determine if a previous interaction is already in progress. If it is, then an Append Conversation node is invoked to append the incoming message to the existing conversation, else a new conversation is created in Webex Engage. Every Facebook page that is integrated with <<prodname>> as an asset will need its own flow to handle conversations that an end customer initiates with a business. An end user interacting with a Facebook page is assigned a unique ID called Facebook PSID (Page Scoped Identifier) which is used as a channel identifier to uniquely identify an end user interacting with the Facebook page and tie all the messages together in a conversation.  
The <<prodname>> platform provides rich content like carousel messages, quick replies etc that can be used while interacting with an end user, and the template flow showcases how this can be done during self service before escalating the conversation to an agent, based on the user's selection received via a quick reply response. The corresponding Script Selector is passed along to CCE that will indirectly try to assign an agent from a pool of agents having the corresponding skill set to handle the query. The name of the customer as received from the Facebook platform is also passed along into CCE via the CCE Create Task node with an option to additionally pass task context via ECC (Expanded Call Context) or call variables, while creating the CCE task.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9947227a624865df1ca1d5c342f7ce8d4c31949057587ef58da3ab70d563760d-Facebook_Inbound_Flow_-_Part_1.jpg",
        null,
        "Screenshot of Facebook Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Facebook Inbound Message Flow - Part 1"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4f05768d6de3cdfebfc348d0992cf3dd6f982d86da88d9cfae5e16236987a388-Facebook_Inbound_Flow_-_Part_2.jpg",
        null,
        "Screenshot of Facebook Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Facebook Inbound Message Flow - Part 2"
    }
  ]
}
[/block]


The flow ends when the CCE taskID gets updated in Webex Engage using the Update Conversation node.  
The custom variables used in this flow are as follows:

- FBpageid
- messagetext
- messengerPayloadObject
- conversationId
- automatedresponse
- errorTechnicalIssue
- customerresponse
- ClosedMessage
- postbackresponse
- attachmentURL
- location
- customerName
- errorSendingMessage
- check_message_content
- actual_message_content
- locationURL
- latitude
- longitude
- contentType
- LocationLabel
- transId
- isPCIValidationDone
- droppedAttachmentCount
- isPCICompliance
- nonPCIComplianceReasonObject
- CustomerEndedAgentMessage
- ScriptSelector
- UtcConvertedTimeStamp
- AssignedAgentID
- ConversationStatus
- CCETaskID

You can view these variables and their default values by clicking on the setting icon on the top right hand side of the flow canvas. You may customize the messages as needed. Some of the variables like FBpageid should definitely be updated to the Facebook Page ID of the Messenger asset created in <<prodname>>. While Location can be received in the Connect platform, they currently cannot be shared with an agent since Webex Engage currently doesn't support it - you may choose to store this in other external systems if a Delivery / Pick up location has been shared by an end user interacting with your business.

### WhatsApp Inbound Message Flow

The sequence and logic of the flow is similar to that of the SMS Inbound Flow, where every message sent by the end user using the WhatsApp Messenger triggers a Search Conversation node to determine if a previous interaction is already in progress. If it is, then an Append Conversation node is invoked to append the incoming message to the existing conversation, else a new conversation is created in Webex Engage. Every WhatsApp Business account (WABA) integrated with <<prodname>> as an asset will need its own flow to handle conversations that an end customer initiates with the business account.  
The <<prodname>> platform provides rich content like embedded images / videos, quick replies etc that can be used while interacting with an end user, and the template flow showcases how this can be done during self service before escalating the conversation to an agent, based on the user's selection received via a quick reply response. The corresponding Script Selector is passed along to CCE that will indirectly try to assign an agent from a pool of agents having the corresponding skill set to handle the query. The name of the customer as received from the WhatsApp platform is also passed along into CCE via the CCE Create Task node with an option to additionally pass task context via ECC (Expanded Call Context) or call variables, while creating the CCE task.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d2320f3243891cae0f3a42fd47b712608129a89846706187cc123cf558a45a94-WhatsApp_Inbound_Flow_-_Part_1.jpg",
        null,
        "Screenshot of WhatsApp Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "WhatsApp Inbound Message Flow - Part 1"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5c7dd502e1752b5b178f81405502aef70234960aec905acff37c4af9023dd335-WhatsApp_Inbound_Flow_-_Part_2.jpg",
        null,
        "Screenshot of WhatsApp Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "WhatsApp Inbound Message Flow - Part 2"
    }
  ]
}
[/block]


The flow ends when the CCE taskID gets updated in Webex Engage using the Update Conversation node.  
The custom variables used in this flow are as follows: 

- messagetext
- messengerPayloadObject
- conversationId
- WANumber
- errorTechnicalIssue
- customerresponse
- ClosedMessage
- postbackresponse
- attachmentURL
- location
- customerName
- automatedresponse
- errorSendingMessage
- check_message_content
- actual_message_content
- locationURL
- latitude
- longitude
- contentType
- LocationLabel
- transId
- isPCIValidationDone
- droppedAttachmentCount
- isPCICompliance
- nonPCIComplianceReasonObject
- CustomerEndedAgentMessage
- ScriptSelector
- UtcConvertedTimeStamp
- customerResponseTimestamp
- postbackResponseTimestamp
- messageTimestamp
- AssignedAgentID
- ConversationStatus
- CCETaskID

You can view these variables and their default values by clicking on the setting icon on the top right hand side of the flow canvas. You may customize the messages as needed. Some of the variables like WANumber should definitely be updated to the WhatsApp Business phone number of the WABA asset created in <<prodname>> including country code sans the plus sign. Similar to Facebook Messenger, while Location can be received in the Connect platform, they currently cannot be shared with an agent since Webex Engage currently doesn't support it - you may choose to store this in other external systems if a Delivery / Pick up location has been shared by an end user interacting with your business.

> 📘 Note
> 
> Please note that we do not support appending WhatsApp Location messages to conversations. As a workaround, you must extract the latitude and longitude and provide them as plain text by generating a map URL using Google Maps or a similar service.

### Apple Messages for Business (AMB) Inbound Message Flow

When an inbound message is received over the <<AMB>> channel, <<prodname>> initiates a conversation search within Webex Engage to determine if an existing interaction exists.

- If a conversation already exists, the incoming message is appended to the same conversation.
- If no active conversation exists, a new conversation is created.
- If a conversation was previously closed, it can be reopened under the same interaction history. The main advantage of reopening a Conversation is that the conversation history is preserved, allowing agents to view past customer interactions when the conversation reaches the agent desktop, and that customers need not repeat themselves, as past messages remain available for context. Disadvantage is that unrelated interactions from the same customer even for different Lines of Business (LOB) or assets will be seen by other agents as well. Discretion of whether conversation should be reopened or a new one created, should be based on business requirement.

In the representative flow, a new conversation gets created if an existing conversation is found to be closed. Once a new conversation is created, a welcome message is sent to the end customer, followed by a couple of options to choose from, so as to determine what service is being requested. Depending on the customer's input, a task would be created in CCE with the corresponding Script Selector being passed in the Create Task API request. Script Selectors determine which CCE script gets executed for the task, which in turn determines which Skill Groups and Precisions Queues should be targeted for the task. One may pass additional call context data to take appropriate routing decisions or determine task priority in CCE scripts.  
The Customer Name is not provided by Apple to Messaging Service Providers (MSPs) like <<prodname>>. Your business will need to present a form to fetch the detail as an input which the CCE template flow also does, so that the customer name can be passed to CCE as a call variable.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8c9254b00f1c8cc5ad31e1041a4ea24afb193d0130ded5a15b5bdfaebd767969-Apple_Inbound_Flow_-_Part_1.jpg",
        null,
        "Apple Messages for Business Inbound Message Flow - Part 1"
      ],
      "align": "center",
      "border": true,
      "caption": "Apple Messages for Business Inbound Message Flow - Part 1"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2e1334f0032a422058d104b0e2228231d4e2caeea6719c1a2b4cf85db77a8fef-Apple_Inbound_Flow_-_Part_2.jpg",
        null,
        "Apple Messages for Business Inbound Message Flow - Part 2"
      ],
      "align": "center",
      "border": true,
      "caption": "Apple Messages for Business Inbound Message Flow - Part 2"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ccdc6c12bd9c8c6ccc126c98eb3541d5bbc38029f48207db936f8c6998a30dfa-Apple_Inbound_Flow_-_Part_3.jpg",
        null,
        "Apple Messages for Business Inbound Message Flow - Part 3"
      ],
      "align": "center",
      "border": true,
      "caption": "Apple Messages for Business Inbound Message Flow - Part 3"
    }
  ]
}
[/block]


Search Conversation, Append Conversation, Create Conversation and Close Conversation nodes are designed for conversation handling in Webex Engage.  
The flow also allows for and checks whether a customer wants to end an interaction by searching for the "End Conversation" phrase in the text message. This allows the customer to start a new interaction all over again, starting with the welcome message. If the task was already submitted to CCE, the flow invokes the "CCE End Task" node to close or abandon the task, depending on whether the Agent was already assigned to it.  
The flow inherently also checks for PCI compliance in the message sent by end customer and informs the end user if sensitive information has been detected. The sensitive data is automatically masked before it gets appended to the Conversation to be sent to the Agent, or recorded as response during self service.  
The <<AMB>> Inbound flow ends when a task has been created and the CCE taskId has been updated in the Conversation object in Webex Engage.

The custom variables used in this flow are:-

- messagetext
- messengerPayloadObject
- conversationId
- automatedresponse
- errorTechnicalIssue
- customerresponse
- ClosedMessage
- postbackresponse
- attachmentURL
- location
- customerName
- errorSendingMessage
- check_message_content
- actual_message_content
- locationURL
- latitude
- longitude
- contentType
- LocationLabel
- transId
- isPCIValidationDone
- droppedAttachmentCount
- isPCICompliance
- nonPCIComplianceReasonObject
- CustomerEndedAgentMessage
- ScriptSelector
- UtcConvertedTimeStamp
- AssignedAgentID
- ConversationStatus
- CCETaskID

### Apple Messages for Business (AMB) Customer Abandon Close Flow

This flow is invoked when the customer ends a chat session by closing the chat window or the browser. The flow invokes the CCE End Task node or an Append Conversation depending on whether the Conversation is in Active state (meaning already assigned to an Agent) or if it is still waiting for Agent assignment, which is akin to abandoning the task in queue. If the Agent was handling the task, then the Append Conversation node lets the Agent know that the customer has left the chat session, so that the Agent can finish wrapping up the task before marking it complete.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/004d6a2c7e2854aff79e4e4583d8386543f99fe6643b53ed16a1b844265b7c67-AMB_Flow_2.png",
        null,
        "Apple Messages for Business Customer Abandon Close Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Image for Apple Messages for Business Customer Abandon Close Flow"
    }
  ]
}
[/block]


The custom variables used in this flow are:

- status
- userId

## CCE Webhook event triggered Flows for routing and closing tasks

### Conditional execution of Webhook event triggered flows

The Webhook flows that are meant to interact with and send messages back to the customer as the task transitions in the underlying CCE system, can only be associated with one asset at a time per media channels - SMS, Live Chat and Email. That is because a flow can only be associated with a single Live Chat or Email asset at a time, when the flow is made live. The CCE template/representative flows have a pre-defined conditions set per media channel with a sample Asset/AppID, that would not match the assets being employed in the tenant where these flow templates get imported to create new flows. These asset IDs need to be updated to match the ID of the assets or SMS number being used in the tenant. **This is an important step before making the flow live to ensure that end to end messaging and other operations like agent assignment and transfer of tasks (Email or Chat) works seamlessly.**

Shown below is a sample screenshot of the ROUTED node, that has these conditions specified in the template / representative flows (the same applies for all the other webhook triggered flows as well).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fee4ef497e32c301f2a8d7f772ea13b702f38c4af80b5151c4b2b2ddd06b92fa-Conditional_Execution_Of_Webhook_Flows.png",
        "",
        "Screenshot of the ROUTED node"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of the ROUTED node."
    }
  ]
}
[/block]


The destination field in the CCE Webhook event maps to the AppID / AssetID of a LiveChat and Email asset ( $(n2.inappmessaging.appId) / $(n2.email.appId) ), or to the Service Number of an SMS asset ($(n2.sms.serviceNumber)) when creating a task using the "CCE Create Task" node. This Asset AppID or number can be determined by navigating to the Assets → Apps or Assets → Numbers menu in <<prodname>>.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b52ffc05c6b88aee9d4af6613f29e2e7d79c2bb6d9fd736b809714c902f1a2ef-Conditional_2.png",
        "",
        "Screenshot of the Channel Listing Page displaying Email and Mobile/Web App channels."
      ],
      "align": "center",
      "border": true,
      "caption": "Viewing the Channel Listing Page"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ec2ad64e75f8b2bcb5c7041cfd586d2e087d839ceaa1e624e3650136709c0cb9-Conditional_3.png",
        "",
        "Screenshot of the Channel Listing Page displaying SMS channel."
      ],
      "align": "center",
      "border": true,
      "caption": "Viewing the Channel Listing Page."
    }
  ]
}
[/block]


Conditional execution of flow is absolutely necessary when dealing with more than one asset, to ensure the same CCE webhook event does not trigger more than one flow and cause experience issues for either the Agent or the end customer. In order to facilitate different entry points or assets that one has in the Contact Center, a flow developer can assign the right asset ID in the Start Node of these webhook flows, to ensure that the right flow gets executed based on which asset / entry point (indirectly website or email alias) triggered the task creation in CCE. 

**If there is only a single asset in the system per media channel, you may remove these conditions before making the flow live to invoke the flow regardless.** 

Here is a sample screenshot of the ROUTED flow, that has these conditions specified in the template / representative flows (the same applies for all the other webhook triggered flows as well.

### Created Flow

This flow is triggered when the Digital Routing Service accepts the task creation request from <<prodname>>. This is the first asynchronous event notification sent for a task, by the Digital Routing Service. It does not indicate that the task has been submitted to CCE for queueing and routing, but is just an acknowledgement of the request having been accepted by the Digital Routing service. Depending on the Media Channel on which the task was created, a message is sent to the end customer notifying him / her about the live Agent request. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2b4876fa8b2bdbf92a35e5ffd7e0caa733d4f3219f86527a3e88e6db58299627-Created_Flow.jpg",
        "Created Flow.jpg",
        "Screenshot of Created Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Created Flow"
    }
  ]
}
[/block]


Depending on whether or not you have Live Chat, SMS or Email channels set up in your system, you may retain or remove the branches and corresponding nodes in this flow before making it live. The Evaluate node is used to extract extension variables associated with the task, so as to be able to send a message / email to the customer on Live Chat and Email channel respectively.

Following are the custom variables used in the flow:-

- TaskContextVariables
- CreatedMessage
- chatThreadID
- mediaResourceID
- CreatedTimeStamp
- EmailSubject
- EmailMessageID
- EmailCCRecipients
- EmailBCCRecipients
- SenderName
- SystemGenerated

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node.

### Queued Flow

This flow is invoked when a task gets submitted to CCE for queueing and routing by the Digital Routing service, or when there are updated task context or Estimated Wait Time (EWT) received from CCE for a queued task, by the Digital Routing service. The first queued event does not have any EWT and is fired as soon as the request is sent to Media Routing (MR) Peripheral Gateway, and before the CCE script gets executed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b5e79c1a025a3f237e940a6966cbb53928ed93c84a811b5d2744f1c34a77b3bc-Queued_Flow.jpg",
        "Queued Flow.jpg",
        "Screenshot of Queued Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Queued Flow"
    }
  ]
}
[/block]


An Evaluate node is used to determine whether an EWT has been received in the asynchronous Queued event, and depending on the Media Channel associated with the task, the same gets relayed to the end customer on the respective channel. This is just for demonstrating that the EWT retrieved from the CCE system, can be utilized in the flow to take actions. In the representative flow, every queued event with an EWT gets relayed to the end user, which may be undesirable in the real world. 

The following custom variables are used in this flow:-

- TaskContextVariables
- QueuedMessage
- EstimatedWaitTime
- chatThreadID
- mediaResourceID
- QueuedTimeStamp

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node.

### Routed Flow

This flow is invoked on receipt of the Routed event from Digital Routing Service, which in turn is an indication of an Agent being assigned to the task by the CCE Router. The flow uses an Evaluate node to extract the Webex Engage ConversationId from the user_DR_MediaResourceID ECC variable of the Routed event, to use in subsequent nodes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/509baf37bdbf791ec806958b413b4c7c82e7a8ac6261327c99bc9d88751c9813-Queued_Flow.jpg",
        "Routed Flow.jpg",
        "Screenshot of Routed Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Routed Flow"
    }
  ]
}
[/block]


It invokes the Add Participant node to add the Agent to the existing Conversation with the customer. The customer gets intimated about the same depending on the channel on which the customer is interacting with the Contact Center.

Following are the custom variables used in the flow:-

- TaskContextVariables
- RoutedMessage
- mediaResourceID
- chatThreadID
- RoutedTimeStamp

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node.

### Closed Flow

This flow is invoked when a CCE task get closed by an Agent gracefully, or when the system ends the task abruptly owing to an error or maximum allowed queue time getting elapsed. The Digital Routing Service sends the Closed event in such cases, along with a DispositionCode that can be used to infer the reason for the task closure. For a list of Disposition Codes, refer to the CCE Features Guide.  

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ef57b94cc74885d35e69e9352e2cd86466796f4d9806229c430e8d2a9a7da94e-Closed_Flow.jpg",
        "Closed Flow.jpg",
        "Screenshot of Closed Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Closed Flow"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dfd34af814c5a1d7ce9f049ddacdd8635d2de92f89c89adfa0e213a05b87acfa-Closed_Flow_-_Part_2.jpg",
        "",
        "Screenshot of Closed Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Closed Flow"
    }
  ]
}
[/block]


The flow informs the end customer about task closure on the respective channel, depending on the media channel associated with the task.

Following are the custom variables used in this flow:-

- TaskContextVariables
- ClosedMessage
- mediaResourceID
- chatThreadID
- ClosedTimeStamp

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node.

### Transferred Flow

This flow is invoked on receipt of the Transferred event from the Digital Routing Service. An agent handling a contact, can transfer the task to other queues using the Agent desktop. The transferred event also gets triggered by the system automatically in certain scenarios like RONA (Redirect On No Answer) and Agent Logout with active tasks still in the inbox. The flow first extracts the ConversationID using an Evaluate node, and then removes the Agent as a participant in the Webex Engage platform by invoking the "Remove Participant" node.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5bed3e5f3f02aa5bb84e72b3a000771e5e2bcd71486e4e0061c400c1163147be-Transferred_Flow.jpg",
        "Transferred Flow.jpg",
        "Screenshot of Transferred Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Transferred Flow"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/efa5f827c865a695aaad60883645073c6ddf17f859ce7ca94879fc2e2358056e-Transferred_Flow_-_Part_2.jpg",
        null,
        "Screenshot of Transferred Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Transferred Flow"
    }
  ]
}
[/block]


The flow then resubmits the task to CCE using the same CCE taskId as was received in the Transferred event, using the Create Task node. It subsequently informs the end customer about the transfer having been initiated on the respective media channel. In case there are any errors while performing the transfer operations, the task is closed and the end user is informed about the failure.  

The following custom variables are used in this flow:-

- TaskContextVariables
- TransferredMessage
- mediaResourceID
- FailedTransferMessage
- errorTechnicalIssue
- chatThreadID
- TransferredTimeStamp
- CustomerName
- EmailMessageId
- EmailSubject
- SystemGenerated

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node.