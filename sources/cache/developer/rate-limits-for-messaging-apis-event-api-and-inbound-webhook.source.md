<<prodname>> is used by a large number of users to automate millions of customer interactions every day. We implement certain limits on the number of requests that can be made to various <<prodname>> APIs to provide you with a reliable and scalable experience that you can rely on.

There is a limit to the maximum number of requests you can make within a second to the following APIs and Webhooks:

**Messaging API** - A single rate limit applies to the usage of Messaging API v1 and v2. E.g., if the Messaging API rate limit, configured for your account is 20 per second, you can make 20 API calls per second to Messaging API v1, or you can make 20 API calls per second to Messaging API v2, or 10 API calls per second to each of Messaging API v1 and v2. In addition to the Messaging API Transaction Per Second (TPS) limit, we have channel-level TPS that applies for the specific channel. It limits the number of requests allowed per channel, ensuring that the channel-level TPS does not exceed the overall Messaging API TPS limit.

- **Burst Mode**  
  The burst mode enables tenants to temporarily exceed their subscribed Messaging API TPS limits by up to 1.5 times their provisioned TPS, with a maximum additional allowance of 100 TPS. This can be utilized for a total of 30 minutes (1,800 seconds) per day, which does not need to be used continuously but can be spread across multiple intervals. Additionally, tenants have a cumulative usage limit of up to 8 hours per month, which resets at the beginning of each calendar month. Any requests surpassing these limits will be rejected. Unused burst mode capacity in a given month does not carry over to the following month.  
  For example, if a client’s Messaging API TPS is 100, they are permitted to use 150 TPS for up to 30 minutes per day and 8 hours in total per month. If the client's messaging limit is 300, then they are permitted to use up to 400 TPS instead of 450 TPS (as the 100 TPS threshold is reached).  
  Along with the Messaging API TPS limit, the channel-level TPS limit will also be increased by up to 1.5x (subject to the 100 TPS threshold), with duration limits applied. Requests sent in burst mode will be queued and processed at the normal TPS rate.

> 📘 Note
> 
> The supported channels for burst TPS capability on the Messaging API include SMS, MMS, RCS, Voice, Email, and WhatsApp.
> 
> The requests from the event scheduler are not permitted to exceed the configured Messaging API TPS limit and will be rejected once the messaging threshold has been reached.

**Custom Event API and Inbound Webhook** - A separate but shared rate limit applies to the usage of Custom Event API v1 and inbound webhook.

**Burst Mode**-The burst mode enables tenants to temporarily exceed their subscribed Custom Event API TPS limits by up to 1.5 times their provisioned TPS, with a maximum additional allowance of 100 TPS.  
The requests sent in burst mode are queued and processed at the normal TPS rate.

** Profile API**—Profile API has a separate rate limit.

When <<prodname>> receives API calls or inbound webhook requests from your applications, these requests are queued for processing until the rate of requests is within the configured rate limit. If you exceed the rate limit, the requests are rejected with 7020, i.e., 'You have reached the maximum transaction limit, error code.

These limits are applied at a tenant level.

## How can I increase the Rate Limits for my account

The limits are configurable and can be increased based on your requirements. Please get in touch with your account manager in case you want to increase the API rate limits.

## Rate Limit for Thread APIs

The following are the default TPS values for Thread APIs.

| API Name                                                | Default TPS at Tenant Level                                            |
| :------------------------------------------------------ | :--------------------------------------------------------------------- |
| Get App Threads                                         | For existing tenants unlimited and default value for new tenants - 10  |
| Get User Threads (with and without unread thread count) | For existing tenants unlimited and default value for new tenants -10   |
| Get User Messages all versions                          | For existing tenants unlimited and default value for new tenants -100  |
| Delete User Messages (all versions)                     | For existing tenants unlimited and default value for new tenants - 100 |

## Segment Messaging APIs

The following are the default TPS values for processing Segment and Topic Messaging API requests.

| API Name              | Default TPS at Tenant Level          |
| :-------------------- | :----------------------------------- |
| Topics and Segments   | Default processing rate to be 30 TPS |
| Topic Messaging API   | Default value 30                     |
| Segment Messaging API | Default value 30                     |