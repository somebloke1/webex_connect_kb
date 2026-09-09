Webex Connect v6.22.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

## Summary

Here's a list of the key updates and enhancements that are a part of this release:

- WhatsApp Channel Asset Configuration in Control Hub
- Facebook Messenger Channel Asset Configuration in Control Hub
- Channel-specific CI Authentication for Webex Connect Outbound Messaging APIs
- Carrier Submit Timestamp in Webex Connect SMS Delivery Receipt and Data Streams
- Audit Log Export via Export Logs
- WhatsApp Template Management APIs on Developer Portal
- CI Authentication for Outbound Webhook Configuration APIs
- Live Chat/In-App Messaging Form Response Webhook Update
- Automated Workflow for US 10DLC Registration and Number Management

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

## Details

### Added - WhatsApp Channel Asset Configuration in Control Hub

Webex Connect now enables Administrators to create and manage WhatsApp channel assets directly from Control Hub Digital Assets. This centralizes digital-channel onboarding and workload configuration in a single administrative experience. Assets can be assigned to Webex Connect, Webex Contact Center, or Contact Center Enterprise, depending on the workloads enabled for the organization or tenant. The appropriate workload-specific settings are displayed based on the selected assignment.

**Important note:** Standalone Webex Connect tenants that are not associated with a valid Webex Organization ID cannot sign in through Control Hub.

### Added - Facebook Messenger Channel Asset Configuration in Control Hub

Webex Connect now enables Administrators to create and manage Facebook Messenger channel assets directly from Control Hub Digital Assets. This centralizes digital-channel onboarding and workload configuration in a single administrative experience. Assets can be assigned to Webex Connect, Webex Contact Center, or Contact Center Enterprise, depending on the workloads enabled for the organization or tenant. The appropriate workload-specific settings are displayed based on the selected assignment.

**Important note:** Standalone Webex Connect tenants that are not associated with a valid Webex Organization ID cannot sign in through Control Hub.

### Added - Channel-specific CI Authentication for Webex Connect Outbound Messaging APIs

Webex Connect now supports CI token authentication for supported outbound Messaging APIs across Webex Connect channels. One supported Messaging API version is enabled for each channel. To use the API, the required CI authentication scope must first be enabled for that specific channel. Existing JWT and service-key authentication methods continue to be supported, and current integrations will continue to work as expected without any changes.

### Changed - Carrier Submit Timestamp in Webex Connect SMS Delivery Receipt and Data Streams

We have added a new parameter named `carrierSubmitTimeStamp` in SMS Outbound Delivery Receipts Webhook and Data Stream payloads. This parameter contains the date and time an SMS was submitted to the carrier and will be added to delivered, failed and undelivered delivery receipts only.

We recommend referring to the changes documented below and making any required changes in your implementation to consume this information.

**Name:** `carrierSubmitTimeStamp`

**Description:** Date and time when the SMS was submitted to the carrier.

### Added - Audit Log Export via Export Logs

Audit logs can now be exported through the existing Scheduled Export Logs workflow. When enabled for a tenant using the Admin Console custom tag, this feature allows customers to schedule audit-log CSV exports to their configured SFTP destination. This productized Webex Connect export path helps enterprise customers meet audit and compliance requirements without relying on custom export pipelines. Audit log export is supported only through scheduled exports; on-demand export is not supported.

### Added - WhatsApp Template Management APIs on Developer Portal

Webex Connect now enables secure, programmatic management of WhatsApp message templates using CI authentication. Using this API, organizations can create and update templates, monitor their approval status, and remove templates when they are no longer needed. This provides a consistent way to manage the complete template lifecycle, supports API-first and headless CPaaS use cases, and reduces reliance on manual portal operations.

### Added - CI Authentication for Outbound Webhook Configuration APIs

Webex Connect now supports managing outbound webhook configurations programmatically using CI-authenticated APIs. The corresponding CI scope must be enabled before the APIs can be used. Once the scope is enabled, clients can configure webhook destinations, select supported notification events, validate configurations, and manage existing webhook setups.

### Changed - Live Chat/In-App Messaging Form Response Webhook Update

Live Chat and In-App Messaging form response outbound webhook payloads now include clientId, thread_id, thread_title, and a thread object. This aligns the form response event with other incoming events and gives customers more consistent context for routing, reporting, and downstream processing.

### Added - Automated Workflow for US 10DLC Registration and Number Management

Webex Connect now supports an automated workflow for US 10DLC registration and number management. Once the required scope is enabled, customers can register brands and campaigns, purchase 10DLC numbers, bring their own numbers or port existing numbers, request Number Pools, and provision numbers. This capability is initially available through an Early Access release, and availability and release timing may vary by account and region.

## Important Additional Notes

No additional notes for this release.

## Changelog

| Update | Description |
|---|---|
| Added | WhatsApp Channel Asset Configuration in Control Hub |
| Added | Facebook Messenger Channel Asset Configuration in Control Hub |
| Added | Channel-specific CI Authentication for Webex Connect Outbound Messaging APIs |
| Changed | Carrier Submit Timestamp in Webex Connect SMS Delivery Receipt and Data Streams |
| Added | Audit Log Export via Export Logs |
| Added | WhatsApp Template Management APIs on Developer Portal |
| Added | CI Authentication for Outbound Webhook Configuration APIs |
| Changed | Live Chat/In-App Messaging Form Response Webhook Update |
| Added | Automated Workflow for US 10DLC Registration and Number Management |
| Fixed   | Arabic characters were not represented correctly when flows were exported and then imported. This issue has been resolved for new flows where the base file does not contain the character-rendering problem. |