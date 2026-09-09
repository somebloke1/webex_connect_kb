> 📘 Please Note
> 
> The Email channel is supported via <<prodname>> Send Message API v2.
> 
> The API endpoint for it is: [https://{YourRegion}.webexconnect.io/v2/messages].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying various types of email notifications supported by <<prodname>>.

## Request Body for Email

```json Send Text Email
{
    "channel": "email", //Mandatory. channel used for messaging.
    "from": "{{fromEmailAddress}}", //Mandatory. Email id of the sender.
    "to": [
        {
            "email": [
                "{{toEmailAddress}}"
            ], //Mandatory. email id of the recipients
            "substitutions": { //Optional. 
                "{{param1}}": "{{param1Value}}",
                "{{param2}}": "{{param2Value}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. 
        "{{param3}}": "{{param3Value}}",
        "{{param4}}": "{{param4Value}}"
    },
    "cc": [], //Optional. Email id of the copied recipients.
    "bcc": [], //Optional. Email id of the bcc recipients.
    "multipleToRecipients": true, //Optional. If this parameter is not included then the same email is sent individually to each of the email addresses specified in 'to' field including all cc and bcc email ids.
    "options": { //Optional.
        "fromName": "{{emailSendername}}", //Optional. A string that will appear next to the from address in most email inboxes
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "content": {
        "type": "text", //Mandatory. Either text or html. Use text while sending text emails.
        "subject": "{{subject}}", //Mandatory. Subject of the email
        "replyTo": "{{replyToEmailAddress}}", //Optional. Reply path for the email when the customer responds
        "text": "Simple text content" //Mandatory. Text content of the email
    },
    "requestedReceipts": [ //Optional.
        "submitted",
        "delivered",
        "bounce",
        "not verified",
        "invalid",
        "complaint",
        "failed"
    ], //JSON array that can filter message delivery web-hooks to the notifyURL. Can contain one or more of the following: "submitted", "delivered", "not verified", "invalid", "bounced", "complaint", "read", "clicked", "failed". Check Outbound Webhooks for more information on receipts. Note: All the above receipts are relevant for email via AWS SES. For email via SMTP, only "submitted" receipt is applicable
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional. Provide a URL to get notifications on message delivery status. Use requestedReceipts block to specify list of messages status you want to track.
    "notifyUrlAuthId":"TNPXXXT09U", //Optional
    "contactPolicy": { //Optional. 
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

## Send Message API v2 for Email channel - Common Body Parameters

The following are the parameters of the request body:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "channel",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "The value must be 'email' when sending an email.",
    "1-0": "from",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "Email ID, i.e., the email ID of the sender to be used for sending the email.",
    "2-0": "to",
    "2-1": "JSONArray",
    "2-2": "yes",
    "2-3": "An array of \"to\" JSON objects that contain the mandatory email ID of the recipients and optional personalised substitutions for each \"to\" object.",
    "3-0": "email",
    "3-1": "JSONArray",
    "3-2": "yes",
    "3-3": "Email ID of the recipients.",
    "4-0": "substitutions",
    "4-1": "JSONObject",
    "4-2": "no",
    "4-3": "List of key-value pairs for dynamic fields in the Email content. They are typically used for specifying the values of dynamic fields in an email template.  \n  \nThere are two ways to define the 'substitutions' parameter, one inside the 'to' block and another outside the 'to' block.  \n  \nThe 'substitutions' parameter inside the 'to' block takes precedence over the 'substitutions' block that is outside the 'to' block, in case these values are provided in both places. ",
    "5-0": "correlationId",
    "5-1": "string",
    "5-2": "no",
    "5-3": "User defined ID that is assigned to an individual message for unique identification.",
    "6-0": "cc",
    "6-1": "JSONArray",
    "6-2": "no",
    "6-3": "Email ID of the copied recipients.",
    "7-0": "bcc",
    "7-1": "JSONArray",
    "7-2": "no",
    "7-3": "Email ID of the BCC recipients.",
    "8-0": "multipleToRecipients",
    "8-1": "boolean",
    "8-2": "no",
    "8-3": "_ When this option is set to true, the platform sends a single email to multiple recipients in the 'to' field list.  \n_ When the option is set to false, the platform sends separate emails to multiple recipients in the 'to' field list.",
    "9-0": "options",
    "9-1": "JSONObject",
    "9-2": "no",
    "9-3": "A JSON object that contains additional, email-specific options such as 'fromName', 'trackClicks', and 'trackOpens' in the API. ",
    "10-0": "fromName",
    "10-1": "string",
    "10-2": "no",
    "10-3": "A string that will appear next to the 'from' address in most email inboxes.",
    "11-0": "trackClicks",
    "11-1": "boolean",
    "11-2": "no",
    "11-3": "When enabled, this option tracks all links in the HTML body, unless a link is tagged as _no-track-connect_ within the anchor tags.",
    "12-0": "shortenLinks",
    "12-1": "boolean",
    "12-2": "np",
    "12-3": "When enabled, this shortens any HTTPS links in the message request's body. The expiry of the shortened URL is 180 days.",
    "13-0": "domain",
    "13-1": "string",
    "13-2": "no",
    "13-3": "It is the domain configuration for shortening the links.  \nNote: 'domain' is mandatory only when 'options' object is used in the payload.",
    "14-0": "tags",
    "14-1": "string",
    "14-2": "yes",
    "14-3": "Reporting tags for tracking the shortened link creates and clicks.",
    "15-0": "allowFallbackUR",
    "15-1": "",
    "15-2": "yes",
    "15-3": "if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.",
    "16-0": "trackOpens",
    "16-1": "boolean",
    "16-2": "no",
    "16-3": "When enabled, this option tracks when the email is opened by the recipient of the email.",
    "17-0": "listUnsubscribeUrl",
    "17-1": "string",
    "17-2": "no",
    "17-3": "Allows you to pass the link to your own subscription management portal, as part of the list-unsubscribe headers, instead of using Webex Connect subscription management capability.",
    "18-0": "unsubscribeEmailAddress",
    "18-1": "string",
    "18-2": "no",
    "18-3": "Contains the email address to which the unsubscribe email will be sent, when the customer sends unsubscribe request via mail to unsubscribe route.",
    "19-0": "unsubscribeEmailSubject",
    "19-1": "string",
    "19-2": "no",
    "19-3": "Specify the subject that you would like to use for the email unsubscribe requests triggered via mail to unsubscribe route.",
    "20-0": "content",
    "20-1": "JSONObject",
    "20-2": "yes, if the template is not provided",
    "20-3": "It is the JSON object that contains mandatory parameters 'type', 'encoding', 'subject', 'replyTo', and 'text' for the email channel.",
    "21-0": "type",
    "21-1": "string",
    "21-2": "yes",
    "21-3": "Used for specifying the message content type. The acceptable values are Text or HTML.",
    "22-0": "subject",
    "22-1": "string",
    "22-2": "yes",
    "22-3": "Subject of the email.",
    "23-0": "replyTo",
    "23-1": "string",
    "23-2": "no",
    "23-3": "An email header that allows recipients to reply to a different email address than the one used to send the original message.",
    "24-0": "text",
    "24-1": "string",
    "24-2": "yes, when type=text  \noptional, when type=html",
    "24-3": "Text content of the email.",
    "25-0": "requestedReceipts",
    "25-1": "JSONArray",
    "25-2": "no",
    "25-3": "A JSON array that can filter message delivery webhooks to the notifyUrl.  \n  \nIt can contain one or more of the following:  \n\"submitted\",  \n\"delivered\",  \n\"read\",  \n\"clicked\",  \n\"bounce\",  \n\"not verified\",  \n\"invalid\",  \n\"complaint\",  \n\"failed\"  \n  \nCheck [Outbound Webhooks](https://developers.webexconnect.io/reference/outbound-webhooks) for delivery receipt samples.",
    "26-0": "callbackData",
    "26-1": "string",
    "26-2": "no",
    "26-3": "A string that is returned with each outbound webhook for the message (delivery, failed, etc.). The maximum number of characters allowed for callbackData including any spaces, is 2000.",
    "27-0": "notifyUrl",
    "27-1": "string",
    "27-2": "no",
    "27-3": "If provided, updates related to the delivery status of this message will be posted to this URL. Refer to the [Email](https://developers.webexconnect.io/reference/email-outbound-webhooks) section for notification samples.",
    "28-0": "notifyUrlAuthId",
    "28-1": "string",
    "28-2": "no",
    "28-3": "Unique Authentication ID.",
    "29-0": "contactPolicy",
    "29-1": "JSONObject",
    "29-2": "no",
    "29-3": "JSON Object to specify Contact Policy checks before sending the outbound email. The Contact Policy App should be configured as a prerequisite to be able to use this feature.",
    "30-0": "contactPolicyGroup",
    "30-1": "string",
    "30-2": "yes (if you want to apply Contact Policy checks before sending the message)",
    "30-3": "The GroupID is to be applied. It is required if any of the options below are included and set to true.",
    "31-0": "channelCheckConsent",
    "31-1": "boolean",
    "31-2": "no",
    "31-3": "Optional, assumed false if not specified. Set to true to require 'Opt-In' before sending the message. At least one out of “channelCheckConsent”, or “channelApplyFrequencyCap” parameters, should be set to “true”.",
    "32-0": "channelApplyFrequencyCap",
    "32-1": "boolean",
    "32-2": "no",
    "32-3": "Optional, assumed false. Set to true to enforce group frequency cap for that channel. At least one out of “channelCheckConsent”, or “channelApplyFrequencyCap” parameter, should be set to “true”."
  },
  "cols": 4,
  "rows": 33,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

> 📘 Multiple 'To' Recipients
> 
> - You have the ability to send emails to multiple ‘To’ recipients in a single email transaction using Messaging API v2. This would require you to pass an additional parameter ‘multipleToRecipients’ to be passed as part of the request with its value set to ‘true’. When multiple email IDs are mentioned in the “Email” parameter of the “To” block, Webex Connect submits a single request to AWS SES or to SMTP server to send the concerned email to all - To, CC, and BCC. In this case, the API response will contain only one transaction ID for all recipients. Refer API reference for more information.
> - When Webex Connect is used to send emails to multiple email recipients (To, CC, BCC), the message submitted count reflects the total number of emails sent (counting each of the recipient in To, CC, and BCC fields individually). These changes will reflect in the ‘Reports’ and in the ‘Usage’ sections for email transactions.
> - For email transactions with multiple recipients, the Status field in Debug Console and Export Logs, and Error Codes details, will only be updated for entries with the ‘Submitted’ Status. Email delivery status for each of the individual recipients will need to be tracked using Outbound Webhooks. Separate outbound notifications will be sent for email delivery or failure to each of the recipients mentioned in To, CC, and BCC sections with the same transaction ID. For outbound email transactions, destination will contain an email ID for scenarios where only one email ID has been mentioned (that can in be in either of to, bcc, or cc fields but overall one email ID is mentioned in one outbound request).  
>   Read receipts are not generated for emails sent as plain text, i.e., when the email type is text.

> 📘 List Unsubscribe Parameters
> 
> There is an option to pass list-unsubscribe headers when sending emails using Webex Connect Messaging API v2. This will allow you to pass the links to your own unsubscribe management portal as part of the list-unsubscribe headers instead of using Webex Connectunsubscribe management capability. The following headers can be passed:
> 
> - listUnsubscribeUrl
> - unsubscribeEmailAddress
> - unsubscribeEmailSubject
> 
> When the list-unsubscribe URL and/or unsubscribe mailto address are added, the Webex Connect platform will overwrite the asset setting with the values provided in the Messaging API, even for the assets for which the platform manages unsubscriptions. In such cases, the Webex Connect platform will no longer have control over the Outbound Webhook notifications for the unsubscribe events originated from the list-unsubscribe header. Therefore, you are recommended to use these options only when you have a mechanism to handle unsubscriptions (including one-click unsubscription) on your own.
> 
> Since it’s an email compliance requirement, the one-click unsubscribe header will be added to the outbound email, every time the list-unsubscribe URL is added in the Messaging API. You are expected to handle one-click unsubscriptions, i.e., receive postback from the email clients, perform action (add user email address to unsubscribe list), and respond with appropriate success status.

## Examples

### Send HTML Email

```json Send HTML Email
{
    "channel": "email", //Mandatory. channel used for messaging.
    "from": "{{fromEmailAddress}}", //Mandatory. Email id of the sender.
    "to": [
        {
            "email": [
                "{{toEmailAddress}}"
            ], //Mandatory. email id of the recipients
            "substitutions": { //Optional.
                "{{param1}}": "{{param1Value}}",
                "{{param2}}": "{{param2Value}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional.
        "{{param3}}": "{{param3Value}}",
        "{{param4}}": "{{param4Value}}"
    },
    "cc": [], //Optional. Email id of the copied recipients.
    "bcc": [], //Optional. Email id of the bcc recipients.
    "options": { //Optional.
        "fromName": "{{emailSendername}}", //Optional. A string that will appear next to the from address in most email inboxes
        "trackClicks": true, //Optional. When enabled, this tracks all links in the HTML body unless a link is tagged as no-track-connect within the anchor tags. Link tracking is supported only for Email app assets configured using AWS SES.
        "trackOpens": true, //Optional. When enabled, this tracks opens of the email. Open tracking is supported only for Email app assets configured using AWS SES. 
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "content": {
        "type": "html", //Mandatory. Either text or html. Use html while sending html emails.
        "subject": "{{subject}}", //Mandatory. Subject of the email
        "replyTo": "{{replyToEmailAddress}}", //Optional. Reply path for the email when the customer responds
        "text": "Fallback text in the event the email client does not support HTML emails", //Optional. Text content of the email
        "html": "<a track_enable href=\"http://example.com\">link text</a><footer><a data-mce-href='$(unsubscribe)' href='$(unsubscribe)' target='_blank' rel='noopener'><span st-unsubscribe='' style='text-decoration: none; color: #0088cc;' data-mce-style='text-decoration: none; color: #0088cc;'>unsubscribe</span></a></footer>" //Mandatory. Raw HTML for the email. Up to 350 kbps in size.
    },
    "requestedReceipts": [ //Optional.
        "submitted",
        "delivered",
        "read",
        "clicked",
        "bounce",
        "not verified",
        "invalid",
        "complaint",
        "failed"
    ], //JSON array that can filter message delivery web-hooks to the notifyURL. Can contain one or more of the following: "submitted", "delivered", "not verified", "invalid", "bounced", "complaint", "read", "clicked", "failed". Check Outbound Webhooks for more information on receipts. Note: All the above receipts are relevant for email via AWS SES. For email via SMTP, only "submitted" receipt is applicable
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional. Provide a URL to get notifications on message delivery status. Use requestedReceipts block to specify list of messages status you want to track.
    "notifyUrlAuthId":"TNPXXXT09U", //Optional
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

#### **Parameter table with parameters unique to HTML Email type**

| Parameter | Type   | Mandatory              | Description                                                                                    |
| :-------- | :----- | :--------------------- | :--------------------------------------------------------------------------------------------- |
| type      | string | yes                    | Possible options are 'text' or 'html'. In this case, it is 'html' while sending 'html' emails. |
| html      | string | yes, when type is HTML | Raw 'html' for the email. Up to 500 KB in size.                                                |

> 📘 Email Size Limitations
> 
> The default email size limit for AWS SES based email assets in <<prodname>> is 10 MB. This is the overall email size limit including (the email text, images, attachments, and the MIME encoding). Please note that the size increases post MIME encoding. If you attach a 5 MB file in your email, the attachment size after MIME encoding will be ~6.85MB (about 137% of the original file size).

### Send Email with Attachments

```json SendEmailwithAttachments
{
    "channel": "email", //Mandatory. channel used for messaging.
    "from": "{{fromEmailAddress}}", //Mandatory. Email id of the sender.
    "to": [
        {
            "email": [
                "{{toEmailAddress}}"
            ], //Mandatory. email id of the recipients
            "substitutions": { //Optional.
                "{{param1}}": "{{param1Value}}",
                "{{param2}}": "{{param2Value}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional.
        "{{param3}}": "{{param3Value}}",
        "{{param4}}": "{{param4Value}}"
    },
    "options": { //Optional.
        "fromName": "{{emailSendername}}", //Optional. A string that will appear next to the from address in most email inboxes
        "trackClicks": true, //Optional. When enabled, this tracks all links in the HTML body unless a link is tagged as no-track-connect within the anchor tags. Link tracking is supported only for Email app assets configured using AWS SES.
        "trackOpens": true, //Optional. When enabled, this tracks opens of the email. Open tracking is supported only for Email app assets configured using AWS SES. 
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "content": {
        "type": "html", //Mandatory. Either text or html.
        "subject": "{{subject}}", //Mandatory. Subject of the email
        "text": "Fallback text in the event the email client does not support HTML emails", //Text content of the email Note:yes, when type=text optional, when type=html
        "attachments": [
            {
                "mimetype": "image/png", //Mandatory. Supported mimeTpes
                "name": "Flower", //Mandatory. Name of the attachments
                "mediaUrl": "" //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format.
            }
        ]
    },
    "requestedReceipts": [ //Optional.
        "submitted",
        "delivered",
        "read",
        "clicked",
        "bounce",
        "not verified",
        "invalid",
        "complaint",
        "failed"
    ], //JSON array that can filter message delivery web-hooks to the notifyURL. Can contain one or more of the following: "submitted", "delivered", "not verified", "invalid", "bounced", "complaint", "read", "clicked", "failed". Check Outbound Webhooks for more information on receipts. Note: All the above receipts are relevant for email via AWS SES. For email via SMTP, only "submitted" receipt is applicable
     "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
     "notifyUrl": "", //Optional. Provide a URL to get notifications on message delivery status. Use requestedReceipts block to specify list of messages status you want to track.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
} 
```
```json Send Email with Inline Images
{
    "channel": "email", //Mandatory. channel used for messaging.
    "from": "{{fromEmailAddress}}", //Mandatory. Email id of the sender.
    "to": [
        {
            "email": [
                "{{toEmailAddress}}"
            ], //Mandatory. email id of the recipients
            "substitutions": { //Optional. 
                "{{param1}}": "{{param1Value}}",
                "{{param2}}": "{{param2Value}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional. 
        "{{param3}}": "{{param3Value}}",
        "{{param4}}": "{{param4Value}}"
    },
    "cc": [], //Optional. Email id of the copied recipients.
    "bcc": [], //Optional. Email id of the bcc recipients.
    "multipleToRecipients": true, //Optional. If this parameter is not included then the same email is sent individually to each of the email addresses specified in 'to' field including all cc and bcc email ids.
    "options": { //Optional.
        "fromName": "{{emailSendername}}", //Optional. A string that will appear next to the from address in most email inboxes
        "shortenLinks": "true",
        "domain": "https://s.imiconnect.co",
        "tag1": "tag1", // reporting tags for tracking the  shortened link creates and clicks
        "tag2": "tag2",
        "allowFallbackURL": "false" // if true, the long URL passed will be sent in case the SLS service is down or fails to create the shortened link.
    },
    "content": {
        "type": "html", //Mandatory. Either text or html. Use html while sending html emails.
        "subject": "{{subject}}", //Mandatory. Subject of the email
        "replyTo": "{{replyToEmailAddress}}", //Optional. Reply path for the email when the customer responds
        "text": "Fallback text in the event the email client does not support HTML emails", //Optional. Text content of the email
        "html": "<body> <h2>Thanks for placing order with us</h2> <p>Please find the confirmation of your order below</p> <img src=\"cid:orderconf\" alt=\"order confirmation image\" style=\"width:128px;height:128px;\"> </body>", //Mandatory. Raw HTML for the email. Up to 350 kbps in size.
        "attachments": [
            {
                "mimetype": "image/jpg", //Mandatory. Supported mimeTpes
                "name": "order_confirmation", //Mandatory. Name of the attachments
                "mediaUrl": "https://res.cloudinary.com/demo/w_200,h_200,c_fill/order_confirmation.jpg", //Mandatory. Direct URL pointing to the media file. The URL should end with specified file-format.
                "cid": "orderconf" //Optional. Used as inline image reference in the HTML payload
            },
    "requestedReceipts": [ //Optional.
        "submitted",
          "delivered",
          },
			}
```

#### **Parameter table with parameters unique to Email with Attachments**

| Parameter   | Type      | Mandatory | Description                                                                                                                                                                           |
| :---------- | :-------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| attachments | JSONArray | no        | Attachment sizes are subject to the overall email message size limitations according to the parameters as part of the table below.                                                    |
| mimetype    | no        | yes       | Mime type of the attachment that is being sent. For example, "image/png". Refer to [supported file types](https://help.webexconnect.io/docs/supported-file-types-for-channels#email). |
| name        | string    | yes       | Name of the attachment.                                                                                                                                                               |
| mediaUrl    | string    | yes       | Direct URL pointing to the media file.                                                                                                                                                |

### Send Email Using Templates

```json SendEmail-UsingTemplates
{
    "channel": "email", //Mandatory. channel used for messaging.
    "from": "{{fromEmailAddress}}", //Mandatory. Email id of the sender.
    "to": [
        {
            "email": [
                "{{toEmailAddress}}"
            ], //Mandatory. email id of the recipients
            "substitutions": { //Optional.
                "{{param1}}": "{{param1Value}}",
                "{{param2}}": "{{param2Value}}"
            },
            "correlationId": "" //Optional. The CorrelationID is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
        }
    ],
    "substitutions": { //Optional.
        "{{param3}}": "{{param3Value}}",
        "{{param4}}": "{{param4Value}}",
        "{{param5}}": "{{param5Value}}",
        "{{param6}}": "{{param6Value}}"
    },
    "template": {
        "id": "{{templateId}}", //Mandatory. Unique identifier of the email template used for constructing the email
        "subject": "{{subject}}" //Optional. Subject of the email. If mentioned, this subject value takes precedence over that of the 'Template'.
    },
    "requestedReceipts": [ //Optional.
        "submitted",
        "delivered",
        "read",
        "clicked",
        "bounce",
        "not verified",
        "invalid",
        "complaint",
        "failed"
    ], //JSON array that can filter message delivery web-hooks to the notifyURL. Can contain one or more of the following: "submitted", "delivered", "not verified", "invalid", "bounce", "complaint", "read", "clicked", "failed". Check Outbound Webhooks for more information on receipts. Note: All the above receipts are relevant for email via AWS SES. For email via SMTP, only "submitted" receipt is applicable
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
    "notifyUrl": "", //Optional. Provide a URL to get notifications on message delivery status. Use requestedReceipts block to specify list of messages status you want to track.
    "notifyUrlAuthId": "TNPXXXT09U", //Optional.
    "contactPolicy": { //Optional.
        "contactPolicyGroup": "", //the GroupID to be applied. Required if any of the following options are included and set to true
        "channelCheckConsent": true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
        "channelApplyFrequencyCap": true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

#### **Parameter table with parameters unique to Email Using Templates**

| Parameter  | Type       | Mandatory | Description                                                              |
| :--------- | :--------- | :-------- | :----------------------------------------------------------------------- |
| template   | JSONObject | yes       | JSON Object for configuration of the template.                           |
| templateid | string     | yes       | Unique identifier of the email template used for constructing the email. |
| subject    | string     | no        | Subject of the email.                                                    |

## Sample Response Body

```json 201 Result
{
    "requestTimestamp": "2024-09-05T00:03:01.708-04:00",
    "messageId": "a770f205-1234-XXXX-x5x3-6dc3e388b9b5",
    "correlationId": "12345",
    "status": "queued"
}
```
```json 400 Bad Request
   {
        "code": "7000",
        "message": "Invalid JSON"
    }
```
```Text 401 Unauthorised
No response body
```