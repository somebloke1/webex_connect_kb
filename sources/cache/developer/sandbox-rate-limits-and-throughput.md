# Sandbox Rate Limits and Throughput

Source: https://developers.webexconnect.io/reference/sandbox-rate-limits-and-throughput
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:40+00:00

Please note that the following throughput limits apply to various APIs and Webhooks available as part of Webex Connect Sandbox mode.

**Communication APIs** 

  * You can make a maximum of one API call every second to each of the SMS, Voice, and WhatsApp API individually. 
  * Apart from this, there is a lifetime usage limit of 10000 outbound messages on SMS and WhatsApp channels, and 5000 inbound and 5000 outbound calls on voice. 
  
**Custom Event API and Inbound Webhooks**

You can make a maximum of one API call every second to custom event API or inbound webhooks. This is an aggregate limit that applies to all your Webex Connect custom event APIs or inbound webhooks. A maximum of 2500 calls can be made to custom event API or inbound webhooks within a month.

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
  "params": []
}
```
