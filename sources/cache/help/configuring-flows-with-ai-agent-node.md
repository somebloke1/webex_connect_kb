# Configuring flows with AI Agent Node - WXCC

Source: https://help.webexconnect.io/docs/configuring-flows-with-ai-agent-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:45+00:00

Webex Connect offers a rich and intuitive AI Agent Studio to configure agents to automate responses to standard customer queries and configure Task bots to fulfil customer requests without manual intervention. 

The description below covers how you can use bots configured using Webex Connect Bot Builder within the visual flow builder to automate handling of customer requests before escalating it to Webex Contact Centre agents, if needed.

## FBM Inbound Message Flow with bot nodes

### Use case description

You can direct the user queries to a chatbot built using imconnect bot builder by using QnA Bot and Task Bot nodes within the visual flow builder . If the bot isn’t able to resolve the user query and there is a need for escalation, the chat can easily be handed over to a Cisco Webex Contact Center agent. In case of an agent handover, a transcript of the conversation between user and bot until the point of handover is also available to the agent for enabling contextual customer support. 

In this below example, the bot arranges a call back for customers who wish to open a new account and posts this information to a CRM system.

### Understanding Flow Logic

Taking ‘FBM Inbound’ flow from Webex Contact Center flow templates as reference, the initial part of the flow remains the same as the standard FBM Inbound Message Flow. On receiving an inbound message on Facebook Messenger, the Search Conversation node searches for an existing conversation using customer's Facebook Messenger PSID. 



![Source screenshot](https://files.readme.io/5c591c0-Picture3.png)




**Conversation active, in queue or on hold**

- If a conversation already exists in active, queued or on-hold state, this signifies that the user has invoked the same flow before and is already in touch with an agent. In this case (top branch in the flow after Search conversation), the append conversation node is used to append new messages to the existing chat of the customer.

**No conversation found**

- In cases where no conversation is found for a user, the Create Conversation node is used to create a new conversation. On conversation creation, the Create Task node is used to create a task in Webex Contact Center. Instead of queueing the task directly, the conversation goes to the configured bot to handle customer queries. In the example flow, a Task bot node is used after the task is created. A Q&A bot node can also be used interchangeably depending on the bot use case. 



![Source screenshot](https://files.readme.io/35ab2fe-Task.jpg)




- The task bot node is configured by selecting the appropriate bot from the dropdown, providing the message to be forwarded to the bot (in this case, a custom variable ‘**messagetext**’ that is created using the incoming message in the initial inbound Facebook Messenger node), and providing customer details. 



![Source screenshot](https://files.readme.io/b1f467f-Messenger.jpg)




- The subsequent branch node is used to check if certain conditions are met by the bot and proceed accordingly. In this flow, it checks if the user has provided all the details required for requesting a call back. If so, the collected entities are parsed using a data parser node and passed to the CRM using an HTTP node (top green branch of the bot loop). The input to Data Parser should be task bot node’s output variable ‘**taskbot.entities**’. A sample JSON body for entities can be downloaded from Sessions in the bot builder by opening a session, selecting a transaction where all the entities are available and downloading the transaction info from the right. 



![Part of the flow responsible for branching based on conversation state](https://files.readme.io/bfe483d-Picture4.png)






![Extracting entity values using Data Parser node](https://files.readme.io/bf6046a-Picture5.png)




If not all the required entities are present, the flow continues through the ‘None of the above’ branch.

- In either of the above scenarios, the bot response is sent to the user using the Messenger channel node. The same message is logged in the conversation using the Append Conversation node that follows the Messenger node.

- A Receive node is used to get the user message. In this receive node, the ‘messagetext’ variable defined in the inbound Facebook Messenger node is updated with the newly received user message. This is again appended to the existing conversation using the Append Conversation node. If no message is received from the user, the conversation and the task are closed after a predefined period of time (onTimeout edge of receive node branch in the flow).

- If the conversation is successfully appended, the Task bot node is invoked again. This loop continues until the user stops responding and the receive node times out or if the Task bot node initiates an agent handover. The handover is triggered if the user explicitly asks for it or using certain rules in the bot builder.

- When an agent handover is initiated, a Queue Task node is used to queue the active task in Cisco Webex Contact Center for an agent allocation.

## Conversation closed

- If a conversation exists in closed state, it is re-opened using the Re-Open Conversation node. The incoming message is then appended to this conversation using Append Conversation node. From here, the flow proceeds in the same way as the above scenario.

- In both the scenarios (No conversation found and Conversation closed) – the flow ends once the task is successfully queues or if the user query is closed when the customer stops responding without needing an agent handover.

## Processing bot response

- Bot nodes’ output variables contain two different variables for bot responses – ‘bot.text_response’ and ‘bot.full_response’. In cases where the bot’s response is text only, ‘bot.text_response’ can be used directly in the ‘Message’ field of Messenger node. For cases where a rich response containing templates other than text is configured for the bot, a Data Parser node has to be used to parse ‘bot.full_response’ before using the Messenger channel node. For example, if the bot response contains quick replies, ‘bot.full_response’ has to be provided as input to the Data Parser node to extract button titles and payloads. 



![Extracting quick reply button titles and payloads along with text response](https://files.readme.io/52d1cdc-Picture6.png)




- A sample JSON body for rich responses can be downloaded from Sessions in the bot builder by opening a session, selecting a transaction where a rich response is sent out, and downloading the transaction info from the right. The extracted values for text, button titles and payloads is used in the Messenger node to deliver the response to users. 



![Using the values extracted from Data Parser in Messenger node](https://files.readme.io/e52401f-Messenger1.jpg)




The method for delivering other rich messages remains the same, where relevant values are extracted from the data parser node and delivered using Messenger channel node by selecting the appropriate Message Type

## Livechat Inbound Message Flow with bot nodes

For the Livechat Inbound Message flow, sequence, and logic largely remain the same as Messenger 

![](https://files.readme.io/a4090db-Picture8.png "Picture8.png")

The major differences are:

- For using a pre-chat form, an In-app Messaging node in conjunction with Receive node should be used before the Create conversation node. When using a pre-chat form, the Message Type in the in-app Messaging node should be ‘Form’ and the relevant Form Template can be selected.



![Using a pre-chat form through In-app Messaging node](https://files.readme.io/2798237-Picture9.png)




- The values collected in the pre-chat form are accessible from the receive node that follows it. The Event name in the Receive node should be ‘Form Response’ and the same template that was selected in the previous node has to be selected.
- The values collected in the pre-chat form can be used throughout the flow to branch to different bots or queues, or to use these values inside bot responses. If these values are sent to bot, they can be used in the bot response designer using [variable substitution](https://help.imiconnect.io/docs/response-designer#variable-substitution-in-responses). A list of all variables that can be used is available [here](https://help.imiconnect.io/docs/response-designer#section-conditional-response) 



![Using Name and Email values collected in pre-chat form and sending them to the bot as Customer Parameters](https://files.readme.io/a33b529-QnA.jpg)




- Rest of the flow remains the same as Inbound Message flows for other channels.