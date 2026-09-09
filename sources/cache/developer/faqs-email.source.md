[block:callout]
{
  "type": "info",
  "body": "The below FAQs apply to Email App assets that use AWS SES configuration option on Webex Connect for sending and receiving emails."
}
[/block]

[block:api-header]
{
  "title": "Does the platform suppress outbound emails sent to email addresses that have previously hard bounced?"
}
[/block]
Yes, by default <<prodname>> suppresses outbound emails sent to email addresses that have hard bounced in the last 7 days. If needed, the retention period can be changed to any value between 1 to 365 days by sending an email to the support team. The retention period is common for all email app assets configured in your account.
[block:api-header]
{
  "title": "Maximum number of recipients per message when using AWS SES"
}
[/block]
You can send an email to a maximum of 50 recipients in one request when using AWS SES. This includes email addresses mentioned in either of TO, CC, or BCC fields. If you send an email to more than 50 recipients in one request, it will fail. Emails will not be sent to any of the recipients, and the request will fail citing *'Recipient count exceeds 50'* error.
[block:api-header]
{
  "title": "TLS Policy configurations for sending emails"
}
[/block]
Amazon SES uses opportunistic TLS by default. This means that Amazon SES always attempts to make a secure connection to the receiving mail server. If Amazon SES can't establish a secure connection, it sends the message unencrypted. This behavior can be changed by using configuration sets. If you want to set TlsPolicy property set to 'Require' in the Amazon SES account provided by <<Webex Connect>> team for your tenant, you can place a request by reaching out to the support team.
[block:api-header]
{
  "title": "Is there a way to track delayed email deliveries when using AWS SES with Webex Connect?"
}
[/block]
Currently, <<Webex Connect>> doesn't provide an option to track email delivery delays due to temporary issues (for example, if the recipient’s inbox was full, or if there was a temporary problem with the receiving email server). However, outbound notifications are sent in case of bounces.
[block:api-header]
{
  "title": "Does Webex Connect provide the option to track email delivery and read receipts for Email addresses in CC and BCC fields?"
}
[/block]
No, we do not provide the ability to track email delivery status when you send emails to CC and BCC recipients in addition to a primary To recipient. This is currently a limitation at AWS SES level. We recommend you to send emails to a single recipient, rather than sending a single message to multiple recipients in case you want to track delivery status at an individual email level.
[block:api-header]
{
  "title": "How does Webex Connect handle multiple recipients' scenario?"
}
[/block]
You have the ability to send emails to multiple ‘To’ recipients in a single email transaction using Messaging API v2. This would require you to pass an additional parameter ‘multipleToRecipients’ to be passed as part of the request with its value set to ‘true’. Refer API reference for more information. When multiple email IDs are mentioned in the “Email” parameter of the “To” block, <<Webex Connect>> submits a single request to AWS SES or to SMTP server to send the concerned email to all - To, CC, and BCC. In this case, the API response will contain only one transaction ID for all recipients. Refer API reference for more information.

When <<prodname>> is used to send emails to multiple email recipients (To, CC, BCC), the message submitted count reflects the total number of emails sent (counting each of the recipient in To, CC, and BCC fields individually). These changes will reflect in the ‘Reports’ and in the ‘Usage’ sections for email transactions.

For email transactions with multiple recipients, the Status field in Debug Console and Export Logs, and Error Codes details, will only be updated for entries with the ‘Submitted’ Status. Email delivery status for each of the individual recipients will need to be tracked using Outbound Webhooks. Separate outbound notifications will be sent for email delivery or failure to each of the recipients mentioned in To, CC, and BCC sections with the same transaction ID. For outbound email transactions, destination will contain an email ID for scenarios where only one email ID has been mentioned (that can in be in either of to, bcc, or cc fields but overall one email ID is mentioned in one outbound request).

AWS SES doesn’t provide the recipient details for events such as opening and/or clicking the link of an email by a specific recipient. The counts for Open and Click events can be higher than the Submit count. For multiple recipient scenarios, given the lack of information of unique recipient info from AWS SES, the redundancy is not uniquely identified, and all Open events are accounted for in reports.
[block:api-header]
{
  "title": "How does Webex Connect handle cases where the Sender Email ID is the same as the Recipient Email ID?"
}
[/block]
The platform will not trigger or resume a flow, nor trigger a rule or an outbound webhook notification for incoming emails where Sender Email ID is same as the Recipient Email ID. However, details of such incoming emails will be available within Export Logs.