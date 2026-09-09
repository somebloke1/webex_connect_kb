<div class="article-content" id="content">
  <main role="main">
    <article data-role="Administrator" data-product="Webex Contact Center" data-operatingsystem="Web Browser" role="article">
  
  
  <div><article class="topic concept" id="concept-template_57259ce1-4879-4150-a360-10681a699308"><div class="body conbody" id="">
      <p class="p">AI agent templates are prebuilt examples designed to help you learn how to build agents on
      the platform. These templates come with preconfigured actions, intents, workflows that
      demonstrate core features and best practices, serving as hands-on guides for understanding the
      platform's capabilities. Use them to explore the agent creation process, experiment with
      configurations, and develop the skills needed to build your own custom agents effectively.
      These are industry-specific templates that can serve as a starting point, allowing you to
      customize the agent to meet your specific requirements.</p>
      <p class="p">To use a template, select it from the list of available agents at the time of creating a new
      agent.</p>
    </div></article></div>
  <p class="topictitle1" id=""></p><div class="tabs-container"><ul class="nav nav-tabs"><li class="active"><a href="#concept-template_0afc5a1d-dc9b-4dfd-8b3e-ad25c3a8c2d4" data-toggle="tab" class="btn btn-primary">Autonomous agent templates</a></li><li><a href="#concept-template_e5d845d1-de58-4dab-8e82-d8e42f6661bd" data-toggle="tab" class="btn btn-primary">Scripted agent templates</a></li></ul><div class="tab-content"><div id="concept-template_0afc5a1d-dc9b-4dfd-8b3e-ad25c3a8c2d4" class="tab-pane fade in active"><div><article class="topic concept" id="concept-template_0afc5a1d-dc9b-4dfd-8b3e-ad25c3a8c2d4"><div class="body conbody" id="">
        <p class="p"> The following templates are available for creating autonomous AI agents. </p>
        <p class="p">
      
    </p>
      </div><div><article class="topic concept" id="concept-template_96fd220b-fb29-415d-8993-a54d650e4c66"><h2>Doctor’s Appointment</h2><div class="body conbody" id="">
          <p class="p">This template demonstrates an autonomous AI agent for managing doctor appointment bookings
      and cancellations. Unlike scripted agents, autonomous agents dynamically generate responses,
      requiring users to define only the actions the agent performs. This agent contains actions to
      check availability of slots, create appointments, lookup appointments and cancel them. There’s
      an additional action (disabled by default) to send appointment confirmation SMS, which can be
      enabled if a phone number asset is available in Webex Connect to send SMS.</p>
          <section class="section" id="section_clq_xzc_gfc">
      <h3 class="title sectiontitle">Core features</h3>
      <p class="p">
        </p><ul class="ul"><li class="li">
            <strong class="ph b">Writing goals and instructions</strong>: Learn how to define the agent's overall
            objectives (for example, booking and canceling appointments) and provide clear
            instructions to guide the LLM's behavior. </li><li class="li">
            <strong class="ph b">Adding actions and linking fulfillment</strong>: <ul class="ul"><li class="li">Includes four preconfigured actions: <ul class="ul"><li class="li">
                    <strong class="ph b">check_availability</strong>—Looks up available appointment slots based on date and
                    time preference.</li><li class="li">
                    <strong class="ph b">create_appointment</strong>—Schedules appointments after collecting the patient's
                    name, date of birth and reason for booking the appointment.</li><li class="li">
                    <strong class="ph b">lookup_appointment</strong>—Searches for existing appointments using patient date
                    of birth and name.</li><li class="li">
                    <strong class="ph b">cancel_appointment</strong>—Cancels the appointment after user confirmation.</li></ul></li><li class="li">Demonstrates how to link actions to Webex Connect flows that use third-party APIs
                for real-time fulfillment.</li></ul>
          </li></ul>
      <p></p>
    </section>
          <section class="section" id="section_kgq_yzc_gfc">
      <h3 class="title sectiontitle">Using this template</h3>
      <p class="p">
        </p><ol class=""><li class="li">Import the template at the time of creating a new agent by choosing the <strong class="ph b">Doctor's
              Appointment</strong> autonomous template.</li><li class="li">Explore and review the configured goal, instructions, and the welcome message and
            update them as needed.</li><li class="li">Create fulfillment flows for various actions in the linked Webex Connect tenant.
            Download the flows and import them to the required service:  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/ai-agent-fulfilment-flows/doctor-clinic-fulfilment-flows" data-scope="external">doctor-clinic-fulfilment-flows</a>. <ul class="ul"><li class="li">Optionally, you can link a knowledge base by creating a knowledge base and adding
                sample FAQs. A sample knowledge document for the doctor's appointment agent can be
                found  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/ai-agent-fulfilment-flows/sample-knowledge-bases/doctor-faq.pdf" data-scope="external">here</a>. </li></ul></li><li class="li">Configure fulfillment for each action by selecting the appropriate Webex Connect
            service and fulfillment flows created in the preceding step.<ul class="ul"><li class="li">Test the agent over chat or voice by using the preview option. The sample data for
                testing these agents is available  <a title="" href="http://ec2-18-225-36-23.us-east-2.compute.amazonaws.com:5003/appointments" data-scope="external">here</a>.</li></ul></li><li class="li">
            <strong class="ph b">Deploy the agent</strong>: Import the appropriate template flows in Webex Contact Center
            flow builder or Webex Connect to deploy the agent over voice or web chat. <ol class=""><li class="li">Use the instructions provided here to set up the voice flow and use Doctor’s
                appointment agent instead of Track package:  <a title="" href="https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking" data-scope="external">AI Agent Autonomous (Package Tracking)</a>. </li><li class="li">For digital channels, use the instructions provided here:  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic" data-scope="external">AI Agent Livechat generic</a>.</li></ol>
          </li><li class="li">Test the agent on the channel of your choice based on the preceding step. Try booking
            an appointment by providing preferences for the date, time, and reason for the visit.
            Attempt canceling an appointment by entering patient details.</li><li class="li">
            <strong class="ph b">Modify and Experiment</strong>: <ol class=""><li class="li">Add new goals or instructions to expand the agent's capabilities and see how they
                affect agent behaviour.</li><li class="li">Add knowledge to your agent by adding FAQs about the clinic to a knowledge base
                and linking the knowledge base to your agent.</li><li class="li">Test prompts to optimize the LLM's tone and response style.</li><li class="li">Update the API configurations for integration with your specific backend systems
                by updating connect fulfillment flows. Reference for mock APIs used in this template
                is available here:  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API" data-scope="external">Webex Contact Center API Samples</a>.</li></ol>
          </li></ol>
      <p></p>
    </section>
          <section class="section" id="section_p2w_zzc_gfc">
      <h3 class="title sectiontitle">Expected outcomes</h3>
      <p class="p">After working with the autonomous Doctor's Appointment template, you will:</p><ul class="ul"><li class="li">Understand how to write effective goals and instructions for autonomous agents capable
            of handling multiple actions. For more information, see  <a title="" href="https://help.webex.com/en-us/article/nelkmxk/Guidelines-and-best-practices-for-automating-with-AI-agent#concept-template_cce8a04c-a0d8-4c35-b20b-e5846eaf5293" data-scope="external">Do's and Don'ts when writing goals</a>.</li><li class="li">Learn how to define actions, add slots, and configure fulfillment for them.</li><li class="li">Discover how to set up fulfillment flows in Webex Connect. For more information, see
               <a title="" href="https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions" data-scope="external">Configure Fulfillment Flows for AI Agent
            Actions</a>. </li></ul><p></p>
    </section>
        </div></article></div><div><article class="topic concept" id="concept-template_c9cda857-c688-44b5-b1c8-9331082630de"><h2>Track package</h2><div class="body conbody" id="">
          <p class="p">This template demonstrates how to build an autonomous agent for package tracking. This agent
      dynamically generates responses, requiring minimal configuration, and uses a single action,
        <strong class="ph b">trackPackage</strong>, to retrieve package status. The template highlights how to define goals
      and instructions, create actions, and integrate fulfillment for real-time data retrieval.</p>
          <section class="section" id="section_fxh_pzc_gfc">
      <h3 class="title sectiontitle">Core features</h3>
      <p class="p">
        </p><ul class="ul"><li class="li">
            <strong class="ph b">Writing Goals and Instructions</strong>: Learn how to define the agent's purpose (for
            example, "Assist users in tracking their packages") and provide clear instructions to
            guide the LLM's conversational behavior. </li><li class="li">
            <strong class="ph b">Adding and Linking Actions</strong>: this agent includes a single action named
            trackPackage to retrieve package status. Demonstrates how to configure the action for
            fulfillment by integrating with external systems. </li></ul>
      <p></p>
    </section>
          <section class="section" id="section_kbh_qzc_gfc">
      <h3 class="title sectiontitle">Using this template</h3>
      <p class="p">
        </p><ol class=""><li class="li">Import the template at the time of creating a new agent by choosing the <strong class="ph b">Track
              Package</strong> autonomous template.</li><li class="li">Explore and review the configured goal, instructions, and welcome message, and update
            them as needed.</li><li class="li">Create fulfillment flows for various actions in the linked Webex Connect tenant. Use
            the template flow available in Webex Connect:  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-fulfilment-track-package" data-scope="external">AI Agent Fulfilment Track Package</a>. <ul class="ul"><li class="li">Optionally, you can link a knowledge base by creating a knowledge base and adding
                sample FAQs. A sample knowledge document for the package tracking agent can be found
                   <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/ai-agent-fulfilment-flows/sample-knowledge-bases/Logistics%20FAQ.pdf" data-scope="external">here</a>.</li></ul></li><li class="li">Configure fulfillment for trackPackage action by choosing the appropriate Webex
            Connect service and flow.</li><li class="li">
            <strong class="ph b">Deploy the agent</strong>: Import the appropriate template flows in Webex Contact Center
            flow builder or Webex Connect to deploy the agent over voice or web chat.<ol class=""><li class="li">Use the instructions provided here to set up the voice flow:  <a title="" href="https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking" data-scope="external">AI Agent Autonomous (Package Tracking)</a>.</li><li class="li">For digital channels, use the instructions provided here:  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic" data-scope="external">AI Agent Livechat generic</a>.</li></ol></li><li class="li">Test the agent on the channel of your choice based on the preceding step. Use
              <strong class="ph b">ABC123456</strong> as a sample package number.</li><li class="li">
            <strong class="ph b">Modify and experiment</strong>: <ol class=""><li class="li">Add new goals or instructions to expand the agent's capabilities and see how they
                affect agent behaviour.</li><li class="li">Add knowledge to your agent by adding FAQs about the package tracking
                company.</li><li class="li">Change the entity type or validation format to explore how different entity types
                in the platform work.</li><li class="li">Update the API configurations for integration with your specific backend systems
                by updating connect fulfillment flows. Reference for mock APIs used in this template
                is available here:  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API" data-scope="external">Webex Contact Center API Samples</a>.</li></ol></li></ol>
      <p></p>
    </section>
          <section class="section" id="section_nz2_rzc_gfc">
      <h3 class="title sectiontitle">Expected outcomes</h3>
      <p class="p">After working with the autonomous Track package template, you will:</p><ul class="ul"><li class="li">Understand how to write effective goals and instructions for autonomous agents. For
            more information, see  <a title="" href="https://help.webex.com/en-us/article/nelkmxk/Guidelines-and-best-practices-for-automating-with-AI-agent#concept-template_cce8a04c-a0d8-4c35-b20b-e5846eaf5293" data-scope="external">Do's and Don'ts when writing goals</a>. </li><li class="li">Learn how to define actions, add slots, and configure fulfillment for them.</li><li class="li">Discover how to set up fulfillment flows in Webex Connect. For more information, see
               <a title="" href="https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions" data-scope="external">Configure Fulfillment Flows for AI Agent
            Actions</a>. </li></ul><p></p>
    </section>
        </div></article></div><div><article class="topic concept" id="banking"><h2>Cumulus Bank</h2><div class="body conbody" id="">
          <p class="p">This template demonstrates an autonomous AI agent for managing common banking tasks. This
      agent includes actions to verify user identity, fetch account balance, report fraudulent
      transactions, block cards, order replacement cards, and request expedited shipping.</p>
          <section class="section" id="section_clq_xzc_gfc">
      <h3 class="title sectiontitle">Core features</h3>
      <p class="p">
        </p><ul class="ul"><li class="li">
            <strong class="ph b">Writing goals and instructions:</strong> Learn how to define the agent's overall
            objectives for more complex use cases. In this template, some actions depend on others
            and follow a natural conversation flow. For example, the user needs to fetch their
            transactions before raising a dispute against one. This template shows how to write
            goals and instructions to create such dependencies in an autonomous agent. </li><li class="li">
            <strong class="ph b">Authentication:</strong> The agent begins by authenticating the customer using information
            in the bank's records, ensuring secure access to account information. This
            authentication occurs once per interaction, even if the customer has multiple requests. </li><li class="li">
            <strong class="ph b">Adding actions and linking fulfillment:</strong><ul class="ul"><li class="li">Includes the following pre-configured actions: <ul class="ul"><li class="li">
                    <strong class="ph b">verify_user:</strong> Verifies the user's identity by validating their date of
                    birth and zipcode against bank records.</li><li class="li">
                    <strong class="ph b">fetch_account_balance:</strong> Retrieves the customer's current account
                    balance.</li><li class="li">
                    <strong class="ph b">fetch_recent_transactions:</strong> Fetches recent credit card transactions to
                    help identify fraudulent activity.</li><li class="li">
                    <strong class="ph b">register_transaction_dispute:</strong> Registers a dispute for a fraudulent
                    transaction, after confirmation with the user.</li><li class="li">
                    <strong class="ph b">block_card_and_order_replacement:</strong> Blocks the customer's current credit
                    card and orders a replacement.</li><li class="li">
                    <strong class="ph b">request_priority_shipping:</strong> Places a request for expedited shipping of the
                    replacement card (for an additional fee), after confirmation with the user.</li></ul></li><li class="li">Demonstrates how to link actions to Webex Connect flows that use third-party APIs
                for real-time fulfillment.</li></ul>
          </li></ul>
      <p></p>
    </section>
          <section class="section" id="section_kgq_yzc_gfc">
      <h3 class="title sectiontitle">Using this template</h3>
      <p class="p">
        </p><ol class=""><li class="li">Import the template at the time of creating a new agent by choosing the <strong class="ph b">Cumulus
              Bank</strong> autonomous template.</li><li class="li">Explore and review the configured goal, instructions, and welcome message, and update
            them as needed.</li><li class="li">Create fulfillment flows for various actions in the linked Webex Connect tenant.
            Download the flows from  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/ai-agent-fulfilment-flows/banking%20template%20fulfilment%20flows" data-scope="external">here</a> and import them to the required
            service.</li><li class="li">Configure fulfillment for each action by selecting the appropriate Webex Connect
            service and fulfillment flows created in the above step.<ul class="ul"><li class="li">Test the agent over chat or voice by using the preview option. The sample data for
                testing these agents is available  <a title="" href="http://ec2-18-225-36-23.us-east-2.compute.amazonaws.com:5003/view_users" data-scope="external">here</a>.</li></ul></li><li class="li">
            <strong class="ph b">Deploy the agent</strong>: Import the appropriate template flows in Webex Contact Center
            flow builder or Webex Connect to deploy the agent over voice or webchat. <ol class=""><li class="li">Use the instructions provided  <a title="" href="https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking" data-scope="external">here</a> to setup the voice flow and use Banking
                agent instead of Track package. </li><li class="li">For digital channels, use the instructions provided  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic" data-scope="external">here</a>.</li></ol></li><li class="li">Test the agent on the chosen channel. Try checking balance for a sample user, fetching
            transactions, disputing one of the fetched transactions, and then blocking the card. Add
            new users by using the API collection available in the step below. <p class="p">You can use the
              following details for testing purposes:</p><ul class="ul"><li class="li">DOB: 25-12-1975 and Zip code: 11223</li><li class="li">DOB: 22-06-1992 and Zip code: 67890</li></ul><p></p></li><li class="li">
            <strong class="ph b">Modify and Experiment</strong>: <ol class=""><li class="li">Add new goals or instructions to expand the agent's capabilities and observe
                changes in agent behavior.</li><li class="li">Enhance the agent's knowledge by adding airline FAQs to a knowledge base and
                linking it to your agent.</li><li class="li">Test prompts to optimize the LLM's tone and response style.</li><li class="li">Update the API configurations for integration with your specific backend systems
                by updating connect fulfillment flows. Reference for mock APIs used in this template
                is available  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/WEbEx-AI-Template-API/Banking%20template.postman_collection.json" data-scope="external">here</a>. </li></ol>
          </li></ol>
      <p></p>
    </section>
          <section class="section" id="section_p2w_zzc_gfc">
      <h3 class="title sectiontitle">Expected outcomes</h3>
      <p class="p">After working with the autonomous Cumulus Bank template, you will:</p><ul class="ul"><li class="li">Understand how to write effective goals and instructions for autonomous agents,
            especially when actions are interdependent and require authentication. More information
            is available  <a title="" href="https://help.webex.com/en-us/article/nelkmxk/Guidelines-and-best-practices-for-automating-with-AI-agent#concept-template_c9133e5c-3d05-4322-b7d8-b6f714c9e2bb" data-scope="external">here</a>. </li><li class="li">Learn how to define actions, add slots, and configure fulfillment for them.</li><li class="li">Discover how to set up fulfillment flows in Webex Connect. More information is
            available  <a title="" href="https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions" data-scope="external">here</a>. </li></ul><p></p>
    </section>
        </div></article></div><div><article class="topic concept" id="airlines"><h2>Cumulus Airline</h2><div class="body conbody" id="">
          <p class="p">This template demonstrates an autonomous AI agent designed to streamline airline customer
      service operations. The agent efficiently manages tasks such as retrieving flight details,
      facilitating check-ins, handling flight modifications, and processing cancellations. Its
      design prioritizes security and a customer-focused approach, ensuring travelers experience a
      seamless and efficient service. </p>
          <section class="section" id="section_clq_xzc_gfc">
      <h3 class="title sectiontitle">Key capabilities</h3>
      <p class="p">The agent is equipped with the following pre-configured actions:</p><ul class="ul"><li class="li">
            <strong class="ph b">get_flight_info:</strong> Securely access flight details using the booking ID and last
            name, forming the basis for all subsequent operations.</li><li class="li">
            <strong class="ph b">checkin:</strong> Enable passengers to check in for their flights, capturing any special
            requests or notes during the process.</li><li class="li">
            <strong class="ph b">cancel_checkin:</strong> Process check-in cancellations, providing passengers with the
            ability to undo their check-in status.</li><li class="li">
            <strong class="ph b">lookup_flights:</strong> Searches for alternative flights based on the passenger's
            preferred new date for rescheduling.</li><li class="li">
            <strong class="ph b">reschedule_flight:</strong> Allow passengers to modify their flight bookings by searching
            for alternative flights on their preferred dates.</li><li class="li">
            <strong class="ph b">cancel_booking:</strong> Facilitate flight cancellations, offering passengers a
            straightforward way to cancel their reservations.</li><li class="li">
            <strong class="ph b">Agent handover:</strong> Seamlessly transfer complex or sensitive inquiries to a human
            agent for personalized support.</li></ul><p></p>
    </section>
          <section class="section" id="section_kgq_yzc_gfc">
      <h3 class="title sectiontitle">Using this template</h3>
      <p class="p">
        </p><ol class=""><li class="li">Import the template at the time of creating a new agent by choosing the <strong class="ph b">Cumulus
              Airline</strong> autonomous template.</li><li class="li">Explore and review the configured goal, instructions, and welcome message, and update
            them as needed.</li><li class="li">Create fulfillment flows for various actions in the linked Webex Connect tenant.
            Download the flows from  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/ai-agent-fulfilment-flows/airline%20template%20fulfilment%20flows" data-scope="external">here</a> and import them to the required
            service.</li><li class="li">Configure fulfillment for each action by selecting the appropriate Webex Connect
            service and fulfillment flows created in the above step.<ul class="ul"><li class="li">Test the agent over chat or voice by using the preview option. The sample data for
                testing these agents is available  <a title="" href="http://ec2-18-225-36-23.us-east-2.compute.amazonaws.com:5003/bookings" data-scope="external">here</a>.</li></ul></li><li class="li">
            <strong class="ph b">Deploy the agent</strong>: Import the appropriate template flows in Webex Contact Center
            flow builder or Webex Connect to deploy the agent over voice or webchat.<ol class=""><li class="li">Use the instructions provided  <a title="" href="https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-autonomous-package-tracking" data-scope="external">here</a> to setup the voice flow and use Cumulus
                Airline agent instead of Track package. </li><li class="li">For digital channels, use the instructions provided  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic" data-scope="external">here</a>. </li></ol></li><li class="li">Test the agent on the chosen channel. Try checking balance for a sample user, fetching
            transactions, disputing one of the fetched transactions, and then blocking the card. Add
            new users by using the API collection available in the step below. <p class="p">You can use the
              following details for testing purposes:</p><ul class="ul"><li class="li">Booking id: X6Q4MN and last name: Watson</li><li class="li">Booking id: R5PT9X and last name: Rivera</li></ul><p></p></li><li class="li">
            <strong class="ph b">Modify and Experiment</strong>:<ol class=""><li class="li">Add new goals or instructions to expand the agent's capabilities and observe
                changes in agent behavior. Experiment with clarification prompts, fallback
                responses, and adjust the agent’s tone and persona. </li><li class="li">Enhance the agent's knowledge by adding airline FAQs to a knowledge base and
                linking it to your agent. </li><li class="li">Update API configurations for integration with your specific backend systems by
                updating Webex Connect fulfillment flows. Reference for mock APIs used in this
                template is available  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/WEbEx-AI-Template-API/airlines%20template.postman_collection.json" data-scope="external">here</a>. </li></ol></li></ol>
      <p></p>
    </section>
        </div></article></div></article></div></div><div id="concept-template_e5d845d1-de58-4dab-8e82-d8e42f6661bd" class="tab-pane fade"><div><article class="topic concept" id="concept-template_e5d845d1-de58-4dab-8e82-d8e42f6661bd"><div class="body conbody" id="">
        <p class="p"> The following templates are available for creating scripted AI agents. </p>
      </div><div><article class="topic concept" id="concept-template_8c5068aa-2f60-44c7-8fbe-41c86929e8dd"><h2>Doctor’s appointment</h2><div class="body conbody" id="">
          <p class="p">This template demonstrates a scripted AI agent for managing doctor appointment bookings and
      cancellations. This agent is designed to guide users through structured conversations, using
      developer-defined training data to handle intents like booking and canceling appointments. It
      showcases how to use platform features like context and custom events for dynamic interactions
      and how to integrate third-party APIs on voice and digital channels.</p>
          <section class="section" id="section_fwq_ryc_gfc">
      <h3 class="title sectiontitle">Core features</h3>
      <p class="p">
        </p><ul class="ul"><li class="li">
            <strong class="ph b">Intent and entity detection</strong>—The agent detects user intents to detect intents for
            appointment booking and canceling. Based on the intent detected, it proceeds to capture
            entities/slots to complete the intents.</li><li class="li">
            <strong class="ph b">Context management</strong>—Routes users to appropriate intents (for example, confirming
            or declining an appointment slot) based on their responses.</li><li class="li">
            <strong class="ph b">Custom Events</strong>—Facilitates communication between the AI agent and Webex Contact
            Center flow for fulfillment tasks.</li><li class="li">
            <strong class="ph b">AI agent deployment on voice or digital channels</strong>—This agent is packaged with
            accompanying voice and digital channel flows that let developers deploy the agent on
            these channels.</li></ul>
      <p></p>
    </section>
          <section class="section" id="section_ekt_syc_gfc">
      <h3 class="title sectiontitle">Using this template</h3>
      <ol class=""><li class="li">Import the template at the time of creating a new agent by choosing the <strong class="ph b">Doctor's
            Appointment</strong> scripted template.</li><li class="li">Explore the configuration by reviewing the intents and the linked slots, how context is
          used to manage user responses like "yes" or "no" after a slot is presented, how <strong class="ph b">custom
            events</strong> are set up to interact with WxCC flow builder. Publish the agent upon
          reviewing the configuration.</li><li class="li">
          <strong class="ph b">Deploy the agent</strong>: Import the appropriate template flows in WxCC flow builder or
          Webex Connect to deploy the agent over voice or web chat. <ol class=""><li class="li">Use the instructions provided here to set up the voice flow:  <a title="" href="https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-scripted-doctors-appointment-booking" data-scope="external">AI Agent Scripted (Doctor's Appointment
                Booking)</a>. </li><li class="li">For digital channels, use the instructions provided here:  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-scripted-doctor-appointment" data-scope="external">AI Agent Scripted Doctor Appointment </a>.</li></ol>
        </li><li class="li">Test the Agent on the channel of your choice from step 3. Try booking an appointment by
          providing preferences for the date, time, and reason for the visit. Attempt canceling an
          appointment by entering patient details.</li><li class="li">
          <strong class="ph b">Modify and Experiment</strong>: <ol class=""><li class="li">Customize the responses to fit your organization's tone or style.</li><li class="li">Update the API configurations for integration with your specific backend systems.
              Reference for mock APIs used in this template is available here  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API" data-scope="external">Webex Contact Center API Samples</a>.</li><li class="li">Add new intents, such as rescheduling an appointment, to expand functionality.</li></ol>
        </li></ol>
    </section>
          <section class="section" id="section_zp1_5yc_gfc">
      <h3 class="title sectiontitle">Expected outcomes</h3>
      <p class="p">After working with the <strong class="ph b">Doctor's Appointment</strong> template, you will:</p><ul class="ul"><li class="li">Understand how to configure intents, entities, and ways to link them to structure a
            conversation.</li><li class="li">Discover how to manage structured conversations using context.</li><li class="li">Gain familiarity with custom events to manage the switching of control between the AI
            agent and the voice flow.</li><li class="li">Learn how to configure fulfillment for various intents on digital channels.</li></ul><p></p>
    </section>
        </div></article></div><div><article class="topic concept" id="concept-template_e24d61f5-2ad1-4644-9410-dc5b10c28b07"><h2>Track package</h2><div class="body conbody" id="">
          <p class="p">The template showcases how to build a simple AI agent for tracking packages. This agent
      demonstrates how to set up an intent and integrate fulfillment to fetch real-time package
      status through a third-party API. Designed for both voice and digital channels, this template
      is ideal for learning the basics of intent configuration and API-based fulfillment.</p>
          <section class="section" id="section_uc1_bzc_gfc">
      <h3 class="title sectiontitle">Core features</h3>
      <p class="p">
        </p><ul class="ul"><li class="li">
            <strong class="ph b">Input Validation</strong>—Ensures the package number follows the alphanumeric format (in
            this case, a few alphabets followed by six numbers).</li><li class="li">
            <strong class="ph b">Third-Party API Integration</strong>—Fetches package status using an external API using
            Webex Connect flows for digital channels and custom events through Webex Contact Center
            flow builder for voice.</li></ul>
      <p></p>
    </section>
          <section class="section" id="section_dlh_czc_gfc">
      <h3 class="title sectiontitle">Using this template</h3>
      <p class="p">
        </p><ol class=""><li class="li">Import the template at the time of creating a new agent by choosing the <strong class="ph b">Track
              package</strong> scripted template.</li><li class="li">Explore the configuration by reviewing the intents and the linked slots, how context
            is used to manage user responses like "yes" or "no" after a slot is presented, how
              <strong class="ph b">custom events</strong> are set up to interact with WxCC flow builder. Publish the agent
            upon reviewing the configuration.</li><li class="li">
            <strong class="ph b">Deploy the agent</strong>: Import the appropriate template flows in WxCC flow builder or
            Webex Connect to deploy the agent over voice or web chat.<ul class="ul"><li class="li">Use the instructions provided here to import the <strong class="ph b">voice</strong> flow:  <a title="" href="https://help.webex.com/en-us/article/nhovcy4/Build-and-manage-flows-with-Flow-Designer#ai-agent-scripted-package-tracking" data-scope="external">AI Agent Scripted (Package Tracking)</a>.</li><li class="li">For <strong class="ph b">digital</strong> channels, use the AI Agent Livechat generic template and add
                fulfillment in the flow:  <a title="" href="https://help.webexconnect.io/docs/using-ai-agent-flow-templates#ai-agent-livechat-generic" data-scope="external">AI Agent Livechat generic</a>. Refer to the ‘AI
                Agent Scripted Doctor Appointment’ flow for guidelines on how to add fulfillment or
                refer to the chapter named ‘Configuring AI Agent Fulfillment for scripted agents’ in
                this Vidcast:  <a title="" href="https://app.vidcast.io/share/0b66bed4-8054-4da5-975b-941f85ce4ba3?t=740" data-scope="external">Webex AI Agent: Using AI agents on digital
                  channels</a>.</li><li class="li">API reference for adding and tracking packages:  <a title="" href="https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/WEbEx-AI-Template-API" data-scope="external">Webex Contact Center API Samples</a>.</li></ul></li><li class="li">Test the Agent on the channel of your choice from step 3. Use <strong class="ph b">ABC123456</strong> as a
            sample package number.</li><li class="li">
            <strong class="ph b">Modify and Experiment</strong>: Change the entity type or validation format to explore how
            different entity types in the platform work. </li></ol>
      <p></p>
    </section>
          <section class="section" id="section_khc_2zc_gfc">
      <h3 class="title sectiontitle">Expected outcomes</h3>
      <p class="p">After working with the <strong class="ph b">Track package</strong> scripted template, you will:</p><ul class="ul"><li class="li">Understand how to configure intents, and how input validation with entities
            works.</li><li class="li">Get hands-on experience for configuring fulfillment for intents on digital
            channels.</li><li class="li">Gain familiarity with custom events to manage the switching of control between the AI
            agent and the voice flow.</li></ul><p></p>
    </section>
        </div></article></div></article></div></div></div></div><p class="topictitle1" id="">
</p></article>
  </main>
</div>