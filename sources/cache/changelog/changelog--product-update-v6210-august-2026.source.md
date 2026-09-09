<<prodname>> v6.21.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

## Summary

Here's a list of the key updates and enhancements that are a part of this release:

- CPaaS MCP Server for SMS and email (Beta)
- Mobile and Web App Asset Configuration in Control Hub
- Email Asset Configuration in Control Hub
- Enhancements in Export Logs for Push, Live Chat and In-App Messages
- Support for HEIC Images in Email and AMB Channels

Please refer to the details below to learn about all the changes and enhancements.

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

## Details

### Added - CPaaS MCP Server for SMS and email (Beta)

Webex Connect introduces a CPaaS MCP Server that enables MCP-compatible AI agents and applications to discover approved sender IDs and send governed outbound, non-templated SMS and email using the customer's existing Webex Connect tenant. This brings messaging actions into AI workflows while retaining tenant, asset, and administrator controls.

The Beta includes three tools: **webex-sender-ids**, **webex-sms-message**, and **webex-email-message**.

Administrators enable MCP messaging in Webex Connect Tenant Settings, and approve eligible SMS or email assets for Marketing, Utility, or Service use cases. Authentication uses the spark:mcp OAuth scope.

**Availability and scope:** The capability is initially available to selected Beta tenants and is not listed in Webex App Hub during Beta. Regional production access is supported for Canada, Ireland, London, Oregon, Mumbai, Sydney, and Singapore. This release covers outbound, non-templated SMS and email only; inbound messaging, templates, and other channels are not included.

### Added - Mobile and Web App Asset Configuration in Control Hub

Webex Connect now enables Administrators to create and manage Mobile App and Web App assets directly from Control Hub Digital Assets. This centralizes digital-channel onboarding and workload configuration in a single administrative experience.

Assets can be assigned to Webex Connect, Webex Contact Center, or Contact Center Enterprise, depending on the workloads enabled for the organization or tenant. The appropriate workload-specific settings are displayed based on the selected assignment.

**Important note:** Standalone Webex Connect tenants that are not associated with a valid Webex Organization ID cannot sign in through Control Hub.

### Added - Email Asset Configuration in Control Hub

Administrators can now create and manage enterprise Email assets for Gmail, Microsoft 365, and other supported providers directly from Control Hub. This centralizes Email channel onboarding and reduces the need to switch between administrative portals.

Email assets can be assigned to workloads such as Webex Contact Center, Contact Center Enterprise, or Webex Connect. An asset assigned to one workload for two-way messaging cannot be used by another workload simultaneously.

**Important note:** Standalone Webex Connect tenants that are not associated with a valid Webex Organization ID cannot sign in through Control Hub.

### Changed - Enhancements in Export Logs for Push, Live Chat and In-App Messages

Previously, the User ID and Thread ID fields were left empty when the recipient's profile could not be found. These fields are now populated in export logs for Push and Live Chat/In-App messages, providing additional context for failed message attempts.

### Added - Support for HEIC Images in Email and AMB Channels

Webex Connect now supports HEIC images in Media Manager, Email, and Apple Messages for Business, reducing the need for manual format conversion.

Users can upload or import HEIC assets and use them in Email attachments through the Send node, Dynamic Attachments Payload, and Send Message API v2. Inbound Email also supports HEIC attachments. For Apple Messages for Business, HEIC images are supported in the Send node and Send Message API v1.

Supported MIME types are `image/HEIC` and `image/HEIF`. Display of HEIC images depends on the recipient's client support.

## Important Additional Notes

### Upcoming Customer Data Service Node (JDS) Infrastructure Migration

We will soon migrate the backend infrastructure supporting JDS workflows and the associated Customer Data Service node. This change is intended to improve service reliability, maintainability, and scalability.

The migration may require a maintenance window during which JDS workflows and related Node functionality could be temporarily unavailable. Existing workflows, integrations, authentication tokens, CLI tokens, API credentials, and access permissions will remain unchanged.

No action is required at this time. The confirmed migration date, maintenance window, expected duration, and customer impact will be shared in a separate notification in advance.

## Changelog

| Update  | Description                                                                                                                                                                                                                                                                                                                                                                                                |
| :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Added   | CPaaS MCP Server for SMS and email (Beta)                                                                                                                                                                                                                                                                                                                                                                  |
| Added   | Mobile and Web App Asset Configuration in Control Hub                                                                                                                                                                                                                                                                                                                                                      |
| Added   | Email Asset Configuration in Control Hub                                                                                                                                                                                                                                                                                                                                                                   |
| Changed | Enhancements in Export Logs for Push, Live Chat and In-App Messages                                                                                                                                                                                                                                                                                                                                        |
| Added   | Support for HEIC Images in Email and AMB Channels                                                                                                                                                                                                                                                                                                                                                          |
| Fixed   | The Schedule Export Log configuration now correctly displays the available communication channels associated with the selected service(s) when users configure outbound log schedules. This resolves an issue where the Select Channel dropdown could show "No data available" even when channels existed, preventing users from selecting channels and completing the scheduled export log configuration. |
| Fixed   | Resolved an issue where exported logs could show an incomplete log line when an RCS postback URL contained a semicolon character. Export Logs now correctly preserves the full log entry in this scenario, allowing users to review complete RCS postback URL details from the exported file.                                                                                                              |