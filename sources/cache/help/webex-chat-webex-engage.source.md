> 📘 Deprecation Alert
> 
> Please note that this integration has been deprecated and is no longer supported. This decision does not impact the existing tenants that have access to and are using this node.

This integration allows any client to use IMIchat endpoint User Interface with channel capabilities provided by <<prodname>>.

The integration enables IMIchat vendors to support chat with their end customers on multiple channels (Example: Facebook Messenger, Real-Time Messaging) along with their own primary channel like web chat.

## Configure IMIchat Details

A client interested in using the capabilities of  IMIchat and <<prodname>> to facilitate customer contact through IMIchat is required to first set up the IMIchat integration on <<prodname>>. 

The connection parameters are to be configured to integrate IMIchat on <<prodname>> specific to a customer.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9fbee8d-imichat.jpg",
        "imichat.jpg",
        "Screenshot of Configuring New IMIchat Integratio"
      ],
      "align": "center",
      "border": true,
      "caption": "Configuring New IMIchat Integration."
    }
  ]
}
[/block]


| Parameter                 | Description                                                                                                                                   |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME                      | Name of  IMIchat Integration                                                                                                                  |
| **Chat Endpoint Details** | These details are required to connect IMIchat with IMIconncet. Get in touch with the support team to receive client-specific endpoint details |
| IMICHAT INSTANCE          | IMIchat URL to integrate with <<prodname>>.                                                                                                   |
| API KEY                   | The  key used to Identitfie teams on IMIchat                                                                                                  |

## CONFIGURE RULES BASED ON IMIchat EVENTS

Set up a rule to start a chat session, when events on any of channels meet the condition defined within the rule. 

1. Select a trigger channel, from the available list and configure the trigger event ( incoming message)
2. Set the action to **Forward to CCSP,** and choose an IMIchat integration.
3. Confirm the details of the rules.  
   a. Enter the Name of the rule.  
   b. Set the status of the rule.  
   c. Set notification URL to notify the execution of the rule each time.
4. Save the rule.

[block:parameters]
{
  "data": {
    "h-0": "Trigger",
    "h-1": "Action",
    "0-0": "Incoming message from any of the channels selcted",
    "0-1": "Invoke a flow  \nFoward to CCSP (  Choose IMIchat integration)  \nForward to BOT and CCSP."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]