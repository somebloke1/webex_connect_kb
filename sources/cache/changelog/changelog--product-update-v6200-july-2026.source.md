<<prodname>> v6.20.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

# Summary

- Apple Messages for Business Invitation Messages
- Inbound SMS Message Part Count in Outbound Webhooks and Data Streams
- IP Address Allowlist Management in Webex Connect Tenant Settings
- TLS 1.3 support for Custom Node integrations
- Enhanced Consent Policy Reports for Data Visibility with Download Capability

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

<br />

# Details

<br />

## Added - Apple Messages for Business Invitation Messages

With this update, Webex Connect will support Apple Messages for Business Invitation Messages, enabling businesses to invite customers to start an Apple Messages for Business conversation using a mobile number.

Invitation Messages will be supported in the Apple Messages for Business Send Node and Send Message API v1. In the Send Node, flow authors will be able to select the new Invitation Message option and configure invitation-specific fields, including Destination Type = Mobile Number, Mobile Number, Send With Image, Brand Name, and optional Locale.

For API users, Send Message API v1 will support invitation messages through the existing Apple Messages for Business endpoint using `destination.msisdn` and invitation-specific channels. Apple Business Chat parameters: type=`invitation`, `withImage`, `brandName`, and `requestIdentifier`.

Once the recipient responds, Webex Connect will make the response available through the new Invitation Response event. In Start Node, this event will be available as `InteractiveMessage`: Invitation Response. In Receive Node, it will be available as `Interactivemessageresponse`: Invitation.

Invitation-specific variables such as `abc.mobileNumber`, `abc.invitationAccepted`, and `abc.invitationResponse` will be available for downstream flow logic. Outbound webhooks and Rule Notify URL events will support invitation submission, failure, and response events. Submission and failure delivery receipts will use the existing `deliveryInfoNotification` contract with `destinationType`=`msisdn` and the invited customer’s mobile number in destination.

Invitation send and response details will also be available in Debug Logs and Export Logs. Webex Connect will apply suppression checks before sending invitations and block invitation sends to restricted destinations where required. Existing Apple Messages for Business behavior for non-invitation message types will remain unchanged.

<br />

## Added - Inbound SMS Message Part Count in Outbound Webhooks and Data Streams

We have added a new parameter named `messageCount` in SMS MO Outbound Webhook and DataStream payloads to include the total number of message parts received for an inbound SMS. This value will be used to accurately count inbound SMS message volumes in Webex Connect usage reports.

This change applies to SMS Inbound usage reporting, specifically the `messages_received` count.

We recommend referring to the changes documented below and making any required changes in your implementation to consume the information.

The following value has been added:

**Name**: `messageCount`

**Description**: Total number of message parts received for the inbound SMS.

**Sample SMS MO Payload**

```Text Sample Delivery Receipt
{
  "userId": "8765",
  "Channel": "SMS",
  "da": "565XX",
  "message_source": "SMS",
  "oa": "XXXXXXXXXX",
  "message": "Incoming Text Message",
  "messageCount": "1", // New variables will be sent starting v6.20.0 onwards.
  "tid": "0044_7826374XXXX",
  "datetime": "2024-01-07T14:36:09.266Z",
  "ts": "2024-01-07T14:36:09.266Z",
  "x_networkid": "9"
}
```

<br />

## Added - IP Address Allowlist Management in Webex Connect Tenant Settings

Tenant Owners can now add, remove, validate, and save IPv4 addresses or CIDR ranges directly from Webex Connect Tenant Settings without raising a support ticket. Once configured, tenant API traffic is restricted to the listed IP addresses or ranges.

<br />

## Added - TLS 1.3 support for Custom Node integrations

Custom Nodes now support TLS 1.3 for secure connections to downstream REST and SOAP services. New configurations can use TLS 1.2 or TLS 1.3.

TLS 1.0 and TLS 1.1 are unavailable for new configurations, while existing custom nodes using these protocols continue to operate.

> 📘 Note
> 
> As a security recommendation, customers using TLS 1.0 or TLS 1.1 are strongly encouraged to migrate to TLS 1.3.
> 
> TLS 1.0 and TLS 1.1 will be deprecated in an upcoming sprint, so customers should update their configurations in advance.

<br />

## Added - Enhanced Consent Policy Reports for Data Visibility with Download Capability

Webex Connect now offers enhanced Contact Policy reporting capabilities, making it easier for business users to review, analyze, and share Consent Group Activity reporting data.

Users can generate Contact Policy reports for a selected time and download the report data in .xlsx format for offline analysis, stakeholder sharing, presentations, and audit or compliance recordkeeping. The updated reporting experience also improves visibility into the groups included in the selected period and helps users quickly find specific groups within the generated report.

<br />

# Important Additional Notes

### Legacy Export Logs No Longer Available

The [Legacy Export Logs](https://help.webexconnect.io/docs/legacy-export-logs) option will no longer be available in Webex Connect.

This is replaced by New Export Logs capability for exporting logs. This updated experience should be used for all log export requirements going forward.

For more information, refer to the [New Export Logs](https://help.webexconnect.io/docs/new-export-logs) documentation.

<br />

# Changelog

| Update | Description                                                                                                                                                          |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Added  | Apple Messages for Business Invitation Messages                                                                                                                      |
| Added  | Inbound SMS Message Part Count in Outbound Webhooks and Data Streams                                                                                                 |
| Added  | IP Address Allowlist Management in Webex Connect Tenant Settings                                                                                                     |
| Added  | TLS 1.3 support for Custom Node integrations                                                                                                                         |
| Added  | Enhanced Consent Policy Reports for Data Visibility with Download Capability                                                                                         |
| Fixed  | Improved timestamp consistency for records in exported logs. Millisecond precision is now preserved across all records, including timestamps with .000 milliseconds. |
| Fixed  | The script section in the Evaluate node now preserves its original multi-line formatting when copied flows are reopened, improving readability and ease of editing.  |