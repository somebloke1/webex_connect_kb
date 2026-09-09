# Cisco ECE Integration - Deprecated

Source: https://help.webexconnect.io/docs/cisco-ece-integration-deprecated
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:11+00:00

> ❗️ Deprecation Alert
> 
> Please note that the below integration has been deprecated.

**_Enterprise Chat and Email (ECE)_** is an offering from Cisco CCE suite that allows customer support agents to respond to customer queries/tickets in real-time on webchat and email.<br>  
The Enterprise Chat and Email APIs provide partners & customers with a powerful way to interact with the ECE resources like a _case_, _activity_, or _customers_ using the standard HTTP methods (GET, PUT, POST, and DELETE). You can use these APIs for many purposes such as including modern web applications as well as integrating the platform with other applications.<br>  
Webex Connect chat engine offers a pre-built connector to integrate with Cisco ECE and enable customer support over digital messaging channels such as SMS, Apple Messages for Business, and WhatsApp.

## Channel Support

Webex Connect's Cisco ECE Integration supports the following channels:

- Apple Messages for Business
- In-app Messaging
- Messenger 
- WhatsApp
- SMS

## Capabilities

The key capabilities of the Cisco ECE Integration within Webex Connect are as follows:

- Enable customer support over telco, digital messaging, and social channels through Cisco ECE
- Enable customers and agents to share attachments during a conversation  
  Channel-specific limitations related to the type and format of attachments apply. Attachments are sent in one of the following ways:
  - Attachment is available online and is sent as downloadable content through a URL
  - Attachment is sent in the native file format.
- Notify agents about the customer-related events such as:
  - <code>Customer started/stopped typing</code>
  - <code>Customer uploaded attachment</code>
  - <code>Customer accepted attachment</code>
  - <code>Customer rejected attachment</code>.

> 📘 The events may vary based on the communication channel.

- Notify customers about agent-related events such as:
  - <code>Agent started/stopped typing</code>
  - <code>Chat started</code>
  - <code>Chat assigned</code>
  - <code>Chat transferred</code>
  - <code>Chat closed</code>
  - <code>Agent uploaded attachment</code>
  - <code>Agent accepted attachment</code>
  - <code>Agent rejected attachment</code>.

> 📘 The events may vary based on the communication channel.

- Capture channel-specific customer details such as mobile number in case of SMS, or _user name_ and _locale_ in case of Messenger
- Trigger pre-chat and post-chat flows on Webex Connect from Cisco ECE
  - Examples of pre-chat flows include customer identity and verification before handing over the chat to the agent
  - Examples of post-chat flows include customer satisfaction surveys or feedback forms.
- Chatbot integration for customer self-service  
  Enable customer self-service over supported channels by integrating Webex Connect with Bot or any other third-party chatbot with a seamless handover from chatbots to live agents on Cisco ECE when human intervention is needed.
- Automated Language detection  
  Webex Connect supports automatic language detection and routing of messages to relevant teams on the Cisco ECE.
- System messages  
  The chat engine allows you to configure additional messages that can be automatically sent to the customers, like the welcome message, chat transferred from one agent to another.

## Integrate Cisco ECE with Webex Connect

To set up a Cisco ECE integration in Webex Connect:

1. Sign in to Webex Connect with your credentials.
2. Navigate to **Assets** > **Integrations** on the left navigation bar.



![List of Integrations](https://files.readme.io/5e17adc-CiscoECE.jpg)




3. Click **Add Integration** and select the **Cisco ECE** option.
4. Enter a suitable **Name** for the integration.
5. Select the required **Version** of the Cisco ECE connector.
6. Enter **Authentication Details** for the integration.
   - **Base URL**: this URL lets you connect to the Cisco Finesse Chat console. Obtain this URL from Cisco Finesse.
   - **User Name**: username used to login to the Cisco Finesse chat console
   - **Password**: password used to login to the Cisco Finesse chat console.



![Authentication Details](https://files.readme.io/cd70545-ece_authentication_details.png)




7. Provide details for **Entry Point Configurations** (an entry point is an agent or a group of agents in Cisco Finesse):
   - **Name** – a suitable name for the entry point.
   - **Cisco Entry Point ID** – a unique identifier of the entry point. Obtain this from Cisco Finesse.  
     When multiple agents keep signing in and out of the Cisco Finesse chat console, the status of the agents' changes. In such cases, the **Refresh** icon allows you to refresh the status of the agent and view the current status.



![Entry Point Configurations](https://files.readme.io/7a75b37-entry_point_configs.png)




   The following icons provide details about the agent:

| <p>Icon</p>   | <p>Description</p>                                                                                                                                                                                                                                                                                                   |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Agent</p>  | <p>Indicates whether an agent can accept new chats or is busy:</p><blockquote><ul><li>Red – indicates that the agent is busy and cannot accept pick up any chat</li><li>Green – indicates that the agent is ready to accept the chat</li></ul></blockquote>                                                          |
| <p>Depth</p>  | <p>Indicates whether the maximum number of chats that an agent can handle concurrently has been reached:</p><blockquote><ul><li>Red – indicates that the agent is out of capacity</li><li>Green – indicates that the agent can pick up a chat</li></ul></blockquote>                                                 |
| <p>Wait</p>   | <p>Indicates whether the waiting time for the customers before an agent picks up the chat is within an acceptable range or not: </p><blockquote><ul><li>Red – indicates that wait time is out of acceptable range</li><li>Green – indicates that the wait time is within the acceptable range</li></ul></blockquote> |
| <p>Status</p> | <p>Indicates the availability status of the agent: </p><blockquote><ul><li>Red – offline</li><li>Green - online</li></ul></blockquote>                                                                                                                                                                               |

8. Configure the set of messages that appear to the customer when certain events are triggered. This is an optional step.



![Configure Messages](https://files.readme.io/9e49169-messages_for_events.png)




   You can configure the following messages:

> - **Welcome/Chat Started** - a welcome message that appears when a customer starts the chat
> - **Agent Closed Chat** - a message that appears when the agent closes/ends the chat
> - **Agent Assigned** - a message that appears when an agent is assigned to the chat
> - **Agent Transfer Queue** - a message that appears when an agent transfers the chat back to the queue
> - **Agent Transfer Agent** - a message that appears when an agent transfers the chat to another agent
> - **Agent Rejected Attachment** - a message that appears when the agent rejects an attachment sent by the customer
> - **Agent Accepted Attachment** - a message that appears when the agent accepts an attachment sent by the customer
> - **Unavailable – No agents** - a message that appears when no agents are available
> - **Unavailable – Entry point disabled** - a message that appears when an entry point is disabled.

9. Click **Add Entry Point** and repeat the above steps to add other entry points to the integration. This is an optional step.  
   You can add entry points in scenarios where multiple entry points are associated with a single Cisco ECE integration in Webex Connect.
10. Use **Custom Attributes** to map channel attributes with integration attributes. For example, to map Facebook username to the Messenger username, enter <code>$(fb.username)</code> in the **Name** field and <code>$(messenger.username)</code> in the **Value** field. Click **Add Custom Attribute** to map the required attributes. This is an optional step.



![Custom Attributes](https://files.readme.io/2f4c506-CustomAttributes.jpg)




11. Click **Save** to test and save the integration.  
    This step verifies if Webex Connect can connect to Cisco Finesse chat console and retrieve an access token successfully. An error message appears for any connection issues.

## Use the Cisco ECE Integration

Once you’ve integrated Cisco ECE with Webex Connect, you can test the end-to-end experience from receiving a customer message through any of the supported channels to facilitating a two-way chat communication between an agent and the customer by following the below steps:

1. Integrate Cisco ECE with Webex Connect.
2. Configure the channels that you want to use with Cisco ECE.
3. Create a new service in Webex Connect to use this integration.
4. Map the Cisco ECE Integration as a CCSP endpoint within the service. Define logic to route the customer messages to CCSP in one of the following ways:
   - [Create a rule](https://help.webexconnect.io/docs/rules) to forward the customer messages to Cisco ECE.
   - [Create a flow](https://help.webexconnect.io/docs/flows-introduction#section-creating-a-flow) that uses the CCSP (Create Chat and Validate Chat) nodes. Publish the flow and then launch it.

When a customer sends a message through the configured communication channel, the message reaches the agents on Cisco ECE. When an agent responds, Cisco ECE notifies Webex Connect of any outbound messages that need to be sent to the customers. Based on the conversation object, Webex Connect automatically detects the original channel and pushes messages to the customer on that channel.

## Use Cisco ECE Integration for Customer Support over Messenger

In this sample tutorial, you can see how to integrate Messenger to Cisco ECE through Webex Connect chat engine to allow direct communication between an agent and a customer.

1. Create a Cisco ECE integration with the name _MyCiscoECEIntegration_. For more information, see the [Integrate Cisco ECE with Webex Connect](#section-integrate-cisco-ece-with-imiconnect) section.
2. Create a Messenger asset.  
   a. Go to **Assets** > **Apps** > **Configure New App** and select **Messenger**.  
   b. Enter the name as _MyCiscoECEFBMessenger_.  
   c. Click **Add Messenger Page** and select the _Cisco ECE Integration_ or any other relevant page from your Facebook account. This is the page that you created previously created in your Facebook account.

> 📘 Add Messenger Page
> 
> You can add only the pages that you have created.



![Add Messenger Page](https://files.readme.io/398dc90-create_messenger_app.png)




For more information, see [Creating a Messenger App](https://help.webexconnect.io/docs/facebook-messenger#section-creating-a-facebook-messenger-messenger-app).

3. Create a service to route incoming customer inquiries from Facebook messenger account to Cisco ECE.  
   a. Create a new service with the name _MyCiscoECEService_.  
   b. Go to the **Rules** tab and click **Add New Rule**.  
   c. Select **Messenger** as the channel, _Incoming Message_ as the event, and _MyCiscoECEFBMessenger_ as the Facebook Messenger. Click **Next**.



![Select Event](https://files.readme.io/097fc52-rule_select_event.png)




d. Select **Forward to CCSP** as the action, _MyCiscoECEIntegration_ as the integration, and the entry point, which you have configured while creating the integration, as the parameter. You can specify additional parameters if required.



![Select Action - Forward to CCSP](https://files.readme.io/2a7cd7f-rule_select_action.png)




e. Configure rule details like **Name**, **Start Date**, **End Date**, **Status**, and then **Save **the rule as _MyECEMessengerRule_.



![Rule Details](https://files.readme.io/e75f90a-rule_details.png)




This rule forwards all the incoming messages on Messenger to Cisco ECE directly.

## Use Cisco ECE Integration for Customer Support over SMS

In this sample tutorial, you can see how to send and receive messages to Cisco ECE chat console on the SMS channel through the Webex Connect chat engine.

1. Select _MyCiscoECEService_ on the Services Dashboard.
2. Go to the **Rules** tab and click **Add New Rule**.
3. Select **SMS** as the channel, _Mobile Originated - MO_ as the event.
4. Select the number on which you want to receive the SMS from the customer.
5. Enter the keyword that you want to associate with the number and click **Verify** to check the availability of the keyword.
6. Select **Forward to CCSP** as the action, _MyCiscoECEIntegration_ as the integration, and the entry point that you have configured while creating the integration as the parameter. You can specify additional parameters if required.
7. Add details for the rule like **Name**, **Start Date**, **End Date**, **Status**, and then **Save** the rule as _MyECESMSRule_.

This rule sends all the mobile originating message through the SMS channel (to the configured number with the defined keyword) to the Cisco ECE chat console. Webex Connect sends all the messages from Cisco ECE to the customer in the form of SMSes.

## Use Cases

This section illustrates how communication journeys look like when the agents are available/unavailable.  
##Agent Available  
In this use case, you can see the customer journey from chat initiation to chat completion.

1. A customer sends a message on the Cisco ECE Integration Facebook page through Messenger.
2. The message reaches the Cisco ECE chat console through Webex Connect and a pre-configured welcome message appears in the Messenger window. For example, <code>Thank you for contacting us. We are here to help you resolve your issue. Please be patient until an agent attends you</code>.
3. When an agent picks up the chat on Cisco ECE console, a pre-configured agent-assigned message appears. For example, <code>You are now chatting with CiscoAgent1</code>.
4. If the agent transfers the chat to another agent or queue, a pre-configured message appears. For example, <code>You have been transferred to the Network Issues queue</code>.
5. When the customer sends an attachment to the agent and if the agent accepts it, a pre-configured message like <code>The agent has accepted your attachment.</code> appears to the customer. When the agent clicks the attachment, it is downloaded. If the agent rejects the attachment, a message indicating that appears on the customer screen if configured.
6. If the agent pushes a page to the customer using _Page Push_ in the chat console, again a pre-configured message appears on the customer screen.<br>

Finally, when the agent completes the chat, a message like <code>The agent has marked your chat closed.</code> appears if configured.

## Agent Unavailable

In this use case, you can see what happens when there are no agents available to pick the customer’s chat.

1. A customer sends a message on the Cisco ECE Integration Facebook page through Messenger.
2. The message reaches the Cisco ECE chat console through Webex Connect and a pre-configured welcome message appears in the Messenger window.
3. If there are no agents available/ready to pick up the chat, a pre-configured message like <code>Sorry! There are no agents available right now to be with you. Please come back later.</code> appears to the customer.<br>

You can embed the logic into the workflow and define how to handle customer messages in such scenarios. For example, you can discard the message after a pre-defined time interval or close the chat.

_Note: This integration is available only in the cloud version of Webex Connect._