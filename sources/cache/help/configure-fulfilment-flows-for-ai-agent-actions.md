# Configure Fulfillment Flows for AI Agent Actions

Source: https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:45+00:00

## Introduction

This document details the procedure for configuring fulfillment flows for AI Agent actions on Webex Connect and the steps for selecting these AI Agent-triggered fulfillment flows within the Webex AI Agent Studio. Execution of an AI Agent action in Webex AI Agent Studio triggers the corresponding selected flow in Webex Connect. By default, Webex Connect automatically notifies flows initiated by AI Agent as the Start node. Upon completion of the flow execution, the system communicates the outcome and any associated payload (defined in the flow outcome settings) back to the AI Agent.

## Configure AI Agent Fulfillment Flow

**Steps to create an AI Agent fulfillment flow:**

1. Click on the preferred **Service** from the Services dashboard.

   

![Select Service ](https://files.readme.io/cf5e30ab84102c128d890a07f0c193717e139608cf376bf315810aaa92b3e663-AI_1.png)


2. Click the **Create Flow** button from the Services page.

   

![Click Create Flow](https://files.readme.io/b69d1e5f6cf59aa9858f5f2ec1ac8ad8b77943a64ae9533e71a4f025d2cfe178-AI_2.jpeg)


3. Enter the **Flow Name**. 

   1. Under **Method**, select **New Flow **as the Flow option. You can also **Copy from existing** or **Upload **a new flow.  
      When constructing an AI Agent fulfillment flow, ensure that whether you are copying from an existing flow or uploading a new one, the AI Agent should be set as the start node.
   2. If you are building a new flow, select the **Start from Scratch** option to create a flow from the beginning and click on **Create** to proceed.

   

![Add Flow Name on Create Flow ](https://files.readme.io/2e2ea2232868c8a0be8e986ca2dbfed10b5655f34e4005d7531c6b02e0e352e7-AI_3.png)


4. Select **AI Agent** Trigger category as the Start node.

   

![Select AI Agent Trigger Category](https://files.readme.io/adb06c8705c05bd591ddfefe6eb7c47c242feeae30aabfaa74fcc6d970117f7d-AI_5.png)



   > 📘 Note
   > 
   > If you change the Start Node, the notification set from the flow outcome is disabled and the configured payload in the Start node is automatically deleted. A warning message is displayed as shown below:

   

![Warning Message received when changed the Start Node](https://files.readme.io/dfd1b7dcbe9be25fc36ba1d9404944ee4b2fd168ab687af3ef4b31faaedb6dbd-AI_Note1.png)


5. Once you choose AI Agent as the Start node, you will find the event auto-populated as “**Trigger from AI Agent to initiate flow**“.

   

![Configure AI Agent Event](https://files.readme.io/2d776f153ce693cddc68984d413097b46a0524b2435218374071b55307cd3acf-AI_7.png)



   The configuration popup displays an endpoint URL used by Webex AI Agent Studio to trigger the Webex Connect fulfillment flow. This URL is secured by Webex CI authentication.  
   A sample input JSON is provided by default in the **Provide sample JSON** which you can modify within the Webex AI Agent Studio. For more information, refer to [Configure Fulfillment Flows for AI Agent Actions](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions#how-to-get-the-payload-on-ai-agent-studio) and click **Parse ** to view the sample payload's parameters as output variables. You can also configure conditional triggering based on the payload. This ensures flows are invoked only when the specified conditions are met.

   > 📘 Note
   > 
   > AI Agent flows have a 30-second execution time limit. Using Waiting Nodes such as Delay, Social Hour, Receive Node, and Call Workflow is restricted, as these nodes can cause flow execution to exceed this limit. Exceeding the 30-second limit prevents the AI Agent from receiving the journey fulfillment response, leading to unexpected issues in AI Agent Action fulfillment.
6. Build your flow by dragging and dropping the nodes.
7. The AI Agent is notified of flow completion. By default, the notification for AI Agent is enabled under the flow setting with the default payload. On flow completion, you can update the payload shared with the AI Agent.  
   Under **Flow Settings**, click on **Flow Outcomes**. 

   In the Flow Outcomes, open the ‘**Last Execution Status**’ Outcome. The ‘Notify AI Agent’ radio button is enabled by default for the start node with 'AI Agent’ as the trigger.

   You can send a simple JSON payload using key-value pairs or a more complex payload (including arrays) using the "Paste JSON" option. The system provides default key-value pairs for TransactionID, service name, status code, and flow name. You can **add more** or **delete** the previous one as required. For the key, you can provide the key name, and either a static value, or select a variable from the Input Variables panel for dynamic population. This payload would be sent to the AI Agent after the execution of the flow.

   > 📘 
   > 
   > The maximum length of payload can be 16000 characters.

   

![Flow Settings](https://files.readme.io/1b5c7955cac15691355c27e9e4617a45147483349c823d07ff2840b8082b29e2-AI_Note2.png)



   > 📘 Note
   > 
   > - Last Execution Status captures the final node outcome and doesn’t require a mapping between node event and flow outcome in the End pop up screen. Last Execution Status automatically captures the last node event and sends a notification to AI Agent (given the AI Agent notification is not disabled).
   > - Disabling the outcome prevents the AI Agent from receiving notifications, the same is explained in a toast message appearing on the screen as illustrated below. It is essential to enable notifications for the AI Agent; disabling them prevents the AI Agent from receiving the fulfillment outcome. Understand the implications before disabling notifications.  
   >   You may toggle on notify to restore the notification. This action restores your last configured payload or key-value information.
8. Click **Make Live** to publish the flow live. Before going live, make a few settings.

   1. Select the asset that is used in the flow.
   2. Enter the **Comments** for the flow.

   

![Make Live Configuration](https://files.readme.io/0a93ba8b672fa5021fd2f223dbc699fb79c58860f73bffd98fc50cdba8e103d0-AI_11.png)


9. Click **Make Live**.  
   Upon completion of flow execution, the AI Agent is notified of the flow outcome. The payload configured in the flow settings screen is used for the notification. For more information, refer to the [notification](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions#configure-the-flow-outcomes-for-ai-agent-in-webex-connect) section.

## Fulfillment Flow Selection in Webex AI Agent Studio

**Steps to select a flow in Webex AI Agent Studio:**

1. Log in to Webex AI Agent Studio by crosslaunching from Control Hub.

   

![Webex AI Agent](https://files.readme.io/ef69732c59a11963a57c16b314377fd93c8e245f952bacd4268b18a38c6d3703-AI_Flow-_Intro_1.png)



   

![AI Agents](https://files.readme.io/33660a510b0fa21231a9aa90382b8311be3b9f25048d18e9f03305fa8a8ee294-AI_Flow_Intro-2.png)


2. Launch the agent. Go to **Actions**. Select the **Action ** for which you want to configure the fulfillment flow. 

   

![AI agent settings—Actions Tab](https://files.readme.io/8279a4475d1f2753ddbc9fe530b76be03072a67bd63d385e683c3dbfc5e31617-AI_Flow_1.png)


3. Scroll down to **Webex Connect Flow Builder Fulfillment**  section on the Actions page.

   

![Webex Connect Flow Builder Fulfillment](https://files.readme.io/f9a2c5a1408473a79733e105d491a51bb5d8b5d96be7032f471f9060cb08cd2a-AI_Flow_2.png)


4. **Select a service** that is configured in the Webex Connect client workspace. This will enable you to view a list of the selected service's flows, where the start node is the AI Agent.
   > 📘 Note
   > 
   > The Webex AI Agent Studio can only access service and flows configured within the Client-level workspace.
5. **Select a flow** from the dropdown. When the action executes the selected flow in Webex Connect, the outcomes will be notified to the AI Agent.
   > 📘 For more information on AI agent configuration set up and add actions to AI Agent, refer to our [help.webex.com guide](https://help.webex.com/article/ncs9r37)

## Configure the Flow Outcomes for AI Agent in Webex Connect

1. Click on **Flow Settings** on the Flow Builder page.
2. Click **Flow Outcomes** to configure the outcomes of a flow.  
   The AI Agent notification is enabled by default with a default-configured payload.
3. Select **Enter key** and **value** or **Enter JSON ** to use the nested payloads. You can modify the default outcomes as required.

   

![Flow Outcomes](https://files.readme.io/14c84b56157c255ad28828744675247bbc8f4ebf1d82b50c84f5a4542d89f85e-AI_Flow_Intro-3.png)



   > 📘 Note
   > 
   > - Variables can be added with a '$' prefixed. Variable names are case-sensitive. 
   > - Sending flow outcomes is mandatory for AI Agent flow with the ‘AI Agent’ as the Start node.
4. Within a flow, the **Transaction Action** assigns each node a variable and a corresponding value. This ensures the AI Agent receives the most current variable value during flow execution. When the flow reaches its endpoint, the latest value of the variable at that stage is sent to notify the AI Agent.  
   For instance, consider a flow that begins with a start node and progresses through two HTTP nodes. Each HTTP node is configured with a variable named `phone` but assigned different values—`1` for the first HTTP node and `2 `for the second. If the flow concludes at the first HTTP node, the value sent to the AI Agent is `1`. Conversely, if the flow ends at the second HTTP node, the value sent is `2`.

## How to get the payload on Webex AI Agent Studio

1. Log in to Webex AI Agent Studio by crosslaunching from Control Hub.



![Webex AI Agent](https://files.readme.io/ef69732c59a11963a57c16b314377fd93c8e245f952bacd4268b18a38c6d3703-AI_Flow-_Intro_1.png)






![AI Agents](https://files.readme.io/82398ff5215bf47ba0b2c59b48e239d0dac3ade39a00300cfe7ad65149dcd2b4-AI_Flow_Intro-2.png)




2. Launch the agent. Click on **Actions** tab. Select the **Action** for which you want to configure the fulfillment flow.

   

![Actions Tab in Webex AI Agent Studio](https://files.readme.io/0aec0c4e8eced35aae66852bf05bb66fa5115160207d11b4cb136f8726fe1ba8-AI_Payload_1.png)


3. Scroll down to **Slot filling** on the **Update Action** page.

   

![Slot Filling on the Update Action ](https://files.readme.io/a562538d818aa80b931309b3b710b43b48ab784333277331845511f946021d7b-AI_Payload_3.png)


4. Under **Input entities**, you would see the list of entities added to the flow. The input entities have to be converted into a JSON.  
   For example, for the above screenshot, the JSON example for the input entities is below:  
   `{"city": "city_value",
   "country": "country_value"}`