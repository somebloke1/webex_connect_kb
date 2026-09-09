> 📘 Deprecation Alert
> 
> Please note that this integration has been deprecated and is no longer available. Refer [Salesforce Node](https://help.imiconnect.io/docs/salesforce-node) page to know how you can fetch/update info in Salesforce as part of flow executions.

<<prodname>> for Salesforce is an AppExchange app that enables you to improve customer experience by engaging your Salesforce customers across 10+ communication channels including <<AMB>>, WhatsApp, and RCS Business Messaging. 

With <<prodname>> for Salesforce app you can:

- Consume real-time event triggers from 400+ Salesforce objects, and send contextual alerts and notifications over customers' preferred channels.
- Configure time-based triggers to send interactive notifications for upcoming appointments or renewals, overdue payments, abandoned carts & more.
- Easily invoke <<prodname>> multichannel communication flows from Salesforce Process Builder without any coding using our pre-built APEX classes.
- Enable conversational customer engagement across channels using <<prodname>>'s integrated NLP and AI capabilities.

## Installing <<prodname>> for Salesforce app

<<prodname>> for Salesforce app can be installed from [AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FYEGIUA5) .

## Trigger <<prodname>> flows from Salesforce

<<prodname>> for Salesforce is an automation champ and comes with easy webhook creation configurations.

There are three different ways to configure two different types of triggers:

- Process Builder
- Event Trigger
- Schedule Trigger.

## Process Builder

The trigger can be created on all process builder supported sObjects. <<prodname>> for Salesforce adds features to Saleforce’s process builder to make callouts.

The following can be achieved by:

1. Choose +Add Action under IMMEDIATE ACTION or SCHEDULED ACTION in the process builder.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/160a48d-img7.png",
        "img7.png",
        "Screenshot of Choose +Add Action under IMMEDIATE ACTION or SCHEDULED ACTION"
      ],
      "align": "center",
      "caption": "Choose +Add Action"
    }
  ]
}
[/block]


2. Choose the following configurations:  
    i.  Action type – Apex  
    ii. Action Name – Enter a friendly name  
   iii. Apex Class – Choose ‘<<prodname>>’ from the list. 

### Set Apex Variables

[block:parameters]
{
  "data": {
    "h-0": "Apex Variables",
    "h-1": "Type",
    "h-2": "Value",
    "0-0": "<<prodname>>\\_Webhook_URL",
    "0-1": "String",
    "0-2": "Enter <<prodname>>custom event URl",
    "1-0": "sObject_ID",
    "1-1": "Field Reference",
    "1-2": "Choose ID formula field  \n  \nEg: For Account ID – : \"Apex V.Id",
    "2-0": "sObject_Name",
    "2-1": "String",
    "2-2": "Enter sObject Name  \n  \nEg: Account",
    "3-0": "Variable_1_optional",
    "3-1": "Any type",
    "3-2": "Optional (Use if you desire a specific field data)"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 
> 
> Only three optional variables are provided. However, on requirement, the number of variables can be increased. Obtain more details on the configured sObject using custom node and sObject_ID variable.

## Event Trigger

Any platform/database event Before/After (Insert/Update/Delete) can be configured as event trigger. Standard and custom sObjects are supported and can be configured as triggers. System sObjetcs cannot be used as they are marked as non-triggerable objects by Salesforce.  

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b0cb567-img8.png",
        "img8.png",
        "Screenshot of Event Trigger Page"
      ],
      "align": "center",
      "caption": "Event Trigger"
    }
  ]
}
[/block]


- Trigger Name - a user-friendly name for the trigger. Trigger name can only contain alphabets and digits.
- sObject Name - Select the sObject on which the trigger is to be configured. <<prodname>> for Salesforce app supports all standard and custom sObject available in the organization.
- Events – Select events in any combination. At least one event is required for the trigger to be successfully configured.
- BEFORE trigger - BEFORE triggers are usually used when validation needs to take place before accepting the change. They run before any change is made to the Salesforce platform.
- AFTER trigger - AFTER triggers are usually used when information needs to be updated in a separate table due to a change. They run after changes have been made to the platform (not necessarily committed).
- Filter – Filter out the record to be processed by trigger using filters. <<prodname>> for Salesforce supports single/multiple filters.
- <<prodname>> Webhook URL – Enter <<prodname>> Webhook URl. You can obtain the URl from the Start node.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/21d4541-img9.png",
        "img9.png",
        "Screenshot of Webhook URL Configuration Page."
      ],
      "align": "center",
      "caption": "Screenshot of Webhook URL Configuration Page."
    }
  ]
}
[/block]


- <<prodname>> Service Key (Optional) – Service key is an extra security key for securing webhook requests. It is used to identify the incoming event API. If ‘Required Authentication’ is switched ‘ON’ while configuring webhook on the <<prodname>> platform, only a request with a matching service key from the Salesforce trigger will be processed by <<prodname>>.

## Schedule Trigger

<<prodname>> for Salesforce app can be used to schedule a time-based trigger. Schedule trigger uses schedule jobs to poll user saved trigger configurations every hour and make callouts for configuration matching records. Triggers can be configured for:

- Number of + hours or days + before or after + All DateTime or Date fields in selected sObject

For example, 2 + days + before + ‘Order sObject enddate field’.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/52067ec-image1.png",
        "image1.png",
        "Screenshot of Configure Schedule Trigger Page."
      ],
      "align": "center",
      "caption": "Screenshot of Configure Schedule Trigger Page."
    }
  ]
}
[/block]


> 📘 
> 
> However, if the configured field has data type only ‘Date’ then callouts for successful configuration matching records are done at 9:00 AM (for all time zones).

## Dashboard within <<prodname>> for Salesforce App

This is a comprehensive page for all trigger related activities on Salesforce organization.

## Reports

<<prodname>> Home features three standard Salesforce reports:

- Total Calls to <<prodname>>– shows a graph of the total number vs successful callouts made to <<prodname>>.
- Event trigger calls to <<prodname>> – depicts the total number of successful callouts made by the triggers configured using ‘Event trigger’ tab of <<prodname>> for Salesforce app.
- Schedule trigger calls to <<prodname>> – shows the total number of successful callouts made by triggers configured using ‘Schedule trigger’ tab of imionnect for Salesforce app.