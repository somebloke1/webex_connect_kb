# Configuring Branded Mail in Apple Business Connect

Source: https://help.webexconnect.io/docs/configuring-branded-mail-in-apple-business-connect
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:02+00:00

## Overview

Branded Mail allows businesses to add their logo and brand name to emails sent from their domain. This feature helps build brand identity, increase trust, and make emails stand out in the Mail app on Apple devices and iCloud Mail on the web. 

You can configure Branded Mail in Apple Business Connect by following the detailed instructions mentioned in subsequent sections.

## Prerequisites

Before you set up Branded Mail, some of the important points to consider are: 

1. The company must own the logo.
2. The email domain name must be a commercial name.
3. The company must be verified by Apple.
4. The mail server must meet [DMARC requirements](https://help.webexconnect.io/docs/best-practices-to-improve-email-deliverability#set-up-a-dmarc-policy).

## Domain Structure

Branded Mail can be set up at one of the following levels: 

- Domain and subdomains. e.g., domain.tld or subdomain.domain.tld
- Subdomain only. e.g., subdomain.domain.tld
- Specific email address. e.g., [mailid@domain.tld](mailto:mailid@domain.tld)

> 📘 
> 
> After adding a domain on Apple Business Connect and generating TXT record, the domain must be verified within 14 calendar days.

## Set up Branded Mail in Apple Business Connect

Configure Branded Mail by signing in to Apple Business Connect with an Administrator role, add your domain or email address, and verify your company as mentioned in [Configure your brand email](https://support.apple.com/en-gb/guide/apple-business-connect/abcb28ad2a2d/1.0/web/1.0). 

Also, you can add, review, or remove Domain or Email Address for which you are setting up Branded Mail by following the instructions specified in [Configure your brand email](https://support.apple.com/en-gb/guide/apple-business-connect/abcb28ad2a2d/1.0/web/1.0).

## Verify Domain for Branded Mail in Apple Business Connect

To verify your domain for Branded Mail, you should copy the TXT record generated in Apple Business Connect into your domain’s DNS zone file and initiate verification as mentioned in [Verify your domain for Branded Mail in Apple Business Connect](https://support.apple.com/en-gb/guide/apple-business-connect/abcbed57e96d/1.0/web/1.0).