<<prodname>> v6.19.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

## Summary

- WhatsApp BSUID Support for Contact Policy and Event Scheduler
- Email Channel Onboarding Experience for domain-mapping based Assets
- Expanded Inbound Email Support Across Regions
- Support for Asymmetric JWT authorization in SDKs and Configuration enhancements for Push, In-App  
  Messaging, and Live Chat

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

## Details

### Added - WhatsApp BSUID Support for Contact Policy and Event Scheduler

We are introducing new parameters to extend support for WhatsApp Business-Scoped User IDs (BSUID) across  
Contact Policy and Event Scheduler, helping customers adapt to WhatsApp’s shift beyond phone-number-only  
identification.

With this enhancement, Contact Policy can use BSUID through ‘alternateAddress’ alongside existing addressbased  
identifiers for consent lookup, opt-out handling, upload, export, and record updates. Event Scheduler also  
supports BSUID through ‘alternateAddress’ mapping, enabling scheduled consent workflows to identify and  
update the correct customer even when a WhatsApp phone number is unavailable.

This update helps customers maintain compliant and uninterrupted WhatsApp journeys, avoid duplicate  
customer or consent records, and continue running consent-aware automation with backward compatibility for  
existing configurations.

[block:parameters]
{
  "data": {
    "h-0": "Component",
    "h-1": "Change",
    "0-0": "Contact Policy",
    "0-1": "Added support for two new parameters,  alternateAddress and replaceAlternateAddress,  \nin Contact Policy APIs and the UI file upload flow. alternateAddress stores the WhatsApp BSUID and maps it to the corresponding msisdn. replaceAlternateAddress defaults to false; when  \nset to true, it allows an existing BSUID mapped to an msisdn to be replaced with an updated  \nmapping.",
    "1-0": "Event Scheduler",
    "1-1": "Event Scheduler now supports alternateAddress for WhatsApp-enabled consent groups to enable  \nBSUID-based targeting in addition to msisdn. When a consent group configured through the  \nWebex Connect Contact Policy app is selected as the destination for scheduled messaging, calling,  \nor Custom Event-based flow triggers, alternateAddress is displayed for WhatsApp  \ngroups and can be mapped to the BSUID used for message delivery."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Changed - Email Channel Onboarding Experience for domain-mapping based Assets

Setting up a new Email app asset in Webex Connect currently requires you to configure AWS SES  
access credentials.

With this release, we are introducing a new onboarding experience that doesn’t require you to  
provide any such credentials. You can simply configure your email domain, generate verification  
records and complete DMARC and other standard email set-up requirements. Once done you can  
proceed with using Webex Connect for sending and receiving email messages. You would still be  
required to raise requests for settings such as Custom Mail From sub-domain, or for provisioning  
of dedicated IPs however the basic set-up can now be finished without any dependencies  
allowing you to start using the asset for test traffic without delays.

The existing Email App Assets that were configured using SES credentials provided by Webex  
Connect team will be updated to reflect these changes and will no longer show the Access  
Credentials section. However, any assets created with your own AWS SES accounts before this  
update will remain unchanged.

Further, the bring your own AWS SES account model will no longer be supported for email  
messaging via Webex Connect.

These changes are not applicable to custom SMTP server based Email App assets.

### Added – Expanded Inbound Email Support Across Regions

With this update, Webex Connect will expand inbound email support to align with all the regions that support  
email sending. This will allow customers to configure inbound email processing in more AWS regions and reduce  
dependency on a limited set of supported locations. The newly added regions are Europe (London) and Asia  
Pacific (Singapore).

This enhancement will help customers use inbound email in regions closer to their deployment needs.

### Changed – Support for Asymmetric JWT authorization in SDKs and Configuration enhancements for Push, In-App Messaging, and Live Chat

#### SDK Updates

We are releasing the following Push, Live Chat, and In-App Messaging SDK versions as part of the Webex  
Connect v6.19.0 release:

- Android SDK v3.1.0
- iOS SDK v3.1.0
- JavaScript SDK v1.9.0

Here’s a summary of the changes:

This release adds support for Asymmetric JWT authorization in Android, iOS, JavaScript SDKs and Webex Contact  
Center (WxCC) integration in Android and iOS SDKs, along with several technical enhancements.

- Support for Asymmetric JWT Authorization:
  - The Android, iOS and JavaScript SDKs now support secure authorization using a customer-provided JWT.  
    The customer is responsible for generating and signing the customer JWT using their private key. The  
    mobile application that integrates the SDK provides this JWT to the SDK.
  - If enableAuthTokenExchange is set to true, the SDK sends the customer JWT to Webex Connect for  
    verification. After the customer JWT is successfully verified using the public JWK configured in the  
    Mobile/Web App asset, Webex Connect returns a short-lived Webex Connect access token. The SDK  
    then uses this access token for subsequent communication with Webex Connect, including registration  
    and messaging requests. The SDK also manages access token storage, injection, refresh, and retry,  
    helping reduce the need for the mobile application to manage the Webex Connect token lifecycle  
    directly.
  - If enableAuthTokenExchange is set to false, the SDK sends the customer JWT directly with each request,  
    preserving the legacy authentication behavior used by existing symmetric JWT assets. (Relevant changes  
    have also been made to Mobile/Web App assets; see the following section).
  - Based on the Mobile/Web App asset policy configuration, the SDK automatically works with either  
    Webex Connect or WxCC.
  - For Mobile/Web App assets integrated with WxCC, we have added the SDK methods to support business  
    hours.

For details on SDK updates, see the SDK release notes in our documentation and the Quick Start Guide for WxCC  
Integration.

#### 2.3.2 Webex Connect Platform Updates

- Updated: Mobile/Web App Asset Configuration Experience  
  As part of this release, we have added the “Channels” section in the Mobile/Web App asset configuration  
  page. This section lets users specify whether the asset will be used for:
  - Mobile Push and/or In-App Messaging
  - Web Push and/or Live Chat
  - Both  
    For Mobile Push and/or In-App Messaging, users can also select the applicable platforms, including Android  
    and iOS. This helps users clearly identify the channels and platforms associated with each asset during  
    setup.  
    Existing Mobile/Web App assets remain backward compatible. For existing assets, both Mobile Push and/or  
    In-App Messaging and Web Push and/or Live Chat channels are enabled by default, and existing services  
    continue to work without any changes. Clients can disable unused channels for existing assets from the UI.
- Added: Asymmetric JWT Authorization for New Mobile/Web App Assets  
  Webex Connect now supports Asymmetric JWT Authorization for new Mobile/Web App assets. Previously,  
  Mobile/Web App assets did not show separate Symmetric and Asymmetric authorization options. The JWT  
  Authorization section directly displayed the JWT Secret Key field. Starting with this release, the JWT  
  Authorization section differentiates between the following authorization types:
  - Symmetric (Legacy): Used by existing Mobile/Web App assets. These assets continue to show the JWT  
    Secret Key field and continue to work as before.
  - Asymmetric: Used by new Mobile/Web App assets. These assets allow clients to upload public JSON  
      Web Keys, or JWKs, that Webex Connect uses to verify customer JWTs.  
    For Asymmetric JWT Authorization, clients can upload up to two JWKs, allowing a second key to be added  
    for key rotation. Clients retain the corresponding private key and use it to generate and sign customer  
    JWTs. These JWTs must include the required claims, such as Webex Org ID, User ID, Issuer URL, hash  
    (user&deviceid) and App ID.  
    Clients can also configure the “Authorization Token Expiration Time” from 5 to 360 minutes. When a  
    customer JWT is received, Webex Connect verifies it using the uploaded JWK. After successful verification,  
    Webex Connect issues a Webex Connect access token with the configured Authorization Token Expiration Time. This token is then used for subsequent SDK communication, including registration and sending and  
    receiving messages.  
    Existing Mobile/Web App assets continue to use Symmetric (Legacy) JWT Authorization. If a JWT Secret Key  
    is already configured on an existing asset, it remains unchanged and continues to work as before. This  
    update does not impact existing assets or existing services.  
    Notes:
  - To enable the JWT Asymmetric Webex Org ID is mandatory. For Webex Connect tenants that do not  
    have a Webex Org ID assigned yet, there is an additional pre-requisite step of getting it generated by  
    logging a request with your account manager.
  - Migration from Symmetric JWT Authorization to Asymmetric JWT Authorization is not supported in this  
    release. To use Asymmetric JWT Authorization, create a new Mobile/Web App asset and configure it  
    with the asymmetric option.  
    For more information, refer to the Create Mobile application and Asymmetric JWT Authorization pages in  
    the documentation.
- Added: Asymmetric JWT Authorization for Thread APIs and Get User Messages API  
  Starting with this release, when Asymmetric JWT Authorization is enabled, the WX-Device-Id header is  
  required for the Get Thread API, Update Thread API, and Get User Messages API. The WX-Device-Id header  
  is not required for the Create Thread API.  
  This requirement does not apply to existing assets that use Symmetric JWT Authorization.
- Changed: Enhancements to Webex Contact Center Integrated Tenants:
  - WxCC Asset Registration: As part of this release, when users make changes to Mobile/Web App assets,  
    such as push configuration or JWT authorization updates, they can reregister the asset with Webex  
    Engage. During reregistration, users can also select a different service.
  - Asymmetric JWT Authorization: For WxCC assets, users can select either Mobile Push and/or In-App  
    Messaging or Web Push and/or Live Chat, but not both. Asymmetric JWT Authorization is mandatory  
    for Mobile Push and/or In-App Messaging. Web Push and/or Live Chat does not currently support JWT  
    Authorization.
  - Server Side Inbox: As part of this release, the Server Side Inbox feature is hidden for all WxCC tenants.  
    If it was enabled previously, it no longer appears in the UI, but the flag remains enabled.
  - Multi-User Registration on Same Device: Multi-user registration on the same device is enabled by  
    default for all WxCC tenants.  
    For more information, refer to the [Live Chat - WXCC page](https://help.webexconnect.io/docs/livechat-asset-creation-wxcc) in documentation.

## Important Additional Notes

- **iOS SDK Distribution via CocoaPods**  
  CocoaPods has announced that its public specs repository will transition to a read-only state effective  
  December 2, 2026. Following this change, it will no longer be possible to publish new versions of SDKs to  
  the public CocoaPods repository.  
  **Impact on our iOS SDK**  
  Existing versions of our iOS SDK distributed via CocoaPods will remain available and continue to function  
  as expected. New releases and updates of the iOS SDK beyond the stated date may not be distributed  
  through CocoaPods.  
  We recommend adopting Swift Package Manager (SPM) as the preferred integration method for our iOS  
  SDK, as it will serve as the primary distribution channel for future releases. We will continue to support  
  CocoaPods-based integrations for our iOS SDK during the transition period and will provide guidance to  
  ensure continuity and stability. For all new integrations of our iOS SDK, Swift Package Manager (SPM) is  
  the recommended approach.
- **Outbound Webhook and Data Stream payloads for Incoming SMS Message**
  As part of Webex Connect version 6.20 (upcoming release), a new parameter will be  
  added in the Outbound Webhook and Data Stream payloads for Incoming SMS Messages  
  (MOs) to indicate the multipart message count of an inbound SMS. Please refer to the  
  official documentation for detailed information and update your implementations  
  accordingly.
- **Removal of 'Device Attributes for Mobile Apps' Feature**
  As previously communicated, the Device Attributes for Mobile Apps feature is no longer  
  supported for the Push, Live Chat, and In-App Messaging channels on Webex Connect.  
  With the v6.19.0 release, this feature has been fully removed from the Webex Connect  
  user interface and documentation.

## Changelog

[block:parameters]
{
  "data": {
    "h-0": "Update",
    "h-1": "Description",
    "0-0": "Added",
    "0-1": "WhatsApp BSUID Support for Contact Policy and Event Scheduler",
    "1-0": "Changed",
    "1-1": "Email Channel Onboarding Experience for domain-mapping based Assets",
    "2-0": "Added",
    "2-1": "Expanded Inbound Email Support Across Regions",
    "3-0": "Changed",
    "3-1": "Push, In-App Messaging, and Live Chat-related enhancements",
    "4-0": "Added",
    "4-1": "Added filtering and sorting controls to the Template Management page, making it easier to find templates as template lists grow. Users can filter by channel, type, status, and creator, and sort by name, created date, or last modified date.",
    "5-0": "Changed",
    "5-1": "In the previous release, we are having the blank separator row between transactional export records and carrier deactivation failure records. From this release we are removing the empty row between them.",
    "6-0": "Fixed",
    "6-1": "Resolved an issue where the WhatsApp embedded signup flow incorrectly allowed the creation of duplicate  \nWhatsApp apps for the same number. The platform now prevents these duplicates, ensuring each number is associated with only one app.",
    "7-0": "Fixed",
    "7-1": "Resolved an issue in the RCS Flow Send node where the \"file size\" parameter incorrectly triggered a \"Required\" validation error when the Media URL and Thumbnail URL fields were empty. The validation logic has been corrected to ensure accurate error messaging.",
    "8-0": "Fixed",
    "8-1": "Fixed the issue where Flow Settings tabs could take longer to open for flows with many session variables. Scrolling is now consistent across all Flow Settings tabs.",
    "9-0": "Fixed",
    "9-1": "Fixed the issue where the onAnsweringMachine outcome could sometimes connect to the wrong graph edge because its ID conflicted with generated graph IDs. Flow graphs now render more reliably.",
    "10-0": "Fixed",
    "10-1": "We have improved the feedback provided during Contact Policy (CP) file uploads. Previously, issues such as header mismatches or column errors resulted in upload failed without proper error message. The UI now displays clear, descriptive failure reasons, allowing users to quickly identify and resolve upload issues."
  },
  "cols": 2,
  "rows": 11,
  "align": [
    "left",
    "left"
  ]
}
[/block]