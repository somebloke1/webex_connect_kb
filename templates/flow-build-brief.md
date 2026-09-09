# Flow build brief

This is a design document, not a Webex Connect import format. Replace bracketed
values with the actual contract; do not invent tenant asset IDs or node outputs.

## Outcome and environment

- Business result and success measure: [result]
- Tenant / observed product version / service / draft version: [values]
- Channel assets, identities and approved recipients: [values]
- Trigger and triggering system: [event, sample, authentication]
- Expected traffic, peak rate, response deadline and maximum session lifetime: [values]
- External systems, ownership and source of truth: [values]
- Scope authorized by the user: [design / draft build / test / publish]

## Data contract

| Logical name | Type / required / default | Origin and exact picker reference | Scope / lifetime | Sensitivity / log handling |
|---|---|---|---|---|
| eventId | string / required / none | [trigger output] | [custom variable] | [policy] |
| customerKey | string / required / none | [identity system] | [lifetime] | [mask] |
| conversationKey | string / conditional / none | [channel-specific reference] | [lifetime] | [mask] |

Record invalid, missing, empty and unexpected-type behavior. Give each mutable
value one owner. Preserve identifiers as strings. Define cross-page and
parent/child-flow inputs and outputs explicitly.

## Node configuration and connections

| Node ID / purpose | Actual palette type | Field → literal or exact variable reference | Outcome label → next node or end | Timeout / retry / duplicate behavior |
|---|---|---|---|---|
| N01 / accept event | Start | [actual fields] | [actual outcome] → N02 | [policy] |

List every outcome displayed by each configured node. Distinguish the product's
exact edge label from your descriptive name. Mark intentionally unused outcomes
and how they terminate. Attach a diagram when branches are hard to inspect.

## State and failure contracts

- Session/correlation key and concurrent-event policy: [definition]
- Duplicate event behavior, including after the original flow ends: [definition]
- Side effects and business idempotency key: [definition]
- Retry allowlist, maximum attempts, delay and overall deadline: [definition]
- Ambiguous external result (timeout after possible commit): [reconciliation]
- No response, invalid reply, opt-out, human handoff and terminal states: [paths]
- Dependencies and entitlement requirements: [list]

## Verification and release evidence

Use [test-cases.csv](test-cases.csv) as a starting point. Record actual values,
expected side effects, observed edges, transaction IDs (redacted), and verdicts.
Separate configured, tested, live, and end-to-end verified status.

- Unresolved documentation conflicts and tenant observations: [evidence]
- Saved/exported artifact and version: [path or identifier]
- Authorized test recipients and expected external writes: [values]
- Validation results and rollback target: [evidence]
- Publication authorization and actual status: [evidence]

