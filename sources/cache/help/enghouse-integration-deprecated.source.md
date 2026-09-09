> 📘 Deprecation Alert
> 
> Please note that this integration has been deprecated and is no longer available. This doesn't impact any of your existing live services however the integration won't be available for newer <<prodname>> tenants.

The integration enables Enghouse to support chat with their end customers on multiple channels (Example: Facebook Messenger, Real-Time Messaging) along with their own primary channel like web chat.

With Enghouse integration with <<prodname>>, Enghouse chat agents will be able to receive messages from multiple channels using the same interface. 

**Note: You have to source Enghouse connection parameters to configure in <<prodname>>, which are specific to a customer.**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2c0f40d-Enghouse.png",
        "Enghouse.png",
        "Screenshot of Enghouse Integration"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Enghouse Integration"
    }
  ]
}
[/block]


## Configure Enghouse

1. Log on to <<prodname>> with your credentials.
2. On the left navigation bar, click ASSETS > **INTEGRATIONS**. 
3. Click **ADD INTEGRATION** > **Enghouse** to add new integration. 
4. Enter the connection parameters and save the details.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "NAME",
    "0-1": "Name of the Enghouse integration on <<prodname>>.",
    "1-0": "**Configuration**",
    "1-1": "Parameters required to configure  Enghouse on <<prodname>>",
    "2-0": "CALL CENTER ADDRESS",
    "2-1": "Call center address to route the incoming messages.  \nE.g: webchat.ngcc.bt.com",
    "3-0": "CALL CENTER PORT",
    "3-1": "Port address of the call center.",
    "4-0": "TENANT ID",
    "4-1": "Unique Tenant ID provided by Enghouse.",
    "5-0": "APPLICATION ID",
    "5-1": "",
    "6-0": "SERVER URL",
    "6-1": "Server URL of the hosted tenant.  \nE.g: demotrial3",
    "7-0": "API VERSION",
    "7-1": "API version in use to access Enghouse.",
    "8-0": "ACCOUNT ID",
    "8-1": "Account ID provided by Enghouse.",
    "9-0": "**Saved replies**",
    "9-1": "Message configured for automated replies.",
    "10-0": "WELCOME MESSAGE",
    "10-1": "The welcome message for first time user.",
    "11-0": "GOODBYE MESSAGE",
    "11-1": "Message displayed when a user end the chat conversation.",
    "12-0": "**System replies**",
    "12-1": "Codes send to users when error occurs while replying to message.",
    "13-0": "STATUS CODE",
    "13-1": "",
    "14-0": "ERROR CODE",
    "14-1": "",
    "15-0": "REPLY MESSAGE",
    "15-1": "",
    "16-0": "**+ ADD MORE**",
    "16-1": ""
  },
  "cols": 2,
  "rows": 17,
  "align": [
    "left",
    "left"
  ]
}
[/block]


_Note: This integration is available only in the cloud version of <<prodname>>._