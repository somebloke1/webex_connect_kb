# Rules

Source: https://help.webexconnect.io/docs/rules
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:58+00:00

Rules evaluate conditions, validate user inputs, and route the incoming messages to various communication channels. The rules also focus on decision making. A rule can either be a business rule or a set of sequential tasks with simple <code>if-then</code> logic.<br>

You can configure rules on event triggers and associate them with various actions like sending a message or notifying a bot/HTTP service. A single rule is capable of supporting multiple actions.

You can also send extra parameters while configuring SMS requests.

## Triggers

A trigger automatically launches a flow when a defined event occurs. Triggers are set up to automate tasks using actionable events. Triggers enable you to automate complex business processes, eliminating the need to manually run the flow every time.<br>

You can configure any of the trigger categories for a service. A rule is triggered when events of the configured category meet the condition(s) defined within the rule.

1. Select **Trigger Category**.
2. Select the trigger event and add conditions.
3. Set **Conditions** (optional).  
   a. Choose an event parameter.  
   b. Select a condition.  
   c. Define a value.

You can build a condition using `AND` or `OR` logical operators. When you add `AND` to a condition, the whole expression must evaluate to true to qualify the condition. When you use `OR` in a statement, the statement is executed if any one of the conditions evaluates to true.



![Rule Triggers](https://files.readme.io/8039f17-2.jpeg)




## Channels and Trigger Events

Each communication channel has a set of pre-defined events that can trigger a flow.



| Channel | Possible Events |
| --- | --- |
| SMS | _ `Mobile Originated - MO`  <br>_ `On Link Click` |
| MMS | \* `Mobile Originated - MO` |
| RCS | _ `Incoming Attachment`  <br>_ `Incoming Message`  <br>_ `Location Response`  <br>_ `Postback`  <br>-`Subscribe`  <br>-`Unsubscribe` |
| Voice | _ `Inbound Call`  <br>_ `Missed Call` |
| Instagram | _ `Incoming Message`  <br>_ `Postback`  <br>\* `Message Deleted` |
| Email | _ `Incoming Message`  <br>_ `Subscribe`  <br>\* `Unsubscribe` |
| Mobile & Web App  <br>(i.e., Push, Live Chat and In-App Messaging) | _ `Custom Event`  <br>_ `Incoming Message`  <br>_ `Location Change`  <br>_`Typing Indicator` |
| Apple Messages for Business | _ `Conversation Closed`  <br>_ `Incoming Message`  <br>_ `Invitation Response`  <br>_ `Interactive Message`  <br>\_ `Typing Indicator` |
| Messenger | _ `Incoming Message`  <br>_ `On Link Click`  <br>\* `Postback` |
| WhatsApp | \* `Incoming Message` |
| Enterprise Chat and Email (Deprecated) | \* `Incoming Message` |




> 📘 Note
> 
> If +E.164 format is enabled for your tenant - all the numbers in the **Destination** field should follow the "+E.164" format.
> 
> This format displays the number with a "+" followed by the country code and the phone number.
> 
> \+E.164 format is not applicable to the numbers in the **Sender** field.
> 
> This applies to the following channels: SMS, Voice, RCS, and WhatsApp

## Apple Messages for Business Invitation Response

You can configure a rule to trigger when a customer responds to an Apple Messages for Business invitation message. The **Invitation Response** trigger is fired when Webex Connect receives the first customer response to the invitation.

You can add conditions using invitation response variables such as customer mobile number, invitation accepted status, and request identifier.

| Variable                 | Description                                                                | Supported Operators                                      |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| `abc.msisdn`             | Customer mobile number used for the invitation.                            | equals, notequals, contains, startswith, endswith, regex |
| `abc.invitationAccepted` | Boolean value that indicates whether the customer accepted the invitation. | equals, notequals                                        |
| `abc.requestIdentifier`  | Identifier used to correlate the invitation request and response.          | equals, notequals, contains, startswith, endswith, regex |

## Integrations and Trigger Events

Every integration in⁣ Webex Connect has a different set of trigger events for a flow.



| Integration | Possible Events |
| --- | --- |
| CCSP (Deprecated) | _ `Agent Chat Initiated`  <br>_ `Chat Closed`  <br>_ `Chat Idle`  <br>_ `Chat Opened`  <br>_ `Chat Picked`  <br>_ `Chat Reopened`  <br>_ `Chat Transferred`  <br>_ `Custom Event`  <br>\* `Incoming Message` |
| Skype for Business (Deprecated) | \* `Incoming Message From Skype` |
| BOT (Deprecated) | _ `Custom Event`  <br>_ `Handover`  <br>_ `Milestone Reached`  <br>_ `Notify`  <br>\* `Unhandled Message` |




## Custom Trigger Events

| Custom       | Possible Events         |
| :----------- | :---------------------- |
| Webhook      | List of existing events |
| Custom Event | List of existing events |

## Actions

You can select more than one action for an event. All actions are executed with equal priority when an event occurs.

Actions for a rule can be sending a message on any of the channels, notifying an external URL, or initiating a workflow. For sending an outbound message, you can either enter the message or use one of the existing templates while configuring the rule. Notifying URL can be entered directly on the UI and the flow to be triggered can be selected from the drop-down list. You can add multiple actions within a single rule.

The list of actions that can be associated with a rule is: 

- Send SMS
- Send MMS
- Send RCS Message
- Initiate Voice Call
- Send Push Notification
- Live Chat/In-App Messaging 
- Send Messenger Message
- Send WhatsApp Message
- Notify URL
- Invoke a Flow
- Forward to Bot
- Forward to BOT+CCSP
- Forward to CCSP (Deprecated)
- Skype For Business (Deprecated)

## Notify URL

You can choose to notify a URL with the delivery report for your preferred channel. This field accepts only a valid URL or a variable. If an invalid URL is passed in an API request or via a variable, then such a request will not be considered eligible for retries.

**Validations for Notify URL:**

- It is an optional field for all the channels. Send node can be executed without including these values.
- The notify URL should be updated with the proper URL format. The system returns the error message when the Notify URL field is not updated correctly as ‘Invalid URL: field accepts only valid URL or variable.’
- When you provide a space in front of the URL, the system displays the 'Invalid URL: field accepts only valid URLs or variables' error message.
- When you provide space at the end of the URL, the system trims and ignores the space, and the URL receives DRs.
- There is no maximum length validation defined.
- Variables can be added to this field.

> 📘 Note
> 
> - It is recommended to use a valid authorization ID. If notification delivery fails, the failure is not logged in Debug Logs.
> - For Apple Messages for Business invitation messages, Notify URL can receive invitation submission success or failure notifications and invitation response events. Invitation response payloads include the resolved AMB user ID, `msisdn`, `invitationAccepted`, `requestIdentifier`, and the raw invitation response payload, when available.

### Adding Actions to Rules

To add an action in rule, follow the procedure below:

1. Select the required channel from **Select Actions**.



![Add New Rule](https://files.readme.io/d739314-2.jpg)




2. Select the **Event** and required number from **MMS** drop-down.



![Select Event and Conditions](https://files.readme.io/b15ac2b-3.jpg)




3. Click  **Next**. 
4. Enter the required details in the **Enter Action Details** page.



![Enter Action Details](https://files.readme.io/b15ac2b-3.jpg)




5. The **Confirm** page is displayed. Enter the required details.



![Add Details](https://files.readme.io/d87050e-MMS_-_Confirm.jpg)




- Name: Enter the name for the event rule.
- Start Date: Select the date on which you want the rule to be start.
- Start Time: Select the time on which you want the rule to start.
- End Date: Select the date on which you want the rule to be end.
- End Time: Select the time on which you want the rule to stop.
- Set a status for your rule: Select the required status Active/Inactive.
- URL: Enter the URL to be notified when the rule is successfully executed.

> 📘 Note
> 
> You can add multiple actions.

6. Click **Complete and save rule**.

### Notify URL Authorisation

To enable Notify URL Signature and Authorization, add an action in the rule and follow the procedure below:

1. Select the required channel from **Select Actions**.

   

![Select Actions](https://files.readme.io/1c2fac2f401be709b6b02a80cb4f94445435fb5bf5ebb2f1be91cb50a60ad410-d739314-2.jpg)


2. Select the **Event** and required app from the **WhatsApp** drop-down.

   

![Select Event And Add Conditions](https://files.readme.io/2ef261dacd8a95464eb542526030b95ec30f6430159435c05f61a9e0b7cc2610-8bf65a04-4af9-412b-a5ed-548cee5a5cef.png)


3. Click **Next**.
4. Enter the required details in the **Enter Action Details** page.

   

![Enter Action Details - Notify URL](https://files.readme.io/db0d7decb7ac9fa0f426d783a8587b1bea0d68f04df98aa48a4f05c799260b09-image-20250904-101808.png)


5. Select the **Enable Notify URL Authorization** checkbox and provide the associated details.

   

![Enter Notify URL Authentication](https://files.readme.io/d81ef8d44fec4e84524bfe8b94b61ca358bbb69dc27c1460373dcc77eb10f173-image-20250904-102029.png)


6. The **Confirm** page is displayed. Enter the required details.

   

![Add New Rule](https://files.readme.io/d53c1e9824fa5a21184fd61f9a549fad2a99da1925b766c5e929ddf0a81b51d8-image-20250904-102235.png)


7. Click **Complete and save rule**.