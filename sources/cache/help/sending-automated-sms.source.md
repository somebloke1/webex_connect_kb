> 📘 Prerequisites
> 
> - Access to <<prodname>> platform (request your [trial access](https://imimobile.com/contact))
> - Postman app (or an alternative tool) to invoke APIs (Download [Postman](https://www.getpostman.com/apps))

## Step 1: Create a Service

Create new service from the Services Dashboard. If this is the first time you are creating a service in <<prodname>>, refer to the [tutorial](https://help.webexconnect.io/docs/create-a-service-on-imiconnect).

## Step 2: Get a phone number

A phone number is needed for sending and/or receiving messages from your customers using <<prodname>>. You can skip this step if you already have a number.

Here's a quick tutorial on [Buy a Phone Number using <<prodname>>](https://help.webexconnect.io/docs/buy-a-phone-number)

## Step 3: Create a Flow to Send SMS

### 1. Create a New Flow

For detailed steps, refer to [creating a new flow](https://help.webexconnect.io/docs/create-a-new-flow).

### 2. Select the custom event as the event trigger on the trigger category selection page

- On the next window, configure your custom event. Select radio button "**Create New Event**"
- Name the custom event. Next, define the parameters to be used in this event. 
- Under the **PARAMETERS (OPTIONAL) **section, choose the **TYPE **as String from the drop-down. 
- Enter **msisdn **as the variable. 
- Check the Mandatory box. 
- Click on **+ADD NEW** to define another parameter & define all the parameters as follows 

| TYPE   | VARIABLE         | MANDATORY |
| :----- | :--------------- | :-------- |
| String | msisdn           | Yes       |
| String | cust_name        | No        |
| String | appointment_time | Yes       |

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/deae17f-Sending_Automated_.jpg",
        "SMS Appointment Reminder.PNG",
        "Screenshot of Configuring Custom Event Page."
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Screenshot of Configuring Custom Event Page."
    }
  ]
}
[/block]


### 3. Build the Flow

- You will arrive at the **Visual Flow Builder** screen with the custom event node already present in the flow builder.
- Drag and drop a **Send node** from the node palette to the left of the screen, under the **Channels **tab. 
- Connect the custom event node with the Send node by dragging the green dot towards the Send node.
- Double-click on the Send node to configure its parameters. You will arrive at the configuration window.
- Here, enter** $(msisdn)** in the **DESTINATION **field. 
- **Note**: **MSISDN **stands for Mobile Station ISDN number, which refers to the mapping of the telephone number to SIM card.
- Select the sender id from the drop-down under **FROM NUMBER**
- Type the message that you wish to send to your customers in the **MESSAGE **section and click on **SAVE **to save these settings.

## Step 4 : Configure the 'onsuccess' event

[block:html]
{
  "html": "<a href=\"http://help.imiconnect.io/docs/configure-the-onsuccess-event\" target=\"_blank\"><b>Click here</b></a> for detailed steps on configuring <b>onsuccess</b> event for SMS node.\n\n"
}
[/block]


## Step 5 : Configure the 'onerror' event

[block:html]
{
  "html": "<a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>Click here</b></a> for detailed steps on configuring <b>onerror</b> event for SMS node."
}
[/block]


## Publish the Flow

[block:html]
{
  "html": "<a href=\"https://help.imiconnect.io/docs/flows#configuring-and-publishing-a-flow\" target=\"_blank\"><b>Click here</b></a> to know more about publishing a flow."
}
[/block]


## Step 7: Invoke the flow using Postman

[block:html]
{
  "html": "<a href=\"http://help.imiconnect.io/docs/invoke-the-flow-using-postman-or-any-alternative-tools\" target=\"_blank\"><b>Click here</b></a> for steps on testing using postman"
}
[/block]


Here's how the complete flow will look:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a1a1d11-Appointment_Reminder_Flow_1.png",
        "Appointment Reminder Flow 1.png",
        "Screenshot of Sample Flow."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Sample Flow."
    }
  ]
}
[/block]