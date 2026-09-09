While you can always configure your own flows for handling incoming inquiries over digital messaging channels (such as SMS, Live Chat, etc.) supported by <<prodname>> and <<WebexCC>> in combination, we have provided some representative flows to provide you with a reference on how to configure such flows.

These flows are available for download [here](https://github.com/CiscoDevNet/webexcc-digital-channels). 

There are a total of 7 representative flows as listed below:

| Flow Name                | Description                                                                                                                                                                      | Additional context                                                                                         |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| FBM Inbound Message      | Handling incoming messages from end customers over Facebook Messenger                                                                                                            | This flow needs to be configured separately for each Facebook Messenger asset.                             |
| Email Inbound            | Handling incoming messages from end customers over Email                                                                                                                         | This flow needs to be configured separately for each Email asset.                                          |
| Livechat Inbound message | Handling incoming messages from end customers over Live Chat                                                                                                                     | This flow needs to be configured separately for each Live Chat asset.                                      |
| Livechat Close thread    | Handles closing messages from end customers over Live Chat and informs the Agent that the chat is closed                                                                         | This flow needs to be configured separately for each Live Chat asset.                                      |
| SMS Inbound Message      | Handling incoming messages from end customers over SMS                                                                                                                           | This flow needs to be configured separately for each SMS number/Sender ID.                                 |
| Task Routed              | Adding an agent participant to a conversation once <<prodname>> receives the Task Routed event from <<WebexCC>>                                                                  | This needs to be updated only once per Webex CC org and is applicable for all channels and channel assets. |
| Task Modified            | Adding an agent to or removing an agent from an ongoing conversation once <<prodname>> receives the Task Modified event from <<WebexCC>> (e.g., for chat transfer or conference) | This needs to be updated only once per Webex CC org and is applicable for all channels and channel assets. |
| Close Task               | Close the conversation in imiengage and the  task in <<WebexCC>> once a close task request is received from <<WebexCC>>                                                          | This needs to be updated only once per Webex CC org and is applicable for all channels and channel assets. |

> 📘 Note
> 
> Please note that we do not support appending WhatsApp Location messages to conversations. As a workaround, you must extract the latitude and longitude and provide them as plain text by generating a map URL using Google Maps or a similar service.

You can use these flows to create flows in your <<prodname>> account by using the 'Create Flow -> Upload a Flow' method under Flows Tab within a service.

To create a flow using upload a flow option:

1. Create a Service (it should be the same as the service that you mapped with <<WebexCC>> for the Messenger asset) and create a flow by importing the representative flow named _FBM Inbound Message_.
2. Click the service and navigate to Service Dashboard.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/208e992-1.jpg",
        null,
        ""
      ],
      "align": "center",
      "border": true
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
        "https://files.readme.io/6a6eb7e-Create_Flow.jpg",
        null,
        "Interface with the Choose File button highlighted, prompting users to select and upload the necessary file."
      ],
      "align": "center",
      "sizing": "500px",
      "border": true
    }
  ]
}
[/block]


8. Click **Create**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/32d424e-CISCO_WEBEX_CONTACT_CENTER__IMICONNECT_INTEGRATION_Flow_Configuration_using_Sample_Templates_Create.png",
        null,
        "Screenshot displaying the Create Flow button on the interface."
      ],
      "align": "center",
      "sizing": "450px",
      "border": true,
      "caption": "Screenshot showing Create Floe"
    }
  ]
}
[/block]


> 📘 Note
> 
> When a flow is created using an Upload Flow method, it is mandatory to **Save** the flow before proceeding further. This is required to ensure that configurations are saved correctly. As a known limitation missing this step can lead to Evaluate node script formatting getting lost.

## Configure Flows

1. Open the required flow in the flow editor.
2. Double click the pre-built <<WebexCC>> nodes one at a time and provide authorization for the concerned node.
3. Keep the Method Name as is.
4. Select Add New Authorization in the Node Runtime Authorization drop-down.  
   a. The Add new authorization pop-up window opens.  
   b. Provide a name for the authorization that appears in the Node Runtime Authorization drop-down. Click Authorize. The Cisco Webex Contact Center login page appears and you need to provide valid credentials to add the authorization.
5. Refer to the pre-built integration node documentation to configure other fields in the node. 
6. For SMS flow, click the Start Node and select incoming message as the flow trigger option. This step doesn't apply to other channels.

Repeat this process for all of the pre-built integration nodes within the flow. 

Publish your flow once you've made all the changes.

Repeat the above steps for the remaining flows.

> 📘 Note
> 
> If you create a flow or edit an existing flow it is recommended to use the "securityscaninfo variable. The securityscaninfo variables displays a combined result of PCI and malware scans.The securityscaninfo variable is backward compatible with PCI info variable. If PCI and malware are enabled for the tenant, <<prodname>> first performs a PCI scan, then a malware scan, and stores the combined result in the securityscaninfo variable. The combined result is also updated in the PCI variables, so that all existing flows that were using PCI can have malware scan enabled for them without requiring any changes to the flow.

## Understanding Representative Flows

Here's a high level overview of the logic configured in each of the representative flows:

### FBM Inbound Message Flow

When an inbound message is received on Facebook Messenger, <<prodname>> searches for the conversation. If the conversation already exists, the incoming message is appended to the existing conversation, else a new conversation is created or an existing conversation is reopened. Once a new conversation is created, a new task is created. This task needs to be queued. If it is successfully queued, the flow ends at that point. Incoming inbound event lands on the Routed flow. is also created and it is queued in Cisco Webex Contact Center for an agent allocation.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0808ded-MicrosoftTeams-image_6.png",
        "MicrosoftTeams-image (6).png",
        "Screenshot of FBM Inbound Message Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "FBM Inbound Message Flow"
    }
  ]
}
[/block]


Search Conversation, Append Conversation and Create Conversation nodes are designed for conversation handling.

Queues are configured on the Cisco Webex Contact Center portal and then mapped to the <<prodname>> tenant. You can see the list of configured queues in the Queue Task node for you to select the queue and assign an agent appropriately. Some queues have skill-based routing embedded into them. When you select a queue with skill-based routing capability, you can see on the UI that the queue routing type is skill-based routing.

You need to add/configure the skill settings:

1. Select the required skill. The skills configured in the Webex Contact Center portal appear in this drop-down list. You (flow designer) can configure how a task is allocated to an agent based on the skills. 
2. Select the required condition and value for the skill. 
3. You can add multiple skills.

If required, you can also configure skill relaxation after a certain number of steps.

1. Enable Skill relaxation.
2. Configure the Timeout, skill, skill condition, and skill value.  
   You can add multiple skill relaxations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/091d880-Queue_Task.jpg",
        null,
        "Screenshot of Queue Task Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Queue Task Node"
    }
  ]
}
[/block]


The FBM Inbound Message flow ends when an asynchronous event is successfully received on the Queue Task node.

Please note that the following custom variables are being used in this flow:

- FBpageid
- conversationId
- messengerPayloadObject
- messagetext
- attachmentURL
- nonPCIComplianceReasonObject. 

You can view these configurations by clicking on the setting icon on the top right side of the flow canvas.

## Routed Flow

The Task routed flow is a global flow. This flow is triggered when a queued task is routed to an agent. When the task routed event comes in, the Extract node is used to extract some variables to use subsequently in other nodes like Add Participant to Conversation node, Screen Pop node. The variables are part of the event payload.

The Add Participant to Conversation node adds the agent as a participant to the conversation, then the agent gets notified through the Agent Desktop and can accept the contact. After the agent has accepted the contact and the customer and the agent are interacting with each other. 

The Screen Pop node can be used to showcase either a URL or a pop-up screen on their agent desktop, during the interaction between the customer and agent. 

While configuring the Screen Pop node, you can configure the Display Settings like the screen pop loading behavior. The screen pop can be inside the desktop, a new tab, or a new browser.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f644d3a-Screen_Pop1.jpg",
        null,
        "Screenshot of Screen Pop Node"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Screen Pop Node"
    }
  ]
}
[/block]


This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0f9682fc6a5a3429647d46fa866acaf0cc08f7e03e652d6682d2499d88788a31-image.png",
        null,
        "Screenshot of Task routed flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Task routed flow"
    }
  ]
}
[/block]


## Task Modified

The Task modified flow is a global flow. 

When an agent is handling the contact, the agent has the option to Transfer and Conference. Transferring the conversation or conferencing other agents is handled by the Task Modified flow. When an agent ops to transfer or conference, a Task Modified event is received as an inbound event on Task Modieifed flow along with the context which specifies to add/remove the participant from the conversation.

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9719a73feac4d4d4d6b7e7ce7f4bc172ba3f8a08ef3af9a360ef2166c08c031f-image.png",
        null,
        "Screenshot of Task modified"
      ],
      "align": "center",
      "border": true,
      "caption": "Task modified flow"
    }
  ]
}
[/block]


## Close Task

The Close task flow is a global flow.

When an agent clicks the End button on Agent Desktop, <<prodname>> receives the Task Closed event which triggers the Close Task flow. On receiving a Task Closed event, the conversation is closed first and then <<prodname>> notifies the Cisco Webex Contact Center about the task close. 

This flow is channel-agnostic but the flow designer can choose to make it channel-specific by applying conditions in the Start node. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8f7a0d16f1ee7728a40bda257b40348e6ab2e69c8de5ccac921f28703fa9172f-image.png",
        null,
        "Screenshot of Close task node"
      ],
      "align": "center",
      "border": true,
      "caption": "Close task flow"
    }
  ]
}
[/block]


## Livechat Inbound Message Flow

For the Livechat Inbound Message flow, sequence, and logic remain the same as other flows. Additionally, we use Pre-form chat which uses the form template, and the flow transitions into the next steps.

> 📘 Note
> 
> The following variables are subject to change and are used for internal reasons to handle integrations between solution components. We do not encourage <<WebexCC>> flow developers to use these variables (OR) if you do, please acknowledge the risks in doing so. We cannot undertake responsibility if your flows break due to changes in the values stored in these variables.
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