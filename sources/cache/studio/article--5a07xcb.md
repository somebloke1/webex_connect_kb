# Multi-agent orchestration

Source: https://help.webex.com/article/5a07xcb
Documentation version: not specified by publisher
Source last modified: 2026-05-26T12:14:04.495Z
Retrieved: 2026-09-08T23:48:49+00:00

<a id="content"></a>

<a id="concept-template_c583a7c5-84e6-43bf-a9a3-69d1855f1b08"></a>

The custom transfer action feature enables you to transfer calls from one AI agent to another AI agent, to a human agent, or to any another desired destination (voicemail box, hunt group, or any number) to ensure seamless customer experience. By using a transfer action, you exit out of the escalated path of the Virtual Agent V2 Activity in Flow Builder with metadata that allows you to orchestrate the next path in the conversation. See the following sections for more details.

Some business scenarios require the AI agent to announce the transfer so the customer knows what is happening. In other scenarios, using transfer-related language can be confusing or undesirable.

Based on your need, you can configure the transfers as:

- **Announced transfer**: AI agent clearly informs the customer about an upcoming transfer (for example “Let me transfer you to a billing specialist”).

- **Silent transfer**: AI Agent performs the transfer silently without mentioning it to the customer. In these scenarios, the AI agent uses neutral language (for example "Let me take care of that", "Please hold on a moment while I process your request").

See the following sections for details.

<a id="task-template_f456c185-ae1e-457c-b33d-8663eb3a3cba"></a>

## Announced transfers

Before you begin

Ensure to create multiple agents for a complex task.

|  |  |
| --- | --- |
| 1 | **Create an action:**<br> <br>- Define a transfer action with your specific transfer condition.<br>- Turn on the Announce Transfer toggle option to enable the announcement.<br>  <br>   <br>  <br>  See the [Configure a custom transfer action](https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_91018ba5-7914-4ad9-938f-f8837f776f8c) section in the Webex AI Agent Studio Administration Guide for step-by-step instructions. |
| 2 | **Route the interaction using a flow:**<br> <br>Once the flow regains control, route the interaction to a human or another AI agent. Use the metadata from the Virtual Agent V2 activity to identify the specific transfer trigger. You can use `$.escalation_trigger`. For more details, see the [Use AI agents for customer interactions](https://help.webex.com/en-us/article/s0qro1/Use-AI-agents-for-customer-interactions) article. |
| 3 | **Configure Voice:** Because the caller is aware of the transition, it is recommended to set a distinct voice using the `Global_VoiceName` variable. For more details see the [Supported languages and voices for AI agents](https://help.webex.com/en-us/article/pdef2d/Supported-languages-and-voices-for-AI-agents) article. |
| 4 | **Data Sharing:** Conversation history is shared automatically. You may optionally pass additional information using the custom data field. |

<a id="task-template_2ec39965-15bf-4891-8073-3cd31afc018b"></a>

## Silent transfers

Before you begin

Ensure to create multiple agents for a complex task.

|  |  |
| --- | --- |
| 1 | **Create an action:**<br> <br>- Define a transfer action with your specific transfer condition.<br>- Turn off the Announce Transfer toggle option to disable the announcement.<br>  <br>   <br>  <br>  See the [Configure custom transfer action](https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_91018ba5-7914-4ad9-938f-f8837f776f8c) section in the Webex AI Agent Studio Administration guide for step-by-step instructions. |
| 2 | **Route the interaction using a flow:**<br> <br>When the flow regains control, route the interaction to a human or another AI agent. Use the metadata from the Virttual Agent V2 activity to identify the transfer trigger. You can also use the `$.escalation_trigger`. For more details, see the [Use AI agents for customer interactions](https://help.webex.com/en-us/article/s0qro1/Use-AI-agents-for-customer-interactions) article. |
| 3 | **Configure the Welcome Message:**<br> <br>Perform the following configuration in the State Event setting of the Virtual Agent V2 activity. Ensure **dynamic_welcome_message** is set to True for the receiving agent to skip the static welcome prompt.<br>![](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/495889.png) |
| 4 | **Configure Voice:**<br> <br>To maintain a seamless experience, it is recommended to use the same voice for the receiving agent using the `Global_VoiceName` variable. For more details, see the [Supported languages and voices for AI agents](https://help.webex.com/en-us/article/pdef2d/Supported-languages-and-voices-for-AI-agents) article. |
| 5 | **Data Sharing**: Conversation history is shared automatically. You may optionally pass additional information using the custom data field. |

<a id="concept-template_5afe054a-9a6f-4387-876e-2fffe04cf18c"></a>

## Best practices when creating transfer actions

See the following best practices when creating transfer actions:

- **Modularity**: Use actions to keep your logic clean by separating specialized tasks into dedicated agents.
 
- **Metadata**: Always leverage VAV2 activity metadata to define the routing logic.
 
- **Consistency**: When performing silent transfers, maintaining the same voice profile helps ensure the caller perceives the interaction as a continuous experience.
 
- **Define agent roles in transfer condition**: Treat the transfer condition as an action description. When configuring your multi-agent setup, focus on the specific function of the receiving agent rather than the act of transferring. For example, describe the agent by its capability, such as a 'Booking Agent' that handles tasks like booking, canceling, or rescheduling appointments. This provides clearer context for the LLM.
