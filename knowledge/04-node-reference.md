# Core node and control-flow reference

Checked 2026-09-08. The local official-source cache identifies documentation version **6.20.0**. A documentation version is not proof of a tenant's deployed version or enabled features. Exact source update timestamps are recorded in adjacent `sources/cache/help/*.metadata.json` files. This chapter summarizes the operational contracts; the local source pages retain the full event-specific catalogs.

## Configure and connect a node

Drag a palette node onto the canvas, double-click it, configure its fields, and inspect its Input Variables, Output Variables, and Node Outcomes panes. Output availability changes with configuration. Connect each intended event separately even when events share a colored edge. Green indicates continuation, orange timing, and red error. A node without an outgoing connector requires termination configuration. The Nodes guide disallows a connector back to the immediately preceding node. [Nodes](https://help.webexconnect.io/docs/nodes).

For termination, drag an outcome into empty canvas space, select its Node Event and Flow Result, then save. Configure each event separately. The intermediate-breakpoint checkbox belongs to particular integrations that resume waiting for later events; normally leave it unset. [Node transitions](https://help.webexconnect.io/docs/node-transitions).

**Engineering recommendation:** name outcomes by business meaning, retain their underlying product event in the flow specification, and make success, invalid input, timeout, transient failure, and terminal failure visibly distinct. A red edge need not mean a customer-visible failure, and an orange edge can be the expected successful completion of a wait.

## Start: select the event that creates an execution

Choose a channel/integration event, inbound webhook, or custom event; bind the relevant asset and optional AND/OR trigger conditions. Trigger variables depend on the selected event. Custom Event v1 requires service authentication; saving generates `evtid` and a sample request. [Start](https://help.webexconnect.io/docs/start-node).

| Event design issue | Documented behavior |
| --- | --- |
| SMS entry versus active reply | Enabling the no-live-session option prevents a new trigger when a Receive is waiting on matching keyword/number. |
| Competing SMS flows | Same-service and different-service behavior differ; an unguarded Start may consume a reply or produce another execution. |
| Digital event types | A Postback and an Incoming Message can activate different Starts; a Receive waiting for another type is not necessarily resumed. |
| RCS session guard | Matches event type, RCS app, and user; Branded Text enablement extends the check across corresponding SMS flows. |
| Deprecated entry choices | Instagram, CCSP, and legacy BOT entries are marked deprecated. |

Source updated 2026-07-29. **Engineering requirement:** write a trigger collision table before launch: asset, event, keyword/condition, service, existing waiting session, expected winner. Test first message, reply, late reply, and duplicate event.

## Receive: correlate a response to a waiting execution

Configure one or more channels/events and `Max Timeout` in seconds. Custom events require a selected event plus Resume Key/Value pairs unique to the session. Success events become channel-specific, such as `sms.mo` or `whatsapp.mo`; also route `onTimeout` and `onError`. [Receive](https://help.webexconnect.io/docs/receive-node).

| Channel | Correlation inputs |
| --- | --- |
| SMS | Number, Keyword, From Number |
| MMS | Number, From Number |
| Voice | Voice Number, From |
| Messenger | From PSID, Event Name |
| WhatsApp | From WhatsAppID; Incoming Message/Postback/List Message/Reply Buttons |
| Live Chat/In-App | From ThreadID, From UserID, Event Name |
| Email | From EmailID |
| AMB | From AMB ID; invitation responses also accept mobile number |
| RCS | From MSISDN, Event Name |

Common outputs include `receive.message`, `receive.channel`, `receive.payload`, `receive.attachment`; channel tables add sender, transaction, and event-specific values. For SMS, a matched first-word keyword is separated from `sms.message`; a keyword-only message can leave message empty. Form Response must be configured first when combining in-app response types because of a documented UI issue. Source updated 2026-07-31. Full catalogs: [local Receive source](../sources/cache/help/receive-node.md).

**Engineering recommendations:** snapshot the channel identity on entry; do not hard-code a demo recipient. Use country-coded phone strings. Match both conversation and person when the channel exposes both. Use a business request ID as part of custom-event resume correlation. Define what a late event does after timeout. A Receive timeout is not evidence that the external system never performed the action.

## Branch: ordered conditions

| Configure | Behavior |
| --- | --- |
| Branch name; Variable; Condition; Value; AND/OR | Branches evaluate top to bottom and stop on a matching condition. Avoid special characters in branch names. |
| Comparison choices | Equality/inequality, numeric comparisons, case-insensitive equality, contains/case-insensitive contains, In/Not in, starts/ends with, Between, RegEx. |
| In/Not in values | Press Enter after each list member. |
| Output | `branch.output` reports a Boolean. |
| Outcomes | Named branches, default `None of the above`, and `onError`. |

Use Test with input values to see the selected branch. RegEx matching is case-sensitive by default; full-string validation needs anchors. The documentation itself qualifies inline case flags as runtime-dependent. [Branch](https://help.webexconnect.io/docs/branch-node).

**Engineering recommendation:** place specific cases before broad cases. Test overlapping conditions, both boundaries of Between, malformed input, and the default path. A pattern that recognizes a date's shape does not establish that the date exists. Prefer `[0-9]` for a deliberately ASCII numeric code when escaping through UI/export layers is uncertain.

## Evaluate, Data Parser, and Data Transform

Use [variables and expressions](03-variables-and-expressions.md#evaluate-and-supported-expressions) for Evaluate script outputs, libraries, substitution, and runtime limits.

| Node | Required configuration | Output/verification |
| --- | --- | --- |
| Data Parser | Source variable, JSON/XML format, sample body; parse and select extraction paths; output variable names | Test real payload shapes, including absent paths. |
| Data Transform | Input variable, JSON/XML, VTL template | `dataTransform.output`; inspect generated serialization. |

Sources and precise syntax are consolidated in [parsing and rendering](03-variables-and-expressions.md#parsing-and-rendering), avoiding inconsistent copies of those contracts.

## HTTP Request

| Configure | Contract |
| --- | --- |
| Method, Endpoint URL | GET/POST/PUT/PATCH/DELETE; query values are automatically encoded. |
| Headers; Body; optional Proxy Address | Body applies to POST/PUT/PATCH. |
| Connection Timeout; Request Timeout | Milliseconds; both maximum 20,000 from v5.6.3. Connection failure uses error; response timeout uses `onTimeout`. |
| Output extraction | JSON/XML sample → Parse → selected paths → Import. |
| Standard outputs | `https.statusCode`, `https.statusText`, `https.responseBody`, `https.responseHeaders`. |
| Outcomes | `onSuccess`, `onError`, `onTimeout`. |

Test the request in-node. Pre-encoded query values can be encoded again. The guide suggests bounded delayed retries for 429 bursts following waiting-node release. OAuth 2.0 integrations are directed to Custom Integration. [HTTP Request](https://help.webexconnect.io/docs/http-request-node).

**Engineering recommendations:** inspect the status code and application error before business success; do not assume transport completion means order acceptance. Retry only when the operation is safe to repeat or has an idempotency key. Separate network timeout from application rejection. Reconcile an uncertain write before repeating it. Keep credentials in the supported authorization mechanism, not sample payloads or diagnostic output. See the [namespace discrepancy](03-variables-and-expressions.md#documentation-discrepancies-to-resolve-with-the-picker).

## Delay and Social Hour Check

| Node | Fields | Outputs and outcomes |
| --- | --- | --- |
| Delay | Delay time → seconds; or Wait for date → `dd-mm-yyyy hh:mm:ss`, using server timezone | `delay.waitTime`; `onTimeout` after waiting; `onError` for invalid input. |

The configured delay is a **minimum**, and actual waiting can be longer under tenant load. [Delay](https://help.webexconnect.io/docs/delay-node).

| Social Hour field | Configure |
| --- | --- |
| Policy | Wait until the next permitted window, or branch immediately outside it. |
| Schedule | Whole week or Customize by Day; 24-hour From/To values. |
| Exclusions | Multiple within-day exceptions; holiday dates override normal hours. |
| Extra delay | Optional minutes. |
| Time Zone | Static zone or runtime Dynamic Time Zone parameter. |
| Output | `socialHour.timeToNext` (unit not stated in the page). |
| Outcomes | `onSuccess`, `nextSocialHour`, `notInSocialHour`, `onError`. |

Invalid timezone codes produce error. The guide states existing tenants use a 2025 IANA timezone file and need an operations request for a newer file. [Social Hour Check](https://help.webexconnect.io/docs/social-hour-check-node).

**Engineering recommendations:** store the customer's intended timezone explicitly, test DST transitions and holidays, and use a business expiry check after waking. An appointment reminder may become obsolete while delayed. A large release at opening time needs downstream capacity controls. Social hours, customer consent, campaign policy, and agent working hours are separate requirements.

## Page Connector and Call Workflow

| Node | Use and configuration |
| --- | --- |
| Page Connector | Reuse a sequence within one flow. Create/select a page, then connect the Page Connector to the destination node. A page without the target connection is incomplete. The guide warns canvas performance can degrade beyond roughly 200 nodes. |

[Page Connector](https://help.webexconnect.io/docs/page-connector-node).

| Call Workflow | Contract |
| --- | --- |
| Target | Another flow in the **same service**. |
| Fields | Workflow Name; Node Type (`All`, `Start`, `End`); Node Name. |
| Modularity | Separately maintained flows; guide recommends this around 150 nodes, sometimes fewer with many integration nodes. |
| Asset caveat | A parent without channel assets calling a channel-using child may produce `Channel Bean is null`; documented workaround is a placeholder Send node and correct asset mapping at parent publication. |

[Call Workflow](https://help.webexconnect.io/docs/call-workflow-node). See [cross-boundary variable contracts](03-variables-and-expressions.md#page-and-child-flow-boundaries) for the conflicting page-visibility statements.

**Engineering recommendations:** define module ownership, input/output variables, error meanings, side effects, and permitted callers. Test parent and child together after either changes. Do not treat canvas-size guidance as a guaranteed hard limit or wait until the canvas becomes unusable before separating responsibilities.

## Looping and bounded retries

This reference does not invent a native Loop node: the inspected core node inventory describes connectors, and HTTP guidance describes building a loop. Use an explicit graph pattern with a counter, condition, wait, and exit. [Nodes](https://help.webexconnect.io/docs/nodes).

**Engineering pattern, configurable values rather than product defaults:**

```text
Initialize RequestAttempt=0
Define MaximumAttempts as total requests, including the first
  -> Check expiry/cancellation before every attempt; stop if expired/cancelled
  -> If RequestAttempt >= MaximumAttempts, exhausted failure
  -> Increment RequestAttempt
  -> Attempt request
  -> Classify result
       accepted -> success
       permanent rejection -> terminal failure
       uncertain write -> reconcile business status
       retryable AND RequestAttempt < MaximumAttempts
         -> compute next delay within remaining time budget
         -> wait
         -> return to expiry/cancellation and attempt-budget checks
       otherwise -> exhausted failure
```

Respect the preceding-node connector restriction; include actual classification/wait work in the return path. Here MaximumAttempts includes the first attempt: a value of three permits at most three requests. Keep user reprompts, dependency retries, and OTP resend counts separate. Define a total elapsed-time budget, stop on cancellation, and test the exhausted path. A no-response customer loop should have a final timeout result, not another infinite reminder.

## Generate OTP and Validate OTP

| Generate OTP field | Documented setting |
| --- | --- |
| OTP Format | Alphabetic, Numeric, Alphanumeric (default). |
| OTP Length | 4–64; default six. Known save issue: leaving length empty saves using six. |
| OTP Validity | Minutes; default 30. |
| On Resend OTP Request | Generate a new code or reuse current; either resets validity. |
| Transaction Reference | Reference binding generation to validation. |
| Extra Parameters | Optional key/value bindings that must also be supplied for validation. |
| Output / outcomes | `generateOTP.OTP`; `onSuccess`, `onError`. |

Regenerating the service key during a session breaks OTP operations for existing sessions. [Generate OTP](https://help.webexconnect.io/docs/generate-otp-node), updated 2026-04-15. Generation and channel delivery must be represented explicitly in the journey; do not treat the sample code display as a sent message.

| Validate OTP field | Documented setting |
| --- | --- |
| OTP | Variable containing submitted code. |
| OTP Format | Optional surrounding prefix/suffix to remove before checking. |
| Transaction Reference | Same binding as generation. |
| Notify URL | Optional result notification endpoint. |
| Resend OTP Command | Optional keyword recognized in the submitted input. |
| Extra Parameters | Same key/value bindings as generation. |
| Output / outcomes | No standard output variables; `onSuccess`, `onFail` for incorrect code, `onError` for invalid processing input. |

[Validate OTP](https://help.webexconnect.io/docs/validate-otp-node).

**Engineering recommendations:** mask code values, limit attempts and resend frequency, avoid exposing whether an account exists, and invalidate the business authorization when its underlying request changes. Test wrong/expired code, resend, changed reference, timeout, and post-success reuse against the real tenant behavior. Do not implement code validation using string equality against a logged generated code.

## Profile and durable state

| Profile action | Configuration |
| --- | --- |
| Fetch | Action, Customer/Application Profile type, Identifier Type/Value, destination variable → profile attribute mappings. |
| Create/Update | Profile type, identifier, attribute/value mappings. |
| Delete | Profile type and identifier. |
| Common customer attributes | `customerid`, `email`, `msisdn`, `name`. |
| Outputs / outcomes | No standard node outputs are listed; fetch uses mapped variables. `onSuccess`, `onError`. |

The page uses both Customer and Master profile labels. Default customer-profile creation depends on Push, Live Chat, or In-App enablement. Application attributes depend on channel. [Profile](https://help.webexconnect.io/docs/profile-node).

**Engineering recommendation:** flow custom variables are execution context; they are not a durable order database or cross-session deduplication guarantee. Keep durable business state behind a supported profile/integration/API contract. Define its ownership, retention, concurrency, and deletion behavior independently of the graph.

| Legacy storage node | Existing-tenant reference |
| --- | --- |
| Registry — deprecated | Instance, Get/Set/Delete operation, Store, User Key; Structured Data column mappings or Open Format body. |
| Database — deprecated | SQL database, Select/Update operation, Instance, DB Pool, Query; first-record, JSON records, or serialized-array result; variable/column mappings and counter when applicable. |

Sources: [Registry](https://help.webexconnect.io/docs/registry-node), [Database](https://help.webexconnect.io/docs/database-node). Both guides preserve existing tenants while discontinuing future availability. They are migration-reading aids, not the default recommendation for new work. Product-wide storage arrangements such as private profile/consent/transaction stores are arranged case by case. [Data storage](https://help.webexconnect.io/docs/data-hosting).

## Hash, Encryption, Decryption

| Cryptographic Hash field | Contract |
| --- | --- |
| Algorithm | SHA-256 or SHA-512 are explicitly named. |
| Plain Text | String or input variable. |
| Salt | Optional; Text/Base64/Hex type and value, or Autogenerate Salt. |
| Outputs | `hash.output`, `hash.salt`. |
| Outcomes | `onSuccess`, `onError`. |

The page says four algorithms but only enumerates two; do not infer the missing choices. [Cryptographic Hash](https://help.webexconnect.io/docs/cryptographic-hash-node-configuration).

| Encryption method | Required configuration context |
| --- | --- |
| AWS KMS | Access Key, Secret Key, AWS Region, Plain Text, Key ID; optional encryption-context key/value pairs and grant tokens. |
| Webex Connect | Plain Text and destination Variable Name. |

[Encryption](https://help.webexconnect.io/docs/encryption-node).

| Decryption method | Required configuration context |
| --- | --- |
| AWS KMS | Access Key, Secret Key, AWS Region, Cyphertext Blob, matching encryption context, grant token where used. |
| Webex Connect | Text To Be Decrypted and Store Decrypted Data In. |

Use the corresponding encryption method and parameters. [Decryption](https://help.webexconnect.io/docs/decryption-node). These pages do not provide stable generic output/event catalogs for every method; inspect configured node panes rather than inventing output names.

**Engineering recommendations:** hashing is one-way and is not reversible encryption. Salted hashes are not an HMAC/signature scheme. Use the organization's approved key-management and authorization contract; do not print credentials or plaintext in tests. Validate encryption/decryption with synthetic values, correct context, deliberately wrong context, and key access failures. Do not assume encrypting a field retroactively removes copies already logged elsewhere.

## Event Scheduler: launch work outside an active flow

Event Scheduler is an App Tray tool, not a waiting node. Select SMS or Custom Event, service/event, input source, field mappings, name, schedule, timezone, and TPS. Inputs include upload/SFTP and enabled consent groups. Supported files: TXT/CSV/XLSX; one file, at most 75 MB, filename under 75 characters. Match event headers; preserve identifiers as text. Configurable TPS is 1–50, further constrained by available tenant limits; error 7020 is retried when capacity returns. [Event Scheduler](https://help.webexconnect.io/docs/event-scheduler).

Schedules use tenant timezone. Social-hours checks can skip a scheduled SFTP pickup until a later eligible run; a large run already started may continue beyond closing. Schedule-wide correlation IDs are reused across its messages, unless overridden in a Send node. Source updated 2026-06-24. Full configuration: [local scheduler reference](../sources/cache/help/event-scheduler.md).

**Engineering recommendations:** use a distinct business idempotency key per input record, not only the schedule correlation ID. Validate the selected event/service association and a small test file before a bulk run. Reconcile valid, invalid, duplicate, attempted, and accepted record counts. Recheck consent and business expiry at actual send time when a long wait can make the input stale.

## Node readiness worksheet

For each configured node, capture:

1. Purpose, node ID, display name, and source/version used.
2. Each field's literal or variable binding, format/unit, allowed values, default, and sensitivity.
3. Each output consumed later, including exact case, source node, and missing-value behavior.
4. Every event's destination or termination result; note deliberate intermediate events.
5. External side effects, correlation key, repeat-safety rule, timeout, and compensation/reconciliation step.
6. One positive case and the material boundary/failure cases for this node.

This worksheet is an engineering artifact. It makes a configured flow reviewable without claiming that a documentation-only example has been executed in a tenant.
