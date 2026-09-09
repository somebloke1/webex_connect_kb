This document covers how you can branch your flow to automate handling of various customer requests/intents when using <<prodname>> Bot Builder and bot nodes within flows.

## Branching flows based on bot variables and fulfilling customer requests

**Use-case**

Using bot nodes, <<prodname>> can detect different user intents in natural language. Based on these intents, different logic can be executed in the flow to provide appropriate fulfillment. In this example, the bot allows customers to:

- Book an appointment: once the required information is collected, the appointment is booked and logged to a database, and a message is sent to the customer with the booking details. 
- Update an existing appointment: users can choose to update their existing appointments using this intent. Once all the information is gathered, the appointment is updated in the database.
- View booked appointments: after gathering the required information, a data dip is performed to fetch relevant appointment details. 

**End-to-End flow** 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8ba7add-Picture12.png",
        "Picture12.png",
        "Visual representation of the complete flow for booking an appointment."
      ],
      "align": "center",
      "border": true,
      "caption": "Visual representation of the complete flow for booking an appointment,"
    }
  ]
}
[/block]


- The flow starts with an incoming message from the user to the Messenger start node. In the transition actions for this node, we create a new variable ‘**messagetext**’ using the user’s message. This message is then forwarded to  the task bot node for intent detection. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7f4fe8d-Picture11.png",
        "Picture11.png",
        "Screenshot showing the Messenger start node configuration with variable initialization."
      ],
      "align": "center",
      "caption": "Initialising a variable in Messenger start node that can be used for incoming messages throughout the conversation"
    }
  ]
}
[/block]


- The Task bot node is configured by selecting the appropriate bot from the dropdown, and using the ‘messagetext’ variable as the Message. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/968a5c8-Picture13.png",
        "Picture13.png",
        "Screenshot of the Task bot node setup, showing the selection of the appropriate bot from the dropdown and the use of the 'messagetext' variable as the message content."
      ],
      "align": "center",
      "caption": "Configuring Task Bot Node with Message Variable."
    }
  ]
}
[/block]


- The Branch node that follows decides how the conversation will proceed based on the intent detected by the task bot. Here, we use ‘taskbot.intent’ output variable of the task bot node as the input to create various branches. The values used in the different branches in this scenario are the intent names configured in the bot builder.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cb9e434-CISCO_WEBEX_CONTACT_CENTER__IMICONNECT_INTEGRATION_Handling_various_customer_intents_using_flows_and_Bot_Builder_Branch_Node.png",
        "CISCO WEBEX CONTACT CENTER & IMICONNECT INTEGRATION Handling various customer intents using flows and Bot Builder  Branch Node.png",
        "Screenshot of showing the use of the 'taskbot.intent' output variable from the task bot node to create various branches."
      ],
      "align": "center",
      "caption": "Branching Using Task Bot Intent Output."
    }
  ]
}
[/block]


There are four branches created, one for each of the three in-scope intents and one for cases where user intent is none of these three intents.

## Booking an appointment

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4724a6c-Picture15.png",
        "Picture15.png",
        "Screenshot of booking an appointment flow."
      ],
      "align": "center",
      "caption": " Appointment Booking Flow"
    }
  ]
}
[/block]


- In the book an appointment branch, we use another branch node to check the state of the intent – whether all the required slots (date, time, and mode of appointment) are available or not. Here ‘taskbot.template_key’ output variable is used to create a branch for cases where the intent is complete. The ‘final template key’ configured for ‘book an appointment’ intent in the bot builder is used to create this branch.
- If the intent is not complete, ‘none of the above’ branch is traversed and bot response is sent to the user (using the messenger node in red) to fill the slots and continue the conversation.
- In cases where the intent is complete, the Data parser node parses the booking details (date of appointment, time of appointment, and mode of appointment) from ‘taskbot.entities’. A sample JSON body for entities can be downloaded from Sessions in the bot builder by opening a session, selecting a transaction where all the entities are available and downloading the transaction info from the right.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bbff0e7-Picture16.png",
        "Picture16.png",
        "Screenshot of extracting entity values using data parser node."
      ],
      "align": "center",
      "caption": "Extracting entity values using data parser node"
    }
  ]
}
[/block]


- These entity values and other user details are used in the HTTP node, which makes a POST request to the database to post the booking details. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/22e4cac-Picture17.png",
        "Picture17.png",
        "Screenshot displaying the configuration of an HTTP node set to make a POST request to a database, aimed at submitting booking details."
      ],
      "align": "center",
      "caption": "Posting Booking Details with HTTP Node"
    }
  ]
}
[/block]


- The messenger node gives the response to the customer about the booking details. Here users can use the response from Task bot or construct their own response using the variables available.
- Once the message is delivered to the user, irrespective of whether it’s through ‘None of the above’ or ‘Flow completed’ branch, a Receive node is used wait for the user’s response. In transition actions of the receive node, we use the newly received message to update the ‘messagetext’ variable. The receive node is connected back to the Task bot node to keep the conversation going until it times out.

## Update an appointment

The flow of conversation and the logic in this branch is the same as Book an appointment branch. The only difference is in the HTTP node where a PATCH request is made to update an existing appointment instead of POST.

## Check an appointment

- The HTTP node makes a GET request to the database to fetch the booking details based on the user details.
- The Data parser parses the information such as mode, time, and date of appointment from the response received from the HTTP node.
- The messenger node displays the booking details to the customer. In this branch, the response must be constructed in the messenger node. The bot response can’t be used here as the appointment details are fetched in the connect flow and those details are not sent back to the bot.

The fourth branch is none of the above, which works for all the other intents except these three. In this branch the bot’s response is sent to the user through a messenger node and we wait for the user’s response by using a receive node.

## Processing bot response

Bot nodes’ output variables contain two different variables for bot responses – ‘bot.text_response’ and ‘bot.full_response’. In cases where the bot’s response is text only, ‘bot.text_response’ can be used directly in the ‘Message’ field of Messenger node. For cases where a rich response containing templates other than text is configured for the bot, a Data Parser node has to be used to parse ‘bot.full_response’ before using the Messenger channel node. For example, if the bot response contains quick replies, ‘bot.full_response’ has to be provided as input to the Data Parser node to extract button titles and payloads.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cce4910-Picture18.png",
        "Picture18.png",
        "Screenshot showing the extraction process for quick reply button titles, payloads, and associated text response."
      ],
      "align": "center",
      "caption": "Extracting quick reply button titles and payloads along with text response"
    }
  ]
}
[/block]


A sample JSON body for rich responses can be downloaded from Sessions in the bot builder by opening a session, selecting a transaction where a rich response is sent out, and downloading the transaction info from the right. The extracted values for text, button titles and payloads is used in the Messenger node to deliver the response to users.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/69ca73e-Picture19.png",
        "Picture19.png",
        "Interface showing the Messenger node configuration, where values extracted from the Data Parser are being utilized. "
      ],
      "align": "center",
      "caption": "Using the values extracted from Data Parser in Messenger node"
    }
  ]
}
[/block]


The method for delivering other rich messages remains the same, where relevant values are extracted from the data parser node and delivered using Messenger channel node by selecting the appropriate Message Type.