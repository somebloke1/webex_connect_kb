# Understand intents, entities, and responses in AI Agent Studio

Source: https://help.webex.com/article/sz02k8
Documentation version: not specified by publisher
Source last modified: 2026-07-16T12:38:10.244Z
Retrieved: 2026-09-08T23:48:49+00:00

<a id="content"></a>

<a id="concept-template_b4a6c683-e86e-44d4-964a-c7060230c526"></a>

## Intents

Intent is a core component of the Webex AI Agent Studio platform that enables the AI agent to understand and respond to your input effectively. It represents a specific task or action that you want to accomplish during a conversation. You can define all intents that correspond to the tasks you want to perform. The accuracy of intent classification directly impacts the AI agent's ability to provide relevant and helpful responses. Intent classification is the process of identifying intent based on your input, allowing the AI agent to respond in a meaningful and contextually relevant manner. For details on how to create intents, see [Create an intent](https://help.webex.com/article/ncs9r37/#task-template_6361ba29-ee9e-4b62-b9b5-b80cfe6652e7).

<a id="section_o21_vjm_vcc"></a>

### System intents

- **Default Fallback Intent**—An AI agent's capabilities are inherently limited by the intents that are designed to recognize and respond to. While an enterprise can't anticipate every possible question you might ask, the default fallback intent can help conversations to be on track.
  
  By implementing a default fallback intent, AI agent developers can ensure that the AI agent gracefully handles unexpected or out of scope queries, redirecting the conversation back to known intents.

  AI agent developers need not add specific utterances to the fallback intent. The agent can be trained to automatically trigger the fallback intent when it encounters known out of scope questions that might otherwise be incorrectly categorized into other intents.

  For example, in a banking AI agent, customers might attempt to inquire about loans. If the AI agent is not configured to handle loan-related inquiries, these queries can be incorporated as training phrases within the **default fallback intent**. When a customer queries about loans at any point in the conversation, the AI agent recognizes the query as falling outside of its defined intents and triggers the fallback response. This ensures a more appropriate response.

  The fallback intent:

  - shouldn’t have any slots associated with it.
  
  - must use the default fallback template key for its response.

- **Help**—This intent is designed to address customer inquiries about the AI agent's capabilities. When customers are unsure of what they can accomplish or encounter difficulties during a conversation, they often seek assistance by asking for `help.` 
  
  By default, the response for the help intent is mapped to the `Help message` template key. However, AI agent developers can customize the response or change the associated template key to provide more tailored and informative guidance.

  It’s recommended to convey the AI agent's capabilities at a high level, providing customers with a clear understanding of what they can do next.

- **Talk to an agent**—This intent enables customers to request assistance from a human agent at any stage of their interaction with the AI agent. When this intent is invoked, the system automatically initiates a transfer to a human agent. The default response template for this intent is `agent handover`. While there are no UI restrictions on changing the response template key, altering it won’t affect the outcome of the human handover.

<a id="section_a1n_npm_vcc"></a>

### Small talk intents

All newly created AI agents include four predefined small talk intents to handle common customer greetings, expressions of gratitude, negative feedback, and farewells:

- Greetings

- Thank you

- The AI agent wasn’t helpful

- Goodbye

These intents and their corresponding responses are available by default in every AI agent. However, you can customize or delete them to align with your specific use case and the desired conversational flow.

<a id="concept-template_b150cc96-f8db-484d-8cd5-e7cbbef3bb24"></a>

### Contexts

Context makes agent-customer interactions simpler and more concise. AI agent easily understands phrases like "I want to buy that" when there's enough context to identify what "that" refers to. Contexts help in achieving clarity in interactions with customers. Such expressions can be aligned with an intent if the appropriate context is provided.

To enable follow-up intents and organize ways to structure the flow of a conversation, each intent can be configured with entry context and exit context. This context variable is stored for each session and the state of this variable changes based on intents that are invoked over the course of a session.

<a id="section_t1b_th1_v2c"></a>

#### Entry context

Entry contexts control whether an intent can be matched with the end-user query based on the active context of the session. When context is present in a session, the following rules are applied for intent matching:

- An intent with entry contexts will only be matched if the active context in the session already contains all the required entry context values. In other words, the entry context of an intent must be a subset of the active context for it to be matched.

- For all intents satisfying the above rule, preference is given to intents whose input context matches the active more closely if the confidence scores for multiple intents are the same. In other words, the input context will be used for tie-breaking partial matches.

<a id="section_vsv_xh1_v2c"></a>

#### Exit context

Exit contexts control the active contexts for a session. An exit context contains the context value string and the duration of that context. When an intent is completed (all the slots are filled and the final response is invoked), the configured exit contexts for that intent become exit for their respective durations. Developers can configure a maximum of 15 exit contexts for a particular intent. An exit context can be added by pressing the enter/return key after typing the context.

<a id="concept-template_4bcc12bf-2c65-4ab7-b7bd-e63252bdfb73"></a>

## Entities

Entities are the building blocks of conversations. They are essential elements that the AI agent extracts from user utterances. Entities represent specific pieces of information, such as product names, dates, quantities, or any other significant group of words. By effectively identifying and extracting entities, the AI agent can better understand user intent and provide more accurate and relevant responses. For details on how to create an entity, see [Create an entity](https://help.webex.com/en-us/article/preview/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_5e5dea5a-2b74-4883-a52f-8b70e07671b7).

<a id="section_gsf_xqw_1dc"></a>

### Entity types

Webex AI Agent Studio offers 11 prebuilt entity types to capture various types of user data. You can also create any of the following custom entities.

**Custom Entities**

These entities are configurable and allow developers to capture use-case specific information.

- Custom list—Define lists of expected strings to capture specific data points not covered by prebuilt entities. You can add multiple synonyms against each string. For example, a custom pizza size entity.

- Regex—Use regular expressions to identify specific patterns and extract corresponding data. For example, a phone number regex, as in `123-123-8789`

- Digits—Capture fixed-length numerical inputs with high accuracy, especially in voice interactions. We use this as an alternative to Custom and Regex entity types in nonvoice interactions. For example, define a length of five to detect a five-digit account number.

- Alphanumeric—Capture combinations of letters and numbers, providing accurate recognition for both voice and nonvoice inputs.

- Free form—Capture flexible data points that are difficult to define or validate.

- Map location (WhatsApp)—Extract location data shared by you on the WhatsApp channel.

**System Entities**

| Entity name | Description | Example input | Example output |
| --- | --- | --- | --- |
| Date | Parses dates in natural language to a standard date format | “july next year” | 01/07/2020 |
| Time | Parses time in natural language to a standard time format | 5 in the evening | 17:00 |
| Email | Detects email addresses | write to me at [info@cisco.com](mailto:info@cisco.com) | [info@cisco.com](mailto:info@cisco.com) |
| Phone number | Detects common phone number | call me at 9876543210 | 9876543210 |
| Monetary units | Parses currency and amount | I want 20$ | 20$ |
| Ordinal | Detects ordinal number | Fourth of ten people | 4th |
| Cardinal | Detects cardinal number | Fourth of ten people | 10 |
| Geolocation | Detects geographic locations (cities, countries etc.) | I went swimming in the Thames in London UK | London, UK |
| Person names | Detects common names | Bill Gates of Microsoft | Bill Gates |
| Quantity | Identifies measurements, as of weight or distance | We’re 5km away from Paris | 5km |
| Duration | Identifies time periods | 1 week of vacation | 1 week |

You can edit created entities from the entities tab. Linking entities to an intent annotates your utterances with detected entities as you add them.

<a id="concept-template_9411b41f-8060-4f42-94ea-6e3ddb079298"></a>

## Responses

Responses are the messages that your AI Agent sends to customers in response to their queries or intents. You can create responses that include:

- **Text**—Plain text messages for direct communication.

- **Multimedia**—Images, audio, or video elements to enhance the user experience.

For details on how to create responses, see [Create a response](https://help.webex.com/article/ncs9r37/#task-template_336f85da-d3db-4427-b942-d5821752e630).

<a id="section_vwb_ldk_g2c"></a>

### System responses

The following pre-configured system responses are available for the scripted AI agent. You can customize the messages for the default system responses. However, you cannot delete these responses.

- Welcome message

- Response suggestion

- Partial message

- Fallback message

- Entity suggestion

- Agent handover

<a id="section_l2m_zdk_g2c"></a>

### Small-talk responses

You can customize and delete the following small-talk responses:

- Goodbye

- Greetings

- Help message

- Not helpful

- Thank you

The supported channels for which you can configure the responses are Web (default), Apple Messages for Business, Messenger, RCS, SMS, Voice, WhatsApp.

<a id="section_rdk_hwj_t2c"></a>

<a id="concept-template_2642b8de-7fd8-4ff0-a719-a02dd8a058ad"></a>

### Response designer

The response designer offers a user-friendly interface for creating responses without requiring extensive coding knowledge. The conditional responses option allows easy construction of responses for non-developers that the AI agent delivers to customers.

The response designer is designed to ensure that the user experience caters to the specific channel the AI agent is interacting with.

<a id="section_bgj_f1k_t2c"></a>

#### Supported response types for channels

In Response Designer, you can configure channel-specific responses for the intents. For more information on how to configure various response types, see the [Configure response types](https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#concept-template_86a220a2-df7a-4973-be7b-fa58dba3dce7) section. 

Table 1. Response types for channels
| Response type | Description | Supported channels |
| --- | --- | --- |
| [Text](https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#text-response-type-configuration) | Simple text replies allow multiple text boxes in one response. This setup breaks lengthy messages into manageable parts. You can add multiple response options to your responses, and the system will randomly choose one to display, ensuring dynamic interactions. | All |
| [Carousel](https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#carousel-response-type-configuration) | Rich responses consist of a single card or multiple cards displayed in a carousel format. | Web (Default), Messenger |
| [Quick Reply](https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#quick-reply-response-type-configuration) | A pre-defined response that the AI agents use to respond to customer queries swiftly. | Web (Default), SMS, Messenger, Apple Messages for Business, RCS |
| [Image](https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#image-response-type-configuration) | A multimedia response type where you can configure images by providing URLs. | Web (Default), Messenger, WhatsApp |
| [Video](https://help.webex.com/article/ncs9r37#video-response-type-configuration) | Renders videos in the preview based on the configured video URL. | Web (Default), WhatsApp |
| [Audio](https://help.webex.com/article/ncs9r37#audio-response-type-configuration) | Renders audio file by providing the audio URL. It also shows the duration of the audio message in the output. | Web (Default), WhatsApp, Webchat |
| [File](https://help.webex.com/article/ncs9r37#file-response-type-configuration) | Shows/plays the file type based on the configured File URL. | WhatsApp |
| [Reply Button](https://help.webex.com/article/ncs9r37#reply-button-response-type-configuration) | Offers quick responses from a limited set of options, such as choosing a product to return. <br>Each message is comprised of:<br>- Header - an optional field that can be 20 characters of text, image, video, or a document.<br>- Body - a mandatory text field that can contain up to 1024 characters.<br>- Footer - an optional text field allowing up to 60 characters.<br>- Buttons - maximum of 3 text buttons with a 20-character limit. | WhatsApp |
| [List Message](https://help.webex.com/article/ncs9r37#list-messages-response-type-configuration) | Presents multiple options for easy user selection, suitable for various uses like take-out menus or product catalogs. To set up a list message, fill in the 'configuration' and 'list sections' tabs. The 'configuration' screen shows the message content users will see on their devices. <br>Each message is comprised of:<br>- Header - an optional text field with a maximum of 60 characters.<br>- Body - a mandatory text field that can contain up to 1024 characters.<br>- Footer - an optional text field allowing up to 60 characters.<br>- List title - a button field with maximum of 20 characters.<br>List section consists of:<br>- Section titles - optional text field used for categorizing several rows with a maximum of 24 characters.<br>- Row title - mandatory text field that is sent as a selection choice accompanied by a radio button with a maximum of 24 characters.<br>- Row description - optional text field that provides additional context for row items with a maximum of 72 characters.<br>Configuring a list message on the platform will require an additional field: Row ID - unique identifier for each row that will help you identify the users' choice. | WhatsApp |
| [Numbered List](https://help.webex.com/article/ncs9r37#numbered-list-response-type-configuration) | Quick reply in WhatsApp is defined as Numbered list. When users pick a number from the list of items, the payload configured against the item is received. | WhatsApp |
| [List Picker](https://help.webex.com/article/ncs9r37#list-picker-response-type-configuration) | With the list picker, the AI agent shares a list of items with a customer based on the query. This allows the customer to select the items from the given options and reply with the selection. If the customer query matches partially, the AI agent responds with the intents that are close to the customer query as options. The partial match responses are rendered only for the List Picker option in the Apple Messages for Business channel. | Apple Messages for Business |
| [Time Picker](https://help.webex.com/article/ncs9r37#time-picker-response-type-configuration) | The time picker response type lets you set up time slots for booking appointments or meetings. Each section needs a title, timezone, and multiple slots. Once set up for an intent, the AI agent sends these time slots to users for them to choose from. | Apple Messages for Business |
| [Media](https://help.webex.com/article/ncs9r37#media-response-type-configuration) | This template supports attachments that are in various formats such as jpeg, mp3, mp4, png, pdf, and aac. | Apple Messages for Business |
| [Rich Link](https://help.webex.com/article/ncs9r37#rich-link-response-type-configuration) | The Rich link URL is embedded in the image or a video that is in a chat bubble. When you click this bubble, the customer is redirected to the website specified in the image or video. | Apple Messages for Business |
| [Form](https://help.webex.com/article/ncs9r37#form-response-type-configuration) | Business Forms Messages let you create complex, multi-page interactive experiences for iOS and iPadOS using a single JSON file. This feature helps businesses collect detailed customer data through an easy-to-use interface within Apple Messaging. It allows for various interactions without users having to leave the chat. | Apple Messages for Business |
| [Custom Event](https://help.webex.com/article/ncs9r37#custom-events-response-type-configuration) | Provides a control over a conversation while interacting with the scripted AI agent. | Voice |

<a id="concept-template_352cad79-2ed2-433b-a37d-658b8e003604"></a>

### List of common response variables

Use the response variables in the **Rules** section of the conditional response designer to define conditions. You can also use the response variables in the AI agent responses to personalize and enrich the agent responses. For more information on how to configure rules, see [Create a response](https://help.webex.com/article/ncs9r37#task-template_336f85da-d3db-4427-b942-d5821752e630).

Table 2. Common response variables
| Variable name | **Variable key** | Description |
| --- | --- | --- |
| Entity value | `entity.<entity-name> OR lastdfState.model_state.entities.<entity-name>.value` | Use this variable to use the value of entities collected from the users. For example, in an appointment booking use-case where we ask the user for their preferred date using an entity named ‘Date’ entity.Date returns the value provided by the user. |
| Intent | `intent OR lastdfState.model_state.intent.name` | Use this variable to return the intent that is entered by the customer. |
| Event Store | `eventStore` | Use this to access the dictionary that contains all the parameters sent in the event payload of custom events through Webex Contact Center Flow Designer. |
| Event Store Values | `EventStore.<key>` | Use this to access the values of specific keys sent in event payloads of custom events through Webex Contact Center Flow Designer. |
| Extra parameter/Message parameter value | `extra_params.<key>` | Use this to access information passed under ‘Message parameters' in the AI Agent node for scripted agents. For example, if a key ‘user_plan’ is passed in the AI agent node, it’s accessible as extra_params.user_plan. These values are persisted for one message turn only, that is, the value for the key can only be used in the response to the message that accompanied these message parameters. |
| Extra parameters | `extra_params` | Use this to access the dictionary containing all values passed under ‘Message parameters' in the AI Agent node for scripted agents. |
| Consumer data store/Customer parameters | `consumerDataStore.extra_params` | Use this to access the dictionary containing all parameters passed under 'Customer parameters' in the AI Agent node for scripted agents. |
| Consumer data store/Customer parameter values | `consumerDataStore.extra_params.<key>` | Use this to access information passed under 'Customer parameters' in the AI Agent node for scripted agents. For example, if a key ‘user_name’ is passed in the AI agent node, it’s accessible as consumerDataStore.extra_params.user_name |
| Previous intent/Last active intent | `lastdfState.previous_intent_model_state.intent.name` | Use this variable to access the name of the intent that was active in the conversation before the current intent. |
| Context array | `lastdfState.context` | Use this to access the names of all the contexts present in the conversation in the form of an array. |
| Context duration | `LastdfState.context.<context-name>` | Fetches the value of the duration of a specific context. |
| Customer UID | `consumerData.uid` | Use this variable to access the customer’s unique ID in the AI agent response conditions or content. For digital channels, the UID is configured in the flow and varies per channel. |
| Data store variable | `dataStore.<key>` | Use this variable to access custom variables stored at a session level. |
| Agent handover by rules flag | `messageStore.agent_handover_by_rules` | Use this variable to check is the conversation was handed over to a human based on any of the agent handover rules. |
| Matched template key | `messageStore.templateKey` | Use this variable to access the current response name. |
| NLP text | `nlp.text` | Use this variable to access the unprocessed customer query. |
| Processed query | `nlp.processed_query` | Use this variable to access the processed customer query. |
| Transaction id | `transaction_id` | Use this variable to access the transaction id. |

In addition to the above, there are certain other data objects that are accessible as response variables. These include messageStore, newdfState, and lastdfState that contain metadata about the agent’s response. Developers can print this in their responses to access the details and use any parameters from these dictionaries in their responses. However, in most use-cases, the variables listed in the above table are enough to build your agent.
