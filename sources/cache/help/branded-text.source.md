## What is Branded Text ?

Branded Text upgrades SMS to RCS (Rich Communication Services) and delivers enhanced messaging as a service, without requiring technical changes for your enterprise. Branded Text feature lets brands provide a richer, fully branded messaging experience to SMS subscribers. With Branded Text, messages are branded, verified, and secured, helping you build trust and stand out in message inboxes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b3547435c72a5fb26d86ea3a1ac39559add9d33a48f0b337051ff2481cf0b92c-73498bb5-481c-4be9-bcd3-751b28e7d59d.png",
        "",
        "Screenshot of an SMS received on your number."
      ],
      "align": "center",
      "sizing": "30% ",
      "caption": "SMS"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0d5f23cc49eb792d86336ef00c693b6daa48379ff1d9b4ee6ad03688ea1b48bf-bd8b75d8-3e0a-44c0-a3e0-1d04667e48e8.png",
        "",
        "Screenshot of the SMS upgraded to Rich Communication Services Branded Text. If your number is enabled for Branded Text."
      ],
      "align": "center",
      "sizing": "30% ",
      "caption": "Branded Text"
    }
  ]
}
[/block]


## Key Benefits

- Control your branding and appearance: Customize how your brand appears within the messaging experience.
- Strengthen consumer confidence: Messages display a verified checkmark, assuring customers that the messages come from your business.
- Increase engagement and response rates: Enhanced branding and trust drive higher interaction with your messages.

## Key Features of Branded Text

- **Branded and Verified Messaging: **Display your business name, logo, and contact details. Clearly mark messages as verified to strengthen brand trust and recognition.
- **Delivery and Read Receipts: **Track the status of every message with delivery and read receipts to ensure transparency and reliability.
- **Broad Coverage: **Reach both iOS and Android users, with coverage depending on RCS availability on their devices.
- **Fallback to SMS: **If RCS does not deliver a message, automatically fall back to SMS to ensure consistent delivery to all users.

## Simplified Enablement of Branded Text

You can enable Branded Text for a Number on the <<prodname>> platform. To enable this feature, you must enable Branded Text at the tenant-level. This feature is not available by default. Please contact your account manager if you wish to enable it for your account.

> 📘 Note:
> 
> Enabling Branded Text at the tenant-level modifies the payload structure for Outbound Webhooks, Delivery Receipts, Data Streams - SMS outbound request, and Incoming Messages. For detailed information, see the [Updates to Logs, Integrations, and Reports ](#updates-to-logs-and-reports) section.

After you enable Branded Text for your account, you can enable a Number, Sender ID, or Short Code for Branded Text through the Numbers section in the <<prodname>> platform. You require an approved RCS Asset before you can enable Branded Text for a Number. Also, you can map only one Number to one RCS Asset. Please follow the steps in the section below for enabling Branded Text for a Number.

## Enabling Branded Text for a Specific Phone Number, Sender ID, or Short Code

You can enable Phone Number, Sender ID, and Short Code for Branded Text. Once you enable the Branded Text feature for your tenant, you can enable it for a Number and map the corresponding RCS App IDs to send upgraded messages.

**Steps** 

1. Log in to the <<prodname>> platform
2. Navigate to **Assets **> **Numbers** section.
3. Select **Phone Number**, **Sender ID **or **Short Code **from the **Number **Type.
4. Click **Action **> **Manage** associated with the **Phone Number**, **Sender ID**, or **Short Code**. 
5. Turn on the **Branded Text** option.  
   Ensure the **Branded Text Enablement **and the mapping of the respective **RCS App ID** is displayed.

   [block:image]{"images":[{"image":["https://files.readme.io/7f467ac524edadcfc285afdcab2eaa78499cae9916cbbedd425a5060c69970f2-2025-09-15_13-19-39.png","","Screenhot of enabling Branded Text for a Number."],"align":"center","border":true,"caption":"Enabling Branded Text "}]}[/block]
6. Click **Save**

> 📘 Note
> 
> Only approved App IDs appear in the RCS App ID drop-down list.

## Start Node

### Conditional Trigger in RCS

When you access the Start Node in the Flow Builder and select the RCS channel, you see the ‘**Trigger only when there are no live sessions**’ checkbox. When you enable this option, the RCS flow triggers only if no active sessions exist with a matching event type for the same RCS App and same user. If you enable Branded Text for the tenant, the system checks for active sessions across both RCS and Branded Text-enabled SMS flows. For more information refer to [Start Node](https://help.webexconnect.io/docs/start-node).

This prevents multiple flows from starting simultaneously for the same user, ensuring their conversation continues in the existing session until it either completes or times out.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/69aefd860ff07fe3a1d83cc0cd123208f1a10267828d82020afadfe6aa588191-2025-09-15_13-26-52.png",
        "",
        "Screenshot of Configuring RCS Event and enabling conditons."
      ],
      "align": "center",
      "border": true,
      "caption": "Configure RCS Event"
    }
  ]
}
[/block]


**For example:**  
Let us suppose that in a tenant, there are two RCS flows - Flow 1 and Flow 2. Both are configured with the same Event Type, 'Incoming Message' in the RCS Start Node. For Flow 1, Conditional Trigger (CT) is disabled, and for Flow 2, it is enabled. Consider that the Branded Text setting is not enabled for this tenant.

**Same Service:** Consider that both the RCS Flows (Flow 1 and Flow 2) are configured in the same service. The table below describes how these two RCS flows behave when an incoming message arrives, depending on their current states. Each row represents an independent scenario and it does not depend on the previous rows.

**RCS Flows (Flow 1 and Flow 2) are configured in the same service**

| Current State of Flow 1 (F1) | Current State of Flow 2 (F2) with Conditional Trigger Enabled | Outcome                                                          |
| :--------------------------- | :------------------------------------------------------------ | :--------------------------------------------------------------- |
| Is at Start Node             | Waiting on the Receive Node                                   | F1 will get triggered, and F2 doesn't trigger and keeps waiting. |
| Waiting on Receive Node      | Is at Start Node                                              | F1 will continue; F2 will not trigger.                           |
| Is at Start Node             | Is at Start Node                                              | Both flows, F1 and F2, will trigger.                             |
| Waiting on Receive Node      | Waiting on Receive Node                                       | Both flows, F1 and F2, will continue.                            |

**Different Service:** Consider that both the RCS Flows (Flow 1 and Flow 2) are configured in different services. The table below describes how these two RCS flows behave when an incoming message arrives, depending on their current states. Each row is representing an independent scenario and it does not depend on the previous rows.

**RCS Flows (Flow 1 and Flow 2) are configured in the different service**

[block:parameters]
{
  "data": {
    "h-0": "Current State of Flow 1 (F1),  \nService 1",
    "h-1": "Current State of Flow 2 (F2), Service 2, with Conditional Trigger Enabled",
    "h-2": "Outcome",
    "0-0": "Is at Start Node",
    "0-1": "Waiting on Receive Node",
    "0-2": "F1 will get triggered, and F2 will continue.",
    "1-0": "Waiting on Receive Node",
    "1-1": "Is at Start Node",
    "1-2": "F1 will continue; F2 will not trigger.",
    "2-0": "Is at Start Node",
    "2-1": "Is at Start Node",
    "2-2": "Both flows, F1 and F2, will trigger.",
    "3-0": "Waiting on Receive Node",
    "3-1": "Waiting on Receive Node",
    "3-2": "Both flows F1 and F2 will continue."
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


### Conditional Trigger in RCS when Branded Text is enabled:

If Branded Text is enabled for a tenant and the RCS App is mapped to a Number, and when the conditional trigger is enabled on the RCS Start Node, the system will check for any active SMS/Branded Text flows as well as RCS flows associated with that Number or RCS App. This check occurs only if the incoming event is a Text message.

**Incoming message handling with Branded Text enabled flows:**

When an incoming 'Text' message is received by the <<prodname>> platform on an associated RCS App that has a Number mapped, the system will duplicate the incoming message event for further processing. 

The duplicated message is converted into an SMS incoming message and is labeled as ‘Branded Text’ in the Message Source field. The duplicated message does not execute any new SMS or Branded Text flows. Instead, it only executes branded text-enabled SMS flows that are already waiting to receive a message on a Receive Node. 

**Example:**

Suppose there are three flows: Flow 1 and Flow 2 from Service 1, and Flow 3 from Service 2. The Number mapped to Flow 1 enables Branded Text and is mapped to RCS App 1. Therefore, Flow 1 is a Branded Text - enabled SMS flow. Flow 2 and Flow 3 are also mapped to RCS App 1:

- **SMS/Branded Text Flow 1**: The Start Node in Flow 1 is selected as SMS, and the keyword configured is 'Refill'. The next Node is the Receive Node.
- **RCS Flow 2**: The Start Node in Flow 2 is selected as RCS, with 'Incoming Message' as the event, and Conditional Triggering enabled on the RCS Start Node. The next Node is a Receive Node with 'Incoming Message' as the event.
- **RCS Flow 3**: The Start Node in Flow 3 is selected as RCS, with 'Incoming Message' as the event, and Conditional Triggering disabled on the RCS Start Node. The next Node is a Receive Node with 'Incoming Message' as the event.

When an incoming message from Number is `‘Refill'`, Flow 1 (the Branded Text-enabled SMS flow) is triggered and it sends an outbound message, which then gets upgraded to Branded Text and is delivered to the user. Flow 1 will then wait at the Receive Node.

Next, the user responds to this message as `"Yes, I want to Refill medicines"` through the RCS application. The incoming message, since it is a 'Text' message, will be duplicated as explained above. As SMS/Branded Text flow is waiting at the Receive Node, it will continue the SMS/Branded Text flow. The RCS message will not trigger Flow 2 because the SMS/Branded Text flow is already waiting at the Receive Node.

For more scenarios, refer to the [Illustration](#illustration)  table below.

## Illustration

The behavior of the flows is illustrated in the following table, based on the current state of each flow. Each of the scenarios below are considered to be independent.

### **Flow 1 and  Flow 2 Scenarios with Conditional Trigger Enabled:**

| Current State of SMS/Branded Text Flow 1 (F1) | Current State of  RCS Flow 2 (F2), with Conditional Trigger Enabled | Behaviour with duplicated SMS/Branded Text Incoming Message | Behaviour with RCS Incoming Message |
| :-------------------------------------------- | :------------------------------------------------------------------ | :---------------------------------------------------------- | :---------------------------------- |
| Waiting on Receive Node                       | Is at Start Node                                                    | Continue SMS flow                                           | Will not trigger the flow           |
| Waiting on Receive Node                       | Waiting on Receive Node                                             | Continue SMS flow                                           | Continue RCS flow                   |
| Is at Start Node                              | Is at Start Node                                                    | Will not trigger the SMS flow                               | Trigger RCS flow                    |
| Is at Start Node                              | Waiting on Receive Node                                             | Will not trigger the SMS flow                               | Continue RCS flow                   |

### **Flow1 and  Flow 2 Scenarios with Conditional Trigger Disabled:**

| Current State of SMS/Branded Text Flow 1 (F1) | Current State of  RCS Flow 2 (F2), with Conditional Trigger Disabled | Behaviour with duplicated SMS/Branded Text Incoming Message | Behaviour with RCS Incoming Message |
| :-------------------------------------------- | :------------------------------------------------------------------- | :---------------------------------------------------------- | :---------------------------------- |
| Waiting on Receive Node                       | Is at Start Node                                                     | Continue SMS flow                                           | Trigger RCS flow                    |
| Waiting on Receive Node                       | Waiting on Receive Node                                              | Continue SMS flow                                           | Continue RCS flow                   |
| Is at Start Node                              | Is at Start Node                                                     | Will not trigger the SMS flow                               | Trigger RCS flow                    |
| Is at Start Node                              | Waiting on Receive Node                                              | Will not trigger the SMS flow                               | Continue RCS flow                   |

### **Use case where there are three flows - Flow 1, Flow 2, and Flow 3, from different services:**

| SMS Flow 1 (S1)            | RCS Flow 1 (S1, CT-ON)     | RCS Flow 2 (S2, CT-OFF)    | SMS/Branded Text Incoming Message Outcome (Duplicated) | RCS Incoming Message Outcome              |
| :------------------------- | :------------------------- | :------------------------- | :----------------------------------------------------- | :---------------------------------------- |
| Is at the Start Node       | Is at the Start Node       | Is at the Start Node       | Will not trigger the SMS flow                          | Both RCS Flow 1 & Flow 2 get triggered    |
| Is at the Start Node       | Is waiting at Receive Node | Is at the Start Node       | Will not trigger the SMS flow                          | RCS Flow 1 continues, RCS Flow 2 triggers |
| Is waiting at Receive Node | Is at the Start Node       | Is at the Start Node       | SMS Flow 1 continues                                   | RCS Flow 1 blocked, Flow 2 triggers       |
| Is waiting at Receive Node | Is waiting at Receive Node | Is at the Start Node       | SMS Flow 1 continues                                   | RCS Flow 1 continues, Flow 2 triggers     |
| Is waiting at Receive Node | Is waiting at Receive Node | Is waiting at Receive Node | SMS Flow 1 continues                                   | RCS Flow 1 and Flow 2 continues           |
| Is at the Start Node       | Is at the Start Node       | Is waiting at Receive Node | Will not trigger the SMS flow                          | RCS Flow 2 continues                      |
| Is waiting at Receive Node | Is at the Start Node       | Is waiting at Receive Node | SMS Flow 1 continues                                   | RCS Flow 1 blocked, Flow 2 continues      |
| Is at the Start Node       | Is waiting at Receive Node | Is waiting at Receive Node | Will not trigger the SMS flow                          | RCS Flow 1 continues, Flow 2 continues    |

## Updates to Logs, Integrations and Reports

For outbound requests, two new fields ‘Attempted Upgrade to’, ‘Upgrade Result’ and for inbound requests, ‘Message Source’ are added in across the various sections in the application:

- **Attempted Upgrade To**- Indicates whether Branded Text was attempted during the transaction.
- **Upgrade Result **- Displays the outcome of the Branded Text upgrade attempt.
- **Message Source**- Displays the source of the incoming message.

> 📘 Note:
> 
> These changes apply only to Branded Text configured after v6.11.0. Users with Branded Text set up before this version does not receive the new details.

## Changes related to Outbound requests

When a Branded Text is enabled for your Number, you will see the following changes in these sections:

### Debug Console:

If Branded Text is enabled for your Number, for any transaction logs for SMS requests sent through this Number, displays the values as specified below:

- **Attempted Upgrade To**: The system displays the value as '**Branded Text**'.
- **Upgrade Result**: If the system successfully delivers the request as Branded Text, it displays the value as ‘**Upgraded to RCS basic**’. If the Branded Text upgrade fails and the system sends the request as SMS, it displays the value as ‘**Fallback to SMS**’. 
- Additionally, the system adds a new process log section to show steps involved in the fallback transaction.

For SMS requests that you send through a Number you do not enable for Branded Text, the system displays the following values:

- **Attempted Upgrade To**: The system displays the value as 'NA'.
- **Upgrade Result**: The system displays the value as ‘NA’.

For more information refer to Query by Transaction ID section on [Debug Console](https://help.webexconnect.io/docs/console#query-by-transaction-id) page. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b954013d2cd874f33c3bcdd3866b165db8b2814f8567bdc999028bb1b8e209c8-c52d2a9c-fda9-4168-8239-089014587109.png",
        "",
        "Screenshot of Transaction Details when Branded Text enabled and Fallback Process Log"
      ],
      "align": "center",
      "border": true,
      "caption": "Transaction Details when Branded Text enabled and Fallback Process Log"
    }
  ]
}
[/block]


### Export Logs & Schedule Logs

You can download or export outbound logs by selecting one or more Services, one or more Channels, and defining a specific time range. The downloaded Export Log excel file includes additional fields.

If you enable Branded Text for your Number, the outbound logs for SMS display the following values:

- **Attempted Upgrade To**: The system displays the value as '**Branded Text**'.
- **Upgrade Result**: If the system successfully delivers the request as Branded Text, the value displays as ‘**Upgraded to RCS basic**’. If the Branded Text upgrade fails and the system sends the request as SMS, the value displays as ‘**Fallback to SMS**’.

For SMS requests you send through a Number not enabled for Branded Text, the following values display:

- **Attempted Upgrade To**: The system displays the value as ‘NA’.
- **Upgrade Result**: The system displays the value as 'NA'.

These fields help capture Branded Text-related outcomes in your exported logs.

**Export to SFTP/S3 and Scheduled Export Logs:**

The fields **Attempted Upgrade To** and **Upgrade Result **are not included by default. These fields appear only when you select new fields and add a new schedule. Existing schedules remain unaffected.

For more information refer to Adding a Schedule Log section on [New Export Log](https://help.webexconnect.io/docs/new-export-logs#adding-a-schedule-log) page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3b1ef493bc6b32d6e58dad44089ddff15e769f24a3712bf6c0e6c1a877cfff51-5fb2fa4f-1292-4010-9344-0c03b75cfe7e.png",
        "",
        "Screenshot fo Schedule Export Log"
      ],
      "align": "center",
      "border": true,
      "caption": "Scheduled Export Logs"
    }
  ]
}
[/block]


### Outbound Webhooks

If Branded Text is enabled for your Number, the new fields '**Attempted Upgrade to**’ and ‘**Upgrade Result**’, are added in all delivery receipts-Submitted, Delivered, Failed, and Clicked. These fields are included in the Outbound webhooks request with the following values:

- **Attempted Upgrade To** - The system displays the value as '**Branded Text**'. 
- **Upgrade Result **- If request is successfully delivered as Branded Text, it displays the value as ‘**Upgraded to RCS basic**’. If the Branded Text upgrade fails and the system sends the request as SMS, it displays the value as ‘**Fallback to SMS**’.

For SMS requests sent through a Number not enabled for Branded Text, the system displays the following values: 

- **Attempted Upgrade To** – The system displays the value as ‘NA’. 
- **Upgrade Result** - The system displays the value as 'NA'.

For more information refer to SMS Delivery Receipts section on [SMS](https://developers.webexconnect.io/reference/sms-1#sms-delivery-receipts) Outbound Webhooks page.

```json Submitted
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Submitted",
      "code": "7501",
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Submitted",
      "attemptedUpgradeto": "Branded Text",
      "upgradeResult": "Fallback to SMS"
    },
    "subtid": "",
    "transid": "7f3af32c-8d6a-XXXX-XXXX-4805135ada71",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Delivered
{
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2022-10-10T13:53:13.749+01:00",
      "Description": "Delivered",
      "code": "7500",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards. 
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "9189xxxxxxxx",
      "destinationType": "msisdn",
      "deliveryStatus": "Delivered",
      "attemptedUpgradeto": "Branded Text",
      "upgradeResult": "Fallback to SMS"
    },
    "subtid": "",
    "transid": "7f3af32c-8d6a-XXXX-XXXX-4805135ada71",
    "callbackData": "",
    "correlationid": ""
  }
}
```
```json Clicked
{
    "deliveryInfoNotification": {
        "deliveryInfo": {
            "deliveryChannel": "sms",
            "Description": "http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html|192.0.2.1",
            "destinationType": "msisdn",
            "timeStamp": "2022-10-10T13:53:13.749+01:00",
            "additionalInfo": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "code": "7528",
            "deliveryStatus": "Clicked",
            "attemptedUpgradeto": "Branded Text",
            "upgradeResult": "Fallback to SMS",
            "destination": "4475xxxxxxxx"
        },
        "correlationid": "3bd8edf31c81-XXXXXXXX-290d-49e2-993e",
        "callbackData": "return callbackdata",
        "transid": "4b72d8a2-290d-XXXX-XXXX-3bd8edf31c81"
    }
}       "correlationid": ""
    }
}
```

### Data Streams

If Branded Text is enabled for your Number, the new fields '**Attempted Upgrade to**’ and ‘**Upgrade Result**’, are added to all delivery receipts - Submitted, Delivered, Failed, and Clicked. The data streams request includes the following values:

- **Attempted Upgrade To**- The system displays the value as ‘**Branded Text**’
- **Upgrade Result **-  If request is successfully delivered as Branded Text, it displays value as ‘**Upgraded to RCS basic**’. If the Branded Text upgrade fails and the request is sent as SMS, it displays value as ‘**Fallback to SMS**’.

For SMS requests sent through a umber not enabled for Branded Text, the system displays following values:

- **Attempted Upgrade To **- The system displays value as ‘NA’. 
- **Upgrade Result **- The system displays value as 'NA'.

For more information refer to SMS Delivery Receipts section on [Data Streams - SMS](https://developers.webexconnect.io/reference/data-streams-sms) page.

```json Submitted
{
  "x-wx-gtrid": "0dXXXXed-9XXe-6XX5-cXX3-a81XXXXXXXX5f4",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-03-04T15:30:28.744+05:30",
      "Description": "Submitted",
      "code": "7654",
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "+4477XXXX2543",
      "destinationType": "msisdn",
      "deliveryStatus": "Submitted",
       "attemptedUpgradeto": "Branded Text",
      "upgradeResult": "Fallback to SMS"
    },
    "subtid": "7dXXXXa6-4XX6-4XX4-8XX6-fdXXXXXXXXf9",
    "transid": "0007_1709XXXXXXXX06",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "SMSSendNode": "200",
      "serviceId": “1234”,
      "serviceName": "MyFirstSMSService",
      "flowId": “4321”,
      "flowName": “MyFirstSMSFlow",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  }
}
```
```json Delivered
{
  "x-wx-gtrid": "0dXXXXed-9XXe-6XX5-cXX3-a81XXXXXXXX5f4",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2024-03-04T15:30:33.000+05:30",
      "Description": "Delivered",
      "code": "7654",
      "messageCount":"1",//New variables will be sent starting v6.9.0 onwards. 
      "deliveryChannel": "SMS",
      "additionalInfo": "",
      "destination": "+4477XXXX2543",
      "destinationType": "msisdn",
      "deliveryStatus": "Delivered",
      "attemptedUpgradeto": "Branded Text",
      "upgradeResult": "Fallback to SMS"
    },
    "subtid": "7dXXXXa6-4XX6-4XX4-8XX6-fdXXXXXXXXf9",
    "transid": "0007_1709XXXXXXXX06",
    "callbackData": "",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "SMSSendNode": "200",
      "serviceId": “1234",
      "serviceName": "MyFirstSMSService”,
      "flowId": “43”21,
      "flowName": "MyFirstSMSFlow",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  }
}
```
```json Clicked
{
  "x-wx-gtrid": "4dda02a9-XXXX-XXXX-XXXX-2a7c1614e0c6",
  "deliveryInfoNotification": {
    "deliveryInfo": {
      "timeStamp": "2025-09-15T16:13:01.504+05:30",
      "Description": "https://www.gmail.com|107.77.224.156",
      "code": "1234",
      "messageCount": "",
      "deliveryChannel": "SMS",
      "upgradeResult": "Upgraded to RCS basic",
      "additionalInfo": "Mozilla\\/5.0 (Linux; Android 10; K) AppleWebKit\\/537.36 (KHTML, like Gecko) Chrome\\/133.0.0.0 Mobile Safari\\/537.36",
      "destination": "+1781XXXX232",
      "destinationType": "msisdn",
      "attemptedUpgradeto": "Branded Text",
      "deliveryStatus": "Clicked"
    },
    "subtid": "",
    "transid": "a81681b9-XXXX-XXXX-XXXX-11b673d4be91",
    "callbackData": "CallBackdata",
    "correlationid": ""
  },
  "dataIntegration": {
    "context": {
      "serviceId": "12326",
      "serviceName": "SMSNMXHTTPService1",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "true"
    },
    "appContext": {
      "tenant_identifier": "connectnmxstagingtenant",
      "Topic": "connectnmxstagingtenantTopic",
      "URL": "b-1.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-3.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096,b-2.dev-campaign-integrat.tefj3j.c20.kafka.us-east-1.amazonaws.com:9096",
      "webhookurl": "https://integrations.imiconnect.co/v1/integration/"
    }
  }
}
```

| Filed Name         | Description                                  | Example                                                                                                                                                                                                                                     |
| :----------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| attemptedUpgradeto | Displays if the message upgraded.            | If attempted upgrade to SMS, the value displayed is Branded Text. `"attemptedUpgradeto": "Branded Text"`                                                                                                                                    |
| upgradeResult      | Displays the outcome of the upgrade attempt. | If request is successfully delivered as Branded Text, Value displayed as ‘Upgraded to RCS basic’, if Branded Text failed and <<prodname>> sends request as SMS, value displayed is ‘Fallback to SMS’.  `"upgradeResult": "Fallback to SMS"` |

### Reports

When you select a service under the Entity dropdown, set the Channel/Flow to SMS, or enable Sender ID for Branded Text, you see Messages enabled for RCS Basic, Delivered as RCS Basic, and Delivered as SMS in the generated report. For more information refer to SMPP reports section on [Reports](https://help.webexconnect.io/v6.11.0/docs/service-reports#smpp-reports)  page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bc5333a6b73034f2ec2d89c668756a58ac94c19256542476d3cec5eb22e34fca-1ad112ed-31bb-40a5-b2d1-4207acbf2c2b.png",
        "",
        "Screenshot for Reports when enabled for RCS Basic"
      ],
      "align": "center",
      "border": true,
      "caption": "Reports When Message Enabled for RCS Basic"
    }
  ]
}
[/block]


### Usage Reports

The Number of message parts will be counted as before and shown under ‘Messages Sent’ column and ‘Messages Delivered as RCS Basic’ column in the SMS Outbound sheet. For more information refer to SMS Outbound section in  [Usage Report Fields](https://help.webexconnect.io/docs/usage-report-fields#sms-outbound)  page.

## Changes Related to Inbound Messages

### Debug Console

If you receive an incoming message through an RCS App or Asset to which a Number maps, the system duplicates the incoming message and labels its **Message Source** with the value ‘**Branded Text**’.

If you receive the message through regular SMS channels, the system displays the **Message Source** value as '**SMS**'.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/778f1e56bb122ee5f84b57a5b7c407be4480702586017c2e60d234dbb0bb2e14-f82f0eb3-4678-4298-92fa-8c996885831a.png",
        "",
        "Screenshot of Debug Console"
      ],
      "align": "center",
      "border": true,
      "caption": "Debug Console"
    }
  ]
}
[/block]


### Export Logs

If Branded Text is enabled for your Number. The inbound logs displays following field:

- **Message Source **- The value displays as '**SMS**' or ‘**Branded Text**’. 

If you receive an incoming message through an RCS App or Asset to which a Number maps, the system duplicates the incoming message and labels its **Message Source** with the value ‘**Branded Text**’.

If you receive the message through regular SMS channels, the Message Source value displays as 'SMS'.

- **Message Source **- displayed as '**SMS**'.

**Export to SFTP/S3**

If you enable Branded Text for your Number, the Export to SFTP/S3 displays the following field:

- **Message Source **- Value displayed as ‘**SMS**’ or ‘**Branded Text**’. 

If you receive an incoming message via an RCS App/Asset linked to a Number, the system duplicates it and labels its **Message Source **as ‘**Branded Text**'.  
Messages received through standard SMS channels are marked as **Message Source** as '**SMS**’.

For more information refer to Adding a Schedule Log section on [New Export Logs](https://help.webexconnect.io/docs/new-export-logs#adding-a-schedule-log) page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6ee799d522e57da825a8f97c0a839097913028e4540e192e2b2a06cd02053879-3ef88e1b-0f5f-4126-9b31-ca2f37fbfbc7.png",
        "",
        "Screenshot for Scheduled Export Log when enabled for Branded Text"
      ],
      "align": "center",
      "border": true,
      "caption": "Scheduled Export Log when Enabled for Branded Text"
    }
  ]
}
[/block]


### Outbound Webhooks

When a user configures an Outbound Webhook for a Number and an incoming message is received via an RCS app or asset linked to that Number, the Outbound Webhook payload for incoming messages will include:

- **Message Source **- value displayed as '**SMS**' or ‘**Branded Text**’

If an incoming message is received via an RCS App or Asset linked to a Number, it is duplicated and labeled it with **Message Source** as ‘**Branded Text**’.

Messages received through standard SMS channels are marked as **Message Source ** as ‘**SMS**’.

When an incoming message is received via an RCS app or asset linked to a Number, the system duplicates the message.  If outbound webhook is configured, the system sends the duplicated messages to both the registered Number and the RCS app.

For more information refer to SMS Incoming Messages section on [SMS](https://developers.webexconnect.io/reference/sms-1#sms-incoming-messages) Outbound Webhooks page.

```json Incoming Message
{
  "userld": "8765",
  "Channel":"'SMS",
  "da": "56263",
  "message_source": "Branded Text",
  "oa": "XXXXXXXXXX",
  "message": "Incoming Text Message",
  "tid": "0044_78263746XXX",
  "datetime": "2024-01-0714:36,09.266Z",
  "ts": "2024-01-07T14:36:09.266Z",
  "x_networkid": "9"
}
```

### Data Streams

When an incoming message is received via an RCS app or asset linked to a Number, the Data Streams payload for incoming messages will include: 

- **Message Source **- Value displays as ‘**SMS**’ or ‘**Branded Text**’.

If an incoming message is received via an RCS App or asset linked to a Number, the system duplicates and labels it with **Message Source **as ‘**Branded Text**’.  
Messages received through standard SMS channels are marked as **Message Source** as '**SMS**'.

For more information refer to SMS Inbound Message section on [Data Streams - SMS](https://developers.webexconnect.io/reference/data-streams-sms) page.

```json Incoming Message
{
  "transid": "cfXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "channel": "SMS",
  "dataIntegration": {
    "context": {
      "serviceId": "",
      "serviceName": "",
      "flowId": "",
      "flowName": "",
      "messagingAPI": "false"
    },
    "appContext": {
      
    }
  },
  "x_networkid": "",
  "message": "r660f",
  "userId": "",
  "message_source": "SMS",
  "tid": "cqXXXX81-2XXe-4XX5-9XXd-36XXXXXXXX3a",
  "clientUUID": "9eXXXX26-9XX1-4XX7-bXXa-d9XXXXXXXXbd",
  "x-wx-gtrid": "d7XXXX76-3XXa-4XXe-9XX3-d6XXXXXXXXf9",
  "oa": "+447XXXXXXX543",
  "datetime": "2024-03-04T15:20:10.725+05:30",
  "da": "447XXXXXXX44",
  "ts": "2024-03-04T15:20:10.725+05:30"
}
```

| Field Name     | Description                                 | Example                                                 |
| :------------- | :------------------------------------------ | :------------------------------------------------------ |
| message_source | Displays the source of the message received | If message_source is SMS the values displayed as 'SMS'. |

### Reports

When you select a Number enabled for Branded Text, messages received now show as '**Messages Received as SMS**' and '**Messages Received as Branded Text**' in the reports generated. For more information refer to [Reports](https://help.webexconnect.io/docs/service-reports#smpp-reports)  page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/97d561793328183203e67bb0918513a88ffaaebe0895f2a6ad1c88398a3d71c7-f2117883-cf86-4dab-a8f3-3c0119d76abe.png",
        "",
        "Screenshot of reports page displaying Message received as SMS and Message received as Branded Text"
      ],
      "align": "center",
      "border": true,
      "caption": "Message Received as SMS and Message Received as Branded Text"
    }
  ]
}
[/block]


### Usage Reports

Incoming messages categorized with **Message Source **as ‘**Branded Text**’ will not be counted in SMS Inbound Report. For more information refer to SMS Inbound section in [Usage Reports Fields](https://help.webexconnect.io/docs/usage-report-fields#sms-inbound) page.