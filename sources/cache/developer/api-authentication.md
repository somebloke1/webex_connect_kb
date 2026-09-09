# API Authentication

Source: https://developers.webexconnect.io/reference/api-authentication
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:39+00:00

## Authentication options for Webex Connect APIs and Webhooks

All requests to the Webex Connect APIs and Webhooks are authenticated using either a key or JSON Web Tokens (JWT). Here are the authentication details for various APIs offered by Webex Connect. 

> 📘 Note
> 
> If you are looking for Authentication details for Webex Connect Sandbox APIs, please refer to [Sandbox APIs Overview](https://developers.imiconnect.io/reference#sandbox-apis-overview).



| API / Webhooks | Authentication Types Supported |
| --- | --- |
| Messaging API (v1 and v2) | 1. Service Key<br>2. Service Specific JWT Tokens  <br>   (Refer to know how you can access [Service Keys and Jason Web Tokens for a Service](https://help.imiconnect.io/docs/api-settings)  in Webex Connect). |
| Custom Event API v1 | 1. Service Key<br>2. Service Specific JWT Tokens |
| Inbound Webhooks | 1. Service Key<br>2. Service Specific JWT Tokens |
| Contact Policy APIs | Profile Key (Available under Tenant Settings page. Refer to [Profile Key](https://help.imiconnect.io/docs/tenant-settings#profile-key) for more info.) |
| RCS Capability Lookup API | 1. Service Key<br>2. Service Specific JWT Tokens |
| Profile API v2 | Profile Key (Available under Tenant Settings page) |
| Thread APIs | JWT Tokens (Refer [JWT Set-up Tutorial](https://developers.imiconnect.io/docs/jwt-setup-validation) in SDK Docs) |
| Segment APIs | JWT Tokens (Refer [JWT Set-up Tutorial](https://developers.imiconnect.io/docs/jwt-setup-validation) in SDK Docs) |
| Topic APIs | JWT Tokens (Refer [JWT Set-up Tutorial](https://developers.imiconnect.io/docs/jwt-setup-validation) in SDK Docs) |
| User Audit Logs API | Cisco Webex Common Identity (CI) (Refer [Webex Contact Center Authentication](https://developer.webex.com/webex-contact-center/docs/authentication-cc)) |




> 🚧 Authentication Best Practice
> 
> You can use either Service Key or JSON Web Tokens (JWT) for authentication when using Messaging APIs, Custom Event API v1, inbound webhooks, and other APIs mentioned above. If you use both JWT authentication and Service Key in an API request, JWT authentication takes priority, and the Service Key is ignored.

## Rotating API Authentication Credentials

We encourage you to rotate your API credentials (Service Key and/or JWT tokens) periodically to strengthen your security posture and prevent unauthorised access. Refer to [Rotating authentication credentials periodically](https://help.imiconnect.io/docs/api-settings#rotating-authentication-credentials-periodically) to understand how you can create a new Service Key / JWT credentials and discard existing ones as per security best practices.

## IP Allowlisting for APIs and Webhooks

Additionally, Webex Connect supports IP Address Allowlisting to validate the request source for supported APIs and inbound webhooks. Tenant Owners can add valid IPv4 addresses or CIDR ranges from [Tenant Settings](https://help.webexconnect.io/v6.20.0/docs/tenant-settings).

When IP addresses or CIDR ranges are configured, API traffic for the tenant is restricted to those entries only. Requests that do not originate from the configured entries are rejected.

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [],
  "examples": {
    "codes": []
  }
}
```
