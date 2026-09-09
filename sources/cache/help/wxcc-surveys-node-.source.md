The Surveys node is an out-of-the-box integration and uses Survey API endpoints for integration. This integration helps you understand your customer's needs and improve your products or services to meet expectations. By integrating Surveys with <<prodname>>, the platform capabilities can be utilized in various use cases related to customer survey management. By using the Surveys pre-built node, you can generate questionnaire URLs that can be sent through different channels.

> 📘 Versions in the node
> 
> Version 1.0 of the Surveys node will be deprecated. Do not configure any new flows using this version.
> 
> In the Japan region, using v1.5 is mandatory. For other regions, we recommend using v1.2 or v1.3 or v1.4 or v1.5. The additional configurations - Name, Valid After, Valid For, and Preferred Languages - are supported only in  v1.2, v1.3, v1.4, and v1.5. These versions also eliminate the need to generate an expiry timestamp, saving you extra work.
> 
> Questionnaires configured on the Surveys platform after the release of v1.2 (August 2023) are only accessible through v1.2 or v1.3 or v1.4 or v1.5. 

> 📘 Note
> 
> While configuring the Surveys Node, if you switch the questionnaire, it is mandatory to manually select the preferred language to ensure it is correctly applied. This cache issue is part of the known backlog and is scheduled for resolution.

## Accessing the Product

To access <<prodname>>, use the directions below:

1. Enter your tenant URL in the browser address bar (e.g., https\://<tenantname>.<region>.webexconnect.io.).
2. Type your username and password to log in.
3. After you successfully log in, the dashboard appears with the Services tab in view.

## Prerequisites

The Surveys node is available by default for all WxCC-linked tenants. If your tenant is WxCC linked tenant and you are not able to find Surveys node in the flow builder, then please reach out to the support Id mentioned in the <<prodname>> tenant under Contact Support.

## Methods and Outcomes

Here’s a brief description of the methods, and corresponding output variables and node outcomes associated with the method.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.

> 📘 Note
> 
> For the Surveys node, you will have to add the authorization again by following the steps provided in the Node Authorization. If a user is using the latest version of the Surveys node, it is mandatory for a user to re-authorize the pre-built integration.

## Webex Connect Setup

1. Login to the <<prodname>> platform.
2. Create a new service if required.
3. From the toolbar on the left, navigate to **Assets** > **Apps**.
4. Click on **Configure New App** and then select the type of Digital Channel to configure the new app.
5. Click **Save**.
6. Click **Register To Webex Engage**.  
   After the app is configured, it will act as the entry point for calling into the <<prodname>> platform.

## Chat Setup in the Webex Connect Portal

1. Login to the <<prodname>> platform.
2. Navigate to **Templates**.
3. Click **Add New Template**.
4. In the **Configure New Template** page, under **Channel**, select **Live Chat / In App Messaging**.
5. Add all the configuration details and click **Save**.
6. Navigate to **Services** and select the associated service.
7. In the selected service page, click **Flows** to the top-left section of the page.
8. Following are the flows that you may mandatorily or optionally require to set-up.
   1. **Task_Routed/Task modified node** - This is an optional node for setting up flows once the customer is connected.
   2. **LiveChat node** - This is the main flow. This handles how Webex Connect is integrated with the queues setup in Contact Center Management Portal.  
      In the Pre-chat and Receive Node, make sure to select the template configured in a step above.  
      In the Queue Task node, match with the queue created in Contact Center Management Portal  
      from the Settings page, and add the Live Chat domain and App ID. The App ID is displayed on the Apps page .
   3. **Task Close node** - The node handles any logic that occurs after the customer disconnects the call. For example, we can configure to send a XM survey at this step.

## Method Name - Create a New Survey Token for a Questionnaire

Click here for more [information](https://help.webex.com/en-us/article/nlu4x20/Experience-Management---Configure-surveys-for-IVR-and-Digital-Channels-for-WebexContact-Center) on questionnaire.

### How to Fetch All Questionnaires

To fetch questionnaires:

1. Select the Method Name.
2. Select the required Node Runtime Authorization from the list.
3. Click **Fetch All Questionnaires** to fetch the questionnaires.  
   All the fetched questionnaires are pre-populated.
4. Select the required questionnaire from **Available Questionnaires**.
5. Click **Save**.

> 📘 Note
> 
> The Interaction ID and Tracking ID are recommended pre-fills for setting up the Surveys node and generating a survey URL, although they are not mandatory and are primarily used for debugging purposes. These two parameters must be unique for each survey URL. You can utilize the flow transaction ID variable or create your own ID using the Evaluate node. Please note that this information is applicable only to v1.1.
> 
> From v1.2, the Interaction ID (Task ID) is automatically configured as one of the pre-fills at the node level, and the Pre-Fills section is removed from the node UI. The pre-fill is automatically set up in the backend with the Interaction ID (Task ID).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/727be04d9758c05bfc8a96fc30e175f4dffbbe2b7e21af630687d02d38781e73-11_29_48.jpg",
        null,
        "Screenshot of configuring Surveys node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of configuring Surveys node."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "h-3": "Versions",
    "0-0": "Name: Enter a valid name for the survey to be used.  \n  \nValid After: Enter the Date and Time in UTC format after which the SurveyToken will be active. Eg: MM-DD-YYYY HH:MM:SS  \n  \nFor Eg: If you enter a date as 27th July and the URL is sent to the customer on 26th July, the URL will not be available and is shown as “Invalid URL”.  \n  \nValid Till - Enter the date and time Enter the date in ISO format. Eg: yyyy-MM-ddTHH:mm:ssZ  \n  \nValid For: Enter an Integer value for the date.  \n  \nFor Eg: If you pass 5 in the Valid For column, the system automatically captures current date (UTC format) and will add 5 more days to the current date.  \n  \nNote: You can either use Valid Till or Valid For to enter the date and time.  \n  \nPreferred Language: Select the required language. This can be configured from the Surveys platform.",
    "0-1": "id - contains the questionnaire token  \n  \norgId - contains the org id of the Surveys platform  \n  \nname - contains the tenant name  \n  \nvalidAfter - contains the range from when the url is valid  \n  \nvalidTill - contains the range until when the url is valid  \n  \nquestionnaireId - contains the questionnaire id which is selected  \n  \npreFill - contains the prefill values if provided  \n  \nonlyForPreviewSurvey - Survey preview mode. The default is false.  \n  \npreferredLanguage - contains the set of languages for the survey  \n  \nskipWelcome - Whether to showcase welcome page before stating of survey. This is default to false always.  \n  \nrestrictOnWebDomain - contains the list of web domains on which  the url is restricted  \n  \nrestrictFromIPSpace - contains the list of ip addresses on which the url is restricted  \n  \nvalidUses - No of times survey URL can be used. The default value is 1.  \n  \nsurveyURL - contains the survey url  \n  \nresponsePayload - contains the entire response payload",
    "0-2": "onInvalidData  \n  \nonError  \n  \nonInvalidChoice  \n  \nonTimeout  \n  \nonauthorizationfail  \n  \ncreateTokenForTheQuestionnaireOnSuccess  \n  \nfailedToAddSurveyToken  \n  \nUserRoleNotAllowedAccessThisResource  \n  \nAPIRequestLimitExceeded",
    "0-3": "v1.0,v1.1,v1.2,v1.3, v1.4 and v1.5  \n  \nName, Valid After, Valid For, and Preferred Language are in available in v1.1,v1.2, v1.3, v1.4, and v1.5  \n  \nNote: v1.0 uses .NET API endpoint.  \nv1.1,v1.2,v1.3,v1.4, and v1.5 uses Java based API endpoints."
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


## FAQ's

### Where can I call the survey node in the Webex Connect flow?

The survey node should be configured in the WxCC Task Close event flow to send the survey URL to the end user for feedback.

### How can I access authentication for the Survey Node configuration?

You can use the admin account credentials you use to log in to the Contact Center and Control Hub.