## What is RCS?

Rich Communication Services, or RCS, is a leap forward for the most commonly used app on mobile phones—the SMS inbox.

The power of RCS lies in the features it brings to native mobile messaging. RCS harnesses advanced device capabilities and enhanced UI elements to provide an app-like experience to traditional text messaging.

## Registering your brand

RCS support brand pages - which means customers can click on your brand logo within the conversation window and can view additional details about your brand.

This add a sense of trust to the conversation.

A brand page is designed to personalize your RCS chatbot and showcase it to the user. It contains elements that ensure your brand is well-represented

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1b86ce0-63I1OBTAin4dfOj3m921VUc_Yb4llbqOAcbruII0ir3qbxU6szTn_1CXf6-Lxicwbp6dUwNbcR0s2048.png",
        "63I1OBTAin4dfOj3m921VUc_Yb4llbqOAcbruII0ir3qbxU6szTn_1CXf6-Lxicwbp6dUwNbcR0=s2048.png",
        "Screenshot of Brand Page."
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Screenshot of Brand Page."
    }
  ]
}
[/block]


Features include: 

- Name (25 character limit) 
- Brand Logo - 224 x 224px (\<50kb | .jpeg)
- Chatbot Description 
- Contact Information (Phone, Email, etc.) 
- URL Link to Privacy Policy 
- Header Image - 1440 x 448px (.jpeg or .png ) & 1080 x 1080px (.jpeg or .png ) to accommodate for differences in Google and Samsung messaging client 

## Message types

RCS supports the following message types -

**Rich Text** -

With RCS, messaging within the native client is no longer restricted to 160 characters. Brands may send and receive text and emojis exceeding this traditional character limit of SMS.

**Suggested Replies** -

Suggested replies are text-based and act as a reply from the user. Tapping a suggested reply sends the label text back to the conversation/ brand. Brands can embed unique postback data in every suggested reply. When the user taps the suggested reply, the corresponding postback data is sent back to the business along with the text. Note: chip lists disappear once an option is tapped. - Up to 11 chips per suggested chip list (users can scroll horizontally through the chip list) - Max 25 characters of text per chip label.

**Suggested Actions** - 

Similar to suggested replies, suggested actions enable users to take an action within the messaging application. Tapping a suggested action does not send a message to the conversation, but rather performs an action within the RCS messaging app or within another app. This action is executed by a link or deep link behind the suggested action button. The business can embed unique postback data in every suggested action.

Actions include • Dial a phone number • Open a URL • Create a calendar event • Request user’s location • Launch an app (such as Maps)

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bb323ea-image_35.png",
        "image (35).png",
        "Screenshot of Suggested Actions."
      ],
      "align": "center",
      "sizing": "500px",
      "caption": "Screenshot of Suggested Actions."
    }
  ]
}
[/block]


**Media **-

RCS messages can contain various types of media. Brands can send media files of the following types: Images — BMP, GIF, JPEG (highly recommended), PNG Videos — MPEG-4 Audio files — MP4, M4A, MP3, WAV Support for other file types, such as PDFs, is coming in a future release.

**Rich Cards** -

Rich cards are used to display information to a user in a more visual format than plain text. A Rich card contains the following fields, in this relative order: 

1. Image or Video 
2. Title Text 
3. Description Text 
4. List of Suggested Replies 
5. List of Suggested Actions 

Each of these fields are optional, although at least one of fields 1-3 must be included to form a viable card. Standalone rich cards expand to the full width of the conversation. They can either be vertical or horizontal in orientation.

**Carousels **-

Multiple rich cards can be sent as a carousel in a single message. There must be at least 2 and up to 10 cards within a carousel. The RCS messaging app will render carousels such that the fields within all contained cards are aligned. All media within the cards must have the same height

## Setting up Delivery Receipts and Inbound Messages

You can start receiving RCS delivery receipts for outbound messages, message content for inbound messages from your customers by setting "[Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks-api-ref)" under Integrations.

Supported outbound webhook events include:

- Submitted
- Delivered
- Read
- Failed

Supported inbound messages include:

- Text
- Attachment
- Postback
- Location
- Subscribe
- Unsubscribe

For detailed JSON webhook formats, please refer to [RCS Outbound Webhooks](https://developers.webexconnect.io/reference/rcs-outbound-webhooks#rcs-incoming-messages--events).

## Handling Subscribe and Unsubscribe events

<<prodname>> supports RCS Subscribe and Unsubscribe events, enabling real-time capture and response to customer opt-in and opt-out actions within your flows. These events help your enterprise honor user preferences and simplify consent management.

- **Subscribe**: Adds a user to a specific event type, allowing them to receive notifications when the event occurs. 
- **Unsubscribe**: Removes the user from the event subscription, stopping notifications. When a user clicks Subscribe or Unsubscribe, the RCS gateway sends a notification to <<prodname>>, which makes the events available for use in flows, outbound webhooks, and other integrations.

> 📘 Note:
> 
> When an end user sends an Unsubscribe or Subscribe request, you may also receive a separate “STOP” or “START” message as an additional incoming message. This helps you transition to the new Unsubscribe and Subscribe webhook events.

## Opt-in management

Opt-in is mandatory before sending a message to the customer. 

An existing opt-in for enterprise messaging may work depending on the wording of the current opt-in process.

All operators verify the opt-in process before allowing enterprises to go live with RCS journeys.

## Are gaming/gambling clients allowed?

Some operators choose to allow gambling clients and some don't. There is currently no consistent policy across the industry.

Reach out to your account manager for more information.

## What happens if a customer doesn't have data connectivity?

If a user does not have data connectivity, messages are queued and sent to the user once they are online

## Are bot only experiences supported?

RCS has no requirement for a human agent to be mandatory. So enterprises can build bot only experiences.

However, we recommend that enterprises provide a suitable fallback mechanism for users to rely upon if the bot fails.

## What regions does Webex Connect have connectivity in?

<br />

## Regions where Webex Connect has connectivity

<<prodname>> today has RCS connectivity in the following countries -

Europe -

- United Kingdom
- France
- Spain
- Germany
- Norway
- Sweden
- Greece
- Italy
- Austria
- Belgium
- Netherland
- Romania
- Portugal

North America -

- United States of America
- Canada
- Mexico

South America -

- Brazil
- Peru

Middle East & Africa -

- Jordan
- Nigeria
- DR Congo
- South Africa

## Can customers opt-out?

Yes, every RCS journey must provide a way for customer to opt-out

## Using API to send RCS messages

We support outbound messages through messaging API. More information on the API is available in our [developer documentation](https://developers.imiconnect.io/reference#send-message).

## What end-user clients are supported?

Currently RCS works on most Android devices with one of Android Messages or Samsung Messages app provided the operator in the region has enabled it.

## Can businesses send promotional content?

Yes, RCS is perfectly suited for promotional content.

However, customer opt-in proof is requested by most operators and customer also must be given an option to opt-out

## Is the channel end to end encrypted?

Currently, RCS is not end to end encrypted due to government policies for operators on lawful interceptions

## Are there any throughput limitations?

Depending on the region and operator, RCS does have throughput limitations.

If you are sending out more than million messages a day, please reach out to your customer success manager/ account manager.

## How does the smsFallback feature work?

When Webex Connect sends an RCS message request to the RCS operator, the operator performs verification checks on the request. If the RCS operator rejects the request, Webex Connect utilizes the information provided in the smsSenderId and text fields to send an SMS using the SMS operator.

Even if the request is accepted by the RCS operator, it may still fail due to asynchronous verifications or rejections from the MaaP. Additionally, if the MaaP is unable to deliver the request, it will respond with a failure to the RCS operator. In such cases, Webex Connect receives a outbound webhook response and reutilizes the smsSenderId and text fields to send an SMS, through the SMS operator as a fallback.

## How to debug smsFallback message?

When submitting a request through the API, the response will include a messaging transaction ID that can be used to track and debug the status of the RCS message. If the RCS message fails, a new messaging transaction is generated with the transaction ID appended with the variable "\_fallbackrcs" to enable further troubleshooting of the SMS message that was triggered as a fallback due to the failure of the RCS message.

**Example**:  
If the transaction ID for the RCS message is _"d3a6f618-d203-48d1-916a-e690fb9d2fb8"_, then the corresponding transaction ID for the SMS fallback message triggered due to the failure of the RCS message would be _"d3a6f618-d203-48d1-916a-e690fb9d2fb8_fallbackrcs"_.