Understanding whether your customers are satisfied with your products and services is a key priority for every business. However, most feedback collection methods do not allow you to analyze the true sentiment and emotions of your customers. This tutorial provides a step-by-step walk-through of how you can integrate IBM Watson Tone Analyzer API with <<prodname>> to analyze the sentiment in the customer feedback captured via SMS.

> 📘 Usecase overview
> 
> •The user receives an SMS message requesting feedback about the services provided by the business  
> •The user replies to the message in natural language with his feedback  
> •The feedback/customer response is captured using <<prodname>> and is then analyzed by the watson API to identify the tone of the message.  
> •The tone will be categorised as either of the following : anger, disgust, fear, joy, and sadness  
> •Based on the user tone, the business can initiate a post feedback journey

## Setup overview

The below section lists the steps involved in building the IBM Watson Sentiment Analyzer use case

> 🚧 Prerequisites
> 
> •Access to <<prodname>> platform  
> •Create an account on IBM Watson to get access to Tone Analyzer API

### Step 1: Create a Service

Create a new service for this use case. If this is the first time you're creating a service refer [this](doc:create-a-service-on-imiconnect) tutorial.

### Step 2: Buy a Phone Number

[Buy a phone number](https://help.imiconnect.io/docs/buy-a-phone-number) for sending and receiving messages from your customers, if you don't already have one provisioned for this purpose. 

### Step 3: Configure a reusable integration with Tone Analyzer API using Custom Node

Set-up a reusable integration with IBM Watson Tone Analyzer API using <<prodname>> custom node integration option. 

For configuring the integration, refer to the [Using Custom Node to configure your own integrations](https://help.imiconnect.io/docs/configure-custom-integration-node) section.

### Step 4: Create a Flow to Analyze Customer Sentiment

Here are the steps for configuring a flow to send a proactive message to request and collect customer feedback, and use IBM Watson Tone Analyzer API to assess customer sentiment based on the content in customer's response.

Let's start by creating a new flow with a **custom event trigger.** 

### Step 5.1: Configure the event trigger for the flow

Select the custom event as the event trigger on the trigger category selection page.

1. On the next window, configure your custom event. Select "**Create New Event**"
2. Name the custom event. Next, define the parameters to be used in this event. 
3. Under the **PARAMETERS (OPTIONAL) **section, choose the **TYPE **as String from the drop down. 
4. Enter **msisdn **as the variable. 
5. Check the Mandatory box. 
6. Click on **+ADD NEW** to define another parameter & define all the parameters as follows

| TYPE   | VARIABLE   | MANDATORY |
| :----- | :--------- | :-------- |
| String | msisdn     | Yes       |
| String | username   | Yes       |
| String | password   | Yes       |
| String | version    | Yes       |
| String | user_input |           |

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/90f0c23-4.jpg",
        "IMIconnect-create-custom-event-trigger-watson-1.png",
        "Screenshot of Optional Parameters."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Optional Parameters."
    }
  ]
}
[/block]


### Step 5.2: Add the Send SMS node

1. Drag and drop the **Send SMS** node on to the flow canvas by dragging from the **Channels **menu under **UTILITIES**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/685f625-Analyse_Customer.png",
        "IMIconnect-sendsms-node-1.png",
        "Screenshot of Adding SMS Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Adding SMS Node."
    }
  ]
}
[/block]


2. Configure the node parameter  
   Double-click on the **Send SMS** node to open the configuration menu. See the image below
3. Under the **Configuration **tab on the Settings window.
4. Choose **msisdn **from the **Destination Type** drop-down.
5. Enter **$(msisdn)** in the Destination field.  
   **Note**: msisdn stands for Mobile Station ISDN number. It refers to the mapping of telephone number to SIM card.
6. Choose **Text **from the **Message Type** drop-down.
7. Choose the **sender id** assigned for the service from the **From Number **drop-down. 
8. Enter the **Message **to be sent to the customer in the **Message text box**. 
9. Edit the **name **of the node by clicking the **pencil icon**   . 
10. Click **OK **at the bottom. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e95ea89-3.jpg",
        "IMIconnect-sendsms-node-configuration.png",
        "Screenshot of SMS Node Configuration Window."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of SMS Node Configuration Window."
    }
  ]
}
[/block]


Now configure the onError event for the node. Refer [this](https://help.imiconnect.io/docs/configuring-error-events-for-a-node) tutorial for more information.

### Step 5.3: Configure the Receive Response node

1. Drag and drop the **Receive node** on to the flow canvas by dragging from the **NODES ** palette under **UTILITIES**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2ecd8d0-IMIconnect-receive-node-configuration.png",
        "IMIconnect-receive-node-configuration.png",
        "Screenshot of Configuring the Receive Response Node"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Receive Response Node."
    }
  ]
}
[/block]


2. Connect the onsuccess node edge of SMS node with the Receive node  
   a. Drag the green dot on the SMS Node and release it on Receive node  
   b. This enables the flow to proceed from the Send node to the Receive node if the event is successful.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c568ae9-IMIconnect-receive-onsuccess-configuration.png",
        "IMIconnect-receive-onsuccess-configuration.png",
        "Screenshot of Connecting the SMS Node with the Receive Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Connecting the SMS Node with the Receive Node"
    }
  ]
}
[/block]


**Configure the Receive Node Parameters**

Double-click on the Receive node to configure its settings. See the image below and follow the steps listed

1. Select the **Receive SMS** event 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8832678-5.jpg",
        "IMIconnect-receive-node-configuration-1.png",
        "Screenshot of Selecting the SMS Receive Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Selecting the SMS Receive Node."
    }
  ]
}
[/block]


2. Select the phone number along with the country code for the service from the Number field  
   dropdown.
3. Select \* from the keyword field dropdown.
4. Enter **$(msisdn)** in the From number field.
5. Enter the maximum timeout in the 'Max timeout' field.
6. Click on **OK **at the bottom.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6dd382b-6.jpg",
        "IMIconnect-receive-node-configuration-2.png",
        "Screenshot of Configuring the Receive Node Parameters."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Receive Node Parameters."
    }
  ]
}
[/block]


Configure the '**ontimeout**' event

The '**ontimeout**' event occurs when the time (in seconds) mentioned in the Time Outfield has expired.  
To configure the **ontimeout **event response:

1. Drag and drop the orange dot on the Receive node .

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/df5bbf7-IMIconnect-receive-node-ontimeout-config.png",
        "IMIconnect-receive-node-ontimeout-config.png",
        "Screenshot of Selecting the Receive Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Selecting the Receive Node."
    }
  ]
}
[/block]


2. Choose **ontimeout **from the Node event drop-down on the **[END FLOW - SETTINGS]** tab. 
3. Choose **103 – Flow ended due to an interruption [Incomplete] **from the Custom flow result drop-down. 
4. Click **OK **at the bottom.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/12ac2e3-7.jpg",
        "IMIconnect-receive-node-ontimeout-config-1.png",
        "Screenshot of Selecting the onTimeout Node Event."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Selecting the onTimeout Node Event."
    }
  ]
}
[/block]


### Step 5.4: Add & Configure the IBM Watson Tone Analyzer node

Drag and drop the IBM Watson Tone Analyzer custom integration node to the Canvas and configure it as per below.

1. Double-click on the IBM Watson node to configure its settings. See the image below & fill in the fields accordingly.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/93488ee-imiconnect-node-IBM-Watson-Tone-Analyzer-config.png",
        "imiconnect-node-IBM-Watson-Tone-Analyzer-config.png",
        "Screenshot of Configuring the IBM Watson Tone Analyzer node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the IBM Watson Tone Analyzer node."
    }
  ]
}
[/block]


2. Configure the error handling edges.

a. Configure the the 'oninvaliddata' event edge. The '**onInvalidData**' event occurs when the response received contains no information. Drag and drop the red dot on the IBM Watson node to configure **onInvalidData **event.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e363743-imiconnect-onInvalidData-Edge-Config.jpg",
        "imiconnect-onInvalidData-Edge-Config.jpg",
        "Screenshot of Configuring the 'oninvaliddata' event edge."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the 'oninvaliddata' event edge."
    }
  ]
}
[/block]


b. Configure the 'onauthorizationfail' event edge. The ‘**onauthorizationfail**’ event occurs when the **username **or password is not valid. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/84cd4a8-imiconnect-onAuthorizationFailure-Edge-Config.png",
        "imiconnect-onAuthorizationFailure-Edge-Config.png",
        1109
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the 'onauthorizationfail' Node event."
    }
  ]
}
[/block]


### Step 5.5: Setup the branch node & conditional logic

Add a branch node and configure various branches based on the value of **$(toneIdentifier) ** variable.

1. Positive Flow
2. Negative Flow

Please refer to the below images for a detailed view.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7180a46-2.jpg",
        "IMIconnect-watson-branch-1.png",
        "Screenshot of Configuring the Positive Feedback"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Positive Feedback."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/56d98d4-3.jpg",
        "IMIconnect-watson-branch-2.png",
        "Screenshot of Configuring the Negative Feedback"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Negative Feedback"
    }
  ]
}
[/block]


If the user tone is identified as Joy, it will flow into the **positive feedback** flow. If the user tone is identified as other than Joy, it will flow into **negative feedback** flow. 

Let us now configure send SMS nodes to respond to the customer based on sentiment analysis.

### Step 5.6: Setup Send SMS nodes for each branch

1. Setup Send SMS node for positive flow. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a9e3d14-1.jpg",
        "IMIconnect-sendsms-node-positive-flow.png",
        "Screenshot of Setup Send SMS node for positive flow."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Setup Send SMS node for positive flow."
    }
  ]
}
[/block]


2. Setup **Send SMS** node for **negative flow**. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d61aabf-8.jpg",
        "IMIconnect-sendsms-node-negativefeedback.png",
        "Screenshot of Setup Send SMS node for Negative flow."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Setup Send SMS node for Negative flow."
    }
  ]
}
[/block]


### Step 6: Publish the flow

1. Click **MAKE LIVE** button at the top right corner of the screen. You will then see a **Confirm – Make Live** message box.
2. Click **OK** to publish the flow.

This finishes the flow set-up for this use case. Go ahead and invoke the flow by sending relevant variables as part of the event API call.