Use a QnA Bot Node where the interactions with users are restricted to answering specific queries from a corpus or knowledge-base with minimal turn-taking involved.

Drag-and-drop the QnA Bot node on to the visual flow builder. This node helps you to leverage QnA bots configured within the Bot Builder app to automate response handling for frequently asked questions using a corpus of knowledge articles.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cefe1b5-image.png",
        null,
        "Screenshot of QnA bot Node"
      ],
      "align": "center",
      "sizing": "200px",
      "caption": "QnA bot Node"
    }
  ]
}
[/block]


> 📘 Node version
> 
> It's recommended to use the newest/latest available version of the node to access all the features.

## Methods and Outcomes

The QnA bot node contains two methods - Process message (to get a response from the bot) and Close session (to end the bot session)

### Method Name - Process Message

This is the main method in QnA bot node. Using this, developers can send the user messages to selected bot and get bot responses back. Here are the input variables for configuring the node:

[block:parameters]
{
  "data": {
    "h-0": "Input fields",
    "h-1": "Description",
    "0-0": "Bot",
    "0-1": "The bot that will be used to process the user message and get a response.  \n**Users will only be able to see the bots that they have access to in the bot builder.** [More information on managing bot builder users and the bots they access to.](https://help.imiconnect.io/docs/enteprise-profile-settings#managing-teammates)",
    "1-0": "Message",
    "1-1": "The variable name that contains the incoming customer message to be sent to the selected bot.",
    "2-0": "Language",
    "2-1": "If the selected bot is multi-lingual, you can select the language of incoming message in the Language dropdown. The dropdown list is populated based on languages in bot settings.  \nFor bots with a single language, this dropdown is disabled.",
    "3-0": "Channel",
    "3-1": "Name of the channel that the user's message is received from.",
    "4-0": "User identifier",
    "4-1": "Next to the channel dropdown, the name of the field changes based on channel selected. User's unique identifier for the selected channel should be provided here.",
    "5-0": "Customer Parameters (Optional)",
    "5-1": "Additional information about the customer can be passed to the bot builder as a key value pair. This is information is associated with the user's profile in Bot builder and can be used for later conversations. For example, you can specify whether a user is a new customer or existing customer.  \nKeys passed as 'Customer parameters' are accessible as ${consumerData.extra_params.\\<your_key>} in bot builder.",
    "6-0": "Message Parameters (Optional)",
    "6-1": "Additional information about the current exchange can be passed to the bot builder as a key value pair. This message is not stored and is only available for use in the next bot response.  \nKeys passed as 'Message parameters' are accessible as ${extra_params.\\<your_key>} in bot builder."
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/460fd78-1.jpg",
        null,
        "Screenshot of Node configuration for Process Message method."
      ],
      "align": "center",
      "border": true,
      "caption": "Node configuration for Process Message method"
    }
  ]
}
[/block]


**Output variables**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c55ecb4-image.png",
        null,
        "Screenshot of Output Variables."
      ],
      "align": "center",
      "sizing": "300px",
      "caption": "Screenshot of Output Variables."
    }
  ]
}
[/block]


Output variables of the 'Process Message' method in QnA bot node:

- **TextResponse** - the text output configured within Bot; works only if no other type of  
  rich/special elements are present. Also for multiple text items in the response, returns the first one.
- **FullResponse** - the full response with all rich elements and multiple messages present in the output from bot. Sends information as an array.
- **Datastore** - a JSON/dict of all user-defined sessions variables within the bot.
- **Article** - the name of the top article identified from the user’s message.
- **TransactionId** - the transaction id for the request in bot builder.
- **SessionId** - the session/conversation id in bot builder.
- **ConsumerId** - the customer id in bot builder.
- **PotentialArticles** - a list of articles which closely matched with the user’s message.
- **AgentHandover** - when the bot wants to handover the chat to an agent, the handover flag changes to true when bot requests for agent handover, else false.
- **CategoryName** - category name of the top article identified from the user’s message.
- **LiveChatRichResponse** - Transformed payload for quick replies and carousels that can be used in In-app nodes used of live chat channel.
- **PreviousIntent** - the article that was detected for the previous user message in the same session. Null for first user message in a session.
- **ResponsePayload** - the complete response payload from bot builder. 

### Method name - Close Session

This method can be used to close a session in the bot builder. If the flow logic demands that the bot session should be closed and future messages from the user should go to a new bot session, developers can use this method to close the existing session. For example, when the receive node times out, flow developers can close the bot session to ensure that a new session is initiated for the next user message.

Input variables for configuring the node:

[block:parameters]
{
  "data": {
    "h-0": "Input fields",
    "h-1": "Description",
    "0-0": "Bot",
    "0-1": "The bot that will be used to process the user message and get a response.  \n**Users will only be able to see the bots that they have access to in the bot builder.** [More information on managing bot builder users and the bots they access to.](https://help.imiconnect.io/docs/enteprise-profile-settings#managing-teammates)",
    "1-0": "Session ID",
    "1-1": "The bot builder session that should be closed. Session ID is available as an output variable of the **Process message** method."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e597abb-2.png",
        null,
        "Screenshot of Node configuration for Close Session method."
      ],
      "align": "center",
      "border": true,
      "caption": "Node configuration for Close Session method"
    }
  ]
}
[/block]


### Node outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit **(pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node. Each QnA node corresponds to a node outcome.

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Error (Red)",
    "0-1": "**onError** - when the bot has not responded with a message  \n**onInvalidCustomerID** - when customer identifier is missing  \n**onInvalidMessage** - when message value is missing",
    "1-0": "Success (green)",
    "1-1": "**onSuccess** - when the bot responds with a message  \n**onAgentHandover** - when the bot raises a request to handover to the agents",
    "2-0": "Timeout (yellow/amber)",
    "2-1": " **onTimeOut** - when the bot has not responded in not more than 15 seconds"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Node versions

Following versions are currently available in the node 

| Version | Description/Enhancements                                                               |
| :------ | :------------------------------------------------------------------------------------- |
| v1.3    | Fixed a bug in v1.2 where _onAgentHandover_ was not triggered at the time of handover. |
| v1.2    | Renamed channel names and customer identifiers.                                        |
| v1.1    | Base version - replica of native bot nodes.                                            |