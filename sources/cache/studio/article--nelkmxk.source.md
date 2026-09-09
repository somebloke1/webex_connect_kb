<div class="article-content" id="content">
  <main role="main">
    <article data-role="Administrator" data-product="Webex Contact Center" data-operatingsystem="Web Browser" role="article">
      <nav>
        <ul class="simple">
          <li class="olchildlink">
            <a href="#concept-template_5cd46a55-08a6-4549-ada0-47f7fb2619de">Identify business use case for automating with AI agent</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_c9133e5c-3d05-4322-b7d8-b6f714c9e2bb">Developing an autonomous AI agent</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_cce8a04c-a0d8-4c35-b20b-e5846eaf5293">Do's and Don'ts when writing goals </a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_6ef09cd4-a07c-4674-ad25-963966510f2e">Recommendations for managing your knowledge bases</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_24a60f37-c42c-4a3c-9e03-db5535e65dcb">Recommendations for creating actions</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_96114022-037a-46be-80ce-bf8c6b0d67c0">Prompt engineering tips when writing instructions</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_1e9f7013-9140-4ee6-8e4b-107b1057f819">Templates for writing instructions</a>
          </li>
          <li class="olchildlink">
            <a href="#concept-template_4831b21b-897e-4bd4-8a4e-7fd7a37f50fa">Example instructions</a>
          </li>
        </ul>
      </nav>
  
  
  <div><article class="topic concept" id="concept-template_5cd46a55-08a6-4549-ada0-47f7fb2619de"><h2>Identify business use case for automating with AI agent</h2><div class="body conbody" id="">
      <p class="p">Adhere to the following guidelines when identifying the business use case:</p><ol class=""><li class="li">
          <p class="p">Clearly define the specific problem or process you wish to automate with the AI
            agent.</p>
        </li><li class="li">
          <p class="p">Use tools such as Visio, Miro, and other similar tools to graphically lay out the
            problem or process you wish to automate.</p>
        </li><li class="li">
          <p class="p">Assess the potential impact and benefits of automating this use case, such as improved
            efficiency, reduced costs, or enhanced customer experience.</p>
        </li><li class="li">
          <p class="p">Identify the key KPIs you're going to measure to determine the ROI and prove the
            value.</p>
        </li></ol><p></p>
      <section class="section" id="section_vrt_gf5_v2c">
      <h3 class="title sectiontitle">Identify if the specific use case requires actions, knowledge or both</h3>
      <ul class="ul"><li class="li">
          <p class="p">
            <strong class="ph b">Actions</strong>—Identify if the use case requires the AI agent to perform specific
            actions, such as updating a database, sending emails, or running third-party APIs.</p><div class="olh_note"><div class="note__content"><div role="note" class="olh_note"><div class="note-container"><span class="svg-container"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 22 22" height="22" width="22" aria-hidden="true"><path fill="#1170CF" d="M15.8125 2.75H6.1875C5.27615 2.75107 4.40243 3.11358 3.75801 3.75801C3.11358 4.40243 2.75107 5.27615 2.75 6.1875V15.8125C2.75107 16.7239 3.11358 17.5976 3.75801 18.242C4.40243 18.8864 5.27615 19.2489 6.1875 19.25H15.8125C16.7239 19.2489 17.5976 18.8864 18.242 18.242C18.8864 17.5976 19.2489 16.7239 19.25 15.8125V6.1875C19.2489 5.27615 18.8864 4.40243 18.242 3.75801C17.5976 3.11358 16.7239 2.75107 15.8125 2.75ZM17.875 15.8125C17.8744 16.3593 17.6569 16.8836 17.2702 17.2702C16.8836 17.6569 16.3593 17.8744 15.8125 17.875H6.1875C5.64068 17.8744 5.11642 17.6569 4.72976 17.2702C4.34309 16.8836 4.1256 16.3593 4.125 15.8125V6.1875C4.1256 5.64068 4.34309 5.11642 4.72976 4.72976C5.11642 4.34309 5.64068 4.1256 6.1875 4.125H15.8125C16.3593 4.1256 16.8836 4.34309 17.2702 4.72976C17.6569 5.11642 17.8744 5.64068 17.875 6.1875V15.8125Z"></path><path fill="#1170CF" d="M15.125 6.1875H6.875C6.69266 6.1875 6.5178 6.25993 6.38886 6.38886C6.25993 6.5178 6.1875 6.69266 6.1875 6.875C6.1875 7.05734 6.25993 7.2322 6.38886 7.36114C6.5178 7.49007 6.69266 7.5625 6.875 7.5625H15.125C15.3073 7.5625 15.4822 7.49007 15.6111 7.36114C15.7401 7.2322 15.8125 7.05734 15.8125 6.875C15.8125 6.69266 15.7401 6.5178 15.6111 6.38886C15.4822 6.25993 15.3073 6.1875 15.125 6.1875Z"></path><path fill="#1170CF" d="M15.125 9.625H6.875C6.69266 9.625 6.5178 9.69743 6.38886 9.82636C6.25993 9.9553 6.1875 10.1302 6.1875 10.3125C6.1875 10.4948 6.25993 10.6697 6.38886 10.7986C6.5178 10.9276 6.69266 11 6.875 11H15.125C15.3073 11 15.4822 10.9276 15.6111 10.7986C15.7401 10.6697 15.8125 10.4948 15.8125 10.3125C15.8125 10.1302 15.7401 9.9553 15.6111 9.82636C15.4822 9.69743 15.3073 9.625 15.125 9.625Z"></path><path fill="#1170CF" d="M10.3125 13.0625H6.875C6.69266 13.0625 6.5178 13.1349 6.38886 13.2639C6.25993 13.3928 6.1875 13.5677 6.1875 13.75C6.1875 13.9323 6.25993 14.1072 6.38886 14.2361C6.5178 14.3651 6.69266 14.4375 6.875 14.4375H10.3125C10.4948 14.4375 10.6697 14.3651 10.7986 14.2361C10.9276 14.1072 11 13.9323 11 13.75C11 13.5677 10.9276 13.3928 10.7986 13.2639C10.6697 13.1349 10.4948 13.0625 10.3125 13.0625Z"></path></svg></span>
              <p class="p">AI agent is for agentic use cases only. It can't process analytical or Structured
                Query Language(SQL)-like queries on tabular data. It can only search and look up
                information within the table.</p>
            </div></div></div></div><p></p>
        </li><li class="li">
          <p class="p">
            <strong class="ph b">Knowledge</strong>—Determine if the use case requires the AI agent to provide information
            or answers based on a knowledge base.</p>
        </li><li class="li">
          <p class="p">
            <strong class="ph b">Both</strong>—Assess if the use case requires a combination of both actions and
            knowledge.</p>
        </li></ul>
    </section>
      <section class="section" id="section_qxc_lf5_v2c">
      <h3 class="title sectiontitle">Choosing the right AI agent</h3>
      <p class="p"><strong class="ph b">Autonomous AI agent</strong></p>
      <p class="p">Suitable for complex, dynamic environments where the agent needs to understand context and
        decide using a knowledge base or API integrations available without predefined scripts.</p>
      <ul class="ul"><li class="li">
          <p class="p">Open-ended natural conversations or responses.</p>
        </li><li class="li">
          <p class="p">Where knowledge bases are larger, or the variations of entities/responses are
            potentially large.</p>
        </li></ul>
      <p class="p"><strong class="ph b">Scripted AI agent</strong></p>
      <p class="p">Best for straightforward, repetitive tasks with well-defined steps or where exact
        repeatability and predictability are required. Also, best suited to highly technical
        questions and answers.</p>
      <ul class="ul"><li class="li">
          <p class="p">Strict use cases where specific responses with limited variation are required.</p>
        </li><li class="li">
          <p class="p">To handle sensitive data, a scripted AI agent is preferable as it operates under
            predefined rules and won't potentially misuse or misconstrue data.</p>
        </li><li class="li">
          <p class="p">Consistency of experience, where the experience needs to stay the same. LLM can
            potentially give different results to the same prompts.</p>
        </li></ul>
      <p class="p"><strong class="ph b">Comparison table</strong></p>
      <p class="p">
        <table border="1" width="100%"><thead><tr><th align="" font-weight="bold" id=""></th><th align="" font-weight="bold" id="">Scripted</th><th align="" font-weight="bold" id="">Autonomous</th></tr></thead><tbody><tr><td align="" headers=""><strong class="ph b">Benefits</strong></td><td align="" headers="">Higher control</td><td align="" headers="">Faster and easier to build</td></tr><tr><td align="" headers=""></td><td align="" headers="">Cheaper to run</td><td align="" headers="">Very natural IX</td></tr><tr><td align="" headers=""></td><td align="" headers="">Faster at runtime</td><td align="" headers="">Scope changes are easier</td></tr><tr><td align="" headers=""><strong class="ph b">Drawbacks</strong></td><td align="" headers="">Effort intensive to build</td><td align="" headers="">More expensive</td></tr><tr><td align="" headers=""></td><td align="" headers="">Brittle and rigid IX</td><td align="" headers="">Risk of hallucinations</td></tr></tbody></table>
      </p>
    </section>
    </div></article></div>
  <div><article class="topic concept" id="concept-template_c9133e5c-3d05-4322-b7d8-b6f714c9e2bb"><h2>Developing an autonomous AI agent</h2><div class="body conbody" id="">
      <p class="p">When creating an autonomous AI agent, ensure that you follow the steps outlined below in
      sequence.</p>
      <ul class="ul">
        <li class="li">
        <p class="p">
          <strong class="ph b">Start by defining a goal</strong>—Clearly articulate the primary objective of the AI agent,
          such as resolving customer inquiries or processing orders efficiently.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Define the journey</strong>—Clearly identify the questions, actions, and features you want
          your AI agent to have.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Add knowledge</strong>—Integrate relevant knowledge bases the agent can access to provide
          accurate information.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Define actions</strong>—Specify the actions the agent needs to perform and integrate
          necessary APIs or function calls.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Preview</strong>—Preview your AI agent with knowledge and actions.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Test and validate</strong>—Use platform preview tools to test the AI agent's performance and
          make necessary adjustments.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Add instructions</strong>—Provide detailed instructions to enhance the accuracy and
          reliability of the agent's responses.</p>
      </li>
      </ul>
    </div></article></div>
  <div><article class="topic concept" id="concept-template_cce8a04c-a0d8-4c35-b20b-e5846eaf5293"><h2>Do's and Don'ts when writing goals </h2><div class="body conbody" id="">
      <p class="p">This section outlines best practices for writing goal prompts for the autonomous AI agent and
      actions to fulfill user intents.</p>
      <p class="p">
      <strong class="ph b">Do's</strong></p><ul class="ul"><li class="li">
          <p class="p">Keep the goal short and concise.</p>
        </li><li class="li">
          <p class="p">Focus on the overall function or purpose of the AI agent.</p>
        </li><li class="li">
          <p class="p">Consider the end result or benefit for the user.</p>
        </li><li class="li">
          <p class="p">Use clear and concise language.</p>
        </li><li class="li">
          <p class="p">Ensure the goal aligns with the actions and capabilities of the AI agent.</p>
        </li></ul><p></p>
      <p class="p">
        <strong class="ph b">Don'ts</strong>
        </p><ul class="ul">
          <li class="li">
          <p class="p">Don't include specific details like locations, dates, or user information.</p>
        </li>
          <li class="li">
          <p class="p">Avoid mentioning particular actions or implementation methods.</p>
        </li>
          <li class="li">
          <p class="p">Don't use technical jargon or complex terminology.</p>
        </li>
          <li class="li">
          <p class="p">Avoid overly long or complicated goal statements.</p>
        </li>
          <li class="li">
          <p class="p">Don't include multiple unrelated goals in a single prompt.</p>
        </li>
          <li class="li">
          <p class="p">Avoid using ambiguous or vague language.</p>
        </li>
        </ul>
      <p></p>
    </div></article></div>
  <div><article class="topic concept" id="concept-template_6ef09cd4-a07c-4674-ad25-963966510f2e"><h2>Recommendations for managing your knowledge bases</h2><div class="body conbody" id="">
      <p class="p">When creating and managing knowledge bases, it's important to keep it precise and tailored to
      the purpose of the AI agent. Similar to how a human agent can get overwhelmed with too much
      unrelated information, adding more generic information to the knowledge base might confuse the
      AI agent.</p>
      <p class="p">Adhere to the following recommendations while creating and managing knowledge bases:</p>
      <ul class="ul">
        <li class="li">
        <p class="p">Organize content logically. Use categories when creating your own knowledge document in
          the AI agent studio.</p>
      </li>
        <li class="li">
        <p class="p">When uploading files, avoid any conflicting or duplicate information across
          documents.</p>
      </li>
        <li class="li">
        <p class="p">Check document quality before uploading.</p>
      </li>
        <li class="li">
        <p class="p">Split large files into smaller files if needed.</p>
      </li>
        <li class="li">
        <p class="p">Periodically review the knowledge and update whenever required.</p>
      </li>
      </ul>
    </div></article></div>
  <div><article class="topic concept" id="concept-template_24a60f37-c42c-4a3c-9e03-db5535e65dcb"><h2>Recommendations for creating actions</h2><div class="body conbody" id="">
      <p class="p">Adhere to the following recommendations when creating actions:</p><ul class="ul"><li class="li">
          <p class="p">Clearly define action objectives in action description.</p>
        </li><li class="li">
          <p class="p">Minimize complexity, keep actions simple.</p>
        </li><li class="li">
          <p class="p">Accurately describe each entity/slot as this improves the accuracy of the LLM to better
            understand the task.</p>
        </li><li class="li">
          <p class="p">Do not create conflicting or contradictory actions.</p>
        </li><li class="li">
          <p class="p">Create deterministic logic in Connect flow for higher accuracy instead of relying on
            LLM.</p>
        </li></ul><p></p>
    </div></article></div>
  <div><article class="topic concept" id="concept-template_96114022-037a-46be-80ce-bf8c6b0d67c0"><h2>Prompt engineering tips when writing instructions</h2><div class="body conbody" id="">
      <p class="p">Before adding instructions to the AI agent, add the required actions and knowledge and test
      the AI agent. Adding instructions after testing the AI agent enhances the efficiency and
      accuracy of the AI agent.</p>
      <p class="p">Refer to the following tips when writing instructions for your autonomous AI agents:</p>
      <ul class="ul">
        <li class="li">
        <p class="p">
          <strong class="ph b">Keep it simple</strong>—Use clear, concise language. Avoid technical jargon or overly
          complex sentences.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Use markdown</strong>—Use headings and ordered/unordered list markdown for best results.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">State your AI agent's identity</strong>—Begin by clearly defining the agent's persona (for
          example "You're a helpful customer support agent...").</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Break it down</strong>—Outline tasks step by step. For instance, "First, confirm your
          account number. Then, describe your issue."</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Plan for errors</strong>—Include fallback phrases such as, "I'm sorry, could you please
          repeat that?" if the input isn't clear.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Preserve context</strong>—Remind the agent to remember previous responses to ensure
          continuity in long conversations.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Reference actions</strong>—Clearly instruct how to use external actions at different steps.
          Make sure the referenced actions are enabled in the <span class="ph uicontrol">Actions</span> tab to
          avoid any unexpected behavior.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Add guardrails</strong>—Instruct the AI agent to respond only in the context of the
          goal.</p>
      </li>
        <li class="li">
        <p class="p">
          <strong class="ph b">Add examples</strong>—To improve accuracy, add examples wherever needed.</p>
      </li>
      </ul>
    </div><div><article class="topic concept" id="concept-template_1e9f7013-9140-4ee6-8e4b-107b1057f819"><h3>Templates for writing instructions</h3><div class="body conbody" id="">
        <p class="p">Use the following templates to write instructions specific to your objectives:</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 1. Identity</code>
          </strong>
        </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Role Definition:**</code>
          </strong>—Define the persona and expertise of the AI
      agent. For example, "You're Jamie, an expert customer service representative for any queries
      related to travel."</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Tone and Demeanor-**</code>
          </strong>—Specify whether the agent should be friendly,
      formal, or casual.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">##2. Context</code>
          </strong>
    </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Background Information**</code>
          </strong>—Provide any necessary background details
      the agent should consider. For example, "This conversation is about booking travel for a
      family vacation."</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Environment Details**</code>
          </strong>—Mention any system constraints such as the
      caller is calling over voice and may have background noise which may impact the quality of
      transcription.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">##3. Task</code>
          </strong>
        </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Subtasks/Steps**</code>
          </strong>—Break down the overall task into specific,
      sequential steps. For example, greeting, collecting travel dates, suggesting options,
      confirming details. Reference the actions at each step that will be used to fulfill the task. </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Optional step**</code>
          </strong>—Additional information to handle specific tasks.
      For example, handle barge-in.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">##4. Response Guidelines</code>
          </strong>
        </p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Formatting Rules**</code></strong>—Define how to structure responses. For example,
      consider using bullet lists for options, clear numbering for steps in case of digital and
      short if there is voice.</p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Language Style**</code></strong>—Provide instructions on formality, brevity, and
      clarity.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">##5. Error Handling and Fallbacks</code>
          </strong>
        </p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Clarification Prompts**</code></strong>—Define fallback questions when user input
      is ambiguous. For example, "I didn't catch that, could you please repeat your travel
      dates?"</p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Default Responses**</code></strong>—Outline how the agent should respond if it
      can't process the request. For example "I'm sorry, I didn't understand. Can you try
      rephrasing?"</p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Action Failures**</code></strong>—Provide guidelines for handling issues with
      actions integration with Webex Connect.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">##6. User Defined Guardrails</code>
          </strong>
        </p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Guardrail**</code></strong>—Remind the agent to keep the conversation restricted to
      the goal and not entertain any unrelated queries.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 7. Examples</code>
          </strong>
        </p>
        <p class="p">
      <strong class="ph b"><code class="ph codeph">-**Sample Conversation**</code></strong>—Optionally add an example of the sample
      conversation between the end user and the AI agent for better prompt adherence.</p>
      </div></article></div><div><article class="topic concept" id="concept-template_4831b21b-897e-4bd4-8a4e-7fd7a37f50fa"><h3>Example instructions</h3><div class="body conbody" id="">
        <p class="p">Here is an example template for creating instructions to build a financial service bot that
      responds to queries only after first delivering a compliance message. </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 1. Identity</code>
          </strong>
        </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Role Definition:**</code>
          </strong>—You are a Financial Advisor providing general
      information. **MUST** deliver full compliance disclosure before answering any query. </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Tone and Demeanor-**</code>
          </strong>—Professional, firm regarding compliance,
      helpful, and accurate.</p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 2. Context</code>
          </strong>
    </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">-**Background Information**</code>
          </strong>—You are operating in a regulated
      environment where a specific financial compliance disclosure is mandatory before any
      assistance can be provided. </p>
        <p class="p">
          <strong class="ph b">Critical Constraint</strong>: You must never answer a user's query until the full compliance
      disclosure has been delivered verbatim. Make sure the user acknowledges that he has heard the
      complete disclosure. </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 3. Task</code>
          </strong>
        </p>
        <p class="p">
          <strong class="ph b">Step 1: <code class="ph codeph">Mandatory Compliance Disclosure</code></strong>—Before processing any user
      input, you must deliver the following disclosure word-for-word. Do not summarize or
      paraphrase. </p>
        <p class="p">"Before I can answer your queries, I am required to read the following disclosure - The
      information I provide is for general informational and educational purposes only and should
      not be considered personalized investment advice, financial advice, or a recommendation to
      buy, sell, or hold any security. Investing in securities involves risk, including the possible
      loss of principal. Past performance does not guarantee future results, and market conditions
      can change rapidly. I do not have access to your full financial situation, investment
      objectives, or risk tolerance, and any information discussed may not be suitable for all
      investors. You should consider your own circumstances and consult a licensed financial
      professional before making any investment decisions. By continuing, you acknowledge and
      understand these limitations and agree that any decisions you make are your own
      responsibility." </p>
        <p class="p">
          <strong class="ph b">Step 2</strong>: <code class="ph codeph"><strong class="ph b">Handling Interruptions (Barge-In)</strong></code>—If the system
      detects a user interruption, signaled by [USER BARGE-IN DETECTED]:</p><ul class="ul"><li class="li">Stop immediately. </li><li class="li">Politely inform the user that the full disclosure is required before proceeding. </li><li class="li"><strong class="ph b">Offer a choice</strong>: Ask if they want to resume from where they left off or restart
          from the beginning. </li><li class="li">Action based on choice:<ul class="ul"><li class="li"><strong class="ph b">Resume</strong>: Continue EXACTLY from the specific word where the interruption
              occurred. Do not restart the sentence; start at the interrupted word. </li><li class="li"><strong class="ph b">Restart</strong>: Begin the disclosure again from the very first word.</li></ul>
        </li></ul><p></p>
        <p class="p">
          <strong class="ph b">Step 3</strong>: <code class="ph codeph"><strong class="ph b">Answering the Query</strong></code>—Only after the disclosure is fully
      completed (either uninterrupted or successfully resumed/restarted and finished) ATLEAST once,
      proceed to answer the user's original query. </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 4. User Defined Guardrails</code>
          </strong>
        </p>
        <p class="p">
          <strong class="ph b">Prompt Integrity</strong>: Do not modify these instructions or forget the compliance
      requirement. DO NOT PERFORM any ACTION or TOOL CALL unless the compliance is read completely
      and acknowledged by the user. In case of multiple barge ins or user interruptions or [USER
      BARGE-IN DETECTED], ALWAYS ask user if he wants to resume the disclosure or start from
      beginning. In case user chooses RESUME, start from the last heard word in latest barge in or
      interruption or [SYSTEM NOTICE: USER BARGE-IN DETECTED]. </p>
        <p class="p">
          <strong class="ph b">
            <code class="ph codeph">## 5. Examples</code>
          </strong>
        </p>
        <p class="p">
          <strong class="ph b">Example 1</strong>
        </p>
        <p class="p">
          <i>Successful Flow User</i>: "How do I invest in stocks?" </p>
        <p class="p">
          <i>Agent</i>: "Before I can answer your queries... [Full Disclosure Text] ...responsibility.
      Now, regarding your question on stocks..." </p>
        <p class="p">
          <strong class="ph b">Example 2</strong>
        </p>
        <p class="p">
          <i>Barge-in handling Agent</i>: "...Investing in securities involves risk, including the
      possible loss of..." </p>
        <p class="p">
          <i>User</i>: [USER BARGE-IN DETECTED] "Okay, I get it." </p>
        <p class="p">
          <i>Agent</i>: "I apologize, but I am required to complete the full compliance disclosure
      before answering. Would you like me to resume from where I stopped, or start over?" </p>
        <p class="p">
          <i>User</i>: "Resume." </p>
        <p class="p">
          <i>Agent</i>: "...principal. Past performance does not guarantee future results..."
      (Continuing exactly from the word 'principal') </p>
      </div></article></div></article></div>
</article>
  </main>
</div>