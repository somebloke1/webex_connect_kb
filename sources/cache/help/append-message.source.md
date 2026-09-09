When setting up flows in Webex Connect, you may use this node to append a message to an ongoing conversation with the end customer. This node utilizes the **Append message ** API from Webex Engage.

## Configuration

To configure a Append message conversation node, follow these steps:

1. Drag and drop the **Append message** node from the Node palette from the left side of the screen.
2. Double-click the Append message node to view the configuration settings.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3813306e2490b7581480dc8f5f55b774a5ee45498d4f1d9d08167c90e2c66061-image.png",
        null,
        "Screenshot displaying the Configuration Settings for Append message node."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Configuration Settings for Append message node"
    }
  ]
}
[/block]


3. Choose **Create conversation** from the Method Name drop-down list.
4. Choose **Authorization** from the Node Runtime Authorization drop-down list.  
   We recommend you set Authorization to a Default Authentication configured in [WxEngage's Integrations](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) screen under WxConnect's Integrations. Once you re-authenticate from the Integrations screen, all your nodes across flows will pick up the updated token.
5. Choose a channel from the **Channel** drop-down list.

- **SMS** - If you choose SMS channel, you will view following settings:
  - **Conversation Alias ID** - $(n6.conversationId).  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables.
  - **Messages** - Select a radio button Single or Dynamic message.
    - **Single Message**: If you select Single Message radio button, you will view the following settings:
      - **Message Alias ID** - In general the value is set to **$(n2.messenger.transId)**.  
        A unique auxiliary external reference identifier is used to map the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type** - Choose Text from the Message Type drop-down list.
      - **Text** - In general the value is set to Custom Variable for Send nodes or $(n30.sms.message) from Receive nodes.
      - **Timestamp** - (ISO8601 Format in UTC Timezone) - $(n30.send.sentDateTime) for Send nodes and $(n30.sms.timestamp) for Receive nodes.
    - **Dynamic message (JSON)** : Pass a variable containing a JSON. Refer to [SMS Schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/sms-1).
- **Facebook Messenger** - If you choose Facebook Messenger channel, you will view following settings:
  - **Conversation ID** - **$(n6.conversationId)**.  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables.
  - **Messages**- Select a radio button Single or Dynamic message.
    - **Single Message**: If you select Single Message radio button, you will view the following settings:
      - **Message Alias ID** - In general the value is set to** $(n2.messenger.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Inbound or Outbound or Announcement.
      - **Message Type** - Set to Text with attachments.
      - **Text** - $(n2.messenger.message).  
        In general value is set to Custom Variable for Send nodes or$(n30.messenger.message) from Receive nodes.
      - **Attachments** - $(parseDataAttachment).  
        This is one of the Evaluate node variables which contains the processed inbound attachment array object.
      - **Timestamp** - (ISO8601 Format in UTC Timezone) - $(n30.send.sentDateTime) for Send nodes and $(n30.messenger.timestamp) for Receive nodes.
    - **Dynamic message(s) JSON**: Pass a variable containing a JSON array. Refer to [Facebook Messenger schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/facebook-messenger-3).
- **Livechat** - If you choose Livechat channel, you will view following settings:
  - **Conversation ID** - **$(n6.conversationId)**.  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables.
  - **Messages**- Select a radio button Single or Dynamic message.
    - **Single Message**: If you select Single Message radio button, you will view the following settings:
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type**: Choose a message type from the drop-down list:
        - ** Text with attachments**: If you select this option, you will view the following fields: 
          - **Text** - In general the value is set to Custom Variable for Send nodes or $(n30.inappmessaging.message) from Receive nodes.
          - **Attachments** - In general the value is set to **$(parseDataAttachment)** in templated flows.  
            This is one of the Evaluate node variables which contains the processed inbound attachment array object.
        - **Livechat Text with carousel**
          - **Text** - In general the value is set to Custom Variable for Send nodes or $(n30.inappmessaging.message) from Receive nodes.
          - **Livechat Carousel Object** - JSON or Flow variable.  
            Pick up from the Send node output variables.
        - **Livechat Text with quick replies**
          - **Text** - In general the value is set to Custom Variable for Send nodes or $(n30.inappmessaging.message) from Receive nodes.
          - **Quick Replies Object** - JSON or Flow variable  
            Pick up from the Send node output variables
        - **Form Response**  
          **Livechat Form Response** - JSON or Flow variable.  
          Pick up from the Receive node output variables.
        - **Livechat Carousel Response** - JSON or Flow variable.  
          Pick up from the Receive node output variables.
        - **Livechat Quick Replies Response** - JSON or Flow variable.  
          Pick up from the Receive node output variables
      - **Dynamic message (JSON)**: Pass a variable containing a JSON array. Refer to [Livechat schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/livechat-1).
    - **Timestamp **(IN UTC) - $(n2.messenger.ts).  
      (ISO8601 Format in UTC Timezone) - $(n30.send.sentDateTime) for Send nodes and $(n30.inappmessaging.timestamp) for Receive nodes.
- **Email** - If you choose Email channel, you will view following settings:
  - **Conversation ID** - **$(n6.conversationId)**.  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables.
  - **Messages**- Select a radio button Single or Dynamic message.
    - **Single Message**: If you select Single Message radio button, you will view the following settings:
      - **Message Alias ID** - In general the value is set to** $(n2.email.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type** - Set to email.
      - **From Address** - In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **To address** -  In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **CC Recipients** - In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
    - **Email message**: Configure the following settings:
      - **Email headers** - In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **HTML email body** -  In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **Plain email body** - In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **Stripped HTML** -  In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **Stripped text** - In general the value is set to **$(n2.email.strippedText)**.  
        In general the value is set to Custom Variable for Send nodes or $(n30.email.emailId) from Receive nodes.
      - **Attachments** -  In general the value is set to **$(parseDataAttachment)**.  
        This Evaluate note variable contains the processed array object of incoming attachments from the customer.
    - **Dynamic message (JSON)**: Pass a variable containing a JSON array. Refer to [Email schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/email-2).
    - **Timestamp** (IN UTC) - $(n2.messenger.ts).  
      ts in the output variables of the start node which contains the Messenger Timestamp.  
      (ISO8601 Format in UTC Timezone) - $(n30.send.sentDateTime) for Send nodes and $(n30.email.timestamp) for Receive nodes.
- **WhatsApp** - If you choose WhatsApp channel, you will view following settings:
  - **Conversation ID** - **$(n6.conversationId)**.  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables.
    - **Messages**- Select a radio button Single or Dynamic message.
      - **Single Message**: If you select Single Message radio button, you will view the following settings:
        - **Message Alias ID** - In general the value is set to** $(n2.whatsapp.transId)**.  
          Unique auxiliary external reference identifier to maps to the message.
        - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list
        - **Message Type** - Choose a message type from the drop-down list:
          - If you choose text, you will view a Text field:
            - **Text** -  In general the value is set to to Custom Variable for Send nodes or$(n30.whatsapp.message) from Receive nodes.
          - If you choose Text with attachments, you will view the following fields:
            - **Text** -  In general the value is set to to Custom Variable for Send nodes or$(n30.whatsapp.message) from Receive nodes.
            - **Attachments** - In general the value is set to **$(parseDataAttachment)**.  
              This is one of the Evaluate node variables which contains the processed inbound attachment array object.
          - If you choose WhatsApp interactive response, you will view following field:
            - **WhatsApp Interactive Response** - JSON or variable.  
              Construct a JSON as per the payload mentioned below.
              - ```json Inbound WhatsApp Interactive Response
                {
                  "title": "Option 1",
                  "identifier": "b0c75e59-3196-442d-9de5-bafaaa83b402"
                } 
                ```

> 📘 $(n30.send.response_interactive) variable for WhatsApp Rich Messages
> 
> The $(n30.send.response_interactive) variable is currently unsupported for WhatsApp Rich Messages, including WhatsApp Buttons and WhatsApp Lists, and should not be used in these flows. To ensure proper functionality, developers must instead construct a custom JSON payload that adheres to the established schema requirements which are mentioned below.

- **WhatsApp List** - In general the value is set to **$(n30.send.response_interactive)**.  
  response_interactive from the output variables of the Send node is WhatsApp List. Refer to the schema below:
  - ```json Outbound WhatsApp List
    {
      "header": {
        "type": "text",
        "text": "your text"
      },
      "body": {
        "text": "your-text-body-content"
      },
      "footer": {
        "text": "your-text-footer-content"
      },
      "action": {
        "button": "cta-button-content",
        "sections": [
          {
            "title": "section-title-content",
            "rows": [
              {
                "id": "unique-row-identifier",
                "title": "row-title-content",
                "description": "row-description-content"
              }
            ]
          },
          {
            "title": "section-title-content",
            "rows": [
              {
                "id": "unique-row-identifier",
                "title": "row-title-content",
                "description": "row-description-content"
              }
            ]
          }
        ]
      }
    }  
    ```
    <br />
- **WhatsApp Buttons** - In general the value is set to **$(n2.send.response_interactive)**.  
     response_interactive from the output variables of the Send node is WhatsApp Buttons. Refer to the schema below:
- ```json Outbound WhatsApp Buttons
    {
      "header": {
        "type": "text",
        "text": "your text",
        "document": {
          "url": "your-media-url",
          "filename": "some-file-name"
        },
        "video": {
          "url": "your-media-url"
        },
        "image": {
          "url": "your-media-url"
        }
      },
      "body": {
        "text": "your-text-body-content"
      },
      "footer": {
        "text": "your-text-footer-content"
      },
      "action": {
        "buttons": [
          {
            "type": "reply",
            "reply": {
              "id": "unique-postback-id",
              "title": "First Button’s Title"
            }
          },
          {
            "type": "reply",
            "reply": {
              "id": "unique-postback-id",
              "title": "Second Button’s Title"
            }
          }
        ]
      }
    }  
  ```
  <br />

**Apple Messages for Business (AMB)** - If you choose AMB channel, you will view following settings:

- - **Conversation ID** - **$(n6.conversationId)**.  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables. 
  - **Messages**- Select a radio button Single or Dynamic message.
    - **Single Message**: If you select Single Message radio button, you will view the following settings:
      - **Message Alias ID** - In general the value is set to ** $(n2.abc.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list
        - **Message Type** - Choose a message type from the drop-down list:
          - **Text with Attachments** -  If you choose Text with attachments, you will view the following fields:
            - **Text** - In general the value is set to Custom Variable for Send nodes or$(n30.abc.message) from Receive nodes.
            - **Attachments** - In general the value is set to **$(parseDataAttachment)** in templated flows.  
              This is one of the Evaluate node variables which contains the processed inbound attachment array object.
          - **AMB List picker response** -If you choose AMB list picker response, enter JSON or Flow variable.  
            Construct payload as per [AMB Schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/apple-messages-for-business-3).
          - **AMB Time picker response** - If you choose AMB time picker response, enter JSON or Flow variable.  
            Construct payload as per [AMB Schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/apple-messages-for-business-3).
          - **AMB Form response** - If you choose AMB form response, enter JSON or Flow variable.  
            Construct payload as per [AMB Schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/apple-messages-for-business-3).
          - **AMB Quick replies response** -If you choose AMB list quick replies response, enter JSON or Flow variable..  
            Construct payload as per [AMB Schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/apple-messages-for-business-3).
  - **AMB List picker** - In general value is set to **$(n30.send.listPicker)**.  
    Pick up from the Output variables of an AMB send node.
  - **AMB Time picker** - In general value is set to **$(n30.send.timePicker)**.  
    Pick up from the Output variables of an AMB send node.
  - **AMB Form** -  In general value is set to **$(n30.send.response_interactive)**.  
    Pick up from the Output variables of an AMB send nodeAMB Quick replies.
  - **AMB Quick replies** - In general value is set to **$(n30.send.quickReplies)**.  
    Pick up from the Receive node output variables.
  - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer to [AMB schema](https://dash.readme.com/project/imiconnect1/v6.7.0/docs/apple-messages-for-business-3).
  - **Timestamp** - (ISO8601 Format in UTC Timezone) - $(n30.send.sentDateTime) for Send nodes and $(n30.abc.timestamp) for Receive nodes.
  - **AMB Capability List **- In general the value is set to $(n2.abc.capabilityList).  
    Determines the supported message types that the customer's device supports.
- **API** - If you choose API channel, you will view following settings:
  - **Conversation ID** - **$(n6.conversationId)**.  
    Conversation ID is obtained upstream from the Create conversation or Search conversation node's output variables.
  - **Single Message**: If you select Single Message radio button, you will view the following settings:
    - **Message Alias ID** - Custom Variable.  
      Unique auxiliary external reference identifier to maps to the message.
    - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
    - **Message Type** - Choose a message type from the drop-down list:
      - **Text** -  In general the value is set to Custom Variable for Send nodes and corresponding variables from Receive nodes.
      - **Text with attachments** - If you choose, text with attachments, you will view following fields:
        - **Text** - In general the value is set to Custom Variable for Send nodes and corresponding variables from Receive nodes.
        - **Attachments** -  In general the value is set to $(parseDataAttachment).  
          This is one of the Evaluate node variables which contains the processed incoming attachment array object from the customer respectively.
  - **Timestamp** - (ISO8601 Format in UTC Timezone) - In general the value is set to Custom Variable for Send nodes and corresponding variables from Receive nodes.

## Output variables

| Variable | Description                                   |
| :------- | :-------------------------------------------- |
| transId  | API request identifier generated by WxEngage. |

## Node outcomes

| Category | Outcome                | Description                                                                                                                                                                                                                |
| :------- | :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success  | onAppendMessageSuccess | Message appended to WxEngage's conversation object successfully                                                                                                                                                            |
| Errors   | onAppendMessageFailure | WxEngage failed to append the message to the conversation                                                                                                                                                                  |
|          | onTimeout              | Could not receive an API response from WxEngage within the agreed time-out                                                                                                                                                 |
|          | onInvalidData          | Invalid data configured in WxConnect node                                                                                                                                                                                  |
|          | onError                | Error in WxConnect's middleware services                                                                                                                                                                                   |
|          | onInvalidChoice        | Invalid choice                                                                                                                                                                                                             |
|          | onauthorizationfail    | Failed to Authorize successfully. We recommend you to recheck your Node Authorization configurations in the [Authorize Integration](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) section |
|          | Failure                | Any other run time failures                                                                                                                                                                                                |