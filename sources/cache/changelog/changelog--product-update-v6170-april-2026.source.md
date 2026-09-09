<<prodname>> v6.17.0 release brings multiple new capabilities to help you continue delivering seamless customer experiences.

# Summary

Here’s a list of the key updates and enhancements that are a part of this release:

- Support for WhatsApp Business-Scoped User IDs (BSUID)
- RCS Onboarding Enhancements
- Carrier Information in SMS Delivery Receipts and Export Logs
- Authentication Context Requirements in SSO Settings
- Push, In-App Messaging, and Live Chat-related Enhancements
- Inclusion of Carrier Deactivation Logs into Contact Policy Export Logs

Please refer to the details below to learn about all the changes and enhancements.

> 📘 Release Date
> 
> The date of release will be communicated separately over an email.

# Details

## Support for WhatsApp Business-Scoped User IDs (BSUID)

Meta will be introducing WhatsApp usernames to enhance user privacy, allowing users to interact with businesses without sharing their phone numbers. As part of this change, businesses may receive a Business-Scoped User ID (BSUID), a unique identifier for user-business interactions, along with the user’s WhatsApp username or user-handle, which represents the end user’s unique name on WhatsApp.

In addition, WhatsApp launched the Contact Book feature, which maintains mappings between phone numbers and BSUIDs for users who have previously interacted with a business. When a user contacts a business, if a matching entry exists in the Contact Book, the user’s phone number is shared with the business; otherwise, only the BSUID is shared.

To support this transition and help maintain customer context, <<prodname>> now provides BSUID visibility across key areas, including Outbound webhooks, Data streams, Start/Receive Nodes, and Export logs. This enables you to capture BSUID alongside the existing WhatsApp ID (WAID) and maintain BSUID-to-WAID mappings in your systems. Please note BSUIDs will begin appearing in incoming payloads in April 2026.

Further enhancements to ensure backward compatibility and broader platform support will be introduced in upcoming releases.

| Component                             | Update                                                                                                                                                                                                                                                                               |
| :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WhatsApp Start Node and Receive Node  | ‘whatsapp.bsuid’ and ‘whatsapp.userHandle’ fields added to capture the BSUID and the user’s WhatsApp username/user-handle. This is added to all WhatsApp incoming events.                                                                                                            |
| Outbound Webhooks and Data Streams    | bsuid and userHandle fields added in app-based incoming event payloads to capture the BSUID and the user’s WhatsApp username/user-handle when available in the inbound WhatsApp event.                                                                                               |
| Export Logs and Scheduled Export Logs | BSUID field/column added to capture BSUID for WhatsApp transactions when available. In inbound logs, this captures BSUID if it is received from Meta. In outgoing export logs and scheduled export logs, this captures BSUID associated with the transaction once available for use. |

For more information on BSUID, WhatsApp Usernames, and Contact Book, refer to the **WhatsApp Usernames and Business-Scoped User IDs (BSUID)** and **New Export Logs** article in the Platform Help (v6.17.0 set) and [WhatsApp Outbound Webhooks](https://developers.webexconnect.io/reference/whatsapp-outbound-webhooks) article in API Reference (v6.17.0 set).

## RCS Onboarding Enhancements

We have enhanced the RCS app creation experience in <<prodname>>. The process now includes a prerequisite help section followed by a two-phase submission workflow. Users must first submit app creation details, which are locked for review upon submission. Once the initial setup is approved, the verification and launch section becomes accessible for users to provide the remaining legal and launch-specific information required to complete the onboarding. This will be available only for tenants that have RCS channel enabled.

For more information on RCS app creation, refer to the **Configure RCS Agent** article in the Platform Help (v6.17.0 set).

## Carrier Information in SMS Delivery Receipts and Export Logs

We have added a new parameter named ‘carrier’ in SMS Outbound Export logs, Delivery Receipts, Outbound Webhook and Data Stream payloads to include Destination Carrier identified. This parameter will be added to delivered, failed and undelivered delivery receipts only. This change is available in all <<prodname>> regions, but data populated is limited to US and Canada. This feature will also be gradually rolled out in the UK, so carrier information will not be available for all traffic. More information will become available in the UK as we progress with the rollout. 

We recommend referring to the changes documented below and making any required changes in your implementation to consume the information.

The following value has been added: 

**Name: ** carrier  
**Description: **unique identifier of the carrier (refer to the mapping table below)

```Text Sample Delivery Receipt
{  
  "deliveryInfoNotification": {  
    "deliveryInfo": {  
      "timeStamp": "2022-10-10T13:53:13.749+01:00",  
      "Description": "Delivered",  
      "code": "7500",  
      "messageCount": "1",  
      "deliveryChannel": "SMS",  
      "additionalInfo": "",  
      "destination": "1189xxxxxxxx",  
      "destinationType": "msisdn",  
      "deliveryStatus": "Delivered"  
    },  
        "carrier": "USTMO", //New variable will be sent starting v6.17.0 onwards.  
        "subtid": "",  
        "transid": "7f3af32c-8d6a-XXXX-b1c8-4805135ada71",  
        "callbackData": "",  
        "correlationid": ""  
  }  
}
```

Refer to the [SMS Carrier Mapping table](https://developers.webexconnect.io/reference/sms-carrier-mapping) that maps the carrier identifier of the delivery receipt payload to the full name and country of the carrier.

## Authentication Context Requirements in SSO Settings

<<prodname>> now includes a new “Authentication Context Requirements” section in SSO Settings in <<prodname>>. This allows Tenant Owners to choose which login methods are accepted during SSO, improving compatibility with Identity Providers that use MFA and other authentication methods, while keeping the default password-based login unchanged.

For more information, refer to the [Single-sign-on](https://help.webexconnect.io/docs/single-sign-on-settings) article (v6.17.0 set) in Platform Help.

## Push, In-App Messaging, and Live Chat-related enhancements

As part of this release, we have updated App Profile Management to remove push-only profiles when Firebase Cloud Messaging (FCM) returns an “Unregistered error”. If the profile is also associated with Live Chat or In-App Messaging, it is retained to help prevent unnecessary profile deletion and keep those channels working. 

For more information, refer to the [App Profile Management](https://developers.webexconnect.io/docs/app-profile-management) article (v6.17.0 set) in Platform Help.

## Inclusion of Carrier Deactivation Logs into Contact Policy Export Logs

We have enhanced existing Contact Policy export logs to include carrier deactivation failure details, improving visibility into deactivation-related consent changes without relying on separate manual reporting workflows. To include Deactivation Logs in your Contact Policy exports, please contact the support team. This enhancement is available only in the Oregon region and for tenants that have Contact Policy feature enabled.

# Important Additional Notes

Meta has updated Messenger policy for messages sent beyond 24 hours from the customer’s last message. For such post-24-hour use cases, only the “HUMAN_AGENT” tag is supported. Other Messenger message tags are no longer supported for this scenario and may result in message failures. <<prodname>> users using Messenger APIs and flows that rely on “non-HUMAN_AGENT” tags outside the 24-hour window should review and update them accordingly.

For more information, refer to the [Messenger Node](https://help.webexconnect.io/docs/messenger) article (v6.17.0 set) in Platform Help and [Facebook Messenger API](https://developers.webexconnect.io/reference/facebook-messenger-api#facebook-messenger-messaging-parameters) article (v6.17.0 set) in API Reference Documentation.

# Deprecated Items

NA

# Changelog

| Update  | Description                                                                                                                                                                                                                      |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Added   | Support for WhatsApp Business-Scoped User IDs (BSUID)                                                                                                                                                                            |
| Added   | RCS Onboarding Enhancements                                                                                                                                                                                                      |
| Added   | Carrier ID Information in SMS Delivery Receipts and Export Logs                                                                                                                                                                  |
| Added   | Authentication Context Requirements in SSO Settings                                                                                                                                                                              |
| Changed | Push, In-App Messaging, and Live Chat-related enhancements                                                                                                                                                                       |
| Changed | Updated Messenger Send Node to reflect Meta's deprecation of several message tags and the transition to the HUMAN_AGENT tag for messaging outside the 24-hour window.                                                            |
| Changed | Inclusion of Carrier Deactivation Logs into Contact Policy Export Logs                                                                                                                                                           |
| Fixed   | Resolved an issue where Export Logs did not capture email soft bounces.                                                                                                                                                          |
| Fixed   | Resolved an issue where the Event Scheduler exceeded the configured Event API TPS limits; it now correctly follows the defined rate limits and properly throttles requests.                                                      |
| Fixed   | Resolved an issue where the "Not Allocated" app sharing status was not saved correctly and reverted to "Share to all groups and teams". The selected option now persists as expected.                                            |
| Fixed   | Resolved an issue were uploading an Excel file containing new lines or line breaks, caused a null pointer exception, preventing the Event Scheduler from running, and failing to generate error logs or notifications.           |
| Fixed   | Resolved an issue where email forwarding verification messages did not appear in the Debug Console, preventing users from verifying forwarding rule for their email assets. These events are now logged and displayed correctly. |
| Fixed   | Resolved an issue where the scope shown during Custom Node access token generation did not match the configured value and fixed a bug that caused the Manage page to become non-scrollable after editing a Custom Node.          |