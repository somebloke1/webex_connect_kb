# Knowledge map and retrieval guide

This library supports Cisco **Webex Connect CPaaS Flow Builder**. It combines
authored explanations, exact locally cached official reference pages, API
schemas/examples, video evidence and a tenant-specific observation layer.

**Primary focus: AI Agent flows.** Start with the
[AI Agent playbook](13-ai-agent-flows.md), then
[email/SMS agent recipes](14-agent-email-sms-recipes.md). The broad reference
corpus supports those designs; it is not a requirement to use every channel.

For agent ingestion, use [the route manifest](agent-index.json) and
[the deterministic workflow](../docs/agent-ingestion.md). Record a design with
[the structured build packet](../templates/agent-flow-build-packet.yaml).

## Start from the problem

| Question | First read | Then retrieve locally |
|---|---|---|
| How do AI Agent conversations and fulfillment flows fit together? | [AI Agent playbook](13-ai-agent-flows.md) | `ai-agent-node`, `configure-fulfilment-flows-for-ai-agent-actions` |
| How do complete samples connect nodes, variables and outcomes? | [Sample walkthroughs](15-sample-flow-walkthroughs.md) | [full sample inventory](../evidence/sample-flows/sample-inventory.json) and [observed graph walkthroughs](../evidence/tenant-samples.md); `--scope samples` |
| How does an agent handle email and SMS? | [Agent email/SMS recipes](14-agent-email-sms-recipes.md) | agent method outputs, email/SMS sender and reply fields |
| How should this journey be structured? | [Platform and design](01-platform-and-design.md), [recipes](08-recipes.md) | `flows-introduction`, `flow-nodes` |
| What starts it, and where does the next reply go? | [Nodes](04-node-reference.md), [channels](05-channels.md) | `start-node`, `receive-node`, `trigger-flow` |
| What exactly goes in a field? | [Nodes](04-node-reference.md) or [channel reference](05-channels.md) | Exact node title; inspect its cached `.md`, output-variable and outcome tables |
| Why is a variable blank or wrong? | [Variables](03-variables-and-expressions.md) | producer node, `transition-actions`, `variable-management-in-flows` |
| How do I call an API? | [Integrations](06-integrations-and-contact-center.md), [API contracts](10-api-contracts.md) | `http-request-node`, actual endpoint operation |
| How do I start a flow from another application? | [API contracts](10-api-contracts.md) | `custom-event-v1`, `api-authentication`, inbound webhook reference |
| How do I reuse logic? | [Variables](03-variables-and-expressions.md), [nodes](04-node-reference.md) | `page-connector-node`, `call-workflow-node` |
| How does human escalation work? | [Integrations and contact center](06-integrations-and-contact-center.md) | exact WxCC / CCE / Engage operation and channel |
| What failed in this transaction? | [Testing and operations](07-testing-and-operations.md) | `console`, `transaction-logs-and-debugging`, exact error code |
| How do I publish, roll back, or migrate? | [Lifecycle](02-flow-lifecycle.md) | version history, import/export, assets/integration restrictions |
| Can I learn from a demonstration? | [Video guide](09-video-guide.md) | timestamped transcript; verify field semantics in current docs |
| What does this particular tenant expose? | [Tenant observations](12-tenant-observations.md) | current authenticated UI; preserve the observation date |

Example commands from the repository root:

```bash
python scripts/search_kb.py 'HTTP Request' --scope sources --limit 4
python scripts/search_kb.py 'responseBody' --scope sources --all --limit 6
python scripts/search_kb.py 'Create Task' --scope sources --phrase --limit 5
python scripts/search_kb.py 'idempotency' --scope knowledge --limit 4
python scripts/search_kb.py 'flow builder' --scope transcripts --limit 3
```

The node reference is compact. The linked source cache supplies exhaustive
field tables and rare-node details; it is part of the usable local library, not
a list of links requiring routine web browsing. `sources/catalog.md` and
`sources/inventory.jsonl` record the actual acquisition result for each source.

## Evidence levels

| Label | What it establishes | What it does not establish |
|---|---|---|
| Official cached documentation | Vendor-described behavior and recorded field definitions | Feature entitlement or exact runtime behavior in every tenant |
| Current release note | Announced change in a specified release | That a particular tenant already runs that release |
| Authored engineering recommendation | Proposed architecture or recovery strategy | A built-in platform guarantee |
| Video transcript / ASR | What was transcribed at that time in that recording | Current field names; ASR may mistranscribe technical names |
| Description / chapter metadata only | Advertised topics and navigation points | That the full video content was reviewed |
| Tenant UI observation | A visible control, field, configured value or palette entry | Successful execution, delivery, external write or availability to other tenants |
| Executed flow evidence | The tested case and its observed boundary | Untested branches, volume or channel configurations |

When sources conflict, state the conflict and use a concrete tenant/node test to
resolve it where authorized. Examples already identified include cross-page
variable visibility, HTTP output namespace/case, custom integration throttle
codes and contact-center identity examples. Follow the relevant chapter's
working rule instead of silently choosing whichever statement is convenient.

## Boundaries and freshness

The capture records documentation versions separately from current release notes.
Do not label the default help-site version as the newest deployed product. Channel
policies, templates, identity changes, tenant limits and controlled integrations
need checking against the captured release context and target tenant when building.

Local-source-first removes repeated broad research. Fresh research remains
appropriate for a missing operation, changed release/channel requirement, source
conflict, or a target tenant capability not covered by the snapshot. Raw source
captures and full transcripts remain local research material; authored chapters
provide the reusable synthesis.
