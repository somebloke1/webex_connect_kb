<div class="article-content" id="content">
  <main role="main">
    <article role="article">
      <nav>
        <ul class="simple">
          <li class="olchildlink">
            <a href="#concept-template_c583a7c5-84e6-43bf-a9a3-69d1855f1b08"></a>
          </li>
          <li class="olchildlink">
            <a href="#task-template_f456c185-ae1e-457c-b33d-8663eb3a3cba">Announced transfers</a>
          </li>
          <li class="olchildlink">
            <a href="#task-template_2ec39965-15bf-4891-8073-3cd31afc018b">Silent transfers</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_5afe054a-9a6f-4387-876e-2fffe04cf18c">Best practices when creating transfer actions</a>
          </li>
        </ul>
      </nav>
  
  
  <div><article class="topic concept" id="concept-template_c583a7c5-84e6-43bf-a9a3-69d1855f1b08"><div class="body conbody" id="">
      <p class="p">The custom transfer action feature enables you to transfer calls from one AI agent to another
      AI agent, to a human agent, or to any another desired destination (voicemail box, hunt group,
      or any number) to ensure seamless customer experience. By using a transfer action, you exit
      out of the escalated path of the Virtual Agent V2 Activity in Flow Builder with metadata that
      allows you to orchestrate the next path in the conversation. See the following sections for
      more details.</p>
      <p class="p">Some business scenarios require the AI agent to announce the transfer so the customer knows
      what is happening. In other scenarios, using transfer-related language can be confusing or
      undesirable.</p>
      <p class="p">Based on your need, you can configure the transfers as:</p><ul class="ul"><li class="li"><strong class="ph b">Announced transfer</strong>: AI agent clearly informs the customer about an upcoming
          transfer (for example “Let me transfer you to a billing specialist”).</li><li class="li"><strong class="ph b">Silent transfer</strong>: AI Agent performs the transfer silently without mentioning it to
          the customer. In these scenarios, the AI agent uses neutral language (for example "Let me
          take care of that", "Please hold on a moment while I process your request").</li></ul><p></p>
      <p class="p">See the following sections for details.</p>
    </div></article></div>
  <div><article class="topic task no_summary_steps" id="task-template_f456c185-ae1e-457c-b33d-8663eb3a3cba"><h2>Announced transfers</h2><div class="body taskbody" id=""><section id="" class="section context"><div id="" class="section prereq p"><div class="tasklabel"><p class="sectiontitle tasklabel cB_Bold" font-weight="bold">Before you begin</p></div>
      <p class="p">Ensure to create multiple agents for a complex task. </p>
    </div><table border="0" id="" class="stepTable"><tbody>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">1</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Create an action:</strong>
          </p>
          <ol class="ol substeps" type="a"><li class="li substep substepexpand">
              <p id="" class="ph cmd">Define a transfer action with your specific transfer condition. </p>
            </li><li class="li substep substepexpand">
              <p id="" class="ph cmd">Turn on the <span class="ph uicontrol">Announce Transfer</span> toggle option to enable the
              announcement.</p>
              <div class="itemgroup info">
              <p class="p">See the  <a title="" href="https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_91018ba5-7914-4ad9-938f-f8837f776f8c" data-scope="external">Configure a custom transfer action</a> section
                in the Webex AI Agent Studio Administration Guide for step-by-step instructions.</p>
            </div>
            </li></ol>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">2</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Route the interaction using a flow:</strong>
        </p>
          <div class="itemgroup info">
          <p class="p">Once the flow regains control, route the interaction to a human or another AI agent.
            Use the metadata from the Virtual Agent V2 activity to identify the specific transfer
            trigger. You can use <code class="ph codeph">$.escalation_trigger</code>. For more details, see the
               <a title="" href="https://help.webex.com/en-us/article/s0qro1/Use-AI-agents-for-customer-interactions" data-scope="external">Use AI agents for customer interactions</a>
            article.</p>
        </div>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">3</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Configure Voice:</strong> Because the caller is aware of the transition, it is
          recommended to set a distinct voice using the <code class="ph codeph">Global_VoiceName</code> variable.
          For more details see the  <a title="" href="https://help.webex.com/en-us/article/pdef2d/Supported-languages-and-voices-for-AI-agents" data-scope="external">Supported languages and voices for AI agents</a>
          article.</p>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">4</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Data Sharing:</strong> Conversation history is shared automatically. You may optionally
          pass additional information using the custom data field.</p>
        </td></tr>
      </tbody></table></section></div></article></div>
  <div><article class="topic task no_summary_steps" id="task-template_2ec39965-15bf-4891-8073-3cd31afc018b"><h2>Silent transfers</h2><div class="body taskbody" id=""><section id="" class="section context"><div id="" class="section prereq p"><div class="tasklabel"><p class="sectiontitle tasklabel cB_Bold" font-weight="bold">Before you begin</p></div>
      <p class="p">Ensure to create multiple agents for a complex task.</p>
    </div><table border="0" id="" class="stepTable"><tbody>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">1</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Create an action:</strong>
          </p>
          <ol class="ol substeps" type="a"><li class="li substep substepexpand">
              <p id="" class="ph cmd">Define a transfer action with your specific transfer condition. </p>
            </li><li class="li substep substepexpand">
              <p id="" class="ph cmd">Turn off the <span class="ph uicontrol">Announce Transfer</span> toggle option to disable the
              announcement.</p>
              <div class="itemgroup info">
              <p class="p">See the  <a title="" href="https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_91018ba5-7914-4ad9-938f-f8837f776f8c" data-scope="external">Configure custom transfer action</a> section in
                the Webex AI Agent Studio Administration guide for step-by-step instructions.</p>
            </div>
            </li></ol>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">2</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Route the interaction using a flow:</strong>
          </p>
          <div class="itemgroup info">
          <p class="p">When the flow regains control, route the interaction to a human or another AI agent.
            Use the metadata from the Virttual Agent V2 activity to identify the transfer trigger.
            You can also use the <code class="ph codeph">$.escalation_trigger</code>. For more details, see the
               <a title="" href="https://help.webex.com/en-us/article/s0qro1/Use-AI-agents-for-customer-interactions" data-scope="external">Use AI agents for customer interactions</a>
            article.</p>
        </div>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">3</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Configure the Welcome Message:</strong>
          </p>
          <div class="itemgroup info">Perform the following configuration in the <span class="ph uicontrol">State Event</span> setting
          of the Virtual Agent V2 activity. Ensure <strong class="ph b">dynamic_welcome_message</strong> is set to True for
          the receiving agent to skip the static welcome prompt.<p class="p"><img width="" data-src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/495889.png" alt="" src="https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-491000/495889.png" class="image"></p></div>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">4</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Configure Voice:</strong>
        </p>
          <div class="itemgroup info">
          <p class="p">To maintain a seamless experience, it is recommended to use the same voice for the
            receiving agent using the <code class="ph codeph">Global_VoiceName</code> variable. For more details,
            see the  <a title="" href="https://help.webex.com/en-us/article/pdef2d/Supported-languages-and-voices-for-AI-agents" data-scope="external">Supported languages and voices for AI agents</a>
            article.</p>
        </div>
        </td></tr>
        <tr id="" class="li step"><td class="ordered-number" valign="middle" align="center">5</td><td border="0" valign="top" align="left">
          <p id="" class="ph cmd">
            <strong class="ph b">Data Sharing</strong>: Conversation history is shared automatically. You may optionally
          pass additional information using the custom data field.</p>
        </td></tr>
      </tbody></table></section></div></article></div>
  <div><article class="topic concept" id="concept-template_5afe054a-9a6f-4387-876e-2fffe04cf18c"><h2>Best practices when creating transfer actions</h2><div class="body conbody" id="">
      <p class="p">See the following best practices when creating transfer actions:</p>
      <ul class="ul">
        <li class="li">
          <strong class="ph b">Modularity</strong>: Use actions to keep your logic clean by separating specialized tasks
        into dedicated agents.</li>
        <li class="li">
          <strong class="ph b">Metadata</strong>: Always leverage VAV2 activity metadata to define the routing logic.</li>
        <li class="li">
          <strong class="ph b">Consistency</strong>: When performing silent transfers, maintaining the same voice profile
        helps ensure the caller perceives the interaction as a continuous experience.</li>
        <li class="li">
          <strong class="ph b">Define agent roles in transfer condition</strong>: Treat the transfer condition as an action
        description. When configuring your multi-agent setup, focus on the specific function of the
        receiving agent rather than the act of transferring. For example, describe the agent by its
        capability, such as a 'Booking Agent' that handles tasks like booking, canceling, or
        rescheduling appointments. This provides clearer context for the LLM.</li>
      </ul>
      <p class="p"> </p>
    </div></article></div>
</article>
  </main>
</div>