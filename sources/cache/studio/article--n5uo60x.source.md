<div class="article-content" id="content">
  <main role="main">
    <article data-role="Administrator" data-product="Webex Contact Center" data-operatingsystem="Web Browser" role="article">
  
  
  <p class="topictitle1" id=""></p><div class="tabs-container"><ul class="nav nav-tabs"><li class="active"><a href="#concept-template_81fd0e34-034e-4039-a402-5d32793a0f6e" data-toggle="tab" class="btn btn-primary">Autonomous AI agent</a></li><li><a href="#concept-template_4cd97a0a-9ab3-4be0-bbdd-6a901166c559" data-toggle="tab" class="btn btn-primary">Scripted AI agent</a></li></ul><div class="tab-content"><div id="concept-template_81fd0e34-034e-4039-a402-5d32793a0f6e" class="tab-pane fade in active"><div><article class="topic concept" id="concept-template_81fd0e34-034e-4039-a402-5d32793a0f6e"><div class="body conbody" id="">
        <section class="section" id="section_yxm_kyg_q3c">
      <h2 class="title sectiontitle">Custom data at the beginning of session</h2>
      <p class="p">Custom data enables developers to perform the following tasks:</p><ul class="ul"><li class="li">Pass data from the client to update an autonomous agent’s design time parameters. For
            example, passing customer name for a personalized welcome message.</li><li class="li"> Update autonomous AI agent design time variables. For example, optimize goals and
            instructions for specific customers, update action description and slots with
            information that’s available with the client so that the users are not re-prompted for
            it.</li></ul><p></p>
      <div class="olh_note"><div class="note__content"><div role="note" class="olh_note"><div class="note-container"><span class="svg-container"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 22 22" height="22" width="22" aria-hidden="true"><path fill="#1170CF" d="M15.8125 2.75H6.1875C5.27615 2.75107 4.40243 3.11358 3.75801 3.75801C3.11358 4.40243 2.75107 5.27615 2.75 6.1875V15.8125C2.75107 16.7239 3.11358 17.5976 3.75801 18.242C4.40243 18.8864 5.27615 19.2489 6.1875 19.25H15.8125C16.7239 19.2489 17.5976 18.8864 18.242 18.242C18.8864 17.5976 19.2489 16.7239 19.25 15.8125V6.1875C19.2489 5.27615 18.8864 4.40243 18.242 3.75801C17.5976 3.11358 16.7239 2.75107 15.8125 2.75ZM17.875 15.8125C17.8744 16.3593 17.6569 16.8836 17.2702 17.2702C16.8836 17.6569 16.3593 17.8744 15.8125 17.875H6.1875C5.64068 17.8744 5.11642 17.6569 4.72976 17.2702C4.34309 16.8836 4.1256 16.3593 4.125 15.8125V6.1875C4.1256 5.64068 4.34309 5.11642 4.72976 4.72976C5.11642 4.34309 5.64068 4.1256 6.1875 4.125H15.8125C16.3593 4.1256 16.8836 4.34309 17.2702 4.72976C17.6569 5.11642 17.8744 5.64068 17.875 6.1875V15.8125Z"></path><path fill="#1170CF" d="M15.125 6.1875H6.875C6.69266 6.1875 6.5178 6.25993 6.38886 6.38886C6.25993 6.5178 6.1875 6.69266 6.1875 6.875C6.1875 7.05734 6.25993 7.2322 6.38886 7.36114C6.5178 7.49007 6.69266 7.5625 6.875 7.5625H15.125C15.3073 7.5625 15.4822 7.49007 15.6111 7.36114C15.7401 7.2322 15.8125 7.05734 15.8125 6.875C15.8125 6.69266 15.7401 6.5178 15.6111 6.38886C15.4822 6.25993 15.3073 6.1875 15.125 6.1875Z"></path><path fill="#1170CF" d="M15.125 9.625H6.875C6.69266 9.625 6.5178 9.69743 6.38886 9.82636C6.25993 9.9553 6.1875 10.1302 6.1875 10.3125C6.1875 10.4948 6.25993 10.6697 6.38886 10.7986C6.5178 10.9276 6.69266 11 6.875 11H15.125C15.3073 11 15.4822 10.9276 15.6111 10.7986C15.7401 10.6697 15.8125 10.4948 15.8125 10.3125C15.8125 10.1302 15.7401 9.9553 15.6111 9.82636C15.4822 9.69743 15.3073 9.625 15.125 9.625Z"></path><path fill="#1170CF" d="M10.3125 13.0625H6.875C6.69266 13.0625 6.5178 13.1349 6.38886 13.2639C6.25993 13.3928 6.1875 13.5677 6.1875 13.75C6.1875 13.9323 6.25993 14.1072 6.38886 14.2361C6.5178 14.3651 6.69266 14.4375 6.875 14.4375H10.3125C10.4948 14.4375 10.6697 14.3651 10.7986 14.2361C10.9276 14.1072 11 13.9323 11 13.75C11 13.5677 10.9276 13.3928 10.7986 13.2639C10.6697 13.1349 10.4948 13.0625 10.3125 13.0625Z"></path></svg></span>
        <p class="p">Currently, custom data for autonomous AI agents is supported through the voice channel
          only.</p>
      </div></div></div></div>
      
        <data>
          <h3>Configure Custom data</h3>
        </data>
        <p class="p">
          </p><ol class=""><li class="li">In the Webex Contact Center Flow Designer, configure the <strong class="ph b">Virtual Agent V2</strong>
              activity in the flow.</li><li class="li">In the <strong class="ph b">State Event </strong>settings, specify the following details in the <strong class="ph b">Event
                Name - Event Data</strong> columns:<ol class=""><li class="li">Leave the event name field blank.</li><li class="li">Enter the custom data that you wish to pass from the Flow Designer to the
                  autonomous AI agent.</li></ol></li></ol>
        <p></p>
        <p class="p"><img width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/493001-494000/493283.png" alt="Illustration for Custom data configuration in Virtual Agent V2 activity" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/493001-494000/493283.png" class="image"></p>
      
      
        <data>
          <h3>Access custom data in AI Agent Studio</h3>
        </data>
        <p class="p">You can access event data (configured in the Flow Designer) using the syntax
            <code class="ph codeph">{{variable name}}</code> in various sections of the autonomous agent. The
          variables passed in the custom data can be accessed in agent’s goal, welcome message,
          instructions, action description, and slot description.</p>
        <p class="p"><img width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/493001-494000/493284.png" alt="Custom data in AI agent studio" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/493001-494000/493284.png" class="image"></p>
        <p class="p">In this example, the developer uses <code class="ph codeph">{{customer_name}}</code> in the welcome
          message and <code class="ph codeph">{{calling_number}}</code> in the agent instructions.</p>
      
    </section>
        <section class="section" id="section_yrf_5wg_q3c">
      <h2 class="title sectiontitle">Custom events for fulfillment</h2>
      <p class="p">Custom event enables developers to perform the following tasks</p>
      <ul class="ul"><li class="li">Define a custom exit out from the AI agent to return control to the WxCC flow designer.
          For example, to execute fulfillment within the flow.</li><li class="li">Resume the conversation with the AI Agent by passing the fulfillment output back to the
          AI Agent from the flow. The fulfillment timeout limitation of Webex connect flow based
          fulfillment doesn't apply here.</li><li class="li">Support PCI use-cases for Autonomous agents as the PCI information stays in the bounds
          of WxCC flow builder.</li></ul>
      <p class="p">Currently, custom events for autonomous AI agents are supported through the voice channel
        only.</p>
      <data>
          <h3>Configure custom event based fulfillment in AI Agent Studio</h3>
        </data><ol class=""><li class="li">In Autonomous agent actions, create a new action where custom event based fulfillment
            is needed.</li><li class="li">In the fulfillment section, select 'Set custom logic for fulfillment' option.</li></ol><img height="" width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495236.jpg" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495236.jpg">
      
        <data>
          <h3>Access custom event data in Flow Designer</h3>
        </data>
        <p class="p">You can access the custom event name and payload from the Output Variables section of
          Virtual Agent V2 activity.</p>
        <p class="p">The action name is returned under the StateEventName variable and the collected slots
          from the action are returned as MetaData:</p>
        <p class="p"><img width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495237.jpg" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495237.jpg" class="image"></p>
      
      
        <data>
          <h3>Invoke custom event from Flow Designer</h3>
        </data>
        <ol class=""><li class="li">Execute fulfillment logic in the flow based on the action or event name received in
            the Virtual Agent V2 activity output.</li><li class="li">Create and use flow variables to dynamically update event name and event data to be
            sent back. In the below example, the event_name flow variable is set to be the same as
            event name passed by the Virtual Agent V2 activity and the event_data_string variable is
            updated to contain the output from the http activity used for communicating with
            third-party systems to get appointment availability details.<img height="" width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495238.jpg" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495238.jpg"></li><li class="li"><p class="p">In the State Event settings of Virtual Agent V2 activity, specify the following
              details in the Event Name - Event Data fields:</p><ul class="ul"><li class="li"> The variable that contains event name Virtual Agent V2 activity exited with.</li><li class="li">The variable that contains fulfillment data that must be passed back to the
                flow.</li></ul><img height="" width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495239.jpg" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/495001-496000/495239.jpg"></li></ol>
      
    </section>
      </div></article></div></div><div id="concept-template_4cd97a0a-9ab3-4be0-bbdd-6a901166c559" class="tab-pane fade"><div><article class="topic concept" id="concept-template_4cd97a0a-9ab3-4be0-bbdd-6a901166c559"><div class="body conbody" id="">
        <p class="p">Custom events enable administrators to perform the following tasks: </p>
        <ul class="ul">
          <li class="li">
        <p class="p">Pass data from the client to create dynamic responses. For example, passing customer name
          for a personalized greeting. </p>
      </li>
          <li class="li">
        <p class="p">Define a custom exit out from the AI agent to return control to the flow designer. For
          example, to execute fulfillment within the flow. </p>
      </li>
          <li class="li">
        <p class="p">Set the AI agent to begin from a custom starting point rather than the welcome prompt by
          using a custom event. </p>
      </li>
          <li class="li">
        <p class="p">Update AI agent state variables. For example, prepopulating the context or slots using
          custom data passed from the flow designer. </p>
      </li>
        </ul>
        <p class="p">Currently, custom event for scripted AI agents is supported through the voice channel
      only.</p>
        <section class="section" id="section_xqz_tqh_c2c">
          <h2 class="title sectiontitle">Configure incoming custom event in AI Agent Studio </h2>
          <p class="p">
        </p><ol class=""><li class="li">On the AI agent configuration page, create a new response in the <strong class="ph b">Responses</strong>
            tab.</li><li class="li">Under Default response, click <span class="ph uicontrol">+ </span> next to the <strong class="ph b">Default
              (Web)</strong> channel to add the <strong class="ph b">Voice </strong>channel </li><li class="li">In the <strong class="ph b">Incoming event name </strong>field, define the event name that the agent
            receives.</li></ol>
      <p></p>
          <img height="333" width="719" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487947.png" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487947.png">
        </section>
        <section class="section" id="section_byd_vr4_c2c">
      <h2 class="title sectiontitle">Invoke custom event from Flow Designer</h2>
      <p class="p"></p><ol class=""><li class="li">In the Webex Contact Center Flow Designer, configure the <strong class="ph b">Virtual Agent V2</strong>
            activity in the flow. </li><li class="li">In the <strong class="ph b">State Event</strong> settings, specify the following details in the <strong class="ph b">Event Name
              - Event Data</strong> columns:<ol class=""><li class="li">
                <p class="p">Enter the custom event name that you've configured in the <strong class="ph b">Response</strong> tab of
                  the AI agent configuration page in AI Agent Studio.</p>
              </li><li class="li">Enter the custom data that you wish to pass from the Flow Designer to the scripted
                AI agent.</li></ol></li></ol><img width="818" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487946.png" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487946.png" class="image"><p></p>
    </section>
        <section class="section" id="section_dgy_4s4_c2c">
          <h2 class="title sectiontitle">Access custom event data in AI Agent
        Studio</h2>
          <p class="p">You can access the event data (configured in the Flow Designer) in the
          <strong class="ph b">Default response</strong> section where you configured your incoming event. In the following
        figure, you can see that the custom event name "<code class="ph codeph">custom_welcome</code>" and event
        data "<code class="ph codeph">store name</code>" are passed from the Flow Designer to AI Agent
        Studio.</p>
          <img height="436" width="701" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487945.png" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487945.png">
        </section>
        <section class="section" id="section_bz4_n2p_c2c">
          <h2 class="title sectiontitle">Configure custom exit event &amp; payload in AI Agent
        Studio</h2>
          <ol class="">
            <li class="li">
          <p class="p">In the AI Agent Studio, navigate to the scripted AI agent configuration page and go to
              <strong class="ph b">Response</strong> where you want the control to be passed back to the flow designer.</p>
        </li>
            <li class="li">
          <p class="p">Add Custom Event to the <strong class="ph b">Default response</strong> section.</p>
        </li>
            <li class="li">
          <p class="p">Enter the event name and event payload data in the JSON that you want to be returned to
            the flow.</p>
        </li>
          </ol>
          <img height="434" width="694" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487944.png" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487944.png">
          <p class="p">In this example, the slots collected are
        returned to the flow with the custom exit event
      <code class="ph codeph">“order_details”</code>.</p>
        </section>
        <section class="section" id="section_n14_13p_c2c">
      <h2 class="title sectiontitle">Access custom event data in Flow Designer</h2>
      <p class="p">You can access the custom event and payload from the <strong class="ph b">Output Variables</strong> section of
          <strong class="ph b">Virtual Agent V2</strong> activity. </p>
      <p class="p">The <code class="ph codeph">Event name</code> is returned under the <code class="ph codeph">StateEventName</code>
        variable and the <code class="ph codeph">Event payload </code> is returned as <code class="ph codeph">Metadata</code> as
        shown in the following figure:</p>
      <p class="p"><img width="962" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487943.png" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487943.png" class="image"></p>
    </section>
        <section class="section" id="section_bbw_4sp_c2c">
      <h2 class="title sectiontitle">Update system values in AI Agent Studio</h2>
      <p class="p"> You can update system values such as context, intent, and slot using a special event
          <code class="ph codeph">state_update</code> and <code class="ph codeph">Event payload</code> with the values, as shown
        in the following example:</p>
      <p class="p">
        </p><pre class="codeblock"><code class="codeblock">{ 
 "intent": "order_status", 
 "slots": { 
 "first_name": "John" 
 } 
"context": {
    "track": 1
 }
} </code></pre>
      <p></p>
      <p class="p">In the above example, the intent of the scripted agent is set to
          <code class="ph codeph">order_status</code>, the slot ‘first_name’ within that intent is set to ‘John’
        and a context called ‘track’ is added to the session.</p>
      <p class="p">This event is useful for use-cases where the scripted agent conversation must be controlled
        by flow logic. Some use cases where this is especially useful include:</p>
      <ul class="ul"><li class="li">
          <p class="p"><strong class="ph b">Re-prompt the user for information if fulfillment in the flow fails</strong></p>
          <p class="p">Consider a scenario where the agent is booking an appointment for a user. After
            gathering the date and time, this information is sent to the flow through a custom
            event, which then attempts to book the appointment using an HTTPS request activity. If
            the appointment is rejected due to a scheduling conflict, the AI agent needs to request
            an alternative time slot. To handle this, the developer can use the following event
            payload:</p>
          <pre class="codeblock"><code class="codeblock">{
"intent": "book appointment",
"slots": {
"time": ""
}
}</code></pre>
          <p class="p">In this case, the value collected for time is cleared, and the AI agent prompts the
            user to provide a new one. Developers can set up conditional responses to let users know
            the previous slot was unavailable and request a new time.</p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Navigate to a different intent</strong></p>
          <p class="p">Consider a scenario where a user requests to check their balance but as a prerequisite,
            the user must first verify their identity. As part of the balance inquiry process,
            developers can send an event payload to inform the flow whether the user has already
            been verified. If verified, the system can proceed to fetch the balance; if not, the
            flow can prompt the AI agent to initiate the user verification process using the
            following event payload: </p>
          <pre class="codeblock"><code class="codeblock">{
"intent": "verify user",
}</code></pre>
          <p class="p">In this same example, let’s say that verification requires the user’s date of birth and
            pin code. Of the flow already has information about the user’s date of birth via CJDS,
            that can be passed as a slot and only pin code can be collected. The event payload for
            that will look like:</p>
          <pre class="codeblock"><code class="codeblock">{
"intent": "verify user",
"slots": {
"date of birth": "06/26/1993"
}
}</code></pre>
        </li><li class="li"><strong class="ph b">Introduce or reset context in a conversation</strong><p class="p">When the conversation context
            needs to be updated, developers can include it in the event payload for the
              <code class="ph codeph">state_update</code> event. For example, after the AI Agent collects the
            slots for the 'verify user' intent, it sets the conversation context to 'verify'. If
            verification fails in the flow, the context should be reset to prevent the user from
            accessing intents that require the 'verify' context. The event payload for this scenario
            would look like:</p><pre class="codeblock"><code class="codeblock">{
"intent": "verify user",
"slots": {
"date of birth": "",
"pincode": ""
},
"context": {
"verify": 0
}
}</code></pre></li></ul>
    </section>
        <section class="section" id="section_c1w_4sp_c2c">
      <p class="p"> </p>
    </section>
      </div></article></div></div></div></div><p class="topictitle1" id="">
</p></article>
  </main>
</div>