## Which channels are supported in Webex Connect Sandbox?

Channel support in sandbox is limited to SMS, Voice, and WhatsApp. You will need to subscribe for the full platform access if you want to explore additional channels.

Please refer to [a list of countries](https://developers.imiconnect.io/reference/sms-and-voice-support-in-sandbox) you can use <<prodname>> Sandbox for sending or receiving test SMS messages and voice calls.

## Whom all can I send messages to and receive messages from in Sandbox mode?

You can send and receive messages only to the numbers that you have registered as test numbers with your sandbox account. Up to 5 numbers can be registered with one sandbox account and one number can only be registered with one sandbox account. 

## What features are not available in Sandbox mode?

Here's a brief list of features that are not available in <<prodname>> sandbox mode and require you to upgrade to <<prodname>> full platform mode:

- Additional channels such as Email, Push & In-App Messaging, <<AMB>>, Facebook Messenger, RCS, and more.
- Ability to buy numbers, or configure your own channel assets e.g., dedicated WhatsApp app for your business
- Full Node Palette for the Visual Flow Builder 
- Template management for all channels
- Bot Builder and NLP/NLU nodes
- Ability to invite your colleagues to work collaboratively in the same <<prodname>> account 
- Access to Profile Manager 
- Flow Analytics
- Embedded BI
- Logbooks
- Event Scheduler
- Answering Machine Detection (AMD) on voice
- Ability to invite your colleagues to work collaboratively in the same <<prodname>> account 
- Enterprise features such as Single Sign-On (SSO), Audit Trail, etc.
- Ability to create dedicated workspaces for various teams and departments using Groups and Teams 
- Ability to invite your colleagues to work collaboratively in the same <<prodname>> account 
- Higher Throughput for various APIs and more

## I don't see all the nodes in my Sandbox flow palette. Are there some limitations?

Yes, <<prodname>> Sandbox mode provides you access to a limited number of nodes that are sufficient for prototyping automated 2-way interactions/journeys across SMS, voice, and WhatsApp. The list of nodes that are available as part of <<prodname>> sandbox includes:

- Send SMS
- Send WhatsApp
- Call User 
- Play
- Record
- Call Patch
- IVR Menu
- Receive Node
- Http Request
- Data Parser
- Social Hour Check
- Evaluate Node
- Delay
- Branch Node

## Does <<prodname>> sandbox provide an API for bulk SMS sending?

No, <<prodname>> sandbox mode does not offer an API for bulk SMS messaging.

## How many SMS can we send in the sandbox environment?

You are allowed to send up to 10000 SMS and WhatsApp API requests (combined limit) using your sandbox account with 365 days from the day of account creation. You will see the error response saying “You have reached maximum transaction limit (quota)” with the error code 7020.

## Which all countries can I send and/or receive SMS and Voice calls from using <<prodname>> sandbox?

Please refer to [a list of countries](https://developers.imiconnect.io/reference/sms-and-voice-support-in-sandbox) you can use <<prodname>> Sandbox for sending or receiving test SMS messages and voice calls.

## What happens if I send a SMS via API to non-allowed list number?

You see the error code 7102 with the description “Invalid address” if the webhook URL configured for that service or you can see the same in the debug console by passing the message id. 

## What happens if I reply to SMS from a non-allowed list number?

You do not see those messages at our platform, if the number is not in the allowed list. 

## Can I change the numbers registered with my sandbox account?

You can register one primary and four secondary numbers with each <<prodname>> sandbox account. You cannot change the primary number (i.e., the first number that you register with <<prodname>>) but can change the secondary numbers registered with an <<prodname>> account. 

Please note that all the secondary numbers needs to be based in the same country as the primary phone number added with your sandbox account.

## How do I change the voice and language when making outbound calls using text to speech?

If you are using the APIs then you can mention your choice of language and voice. Please note that we only support neural voices in <<prodname>> sandbox mode. We currently support 70+ languages and 250 voices as mentioned in the [Supported Languages for Voice TTS (Text-to-Speech)](https://help.imiconnect.io/docs/supported-languages-for-voice) section.

## Why am I not able to create the new WhatsApp asset in the sandbox account?

<<prodname>> sandbox mode is aimed at enabling you to prototype and test 2-way interactions in a controlled environment and we provide a test asset for WhatsApp to help you meet that objective. Please [register your interest](https://imimobile.com/products/imiconnect/sandbox/request-upgrade) if you would like to upgrade to full platform mode.

## How do I add new messaging templates for WhatsApp?

WhatsApp template creation is not available as part of the <<prodname>> sandbox account. You would be able to create and manage WhatsApp templates once you upgrade to full platform mode.

## Where can I see the status of a message as submitted, delivered, read or failed?

You can use one of the following options to track the delivery status of your messages and/or calls:

- Visit Debug Console and search using the transaction ID or destination ID 
- Configure an outbound webhook to get notified about the message status in real time 
- Use 'Get Message Status API' 

## Can I setup chatbots using <<prodname>> sandbox account?

Currently, <<prodname>> Bot Builder and NLP/NLU nodes are available only in the full platform mode once you have subscribed for it. You can use <<prodname>> Sandbox for configuring basic chatbots through keyword matching or by integrating <<prodname>> flows with other bot platforms.

## Why do I see an error saying "We are unable to process your request" on the create account screen after submitting OTP?

At times, after submitting an OTP (One-Time Password), you might encounter an error indicating that "We are unable to process your request." This issue could be due to internet connectivity problems. Please check your internet connection and try again. Alternatively, you can attempt to log in using your credentials. If the problem persists, ensure that your device is connected to a stable network and try the process once more. Please refer to the below screenshot.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/50b4cddb14f8cc359f9de015301698c6cc5d14ce071b6055ced66ab8fb9cfd58-image.png",
        null,
        "Verify phone number & Create account"
      ],
      "align": "center",
      "border": true,
      "caption": "Verify phone number & Create account"
    }
  ]
}
[/block]