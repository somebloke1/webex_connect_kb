# Variables, expressions, and data contracts

Evidence checked 2026-09-08 against official Webex Connect documentation, whose cached page metadata identifies version 6.20.0. These are Connect Flow Builder conventions. They are not Webex Contact Center Flow Designer expression syntax. Product facts appear with sources; the contract patterns and test matrix are engineering recommendations, not additional platform guarantees.

## Variable categories and lifetime

| Category | Definition and reference form |
| --- | --- |
| Custom | User-created, referenced as `$(OrderId)`. Creation inside a node does **not** make it private to that node; it is available across the flow. |
| Node output | Produced when that node executes, prefixed by node ID; for example `$(n11.receive.message)`. Select it from the contextual picker. |
| Input | The configuration pane lists available upstream data; it is a view of usable variables, not an independent persistent store. |
| Externalized custom | Value supplied at launch, allowing shared configuration across nodes. Externalization is not a secret-storage claim. |
| Session | Platform-managed names; do not create custom variables with these names. Values depend on event/channel. |

Names are case-sensitive. Static values stay fixed; dynamic values vary by execution. Important reserved names include `ts`, `servicekey`, `key`, `appid`, `transid`, `payload`, `message`, `destination`, `senderid`, `msisdn`, `thread_id`, `userid`, `customerid`, `evtid`, `callbackdata`, `notifyurl`, `channels`, and `deliverychannel`. Timestamp formats vary by channel. An unqualified `payload` can change with the last executed node, so retain the required producer-specific value explicitly. [Variable management](https://help.webexconnect.io/docs/variable-management-in-flows).

The custom-variable tutorial specifies alphanumeric names and disallows special characters. It also requires a variable used in Evaluate to have been referenced in an earlier node's configuration or transition action. Set it explicitly before Evaluate, even when a default exists. [Creating custom variables](https://help.webexconnect.io/docs/create-custom-variable-webexconnect).

## Set values at the correct point

Transition actions run on entering or leaving a node. `Set Variable` takes a custom-variable target and mandatory value, permitting a fixed assignment or copying node output. Multiple assignments can be added. Copy freshly generated output on leaving its producer. Debug actions capture all custom variables or one value; both require descriptive logging. A single-value log ID must be an integer greater than 1000. Debug content is not encrypted. Logbook actions require tenant enablement, a logbook mapped under Flow Settings → Custom Logs, and attribute/value mappings. A disabled Logbook feature can leave configuration visible without writing records. [Transition actions](https://help.webexconnect.io/docs/transition-actions).

**Engineering convention:** initialize identifiers, retry counts, and status separately from optional customer content. Use names such as `OrderId`, `CustomerChannelId`, `RequestAttempt`, `BusinessStatus`, and `ResponsePresent`. Maintain a variable dictionary with producer, meaning, representation, sensitivity, default, and consumers. This avoids changing the meaning of a shared variable halfway through a journey.

## Evaluate and supported expressions

Evaluate executes JavaScript entered in its script editor. Configure named script outputs and branch names, then test with input values in the node's Test dialog. Custom references use `$(Name)`; node references use `$(n2.sms.timestamp)`. The documentation identifies Start as node 2, but the picker remains the safest reference source. Numeric results may display a decimal portion; converting the final value to a string suppresses it. The documented library loader is `includeJs(...)`; `imi_general` provides `IMI_GENERAL.typeof`, `IMI_GENERAL.length`, `IMI_GENERAL.unicodeToString`, and `urlEncode`. AI-assisted generation requires the Bot Builder app and still requires testing. The page does not establish an ECMAScript version, Node.js APIs, browser APIs, package installation, or async/network support. [Evaluate node](https://help.webexconnect.io/docs/evaluate-node).

**Engineering recommendations:**

- Use Branch for comparisons, Data Parser for extraction, Data Transform for templates, and HTTP/Integration nodes for network operations. Reserve Evaluate for computation those nodes do not express clearly.
- Treat inserted variables as platform substitution, not automatically safe JavaScript parameter binding. Test apostrophes, quotes, newlines, backslashes, empty values, and Unicode before accepting a script. Do not paste customer text directly into executable code based on an assumed escaping rule.
- Parse quantities intentionally and preserve phone numbers, IDs, account numbers, and OTPs as strings. Leading zeroes and large integers are data, not arithmetic.
- Explicitly distinguish missing, empty, zero, false, and an invalid number. A fallback must not convert malformed customer input into a successful business result.
- Use the node Test result and an actual flow execution to validate syntax and result types. A local Node.js test can test an algorithm but cannot prove Connect compatibility.

Example **algorithm specification**, intentionally not paste-ready Connect script:

```text
input: quantity as text, unit price in integer minor currency units
reject if quantity contains anything except digits
convert quantity; require 1 <= quantity <= configured business maximum
calculate total in integer minor units
output: normalized quantity, total, validation status
route: valid / invalid / missing
```

Bind the input through the current node UI, then test the actual implementation. Define whether whitespace is accepted before conversion.

## Parsing and rendering

| Tool | Configure | Result and caution |
| --- | --- | --- |
| Data Parser | Source variable; JSON or XML; representative sample; Parse; select paths; assign output names; Test | Extracts chosen values. The sample teaches extraction; it does not establish that every live response includes those values. |
| Data Transform | Input variable; JSON or XML; VTL template | Uses Velocity Template Language, not JavaScript. The documented result is `dataTransform.output`; HTTP responses are described as already stringified. |

Sources: [Data Parser](https://help.webexconnect.io/docs/data-parser-node), [Data Transform](https://help.webexconnect.io/docs/data-transform-node).

**Engineering recommendation:** save representative success, empty-result, error, null-field, array, and malformed payload fixtures with each flow specification. Parse only necessary paths. Validate a required field before business use. Render structured JSON/XML using a serialization-aware mechanism and verify the resulting payload; text substitution alone is not proof of valid escaping.

## Page and child-flow boundaries

The Page Connector guide says flow variables are not shared automatically across pages and recommends custom variables. The Call Workflow comparison instead says all variables can be referenced across pages. These statements conflict. Both sources support custom variables as the explicit transfer mechanism, and Call Workflow states only parent custom variables are referenceable by the child. [Page Connector](https://help.webexconnect.io/docs/page-connector-node), [Call Workflow](https://help.webexconnect.io/docs/call-workflow-node).

**Engineering rule for this knowledge base:** define custom-variable input/output contracts at page and child-flow boundaries. Verify producer output → custom variable → destination usage in a tenant execution. Do not assume a node reference remains available merely because it exists on another page. Do not infer synchronous function-return semantics from the name Call Workflow; validate the intended continuation path.

Example contract:

| Variable | Producer | Representation | Contract |
| --- | --- | --- | --- |
| `CustomerChannelId` | Entry adapter | String | Exact identifier for the chosen channel; never reuse a different channel's ID. |
| `BusinessRequestId` | Calling system | String | Stable for one requested business action; not interchangeable with a transaction ID. |
| `ValidatedAmountMinor` | Validation module | Integer representation | Set only on successful validation. |
| `ModuleStatus` | Module completion path | Enumerated string | `SUCCESS`, `REJECTED`, `UNAVAILABLE`; initialize before invocation. |
| `SafeErrorCode` | Error adapter | String | Operational classification, excluding secrets and raw customer content. |

These names and values are suggested conventions, not reserved product fields.

## Documentation discrepancies to resolve with the picker

| Issue | Evidence | Working rule |
| --- | --- | --- |
| HTTP namespace/case | HTTP reference lists `https.responseBody`; Parser example uses `http.responsebody`; Transform example uses `http.responseBody`. | Use the configured HTTP node's output picker, preserve exact case, and test the reference. |
| Variable naming | Custom-variable tutorial permits alphanumeric names; HTTP extraction permits additional characters. | Use alphanumeric custom names. Do not generalize an extraction naming rule to custom variables. |
| Page visibility | Conflicting guidance described above. | Pass named custom values explicitly and test the boundary. |

HTTP evidence: [HTTP Request](https://help.webexconnect.io/docs/http-request-node). The remaining sources are linked in their sections above. These are documented inconsistencies, not observed tenant failures.

## Data-focused acceptance cases

| Case | Expected design behavior |
| --- | --- |
| Required property missing or `null` | Controlled invalid/unavailable path; no accidental send using an empty destination. |
| Identifier has leading zeroes or exceeds safe integer size | Value preserved as text. |
| JSON contains quotes/newlines/emoji | Parsing succeeds and outbound body remains valid. |
| Error response has a different schema | Error classification occurs before reading success-only paths. |
| Upstream node was skipped | No reliance on its output; explicit default or alternative producer. |
| Child invoked from two parent flows | Contract works for both without parent node-ID dependencies. |
| Node copied/recreated | Picker bindings rechecked; old node IDs not assumed valid. |
| Sensitive input enters the flow | Redacted operational logging; no blanket debug snapshot of real customer content. |

See [node reference](04-node-reference.md) for concrete configuration fields and [lifecycle](02-flow-lifecycle.md) for launch validation.
