BIMI is an email specification that allows email clients to display a brand's logo next to authenticated emails. Logos used with BIMI are verified by a third party, so recipients can be sure logos in their inbox are legitimate. The third-party certification must be a Verified Mark Certificate (VMC) or a Common Mark Certificate (CMC).

## Prerequisites

To use BIMI while sending emails through Webex Connect, you need the following: 

- To have an SVG file of your logo
- A VMC or CMC for your domain from a third-party certificate authority
- To have DMARC set up for your domain

## SVG file of your logo

Logos used with BIMI must be in Scalable Vector Graphics (SVG) file format. SVG is an open-standard image format that can display your logo at different resolutions. When you apply for a VMC or CMC, you must submit your logo in SVG format.

### BIMI standard requirements for SVG files

This section summarizes BIMI standard requirements for SVG files. For the complete list of requirements, go to [section 5.2 of the BIMI standard](https://datatracker.ietf.org/doc/html/rfc6170#section-5.2).

The SVG file should not include: 

- External links or references (other than to the specified XML namespaces)
- Scripts
- Animations or other interactive elements
- The x= or y= attributes in the <svg> root element

| SVG file attribute    | Value                                                                                                   |
| :-------------------- | :------------------------------------------------------------------------------------------------------ |
| File format           | SVG Tiny Portable/Secure (SVG Tiny PS), a version of SVG. Learn more                                    |
| baseProfile attribute | tiny-ps                                                                                                 |
| version attribute     | 1.2                                                                                                     |
| <title> element       | There are no strict requirements, but we recommend using a value that reflects your organization’s name |

## VMC or CMC for your domain

Most of the email clients support BIMI only with PEM files that include certified SVG file. To procure the certificate, you need to follow the below instructions: 

- Submit your trademarked logo in SVG format and request a VMC or CMC from one of the certificate authorities (CA) listed in [Mark Certificate Issuers](https://bimigroup.org/vmc-issuers/).
- When your VMC or CMC is issued, you'll receive an entity certificate PEM file. Your SVG file (logo) and VMC/CMC are embedded in the PEM file.
- Get any intermediate CA certificates and root CA certificates from the CA and append them to the PEM file in the order issued. Typically, the order is: Entity certificate, any intermediate CA certificate, root CA certificate.
- Upload the PEM file (including all appended files) to a (preferably your domain’s) public web server.
- Copy the PEM file URL because you'll include it in your BIMI assertion TXT record in the next step. Example PEM file URL: `<https://images.domain.tld/brand/certificate.pem>`

## DMARC Setup

For using BIMI, you need to make sure that your domain has DMARC set up, and for DMARC, you would need either SPF or DKIM set up. However, it’s highly recommended that both SPF and DKIM records are set up since some email service providers (ESPs) require both when using BIMI. 

To configure DKIM, if you haven’t done already, please enable the DKIM Settings in your Webex Connect Email App Asset Configuration Page and update your domain’s DNS records using the information displayed in app asset configuration page. 

The (Sender Policy Framework) SPF authentication, when using AWS SES, if you are using the default MAIL FROM domain, is already configured by AWS SES. However, if you use custom MAIL FROM domain, you can configure SPF by following [the guidelines](https://help.webexconnect.io/docs/best-practices-to-improve-email-deliverability#add-custom-mail-from-domain).

## Add a BIMI TXT record

To turn on BIMI for your domain, you need to add a BIMI assertion TXT record at your domain provider. After you add the record, it can take up to 48 hours for your logo to show in recipients’ mailboxes.  

If you're using a PEM file that contains your logo, your TXT record will look like this example: 

`v=BIMI1;l=;a=https://images.domain.tld/brand/certificate.pem`