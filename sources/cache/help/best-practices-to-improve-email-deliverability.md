# Best Practices to Improve Email Deliverability

Source: https://help.webexconnect.io/docs/best-practices-to-improve-email-deliverability
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:02+00:00

In the crowded digital landscape, reaching your audience through email isn't always straightforward. Missing crucial email set-up steps, like unverified domains or weak authentication, can land even the most well-crafted messages in the dreaded spam abyss. This article offers simple, actionable best practices to help you improve deliverability and ensure that your emails land where they belong: in your customer's inboxes. 

In general, we recommend all clients who use Webex Connect in combination with AWS SES for sending outbound emails to follow the email best practices below:

## Follow-Email Authentication best practices

### Finish Domain Verification

Add a TXT record to your Domain Name System (DNS) to verify with Amazon SES that you own the domain that you will be sending from. Details of TXT records become available on the Email app asset page within Webex Connect after you configure the AWS SES credentials.

### Set-up DKIM to protect your domain against spoofing

DKIM, which stands for DomainKeys Identified Mail, is an email authentication method designed to detect forged header fields and content in emails. DKIM enables the receiver to check if email headers and content have been altered in transit. If you haven’t done setting up DKIM already, please enable the DKIM Settings in your Webex Connect Email App Asset Configuration Page and update your domain’s DNS records using the information displayed in app asset configuration page.

### Sender Policy Framework (SPF) authentication

**SPF** is a form of email authentication that prevents spammers from sending unauthorized messages that appear to be from your domain. SPF acts like a guard, telling mail servers which computers are authorized to send emails under your domain, stopping scammers from impersonating you.  
If you are not using [custom MAIL FROM domain ](https://help.webexconnect.io/docs/best-practices-to-improve-email-deliverability#add-custom-mail-from-domain)for sending emails, AWS SES uses one of the subdomains of amazonses.com as MAIL FROM domain and SPF is already complied with.

### Set-Up a DMARC Policy

A DMARC policy tells receiving servers what action to take on unauthenticated messages (i.e., messages that don’t pass either DKIM or SPF) they get from your domain. 

To set up DMARC, you have to modify the DNS settings for your domain by adding a TXT record as per below.

| Name                | Type | Value               |
| :------------------ | :--- | :------------------ |
| \_dmarc.example.com | TXT  | "v=DMARC1;p=reject" |

> 📘 DMARC Policies
> 
> In the above example, the "p" (policy) value has been set to "reject". There are 3 policies that can be applied depending on your preference.
> 
> - p=none: This tells inbox providers to take no specific action on emails that fail authentication. They will most likely be delivered unless it is very obviously spam. A p=none DMARC policy leaves the decision up to inbox providers.
> - p=quarantine: This policy informs inbox providers to send emails that fail authentication to spam or junk folders. These messages may also be blocked.
> - p=reject: This is the strongest DMARC policy value. If a message fails DMARC when set to “reject” will, it not be delivered at all.

### Complying with DMARC through DKIM

For an email to comply with DMARC based on DKIM, both of the following conditions must be met:

- The message must have a valid DKIM signature.
- The From address in the email header must align with the domain in the DKIM signature. 
  - If the domain's DMARC policy specifies strict alignment for DKIM, these domains must match exactly. **This is our standard setup.**
  - If the domain's DMARC policy specifies relaxed alignment for DKIM, the domain can be a subdomain of the From domain. 

To comply with these requirements, complete the following steps:

1. Set up DKIM by following the [DKIM instructions](https://help.webexconnect.io/docs/best-practices-to-improve-email-deliverability#set-up-dkim-to-protect-your-domain-against-spoofing).

### Complying with DMARC through SPF

For an email to comply with DMARC based on SPF, both of the following conditions must be met:

- The email must pass an SPF check.
- The domain in the From address of the email header must align with the MAIL FROM domain that the sending mail server specifies to the receiving mail server. 
  - If the domain's DMARC policy for SPF specifies strict alignment, the From and MAIL FROM domains must match exactly. 
  - If the domain's DMARC policy for SPF specifies relaxed alignment, the MAIL FROM domain can be a subdomain of the domain in the From header. **This is our recommended setup.**

To comply with these requirements, complete the following steps:

1. Set up a custom MAIL FROM domain by completing the steps in the [custom MAIL FROM domain guide](https://help.webexconnect.io/docs/best-practices-to-improve-email-deliverability#add-custom-mail-from-domain).
2. Ensure that your sending domain uses a **relaxed** policy for SPF. If you haven't changed your domain's policy alignment, it uses a relaxed policy by default.

### Add Custom MAIL FROM domain

Emails that are sent through Amazon SES automatically use a subdomain of amazonses.com as the default MAIL FROM domain. Sender Policy Framework (SPF) authentication successfully validates these messages because the default MAIL FROM domain matches the application that sent the email—in this case, SES. However, if you don't want to have the SES default MAIL FROM domain and would rather use a subdomain of a domain that you own, you can do so by configuring a custom MAIL FROM domain. We do recommend this as a best practice. 

To do this, it requires you to publish your own SPF record for your custom MAIL FROM domain. In addition, SES also requires you to set up an MX record so that your domain can receive the bounce and complaint notifications that email providers send you.



![An email received without a Custom MAIL FROM configured (see "mailed-by" field)](https://files.readme.io/e8920bbef037fc950691039e6504e0ed69cb60b959f71f7b37e0a9c38133464c-email_domain_1.png)






![An email received with a Custom MAIL FROM configured (see "mailed-by" field)

| Name                               | Type | Value                                    |
| :--------------------------------- | :--- | :--------------------------------------- |
| customMAILFROMsubdomain.domain.com | MX   | 10 feedback-smtp.eu-west-2.amazonses.com |](https://files.readme.io/dc1a53756a572c0b054e52f5fa7b61630994c6e6dc82b0fc99999280dc9446ef-email_domain_2.png)




The example in the table below creates an SPF record that allows IP addresses from Amazon SES (our email gateway) to send emails from your subdomain and pass inbox provider's SPF checks.

| Mail From Domain Name              | Type | Example Value                       |
| :--------------------------------- | :--- | :---------------------------------- |
| customMAILFROMsubdomain.domain.com | TXT  | "v=spf1 include:amazonses.com -all" |

If you want to specify individual IP addresses, you can amend the record as displayed in the table below. Having your SPF record configured like this means that only emails sent from servers with the specified IP addresses will pass inbox providers' SPF check.

| Mail From Domain Name              | Type | Example Value                 |
| :--------------------------------- | :--- | :---------------------------- |
| customMAILFROMsubdomain.domain.com | TXT  | "v=spf1 ip4:192.168.0.1 -all" |

<br />

> 📘 Custom MAIL FROM domain requirements
> 
> The subdomain you use for your MAIL FROM domain has to meet the following requirements:
> 
> - The MAIL FROM domain has to be a **subdomain of the verified identity (email address or domain) that you send email from**. For example, mail.example.com is a valid MAIL FROM domain for the domain example.com.
> - The MAIL FROM domain shouldn't be a domain that you send email from. If you have to use the MAIL FROM domain in a From address, there are some additional considerations and you will need to speak to us.
> - The MAIL FROM domain shouldn't be a domain that you use to receive email.

> 🚧 MX Record
> 
> The number 10 listed along with the MX value is the preference order for the mail server, and will need to be entered into a separate value field, as specified by your DNS provider's GUI.

### Reverse DNS and Pointer Records (PTR)

A reverse DNS lookup is the opposite of a DNS lookup. A DNS lookup matches a domain name to an IP address. A reverse DNS lookup starts with the IP address and looks up the domain name. A PTR record is the inverse record of both A records for IPv4 addresses, and AAAA records for IPv6 addresses. Gmail recommends businesses to set-up a valid reverse DNS record to ensure that the IP address they are sending emails from points back to their domain. On this, if a client currently sends email from a shared IP address (A shared IP address is an IP address used by more than one email sender. The activity of any senders using a shared IP address affects the reputation of all senders for that shared IP.), the best practices to be followed include:

- Ensuring that the shared IP address isn’t on any internet blocklist. Messages sent from IP addresses on a blocklist are more likely to be marked as spam.
- If you use an email service provider for your shared IP, use Postmaster Tools to monitor the reputation of the shared IP address.

Given that a shared IP can be in use by multiple email senders, reverse DNS configuration makes sense in the case of dedicated IPs. When one creates a new Amazon SES account, by default the emails are sent from IP addresses that are shared with other SES users. However, clients can also use dedicated IP addresses that are reserved for their exclusive use by leasing them at an additional cost. Please note, Amazon SES does not allow users to specify custom reverse DNS for dedicated IPs. These IPs come pre-configured with proper AWS RDNS on them which should be sufficient and will not cause any delivery issues.

> 📘 Dedicated IPs
> 
> If you have opted for Email via AWS SES, you can request dedicated IPs through Webex Connect support team (refer to the details available within Contact Us page in your Webex Connect account). At least 2 dedicated IPs are recommended to avoid service disruptions. Each dedicated IP has a limit of 40 TPS (Transactions per Second), i.e., if you have 2 dedicated IPs, you can send emails at 80 TPS, provided that the TPS set on Webex Connect for the asset-tenant combination is at least 80.  
> When new dedicated IPs are enabled, AWS SES automatically warms them up by gradually scaling up the traffic on to these dedicated IPs from the erstwhile shared IPs or existing dedicated IPs.

## Provide easy unsubscribe options

As is always recommended, you should send emails to your customers only after taking consent from them to send them communications for the concerned purpose. Further, it’s a well-established best practice and recommendation that you should provide an easy way to recipients to unsubscribe from such communications. 

We already offer the ability to include unsubscribe URLs as part of the emails sent from Webex Connect (using AWS SES). To enable this feature, you are required to enable this at the email app asset level and then include relevant tags as part of your email HTML content. 

For businesses that sent more than 5000 emails per day to Gmail email ids, marketing and subscription i.e., opt-in-based email messages must support a one-click unsubscribe option. To set-up one-click unsubscribe, the headers of the emails in the outgoing messages must include the following tags:

- List-Unsubscribe-Post
- List-Unsubscribe

We are making an enhancement as part of Webex Connect v6.4.2 to support this configuration. You would be able to enable this at an email sender id level from Email app configuration page.

## Ensure you’re sending solicited emails.

This apart, Gmail recommends the following best practices that we highly encourage clients to follow:

- Make sure recipients opt in to get messages from you. 
- Periodically send messages to confirm that recipients want to stay subscribed. 
- Consider unsubscribing recipients who don't open or read your messages. 
- Automatically unsubscribe recipients who have multiple bounced messages.
- Messages of the same category should have the same From: email address. For example, messages from a domain called solarmora.com might have From: addresses like:
  - Account notification messages: [alert@domain.tld](mailto:alert@solarmora.com)
  - Sales receipt messages: [sales@domain.tld](mailto:sales@solarmora.com) 

Finally, businesses should keep spam rates reported in Postmaster Tools below 0.10% and avoid ever reaching a spam rate of 0.30% or higher.

You can track your email sending reputation for Gmail by using Google Postmaster Tools. Refer to [Google support](https://support.google.com/mail/answer/9981691?visit_id=638379471326190846-500514752&rd=1) article that explains how you can set-up your account, confirm ownership of your domain with Google Postmaster and keep a track of your spam rate.

## Errors in case of not meeting the minimum authentication requirements

To avoid email delivery issues, you are required to fulfill the minimum authentication requirements outlined on this page. Messages that fail to authenticate through these methods may be flagged as spam or rejected with a 7520 error.

The following error information can be found in the additionalInfo of the [Outbound Webhook Notifications](https://developers.imiconnect.io/reference/email-outbound-webhooks#outbound-webhook-configuration-for-tracking-email-delivery-status) for bounced email.

Error Details in additionalInfo can be in-line with one of the following:

- 5.7.26|failed|smtp; 550-5.7.26 This mail has been blocked because the sender is unauthenticated. Gmail requires all senders to authenticate with either SPF or DKIM. Authentication results: DKIM = did not pass SPF [domain-name] with ip: [ip-address] = did not pass. For instructions on setting up authentication, go to [Email sender guidelines](https://help.imiconnect.io/docs/best-practices-to-improve-email-deliverability).
- 5.7.26|failed|smtp; 550-5.7.26 The MAIL FROM domain [domain-name] has an SPF record with a hard fail policy (-all) but it fails to pass SPF checks with the ip: [ip-address]. To best protect our users from spam and phishing, the message has been blocked. For more information, go to [Email sender guidelines](https://help.imiconnect.io/docs/best-practices-to-improve-email-deliverability).
- 5.7.26|failed|smtp; 550-5.7.26 Unauthenticated email from domain-name is not accepted due to domain's DMARC policy. Contact the administrator of domain-name domain if this was legitimate mail. To learn about the DMARC initiative, go to [Control unauthenticated mail from your domain](https://help.imiconnect.io/docs/best-practices-to-improve-email-deliverability).
- 5.7.515|failed|smtp; 550-5.7.515 Access denied, sending domain [SendingDomain] does  
  not meet the required authentication level.