# Product Update - v6.15.0, January 2026

Source: https://help.webexconnect.io/changelog/product-update-v6150-january-2026
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:53+00:00

Webex Connect v6.15.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

# Summary

- mTLS Certificate Support in Outbound Webhooks
- Increased Limit of Custom Domains for Link Shortener
- Alternate Text-to-Speech (TTS) provider for Fallback
- Push, In-App Messaging, and Live Chat-related enhancements
- Support for new RCS message categories and fields

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

# Details

## Added - mTLS Certificate Support in Outbound Webhooks

Webex Connect now supports Mutual Transport Layer Security (mTLS) for outbound webhooks. mTLS  
enhances security by ensuring that both Webex Connect and the receiving endpoint authenticate each  
other before establishing a secure connection. This feature is not enabled by default. To enable mTLS for  
your tenant, please contact your account manager. Enabling mTLS may require sharing your endpoint’s  
public certificate and completing additional configuration steps. For full configuration steps and supported  
certificate formats, refer to the Outbound Webhooks documentation.

For more information, refer to the [Outbound Webhooks](https://help.webexconnect.io/docs/outbound-webhooks) topic in the v6.15.0 set of Platform Guide and [In-App Messages](https://developers.webexconnect.io/reference/in-app-messages) topic of API Reference Guide.

## Changed – Increased Limit of Custom Domains for Link Shortener

The maximum number of custom domains supported for the Link Shortener feature has been increased  
from 3 to 50 per client. Both the UI and API now allow configuration and management of up to 50 custom  
domains. This enhancement addresses the growing need for clients who serve multiple end customers,  
each requiring a unique domain. Existing clients with up to 3 configured domains will not be impacted by  
this change.

For more information, refer to the [Link Shortener](https://help.webexconnect.io/docs/link-shortener) topic in the v6.15.0 set of the guide.

## Changed – Alternate Text-to-Speech (TTS) provider for Fallback

 Webex Connect now supports automatic fallback to an alternate Text-to-Speech (TTS) provider when the  
primary provider, Azure Speech Services, experiences failures. To enable this feature for your tenant,  
please contact the support team.

## Added – Push, In-App Messaging, and Live Chat-related enhancements

Here’s a summary of the changes:

- JavaScript SDK v1.8.0 (minified, no functional changes).

**SDK Configuration Files Decoupled from Push Notifications**

SDK configuration files are now independent of Push Notifications and are accessible through a new  
dedicated SDK Configuration Files section on the Mobile & Web Asset page. This section provides access  
to Android, iOS, and Web configuration files, enabling clients using only Live Chat or In-App Messaging to  
download required SDK files without configuring Push Notifications.

**Changed – JavaScript SDK Download and Integration Update**

Previously, the JavaScript SDK could be downloaded directly from the Mobile & Web Asset page under the  
Push Notifications section after configuring Push in the Connect Platform. With this release, only the imienvironment.  
js configuration file is available for download from the Connect Platform. The JavaScript SDK  
v1.8.0 is now publicly available and provided as a minified package. There are no functional updates to the  
JavaScript SDK in this release, so customers are not required to make any changes or re-integrate the  
SDK at this time. Going forward, if updates are introduced to the JavaScript SDK, customers will be  
required to integrate the updated minified SDK. There will be no changes to existing SDK methods or APIs;  
only the integration approach will change. 

For details on the integration process, please refer to the [Live Chat](https://help.webexconnect.io/docs/livechat-asset-creation-wxcc#configuring-live-chat-channel-asset-on-webex-connect) and [Set-up a new Mobile / Web App Asset](https://developers.webexconnect.io/docs/create-mobile-application-on-imiconnect-platform#create-a-mobile-app-asset-in-webex-connect) in the v6.15.0 set of the SDK guide.

## Support for new RCS message categories and fields

We have updated RCS Usage report to align billing definitions with regional carrier standards in the US  
(new categories - ‘rich’ and 'rich media) for both Outbound and Inbound RCS messages.

**Regional Categorization**: The existing ‘**basic_sent**’ and ‘**single_sent**’ columns in the report have been  
updated to include new categorization logic specifically for the US region.  
Inbound message categorization: New columns are introduced in the report to categorize Incoming  
Messages as ‘**basic_received**', ‘**single_received**’, or ‘**suggestionclicks_received**’.

**Note**: The categorization remains the same for regions other than the US.

For more information, refer to the [Usage Reports Fields](https://help.webexconnect.io/docs/usage-report-fields#rcs) topic in the v6.15.0 set of the Platform Guide.

# Important Additional Notes

NA

# Deprecated

NA

# Changelog



| UPDATE | DESCRIPTION |
| --- | --- |
| Added | mTLS Certificate Support in Outbound Webhooks |
| Changed | Increased Limit of Custom Domains for Link Shortener |
| Added | Alternate Text-to-Speech (TTS) provider for Fallback |
| Added | Push, In-App Messaging, and Live Chat-related enhancements |
| Fixed | When attempting to upload a display image in the WhatsApp asset, clicking the ‘Upload Image’ button previously opened a blank page instead of launching the browser or file picker for image selection. |
| Fixed | Resolved an issue where event times in the Social Hour node and platform Tenant Settings were incorrectly displayed for time zones impacted by recent IANA timezone updates, including the 2023 changes in Mexico and multiple other regions. The system now accurately reflects local times year-round based on the latest IANA rules, addressing discrepancies caused by daylight saving time changes. This fix currently applies to selected customers as a controlled release and will be made generally available in future updates. |
| Fixed | Resolved an issue where transaction data older than 30 days was not loading in the Connect tenant when using the Custom Filter, due to a backend exception. Users can now successfully view and access transaction records beyond 30 days without encountering errors. |
| Fixed | Branded Text: In SMS Outbound sheet of Usage Reports, Branded Text entries did not show Carrier info  (Carrier id, Carrier Name), which is fixed now. |
| Fixed | RCS Conditional Triggering: Previously, flows configured with conditional triggering in the RCS Start Node for ‘Postback’ and ‘Location Response’ Event Types were not functioning as expected. With this fix, those flows will now operate as intended for both RCS and Branded Text channels.  <br>**Note**: Since this change restores the intended functionality, it may impact the behavior of existing flows. We recommend reviewing your flows that use conditional triggering with these Event Types to ensure they continue to work as expected. |

