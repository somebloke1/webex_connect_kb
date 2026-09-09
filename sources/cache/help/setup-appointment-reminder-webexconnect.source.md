## Step 1: Create a Service

Create a new service to manage this use case.

[block:html]
{
  "html": "<a href=\"http://help.imiconnect.io/docs/create-a-service-on-imiconnect\" target=\"_blank\"><b>Click here</b></a> for detailed steps on service creation"
}
[/block]


## Step 2: Get a Phone Number & assign it to the service

[block:html]
{
  "html": "For detailed steps on buying and assigning a number <a href=\"http://help.imiconnect.io/docs/buy-a-phone-number\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


## Step 3: Create a Flow to Send Appointment Reminder

### 1. Create a New Flow

[block:html]
{
  "html": "For detailed steps on creating a new flow <a href=\"http://help.imiconnect.io/docs/create-a-new-flow\" target=\"_blank\"><b>click here</b></a>"
}
[/block]


### 2. Configure a Custom Event

- Select 'Custom Event' on the Select Trigger Category screen that's shown while creating a new flow
- On the next window, configure your custom event. Select the "**Create New Event**" option
- Name the custom event. Then, define the parameters that will be used in the flow. 
- Under the **PARAMETERS (OPTIONAL) **section, choose the **TYPE **as String from the drop-down. 
- Enter **msisdn **as the variable. 
- Check the Mandatory box. 
- Click on **+ADD NEW** to define another parameter & define all the parameters as follows 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a9053d8-2.jpg",
        "add_new_param_custom_event.png",
        "Screenshot of the configuration screen for setting up a custom event."
      ],
      "align": "center",
      "caption": "Configuration screen for creating and setting up a custom event."
    }
  ]
}
[/block]


### 3. Configure Send Node

1. You will then see the **Visual Flow Builder** screen with the custom event node already present on the flow canvas.
2. Drag and drop a **Send SMS node** from the node palette to the left of the screen, under the **UTILITIES**tab. 
3. Connect the custom event node with the Send SMS node by dragging the green dot towards the Send node.
4. Double-click on the Send node to configure its parameters. You will arrive at the configuration window.
5. Here, enter** $(msisdn)** in the **DESTINATION **field. 

> 📘 Note
> 
> **MSISDN **stands for Mobile Station ISDN number, which refers to the mapping of the telephone number to the SIM card. In simple words, it's the mobile number

6. Select the sender id from the drop-down under **FROM NUMBER**
7. Type the message that you wish to send to your customers in the **MESSAGE **section and click on **SAVE** to save these settings.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/49c040d-Setting_Up_an_Appointment.jpg",
        "message_sms_node.png",
        "Screenshot of configuring the SMS Send Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Configuration screen for setting up a SMS Send Node."
    }
  ]
}
[/block]


### 4.Configure Exception handling details for the node

1. Set up 'onPolicyFail' exception.
2. Set up 'onError' exception.

[block:html]
{
  "html": "For detailed steps on configuring exception handling <a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


## Step 4 : Configure Receive Node

### 1. Add the Receive Node

Drag and drop the Receive node onto the flow canvas from the left node palette under **UTILITIES**.

### 2. Configure the Receive Node Parameters.

1. Double-click on the Receive node to open its configuration settings.
2. Enter the phone number along with the country code for the service in the Number field.
3. Enter \* in the keyword field.
4. Enter $(msisdn) in the From number field.
5. Configure the timeout duration i.e. the time the flow should be in wait-for mode for receiving the message
6. Enter a name for the node in the Name field.
7. Click on SAVE at the bottom.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4e6bfa8-Setting_Up_an_Appointment1.jpg",
        "receive_node_custom_event.png",
        "Screenshot of configuring parameters for the SMS Receive Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Configuration screen for setting SMS Receive Node parameters."
    }
  ]
}
[/block]


### 3. Configure Exception handling for the node

1. Set up 'ontimeout' exception.
2. Set up 'onError' exception. 

[block:html]
{
  "html": "For detailed steps on configuring exception handling <a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


## Step 5: Evaluate Customer Response

The Branch node is used to perform conditional actions based on the customer response. It evaluates the customer’s response and directs the flow to proceed further accordingly.

### 1. Add the Branch Node

Drag and drop the Branch node onto the flow canvas node palette to the left under **UTILITIES**.

### 2. Configure the Branch Node

Double-click on the Branch node to configure its settings.

Configure Confirmation Conditions:

1. Name the branch condition appropriately. For instance, _Confirm_
2. Enter the system generated variable [e.g. $(n25.receive.message) in this case] in the **VARIABLE** field.
3. Select the **CONDITION** as Equals from the drop-down.
4. Enter the relevant value in the **Value** field. For example, in this case, it should be 1 as mentioned in the SMS message.
5. Click on ADD BRANCH to add a new branch.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c426e77-Setting_Up_an_Appointment2.jpg",
        "confirm_branch.png",
        "Screenshot of configuring the Branch Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Configuration screen for setting up a Branch Node."
    }
  ]
}
[/block]


Configure Cancellation Conditions:

1. Name the branch condition appropriately. For instance, _Cancel_
2. Enter the system generated variable (i.e. $(n25.receive.message) in this case) in the **VARIABLE** field.
3. Select the **CONDITION** as Equals from the drop-down.
4. Enter the relevant value in the **Value** field. For example, 2.
5. Click on ADD BRANCH to add a new branch.

Configure Other/Default Response:

1. Enter a default message in the message box provided below +ADD BRANCH. In this case, _Invalid Response_.

### 3. Configure Exception handling for the node

1. Set up 'onError' exception 

[block:html]
{
  "html": "For detailed steps on configuring exception handling <a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


## Step 5: Send Appointment Confirmation Message

### 1. Add the Send Node

Drag and drop the Send SMS node onto the flow canvas node palette to the left under **UTILITIES**.

### 2. Configure the Send Node

Double-click on the Send node to configure its parameters. You will arrive at the configuration window.

1. Click on SMS on the Settings window. 
2. Enter $(msisdn) in the Destination field. msisdn stands for Mobile Station ISDN number. It's an alternative name for the mobile number. 
3. Choose msisdn from the Destination Type drop-down.
4. Choose Text from the Message Type drop-down.
5. Choose the assigned phone number for the service from the sender id drop-down. 
6. Enter the message to be sent to the customer in the Message box.
7. Enter a name for the node in the Name field.
8. Click on SAVE. 

### 3. Configure Exception handling for the node

1. Set up 'onError' exception 

[block:html]
{
  "html": "For detailed steps on configuring exception handling <a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


## Step 6: Cancelling the Appointment

### 1. Add the Send Node

1. Drag and drop the Send SMS node onto the flow canvas node palette.

### 2. Configure the Send Node

1. Follow the process mentioned in Step 2 of Confirming the Appointment.  
   **Note**: The messaging in the Message box for canceling the appointment will differ from what is written in Step 2 of Confirming the Appointment. Refer to the image below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/824f36e-Setting_Up_an_Appointment3.jpg",
        "appointment_cancellation.png",
        "Screenshot of Configuring the Send Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Send Node."
    }
  ]
}
[/block]


### 3. Configure Exception handling for the node

1. Set up 'onError' exception 

[block:html]
{
  "html": "For detailed steps on configuring exception handling <a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


## Step 7: Handling Invalid Customer Responses

### 1. Add the Send Node for Invalid Response

Drag and drop the Send node onto the flow canvas.

### 2. Configure the Node

Follow the process mentioned in Step 2 of Confirming the Appointment.

### 3. Configure Exception handling for the node

1. Set up 'onError' exception 

[block:html]
{
  "html": "For detailed steps on configuring exception handling <a href=\"https://help.imiconnect.io/docs/configuring-error-events-for-a-node\" target=\"_blank\"><b>click here.</b></a>"
}
[/block]


 The overall flow appears as shown below:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ff67f80-appointment_reminder_flow.png",
        "appointment_reminder_flow.png",
        "Screenshot of Sample Flow."
      ],
      "align": "center",
      "caption": "Screenshot of Sample Flow."
    }
  ]
}
[/block]


## Step 8: Publish the Flow

[block:html]
{
  "html": "<a href=\"http://help.imiconnect.io/v5.4/docs/publishing-the-flow\" target=\"_blank\"><b>Click here</b></a> to know more about publishing a flow."
}
[/block]


## Step 9:  Configure the Event Scheduler

Event Scheduler is used to trigger the custom event at specific time intervals that can be set as per customer preferences. It also allows large entries of data to be fed through .csv files that have variables the same as the ones defined in the custom event. All the values for each of the values can be fed through these files using the event scheduler. Follow the below procedure to create an event in the Event Scheduler for triggering the appointment reminder service:

### 1. Create an Event in the Event Scheduler

1. After logging in to <<prodname>>, click APP TRAY icon from the left Menu bar.
2. Click the Event Scheduler option from the menu which will lead you to the Event Scheduler configuration window. 

### 2. Configure Event Scheduler

1. Choose a name for the event on the Create new trigger screen.
2. Select the service from the Select Service drop-down.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e59c72d-create_schedule_appointment_reminder.png",
        "create_schedule_appointment_reminder.png",
        "Screenshot of Creating a Schedule."
      ],
      "align": "center",
      "caption": "Screenshot of Creating a Schedule."
    }
  ]
}
[/block]


3. Select the Send Trigger notification to the Email ID checkbox.
4. Enter the Email ID to which the notifications have to be delivered. However, this is optional.
5. Click **Next**.

### 3. Configure Action

1. Select CUSTOM EVENT under Type of Action.
2. Select the custom event from the Select Event drop-down.
3. Click **Next**.

### 4. Configure Target Data

1. Select the Upload file option.
2. Upload the .csv file.
3. Click **Next**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/94e7405-Setting_Up_an_Appointment4.jpg",
        "upload_csv_file_appointment_reminder.png",
        "Screenshot of Creating a Schedule."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Creating a Schedule."
    }
  ]
}
[/block]


### 5. Configure Schedule

1. Select the Frequency under How Often.
2. Choose the Date and Time from when the event has to be active by clicking on the popup calendar. 
3. Click **Next**.  
   The appointment reminder setup is now good to go!