# Testing and operations

Use this chapter when proving a flow works, diagnosing a transaction, or preparing its operational handoff. Official behavior was researched on **2026-09-08**. Platform facts below cite their source; sections marked **Design recommendation** are implementation guidance, not claims of built-in guarantees. No authenticated tenant execution was performed while compiling this chapter.

For save, publish, pause, version recovery, import/export, sharing, and service locking, use [Flow lifecycle](02-flow-lifecycle.md). A successful edit or node test is only one piece of the evidence for a working customer journey.

For exact node fields and events use the [Node reference](04-node-reference.md); for transition actions and variable handling use [Variables and expressions](03-variables-and-expressions.md).

## 1. Define what the flow must prove

**Design recommendation.** Write this operational contract before choosing test inputs:

| Contract field | What to record |
| --- | --- |
| Entry | Exact event, asset/service, admissible payload, expected arrival pattern |
| Success | Observable business result, its authoritative system, and how to verify it |
| Side effects | Every message, mutation, task creation, transfer, or external notification |
| Identity | Business request ID; customer/conversation key; event ID; operation key |
| Time budget | User-visible deadline; each wait; each dependency deadline; total retry allowance |
| Terminal paths | Success, expected rejection, customer abandonment, technical failure, unresolved state |
| Recovery | Safe retry conditions, reconciliation lookup, fallback, escalation owner |
| Evidence | Transaction/message IDs, sanitized expected output, actual output, version and time zone |

Define success at the business boundary. For example, an appointment journey succeeds when the booking system records the requested slot and the customer receives the intended confirmation. Record those separately: creating a booking can succeed while the confirmation fails. An HTTP response, a green node edge, and an agent-task acknowledgement each establish narrower facts.

Use synthetic recipients and a test-owned downstream record whenever possible. If the only available trigger is live, constrain the test entry to an explicit test identity and account for each side effect before invoking it. Do not let a failure test send a real fallback campaign.

## 2. Operational flow settings

**Platform behavior.** The following is a compact reference to [Flow Settings](https://help.webexconnect.io/docs/flow-settings):

| Setting | Behavior and limit |
| --- | --- |
| Correlation ID | Optional application reference; maximum 250 characters. |
| Prevent duplicate flow runs | Defaults off; when enabled, matching configured identifiers suppress duplicate requests. Previously called Session Key. |
| Descriptive Logs | Defaults off. Captures detailed execution for live flows; activation can lag two minutes. Since v6.3.0, the switch is independent of version. |
| Automatic log expiry | Tenant-dependent. With auto-disable, configure 1–1440 minutes; documentation also describes a 1000-transaction cutoff. Transactions begun during capture retain logging after expiry. Older tenants may behave differently. |
| Flow Outcomes | Success, Error, Incomplete; custom codes/descriptions are supported. |
| Outcome notification | Supports GET, POST, PUT, DELETE and variable payloads. Invalid URLs are ineligible for retries. |

**Design recommendation.** Use an opaque correlation reference, not a phone number, access token, or full customer record. Test the actual duplicate-key fields and reuse window in your tenant; this page does not establish a durable exactly-once contract. Record the observed logging-expiry behavior rather than assuming every tenant exposes identical controls.

## 3. Find the correct evidence

### Flow Debug: inspect a particular execution

**Platform behavior.** Open Flow Debug from the canvas side panel. It initially lists ten recent runs; select a transaction to inspect ordered nodes, durations, and outcomes. Records ordinarily arrive after about two minutes. The three detail levels are summary, sequence, and node execution. Node detail requires Descriptive Logs and appropriate decrypt permission; prolonged detailed logging can affect tenant performance. The general window is 30 days, but custom-event/webhook transaction detail has a seven-day maximum. [Flow Debug](https://help.webexconnect.io/docs/transaction-logs-and-debugging)

Flows created after v6.3.0 have a 1000-node-execution ceiling. Some variable-change logs appear only without Descriptive Logs. Object values created in Evaluate may appear as Rhino object representations; escaped JSON in logs does not imply runtime mutation. [Flow Debug](https://help.webexconnect.io/docs/transaction-logs-and-debugging)

**Design recommendation.** Start with the first node where actual behavior diverges from expected behavior. Preserve the preceding input and branch condition. The final error may be a consequence of an earlier missing variable, incorrect correlation key, or premature branch termination.

### Debug Console: connect flow and channel evidence

**Platform behavior.** Select Channels or Integrations and a time range, then narrow by transaction ID, service, source, customer/channel identity, or integration resume key. The Integrations tab covers prebuilt integration logs. Drill into the source transaction for the flow; inspect its message records for delivery evidence. A source-row status and a message-row status describe different objects. [Debug Console](https://help.webexconnect.io/docs/console)

Realtime logs typically lag about two minutes; buffered logs can lag ten minutes at high volume and restrict a query to one day. Both normally cover the last 30 days. Enabled archive search can extend available queries to configured 60–90-day ranges. The page also contains an unconditional 30-day statement; treat archive availability as a tenant capability to verify. Sensitive fields are encrypted by default; Decrypt Access is separate from being able to open the console. [Debug Console](https://help.webexconnect.io/docs/console)

**Design recommendation: diagnostic sequence.**

1. Capture the original trigger response, request/event ID, tenant, service, flow/version, asset, and time with offset.
2. Search by the exact ID first. If absent, correct the time zone and scope and allow for the documented ingestion lag before concluding execution never started.
3. Compare observed node order to the intended path. Inspect the input at the first divergence, its node outcome, and the next edge.
4. Follow each side effect into the destination system or message record. Preserve both platform and external IDs.
5. Reproduce with the smallest synthetic payload that keeps the failure. Change one causal condition and retain before/after evidence.
6. Stop detailed capture when the needed transaction has been observed. Retain a sanitized incident record under the project retention policy.

Tenant time zone applies to debug timestamps and delivery receipts. Tenant settings are owner-managed; the platform does not provide a separate report-only time zone. [Tenant Settings](https://help.webexconnect.io/docs/tenant-settings)

## 4. Exercise the behavior, including failures

**Design recommendation.** Choose cases that can change the outcome of the journey. The matrix below is a reusable minimum, not a demand to test every channel feature on every flow.

| Case | Input or induced condition | Evidence required |
| --- | --- | --- |
| Nominal path | Smallest valid real event shape | Correct branch, external result, terminal outcome |
| Required input absent | Omit one required field | Controlled rejection before any unintended side effect |
| Empty versus missing | Empty string, whitespace, null, absent key | Explicit treatment consistent with downstream contract |
| Parser boundary | Unicode, quotes, ampersands, nested JSON, unexpected response type | Actual sent value and parsed output match the contract |
| Invalid choice | Unknown button/postback/option value | Reprompt or controlled end, with a bounded attempt count |
| No customer response | Let the receive/wait deadline expire | Intended timeout branch; no abandoned processing |
| Policy rejection | Test-owned identity that is ineligible for contact | No prohibited send and an intelligible terminal category |
| Dependency refusal | Controlled authorization, validation, or business error | Correct classification; no blind retry |
| Dependency slowdown | Response after the chosen deadline | Deadline honored; uncertain side effect reconciled |
| Transient dependency failure | Controlled rate limit or temporary outage | Bounded retries and eventual recovery or terminal failure |
| Duplicate entry | Same event twice, sequentially and concurrently | Operation occurs at most once where business contract requires it |
| Distinct parallel work | Two legitimate requests from one customer | No key collision, overwritten state, or cross-conversation response |
| Late/out-of-order event | Callback after timeout; previous reply after new prompt | Stale event cannot alter the current operation incorrectly |
| Partial success | Primary mutation succeeds, notification fails | Mutation is preserved; message recovery does not duplicate mutation |
| Downstream record already exists | Repeat completed operation | Reuse/reconcile existing result according to business rules |
| Fallback fails | Primary and alternate route both unavailable | Bounded final state; actionable escalation evidence |
| Resume burst | Release representative waiting transactions together | Acceptable downstream load and completion time |
| Release overlap | Old execution waits while new version is activated | Expected in-flight behavior and correct configuration for both |

For every result record `case_id`, fixture reference, expected path, actual path, business effect, transaction IDs, timestamps, tested flow version, pass/fail, and a short defect description. Avoid attaching raw customer payloads merely to make a test record look complete.

Use three levels of proof:

1. **Configuration proof:** required assets, variables, credentials references, edges, and outcome configuration exist.
2. **Integration proof:** one isolated dependency request returns an understood response and the mapped fields are correct.
3. **Journey proof:** a real entry event follows the intended flow and produces the complete external result, including asynchronous completion.

Do not claim level 3 based on level 1 or 2. See [Flow lifecycle](02-flow-lifecycle.md) for the platform test workflow and activation requirements.

## 5. Route errors deliberately

**Platform behavior.** Node exception edges can terminate or branch. The documented examples map internal `onError` to code `102`/Error and policy or timeout interruption to `103`/Incomplete. A timeout event occurs when that node's configured interval expires. Available event names depend on the node; use its actual event selector rather than assuming all nodes expose the same spelling or events. [Exception handling at the node level](https://help.webexconnect.io/docs/exception-handling-at-the-node-level)

**Design recommendation.** Define a terminal-outcome catalog before wiring error edges. Suggested business categories are `completed`, `customer_declined`, `no_response`, `validation_rejected`, `policy_blocked`, `dependency_failed`, `retry_exhausted`, and `needs_reconciliation`. These are example labels, not reserved platform status codes. Allocate codes according to the tenant convention and distinguish expected business decisions from technical defects.

For each fallible node, answer:

- What does success prove at this point?
- Which errors are permanent for this exact input?
- Which outcomes are transient, and is repetition safe?
- Could the remote operation have succeeded even though its response was lost?
- What data must be retained to recover without repeating completed work?
- Which end state will an operator see if every recovery route fails?

An unhandled red or timeout edge is unfinished business logic. A catch-all success end also hides a defect: it makes failed work appear successful to the reporting consumer.

## 6. Bound retries and make side effects recoverable

**Platform behavior.** The Webex Contact Center integration guidance states that failed HTTP and prebuilt integration calls transition through their failure outcome without implicit retry. Flow designers must provide appropriate retry logic. It also warns that long HTTP/Delay timeouts and unbounded loops can impair concurrent processing. Apply node-specific documentation when a connector specifies a different contract. [WXCC best practices](https://help.webexconnect.io/docs/wxcc-best-practices-guidelines)

**Design recommendation.** Keep platform admission retries, outbound callback delivery retries, business-operation retries, and your own retry loop distinct. Give each a recorded owner and ceiling. Never multiply several unknown retry layers together.

| Result class | Recommended policy |
| --- | --- |
| Invalid input, missing asset, schema failure | Fix configuration/input; do not retry unchanged work |
| Credential or permission failure | Alert/configuration repair; retry only after the cause changes |
| Business conflict or rejection | Interpret the downstream contract; reconcile existing state where appropriate |
| Rate limiting / temporary unavailability | Retry only safe operations, respect a valid provider delay, cap attempts and elapsed time |
| Connection or response timeout | Treat remote side effect as uncertain until its operation status is checked |
| Unknown result | Preserve correlation and request fingerprint; controlled failure or reconciliation |

Suggested control structure, expressed as **pseudocode**, not importable Webex flow JSON:

```text
Initialize retry_count = 0, max_retries = 3, operation_key, deadline
Before EVERY attempt: recheck deadline/cancellation
  expired/cancelled -> terminal or reconciliation outcome; do not start new work
Attempt only the incomplete operation
  success -> persist its external result -> continue
  permanent failure -> record terminal reason -> end/escalate
  ambiguous side effect -> query by operation_key
    already complete -> reuse result -> continue
    still unknown -> reconciliation outcome
  retryable AND safe AND retry_count < max_retries AND before deadline
    increment retry_count
    wait for bounded backoff
    recheck deadline/cancellation after waiting
      expired/cancelled -> terminal or reconciliation outcome
    attempt again with SAME operation_key
  otherwise -> retry_exhausted
```

Here `max_retries = 3` means at most four total attempts. If your team's policy counts attempts instead, name the variable `max_attempts`; do not leave the distinction implicit. Select actual intervals from the downstream contract and journey deadline, and spread synchronized retries when the platform/runtime supports your chosen strategy. Recheck the deadline after every wait and allow time for the operation itself before starting another attempt. A long human wait is not a substitute for limiting an API call.

Keep a durable idempotency record in a system that can atomically claim the operation when correctness demands it. An illustrative key is `business_request_id + operation_type + operation_revision`. Include only a revision that genuinely changes the intended effect; a retry counter must not change the key. Store request fingerprint, state, result reference, and expiry. If the same key arrives with different material input, reject or reconcile rather than silently reusing the old result.

The flow's duplicate-entry setting is one layer. It does not prove that a booking API, message API, webhook receiver, or database update is idempotent. Do not implement critical duplicate prevention as a non-atomic “read then write” check shared by concurrent flows. For an irreversible operation without an idempotency or status-query contract, use a deliberate unresolved state instead of automatic blind repetition.

## 7. Control capacity at the correct layer

**Platform behavior.** Webex defines concurrency in flow threads; waiting nodes split a flow into threads. This differs from incoming API/webhook TPS. In Monitoring → Flow Monitoring, owners can reserve concurrency for a flow, using up to 75% of tenant allocation; remaining/shared capacity serves other eligible work. Reserved capacity is exclusive to that flow. Availability is tenant-dependent. [Flow Monitoring](https://help.webexconnect.io/docs/flow-monitoring)

The report includes invocation/resume volume, average thread duration, ten-minute mean/median/peak execution rates, rejection rate, and reservation. The documented rejection count can include repeated internal attempts to admit queued work. Do not interpret it as a count of unique permanently lost customer requests. [Flow Monitoring](https://help.webexconnect.io/docs/flow-monitoring)

**Design recommendation.** Inventory separate constraints: inbound rate, active flow threads, custom-node throttling, downstream API quota, channel send capacity, voice capacity, and delayed work resuming together. A capacity increase at one layer cannot correct a lower limit elsewhere.

For a first estimate, calculate `average active work ≈ arrival rate × average active duration`, using consistent time units and measured active-thread duration. This is an engineering estimate, not a platform sizing guarantee. Then test peak traffic and resume bursts; averages hide a 09:00 release of thousands of waiting journeys. Reservation decisions must consider the other flows that lose access to reserved capacity.

A useful capacity probe records offered requests, accepted requests, unique completions, unique failures, queued duration, dependency latency, and observed retry attempts over the same time interval. First reduce unnecessary serial work and repeated calls. Then consider bounded backoff, scheduler spreading, upstream queues, or an owner-approved reservation change. Leave sufficient time budget for delayed work to finish before the business deadline.

## 8. Create an operational record that survives debugging

### Logbooks

**Platform behavior.** A Logbook requires a declared schema, tenant enablement, and flow mapping. It can produce CSV/TXT, rotate by count or schedule, and ship to SFTP/S3. Local destinations and FTP are deprecated for new configurations. Disabling the tenant feature stops collection while retaining configuration. Schema changes create a new file. Data fields are not quoted; delimiter collisions can corrupt interpretation. Rotation uses explicit scheduling/time-zone settings and can skip a DST-transition slot. Locks restrict management/access but do not prevent flows from writing to the Logbook. [Logbooks](https://help.webexconnect.io/docs/logbook)

**Design recommendation.** Define a small schema such as:

```text
event_time_utc, schema_version, environment, flow_release,
business_request_id, source_transaction_id, operation_key,
stage, outcome_category, external_reference, attempt_count,
elapsed_ms, error_class
```

These are suggested attributes, not built-in variables. Map them to actual available variables. Keep free-form content, credentials, message bodies, and sensitive identity fields out of the routine record. If a field can contain the chosen delimiter or newlines, normalize or encode it and document the consumer's decoding rule. Test the generated file with the real importer, not just a visual scan.

Place records at meaningful boundaries: accepted request, irreversible side effect confirmed, fallback selected, and terminal result. Avoid a row for every trivial node unless it answers an operational question. Verify both file creation and arrival at the destination; configuration visibility is not export proof. A missing export alert must itself be observable through an independent check.

### Outcome consumers and metrics

**Design recommendation.** For each terminal outcome, define who consumes it, the expected acknowledgement, and a reconciliation path if the consumer is unavailable. Keep outcome notifications small and keyed. A notification receiver should tolerate duplicates and events arriving after its own timeout.

Track:

- **Business completion:** completed intended operations divided by accepted eligible requests.
- **Technical failure:** failed dependency/configuration execution, separated from customer decline or policy blocks.
- **Abandonment:** unanswered journeys after their defined waiting interval.
- **Latency:** end-to-end and dependency timing; include a tail percentile, not only a mean.
- **Recovery:** retries, exhausted retries, fallback use, and unresolved operations.
- **Evidence health:** log/export delay and last successful downstream receipt.

Each metric needs a denominator and time window. Do not count a duplicate delivery receipt as a second customer success, a retried invocation as a new business request, or a rejected contact-policy attempt as a platform outage.

### Data Streams

**Platform behavior.** Data Streams can copy messaging events/receipts and audit records to Kafka. Support enablement and a configured destination are prerequisites. Flow nodes can add contextual key/value data for supported message exchanges; API sends and asset-only configuration cannot add that flow context. Supported node channels include SMS, Email, Live Chat/In-App, RCS, Messenger, Apple Messages for Business, and WhatsApp; Voice/MMS nodes are excluded. Asset and node configuration together can produce duplicate payloads. Clearing an event and saving stops its stream immediately. The page permits AWS/Azure Kafka destinations but separately excludes Azure environments; distinguish destination hosting from tenant hosting and verify availability. [Data Streams](https://help.webexconnect.io/docs/data-streams)

**Design recommendation.** Before treating a stream as the reporting source, send a test event and compare its business ID, message ID, timestamp, context, and duplicate count at the consumer. Record how the consumer deduplicates events and how it detects a silent stoppage. Do not infer a completed business journey from the existence of a copied message event.

### Export Logs

**Platform behavior.** New Export Logs covers inbound, outbound/delivery, and failed outbound-webhook records; non-messaging node failures are excluded. It supports download and SFTP/S3 export. Scheduled export is an Owner-controlled paid feature and always produces decrypted logs. Multi-select can reach 100 million records per request, is unavailable on Azure, and restricts multi-service/channel selection to 24 hours within the preceding 30 days. Large exports may take 30 minutes. Instagram is unsupported. Selecting `All Existing & Any New` temporarily overlaps current schedules, then disables them after 24 hours. Inspect existing schedules before using it. [New Export Logs](https://help.webexconnect.io/v6.21.0/docs/new-export-logs)

The July 2026 release note retires Legacy Export Logs in favor of New Export Logs; release rollout remains deployment-specific. [July 2026 update](https://help.webexconnect.io/changelog/product-update-v6200-july-2026)

**Design recommendation.** Use an explicit export scope, destination, retention owner, and expected schedule. Confirm the exported rows are present and parseable at the destination. Keep a separate source for non-message business failures. Treat decrypted schedules as a data-transfer decision, not merely another dashboard setting.

## 9. Permissions, sensitive evidence, and change control

**Platform behavior.** The role matrix separates console access, decrypt permission, export scheduling, and owner-only administration. Owner and Full Access have granular key permissions; the same page's older prose also mentions Limited Access seeing keys. Because those statements disagree, verify the effective Permissions UI for the target account before depending on key visibility. [User Roles](https://help.webexconnect.io/docs/user-roles-and-hierarchy)

Cisco recommends individual user identities, RBAC, and restricting decryption to authorized users; SAML 2.0 SSO is supported. [Security best practices](https://help.webexconnect.io/docs/references-security-best-practices)

User Audit is an Owner-only subscription feature covering the preceding 30 days of user activity across groups/teams. Filter by role, user, and period; expanded records include action, status, timestamp, and IP address. Audit records can be sent through Kafka Data Streams. These are change/activity records, not flow completion evidence. [User Audit](https://help.webexconnect.io/docs/user-audit)

For the special exposure created by debug transition actions, read [Set values at the correct point](03-variables-and-expressions.md#set-values-at-the-correct-point). No general flow-variable masking checkbox was established by this research; do not assume controls from Webex Contact Center Flow Designer also exist in Webex Connect.

**Design recommendation.** Separate these operational needs explicitly: edit a flow, make a release live, inspect summary evidence, decrypt customer data, change credentials, and schedule external exports. Grant only the access needed by the task. Put secret references in the handoff; do not paste tokens into a flow specification, repository, test fixture, or incident report.

Before sharing an export, inspect it for embedded URLs, credentials, customer data, custom-node configuration, and test identities. Use a redacted review artifact and preserve the authoritative original in its controlled location. A hidden field in one UI view does not establish that every log, export, or destination is sanitized.

## 10. Release and incident handoff

**Design recommendation.** Keep the release record short enough that an operator can use it during a failure:

| Required evidence | Acceptance question |
| --- | --- |
| Flow ID, intended version, environment, service, trigger/assets | Is this the exact flow receiving the intended event? |
| External variables and credential references | Were target-environment values verified? |
| Test case results with transaction IDs | Do the critical successful and failed paths have observed proof? |
| Business side-effect checks | Can partial completion be distinguished from full success? |
| Error/retry/wait policies | Is every loop bounded and every dependency failure recoverable or terminal? |
| Capacity assumptions and observations | Does representative peak/resumed traffic meet the journey deadline? |
| Outcome/log/export sample | Can operations find the result without rerunning the customer request? |
| Recovery version and procedure | Can a maintainer restore service while handling in-flight work correctly? |
| Owner and escalation destination | Does each unresolved outcome have someone responsible for it? |

Execute the activation and rollback mechanics from [Flow lifecycle](02-flow-lifecycle.md). Do not mark a release proven solely because it became live. Capture one constrained post-release journey through the actual trigger and inspect its business result.

For an incident, preserve scope, first/last observed failure, customer-impact estimate, recent change, transaction and external references, expected versus actual behavior, first divergent node, dependency response class, current workaround, and unresolved side effects. Reconcile the affected operations before re-driving them. A rollback can restore routing logic while leaving previously created bookings, tasks, or messages intact.

## 11. What still needs tenant evidence

These are explicit verification boundaries, not invitations to research every flow from scratch:

- Effective duplicate-key configuration and retention/reuse behavior.
- Enabled logging modes, detailed-log expiry controls, retention/archive entitlement, and masking coverage.
- Actual role permissions and hierarchy scope, especially where documentation mixes old and new behavior.
- Assigned throughput/concurrency, integration quota, channel availability, and provider-specific retry/idempotency contracts.
- Exact connector version and async outcome/resume semantics used by the flow.
- Tenant execution results. This knowledge base supplies the method and known semantics; only an observed target run establishes that a particular configured flow works.
