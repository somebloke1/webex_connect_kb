## If a flow containing a send node fails due to an issue with a preceding non-messaging node, will I see the failed transaction in Export Logs?

No, if a flow containing a Send Node fails due to an issue with a preceding non-messaging node, the Send Node will never get executed. Because of this, there will be no messaging transaction corresponding to the Send Node. Hence, you won't find this failed transaction in the Export Logs.

## Can I use same email ID to login into multiple Webex Connect tenants?

No, it is not possible to have multiple accounts linked with the same email id. Only one account can be created for one email id

## Which browsers can I use to access my Webex Connect account?

<<prodname>> can be accessed using the latest versions of Chrome, Mozilla, and Safari.

## What is the difference between Dialogflow ES and Dialogflow CX pre-built nodes?

Dialogflow CX represents an advanced iteration of ES. Dialogflow ES is best suited for simpler chatbot applications, whereas Dialogflow CX is tailored for intricate, multi-turn conversational experiences, particularly in enterprise-level settings. The choice between the two depends on the specific requirements and complexity of the project at hand.

See [here](https://cloud.google.com/dialogflow/cx/docs/how/migrate#:%7E:text=Dialogflow%20CX%20agents%20provide%20you,Dialogflow%20ES%20to%20Dialogflow%20CX) for more information about migrating from Dialogflow ES to Dialogflow CX.

## How is my File Rotation affected by DST (Daylight Savings Time) in Logbooks?

Let's try to understand the behaviour with the help of an example. 

Assume that you have configured a schedule in the logbooks and the time zone selected in **Rotation Policy** is included under DST (Day light saving time zone). In this case, there is a possibility that the scheduled file delivery can be skipped because of DST adjustment in the time zone.

For instance, say you are in Ireland, where daylight savings events occur at 3:00 AM, GMT. If you have a logbook schedule that initiates everyday at 3:15 AM, then on the day of the beginning of daylight savings time, the schedule will be skipped, since, 3:15 AM never occurs that day. If you have a schedule that triggers every 15 minutes of every hour of each day, then on the day and time that daylight savings ends, there will be an hour of time for which no schedule executes. This is because, when 3:00 AM arrives, it will become 1:00 AM again, however all of the scheduling during the 1:00 AM hour has already occurred, and the trigger’s next initiation time was set to 3:00 AM. This is why, for the next hour, no schedule execution will occur.

## I want to use an Integration (Prebuilt/Custom/HTTP) node immediately after a Social Hour node. However, I'm experiencing failures such as HTTP 429 Status Code ("Too Many Requests") and my flow execution stops. What should I do?

The HTTP 429 "Too Many Requests" status code means that the downstream system configured in integration (Custom/HTTP/Prebuilt) node is receiving requests faster than it can process them. This often happens when a large number of requests are released simultaneously from a Delay Node, Social Hour Node, or Event Scheduler and sent to integration node.

To resolve this, we recommend to implement a retry mechanism in your flow. Introduce a loop around the Integration or HTTP node that retries the failed request three times before stopping. This approach helps smooth out request bursts and increases the chances of successful processing, even if the target system is temporarily overloaded. Note that this does not guarantee all requests will be accepted by the downstream system. 

**How to implement a retry:**

1. Add a loop around the Integration(Custom/HTTP/Prebuilt) node.
2. Set the loop to attempt the request up to three times before failing the transaction.
3. Include a delay between retries to avoid overwhelming the endpoint (for example: 60 seconds, 120 seconds, and 180 seconds).
4. Optionally, log failed transactions using Logbook or Flow Outcome for monitoring and troubleshooting.