Contact Policy application provides you with the ability to store customer consent information for various communication purposes. In addition, it offers you with the ability to apply contact thresholds to avoid sending too many messages or calls to the same customer. 

Contact Policy application works in conjunction with the Contact Policy APIs and Messaging APIs. 

At the center of this are Consent Groups that you can configure once you access the Contact Policy app. A consent group is set up on an opt-in or opt-out basis with the following capabilities:

- Customer consent management:  Create and manage consent groups for opt-in or opt-out management.
- Contact preference management: Capture and maintain consumer's preference for the business to utilize a specific channel when contacting them
- Contact Frequency Management – Configure policy limits and track usage against these limits for communication frequency on a daily, weekly, or monthly basis.
- Maintain a clear audit trail of edits, lookups, and changes made to the consent group settings.

> 📘 Important!
> 
> - Contact Policy Application is in GA mode. However, it is not enabled by default for all tenants. Please reach out to the Support Team using the details mentioned in the Contact Support section within your tenant if you want this to be enabled for your tenant.
> - Carrier messaging channels SMS, MMS, and RCS are clubbed into one category referred to as 'Text'.
> - Contact Policy supports Text, Voice, and Email channels on the Messaging API (v1 and v2). WhatsApp consent records can also be maintained for WhatsApp-enabled consent groups, including support for Business-Scoped User ID (BSUID) values through the `alternateAddress` field.
> - For WhatsApp consent records, `alternateAddress` is used to store the Business-Scoped User ID (BSUID). This allows consent lookup and consent updates to use either the WhatsApp address/WAID or the BSUID where applicable.
> - The policy preferences do not apply to the Send nodes in the flows. You will need to apply Contact Policy / Consent checks explicitly in your flows before sending the messages.
> - Contact Policy is now available on Webex Connect Azure deployment site as well.

## WhatsApp BSUID support in Contact Policy

Contact Policy supports WhatsApp consent records that include a WhatsApp address or WAID and, where available, a Business-Scoped User ID (BSUID).

For WhatsApp records, BSUID is stored as an alternate address using the alternateAddress field. This allows consent checks and opt-out handling to work when a customer is identified by BSUID instead of a phone number.

When both WhatsApp address/WAID and BSUID are available, store both values so that Contact Policy can maintain the customer’s consent record without creating duplicate records for the same customer.