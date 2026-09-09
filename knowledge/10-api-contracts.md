# External APIs, event contracts, and webhooks

This chapter is a contract reference for software that invokes or accompanies a Connect flow. **Documented** statements come from the locally captured Cisco reference, documentation version 6.20.0, retrieved 2026-09-08. They establish published behavior, not this tenant's enabled features or a successful live API test. **Engineering recommendations** are implementation choices. Keep the installed node configuration and exact API version in the flow handoff.

## Choose the correct boundary

| Boundary | Purpose |
| --- | --- |
| External application → Messaging/Voice API | Request communication directly. |
| External application → Custom Event/inbound webhook | Supply an event that an associated flow/rule processes. |
| Connect → external callback | Report message progress or forward an incoming event. |
| Application → Profile/Contact Policy API | Manage identity attributes or communication preferences. |

These API families perform different jobs; their existence does not establish a flow-authoring or deployment API. Most communication APIs acknowledge acceptance before reporting subsequent processing through callbacks. [API overview](https://developers.webexconnect.io/reference/apioverview).

**Engineering recommendation:** decide which system owns orchestration before implementing an API sender. Record the entry event, owning service, flow/rule association, business identifier, outbound side effects, and completion evidence. See [flow lifecycle](02-flow-lifecycle.md) for authoring and publication, and [integrations](06-integrations-and-contact-center.md) for calls made from nodes.

## Endpoint and authentication matrix

**Documented regional hosts:** for new-domain tenants, regions are `ca`, `eu`, `uk`, `us`, `us1`, `in`, and `au`. `us` is AWS Oregon; `us1` is Azure USA. Select the matching region; never substitute the portal hostname for the API hostname.

| Family | Regional host pattern |
| --- | --- |
| Messaging, Voice, RCS, Event, Profile | `api.<region>.webexconnect.io` |
| Contact Policy | `contactpolicy.<region>.webexconnect.io` |
| Threads, Segments, Topics | `rtm.<region>.webexconnect.io` |
| Audit logs | `<region>.webexconnect.io` |

Legacy `imiconnect` domains have a separate mapping; the Sandbox uses separate APIs. Contact Policy requires enablement. These are reference mappings, not verified current tenant endpoints. [Endpoint mapping](https://developers.webexconnect.io/reference/know-your-api-endpoints).

| API family | Documented credential |
| --- | --- |
| Messaging v1/v2; Custom Event v1; inbound webhook; RCS lookup | Service Key or service-specific JWT |
| Profile v2; Contact Policy | Tenant Profile Key |
| Thread; Segment; Topic | JWT under the SDK/conversation authentication setup |
| User audit logs | Webex Common Identity authentication |

For supported service APIs, JWT wins if both JWT and Service Key are supplied. Tenant IP allowlisting is an additional check: configured IPv4/CIDR entries restrict request origins. Do not reuse a service credential for Profile APIs merely because both use a key. [API authentication](https://developers.webexconnect.io/reference/api-authentication).

**Service JWT construction:** header `alg=HS256`; payload `iss` is Service ID and `iat` is integer Unix seconds. Base64-decode the Service Secret before signing. The documented lifetime is 60 minutes, so clients need regeneration. Obtain these values from the service's API settings; keep them out of examples, source control, transcripts, and logs. [JWT setup](https://developers.webexconnect.io/reference/using-jwt-for-api-authentication).

## Custom Event v1: structured business trigger

**Documented:** `POST /resources/v1/events/externalevent/` on the regional API host, JSON body. Headers: `Content-Type: application/json`; Service Key in `key`, or service JWT through `Authorization`.

| Field | Contract |
| --- | --- |
| `events` | Required nonempty array; examples contain event objects. |
| `events[].evtid` | Required generated event ID. |
| `events[].correlationid` | Optional string, maximum 50 bytes. |
| `events[].parameters` | Optional object; configured required parameters must exist. |
| `expiry` | Optional UTC expiry. |
| `notifyurl` | Optional callback override for service URL. |

Syntactically valid example; replace placeholders and match the configured event schema:

```json
{
  "events": [
    {
      "evtid": "<EVENT_ID>",
      "correlationid": "<BUSINESS_REQUEST_ID>",
      "parameters": {
        "requestId": "<REQUEST_ID>"
      }
    }
  ]
}
```

`1002` means queued, not completed. Errors: `7000` malformed JSON; `7001/7002` credentials; `7003` missing events; `7004` invalid values/empty array; `7005` internal failure; `7010` IP; `7019` expiry; `7020` capacity; `7025` missing custom parameters. Errors can accompany **HTTP 200**. Normalize `response` object/array; inspect every `code`, preserving `transid` and correlation. [Custom Event v1](https://developers.webexconnect.io/reference/custom-event-v1).

**Documented configuration trap:** save the event to obtain `evtid`; the UI generates a payload matching its parameters. Use the credential belonging to the associated service/group: a different group's credential can produce acceptance without triggering the intended flow. [Custom Events configuration](https://help.webexconnect.io/docs/custom-events).

**Engineering recommendation:** `correlationid` is a tracking identifier, not a documented deduplication guarantee. Persist a separate business idempotency record before irreversible work. Test a duplicate, missing custom field, expired request, and accepted event with no matching consumer.

## Inbound webhook: preserve the caller's payload

**Documented:** use the generated endpoint. JSON/XML is parsed through JPath/XPath into available variables; current integrations use dot notation, such as `employee.name`. Older integrations may retain underscore aliases. An unassociated endpoint can accept/queue requests without executing a flow/rule.

Authentication uses credentials from the associated service when enabled. Signature validation adds SHA-256/SHA-512 support; signature failure returns HTTP 400. Relevant application codes: `7007` inactive service; `7008` invalid/unsaved endpoint; `7027` malformed XML; `7028` invalid signature; `7029` missing required signature.

**Source inconsistency:** this page says both Service Key and JWT use the `key` header, whereas the service JWT tutorial describes bearer authentication. Use `key` for the documented Service Key route. Validate the JWT header against the generated configuration before implementation; this chapter does not resolve that discrepancy by guessing. [Inbound webhook reference](https://developers.webexconnect.io/reference/inbound-webhooks).

Authentication is optional in the integration configuration but recommended by Cisco. Trigger filters support AND/OR and equality, membership, containment, prefix/suffix, regex, and case-insensitive comparisons. The documented default payload limit is **256 KB**, tenant-configurable; oversize rejection uses code `430`. The page does not identify that code as an HTTP status. [Inbound webhook configuration](https://help.webexconnect.io/docs/inbound-webhooks).

**Engineering recommendation:** retain raw body bytes when validating a signature; serialization can change signed content. Do not invent header names, prefix formats, canonicalization, or secret encoding from the algorithm name alone. Record those choices from the saved integration and test an altered body. Exercise nested objects, arrays, absent/null fields, XML namespaces, and exact trigger filtering before launch.

## Messaging API version contracts

### v1: established envelope

**Documented:** `POST /resources/v1/messaging`; `key: <SERVICE_KEY>` or `Authorization: Bearer <JWT>`, with JSON content type.

| Field | Contract |
| --- | --- |
| `deliverychannel` | Channel selector. |
| `destination` | Recipient array; channel identifiers inside. |
| `channels` | Channel-specific configuration. |
| `message.template`, `message.parameters` | Configured template and substitutions. |
| `correlationid` | Caller identifier, up to 50 bytes. |
| `notifyurl` | Request URL overrides service URL. |
| `callbackData` | Context returned with notifications. |
| `expiry` | UTC expiration. |

Channel blocks override base request/service defaults. Success example: HTTP 200 with `response[].code="1001"` and `transid`. Authentication/JSON failures also have HTTP 200 examples. [Send Message v1](https://developers.webexconnect.io/reference/send-message-v1).

Cisco discourages new SMS implementations on Send Message API v1. Its SMS-specific page contradicts itself: prose uses `/resources/v1/messaging`, while embedded OpenAPI uses `/resources/v1/messages`. Use the canonical v1 operation above for existing integrations; do not silently combine those paths. This discrepancy is not a tested server alias. [SMS through Messaging v1](https://developers.webexconnect.io/reference/send-message-api-v1).

### v2: explicit sender, recipients, and content

**Documented:** `POST /v2/messages`; service authentication headers match v1. The queued response example uses **HTTP 201**, `requestTimestamp`, `messageId`, `correlationId`, and `status`. A bad `sendAt` example uses HTTP 400 with `code="7004"` and `message`.

| Field | Contract |
| --- | --- |
| `channel`, `from`, `to` | Channel, sender, destination objects. |
| `to[].substitutions` | Override matching global `substitutions`. |
| `content` / `template` | Alternative content sources. |
| `sendAt` | UTC scheduling, up to seven days. |
| `expireAt` / `validity` | Mutually exclusive; validity is seconds. |
| `notifyUrl`, `notifyUrlAuthId` | Callback URL and configured authorization ID. |
| `callbackData` | Callback context, at most 2,000 characters. |
| `requestedReceipts` | Channel-dependent receipt filter. |

With `sendAt` plus `validity`, expiry is relative to scheduled time. Preserve v2 capitalization; generic sample snippets contain inconsistencies and are not universally runnable JSON. [Send Message v2](https://developers.webexconnect.io/reference/send-message-v2).

**SMS-specific contract:** required `channel="sms"`, `from`, `to[].msisdn[]`, and `content.type`/`content.text` unless using a template. Content types include `text` and `unicode`. Recipient numbers follow E.164; tenant `+E.164` enforcement applies to `to`, not `from`. Scheduling/expiry fields are optional in this channel reference, resolving the generic page's misleading mandatory labels for SMS. Receipt choices include `SUBMITTED`, `DELIVERED`, `FAILED`, and `CLICKED`; legacy `SENT` behaves as `SUBMITTED`. Click receipts require shortened-link tracking. [SMS through Messaging v2](https://developers.webexconnect.io/reference/send-sms-message-api-v2).

**Documented retrieval limitation:** `GET /v2/messages/<messageId>` requires the ID generated by v2. The reference marks access as beta/select-client. Do not promise polling availability. Its status is message state, not business completion. [Get Message v2](https://developers.webexconnect.io/reference/retrieve-message-v2).

## Callbacks and reconciliation

**Documented receiver contract:** HTTPS; URL registration expects HTTP 200 to HEAD, notifications use POST and expect HTTP 200. Timeout is ten seconds. Unreachable receivers have three retries at 60-second intervals, but many explicit HTTP response codes suppress retries; do not assume every non-200 retries. Delivery receipts are selected by service/channel; incoming events by number/app. Optional hub signing adds `x-hub-signature`; `x-wx-gtrid` is also documented. The page's fixed signature-length wording is internally inconsistent with its algorithms, so do not hard-code that length. [Outbound webhooks](https://developers.webexconnect.io/reference/outbound-webhooks-api-ref).

| SMS callback path | Meaning |
| --- | --- |
| `deliveryInfoNotification.transid` | Request transaction reference. |
| `.subtid` | Flow/node subtransaction where supplied. |
| `.correlationid`, `.callbackData` | Caller context. |
| `.deliveryInfo.deliveryStatus` | Submitted, Delivered, Failed, Un-Delivered, etc. |
| `.deliveryInfo.code`, `.deliveryInfo.Description` | Machine status and description. |
| `.deliveryInfo.timeStamp` | Event timestamp. |
| `.deliveryInfo.destination`, `.deliveryInfo.destinationType` | Recipient identity. |

Paths beginning with a dot continue under `deliveryInfoNotification`. SMS codes include `7500` delivery, `7501` submission, `7101` sender, `7102` address, `7107` length, `7208` expiry. Preserve raw casing; examples and prose field tables differ. These are SMS payloads, not a cross-channel universal schema. [SMS webhook schema](https://developers.webexconnect.io/reference/sms-outbound-webhooks).

**Engineering recommendation:** validate/authenticate, durably enqueue, then acknowledge promptly. Retain raw schema/version plus a normalized event. Deduplicate callbacks, tolerate late/out-of-order events, and link business request → API transaction/message → flow/node transaction → receipt. Keep acceptance, provider submission, delivery, customer reply, and completed business action as separate milestones. A missing callback is unknown state, not proof the send failed. See [operations](07-testing-and-operations.md).

## Profiles and contact policy

**Documented identity model:** App Profiles store channel/app registration details such as user/device ID and push tokens; their attributes are predefined. Customer Profiles can add business attributes and connect customer identity to App Profiles. A Customer Profile is not required merely to send push/in-app messages when registration data suffices. Profile API authentication uses the tenant Client Profile Key. [Profile overview](https://developers.webexconnect.io/reference/profile-api-overview).

| Customer Profile operation | Published contract and limits |
| --- | --- |
| Create | `POST /resources/v2/customerprofile`; examples use `Records[]` containing `customerId` and `Attributes`. Header parameter `key`. |
| Update | `PUT /resources/v2/customerprofile`; examples use the same `Records[]` shape. |
| Fetch | `GET /resources/v2/customerprofile/<customerID>`; response `Records[].Attributes[]` carries `Name`, `Value`, `ID`. |

Create's formal schema instead uses top-level `customerId`/lowercase `attributes`; this conflicts with its examples. `7012` indicates the 100-record batch limit; `7015` duplicate customer. Treat the examples as a candidate payload to validate, not a corrected authoritative schema. [Create profile](https://developers.webexconnect.io/reference/createprofile).

Update lists `1002` for partial batch success and `7014` for missing customer. Inspect `Results`, `SuccessCount`, and `FailureCount`, not only HTTP status. [Update profile](https://developers.webexconnect.io/reference/updateprofile).

Fetch documents a `secretKey` header, unlike create's `key`; its `showinwardlinks` parameter is marked as a path parameter absent from the displayed URL. Published values are `0` master only, `1` master plus app profiles, `2` full profile. Verify this operation's generated request before building an adapter. [Get profile](https://developers.webexconnect.io/reference/getprofile).

Profile completion lookup is `GET /resources/v2/profile/status/<transactionID>`, with `secretKey` in the reference. `1000` indicates success; `7600` can mean an invalid transaction or one still queued. [Profile status](https://developers.webexconnect.io/reference/get-profile-status). Customer deletion is `DELETE /resources/v2/customerprofile/<customerID>`; the page documents it as irreversible. [Delete profile](https://developers.webexconnect.io/reference/deleteprofile).

For App Profile adapters, use the cached operation-specific contracts: [create](../sources/cache/developer/createappprofile.md), [update](../sources/cache/developer/updateappprofile.md), [get by customer](../sources/cache/developer/getappprofile.md), [get by user](../sources/cache/developer/get-app-profile-by-user-id.md), and [delete device](../sources/cache/developer/delete-device-app-profile.md). These have distinct identifiers and additional schema/example inconsistencies; do not convert a Customer Profile request by changing only its URL.

**Documented policy boundary:** Contact Policy is not enabled on every tenant. Consent groups manage consent/preferences and daily/weekly/monthly contact limits. SMS/MMS/RCS share the Text category. **Flow Send nodes do not automatically apply policy preferences**: add explicit checks. WhatsApp consent records can use `alternateAddress` for BSUID and retain WAID where available. [Contact Policy](https://help.webexconnect.io/docs/contact-policy).

For direct SMS requests, optional `contactPolicy` contains `contactPolicyGroup`, `channelCheckConsent`, and `channelApplyFrequencyCap`. The group is required when a check is enabled; at least one check must be true; omitted booleans default false. This is an explicit request configuration, not automatic protection. [SMS v1 policy fields](https://developers.webexconnect.io/reference/send-message-api-v1).

| Policy code | Interpretation |
| --- | --- |
| `9000/9001` | Feature disabled / required inputs absent. |
| `9002/9010` | Consent absent / expired. |
| `9003/9005/9007` | Missing consumer / invalid group or channel / missing cap group. |
| `9004` | Policy service unavailable. |
| `9006` | Recipient frequency cap reached. |

Codes are API-family-specific: for example, general channel `7005` means expiry, while Custom Event `7005` means internal failure. Never use one global numeric-code dictionary without API/channel context. [Channel and policy status codes](https://developers.webexconnect.io/reference/channel-specific-status-codes).

**Engineering recommendation:** define the authoritative identity/consent store, purpose/group, identifier mapping, consent timestamps and expiry, and behavior when policy lookup fails. A missing consent record and a temporary policy outage require different dispositions; neither justifies blindly retrying a send. Establish retention/deletion separately from execution variables.

## Batching and capacity

**Documented:** Messaging can address up to 1,000 destinations per batch, further restricted by configured TPS. Cisco's example permits ten destinations when TPS is ten. A single request therefore is not a license to bypass destination limits. [Messaging batching](https://developers.webexconnect.io/reference/getting-started-with-your-messaging-api).

| Capacity pool | Relationship |
| --- | --- |
| Messaging v1 + v2 | Shared tenant limit; channel limits also apply. |
| Custom Event + inbound webhook | Separate shared tenant limit. |
| Profile | Separate limit. |

Burst permits up to `min(1.5 × provisioned TPS, provisioned TPS + 100)`. Messaging burst has 30 minutes/day and eight hours/month allowances; eligible channels are SMS, MMS, RCS, Voice, Email, WhatsApp. Burst requests still process at normal TPS. Event/webhook burst is also documented, but do not copy messaging's duration allowance without confirmation. Exceeding capacity returns `7020`; Event Scheduler requests cannot exceed configured messaging TPS. Actual subscribed limits require tenant/account confirmation. [Rate limits](https://developers.webexconnect.io/reference/rate-limits-for-messaging-apis-event-api-and-inbound-webhook).

**Engineering recommendation:** budget recipient throughput across all producers, including flows and schedulers. Use a bounded queue, jittered retry for classified transient failures, deadline-aware expiry, and per-item reconciliation. Retry only failed/unaccepted items when a batch partly succeeds. After an ambiguous timeout, reconcile before resending side effects.

## Adapter acceptance record

Before implementing or releasing an adapter, record these engineering checks:

1. Exact region, API family/version, method/path, enabled feature, and credential source.
2. A synthetic valid request with every required/conditional field and exact casing.
3. Expected HTTP status **and** body shape/code; individual batch outcomes.
4. Callback registration, authentication/signature, captured schema, and milestone mapping.
5. Correlation versus business idempotency; duplicate and ambiguous-timeout behavior.
6. Invalid credential, missing field, expiry, capacity, and relevant channel/policy failures.
7. Remaining documentation contradictions and the observed tenant result that resolves each.

The source cache contains `.api.json` files and selected OpenAPI operation/component extracts beside these references. ReadMe `api.auth` metadata and an empty OpenAPI security object are not evidence of anonymous API access. Prefer the explicit authentication contract, then verify the generated operation with a harmless authorized test. Do not publish a flow or send customer traffic as an incidental documentation check.
