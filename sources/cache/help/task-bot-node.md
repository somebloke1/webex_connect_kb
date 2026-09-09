# Task Bot Node

Source: https://help.webexconnect.io/docs/task-bot-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:57+00:00

Use a Task Bot node to enable multi-turn conversations where a bot can obtain relevant data from users to perform the task at hand.

Task bot gathers information, executes tasks, and integrates them with systems using a conversational bot with a set of intents and entities.



![Task bot Node](https://files.readme.io/e9e6f4f-image.png)




> 📘 Node version
> 
> It's recommended to use the newest/latest available version of the node to access all the features.

## Methods and Outcomes

The Task bot node contains two methods - Process message (to get a response from the bot) and Close session (to end the bot session)

### Method Name - Process Message

This method in used to send user messages to the selected Task bot and get bot responses back. Here are the input variables for configuring the node:



| Input fields | Description |
| --- | --- |
| Bot | The bot that will be used to process the user message and get a response.  <br>**Users will only be able to see the bots that they have access to in the bot builder.** [More information on managing bot builder users and the bots they access to.](https://help.imiconnect.io/docs/enteprise-profile-settings#managing-teammates) |
| Message | The variable name that contains the incoming customer message to be sent to the selected bot. |
| Channel | Name of the channel that the user's message is received from. |
| User identifier | Next to the channel dropdown, the name of the field changes based on channel selected. User's unique identifier for the selected channel should be provided here. |
| Customer Parameters (Optional) | Additional information about the customer can be passed to the bot builder as a key value pair. This is information is associated with the user's profile in Bot builder and can be used for later conversations. For example, you can specify whether a user is a new customer or existing customer.  <br>  <br>Keys passed as 'Customer parameters' are accessible as ${consumerData.extra_params.\<your_key>} in bot builder. |
| Message Parameters (Optional) | Additional information about the current exchange can be passed to the bot builder as a key value pair. This message is not stored and is only available for use in the next bot response.  <br>  <br>Keys passed as 'Message parameters' are accessible as ${extra_params.\<your_key>} in bot builder. |






![Task bot node configuration](https://files.readme.io/2d403a1-image.png)




**Output variables**



![Screenshot of Output Variables.](https://files.readme.io/c43928c-image.png)




Output variables of the 'Process Message' method in Task bot node:

- **TextResponse** - the text output configured within Bot; works only if no other type of  
  rich/special elements are present. Also for multiple text items in the response, returns the first one.
- **FullResponse** - the full response with all rich elements and multiple messages present in the output from bot. Sends information as an array.
- **Datastore** - a JSON/dict of all user-defined sessions variables within the bot.
- **TemplateKey** - name of the template key (in Responses section of the Task bot) for the response returned by the bot.
- **TransactionId** - the transaction id for the request in bot builder.
- **SessionId** - the session/conversation id in bot builder.
- **ConsumerId** - the customer id in bot builder.
- **PotentialIntents** - a list of top 3 intents which closely matched with the user’s message.
- **AgentHandover** - when the bot wants to handover the chat to an agent, the handover flag changes to true when bot requests for agent handover, else false.
- **Intent** - name of the Intent detected for the user's message.
- **Entities** - list of entities collected for the active intent.
- **LiveChatRichResponse** - Transformed payload for quick replies and carousels that can be used in In-app nodes used of live chat channel.
- **PreviousIntent** - the article that was detected for the previous user message in the same session. Null for first user message in a session.
- **ResponsePayload** - the complete response payload from bot builder. 

### Method name - Close Session

This method can be used to close a session in the bot builder. If the flow logic demands that the bot session should be closed and future messages from the user should go to a new bot session, developers can use this method to close the existing session. For example, when the receive node times out, flow developers can close the bot session to ensure that a new session is initiated for the next user message.

Input variables for configuring the node:



| Input fields | Description |
| --- | --- |
| Bot | The bot that will be used to process the user message and get a response.  <br>**Users will only be able to see the bots that they have access to in the bot builder.** [More information on managing bot builder users and the bots they access to.](https://help.imiconnect.io/docs/enteprise-profile-settings#managing-teammates) |
| Session ID | The bot builder session that should be closed. Session ID is available as an output variable of the **Process message** method. |






![Node configuration for the Close Session method](https://files.readme.io/9fa2a28-image.png)




### Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit **(pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node. Each FAQ corresponds to a node outcome.



|  |  |
| --- | --- |
| Error (Red) | _ **onError** - when the bot has not responded with a message  <br>_ **onInvalidCustomerID** - when customer identifier is missing  <br>\* **onInvalidMessage** - when message value is missing |
| Success (green) | _ **onSuccess** - when the bot responds with a message  <br>_ **onAgentHandover** - when the bot raises a request to handover to agents |
| Timeout (yellow/amber) | \* **onTimeOut** - when the bot has not responded in more than 15 seconds |




### Node versions

Following versions are currently available in the node 

| Version | Description/Enhancements                                                               |
| :------ | :------------------------------------------------------------------------------------- |
| v1.4    | Addition of Google Business Messages as a Channel.                                     |
| v1.3    | Fixed a bug in v1.2 where _onAgentHandover_ was not triggered at the time of handover. |
| v1.2    | Renamed channel names and customer identifiers.                                        |
| v1.1    | Base version - replica of native bot nodes.                                            |