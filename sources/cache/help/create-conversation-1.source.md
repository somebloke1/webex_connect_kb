When setting up flows in Webex Connect, you may use this node to create a conversation with the customer's channel identity and the business's channel asset. Some channels may need additional context to resolve a message, such as including the subject line in email conversations. This node utilizes the "**Create Conversation**" API to check for existing conversations on Webex Engage. A detailed guide is available in the table below:

| Channel                     | Customer Address (customerAddress) | Business Address (bizAddress) | Additional context                                        |
| :-------------------------- | :--------------------------------- | :---------------------------- | :-------------------------------------------------------- |
| SMS                         | Customer Mobile Number             | Business Longcode             | -                                                         |
| Facebook Messenger          | Page Scoped ID                     | Page ID                       | -                                                         |
| Livechat                    | User ID                            | App ID                        | Thread ID, User ID and Browserfingerprint                 |
| Email                       | Email ID                           | Business Mailbox              | Subject, To Recipients, Cc Recipients, In Reply To Header |
| Apple Messages for Business | AMB User ID                        | AMB Account ID                | -                                                         |
| WhatsApp Business           | WhatsApp Mobile Number             | WhatsApp Business Longcode    | -                                                         |
| API                         | User ID                            | Business ID                   | Business ID can be fetched from New Admin console.        |

## Configuration

To configure a Create conversation node, follow these steps:

1. Drag and drop the **Create conversation** node from the Node palette from the left side of the screen.
2. Double-click the Create conversation node to view the configuration settings.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0014e86f232a657c652611c99f4d1046f644f057377e123106cb98ca2de3eb16-image.png",
        null,
        "Screenshot displaying the Configuration Settings for Create conversation node"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Configuration Settings for Create conversation node"
    }
  ]
}
[/block]


3. Choose **Create conversation** from the Method Name drop-down list.
4. Choose **Authorization** from the Node Authorization drop-down list.  
   We recommend you set Authorization to a Default Authentication configured in [WxEngage's Integrations](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) screen under WxConnect's Integrations. Once you re-authenticate from the Integrations screen, all your nodes across flows will pick up the updated token.
5. Choose a channel from the **Channel** drop-down list.

- **SMS** - If you choose SMS channel, you will view following settings:
  - **Conversation Alias ID** - Enter a Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **Business Longcode / Shortcode** - Choose your Longcode / Shortcode from the Business Longcode / Shortcode drop-down list.
  - **Customer Mobile Number** - In general the value is set to **$(n2.sms.msisdn)**.  
    MSISDN from the output variables of the start node is the customer mobile number.
  - **Customer Name** - The value is null or generally set to a value fetched from external services.  
    To be fetched from external services (if any), else set to null.
  - **Message Type** - Choose Text from the Message Type drop-down list.
    - **None**: Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to **$(n2.messenger.transId)**.  
        A unique auxiliary external reference identifier is used to map the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type** - Choose a message type from the drop-down list:
        - **Text** - $(n2.sms.message)  
          Message from the output variables of the start node is the Text.
  - **Timestamp** - (ISO8601 Format in UTC Timezone) - $(n2.sms.ts)  
    tsin the output variables of the start node which contains the SMS Timestamp.
  - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer to [SMS schema](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/sms-1).
  - **Custom Fields** (Optional)  
    **Scope**: Choose the scope of the field. It can be set to Conversation or Profile(mapped to the customer's 360 degree profile).  
    **Key**: Key of the field.  
    **Value**: Value of the field.
- **Facebook Messenger** - If you choose Facebook Messenger channel, you will view following settings:
  - **Conversation Alias ID** - Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **Page ID** - Choose your Facebook Messenger Page from the Page ID drop-down list.
  - **Scoped ID (PSID)** - **$(n2.messenger.psId)**.  
    PSID from the output variables of the start node is the Facebook PSID.
  - **Customer Name** - $(n2.messenger.name).  
    name from the output variables of the start node is the Customer Name.
  - **Messages(s) (Optional)** - Choose Text from the Message Type drop-down list.
    - **None**: Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to** $(n2.messenger.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type** - Recommended to set to Text with attachments.  
        Choose a message type from the drop-down list:
        - **Text** - $(n2.messenger.message).  
          message from the output variables of the start node is the Text.
        - **Text with attachments** - If you select Text with attachments, you will view following options:
          - **Text** - $(n2.messenger.message).  
            message from the output variables of the start node is the Text.
          - **Attachments** - $(parseDataAttachment).  
            This is one of the Evaluate node variables which contains the processed inbound attachment array object.
    - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer FBM schema [here](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/facebook-messenger-3).
  - **Timestamp** (IN UTC) - $(n2.messenger.ts).  
    ts in the output variables of the start node which contains the Messenger Timestamp.
  - **Custom Fields** (Optional).
    - **Scope**: Choose the scope of the field. It can be set to Conversation or Profile(mapped to the customer's 360 degree profile).
    - **Key**: Key of the field.
    - **Value**: Value of the field.
- **Livechat** - If you choose Livechat channel, you will view following settings:
  - **Conversation Alias ID** - Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **Livechat App** - Choose your App from the Livechat App drop-down list.
  - **Livechat Website Domain** - It is stored under custom variables.  
    Website domain in which the Live Chat widget is embedded. The website domain is available in the app settings page.
  - **Livechat Thread ID** - In general the value is set to **$(n2.inappmessaging.threadId)**.  
      threadId from the output variables of the start node is the Thread ID.
  - **Livechat User ID** -  In general the value is set to **$(n2.inappmessaging.userId)**  
    userId from the output variables of the start node is the Customer Address.
  - **Livechat Browser Fingerprint** - In general the value is set to **$(n2.inappmessaging.userId)**.  
      userId from the output variables of the start node is the Livechat Browser Fingerprint.
  - **Customer Name** - It is fetched from Receive node's Form Response (that accepts Name as one of the Form Fields) or an external system.
  - **Messages(s) (Optional)** - Choose Text from the Message Type drop-down list.
    - **None**: Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to** $(n2.messenger.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type**: Choose a message type from the drop-down list:
        - **Text with Attachments**: If you choose Text with attachments, you will view following settings:
          - **Text** - Generally set to$(n2.inappmessaging.message).  
            message from the output variables of the start node is the Text.
          - **Attachments** - In general the value is set to **$(parseDataAttachment)** in templated flows.  
            This is one of the Evaluate node variables which contains the processed inbound attachment array object.
        - **Livechat Text with carousel**: If you choose Live text with carousel, you will view following fields:
          - **Text** - $(n2.inappmessaging.message).  
            message from the output variables of the Start node is the Text.
          - **Livechat Carousel Object** - JSON or Flow variable  
            Pick up from the Send node output variables
        - **Livechat Text with quick replies**: If you choose Live text with quick replies, you will view following fields:
          - **Text** - $(n2.inappmessaging.message).  
            message from the output variables of the Start node is the Text.
          - **Quick Replies Object** - JSON or Flow variable  
            Pick up from the Send node output variables
        - **Livechat Form Response** - JSON or Flow variable.  
          Pick up from the Receive node output variables.
        - **Livechat Carousel Response** - JSON or Flow variable.  
          Pick up from the Receive node output variables.
        - **Livechat Quick Replies Response** - JSON or Flow variable  
          Pick up from the Receive node output variables
  - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer Livechat schema [here](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/livechat-1).
  - **Timestamp **(IN UTC) - $(n2.messenger.ts)  
    tsin the output variables of the start node which contains the Messenger Timestamp.
  - **Custom Fields** (Optional)  
    **Scope:** Choose the scope of the field. Can be set to Conversation or Profile(mapped to the customer's 360 degree profile)  
    **Key**: Key of the field
- **Email** - If you choose Email channel, you will view following settings:
  - **Conversation Alias ID** - Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **Business Email ID**- Choose your Email ID from the Business Emaild ID drop-down list.
  - **Subject** - In general the value is set to **$(n2.email.subject)**.  
    subject in the output variables of the start node is the Subject.
  - **Customer Email ID** - In general the value is set to **$(n2.email.emailId)**.  
    emailId in the output variables of the start node is Customer Email ID.
  - **Customer Name** - In general the value is set to **$(n2.email.senderName)**.  
    The customer's name may only be occasionally received from inbound emails, depending on the email servers' capabilities.
  - **Messages(s) (Optional)** - Choose Text from the Message Type drop-down list.
    - **None**: Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to** $(n2.email.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type** - Set to email.
      - **From Address** - In general the value is set to **$(n2.email.emailId)**.  
        emailId in the output variables of the start node is From Address.
    - **To address** -  In general the value is set to **$(n2.email.toAddresses)**.  
      toAddresses in the output variables of the start node is the To Address.
    - **Cc Recipients** - In general the value is set to **$(n2.email.ccRecipients)**.  
      ccRecipients in the output variables of the start node is the Cc Recipients.
    - **Email headers** - In general the value is set to **$(n2.email.headers)**.  
      Email headers key-value pairs object obtained from the start node output variables.
    - **HTML email body** - In general the value is set to **$(n2.messenger.htmlBody)**.  
      htmlBody in the output variables of the start node is the HTML email body.
    - **Plain email body** - In general the value is set to **$(n2.email.strippedText)**.  
      strippedText in the output variables of the start node is the HTML email body.
    - **Stripped HTML** -  In general the value is set to **$(n2.email.strippedHtml)**.  
      strippedHtml in the output variables of the start node is the Stripped HTML.
    - **Stripped text** - In general the value is set to **$(n2.email.strippedText)**.  
      strippedText in the output variables of the start node is the Stripped Text.
    - **Attachments** -  In general the value is set to **$(parseDataAttachment)**.  
      This Evaluate note variable contains the processed array object of incoming attachments from the customer.
  - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer Email schema [here](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/email-2).
  - **Timestamp** (IN UTC) - $(n2.messenger.ts).  
    ts in the output variables of the start node which contains the Messenger Timestamp.
  - **Custom Fields** (Optional)  
    **Scope**: Choose the scope of the field. Can be set to Conversation or Profile(mapped to the customer's 360 degree profile).  
    **Key**: Key of the field.  
    **Value**: Value of the field.
- **Apple Messages for Business (AMB)** - If you choose AMB channel, you will view following settings:
  - **Conversation Alias ID** - Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **AMB Account ID**Choose your Account ID from the AMB Account ID drop-down list.
  - **AMB User ID** - In general the value is set to **$(n2.abc.abcUserId**).  
    abc.abcUserId in the output variables of the start node is the AMB User ID.
  - **Customer Name** - In general the value is set to **$(customerName)**.  
    By default, AMB does not provide a customer name. You can set this to a variable that points to a value obtained from external integrations such as CRMs.
  - **Messages(s) (Optional)** - Choose Text from the Message Type drop-down list.
    - **None**: Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to ** $(n2.abc.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type**: Choose a message type from the drop-down list:
      - **Text with Attachments**: If you choose Text with attachment, you will view the following fields:
        - **Text** - Generally set to **$(n2.abc.message)**.  
          message from the output variables of the start node is the Text.
        - **Attachments** - In general the value is set to **$(parseDataAttachment)** in templated flows.  
          This is one of the Evaluate node variables which contains the processed inbound attachment array object.
      - **AMB List picker response** - JSON or Flow variable.  
        Pick up from the Receive node output variables.
      - **AMB Time picker response** - JSON or Flow variable.  
        Pick up from the Receive node output variables.
      - **AMB Form response** - JSON or Flow variable.  
        Pick up from the Receive node output variables.
      - **AMB Quick replies response** - JSON or Flow variable.  
        Pick up from the Receive node output variables.
      - **AMB List picker** - In general value is set to **$(n30.send.listPicker)**.  
        Pick up from the Output variables of an AMB send node.
      - **AMB Time picker** - In general value is set to **$(n30.send.timePicker)**.  
        Pick up from the Output variables of an AMB send node.
      - **AMB Form** -  In general value is set to **$(n30.send.response_interactive)**.  
        Pick up from the Output variables of an AMB send nodeAMB Quick replies.
      - **AMB Quick replies** - In general value is set to **$(n30.send.quickReplies)**.  
        Pick up from the Receive node output variables.
    - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer AMB schema [here](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/apple-messages-for-business-3).
  - **Timestamp** (IN UTC) - In general value is set to **$(n2.abc.ts)**.  
    ts in the output variables of the start node which contains the Timestamp.
  - **AMB Capability List** - In general value is set to **$(n2.abc.capabilityList)**.  
    Determines the message types that the customer's device supports.
  - **Custom Fields** (Optional): Click ADD NEW to add custom fields. You will view the following fields:  
    **Scope**: Choose the scope of the field. Can be set to Conversation or Profile(mapped to the customer's 360 degree profile).  
    **Key**: Key of the field.  
    **Value**: Value of the field.
- **WhatsApp** - If you choose WhatsApp channel, you will view following settings:
  - **Conversation Alias ID** - Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **WhatsApp Longcode** - Choose your Longcode from the WhatsApp Longcode drop-down lis.
  - **WhatsApp Mobile Number** - In general the value is set to **$(n2.whatsapp.waId)**.  
    waId in the output variables of the start node is the subject.
  - **Customer Name** - $(n2.whatsapp.username)  
    name from the output variables of the start node is the Customer Name.
  - **Messages(s) (Optional)** - Choose Text from the Message Type drop-down list.
    - **None**: Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to** $(n2.whatsapp.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
        - **Message Type**: Choose a message type from the drop-down list:
          - **Text** -  In general the value is set to **$(n2.whatsapp.message)**.  
            message from the output variables of the start node is the Text.
          - **Text with attachments**: If you choose Text with attachments, you will view the following fields:
            - **Text** -  In general the value is set to **$(n2.whatsapp.message)**.  
              message from the output variables of the start node is the Text.
            - **Attachments** - In general the value is set to **$(parseDataAttachment)**.  
              This is one of the Evaluate node variables which contains the processed inbound attachment array object.
          - **WhatsApp Interactive Response** - JSON or variable.  
            Construct a JSON as per the payload mentioned in the WAB schema page.
    - **WhatsApp List** - In general the value is set to **$(n30.send.response_interactive)**.  
      response_interactive from the output variables of the Send node is WhatsApp List.
    - **WhatsApp Buttons** - In general the value is set to **$(n2.send.response_interactive)**.  
      response_interactive from the output variables of the Send node is WhatsApp Buttons.
  - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer WhatsApp schema [here](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/api).
  - **Timestamp (IN UTC)** - **$(n2.whatsapp.ts)**.  
    ts in the output variables of the start node which contains the WhatsApp Timestamp.
  - **Custom Fields** (Optional): Click ADD NEW to add custom fields. You will view the following fields:  
    **Scope**: Choose the scope of the field. Can be set to Conversation or Profile(mapped to the customer's 360 degree profile).  
    **Key**: Key of the field.  
    **Value**: Value of the field.
- **API** - If you choose API channel, you will view following settings:
  - **Conversation Alias ID** - Unique Auxiliary reference identifier that you would like to associate to the Conversation ID.
  - **Business ID** - Choose your ID from the  Business ID drop-down list.
  - **User ID** - Custom variable.  
    Unique identifier of the customer as per the channel in context.
  - **Customer Name** - **$(n2.whatsapp.username)**.  
    name from the output variables of the start node is the Customer Name.
  - **Messages(s) (Optional)** - Choose Text from the Message Type drop-down list.
    - **None** - Creates a blank conversation without any messages.
    - **Single Message**: If you choose single message, you will view following settings:
      - **Message Alias ID** - In general the value is set to **$(n2.whatsapp.transId)**.  
        Unique auxiliary external reference identifier to maps to the message.
      - **Direction** - Choose the direction (Inbound or Outbound or Announcement) of the message from the Direction drop-down list.
      - **Message Type** -  Choose a message type from the drop-down list.
        - **Text** - $(n2.whatsapp.message).  
          message from the output variables of the start node is the Text.
        - **Text with Attachments** - If you choose Text with attachments, you will view following fields:
          - **Text** - $(n2.whatsapp.message).  
            message from the output variables of the start node is the Text.
          - **Attachments** - $(parseDataAttachment).  
            This is one of the Evaluate node variables which contains the processed incoming attachment array object from the customer respectively.
  - **Timestamp** (IN UTC) - Custom Timestamp Variable.  
    ISO8601 format of the timestamp.
  - **Dynamic Multi-message(s) JSON array**: Pass a variable containing a JSON array. Refer API schema [here](https://dash.readme.com/project/imiconnect1/v6.7.0/docs/api).

## Output variables

| Variable | Description                                   |
| :------- | :-------------------------------------------- |
| transId  | API request identifier generated by WxEngage. |

> 📘 Note:
> 
> Although the output variables do not display the conversation ID created, you can use this value later in the flow with the variable $(conversation).

## Node outcomes

| Category | Outcome               | Description                                                                                                                                                                                                                |
| :------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success  | onConversationCreated | Conversation created successfully                                                                                                                                                                                          |
| Errors   | onConversationFailed  | WxEngage failed to create a conversation                                                                                                                                                                                   |
|          | onTimeout             | Could not receive an API response from WxEngage within the agreed time-out                                                                                                                                                 |
|          | onInvalidData         | Invalid data configured in WxConnect node                                                                                                                                                                                  |
|          | onError               | Error in WxConnect's middleware services                                                                                                                                                                                   |
|          | onInvalidChoice       | Invalid choice                                                                                                                                                                                                             |
|          | onauthorizationfail   | Failed to Authorize successfully. We recommend you to recheck your Node Authorization configurations in the [Authorize Integration](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) section |
|          | Failure               | Any other run time failures                                                                                                                                                                                                |