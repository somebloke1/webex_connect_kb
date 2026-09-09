<div class="article-content" id="content">
  <main role="main">
    <article data-role="Administrator" data-product="Webex Contact Center" data-operatingsystem="Web Browser" role="article">
  
  
  <div><article class="topic concept" id="fulfillment-for-scripted-agents"><div class="body conbody" id="">
    <p class="p">In the context of AI agents, fulfillment refers to the execution of tasks that involve
      interacting with external systems to retrieve, manipulate, or store data through APIs. This
      article outlines the example agent created for tracking packages. You can use this agent
      template while creating a new AI agent for digital and voice interactions.</p>
  </div></article></div>
  <p class="topictitle1" id=""></p><div class="tabs-container"><ul class="nav nav-tabs"><li class="active"><a href="#digital-channels" data-toggle="tab" class="btn btn-primary">Digital</a></li><li><a href="#voice-channels" data-toggle="tab" class="btn btn-primary">Voice</a></li></ul><div class="tab-content"><div id="digital-channels" class="tab-pane fade in active"><div><article class="topic concept" id="digital-channels"><div class="body conbody" id="">
    <p class="p">For digital channels, fulfillment must be orchestrated through the connect flow used to
      deploy the AI agent. Taking the example of a package tracking agent, which you can import from
      a template while creating a new Scripted agent, the flow is also available to import while
      creating a new Webex Connect flow. In addition to fulfillment, this connect flow also routes
      the user to different agent queues based on their last intent.</p>
    <ol class="">
      <li class="li">
        <p class="p">Once you finish setting up your scripted agent, identify the responses that require
          fulfillment.</p>
        <p class="p">In the example agent, fulfillment is required for 'trackPackageResponse'.</p>
      </li>
      <li class="li">
        <p class="p">In these templates, configure a 'holding response' that will be displayed to the user
          while the fulfillment takes place.</p>
        <p class="p">In this example, a holding response is configured for 'trackPackageResponse'.</p>
      </li>
      <li class="li">
        <p class="p">In the flow, use a <strong class="ph b">Data Parser </strong>node to parse the agent session metadata (output
          variable) from the AI agent's response to obtain the response name.</p>
        <p class="p">You can obtain the sample input for the data parser node by downloading transaction info
          from sessions by selecting the appropriate transaction and picking the value of the
          'generatedDf' key from the downloaded file.</p>
      </li>
      <li class="li">
        <p class="p">If you wish to do intent-based routing at the time of agent handover, you can obtain the
          value of the previous active intent in the same step.</p>
      </li>
      <li class="li">
        <p class="p">If you don’t wish to download and parse the sample JSON, you can use
            <code class="ph codeph">\$.model_state.template_key</code> for the response name and
            <code class="ph codeph">\$.previous_intent_model_state.intent.name</code> for the previous intent
          name. </p>
        <p class="p">In our example, we use flow variables 'responseKey' and 'previousIntent' for these
          values.</p>
      </li>
      <li class="li">
        <p class="p">Use a <strong class="ph b">Branch</strong> node to check if a response needs fulfillment.</p>
        <ul class="ul">
          <li class="li">
            <p class="p">The branch node exits through the 'None of the above' node outcome for responses that
              don’t require fulfillment.</p>
          </li>
          <li class="li">
            <p class="p">In our example, since there’s a need for fulfillment for 'trackPackageResponse',
              check for the value of 'responseKey' in our branch node.</p>
          </li>
        </ul>
      </li>
      <li class="li">
        <p class="p">For responses that require fulfillment, use an <strong class="ph b">HTTP </strong>node for making external API
          calls.</p>
        <ul class="ul">
          <li class="li">
            <p class="p">You can parse useful information from the HTTP node response in the same node by
              importing a sample and obtaining output variables.</p>
          </li>
          <li class="li">
            <p class="p">In this example, we obtain 'estimatedDelivery' and 'status' of the package.</p>
          </li>
        </ul>
      </li>
      <li class="li">
        <p class="p">Process the fulfillment response using an <strong class="ph b">Evaluate </strong>node to formulate the agent
          response.</p>
        <p class="p">In our example, we initialize the 'fulfilmentResp' variable and set its value based on
          the package status and estimated delivery.</p>
      </li>
      <li class="li">
        <p class="p">Send the fulfillment response to the user and append it to the conversation.</p>
      </li>
      <li class="li">
        <p class="p">Loop back to the <strong class="ph b">Receive</strong> node to keep the conversation going between the user and
          the AI agent.</p>
      </li>
    </ol>
  </div><div><article class="topic concept" id="intent-based-agent-handover"><h2>Intent-based agent handover</h2><div class="body conbody" id="">
    <p class="p">At the time of agent handover, check for the last active intent through a <strong class="ph b">Branch</strong> node
      before the <strong class="ph b">Queue task</strong> node.</p>
    <p class="p">Check the value of 'previousIntent' and branch to different queues based on your
      requirements. In this example, if the customer asks for an agent handover after the 'Track
      Package' intent, route them to the 'Specialist' queue. All other values lead to a handoff to
      the 'Chat' queue.</p>
  </div></article></div></article></div></div><div id="voice-channels" class="tab-pane fade"><div><article class="topic concept" id="voice-channels"><div class="body conbody" id="">
    <p class="p">For voice channels, fulfillment must be orchestrated by handing the control of the
      conversation back to the voice flow through custom events and later resuming the AI agent
      conversation with the fulfillment data. For this purpose, the example scripted agent for
      tracking packages is reused. The flow is available in 'Import from templates' in the Webex
      Contact Center Flow Designer. In addition to fulfillment, this flow also routes the user to
      different agent queues based on their last intent.</p>
    <section class="section" id="section_gt5_l3z_z2c">
      <h2 class="title sectiontitle">Step-by-step guide: Fulfillment</h2>
      <p class="p">
        </p><ol class="">
          <li class="li">
            <p class="p">Add 'Custom Event' Response Type. </p>
            <ul class="ul">
              <li class="li">
                <p class="p">Locate the template key for which you want to add the custom event. In this case,
                  use the 'trackPackageResponse' template key.</p>
              </li>
              <li class="li">
                <p class="p">Add the 'custom event' response type to the template key.</p>
              </li>
            </ul>
          </li>
          <li class="li">
            <p class="p">Configure the Custom Event response.</p>
            <ul class="ul">
              <li class="li">
                <p class="p">Add Event Name and Event Payload:</p>
                <ol class="">
                  <li class="li">
                    <p class="p">For the custom event response, provide an event name. In this case,
                      ‘TrackPack_Exit’.</p>
                  </li>
                  <li class="li">
                    <p class="p">Add the event payload, which contains data that will be passed to the flow.
                      This must be in JSON format. In this example,
                        <code class="ph codeph">{"PackageNumber":"${entity.PackageNum}"}</code>.</p>
                  </li>
                </ol>
              </li>
            </ul>
          </li>
          <li class="li">
            <p class="p">Use the Event Payload in the flow.</p>
            <ul class="ul">
              <li class="li">Access <strong class="ph b">Virtual Agent V2</strong> Activity Metadata:<ol class=""><li class="li"><p class="p">In your voice flow configuration, the event payload you added is available as
                      part of the <strong class="ph b">Virtual Agent V2</strong> activity metadata.</p></li><li class="li"><p class="p">Create the flow variable PackageNum.</p></li><li class="li"><p class="p">Use a <strong class="ph b">Parse</strong> activity to select your <strong class="ph b">Virtual Agent V2</strong> activity
                      metadata as the input variable.</p></li><li class="li"><p class="p">Set the output variable to ‘PackageNum’ and its Path Expression to
                      ‘$.PackageNum’ (based on the structure of the event payload configured in
                      agent response).</p></li></ol></li>
              <li class="li">Use the Metadata in <strong class="ph b">HTTP</strong> activity:<ol class=""><li class="li"><p class="p">Use the ‘PackageNum’ variable from the processed metadata in your flow to
                      track the package.</p></li><li class="li"><p class="p">Import the attached flow to find the details of the <strong class="ph b">HTTP </strong>activity.</p></li><li class="li"><p class="p">Define flow variables ‘estimatedDelivery’ and set it to
                      ‘$.estimated_delivery’ and another flow variable ‘packStatus’ and set it to
                      $.status.</p></li></ol></li>
              <li class="li">Add conditions based on <strong class="ph b">HTTP</strong> activity:<ol class=""><li class="li"><p class="p">Add a new <strong class="ph b">Condition</strong> activity to the flow. This activity is used to
                      check the response of the <strong class="ph b">HTTP</strong> activity (whether the package exists and
                      its status).</p><p class="p">In this example, the expression <code class="ph codeph">{{ HTTPRequest_8l3.httpStatusCode ==
                        404 }}</code> is used to check if no package was found.</p></li></ol></li>
            </ul>
          </li>
          <li class="li">Add <strong class="ph b">Set Variable </strong>activity based on conditions:<ol class=""><li class="li"><p class="p">For the condition for which the package doesn’t exist:</p><ul class="ul"><li class="li">Under the branch where no package is found, add a <strong class="ph b">Set Variable</strong>
                      activity.</li><li class="li">Set the packageResp (another flow variable) to:<p class="p">No package found with
                        these details.</p></li></ul><p></p></li><li class="li"><p class="p">For the condition for which the package exists:</p><ul class="ul"><li class="li">Under the branch where a package is found (that is, HTTP status code not
                      equals 404), add another<strong class="ph b"> Set Variable</strong> activity.</li><li class="li"><p class="p">Set the packageResp (another flow variable) to:</p><p class="p">Your package has been picked up. It will be delivered by
                        {{estimatedDelivery}}.</p></li></ul><p></p></li><li class="li"><p class="p">Add two more Set variable activities to configure event name and event data. This
                  data will be passed to the Virtual Agent V2 activity.</p><ul class="ul"><li class="li"><p class="p">Create flow variables event_name and event_data.</p></li><li class="li"><p class="p">Set event_name to TrackPack_Entry and event_data to {‘packageResp’:
                        ‘{{packageResp}}’ | json}.</p></li></ul><p></p></li></ol></li>
          <li class="li">
            <p class="p">Loop back to the <strong class="ph b">Virtual Agent V2</strong> activity:</p><ul class="ul"><li class="li">Configure the Virtual Agent V2 activity:<ol class=""><li class="li"><p class="p">Connect the final <strong class="ph b">Set Variable </strong>activity to the Virtual Agent V2
                        activity.</p></li><li class="li"><p class="p">Set the Event Name to {{event_name}}.</p></li><li class="li"><p class="p">Set the Event Data to {{event_data}}.</p></li></ol></li></ul><p></p>
          </li>
          <li class="li">
            <p class="p">Handle incoming event in your virtual agent:</p>
            <ol class="">
              <li class="li">
                <p class="p">Add a New Template Key:</p>
                <ol class="">
                  <li class="li">
                    <p class="p">Go to the Responses tab on the left-hand panel.</p>
                  </li>
                  <li class="li">
                    <p class="p">Add a new template key named packageStatus.</p>
                  </li>
                </ol>
              </li>
              <li class="li">
                <p class="p">Configure Incoming Event:</p>
                <ol class="">
                  <li class="li">
                    <p class="p">Under the voice channel, set the incoming event to TrackPack_Entry (or
                      whatever was sent to the Virtual Agent V2 activity in the flow).</p>
                  </li>
                </ol>
              </li>
              <li class="li">
                <p class="p">Configure the Response:</p>
                <ol class="">
                  <li class="li">
                    <p class="p">Set the response to: &lt;speak&gt; &lt;say-as interpret-as="date"&gt;
                      ${eventStore.packageResp} &lt;/say-as&gt;. Can I help you with anything
                      else?&lt;/speak&gt;</p>
                    <p class="p">This response uses the variables sent in the payload from the flow. Any
                      variables sent as a part of event data are available for developers to access
                      as ${eventStore.&lt;variable_name&gt;}.</p>
                    <p class="p">This also uses SSML tags. In particular, the SSML tag allows you to control
                      how text is interpreted and spoken by a text-to-speech engine. This tag can be
                      used to specify how numbers, dates, times, addresses, and other text should be
                      pronounced. Here we use it for date.</p>
                  </li>
                </ol>
              </li>
            </ol>
          </li>
        </ol>
      <p></p>
    </section>
  </div><div><article class="topic concept" id="agent-routing-based-on-previous-intent"><h2>Agent routing based on previous intent</h2><div class="body conbody" id="">
    <ul class="ul">
      <li class="li">
        <p class="p">If the <strong class="ph b">Virtual Agent V2</strong> activity exits through the 'Escalated' output, use a
            <strong class="ph b">Parse</strong> activity to get the previous intent from agent metadata.</p>
      </li>
      <li class="li">
        <p class="p">Use a <strong class="ph b">Case</strong> activity to check for different values of the previous intent that
          determine the queueing logic. In this example, we check if the previous intent was 'Track
          package'.</p>
      </li>
      <li class="li">
        <p class="p">Attach the <strong class="ph b">Case </strong>activity outputs to the appropriate Queue contact edges.</p>
      </li>
    </ul>
  </div></article></div></article></div></div></div></div><p class="topictitle1" id="">
</p></article>
  </main>
</div>