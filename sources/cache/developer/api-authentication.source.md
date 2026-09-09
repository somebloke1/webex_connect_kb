## Authentication options for Webex Connect APIs and Webhooks

All requests to the <<prodname>> APIs and Webhooks are authenticated using either a key or JSON Web Tokens (JWT). Here are the authentication details for various APIs offered by <<prodname>>. 

> 📘 Note
> 
> If you are looking for Authentication details for Webex Connect Sandbox APIs, please refer to [Sandbox APIs Overview](https://developers.imiconnect.io/reference#sandbox-apis-overview).

[block:parameters]
{
  "data": {
    "h-0": "API / Webhooks",
    "h-1": "Authentication Types Supported",
    "0-0": "Messaging API (v1 and v2)",
    "0-1": "1. Service Key\n2. Service Specific JWT Tokens  \n   (Refer to know how you can access [Service Keys and Jason Web Tokens for a Service](https://help.imiconnect.io/docs/api-settings)  in <<prodname>>).",
    "1-0": "Custom Event API v1",
    "1-1": "1. Service Key\n2. Service Specific JWT Tokens",
    "2-0": "Inbound Webhooks",
    "2-1": "1. Service Key\n2. Service Specific JWT Tokens",
    "3-0": "Contact Policy APIs",
    "3-1": "Profile Key (Available under Tenant Settings page. Refer to [Profile Key](https://help.imiconnect.io/docs/tenant-settings#profile-key) for more info.)",
    "4-0": "RCS Capability Lookup API",
    "4-1": "1. Service Key\n2. Service Specific JWT Tokens",
    "5-0": "Profile API v2",
    "5-1": "Profile Key (Available under Tenant Settings page)",
    "6-0": "Thread APIs",
    "6-1": "JWT Tokens (Refer [JWT Set-up Tutorial](https://developers.imiconnect.io/docs/jwt-setup-validation) in SDK Docs)",
    "7-0": "Segment APIs",
    "7-1": "JWT Tokens (Refer [JWT Set-up Tutorial](https://developers.imiconnect.io/docs/jwt-setup-validation) in SDK Docs)",
    "8-0": "Topic APIs",
    "8-1": "JWT Tokens (Refer [JWT Set-up Tutorial](https://developers.imiconnect.io/docs/jwt-setup-validation) in SDK Docs)",
    "9-0": "User Audit Logs API",
    "9-1": "Cisco Webex Common Identity (CI) (Refer [Webex Contact Center Authentication](https://developer.webex.com/webex-contact-center/docs/authentication-cc))"
  },
  "cols": 2,
  "rows": 10,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 🚧 Authentication Best Practice
> 
> You can use either Service Key or JSON Web Tokens (JWT) for authentication when using Messaging APIs, Custom Event API v1, inbound webhooks, and other APIs mentioned above. If you use both JWT authentication and Service Key in an API request, JWT authentication takes priority, and the Service Key is ignored.

## Rotating API Authentication Credentials

We encourage you to rotate your API credentials (Service Key and/or JWT tokens) periodically to strengthen your security posture and prevent unauthorised access. Refer to [Rotating authentication credentials periodically](https://help.imiconnect.io/docs/api-settings#rotating-authentication-credentials-periodically) to understand how you can create a new Service Key / JWT credentials and discard existing ones as per security best practices.

## IP Allowlisting for APIs and Webhooks

Additionally, <<prodname>> supports IP Address Allowlisting to validate the request source for supported APIs and inbound webhooks. Tenant Owners can add valid IPv4 addresses or CIDR ranges from [Tenant Settings](https://help.webexconnect.io/v6.20.0/docs/tenant-settings).

When IP addresses or CIDR ranges are configured, API traffic for the tenant is restricted to those entries only. Requests that do not originate from the configured entries are rejected.