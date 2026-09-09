# Use AI agent templates

Source: https://help.webex.com/article/n8mo4c
Documentation version: not specified by publisher
Source last modified: 2026-04-14T16:43:59.661Z
Retrieved: 2026-09-08T23:48:48+00:00

<a id="content"></a>

<a id="concept-template_57259ce1-4879-4150-a360-10681a699308"></a>

AI agent templates are prebuilt examples designed to help you learn how to build agents on the platform. These templates come with preconfigured actions, intents, workflows that demonstrate core features and best practices, serving as hands-on guides for understanding the platform's capabilities. Use them to explore the agent creation process, experiment with configurations, and develop the skills needed to build your own custom agents effectively. These are industry-specific templates that can serve as a starting point, allowing you to customize the agent to meet your specific requirements.

To use a template, select it from the list of available agents at the time of creating a new agent.

- [Autonomous agent templates](https://help.webex.com/article/n8mo4c#concept-template_0afc5a1d-dc9b-4dfd-8b3e-ad25c3a8c2d4)

- [Scripted agent templates](https://help.webex.com/article/n8mo4c#concept-template_e5d845d1-de58-4dab-8e82-d8e42f6661bd)

<a id="concept-template_0afc5a1d-dc9b-4dfd-8b3e-ad25c3a8c2d4"></a>

<a id="concept-template_0afc5a1d-dc9b-4dfd-8b3e-ad25c3a8c2d4"></a>

The following templates are available for creating autonomous AI agents.

<a id="concept-template_96fd220b-fb29-415d-8993-a54d650e4c66"></a>

## Doctor’s Appointment

This template demonstrates an autonomous AI agent for managing doctor appointment bookings and cancellations. Unlike scripted agents, autonomous agents dynamically generate responses, requiring users to define only the actions the agent performs. This agent contains actions to check availability of slots, create appointments, lookup appointments and cancel them. There’s an additional action (disabled by default) to send appointment confirmation SMS, which can be enabled if a phone number asset is available in Webex Connect to send SMS.

<a id="section_clq_xzc_gfc"></a>

### Core features

- **Writing goals and instructions**: Learn how to define the agent's overall objectives (for example, booking and canceling appointments) and provide clear instructions to guide the LLM's behavior.

- **Adding actions and linking fulfillment**: 
  
  - Includes four preconfigured actions: 
    
    - **check_availability**—Looks up available appointment slots based on date and time preference.
    
    - **create_appointment**—Schedules appointments after collecting the patient's name, date of birth and reason for booking the appointment.
    
    - **lookup_appointment**—Searches for existing appointments using patient date of birth and name.
    
    - **cancel_appointment**—Cancels the appointment after user confirmation.
  
  - Demonstrates how to link actions to Webex Connect flows that use third-party APIs for real-time fulfillment.

<a id="section_kgq_yzc_gfc"></a>

### Using this template

- Import the template at the time of creating a new agent by choosing the **Doctor's Appointment** autonomous template.

- Explore and review the configured goal, instructions, and the welcome message and update them as needed.

- Create fulfillment flows for various actions in the linked Webex Connect tenant. Download the flows and import them to the required service: [doctor-clinic-fulfilment-flows](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/ai-agent-fulfilment-flows/doctor-clinic-fulfilment-flows). 
  
  - Optionally, you can link a knowledge base by creating a knowledge base and adding sample FAQs. A sample knowledge document for the doctor's appointment agent can be found [here](https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/ai-agent-fulfilment-flows/sample-knowledge-bases/doctor-faq.pdf).

- Configure fulfillment for each action by selecting the appropriate Webex Connect service and fulfillment flows created in the preceding step.
  
  - Test the agent over chat or voice by using the preview option. The sample data for testing these agents is available [here](http://ec2-18-225-36-23.us-east-2.compute.amazonaws.com:5003/appointments).

- **Deploy the agent**: Import the appropriate template flows in Webex Contact Center flow builder or Webex Connect to deploy the agent over voice or web chat. 
  
  - Use the instructions provided here to set up the voice flow and use Doctor’s appointment agent instead of Track package: [AI Agent Autonomous (Package Tracking)](https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking).
  
  - For digital channels, use the instructions provided here: [AI Agent Livechat generic](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic).

- Test the agent on the channel of your choice based on the preceding step. Try booking an appointment by providing preferences for the date, time, and reason for the visit. Attempt canceling an appointment by entering patient details.

- **Modify and Experiment**: 
  
  - Add new goals or instructions to expand the agent's capabilities and see how they affect agent behaviour.
  
  - Add knowledge to your agent by adding FAQs about the clinic to a knowledge base and linking the knowledge base to your agent.
  
  - Test prompts to optimize the LLM's tone and response style.
  
  - Update the API configurations for integration with your specific backend systems by updating connect fulfillment flows. Reference for mock APIs used in this template is available here: [Webex Contact Center API Samples](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API).

<a id="section_p2w_zzc_gfc"></a>

### Expected outcomes

After working with the autonomous Doctor's Appointment template, you will:

- Understand how to write effective goals and instructions for autonomous agents capable of handling multiple actions. For more information, see [Do's and Don'ts when writing goals](https://help.webex.com/en-us/article/nelkmxk/Guidelines-and-best-practices-for-automating-with-AI-agent#concept-template_cce8a04c-a0d8-4c35-b20b-e5846eaf5293).

- Learn how to define actions, add slots, and configure fulfillment for them.

- Discover how to set up fulfillment flows in Webex Connect. For more information, see [Configure Fulfillment Flows for AI Agent Actions](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions).

<a id="concept-template_c9cda857-c688-44b5-b1c8-9331082630de"></a>

## Track package

This template demonstrates how to build an autonomous agent for package tracking. This agent dynamically generates responses, requiring minimal configuration, and uses a single action, **trackPackage**, to retrieve package status. The template highlights how to define goals and instructions, create actions, and integrate fulfillment for real-time data retrieval.

<a id="section_fxh_pzc_gfc"></a>

### Core features

- **Writing Goals and Instructions**: Learn how to define the agent's purpose (for example, "Assist users in tracking their packages") and provide clear instructions to guide the LLM's conversational behavior.

- **Adding and Linking Actions**: this agent includes a single action named trackPackage to retrieve package status. Demonstrates how to configure the action for fulfillment by integrating with external systems.

<a id="section_kbh_qzc_gfc"></a>

### Using this template

- Import the template at the time of creating a new agent by choosing the **Track Package** autonomous template.

- Explore and review the configured goal, instructions, and welcome message, and update them as needed.

- Create fulfillment flows for various actions in the linked Webex Connect tenant. Use the template flow available in Webex Connect: [AI Agent Fulfilment Track Package](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-fulfilment-track-package). 
  
  - Optionally, you can link a knowledge base by creating a knowledge base and adding sample FAQs. A sample knowledge document for the package tracking agent can be found [here](https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/ai-agent-fulfilment-flows/sample-knowledge-bases/Logistics%20FAQ.pdf).

- Configure fulfillment for trackPackage action by choosing the appropriate Webex Connect service and flow.

- **Deploy the agent**: Import the appropriate template flows in Webex Contact Center flow builder or Webex Connect to deploy the agent over voice or web chat.
  
  - Use the instructions provided here to set up the voice flow: [AI Agent Autonomous (Package Tracking)](https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking).
  
  - For digital channels, use the instructions provided here: [AI Agent Livechat generic](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic).

- Test the agent on the channel of your choice based on the preceding step. Use **ABC123456** as a sample package number.

- **Modify and experiment**: 
  
  - Add new goals or instructions to expand the agent's capabilities and see how they affect agent behaviour.
  
  - Add knowledge to your agent by adding FAQs about the package tracking company.
  
  - Change the entity type or validation format to explore how different entity types in the platform work.
  
  - Update the API configurations for integration with your specific backend systems by updating connect fulfillment flows. Reference for mock APIs used in this template is available here: [Webex Contact Center API Samples](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API).

<a id="section_nz2_rzc_gfc"></a>

### Expected outcomes

After working with the autonomous Track package template, you will:

- Understand how to write effective goals and instructions for autonomous agents. For more information, see [Do's and Don'ts when writing goals](https://help.webex.com/en-us/article/nelkmxk/Guidelines-and-best-practices-for-automating-with-AI-agent#concept-template_cce8a04c-a0d8-4c35-b20b-e5846eaf5293).

- Learn how to define actions, add slots, and configure fulfillment for them.

- Discover how to set up fulfillment flows in Webex Connect. For more information, see [Configure Fulfillment Flows for AI Agent Actions](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions).

<a id="banking"></a>

## Cumulus Bank

This template demonstrates an autonomous AI agent for managing common banking tasks. This agent includes actions to verify user identity, fetch account balance, report fraudulent transactions, block cards, order replacement cards, and request expedited shipping.

<a id="section_clq_xzc_gfc"></a>

### Core features

- **Writing goals and instructions:** Learn how to define the agent's overall objectives for more complex use cases. In this template, some actions depend on others and follow a natural conversation flow. For example, the user needs to fetch their transactions before raising a dispute against one. This template shows how to write goals and instructions to create such dependencies in an autonomous agent.

- **Authentication:** The agent begins by authenticating the customer using information in the bank's records, ensuring secure access to account information. This authentication occurs once per interaction, even if the customer has multiple requests.

- **Adding actions and linking fulfillment:**
  
  - Includes the following pre-configured actions: 
    
    - **verify_user:** Verifies the user's identity by validating their date of birth and zipcode against bank records.
    
    - **fetch_account_balance:** Retrieves the customer's current account balance.
    
    - **fetch_recent_transactions:** Fetches recent credit card transactions to help identify fraudulent activity.
    
    - **register_transaction_dispute:** Registers a dispute for a fraudulent transaction, after confirmation with the user.
    
    - **block_card_and_order_replacement:** Blocks the customer's current credit card and orders a replacement.
    
    - **request_priority_shipping:** Places a request for expedited shipping of the replacement card (for an additional fee), after confirmation with the user.
  
  - Demonstrates how to link actions to Webex Connect flows that use third-party APIs for real-time fulfillment.

<a id="section_kgq_yzc_gfc"></a>

### Using this template

- Import the template at the time of creating a new agent by choosing the **Cumulus Bank** autonomous template.

- Explore and review the configured goal, instructions, and welcome message, and update them as needed.

- Create fulfillment flows for various actions in the linked Webex Connect tenant. Download the flows from [here](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/ai-agent-fulfilment-flows/banking%20template%20fulfilment%20flows) and import them to the required service.

- Configure fulfillment for each action by selecting the appropriate Webex Connect service and fulfillment flows created in the above step.
  
  - Test the agent over chat or voice by using the preview option. The sample data for testing these agents is available [here](http://ec2-18-225-36-23.us-east-2.compute.amazonaws.com:5003/view_users).

- **Deploy the agent**: Import the appropriate template flows in Webex Contact Center flow builder or Webex Connect to deploy the agent over voice or webchat. 
  
  - Use the instructions provided [here](https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking) to setup the voice flow and use Banking agent instead of Track package.
  
  - For digital channels, use the instructions provided [here](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic).

- Test the agent on the chosen channel. Try checking balance for a sample user, fetching transactions, disputing one of the fetched transactions, and then blocking the card. Add new users by using the API collection available in the step below. 
  
  You can use the following details for testing purposes:

  - DOB: 25-12-1975 and Zip code: 11223
  
  - DOB: 22-06-1992 and Zip code: 67890

- **Modify and Experiment**: 
  
  - Add new goals or instructions to expand the agent's capabilities and observe changes in agent behavior.
  
  - Enhance the agent's knowledge by adding airline FAQs to a knowledge base and linking it to your agent.
  
  - Test prompts to optimize the LLM's tone and response style.
  
  - Update the API configurations for integration with your specific backend systems by updating connect fulfillment flows. Reference for mock APIs used in this template is available [here](https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/WEbEx-AI-Template-API/Banking%20template.postman_collection.json).

<a id="section_p2w_zzc_gfc"></a>

### Expected outcomes

After working with the autonomous Cumulus Bank template, you will:

- Understand how to write effective goals and instructions for autonomous agents, especially when actions are interdependent and require authentication. More information is available [here](https://help.webex.com/en-us/article/nelkmxk/Guidelines-and-best-practices-for-automating-with-AI-agent#concept-template_c9133e5c-3d05-4322-b7d8-b6f714c9e2bb).

- Learn how to define actions, add slots, and configure fulfillment for them.

- Discover how to set up fulfillment flows in Webex Connect. More information is available [here](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions).

<a id="airlines"></a>

## Cumulus Airline

This template demonstrates an autonomous AI agent designed to streamline airline customer service operations. The agent efficiently manages tasks such as retrieving flight details, facilitating check-ins, handling flight modifications, and processing cancellations. Its design prioritizes security and a customer-focused approach, ensuring travelers experience a seamless and efficient service.

<a id="section_clq_xzc_gfc"></a>

### Key capabilities

The agent is equipped with the following pre-configured actions:

- **get_flight_info:** Securely access flight details using the booking ID and last name, forming the basis for all subsequent operations.

- **checkin:** Enable passengers to check in for their flights, capturing any special requests or notes during the process.

- **cancel_checkin:** Process check-in cancellations, providing passengers with the ability to undo their check-in status.

- **lookup_flights:** Searches for alternative flights based on the passenger's preferred new date for rescheduling.

- **reschedule_flight:** Allow passengers to modify their flight bookings by searching for alternative flights on their preferred dates.

- **cancel_booking:** Facilitate flight cancellations, offering passengers a straightforward way to cancel their reservations.

- **Agent handover:** Seamlessly transfer complex or sensitive inquiries to a human agent for personalized support.

<a id="section_kgq_yzc_gfc"></a>

### Using this template

- Import the template at the time of creating a new agent by choosing the **Cumulus Airline** autonomous template.

- Explore and review the configured goal, instructions, and welcome message, and update them as needed.

- Create fulfillment flows for various actions in the linked Webex Connect tenant. Download the flows from [here](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/ai-agent-fulfilment-flows/airline%20template%20fulfilment%20flows) and import them to the required service.

- Configure fulfillment for each action by selecting the appropriate Webex Connect service and fulfillment flows created in the above step.
  
  - Test the agent over chat or voice by using the preview option. The sample data for testing these agents is available [here](http://ec2-18-225-36-23.us-east-2.compute.amazonaws.com:5003/bookings).

- **Deploy the agent**: Import the appropriate template flows in Webex Contact Center flow builder or Webex Connect to deploy the agent over voice or webchat.
  
  - Use the instructions provided [here](https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking) to setup the voice flow and use Cumulus Airline agent instead of Track package.
  
  - For digital channels, use the instructions provided [here](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic).

- Test the agent on the chosen channel. Try checking balance for a sample user, fetching transactions, disputing one of the fetched transactions, and then blocking the card. Add new users by using the API collection available in the step below. 
  
  You can use the following details for testing purposes:

  - Booking id: X6Q4MN and last name: Watson
  
  - Booking id: R5PT9X and last name: Rivera

- **Modify and Experiment**:
  
  - Add new goals or instructions to expand the agent's capabilities and observe changes in agent behavior. Experiment with clarification prompts, fallback responses, and adjust the agent’s tone and persona.
  
  - Enhance the agent's knowledge by adding airline FAQs to a knowledge base and linking it to your agent.
  
  - Update API configurations for integration with your specific backend systems by updating Webex Connect fulfillment flows. Reference for mock APIs used in this template is available [here](https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/WEbEx-AI-Template-API/airlines%20template.postman_collection.json).

<a id="concept-template_e5d845d1-de58-4dab-8e82-d8e42f6661bd"></a>

<a id="concept-template_e5d845d1-de58-4dab-8e82-d8e42f6661bd"></a>

The following templates are available for creating scripted AI agents.

<a id="concept-template_8c5068aa-2f60-44c7-8fbe-41c86929e8dd"></a>

## Doctor’s appointment

This template demonstrates a scripted AI agent for managing doctor appointment bookings and cancellations. This agent is designed to guide users through structured conversations, using developer-defined training data to handle intents like booking and canceling appointments. It showcases how to use platform features like context and custom events for dynamic interactions and how to integrate third-party APIs on voice and digital channels.

<a id="section_fwq_ryc_gfc"></a>

### Core features

- **Intent and entity detection**—The agent detects user intents to detect intents for appointment booking and canceling. Based on the intent detected, it proceeds to capture entities/slots to complete the intents.

- **Context management**—Routes users to appropriate intents (for example, confirming or declining an appointment slot) based on their responses.

- **Custom Events**—Facilitates communication between the AI agent and Webex Contact Center flow for fulfillment tasks.

- **AI agent deployment on voice or digital channels**—This agent is packaged with accompanying voice and digital channel flows that let developers deploy the agent on these channels.

<a id="section_ekt_syc_gfc"></a>

### Using this template

- Import the template at the time of creating a new agent by choosing the **Doctor's Appointment** scripted template.

- Explore the configuration by reviewing the intents and the linked slots, how context is used to manage user responses like "yes" or "no" after a slot is presented, how **custom events** are set up to interact with WxCC flow builder. Publish the agent upon reviewing the configuration.

- **Deploy the agent**: Import the appropriate template flows in WxCC flow builder or Webex Connect to deploy the agent over voice or web chat. 
  
  - Use the instructions provided here to set up the voice flow: [AI Agent Scripted (Doctor's Appointment Booking)](https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-scripted-doctors-appointment-booking).
  
  - For digital channels, use the instructions provided here: [AI Agent Scripted Doctor Appointment](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-scripted-doctor-appointment).

- Test the Agent on the channel of your choice from step 3. Try booking an appointment by providing preferences for the date, time, and reason for the visit. Attempt canceling an appointment by entering patient details.

- **Modify and Experiment**: 
  
  - Customize the responses to fit your organization's tone or style.
  
  - Update the API configurations for integration with your specific backend systems. Reference for mock APIs used in this template is available here [Webex Contact Center API Samples](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API).
  
  - Add new intents, such as rescheduling an appointment, to expand functionality.

<a id="section_zp1_5yc_gfc"></a>

### Expected outcomes

After working with the **Doctor's Appointment** template, you will:

- Understand how to configure intents, entities, and ways to link them to structure a conversation.

- Discover how to manage structured conversations using context.

- Gain familiarity with custom events to manage the switching of control between the AI agent and the voice flow.

- Learn how to configure fulfillment for various intents on digital channels.

<a id="concept-template_e24d61f5-2ad1-4644-9410-dc5b10c28b07"></a>

## Track package

The template showcases how to build a simple AI agent for tracking packages. This agent demonstrates how to set up an intent and integrate fulfillment to fetch real-time package status through a third-party API. Designed for both voice and digital channels, this template is ideal for learning the basics of intent configuration and API-based fulfillment.

<a id="section_uc1_bzc_gfc"></a>

### Core features

- **Input Validation**—Ensures the package number follows the alphanumeric format (in this case, a few alphabets followed by six numbers).

- **Third-Party API Integration**—Fetches package status using an external API using Webex Connect flows for digital channels and custom events through Webex Contact Center flow builder for voice.

<a id="section_dlh_czc_gfc"></a>

### Using this template

- Import the template at the time of creating a new agent by choosing the **Track package** scripted template.

- Explore the configuration by reviewing the intents and the linked slots, how context is used to manage user responses like "yes" or "no" after a slot is presented, how **custom events** are set up to interact with WxCC flow builder. Publish the agent upon reviewing the configuration.

- **Deploy the agent**: Import the appropriate template flows in WxCC flow builder or Webex Connect to deploy the agent over voice or web chat.
  
  - Use the instructions provided here to import the **voice** flow: [AI Agent Scripted (Package Tracking)](https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-scripted-package-tracking).
  
  - For **digital** channels, use the AI Agent Livechat generic template and add fulfillment in the flow: [AI Agent Livechat generic](https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic). Refer to the ‘AI Agent Scripted Doctor Appointment’ flow for guidelines on how to add fulfillment or refer to the chapter named ‘Configuring AI Agent Fulfillment for scripted agents’ in this Vidcast: [Webex AI Agent: Using AI agents on digital channels](https://app.vidcast.io/share/0b66bed4-8054-4da5-975b-941f85ce4ba3?t=740).
  
  - API reference for adding and tracking packages: [Webex Contact Center API Samples](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API).

- Test the Agent on the channel of your choice from step 3. Use **ABC123456** as a sample package number.

- **Modify and Experiment**: Change the entity type or validation format to explore how different entity types in the platform work.

<a id="section_khc_2zc_gfc"></a>

### Expected outcomes

After working with the **Track package** scripted template, you will:

- Understand how to configure intents, and how input validation with entities works.

- Get hands-on experience for configuring fulfillment for intents on digital channels.

- Gain familiarity with custom events to manage the switching of control between the AI agent and the voice flow.
