# Product Update - v6.18.0, May 2026

Source: https://help.webexconnect.io/changelog/product-update-v6180-may-2026
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:53+00:00

Webex Connect v6.18.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

## Summary

Here’s a list of the key updates and enhancements that are a part of this release:

- WhatsApp Business-Scoped User ID (BSUID) Support in Messaging APIs, Visual Flow Builder and more
- New API for Number Intelligence/Number Lookup (Beta Release)
- mTLS support for OAuth 2.0 based integrations in Custom Node

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

## Details

### Added – WhatsApp Business-Scoped User ID (BSUID) Support in Messaging APIs, Visual Flow Builder and more

In the last release, we added support for WhatsApp Business-Scoped User ID (BSUID) information in Webex Connect Flows (Start and Receive Nodes), Outbound Webhooks, etc. In continuation to that, we are now expanding support for BSUID to Messaging API, WhatsApp Send Node, and Rules and Actions.

To simplify this transition, when Webex Connect receives a WhatsApp message with BSUID details alone (i.e., without phone number (WAID) of the message sender), we will populate the BSUID value into the WAID field as described below.

| Component                                                | Change                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Messaging API, WhatsApp Send Node, and Rules and Actions | - Added new parameter i.e., 'bsuid' in Messaging API for WhatsApp channel to send outbound messages using BSUIDs .   - Added a new Destination Type i.e., ‘BSUID’ in WhatsApp Send Node within Visual Flow Builder, and within Rule-Actions.   - To make it easy for users to transition to the BSUIDs, the platform will accept BSUID value in WhatsApp ID field in Messaging API for WhatsApp, Send Node for WhatsApp, and in Rule-Actions. |
| Delivery Receipts (DRs)                                  | If users send BSUID in the WAID field for outbound messages, Webex Connect sends BSUID to WhatsApp in the correct parameter. Delivery receipts include a new parameter waidNormalised to indicate if message handling remained WAID-based or normalized to BSUID.                                                                                                                                                                              |
| Start Node / Receive Node / Rule Trigger                 | For inbound WhatsApp messages, if WAID is missing and BSUID is present, Webex Connect copies BSUID into WAID for backward compatibility while providing BSUID explicitly. The parameter waidDerived indicates if WAID is original phone number or a derived BSUID value.                                                                                                                                                                       |
| Outbound Webhooks / Data Streams                         | For inbound WhatsApp messages, if WAID is missing and BSUID is present, Webex Connect copies BSUID into WAID for backward compatibility and includes it in outbound webhooks and data streams. The WAID field in outbound data contains BSUID value. The parameter bsuid is added explicitly, and waidDerived indicates when WAID is derived from BSUID.                                                                                       |
| Export Logs / Scheduled Export Logs / Debug Logs         | Added visibility for BSUID, BSUID_DR, and normalization/derived indicators.                                                                                                                                                                                                                                                                                                                                                                   |

**Important Considerations**

- Authentication templates require a phone-number/WAID to be provided. BSUIDs cannot be used for sending Authentication templates.
- You should review your existing flows and any custom business logic configured there in to ensure the above changes do not lead to any disruptions.

### Added – New API for Number Intelligence/Number Lookup (Beta Release)

We are introducing a new and updated Number Intelligence/LookUp API that allows users to submit one or multiple phone numbers to receive essential information for SMS routing decisions. The API supports both international and local number formats, validates and normalises phone numbers, identifies their current carrier, and indicates whether the number is capable of receiving text messages. This information can be used to decide whether to send a communication via SMS or use a different channel.

This feature is currently in Beta and will be available only to a limited number of users and regions. Please reach out to your account manager for more information.

### Added – mTLS support for OAuth 2.0 based integrations in Custom Node

Webex Connect now supports mutual TLS (mTLS) for OAuth 2.0 based integrations configured in Assets -> Integrations → Custom Node section. This enables customers to use mTLS when calling Access Token and Refresh Token URLs using certificates configured under Security Configuration.

When configuring Key Store or Trust Store certificates for a Custom Node, users with permission to add integrations can now choose where each certificate should be applied:

- API Requests
- Authorization Requests (OAuth2.0)
- Both API Requests and Authorization Requests (OAuth2.0)

All existing configurations that already use mTLS for API requests will show the API Requests option enabled in the UI. This is only a UI change and doesn’t impact any existing configurations.

Once Authorization Requests (OAuth2.0) option is selected, Webex Connect will start enforcing mTLS using the selected certificate to the following:

- Access token requests
- Refresh token requests (where applicable based on grant type)

Existing Custom Node behaviour remains unchanged. However, you can upload relevant security certificates and edit and update the configurations to enforce mTLS as needed.

## Changelog

| Update | Description                                                                                                                                                                                                                                                                                                                                                |
| :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Added  | WhatsApp Business-Scoped User ID (BSUID) Support in Messaging APIs, Visual Flow Builder and more                                                                                                                                                                                                                                                           |
| Added  | New API for Number Intelligence/Number Lookup (Beta Release)                                                                                                                                                                                                                                                                                               |
| Added  | mTLS support for OAuth 2.0 based integrations in Custom Node                                                                                                                                                                                                                                                                                               |
| Fixed  | Fixed an issue in the email channel where inbound .msg attachments were not visible in the agent desktop when PCI was enabled. These attachments are now displayed correctly, even when the original filename is unavailable. This applies to email assets which use email forwarding for inbound email processing and SMTP for outbound email processing. |
| Fixed  | Fixed an issue related to text-to-speech (TTS) voice playback where unwanted escaped characters were being spoken aloud in OTP and voice messages.                                                                                                                                                                                                         |
| Fixed  | Fixed duplicate entries in Export Logs for voice trombone/call-patch scenarios in AWS Oregon. Export Logs will not have these duplicate records going forward.                                                                                                                                                                                             |
| Fixed  | Fixed inconsistencies in SMS reporting where Submitted and Failed counts differed slightly across Entity-level and SenderID-level dashboards.                                                                                                                                                                                                              |
| Fixed  | Fixed delivery report status and reason mismatches for one of the error scenarios for Apple Messages for Business transactions                                                                                                                                                                                                                             |
| Fixed  | Fixed an issue in Scheduled Export Logs where filenames used in one-time exports were incorrectly blocked from reuse.                                                                                                                                                                                                                                      |
| Fixed  | Fixed custom-filter reporting issues in RCS where start-date and end-date records were missing across time zones. Date-based report results are now accurate and consistent across supported zones.                                                                                                                                                        |