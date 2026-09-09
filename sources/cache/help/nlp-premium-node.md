# NLP Premium Node

Source: https://help.webexconnect.io/docs/nlp-premium-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:56+00:00

> ❗️ Note
> 
> This node was deprecated since October 2022.

The _NLP Premium_ node provides additional intelligence modules that provide much more complex capabilities. This node gives you the power of analyzing the sentiment of your customer, detect any offensive words in the input, etc.



![NLP Premium Node](https://files.readme.io/0bf261d-nlp-premium.png)




The intelligence modules (represented as methods) available in the NLP Premium node are:

- **Sentiment Analysis** - identifies the sentiments and extracts opinions within the provided input text like attitude, brands, negation, etc.
- **Parse Tree Generation** - parses the provided input text and generates a rooted tree that represents the syntactic structure of the text.
- **Profanity Filter** - detects the offensive or abusive words within the provided input text and masks such words.

> 📘 
> 
> This node is available in Node Palette only if it has been provisioned for you.

## Node Configuration

Drag-and-drop the NLP Premium node onto the visual flow builder and double-click it to open the configuration window.

1. Select the required **Method Name** from the drop-down list.



![Screenshot of NLP Premium configuration page.](https://files.readme.io/37ed330-nlp-premium-config.png)




2. Enter the message body (for a static message) or type the variable name (for a dynamic message) in the **Input Text** field.



![Screenshot of Selecting Sentiment Analysis method.](https://files.readme.io/de983a0-nlp-premium-input-text.png)




3. Enter the **MSISDN** if the selected method is _Profanity Filter_.
4. Click **Save** to complete the configuration.

## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](https://help.imiconnect.io/docs/creating-a-custom-variable-on-imiconnect).

## Output Variables

You can see the data that this node generates as output variables. These variables are available for use in subsequent nodes. The standard output variables for the _NLP Premium_ node vary based on the selected method.



| Method | Output Variable(s) |
| --- | --- |
| Sentiment Analysis | > _ **Library** - contains the library from which sentiment analysis is done  <br>> _ **Sentiment** - contains the sentiment of the provided input text |
| Parse Tree Generation | > - **Parse Tree** - contains the parsed tree of the provided input text |
| Profanity Filter | > - **Filtered Message** - contains the message that has been obtained after filtering out any offensive or abusive words |






![Output Variables](https://files.readme.io/f1c6be1-nlp-premium-output-variables.png)




## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.



| Node Edge | Node Event/Outcome |
| --- | --- |
| Success (green)<br>  <br>  <br>**Note**: You can see this node edge only when you complete the node configuration. | - **onSuccess** - the flow exits through this node when the input text is processed successfully |
| Timeout (yellow/amber) | - **onTimeout** - the flow exits through this node outcome when the input is timed out |
| Error (red) | _ **onFailure** - the flow exits through this node outcome when the input text is not processed successfully  <br>_ **onError** - the flow exits through this node outcome when there is an error  <br>_ **onInvalidData** - the flow exits through this node outcome when the input text is invalid data  <br>_ **onInvalidChoice** - the flow exits through this node outcome when the input text contains an invalid choice |




## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](https://help.webexconnect.io/docs/transition-actions).