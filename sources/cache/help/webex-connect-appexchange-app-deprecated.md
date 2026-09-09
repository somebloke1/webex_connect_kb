# Webex Connect AppExchange App - Deprecated

Source: https://help.webexconnect.io/docs/webex-connect-appexchange-app-deprecated
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:11+00:00

> 📘 Deprecation Alert
> 
> Please note that this integration has been deprecated and is no longer available. Refer [Salesforce Node](https://help.imiconnect.io/docs/salesforce-node) page to know how you can fetch/update info in Salesforce as part of flow executions.

Webex Connect for Salesforce is an AppExchange app that enables you to improve customer experience by engaging your Salesforce customers across 10+ communication channels including Apple Messages for Business, WhatsApp, and RCS Business Messaging. 

With Webex Connect for Salesforce app you can:

- Consume real-time event triggers from 400+ Salesforce objects, and send contextual alerts and notifications over customers' preferred channels.
- Configure time-based triggers to send interactive notifications for upcoming appointments or renewals, overdue payments, abandoned carts & more.
- Easily invoke Webex Connect multichannel communication flows from Salesforce Process Builder without any coding using our pre-built APEX classes.
- Enable conversational customer engagement across channels using Webex Connect's integrated NLP and AI capabilities.

## Installing Webex Connect for Salesforce app

Webex Connect for Salesforce app can be installed from [AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FYEGIUA5) .

## Trigger Webex Connect flows from Salesforce

Webex Connect for Salesforce is an automation champ and comes with easy webhook creation configurations.

There are three different ways to configure two different types of triggers:

- Process Builder
- Event Trigger
- Schedule Trigger.

## Process Builder

The trigger can be created on all process builder supported sObjects. Webex Connect for Salesforce adds features to Saleforce’s process builder to make callouts.

The following can be achieved by:

1. Choose +Add Action under IMMEDIATE ACTION or SCHEDULED ACTION in the process builder.



![Choose +Add Action](https://files.readme.io/160a48d-img7.png)




2. Choose the following configurations:  
    i.  Action type – Apex  
    ii. Action Name – Enter a friendly name  
   iii. Apex Class – Choose ‘Webex Connect’ from the list. 

### Set Apex Variables



| Apex Variables | Type | Value |
| --- | --- | --- |
| Webex Connect\_Webhook_URL | String | Enter Webex Connectcustom event URl |
| sObject_ID | Field Reference | Choose ID formula field  <br>  <br>Eg: For Account ID – : "Apex V.Id |
| sObject_Name | String | Enter sObject Name  <br>  <br>Eg: Account |
| Variable_1_optional | Any type | Optional (Use if you desire a specific field data) |




> 📘 
> 
> Only three optional variables are provided. However, on requirement, the number of variables can be increased. Obtain more details on the configured sObject using custom node and sObject_ID variable.

## Event Trigger

Any platform/database event Before/After (Insert/Update/Delete) can be configured as event trigger. Standard and custom sObjects are supported and can be configured as triggers. System sObjetcs cannot be used as they are marked as non-triggerable objects by Salesforce.  



![Event Trigger](https://files.readme.io/b0cb567-img8.png)




- Trigger Name - a user-friendly name for the trigger. Trigger name can only contain alphabets and digits.
- sObject Name - Select the sObject on which the trigger is to be configured. Webex Connect for Salesforce app supports all standard and custom sObject available in the organization.
- Events – Select events in any combination. At least one event is required for the trigger to be successfully configured.
- BEFORE trigger - BEFORE triggers are usually used when validation needs to take place before accepting the change. They run before any change is made to the Salesforce platform.
- AFTER trigger - AFTER triggers are usually used when information needs to be updated in a separate table due to a change. They run after changes have been made to the platform (not necessarily committed).
- Filter – Filter out the record to be processed by trigger using filters. Webex Connect for Salesforce supports single/multiple filters.
- Webex Connect Webhook URL – Enter Webex Connect Webhook URl. You can obtain the URl from the Start node.



![Screenshot of Webhook URL Configuration Page.](https://files.readme.io/21d4541-img9.png)




- Webex Connect Service Key (Optional) – Service key is an extra security key for securing webhook requests. It is used to identify the incoming event API. If ‘Required Authentication’ is switched ‘ON’ while configuring webhook on the Webex Connect platform, only a request with a matching service key from the Salesforce trigger will be processed by Webex Connect.

## Schedule Trigger

Webex Connect for Salesforce app can be used to schedule a time-based trigger. Schedule trigger uses schedule jobs to poll user saved trigger configurations every hour and make callouts for configuration matching records. Triggers can be configured for:

- Number of + hours or days + before or after + All DateTime or Date fields in selected sObject

For example, 2 + days + before + ‘Order sObject enddate field’.



![Screenshot of Configure Schedule Trigger Page.](https://files.readme.io/52067ec-image1.png)




> 📘 
> 
> However, if the configured field has data type only ‘Date’ then callouts for successful configuration matching records are done at 9:00 AM (for all time zones).

## Dashboard within Webex Connect for Salesforce App

This is a comprehensive page for all trigger related activities on Salesforce organization.

## Reports

Webex Connect Home features three standard Salesforce reports:

- Total Calls to Webex Connect– shows a graph of the total number vs successful callouts made to Webex Connect.
- Event trigger calls to Webex Connect – depicts the total number of successful callouts made by the triggers configured using ‘Event trigger’ tab of Webex Connect for Salesforce app.
- Schedule trigger calls to Webex Connect – shows the total number of successful callouts made by triggers configured using ‘Schedule trigger’ tab of imionnect for Salesforce app.