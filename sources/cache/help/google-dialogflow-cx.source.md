## Introduction

A Dialogflow CX agent is a virtual agent that handles multiple conversations with the end-users. It is a Natural Language Understanding (NLU) module that understands the nuances of human language. You design and build a Dialogflow agent to handle different types of conversations required for your system.

For more information, refer to [Dialogflow CX](https://cloud.google.com/dialogflow/cx/docs).

> 📘 Note
> 
> The Dialogflow CX node has two active versions - v1.0 and v1.1, both of which use the v3 API version. However, we recommend using v1.1 going forward.

## Authorization

You can add an existing authorization or create a new authorization for a Dialogflow CX node.

### Adding an Existing Authorization

You can add an existing authorization while configuring the node in the flow.

To add an existing authorization:

1. Login to the <<prodname>> platform.
2. Navigate to flow canvas. Drag drop the **Dialogflow CX** node.
3. Open the Dialogflow CX node in the flow canvas.
4. Select **Detect Intent** from the Method Name dropdown.
5. Select the required **Node Authentication** from the dropdown.

### Adding a New Authorization

You can add a new authorization at asset integration level while configuring the node if there are no existing authorizations.

To create a new authorization:

1. Login to the <<prodname>> platform.
2. Navigate to Integrations.
3. Filter the Integrations page with **Pre-built Integrations** or search for **Dialogflow CX**.
4. Select **Dialogflow CX** and click **Actions** > **Manage**.
5. On the **Manage Integrations – Dialogflow CX** screen, under **Node Authorizations**, click the dropdown in the **Action** column and then click **Add authentication**.
6. Enter an appropriate authentication name.
7. Enter the **Client ID**, and** Client Secret** details. For more information, refer to instructions on how to obtain [Client ID and Client Secret of Dialogflow CX](https://help.imiconnect.io/docs/google-dialogflow-1#obtaining-the-client-id-and-client-secret-of-dialogflow-cx).
8. Click **Authenticate**.  
   If the credentials are successfully verified by the Dialogflow CX, then a new authorization is added and the access token is saved on <<prodname>>. If the credentials are not verified successfully, you will see an error message from Dialogflow CX. Take the appropriate action based on the error.

> 📘 Note
> 
> During the addition of new authentication, you are prompted to sign in with your Gmail account to complete the OAuth 2.0 authorization with Dialogflow CX.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e8771f7-CX.jpg",
        "",
        "Screenshot of Mange Dialogflow CX Integration Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Mange Dialogflow CX Integration Page"
    }
  ]
}
[/block]


### Obtaining the Client ID and Client Secret of Dialogflow CX

To obtain the Client ID and Client Secret of Dialogflow CX project:

1. Login to the **Dialogflow Console**.
2. Navigate to APIs & Services.
3. Click **Credentials** under **APIs & Services**.
4. To create new set of credentials, click **Create Credentials**. You can also use the existing credentials, but make sure to add the correct **Authorized redirect URIs**. The Callback (authorized redirect URL) for <<prodname>> is mentioned in the ‘**Add New Authentication**’ popup.
5. Select **OAuth client ID**.
6. On the **Create OAuth client ID** page, select **Web Application** from the Application type dropdown.
7. Enter an appropriate **Name** for the OAuth 2.0 client.
8. Under **Authorized redirect URIs**, click **Add URI** and enter the <<prodname>> redirect URL mentioned within the Add New Authentication pop-up in Dialogflow CX node.
9. Click **Create**.  
   The created **Client ID** and **Client Secret** can be used for authentication in <<prodname>>.

> 📘 Note
> 
> For more details on how to add authorization on Google Dialogflow CX, refer to the ([Dialogflow CX setup and cleanup  |  Google Cloud](https://cloud.google.com/dialogflow/cx/docs/quick/setup))

Please make sure your applications, firewalls, etc. do not restrict access to these new Callback URLs in case you have an internal policy or practice to add these URLs to the allow/accept/allowed list.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/77a449e-CX.jpeg",
        "",
        "Screenshot of Creating OAuth 2.0 with Google Cloud Platform."
      ],
      "align": "center",
      "border": true,
      "caption": "Creating OAuth 2.0 with Google Cloud Platform."
    }
  ]
}
[/block]


The authorization configured is OAuth 2.0 with Google Cloud Platform, where you will be prompted to sign in with your Gmail account.

## Configuring OAuth Consent Screen

You must configure the following in the OAuth consent screen:

1. Enter App name and User support email in the App information section.
2. Click **Save and Continue**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1cb0a6d-CX1.jpeg",
        "",
        "Screenshot of OAuth Consent Screen."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of OAuth Consent Screen."
    }
  ]
}
[/block]


- Publishing Status - Select the relevant status. The available options are:
  - Testing - indicates that the app is still in the testing phase. In this status the number of users is limited up to 100.
  - In production - indicates that the app is published and is available in production. In this status any user with a Google account can access the app. Based on the configuration of your app, additional verification may be required.
- User Type - The available options are:
- External - Based on the publishing status, any user with a Google account can access the app. It is mandatory to select external.
- Internal - App is only available to internal users within your organization.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/32b665b-CX2.jpeg",
        "",
        "Screenshot of OAuth Consent Screen."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of OAuth Consent Screen."
    }
  ]
}
[/block]


3. Scopes - To configure scopes, click [here](https://cloud.google.com/dialogflow/cx/docs/concept/access-control). Click **Save and Continue**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/674bf03-CX3.jpeg",
        "",
        "Screenshot of Test Users Screen."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Test Users Screen."
    }
  ]
}
[/block]


## Agent Handover - Dialogflow CX – Detect Intent

**Agent Handover** is the process of transferring an end-user conversation from a Dialogflow virtual agent to a human agent. The transfer from virtual agent to human agent can be done when a user triggers intents.

To create an intent:

1. Log in to the [Dialogflow CX](https://dialogflow.cloud.google.com/cx/projects) using your valid Gmail credentials.  
   The following screen is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63486d8-CX4.jpeg",
        "",
        "Screenshot of Select Project popup."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Select Project popup."
    }
  ]
}
[/block]


2. Select the existing project from the list or click **New Project**.
3. Once the existing project is selected, the **Agents** page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2a9eeae-CX5.jpeg",
        "",
        "Screenshot of Agents Page."
      ],
      "align": "center",
      "caption": "Screenshot of Agents Page."
    }
  ]
}
[/block]


4. Do one of the following:
   - Select the existing agent from the list.
   - Use pre-built agents.
   - Create an agent by clicking **Create agent**.
5. Once you have selected an existing agent or created an agent, the Dialogflow CX flow builder page is displayed.

   [block:image]{"images":[{"image":["https://files.readme.io/bd2643c-CX7.jpeg","","Screenshot of Create Agent Page."],"align":"center","caption":"Screenshot of Create Agent Page."}]}[/block]
6. Click **Manage**.  
   The **Intents** page is displayed.
7. Click **Create** for creating an intent.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8df1c71-CX8.jpeg",
        "",
        "Screenshot of Intent Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Intent Page."
    }
  ]
}
[/block]


8. Fill in the details and click **Save**. The Intent is created and displayed in the list of intents. In the following image, **agent.handover** is created as an intent for handing over to a live agent.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4cbb83b-CX9.jpeg",
        "",
        "Screenshot Highlighting Agent Handover."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Highlighting Agent Handover."
    }
  ]
}
[/block]


Example : 

Once the intent is created, you can add the training phrases.

To add training phrases:

1. Navigate to the **Intents** page. 
2. Click the intent for which you want to add the training phrases.
3. Under the Training Phrases section, type a phrase and press **Enter** or click **Add**, as shown in the following example.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b5eb42e-CX10.jpeg",
        "",
        "Screenshot of Training Phrases Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Training Phrases Page."
    }
  ]
}
[/block]


The training phrases are identified by the Dialogflow by **intent.displayname** and **message body**.

Example Screenshots to configure agent handover:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a06fef0-CX11.png",
        "",
        "Screenshots of Sample Agent Handover Flow."
      ],
      "align": "center",
      "caption": "Screenshot of Sample Agent Handover Flow."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a0ae8f3-CX12.png",
        "",
        "Screenshot of Agent Handover Using Branch Node."
      ],
      "align": "center",
      "caption": "Screenshot of Agent Handover Using Branch Node."
    }
  ]
}
[/block]


## Configuring Dialogflow CX node in flows

Following is the list of Input Variables, Output Variables and Node Outcomes that will be used within Dialogflow CX node:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "h-3": "Versions",
    "0-0": "Project – contains the list of the projects created within your Dialogflow CX. If you want to use a different project for every execution, choose 'Dynamic' and specify the variable with the project Id. For more information, refer to the [Known Limitations](https://help.imiconnect.io/docs/google-dialogflow-cx#known-limitations)   section below.  \n  \nLocation – contains the location of the agent.  \n  \nAgent Name – contains the list virtual agents within your Dialogflow CX. If you want a different agent for every execution, choose 'Dynamic' and specify the variable with the Agent Id.  \n  \nSession ID – contains the  details of the session Id to maintain the context of the conversation with the Dialogflow CX agent. Each conversation is determined uniquely by a session Id. It is a string of 36 bytes in size.  \n  \nLanguage – The language of the conversation with the CX agent. Select 'Dynamic' to specify the language code at the runtime example 'en-US'.  \n  \nInput Message - Input text to be processed to CX agent. Message length must not exceed 256 characters.  \n  \nAdd Query Parameters (Toggle Button) - to send query parameters to Dialogflow CX. For more information, refer to the [Known Limitations](https://help.imiconnect.io/docs/google-dialogflow-cx#known-limitations)  section below.  \n  \nComplete Object - Select this to pass the total JSON object at one go i.e a variable that contains the JSON.  \n  \nNote: When a JSON object is pasted in the Query Parameter JSON Object, the replacement of values by variables is not supported in runtime of the flow. It is mandatory to add a JSON object or a variable before the a node is created.  \n  \nIndividual Parameters - Select this to configure each object and pass the parameters individually.",
    "0-1": "responseId – contains the unique identification number for the response.  \n  \nuserResponse – contains the details of the response from the user.  \n  \nlanguageCode – contains the code details of the language.  \n  \nagentResponse - contains the details of the response from the agent.  \n  \n_Note:If DialogflowCX responds with multiple response.To fetch the responses please follow the  below [steps](https://help.webexconnect.io/docs/google-dialogflow-cx#steps-to-retrieve-multiple-agent-response). _  \n  \ncurrentPageName – contains the details of the current page name.  \n  \ncurrentPageDisplayName - contains the details of the current page display name.  \n  \nintentName – contains the unique name for the intent.  \n  \nintentDisplayName – contains the details of display name for the intent.  \n  \nintentDetectionConfidence - displays the confidence returned by the dialogflow for the intent recognition.  \n  \ntriggeredTransitionNames - Triggered transition route Id.  \n  \nexecutionSequence - contains the list of array of execution.  \n  \nalternativeMatchedIntents - contains the next  recognised intent by dialogflow.  \n  \ntransitionTargetsChain - Page Id of the current page of dialogflow.  \n  \nsessionId – contains the details of the session id.  \n  \nmatch - contains the information of matched intent, type of match and confidence of the current match.  \n  \nresponseType – contains the details of response provided.  \n  \nresponsePayload – contains the details of the response payload.",
    "0-2": "onInvalidData  \n  \nonError  \n  \nonInvalidChoice  \n  \nonTimeout  \n  \nonauthorizationfail  \n  \ndetectIntentOnSuccess  \n  \ndetectIntentOnError",
    "0-3": "v1.0"
  },
  "cols": 4,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


### Steps to retrieve multiple agent response

If Dialogflow CX agent contains multiple responses,please follow the steps below to fetch the responses: 

1. Use the output variable named 'responsePayload' in Dialogflow CX pre-built integration. 

2. Use 'responsePayload' variable in Data Parser or Evaluate Node and parse this varaiable as it contains the entire response payload received from Dialog Flow CX REST API.

3. Extract 'responseMessages' object from responsePayload JSON object and use it in Send Node.

## Known Limitations

- When trying to add the ‘sessionEntityTypes’ parameter under ‘Add Query Parameter,’ the field (sessionEntityTypes input) has to be reselected each time a character is entered.
- When trying to add the ‘sessionEntityTypes’ parameter under ‘Add Query Parameter,’ the field (sessionEntityTypes input) shows ‘is required,’ indicating that the input box is empty. Sometimes, this can happen even if you have already entered a variable or input in the field. If you have already entered a variable or a value, the ‘is required’ error for ‘sessionEntityTypes’ input box can be ignored.
- When entering a dynamic value in the UI configuration, the dynamic input box doesn't get cleared even after clicking the close (X) icon.

## FAQs

1. What is the request timeout for Dialogflow CX node?  
   The request timeout for Dialogflow CX Node is 20 seconds i.e., the Dialogflow CX node must respond within 20 seconds after receiving a request from <<prodname>>. If the Dialogflow CX node does not respond to the request received within 20 seconds, the Dialogflow CX node will timeout in <<prodname>> flow through the onTimeout edge.
2. Does the Dialogflow CX integration support Dialogflow service account?  
   No, the current integration uses the standard Dialogflow CX OAuth 2.0 (authorization code for grant type) for authentication with Dialogflow servers.