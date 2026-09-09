# Mastery path: reusable AI Agent flows

Mastery means producing an implementable agent build packet and, when separately
authorized, demonstrating its business behavior. Start with [agent ingestion](../docs/agent-ingestion.md)
and use the local references as needed. The default exercise is **design-only**:
synthetic fixtures, expected results, and execution status `not_run`. Current
inspection authorization does not permit configuring existing flows, invoking
actions, sending messages, or publishing.

| Stage | Study | Exercise and evidence of competence |
|---|---|---|
| 1. Map ownership | [Platform](01-platform-and-design.md), [AI Agent flows](13-ai-agent-flows.md) | Separate Studio agent, Connect conversation flow, fulfillment flow, channel assets, and business system; name their dependencies |
| 2. Prepare knowledge | [AI Agent knowledge and instructions](13-ai-agent-flows.md#3-configure-the-studio-agent-and-knowledge) | Define scope, authoritative sources, answer fixtures, unavailable-answer behavior, and content revisions |
| 3. Specify one operation | [Fulfillment](13-ai-agent-flows.md#4-autonomous-action-fulfillment-exact-connect-setup), [API contracts](10-api-contracts.md) | Define action inputs, validation, backend request, result schema, business rejection, and technical failure |
| 4. Trace connected samples | [Sample walkthroughs](15-sample-flow-walkthroughs.md) | Explain producer-to-consumer mappings, outcome edges, loop state, and return paths; distinguish observed artifacts from interpreted diagrams |
| 5. Add SMS | [Email/SMS recipes](14-agent-email-sms-recipes.md), [channels](05-channels.md) | Specify sender/recipient identity, current message, agent turn, reply rendering, timeout, and escalation |
| 6. Add email | [Email/SMS recipes](14-agent-email-sms-recipes.md), [variables](03-variables-and-expressions.md) | Adapt identity, thread handling, quoted-text policy, attachments, and output formatting while preserving the business contract |
| 7. Handle failures and handoff | [Operations](07-testing-and-operations.md), [human routing](06-integrations-and-contact-center.md) | Trace invalid input, duplicate request, backend timeout, delivery failure, unavailable human, and ownership transfer |
| 8. Prepare implementation | [Lifecycle](02-flow-lifecycle.md), [build packet](../templates/agent-flow-build-packet.yaml) | Supply exact node fields/outcomes, unresolved bindings, acceptance cases, and release/rollback criteria |

## Capstone

Design one reusable customer-support agent that answers from curated knowledge
and performs **one fulfillment business operation**, such as an authenticated
order-status lookup. Provide both email and SMS adapters around the same agent
and operation. Reuse the business contract while making each channel's message,
identity, session/thread, and delivery decisions explicit.

Complete the [agent flow build packet](../templates/agent-flow-build-packet.yaml)
so another builder can proceed without repeating architecture research. Include:

- Agent purpose, instructions, knowledge provenance, and source-supported answer cases.
- Action input/output schemas, required values, validation, backend authentication reference, and result mapping.
- Node topology, exact documented fields/outcomes, proposed custom variables, and unresolved tenant picker references.
- Channel response formatting, customer/conversation/session identifiers, handoff context, and closure ownership.
- Expected outcomes for success, missing input, no match, backend rejection/timeout, duplicate request, no reply, delivery failure, and failed handoff.

If the chosen operation writes data, add its idempotency and ambiguous-result
reconciliation contract. Keep expectations separate from observations; every
unexecuted case remains `not_run`. A plausible diagram or sample payload is not
proof of a successful agent response, business operation, or message delivery.

## Review and later execution

Review whether a builder can fill every required field, connect material
outcomes, preserve identities, and recognize business completion. Resolve
material missing contracts without expanding the capstone into unrelated
features. Use the [video guide](09-video-guide.md) for demonstrations, checking
current references for exact semantics.

Later execution requires explicit authorization for the relevant tenant changes,
action calls, messages, and publication. When authorized, record actual versions,
transaction evidence, downstream results, and channel observations separately.
Update reusable guidance only from source-backed findings or clearly labeled
execution evidence.
