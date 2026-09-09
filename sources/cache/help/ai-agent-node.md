# AI Agent

Source: https://help.webexconnect.io/docs/ai-agent-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:08+00:00

## Prerequisites

Before integrating AI Agents into your Webex Connect flows, ensure the following prerequisites are met:

1. Configure your digital channel — Webex Connect and Webex Contact Center integration currently supports six channels, namely WhatsApp, SMS, Email, Facebook Messenger, Apple Messages for Business, and Live Chat. For more information to configure the channel assets for each of these channels, see the [Asset Configuration](https://help.webexconnect.io/docs/wxcc-channel-assset-configuration-wxcc) chapter.
2. Create a flow — Create a flow on the Webex Connect platform. For more information, see the [Create New Flow](https://help.webexconnect.io/docs/create-a-new-flow) chapter.  
   Add AI Agents to your flow   
   You can use an AI Agent node to answer specific queries based on a provided corpus or knowledge base. You can also enable multi turn conversations where the AI Agent can ask follow-up questions, understand context, and provide personalized responses.   
   Drag and drop the AI Agent node onto your visual flow builder to get started. This node provides access to both scripted and autonomous AI Agents configured within the Webex AI Agent platform. 

> 📘 Rate limits
> 
> The default rate limit for AI Agents for a tenant is 240 transactions per minute. If your traffic projections indicate a higher usage than the limit, please reach out to your account manager to increase this limit.

## Methods and Outcomes in the AI Agent node 

The AI Agent node contains two methods: 

- Process Message — to get a response from the agent  
- Close session — to end the agent session  

## Configure AI Agent node with Process Message method 

### Process Message

This action sends user messages to the selected agent and receives the agent's response. To configure input variables in the AI Agent node, refer to the following fields:  

- Agent type—The type of agent to be used in the flow — whether scripted or autonomous. 
- Agent—The agent that is used to process the user message and get a response.  

> 📘 AI Agent visibility
> 
> Users will only be able to see the agents that they have access to in the Webex AI Agent. For more information on managing Webex AI Agent users and agents, see  [Managing teammates](https://help.webexconnect.io/docs/enterprise-profile-settings#managing-teammates).

- Message—The variable name that contains the incoming customer message to be sent to the selected agent.  
- Language—If the chosen agent is multilingual, you can choose the language of incoming message from the Language drop-down list. The drop-down list is populated based on languages in agent settings. 

> 📘 Language drop-down list
> 
> This drop-down list is disabled for single-language agents.

- Channel—The name of the channel from which the user's message originated. 
- User identifier—Next to the channel drop-down list, the name of the field changes based on the chosen channel.  Provide the user's unique identifier for the chosen channel.  
- Custom Parameters (optional)—Additional information about the customer can be passed to the Webex AI Agent as a key value pair. This information is associated with the user's profile in Webex AI Agent and can be used for later conversations. For example, you can specify whether a user is a new customer or existing customer.  

> 📘 Keys in AI Agent responses
> 
> Keys passed as Customer Parameters are accessible as ${consumerData.extra_params.\<your_key>} in agent responses.

- Message Parameters (optional)—Additional information about the current exchange can be passed to the Webex AI Agent as a key value pair.  

> 📘 Message storage and keys passed
> 
> This message is not stored and is only available for use in the next agent response. Keys passed as Message Parameters are accessible as ${extra_params.\<your_key>} in agent responses.

### Output variables 

- TextResponse — the text output configured within Agent; works only if no other type of rich/special elements are present. If the Agent's response includes multiple text items, only the first one is returned.
- FullResponse — the full response with all rich elements and multiple messages present in the output from agent. Sends information as an array.  
- Datastore — a JSON/dict of all user-defined sessions variables within the agent.  
- TransactionId — the transaction id for the request in Webex AI agent.  
- SessionId— the session/conversation id in Webex AI agent.  
- ConsumerId — the customer id in Webex AI agent.  
- MessageMetadata — the metadata associated with the current response from the configured Agent.  
- SessionMetadata — the metadata associated with the session for the current response from the configured Agent.  
- ResponsePayload — the complete response payload from Webex AI agent. 

## Configure AI Agent node with Close Session method 

### Close Session

This method is used to close a session in the Webex AI Agent. In certain scenarios, it may be necessary to close an existing AI Agent session and initiate a new one. This can be achieved using a specific method within the Webex AI Agent node. For example, if a session remains inactive for a specified period, it can be automatically closed to optimize resources. The following are some of the input variables for configuring the node: 

- Agent—The agent that is used to process the user message and get a response.  

> 📘 AI Agents' visbility
> 
> Users only see the agents to which they have access to in the Webex AI Agent. For more information on managing Webex AI Agent users and agents, see  [Managing teammates](https://help.webexconnect.io/docs/user-roles-and-hierarchy#addeditdelete-teammates).

- Session ID—The Webex AI Agent session that should be closed. Session ID is available as an output variable of the Process message method.  

## Node Outcomes

You can see the list of possible node outcomes for this node. You can customize the node labels using the Edit (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node. Each AI Agent node corresponds to a node outcome. The following are the node outcomes: 

- Error (Red)—indicates one of the following:
  - onError - when the agent has not responded with a message  
  - onInvalidCustomerID - when customer identifier is missing  
  - onInvalidMessage - when message value is missing  
- Success (Green)—indicates: 
  - onSuccess - when the agent responds with a message  
  - onAgentHandover - when the agent raises a request to handover to the agents  
- Timeout (Yellow/Amber)—indicates:  
  - onTimeOut - when the agent has not responded in not more than 15 seconds