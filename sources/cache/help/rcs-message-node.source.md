RCS (Rich Communication Service) is an enriched messaging service that works on nearly 800,000,000 Android devices globally. It is an exciting way for brands to connect to their customers. Its app-like functionalities drive more engagement between brands and their customers.<br>

In the US, and UK, and Canada - RCS will work on most android devices that were released with Android OS v.8 or later.  Check with your client team for support in other countries.

The _RCS message_ node allows you to bring in rich messaging capabilities into your flows enabling you to interact with your customers in an efficient manner.<br>

Use the [RCS Capability Node](doc:rcs-capability-node) as a predecessor to this node to know if the user's mobile device has RCS capability.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/66bb756-rcs_message.png",
        "rcs_message.png",
        "Screenshot of RCS Message Node"
      ],
      "align": "center",
      "caption": "RCS Message Node"
    }
  ]
}
[/block]


## Prerequisites

Make sure that you have created and configured an [RCS App](doc:rcs) before you can start using the RCS message node in any of the flows.

## Node Configuration

Double-click the node to enter/specify various parameters to complete the node configuration. Perform the following steps to configure the node:

1. Select a **Destination Type**.
   - **Customer Id** - the profile ID of the user
   - **MSISDN** - the mobile number of the user.
2. Enter a value/variable name that contains the customer ID or the mobile number for the selected **Destination** type.
   > 📘 Note
   > 
   > If +E.164 format is enabled for your tenant - all the numbers in the **To** field should follow the "+E.164" format.
   > 
   > This format displays the number with a "+" followed by the country code and the phone number.
   > 
   > \+E.164 format is not applicable to the numbers in the **From** field.
3. Enter an integer in the **Carrier** field if you already know the carrier that the customer uses. Leave it blank if unsure.  
   It is useful when sending messages to users on a single mobile operator and increases the message throughput significantly when provided. See the list of [carrier IDs](doc:carrier-ids-for-rcs-capability-and-rcs-message-nodes).
4. Select an appropriate **Message Type**. Webex Connect supports the following message types for RCS:
   - _Text_ - allows you to send a simple text message.
   - _File_ - allows you to include a file in the message. When you select this type, you can also include the size of the media file along with its location. Provide the size in bytes. File size is recommended and shall be greater than zero.
   - _Rich Card_ - allows you to send information to a user in a more visual format than plain text. Rich cards can contain image/video, the title of the message, a description, list of suggested replies/actions.
   - _Carousel Card_ - allows you to send multiple rich cards as a single message. You can include 2-10 rich cards in a carousel. The RCS messaging app renders the carousels such that the fields within all contained cards are aligned. All media within the cards must be of the same height. Along with the media details, you can also specify the size of each media file in bytes. File size is recommended and shall be greater than zero.
   - _Typing Indicator_ - indicates that the user is typing in the message window.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6642d1c-RCS2.jpg",
        "RCS Message Node RCS Message Configuration Window.png",
        "Screenshot of RCS Message Configuration Window."
      ],
      "align": "center",
      "border": true,
      "caption": "RCS Message Configuration Window"
    }
  ]
}
[/block]


5. Do the **Message Configuration** by completing the following steps:
   - Enter a message for the message type **Text**.
   - Enter a URL of the file that you want to include in the RCS message for the message type **File**. Audio, Image and Video files are supported.
   - Select/configure the following fields for **Rich Card**. Refer to [**supported media**](https://help.imiconnect.io/docs/rcs-message-node#supported-suggestions) for recommended formats and resolutions:  
      (a) Select the **Card Orientation** - **Vertical** or **Horizontal**.  
      (b) Select the **Media** height - **Short**, **Medium**, or **Tall**.  
      (c) Enter a **Media URL** - the URL that points to the media. The character limit of the URL is 2048 characters.  
      (d) Enter a **Thumbnail URL** - the URL that points to the thumbnail of the media. The character limit of the URL is 2048 characters.  
      (e) Provide a suitable **Title** for the rich card. The character limit is 200 characters.  
      (f) Provide an appropriate **Description** for the rich card message. We recommend keeping descriptions as short as possible to avoid truncation.  
      (g) Click **Add Suggestions** to add buttons within the message. You can add up to 4 suggestions within the message. For example, on an order delivery notification rich card, you can add a **Reschedule** or **Leave with neighbor** suggestion to suggest a different time/place for the order delivery.
   - Select/configure the following fields for **Carousel Card**. Refer to [**supported media**](https://help.imiconnect.io/docs/rcs-message-node#supported-media) for recommended formats and resolutions:  
          (a) Select the **Card Width** - **Small** or **Medium**.  
         (b) Select the **Media Height** - **Short**, **Medium**, or **Tall**.  
          (c) Enter a **Media URL** - the URL that points to the media. The character limit of the URL is 2048 characters.  
          (d) Enter a **Thumbnail URL** - the URL that points to the thumbnail of the media. The character limit of the URL is 2048 characters.  
          (e) Provide a suitable **Title** for the rich card. The character limit is 200 characters.  
          (f) Provide an appropriate **Description** for the rich card message. We recommend keeping descriptions as short as possible to avoid truncation.  
          (g) Click **Add Suggestions** and select one of the [**available suggestion types**](https://help.webexconnect.io/docs/rcs-message-node#supported-suggestions) to add buttons within the message. You can add up to 4 suggestions within the message.  
          (h) Use the arrow buttons on the carousel card to move between the rich cards in the carousel. You can also use the switch controls located at the bottom of the carousel card for easy navigation. You can add rich cards to the carousel using the add icon. Use the add/delete icons located at the upper-left corner of the carousel card to delete any rich card.

> 📘 Carousel Card
> 
> A carousel card must contain at least **2** rich cards. You can include a maximum of **10** rich cards within a carousel card.

6. Click **Add Suggestions** and select one of the [**available suggestion types**](https://help.webexconnect.io/docs/rcs-message-node#supported-suggestions) to add suggestions/quick replies outside the message. You can add up to 11 suggestions.
7. Correlation ID - You can assign a unique ID of your choice to each RCS message. This ID is returned to the platform with the delivery report and can be used to identify the message.
8. Callback Data - In case there is additional data to be sent along with the delivery reports to the URL, you must specify that here.  
   **Validations for Callback Data & Correlation ID**:
   1. Callback Data, Correlation Id fields are optional for all the channels. Send node can be saved without providing these fields.
   2. All characters, Alphabets, Numbers, and special characters are accepted.
   3. Variables can be added.
   4. Hard coded values are accepted.
   5. On Platform side, there is no Max or Min length validation for these fields.
9. Notify URL - You can choose to notify a URL with the delivery report for RCS message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.  
   **Validations for Notify URL**:
   1. It is an optional field optional for all the channels. Send node can be saved without providing these fields.
   2. Notify URL should be filled with proper URL format. Otherwise, error message ‘Invalid URL, field accepts only valid URL or variable’ will be displayed.
   3. When space is provided in front of the URL, Invalid URL, field accepts only valid URL or variable’ will be displayed.
   4. When space is provided at the end of the URL, space gets trimmed and ignored and DRs are received to the URL.
   5. No Max length validation.
   6. Variables can be added to this field.
10. Select **Advanced Options**. This is optional.
    - **Wait for** - you can configure the RCS message node to wait for _Gateway Submit_/_Delivery Report_/_Read_ receipts. The **Time out** period is in seconds. 
    - **Expiry** - you can configure the RCS message to expire using either the _UTC_ (date and time) or the number of _Seconds_.

You can see a preview of the RCS message under the **Message Preview** pane. This preview is based on how the message appears on Android Messages on a Google Pixel device.

### Limits and Best Practices

You can see the list of field/elements and their best practices under this pane.

[block:parameters]
{
  "data": {
    "h-0": "Field/ Element",
    "h-1": "Limits and Best Practices",
    "0-0": "Title",
    "0-1": "Max 200 characters",
    "1-0": "Description",
    "1-1": "Max 2000 characters",
    "2-0": "Thumbnail",
    "2-1": "• Max file size: 100 kB (Recommended ≤50 kB)  \n• Dimensions: 800 × 800 px, square  \n• JPG/PNG",
    "3-0": "Media (Images, Video, PDF Preview)",
    "3-1": "• Heights: 112 DP (Short), 168 DP (Medium), 264 DP (Tall)  \n• Total card payload limit: 250 kB",
    "4-0": "Suggested Replies",
    "4-1": "• Up to 4 per card  \n• Max 25 characters each",
    "5-0": "Suggested Actions",
    "5-1": "• Up to 4 per card  \n• Max 25 characters each",
    "6-0": "Chip List Suggestions",
    "6-1": "Up to 11 suggestions below carousel",
    "7-0": "Carousel",
    "7-1": "• Up to 10 cards  \n• Small card: 542 DP height, 180 DP width  \n• Medium card: 592 DP height, 296 DP width",
    "8-0": "Full-Screen View",
    "8-1": "Auto-enabled for all carousels",
    "9-0": "Payload Limit",
    "9-1": "250 kB max per card (including text + media)"
  },
  "cols": 2,
  "rows": 10,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](doc:variable-management).

## Output Variables

You can see the data that this node generates as output [variables](doc:variable-management). These variables are available for use in subsequent nodes. The standard output variables for this node are:

- **sendDateTime** - contains the date and time at which the message was sent from the node
- **gatewayTid** - contains the gateway transaction id of the message
- **deliveryStatusDescription** - contains the delivery status - success or failure
- **deliveryStatusCode** - contains the delivery status code. See the [API Statue Code section](doc:api-codes) for the status codes
- **response_data** - contains the response received
- **response_interactive** - contains the interactive response received.

## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. 

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)  \n  \n**Note**: You can see this node edge only when you complete the node configuration.",
    "0-1": "> _ **onSuccess** - the flow exits through this node when it is a success  \n> _ **onSubmit** - the flow exits through this node when a wait for gateway submit condition is configured and is a success.  \n> \\* **onDeliveryReportSuccess** - the flow exits through this node when a wait for delivery report condition is configured and is a success.",
    "1-0": "Timeout (yellow/amber)",
    "1-1": "> \\* **onTimeout** - the flow exits through this node when a timeout occurs",
    "2-0": "Error (red)",
    "2-1": "> _ **onError** - the flow exits through this node outcome when there is an error  \n> _ **onPolicyFail** - the flow exits through this node outcome when the expiry condition cannot be met  \n> \\* **onDeliveryReportFail** - the flow exits through this node when a wait for delivery report condition is configured and is a failure."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

## Supported Suggestions

Suggestions include quick replies and suggested actions that enable users to reply quickly or take actions directly from within the message. The supported suggestions are:

- **Simple Reply** - a simple pre-configured text message
- **View Location** - coordinates of the location that you want to view
- **Dial Phone** - telephone number that you want to dial
- **Share Location** - the name of the location that you want to share
- **Open URL** - a website link that you want to send
- **Calendar Event** - the details of the event that you want to add to the calendar.

## Supported Media

This section provides detailed information about the size, resolution, and format for the images. imiconnect supports the following media in RCS messages:

[block:parameters]
{
  "data": {
    "h-0": "Media Type",
    "h-1": "Format",
    "h-2": "Size",
    "h-3": "Resolution",
    "0-0": "Image",
    "0-1": "_ BMP  \n_ GIF  \n_ JPEG (highly recommended)  \n_ PNG",
    "0-2": "500 kb or less",
    "0-3": "**Stand-alone Rich Card**  \n  \n> _ Short: 1085x310 pixels (3.5:1 ratio)  \n> _ Medium: 1080x720 pixels (1.5:1 ratio)**Rich Card in Carousel**  \n> 1080x787 pixels (1.37:1) is the recommended resolution",
    "1-0": "Video",
    "1-1": "MPEG-4",
    "1-2": "",
    "1-3": "",
    "2-0": "Audio",
    "2-1": "_ MP4  \n_ M4A  \n_ MP3  \n_ WAV",
    "2-2": "",
    "2-3": ""
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## Dynamic Carousels

Dynamic carousels allow you to send and configure carousel messages without prior configuration of fixed number of cards.

For example, you start node trigger [Inbound Webhooks](doc:inbound-webhooks) or [HTTP Request Node](doc:http-request) may return a dynamic array response as a part of customer journey.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/404a096-RCS3.jpg",
        "RCS Message Node Dynamic Carousel in RCS Node.png",
        "Screenshot of Dynamic Carousel in RCS Send Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Dynamic Carousel in RCS Send Node"
    }
  ]
}
[/block]


Dynamic carousel node can loop over an array and configure cards as a part of a flow run time.

Let's take the below example of recommendations of cars for an imaginary John

```json
{
   "name":"John",
   "age":30,
   "cars":[
      {
         "name":"Ford",
         "description":"This is a good car 1",
         "image":"https://images.com/ford.jpg"
      },
      {
         "name":"BMW",
         "description":"This is a good car 2",
         "image":"https://images.com/ford.jpg"

      },
      {
         "name":"Fiat",
         "description":"This is a good car 3",
         "image":"https://images.com/ford.jpg"
      }
   ]
}
```

To send this is a dynamic carousel to the user -

- Source Variable - Enter the source input variable here. For example if this JSON is expected as a response to earlier HTTP API call then it will be available in **http.response** variable from the input variable list 

All the variables that you intend to loop in the carousel should point to the first array variable. So in this particular case, let's say we want to send cards to the customer with each car in each carousel card. These input variables need to be entered manually and configured into the respective carousel fields as below. In that case, the variables will be configured as following -

- Title - $.cars[0].name
- Description - $.cars[0].description
- Media Url - $.cars[0].image 

These variables are JSON path representations of individual key value pairs from the source variable. 

> ❗️ Incomplete Arrays
> 
> Any incomplete arrays will fail the dynamic carousel send node. The node will only loop on completed arrays up-to 10 cards or the value of max cards set in the send node.
> 
> Dynamic carousel loops only run for variables within the carousel card. Suggestions outside the carousel card will **NOT** be looped.
> 
> Loops will only be run on the first level of array nesting.