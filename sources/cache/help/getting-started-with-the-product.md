# The beginner's guide to Webex Connect

Source: https://help.webexconnect.io/docs/getting-started-with-the-product
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:47+00:00

Webex Connect makes it easy for you to automate customer interactions across 10+ channels by providing a drag-and-drop flow builder. It does away with the need to write complex programs and to go through the traditional software development lifecycle.  

Here are the key steps for automating a customer interaction using Webex Connect:

a. Configure the customer interaction channel(s) you want to use.  
b. Integrate with required business systems like CRM _(optional based on requirements/use case)_  
c. Create a [Service ](https://help.imiconnect.io/docs/introduction)(i.e., a named workspace for managing your customer interaction use case).  
d. Navigate to the service you created in the last step. Build and launch the communication flow using Webex Connect visual flow builder. Refer the navigation guide for Flow Builder [Navigating Flow Builder Canvas.](https://help.imiconnect.io/docs/flow-interface).

**_For example_**, if you want to build a simple communication flow to remind your customers about an upcoming appointment using SMS and trigger the flow simply by invoking an API or uploading a file. Here's how you can do so:

a. As this is an SMS reminder, you will need a phone number to send SMS. You can buy the numbers by visiting 'Assets -> Numbers' section

b. The next step is to integrate any required backend enterprise systems with Webex Connect. For example, you can integrate your CRM system with Webex Connect to fetch the appointment details. (_We recommend skipping this step to keep the things simple for the first time user_)

c. Create a [new service](https://help.imiconnect.io/docs/create-a-service-on-imiconnect).

d. Configure and deploy the desired communication flow using Webex Connect [visual flow builder](https://help.imiconnect.io/docs/sending-automated-sms-using-imiconnect-visual-flow-builder).

That's it. Once live, you can invoke the flow by making an API call. 

## Done making your first flow and ready to explore more?

Now that you've successfully created your first flow, let's explore a few more use cases to help you understand other platform capabilities. 

The use cases listed below offer a hands-on experience for developing end-to-end customer journeys using Webex Connect.

| S. No. | Title                                                                                                                                                               |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | [How to configure a Two Factor Authentication on Webex Connect?](https://help.imiconnect.io/docs/how-to-configure-two-factor-authentication-on-imiconnect)           |
| 2      | [How to set up a customer-initiated WhatsApp conversation?](https://help.imiconnect.io/docs/setting-up-a-customer-initiated-whatsapp-conversation-using-imiconnect) |

## Know more about supported channels

We live in an increasingly multichannel world characterised by the rapid-adoption of new communication channels. Webex Connect enables you to interact with your customers over their preferred channels by offering pre-built access to multiple communication channels. Here are some articles and tutorials on how you can use various channels supported by Webex Connect:

| S.No. | Channel/Apps                                                                         |
| :---- | :----------------------------------------------------------------------------------- |
| 1     | [SMS](https://developers.imiconnect.io/reference#section-smsmessage)                 |
| 2     | [Voice](https://developers.imiconnect.io/reference#call)                             |
| 3     | [MMS](https://developers.imiconnect.io/reference/mms-api)                            |
| 4     | [Email](https://help.imiconnect.io/docs/email)                                       |
| 5     | [Push Notifications](https://developers.imiconnect.io/reference#section-pushmessage) |
| 6     | [In-App Messaging](https://help.imiconnect.io/docs/mobile-web)                       |
| 7     | [Live Chat](https://help.imiconnect.io/docs/mobile-web)                              |
| 8     | [Apple Messages for Business](https://help.imiconnect.io/docs/apple-business-chat-1) |
| 9     | [Facebook Messenger](https://help.imiconnect.io/docs/facebook-messenger)             |
| 10    | [Instagram](https://help.imiconnect.io/docs/instagram)                               |
| 11    | [Whatsapp](https://help.imiconnect.io/docs/whatsapp)                                 |
| 12    | [RCS Business Messaging](https://help.imiconnect.io/docs/rcs)                        |