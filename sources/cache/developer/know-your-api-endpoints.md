# Know Your API Endpoints

Source: https://developers.webexconnect.io/reference/know-your-api-endpoints
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:39+00:00

Webex Connect API endpoints for your account depend on the region your Webex Connect account is hosted in. Here's a brief list to help you select the relevant API endpoints:

> 📘 
> 
> We added new API endpoints from v6.0 onwards and recommend you to use the new endpoints preferably. However, there is no impact on functioning of old endpoints, and they continue to work as well.

New API endpoints: 

| Region      | Your Tenant Domain             | Endpoint for Messaging, Voice, RCS, Event, and Profile APIs | Contact Policy APIs               | Audit Logs API      | Thread, Segment, and Topic APIs |
| :---------- | :----------------------------- | :---------------------------------------------------------- | :-------------------------------- | :------------------ | :------------------------------ |
| AWS Canada  | tenantname.ca.webexconnect.io  | api.ca.webexconnect.io                                      | contactpolicy.ca.webexconnect.io  | ca.webexconnect.io  | rtm.ca.webexconnect.io          |
| AWS Ireland | tenantname.eu.webexconnect.io  | api.eu.webexconnect.io                                      | contactpolicy.eu.webexconnect.io  | eu.webexconnect.io  | rtm.eu.webexconnect.io          |
| AWS London  | tenantname.uk.webexconnect.io  | api.uk.webexconnect.io                                      | contactpolicy.uk.webexconnect.io  | uk.webexconnect.io  | rtm.uk.webexconnect.io          |
| AWS Oregon  | tenantname.us.webexconnect.io  | api.us.webexconnect.io                                      | contactpolicy.us.webexconnect.io  | us.webexconnect.io  | rtm.us.webexconnect.io          |
| USA (Azure) | tenantname.us1.webexconnect.io | api.us1.webexconnect.io                                     | contactpolicy.us1.webexconnect.io | us1.webexconnect.io | rtm.us1.webexconnect.io         |
| AWS Mumbai  | tenantname.in.webexconnect.io  | api.in.webexconnect.io                                      | contactpolicy.in.webexconnect.io  | in.webexconnect.io  | rtm.in.webexconnect.io          |
| AWS Sydney  | tenantname.au.webexconnect.io  | api.au.webexconnect.io                                      | contactpolicy.au.webexconnect.io  | au.webexconnect.io  | rtm.au.webexconnect.io          |

Existing APIs (these APIs will continue to work for existing tenants): 

| Region/Country       | Your Tenant Domain        | Endpoint for Messaging, Voice, Event, Profile APIs, and Contact Policy                                   | Contact Policy APIs            | Thread, Segment, and Topic APIs |
| :------------------- | :------------------------ | :------------------------------------------------------------------------------------------------------- | :----------------------------- | :------------------------------ |
| Canada               | tenantname.imiconnect.ca  | api.imiconnect.ca                                                                                        | contactpolicy.imiconnect.ca    | rtm.imiconnect.ca               |
| EMEA                 | tenantname.imiconnect.io  | api.imiconnect.io                                                                                        | contactpolicy.imiconnect.io    | rtm.imiconnect.io               |
| UK                   | tenantname.imiconnect.eu  | api.imiconnect.eu                                                                                        | contactpolicy.imiconnect.eu    | rtm.imiconnect.eu               |
| USA (AWS)            | tenantname.imiconnect.io  | api-us.imiconnect.io                                                                                     | contactpolicy-us.imiconnect.io | rtm-us.imiconnect.io            |
| USA (Azure)          | tenantname.imiconnect.us  | api.imiconnect.us                                                                                        | contactpolicy.imiconnect.us    | rtm.imiconnect.us               |
| APAC                 | tenantname.imiconnect.in  | api.imiconnect.in                                                                                        | contactpolicy.imiconnect.in    | rtm.imiconnect.in               |
| \--                  | tenantname.imiconnect.com | api.imiconnect.com                                                                                       | contactpolicy.imiconnect.com   | rtmapp.imiconnect.com           |
| Webex Connect Sandbox | Sandbox.imiconnect.io     | Refer [sandbox specific API](https://developers.imiconnect.io/reference#sandbox-apis-overview) reference | Not available in Sandbox       | Not available in Sandbox        |

> 📘 Contact Policy APIs
> 
> Contact Policy APIs can be used only after the Contact Policy App has been enabled for your tenant. Please get in touch with the support team if you want to use this feature.

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "results": {
    "codes": [
      {
        "status": 200,
        "language": "json",
        "code": "{}",
        "name": ""
      },
      {
        "status": 400,
        "language": "json",
        "code": "{}",
        "name": ""
      }
    ]
  },
  "auth": "required",
  "params": [],
  "url": "",
  "method": "get",
  "examples": {
    "codes": []
  }
}
```
