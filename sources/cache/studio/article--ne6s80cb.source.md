<div class="article-content" id="content">
  <main role="main">
    <article data-role="Administrator" data-product="Webex Contact Center" data-operatingsystem="Web Browser" role="article">
  
  
  <div><article class="topic concept" id="concept-template_d9eb2478-54b8-45c4-8f25-6617c3533efb"><div class="body conbody" id="">
      <p class="p">An AI engine is the essential component that drives an AI agent. It handles user input—text
      and voice, understands the user intent, and generates the appropriate responses.</p>
    </div></article></div>
  <p class="topictitle1" id=""></p><div class="tabs-container"><ul class="nav nav-tabs"><li class="active"><a href="#concept-template_108ff606-5316-4c56-880e-4930c823d334" data-toggle="tab" class="btn btn-primary">Scripted AI agent</a></li><li><a href="#concept-template_3b6776fa-9bb5-4691-b944-c939d3d4e8ff" data-toggle="tab" class="btn btn-primary">Autonomous AI agent </a></li></ul><div class="tab-content"><div id="concept-template_108ff606-5316-4c56-880e-4930c823d334" class="tab-pane fade in active"><div><article class="topic concept" id="concept-template_108ff606-5316-4c56-880e-4930c823d334"><div class="body conbody" id="">
        <p class="p">Administrators can choose the AI engine that best aligns with how they want their scripted AI
      agents to behave. </p>
        <section class="section" id="section_vxz_hrx_r2c">
      <h2 class="title sectiontitle">Components of an AI engine </h2>
      <p class="p">The core components are relevant for scripted AI agents, but their function is slightly
        different:</p>
      <ul class="ul"><li class="li"><strong class="ph b">Natural Language Understanding (NLU)</strong>: The NLU component maps customer input to
          the intents defined in their script. It recognizes the customer's input within the
          framework.</li><li class="li"><strong class="ph b">Dialogue Management</strong>: This component manages the flow of the conversation
          according to the script. It ensures the agent follows the defined paths and provides the
          correct responses based on the recognized intent and context. </li><li class="li"><strong class="ph b">Response Retrieval:</strong> This component delivers the responses configured in the
          script.</li></ul>
      <p class="p">For voice-based interactions, in addition to the components mentioned above, the AI engine
        also includes ASR (Automatic Speech Recognition) and TTS (Text-to-Speech).</p>
    </section>
        <section class="section" id="section_lmx_fsx_r2c">
      <h2 class="title sectiontitle">How to choose the right engine</h2>
      <p class="p">
        </p><ul class="ul"><li class="li"><strong class="ph b">Webex AI Pro 2.0 (with Swiftmatch)</strong><p class="p">This is our latest generative AI-powered
              Natural Language Understanding (NLU) engine for scripted AI agents. It leverages
              advanced machine learning algorithms to interpret user inputs and accurately classify
              intents. By learning from diverse LLM generated linguistic patterns, the engine
              delivers high precision in understanding what the user wants to achieve, even when
              phrasing or word choice varies. </p><p class="p"><strong class="ph b">Key Benefits </strong></p><ul class="ul"><li class="li">
                <p class="p"><strong class="ph b">Improved intent recognition</strong>: Capable of understanding a wide range of user
                  queries, including unseen samples or input variations, enabling more accurate
                  intent classification.</p>
              </li><li class="li"><strong class="ph b">Adaptive learning</strong>: The model generalizes effectively across similar
                utterances, reducing the need for exhaustive manual examples. </li></ul><p class="p"><strong class="ph b">Configuration requirements &amp; limitations </strong></p><ul class="ul"><li class="li">
                <p class="p">Each intent must include at least 10 representative utterances to provide the
                  model with enough linguistic diversity for accurate learning. </p>
              </li><li class="li">
                <p class="p">A clear and meaningful intent description is essential, as it helps the system
                  differentiate closely related intents and maintain consistent classification
                  performance. </p>
              </li><li class="li">
                <p class="p">Insufficient or ambiguous training data may reduce classification accuracy,
                  especially for intents with overlapping language patterns.</p>
              </li></ul></li><li class="li"><strong class="ph b">Webex AI Pro 1.0 (with Swiftmatch)</strong><p class="p">This AI engine is ideal for developing AI
              agents that manage diverse user expressions while accurately mapping inputs to
              predefined intents, ensuring consistent and reliable interactions across various
              scenarios. It's useful for: </p><ul class="ul"><li class="li"><strong class="ph b">Handling smaller training data set</strong>: If the training data set has fewer
                  than 10 utterances per intent, this engine is more suitable.</li><li class="li"><strong class="ph b">Multilingual scripted agents:</strong> This is a good choice for creating agents
                  that handle conversations in multiple languages.</li><li class="li"><strong class="ph b">Scripted agents with some level of "smart matching":</strong> While the responses
                  are scripted, this AI engine offers a natural feel by matching user input to the
                  closest intent, even if the phrasing isn't exact. </li></ul><p></p><p class="p"><strong class="ph b">Benefits:</strong> Helps with input variations, better with smaller training
              data sets, has multilingual support, supports smart
                matching.</p><p class="p"><strong class="ph b">Limitations:</strong> Swiftmatch excels in its strong natural language
              understanding abilities. However, if your script requires flexibility in matching user
              input to intents—allowing for variations in phrasing—Swiftmatch might need extra data
              configuration with diverse training data. It's designed for precise and rigid
              matching, which can make handling variations more challenging.</p><p class="p"></p></li></ul>
      <p></p>
    </section>
      </div></article></div></div><div id="concept-template_3b6776fa-9bb5-4691-b944-c939d3d4e8ff" class="tab-pane fade"><div><article class="topic concept" id="concept-template_3b6776fa-9bb5-4691-b944-c939d3d4e8ff"><div class="body conbody" id="">
        <p class="p">AI engine brings together speech technology (ASR/TTS), Large Language Models (LLMs),
      intelligent guardrails, and expertly crafted system prompts together into one single selection
      choice on AI Agent Studio. </p>
        <p class="p">When creating a new AI agent, you can choose from multiple AI engines tailored to meet their
      unique needs. </p>
        <p class="p">Autonomous AI agent currently offers the following AI engine selection options:</p><ul class="ul"><li class="li"><strong class="ph b">Webex AI Pro 1.0 (to be deprecated soon)/Webex AI Pro 2.0:</strong> General purpose engine
          ideal for most contact center use cases with global language support and human-like
          interactions. To view the list of supported languages and voices, see the  <a title="" href="https://help.webex.com/en-us/article/pdef2d/Supported-languages-for-Scripted-AI-Agents" data-scope="external">Supported languages and voices</a> article. </li><li class="li"><strong class="ph b">Webex AI Pro-US 1.0 (to be deprecated soon)/Webex AI Pro-US 2.0</strong>: Localized and
          fine-tuned for regional accents offering enhanced experience, and regulatory compliance
          for US customers. Available in English only. </li><li class="li"><strong class="ph b">Webex AI Pro-Europe 1.0 (to be deprecated soon)/Webex AI Pro-Europe 2.0</strong>:
          Localized and fine-tuned for regional accents offering enhanced experience, and regulatory
          compliance for European customers. Available in English only.</li></ul><p></p>
        <div class="olh_note"><div class="note__content"><div role="note" class="olh_note"><div class="note-container"><span class="svg-container"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 22 22" height="22" width="22" aria-hidden="true"><path fill="#1170CF" d="M15.8125 2.75H6.1875C5.27615 2.75107 4.40243 3.11358 3.75801 3.75801C3.11358 4.40243 2.75107 5.27615 2.75 6.1875V15.8125C2.75107 16.7239 3.11358 17.5976 3.75801 18.242C4.40243 18.8864 5.27615 19.2489 6.1875 19.25H15.8125C16.7239 19.2489 17.5976 18.8864 18.242 18.242C18.8864 17.5976 19.2489 16.7239 19.25 15.8125V6.1875C19.2489 5.27615 18.8864 4.40243 18.242 3.75801C17.5976 3.11358 16.7239 2.75107 15.8125 2.75ZM17.875 15.8125C17.8744 16.3593 17.6569 16.8836 17.2702 17.2702C16.8836 17.6569 16.3593 17.8744 15.8125 17.875H6.1875C5.64068 17.8744 5.11642 17.6569 4.72976 17.2702C4.34309 16.8836 4.1256 16.3593 4.125 15.8125V6.1875C4.1256 5.64068 4.34309 5.11642 4.72976 4.72976C5.11642 4.34309 5.64068 4.1256 6.1875 4.125H15.8125C16.3593 4.1256 16.8836 4.34309 17.2702 4.72976C17.6569 5.11642 17.8744 5.64068 17.875 6.1875V15.8125Z"></path><path fill="#1170CF" d="M15.125 6.1875H6.875C6.69266 6.1875 6.5178 6.25993 6.38886 6.38886C6.25993 6.5178 6.1875 6.69266 6.1875 6.875C6.1875 7.05734 6.25993 7.2322 6.38886 7.36114C6.5178 7.49007 6.69266 7.5625 6.875 7.5625H15.125C15.3073 7.5625 15.4822 7.49007 15.6111 7.36114C15.7401 7.2322 15.8125 7.05734 15.8125 6.875C15.8125 6.69266 15.7401 6.5178 15.6111 6.38886C15.4822 6.25993 15.3073 6.1875 15.125 6.1875Z"></path><path fill="#1170CF" d="M15.125 9.625H6.875C6.69266 9.625 6.5178 9.69743 6.38886 9.82636C6.25993 9.9553 6.1875 10.1302 6.1875 10.3125C6.1875 10.4948 6.25993 10.6697 6.38886 10.7986C6.5178 10.9276 6.69266 11 6.875 11H15.125C15.3073 11 15.4822 10.9276 15.6111 10.7986C15.7401 10.6697 15.8125 10.4948 15.8125 10.3125C15.8125 10.1302 15.7401 9.9553 15.6111 9.82636C15.4822 9.69743 15.3073 9.625 15.125 9.625Z"></path><path fill="#1170CF" d="M10.3125 13.0625H6.875C6.69266 13.0625 6.5178 13.1349 6.38886 13.2639C6.25993 13.3928 6.1875 13.5677 6.1875 13.75C6.1875 13.9323 6.25993 14.1072 6.38886 14.2361C6.5178 14.3651 6.69266 14.4375 6.875 14.4375H10.3125C10.4948 14.4375 10.6697 14.3651 10.7986 14.2361C10.9276 14.1072 11 13.9323 11 13.75C11 13.5677 10.9276 13.3928 10.7986 13.2639C10.6697 13.1349 10.4948 13.0625 10.3125 13.0625Z"></path></svg></span>
      <p class="p">Webex AI Pro 1.0, Webex AI Pro-US. 1.0, and Webex AI Pro-Europe 1.0 will be deprecated in
        the near future.</p>
    </div></div></div></div>
        <section class="section" id="section_hqt_jrf_cgc">
      <h2 class="title sectiontitle">Components of AI engine</h2>
      <ul class="ul"><li class="li">
          <p class="p"><strong class="ph b">Large Language Model</strong>: Powers the AI Agent with it’s advanced intelligence,
            enabling it to understand complex queries, generate coherent responses, perform actions
            or answer from a knowledge base.</p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Guardrails</strong>: Enables responsible AI interactions by setting clear boundaries,
            preventing inappropriate content, and maintaining brand safety.</p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Speech-to-Text (ASR/STT):</strong> Converts spoken language into text, enabling AI agents
            to understand human speech.</p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Text-to-Speech (TTS)</strong>: Converts text into natural, human-like speech, so AI agent
            communicates clearly and engagingly. </p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Interim Response Model</strong>: Provides instant, real-time responses for user queries,
            creating a highly responsive and fluid user experience. </p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Turn Prediction Model</strong>: Intelligently anticipates when a user has finished
            speaking, facilitating natural conversational flow. </p>
        </li><li class="li">
          <p class="p"><strong class="ph b">Standalone Query Generator Model</strong>: Transforms non-contextual, incomplete or
            colloquial inputs (e.g., “interest rate”) into complete, self-contained queries (e.g.,
            “What is the interest rate for home loans?”), enabling more accurate retrieval and
            response generation. </p>
        </li></ul>
      
    </section>
        <section class="section" id="section_ux2_hky_dfc">
      <h2 class="title sectiontitle">How to choose the right engine</h2>
      <p class="p">
        </p><ul class="ul"><li class="li"><strong class="ph b">Language support </strong>: Webex AI Pro-US 1.0/Webex AI Pro-US 2.0 and Webex AI
            Pro-Europe 1.0/Webex AI Pro-Europe 2.0 support English only, while Webex AI Pro
            1.0/Webex AI Pro 2.0 supports English + various other languages in Beta. </li><li class="li"><strong class="ph b">Geo restrictions</strong>: Webex AI Pro-US 1.0/Webex AI Pro-US 2.0 is available only for
            US customers. Webex AI Pro-Europe 1.0/Webex AI Pro-Europe 2.0 is available only for EU
            customers. Webex AI Pro 1.0/Webex AI Pro 2.0 is globally available.</li><li class="li"><strong class="ph b">Voice Experience</strong>: Webex AI Pro-US 1.0/Webex AI Pro-US 2.0 and Webex AI
            Pro-Europe 1.0/Webex AI Pro-Europe 2.0 offer an enhanced human-like conversational
            experience but are limited to fewer voices, while Webex AI Pro 1.0/Webex AI Pro 2.0
            offers a wide range of voices for human-like interactions in various accents.</li></ul>
      <p></p>
    </section>
      </div></article></div></div></div></div><p class="topictitle1" id="">
</p></article>
  </main>
</div>