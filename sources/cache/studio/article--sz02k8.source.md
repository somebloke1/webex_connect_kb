<div class="article-content" id="content">
  <main role="main">
    <article data-role="Administrator" data-product="Webex Contact Center" data-operatingsystem="Web Browser" role="article">
      <nav>
        <ul class="simple">
          <li class="olchildlink">
            <a href="#concept-template_b4a6c683-e86e-44d4-964a-c7060230c526">Intents</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_b150cc96-f8db-484d-8cd5-e7cbbef3bb24">Contexts</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_4bcc12bf-2c65-4ab7-b7bd-e63252bdfb73">Entities</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_9411b41f-8060-4f42-94ea-6e3ddb079298">Responses</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_2642b8de-7fd8-4ff0-a719-a02dd8a058ad">Response designer</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_352cad79-2ed2-433b-a37d-658b8e003604">List of common response variables</a>
          </li>
        </ul>
      </nav>
  
  
  <div><article class="topic concept" id="concept-template_b4a6c683-e86e-44d4-964a-c7060230c526"><h2>Intents</h2><div class="body conbody" id="">
      <p class="p">
        <span class="ph uicontrol">Intent</span> is a core component of the Webex AI Agent Studio platform that enables the AI agent to understand and respond to your input effectively. It
      represents a specific task or action that you want to accomplish during a conversation. You
      can define all intents that correspond to the tasks you want to perform. The accuracy of
      intent classification directly impacts the AI agent's ability to provide relevant and helpful
      responses. Intent classification is the process of identifying intent based on your input,
      allowing the AI agent to respond in a meaningful and contextually relevant manner. For details
      on how to create intents, see  <a title="" href="https://help.webex.com/article/ncs9r37/#task-template_6361ba29-ee9e-4b62-b9b5-b80cfe6652e7" data-scope="external">Create an intent</a>.</p>
      <section class="section" id="section_o21_vjm_vcc">
      <h3 class="title sectiontitle">System intents</h3>
      <ul class="ul"><li class="li"><strong class="ph b">Default Fallback Intent</strong>—An AI agent's capabilities are inherently limited by the
          intents that are designed to recognize and respond to. While an enterprise can't
          anticipate every possible question you might ask, the <span class="ph uicontrol">default fallback
            intent</span> can help conversations to be on track.<p class="p">By implementing a default
            fallback intent, AI agent developers can ensure that the AI agent gracefully handles
            unexpected or out of scope queries, redirecting the conversation back to known
            intents.</p><p class="p">AI agent developers need not add specific utterances to the fallback
            intent. The agent can be trained to automatically trigger the fallback intent when it
            encounters known out of scope questions that might otherwise be incorrectly categorized
            into other intents.</p><p class="p">For example, in a banking AI agent, customers might attempt to
            inquire about loans. If the AI agent is not configured to handle loan-related inquiries,
            these queries can be incorporated as training phrases within the <strong class="ph b">default fallback
              intent</strong>. When a customer queries about loans at any point in the conversation, the
            AI agent recognizes the query as falling outside of its defined intents and triggers the
            fallback response. This ensures a more appropriate response.</p><div class="olh_note"><div class="note__content"><div role="note" class="olh_note"><div class="note-container"><span class="svg-container"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 22 22" height="22" width="22" aria-hidden="true"><path fill="#1170CF" d="M15.8125 2.75H6.1875C5.27615 2.75107 4.40243 3.11358 3.75801 3.75801C3.11358 4.40243 2.75107 5.27615 2.75 6.1875V15.8125C2.75107 16.7239 3.11358 17.5976 3.75801 18.242C4.40243 18.8864 5.27615 19.2489 6.1875 19.25H15.8125C16.7239 19.2489 17.5976 18.8864 18.242 18.242C18.8864 17.5976 19.2489 16.7239 19.25 15.8125V6.1875C19.2489 5.27615 18.8864 4.40243 18.242 3.75801C17.5976 3.11358 16.7239 2.75107 15.8125 2.75ZM17.875 15.8125C17.8744 16.3593 17.6569 16.8836 17.2702 17.2702C16.8836 17.6569 16.3593 17.8744 15.8125 17.875H6.1875C5.64068 17.8744 5.11642 17.6569 4.72976 17.2702C4.34309 16.8836 4.1256 16.3593 4.125 15.8125V6.1875C4.1256 5.64068 4.34309 5.11642 4.72976 4.72976C5.11642 4.34309 5.64068 4.1256 6.1875 4.125H15.8125C16.3593 4.1256 16.8836 4.34309 17.2702 4.72976C17.6569 5.11642 17.8744 5.64068 17.875 6.1875V15.8125Z"></path><path fill="#1170CF" d="M15.125 6.1875H6.875C6.69266 6.1875 6.5178 6.25993 6.38886 6.38886C6.25993 6.5178 6.1875 6.69266 6.1875 6.875C6.1875 7.05734 6.25993 7.2322 6.38886 7.36114C6.5178 7.49007 6.69266 7.5625 6.875 7.5625H15.125C15.3073 7.5625 15.4822 7.49007 15.6111 7.36114C15.7401 7.2322 15.8125 7.05734 15.8125 6.875C15.8125 6.69266 15.7401 6.5178 15.6111 6.38886C15.4822 6.25993 15.3073 6.1875 15.125 6.1875Z"></path><path fill="#1170CF" d="M15.125 9.625H6.875C6.69266 9.625 6.5178 9.69743 6.38886 9.82636C6.25993 9.9553 6.1875 10.1302 6.1875 10.3125C6.1875 10.4948 6.25993 10.6697 6.38886 10.7986C6.5178 10.9276 6.69266 11 6.875 11H15.125C15.3073 11 15.4822 10.9276 15.6111 10.7986C15.7401 10.6697 15.8125 10.4948 15.8125 10.3125C15.8125 10.1302 15.7401 9.9553 15.6111 9.82636C15.4822 9.69743 15.3073 9.625 15.125 9.625Z"></path><path fill="#1170CF" d="M10.3125 13.0625H6.875C6.69266 13.0625 6.5178 13.1349 6.38886 13.2639C6.25993 13.3928 6.1875 13.5677 6.1875 13.75C6.1875 13.9323 6.25993 14.1072 6.38886 14.2361C6.5178 14.3651 6.69266 14.4375 6.875 14.4375H10.3125C10.4948 14.4375 10.6697 14.3651 10.7986 14.2361C10.9276 14.1072 11 13.9323 11 13.75C11 13.5677 10.9276 13.3928 10.7986 13.2639C10.6697 13.1349 10.4948 13.0625 10.3125 13.0625Z"></path></svg></span>
            <p class="p">The fallback intent:</p><ul class="ul"><li class="li">shouldn’t have any slots associated with it.</li><li class="li">must use the default fallback template key for its response.</li></ul><p></p>
          </div></div></div></div></li><li class="li"><strong class="ph b">Help</strong>—This intent is designed to address customer inquiries about the AI agent's
          capabilities. When customers are unsure of what they can accomplish or encounter
          difficulties during a conversation, they often seek assistance by asking for
            <code class="ph codeph">help.</code>
          <p class="p">By default, the response for the help intent is mapped to the <code class="ph codeph">Help
              message</code> template key. However, AI agent developers can customize the response
            or change the associated template key to provide more tailored and informative
            guidance.</p><p class="p">It’s recommended to convey the AI agent's capabilities at a high level,
            providing customers with a clear understanding of what they can do next.</p></li><li class="li"><strong class="ph b">Talk to an agent</strong>—This intent enables customers to request assistance from a human
          agent at any stage of their interaction with the AI agent. When this intent is invoked,
          the system automatically initiates a transfer to a human agent. The default response
          template for this intent is <code class="ph codeph">agent handover</code>. While there are no UI
          restrictions on changing the response template key, altering it won’t affect the outcome
          of the human handover.</li></ul>
    </section>
      <section class="section" id="section_a1n_npm_vcc">
      <h3 class="title sectiontitle">Small talk intents</h3>
      <p class="p">All newly created AI agents include four predefined small talk intents to handle common
        customer greetings, expressions of gratitude, negative feedback, and farewells:</p><ul class="ul"><li class="li">Greetings</li><li class="li">Thank you</li><li class="li">The AI agent wasn’t helpful</li><li class="li">Goodbye</li></ul>These intents and their corresponding responses are available by default in every AI
        agent. However, you can customize or delete them to align with your specific use case and
        the desired conversational flow.<p></p>
    </section>
    </div><div><article class="topic concept" id="concept-template_b150cc96-f8db-484d-8cd5-e7cbbef3bb24"><h3>Contexts</h3><div class="body conbody" id="">
        <p class="p">Context makes agent-customer interactions simpler and more concise. AI agent easily
      understands phrases like "I want to buy that" when there's enough context to identify what
      "that" refers to. Contexts help in achieving clarity in interactions with customers. Such
      expressions can be aligned with an intent if the appropriate context is provided.</p>
        <p class="p">To enable follow-up intents and organize ways to structure the flow of a conversation, each
      intent can be configured with entry context and exit context. This context variable is stored
      for each session and the state of this variable changes based on intents that are invoked over
      the course of a session.</p>
        <section class="section" id="section_t1b_th1_v2c">
      <h4 class="title sectiontitle">Entry context</h4>
      <p class="p">Entry contexts control whether an intent can be matched with the end-user query based on
        the active context of the session. When context is present in a session, the following rules
        are applied for intent matching: </p><ul class="ul"><li class="li">
            <p class="p">An intent with entry contexts will only be matched if the active context in the
              session already contains all the required entry context values. In other words, the
              entry context of an intent must be a subset of the active context for it to be
              matched.</p>
          </li><li class="li">
            <p class="p">For all intents satisfying the above rule, preference is given to intents whose input
              context matches the active more closely if the confidence scores for multiple intents
              are the same. In other words, the input context will be used for tie-breaking partial
              matches. </p>
          </li></ul><p></p>
    </section>
        <section class="section" id="section_vsv_xh1_v2c">
      <h4 class="title sectiontitle">Exit context</h4>
      <p class="p">Exit contexts control the active contexts for a session. An exit context contains the
        context value string and the duration of that context. When an intent is completed (all the
        slots are filled and the final response is invoked), the configured exit contexts for that
        intent become exit for their respective durations. Developers can configure a maximum of 15
        exit contexts for a particular intent. An exit context can be added by pressing the
        enter/return key after typing the context.</p>
    </section>
      </div></article></div></article></div>
  <div><article class="topic concept" id="concept-template_4bcc12bf-2c65-4ab7-b7bd-e63252bdfb73"><h2>Entities</h2><div class="body conbody" id="">
      <p class="p">Entities are the building blocks of conversations. They are essential elements that the AI
      agent extracts from user utterances. Entities represent specific pieces of information, such
      as product names, dates, quantities, or any other significant group of words. By effectively
      identifying and extracting entities, the AI agent can better understand user intent and
      provide more accurate and relevant responses. For details on how to create an entity, see
         <a title="" href="https://help.webex.com/en-us/article/preview/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_5e5dea5a-2b74-4883-a52f-8b70e07671b7" data-scope="external">Create an entity</a>.</p>
      <section class="section" id="section_gsf_xqw_1dc">
      <h3 class="title sectiontitle">Entity types</h3>
      <p class="p">
        Webex AI Agent Studio offers 11 prebuilt entity types to capture various types of user data. You can also
        create any of the following custom entities.</p>
      <p class="p"><strong class="ph b">Custom Entities</strong></p>
      <p class="p">These entities are configurable and allow developers to capture use-case specific
        information. </p>
      <ul class="ul"><li class="li">
          <p class="p">Custom list—Define lists of expected strings to capture specific data points not covered by prebuilt entities. You can add multiple synonyms against each string. For example, a custom pizza size entity.</p>
        </li><li class="li">
          <p class="p">Regex—Use regular expressions to identify specific patterns and extract corresponding data. For example, a phone number regex, as in <code class="ph codeph">123-123-8789</code></p>
        </li><li class="li">
          <p class="p">Digits—Capture fixed-length numerical inputs with high accuracy, especially in voice interactions. We use this as an alternative to Custom and Regex entity types in nonvoice interactions. For example, define a length of five to detect a five-digit account number.</p>
        </li><li class="li">
          <p class="p">Alphanumeric—Capture combinations of letters and numbers, providing accurate recognition for both voice and nonvoice inputs.</p>
        </li><li class="li">
          <p class="p">Free form—Capture flexible data points that are difficult to define or validate.</p>
        </li><li class="li">
          <p class="p">Map location (WhatsApp)—Extract location data shared by you on the WhatsApp channel.</p>
        </li></ul>
      <p class="p"><strong class="ph b">System Entities</strong><table border="1" width="100%"><thead><tr><th align="" font-weight="bold" id="">Entity name</th><th align="" font-weight="bold" id="">Description</th><th align="" font-weight="bold" id="">Example input</th><th align="" font-weight="bold" id="">Example output</th></tr></thead><tbody><tr><td align="" headers="">Date</td><td align="" headers="">Parses dates in natural language to a standard date format</td><td align="" headers="">“july next year”</td><td align="" headers="">01/07/2020</td></tr><tr><td align="" headers="">Time</td><td align="" headers="">Parses time in natural language to a standard time format</td><td align="" headers="">5 in the evening</td><td align="" headers="">17:00</td></tr><tr><td align="" headers="">Email</td><td align="" headers="">Detects email addresses</td><td align="" headers="">write to me at  <a title="" href="mailto:info@cisco.com" data-scope="external">info@cisco.com</a></td><td align="" headers=""> <a title="" href="mailto:info@cisco.com" data-scope="external">info@cisco.com</a></td></tr><tr><td align="" headers="">Phone number</td><td align="" headers="">Detects common phone number</td><td align="" headers="">call me at 9876543210</td><td align="" headers="">9876543210</td></tr><tr><td align="" headers="">Monetary units</td><td align="" headers="">Parses currency and amount</td><td align="" headers="">I want 20$</td><td align="" headers="">20$</td></tr><tr><td align="" headers="">Ordinal</td><td align="" headers="">Detects ordinal number</td><td align="" headers="">Fourth of ten people</td><td align="" headers="">4th</td></tr><tr><td align="" headers="">Cardinal</td><td align="" headers="">Detects cardinal number</td><td align="" headers="">Fourth of ten people</td><td align="" headers="">10</td></tr><tr><td align="" headers="">Geolocation</td><td align="" headers="">Detects geographic locations (cities, countries etc.)</td><td align="" headers="">I went swimming in the Thames in London UK</td><td align="" headers="">London, UK</td></tr><tr><td align="" headers="">Person names</td><td align="" headers="">Detects common names</td><td align="" headers="">Bill Gates of Microsoft</td><td align="" headers="">Bill Gates</td></tr><tr><td align="" headers="">Quantity</td><td align="" headers="">Identifies measurements, as of weight or distance</td><td align="" headers="">We’re 5km away from Paris</td><td align="" headers="">5km</td></tr><tr><td align="" headers="">Duration</td><td align="" headers="">Identifies time periods</td><td align="" headers="">1 week of vacation</td><td align="" headers="">1 week</td></tr></tbody></table></p>
      <p class="p">You can edit created entities from the entities tab. Linking entities to an intent annotates your utterances with detected entities as you add them.</p>
    </section>
    </div></article></div>
  <div><article class="topic concept" id="concept-template_9411b41f-8060-4f42-94ea-6e3ddb079298"><h2>Responses</h2><div class="body conbody" id="">
      <p class="p">Responses are the messages that your AI Agent sends to customers in response to their queries
      or intents. You can create responses that include: </p><ul class="ul"><li class="li"><strong class="ph b">Text</strong>—Plain text messages for direct communication.</li><li class="li"><strong class="ph b">Multimedia</strong>—Images, audio, or video elements to enhance the user experience.</li></ul><p></p>
      <p class="p">For details on how to create responses, see  <a title="" href="https://help.webex.com/article/ncs9r37/#task-template_336f85da-d3db-4427-b942-d5821752e630" data-scope="external">Create a response</a>.</p>
      <section class="section" id="section_vwb_ldk_g2c">
      <h3 class="title sectiontitle">System responses</h3>
      <p class="p">The following pre-configured system responses are available for the scripted AI agent. You
        can customize the messages for the default system responses. However, you cannot delete
        these responses.</p>
      <ul class="ul"><li class="li">
          <p class="p">Welcome message </p>
        </li><li class="li">
          <p class="p">Response suggestion </p>
        </li><li class="li">
          <p class="p">Partial message </p>
        </li><li class="li">
          <p class="p">Fallback message </p>
        </li><li class="li">
          <p class="p">Entity suggestion </p>
        </li><li class="li">
          <p class="p">Agent handover </p>
        </li></ul>
    </section>
      <section class="section" id="section_l2m_zdk_g2c">
      <h3 class="title sectiontitle">Small-talk responses</h3>
      <p class="p">You can customize and delete the following small-talk responses: </p><ul class="ul"><li class="li">
            <p class="p">Goodbye</p>
          </li><li class="li">
            <p class="p">Greetings </p>
          </li><li class="li">
            <p class="p">Help message</p>
          </li><li class="li">
            <p class="p">Not helpful</p>
          </li><li class="li">
            <p class="p">Thank you</p>
          </li></ul><p></p>
      <p class="p">The supported channels for which you can configure the responses are Web (default), Apple
        Messages for Business, Messenger, RCS, SMS, Voice, WhatsApp.</p>
    </section>
      <section class="section" id="section_rdk_hwj_t2c">
      
      <p class="p">
    </p></section>
    </div><div><article class="topic concept" id="concept-template_2642b8de-7fd8-4ff0-a719-a02dd8a058ad"><h3>Response designer</h3><div class="body conbody" id="">
        <p class="p">The response designer offers a user-friendly interface for creating responses without
      requiring extensive coding knowledge. The conditional responses option allows easy
      construction of responses for non-developers that the AI agent delivers to customers.</p>
        <p class="p">The response designer is designed to ensure that the user experience caters to the specific
      channel the AI agent is interacting with.</p>
        <section class="section" id="section_bgj_f1k_t2c">
      <h4 class="title sectiontitle">Supported response types for channels</h4>
      <p class="p">In Response Designer, you can configure channel-specific responses for the intents. For
        more information on how to configure various response types, see the  <a title="" href="https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#concept-template_86a220a2-df7a-4973-be7b-fa58dba3dce7" data-scope="external">Configure response types</a> section. <table border="1" width="100%"><caption><span class="table--title-label table title">Table 1. </span><span class="tabletitle">Response types for channels</span></caption><thead><tr><th align="" font-weight="bold" id="">Response type</th><th align="" font-weight="bold" id="">Description</th><th align="" font-weight="bold" id="">Supported channels</th></tr></thead><tbody><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#text-response-type-configuration" data-scope="external">Text</a></td><td align="" headers="">Simple text replies allow multiple text boxes in one response. This setup
                  breaks lengthy messages into manageable parts. You can add multiple response
                  options to your responses, and the system will randomly choose one to display,
                  ensuring dynamic interactions.</td><td align="" headers="">All</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#carousel-response-type-configuration" data-scope="external">Carousel</a></td><td align="" headers="">Rich responses consist of a single card or multiple cards displayed in a
                  carousel format.</td><td align="" headers="">Web (Default), Messenger</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#quick-reply-response-type-configuration" data-scope="external">Quick Reply</a></td><td align="" headers="">A pre-defined response that the AI agents use to respond to customer queries
                  swiftly.</td><td align="" headers="">Web (Default), SMS, Messenger, Apple Messages for Business, RCS</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#image-response-type-configuration" data-scope="external">Image</a></td><td align="" headers="">A multimedia response type where you can configure images by providing
                  URLs.</td><td align="" headers="">Web (Default), Messenger, WhatsApp</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#video-response-type-configuration" data-scope="external">Video</a></td><td align="" headers="">Renders videos in the preview based on the configured video URL.</td><td align="" headers="">Web (Default), WhatsApp</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#audio-response-type-configuration" data-scope="external">Audio</a></td><td align="" headers="">Renders audio file by providing the audio URL. It also shows the duration of
                  the audio message in the output.</td><td align="" headers="">Web (Default), WhatsApp, Webchat</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#file-response-type-configuration" data-scope="external">File</a></td><td align="" headers="">Shows/plays the file type based on the configured File URL.</td><td align="" headers="">WhatsApp</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#reply-button-response-type-configuration" data-scope="external">Reply Button</a></td><td align="" headers="">Offers quick responses from a limited set of options, such as choosing a
                  product to return. <p class="p">Each message is comprised of: </p><ul class="ul"><li class="li">Header - an optional field that can be 20 characters of text, image,
                        video, or a document.</li><li class="li">Body - a mandatory text field that can contain up to 1024 characters. </li><li class="li">Footer - an optional text field allowing up to 60 characters.</li><li class="li">Buttons - maximum of 3 text buttons with a 20-character limit.</li></ul>
                  <p></p></td><td align="" headers="">WhatsApp</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#list-messages-response-type-configuration" data-scope="external">List Message</a></td><td align="" headers="">Presents multiple options for easy user selection, suitable for various uses
                  like take-out menus or product catalogs. To set up a list message, fill in the
                  'configuration' and 'list sections' tabs. The 'configuration' screen shows the
                  message content users will see on their devices. <p class="p">Each message is comprised
                      of:</p><ul class="ul"><li class="li">
                        <p class="p">Header - an optional text field with a maximum of 60 characters.</p>
                      </li><li class="li">
                        <p class="p"> Body - a mandatory text field that can contain up to 1024
                          characters.</p>
                      </li><li class="li">
                        <p class="p">Footer - an optional text field allowing up to 60 characters.</p>
                      </li><li class="li">
                        <p class="p">List title - a button field with maximum of 20 characters. </p>
                      </li></ul><p></p><p class="p">List section consists of:</p><ul class="ul"><li class="li">
                        <p class="p"> Section titles - optional text field used for categorizing several rows
                          with a maximum of 24 characters.</p>
                      </li><li class="li">
                        <p class="p"> Row title - mandatory text field that is sent as a selection choice
                          accompanied by a radio button with a maximum of 24 characters.</p>
                      </li><li class="li">
                        <p class="p">Row description - optional text field that provides additional context
                          for row items with a maximum of 72 characters.</p>
                      </li></ul><p></p><p class="p">Configuring a list message on the platform will require an
                    additional field: Row ID - unique identifier for each row that will help you
                    identify the users' choice.</p></td><td align="" headers="">WhatsApp</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#numbered-list-response-type-configuration" data-scope="external">Numbered List</a></td><td align="" headers="">Quick reply in WhatsApp is defined as Numbered list. When users pick a number
                  from the list of items, the payload configured against the item is
                  received.</td><td align="" headers="">WhatsApp</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#list-picker-response-type-configuration" data-scope="external">List Picker</a></td><td align="" headers="">With the list picker, the AI agent shares a list of items with a customer
                  based on the query. This allows the customer to select the items from the given
                  options and reply with the selection. If the customer query matches partially, the
                  AI agent responds with the intents that are close to the customer query as
                  options. The partial match responses are rendered only for the List Picker option
                  in the Apple Messages for Business channel.</td><td align="" headers="">Apple Messages for Business</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#time-picker-response-type-configuration" data-scope="external">Time Picker</a></td><td align="" headers="">The time picker response type lets you set up time slots for booking
                  appointments or meetings. Each section needs a title, timezone, and multiple
                  slots. Once set up for an intent, the AI agent sends these time slots to users for
                  them to choose from.</td><td align="" headers="">Apple Messages for Business</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#media-response-type-configuration" data-scope="external">Media</a></td><td align="" headers="">This template supports attachments that are in various formats such as jpeg,
                  mp3, mp4, png, pdf, and aac.</td><td align="" headers="">Apple Messages for Business</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#rich-link-response-type-configuration" data-scope="external">Rich Link</a></td><td align="" headers="">The Rich link URL is embedded in the image or a video that is in a chat
                  bubble. When you click this bubble, the customer is redirected to the website
                  specified in the image or video.</td><td align="" headers="">Apple Messages for Business</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#form-response-type-configuration" data-scope="external">Form</a></td><td align="" headers="">Business Forms Messages let you create complex, multi-page interactive
                  experiences for iOS and iPadOS using a single JSON file. This feature helps
                  businesses collect detailed customer data through an easy-to-use interface within
                  Apple Messaging. It allows for various interactions without users having to leave
                  the chat.</td><td align="" headers="">Apple Messages for Business</td></tr><tr><td align="" headers=""> <a title="" href="https://help.webex.com/article/ncs9r37#custom-events-response-type-configuration" data-scope="external">Custom Event</a></td><td align="" headers="">Provides a control over a conversation while interacting with the scripted AI
                  agent.</td><td align="" headers="">Voice</td></tr></tbody></table></p>
    </section>
      </div></article></div><div><article class="topic concept" id="concept-template_352cad79-2ed2-433b-a37d-658b8e003604"><h3>List of common response variables</h3><div class="body conbody" id="">
        <p class="p">Use the response variables in the <strong class="ph b">Rules</strong> section of the conditional response designer
      to define conditions. You can also use the response variables in the AI agent responses to
      personalize and enrich the agent responses. For more information on how to configure rules,
      see  <a title="" href="https://help.webex.com/article/ncs9r37#task-template_336f85da-d3db-4427-b942-d5821752e630" data-scope="external">Create a response</a>.</p>
        <p class="p">
      <table border="1" width="100%"><caption><span class="table--title-label table title">Table 2. </span><span class="tabletitle">Common response variables</span></caption><thead><tr><th align="" font-weight="bold" id="">Variable name</th><th align="" font-weight="bold" id="">
                <p class="p"><strong class="ph b">Variable key</strong></p>
              </th><th align="" font-weight="bold" id="">Description</th></tr></thead><tbody><tr><td align="" headers="">
                <p class="p">Entity value</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">entity.&lt;entity-name&gt; OR
                    lastdfState.model_state.entities.&lt;entity-name&gt;.value</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to use the value of entities collected from the users. For
                  example, in an appointment booking use-case where we ask the user for their
                  preferred date using an entity named ‘Date’ entity.Date returns the value provided
                  by the user.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Intent</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">intent OR lastdfState.model_state.intent.name</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to return the intent that is entered by the customer.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Event Store</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">eventStore</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access the dictionary that contains all the parameters sent in the
                  event payload of custom events through Webex Contact Center Flow Designer.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Event Store Values</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">EventStore.&lt;key&gt;</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access the values of specific keys sent in event payloads of custom
                  events through Webex Contact Center Flow Designer.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Extra parameter/Message parameter value</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">extra_params.&lt;key&gt;</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access information passed under ‘Message parameters' in the AI Agent
                  node for scripted agents. For example, if a key ‘user_plan’ is passed in the AI
                  agent node, it’s accessible as extra_params.user_plan. These values are persisted
                  for one message turn only, that is, the value for the key can only be used in the
                  response to the message that accompanied these message parameters.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Extra parameters</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">extra_params</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access the dictionary containing all values passed under ‘Message
                  parameters' in the AI Agent node for scripted agents.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Consumer data store/Customer parameters</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">consumerDataStore.extra_params</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access the dictionary containing all parameters passed under
                  'Customer parameters' in the AI Agent node for scripted agents.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Consumer data store/Customer parameter values</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">consumerDataStore.extra_params.&lt;key&gt;</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access information passed under 'Customer parameters' in the AI Agent
                  node for scripted agents. For example, if a key ‘user_name’ is passed in the AI
                  agent node, it’s accessible as consumerDataStore.extra_params.user_name</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Previous intent/Last active intent</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">lastdfState.previous_intent_model_state.intent.name</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to access the name of the intent that was active in the
                  conversation before the current intent.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Context array</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">lastdfState.context</code></p>
              </td><td align="" headers="">
                <p class="p">Use this to access the names of all the contexts present in the conversation in
                  the form of an array.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Context duration</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">LastdfState.context.&lt;context-name&gt;</code></p>
              </td><td align="" headers="">
                <p class="p">Fetches the value of the duration of a specific context.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Customer UID</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">consumerData.uid</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to access the customer’s unique ID in the AI agent response
                  conditions or content. For digital channels, the UID is configured in the flow and
                  varies per channel.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Data store variable</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">dataStore.&lt;key&gt;</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to access custom variables stored at a session level.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Agent handover by rules flag</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">messageStore.agent_handover_by_rules</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to check is the conversation was handed over to a human based
                  on any of the agent handover rules.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Matched template key</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">messageStore.templateKey</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to access the current response name.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">NLP text</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">nlp.text</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to access the unprocessed customer query.</p>
              </td></tr><tr><td align="" headers="">
                <p class="p">Processed query</p>
              </td><td align="" headers="">
                <p class="p"><code class="ph codeph">nlp.processed_query</code></p>
              </td><td align="" headers="">
                <p class="p">Use this variable to access the processed customer query.</p>
              </td></tr><tr><td align="" headers="">Transaction id</td><td align="" headers="">
                <p class="p"><code class="ph codeph">transaction_id</code></p>
              </td><td align="" headers="">Use this variable to access the transaction id.</td></tr></tbody></table>
    </p>
        <p class="p">In addition to the above, there are certain other data objects that are accessible as
      response variables. These include messageStore, newdfState, and lastdfState that contain
      metadata about the agent’s response. Developers can print this in their responses to access
      the details and use any parameters from these dictionaries in their responses. However, in
      most use-cases, the variables listed in the above table are enough to build your agent.</p>
      </div></article></div></article></div>
</article>
  </main>
</div>