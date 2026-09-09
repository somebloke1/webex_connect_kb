---
name: webex-connect-flows
description: Document, design, review, or build Cisco Webex Connect AI Agent flows, especially email and SMS journeys, using a local source-backed knowledge base with exact node fields and fulfillment patterns. Also maintain the reference corpus and transcribe instructional videos. Covers Connect Flow Builder, not Webex Meetings or the separate Contact Center voice Flow Designer.
---

# Webex Connect flows

Use the local knowledge base before doing fresh research. Its canonical location
in this installation is `/home/dgk/workspace/webex_connect_kb`; if relocated,
resolve this skill's real path and use its repository root (two levels above the
skill directory). The source tree is also installed as a discoverable global
skill through a symlink. Do not depend on the caller's current directory.

## Find the relevant contract

The primary focus is **AI Agent flows**, followed by **email and SMS**. Begin an
agent task with `knowledge/13-ai-agent-flows.md` and
`knowledge/14-agent-email-sms-recipes.md`. Distinguish a channel flow that calls
an AI Agent from a fulfillment flow triggered by an AI Agent action; their
input/output, waiting and time-limit contracts differ. Legacy Task/QnA Bot pages
are not the current AI Agent node schema. For documentation-only requests,
produce the KB/how-to without implementing a real journey; inspect or experiment
only within the user's expressly permitted sample scope. For this KB mission,
Control Hub and AI Agent Studio are strictly read-only with no sample exception.

1. Read `<KB>/docs/agent-ingestion.md` and select task routes from
   `<KB>/knowledge/agent-index.json`. Read the KB's `README.md` and `knowledge/00-map.md` for coverage and evidence
   levels. Check `sources/coverage.json` / `sources/catalog.md` and the individual
   source metadata for retrieval dates and documentation versions. A documentation
   version, release note, video date and running tenant version are different facts.
2. Search locally: `python <KB>/scripts/search_kb.py "your node or field" --limit 6`.
   Use `--scope knowledge` for decisions, `--scope sources` for exact field
   definitions, `--scope samples` for exact observed node/edge/binding records, and
   `--scope transcripts` for video evidence. Open the returned
   file and relevant section; a search snippet is not sufficient for a conditional
   rule or a complete node configuration.
3. Route to the smallest useful set of chapters:

   | Task | Files below `<KB>/knowledge/` |
   |---|---|
   | AI Agent, Studio actions/tools and fulfillment | `13-ai-agent-flows.md` |
   | AI Agent email/SMS orchestration and concrete recipes | `14-agent-email-sms-recipes.md` |
   | Complete samples: node connections, loops and data handoffs | `15-sample-flow-walkthroughs.md` and the linked full inventory |
   | Platform boundary, service/assets, architecture | `01-platform-and-design.md` |
   | Create, validate, publish, version, import/export | `02-flow-lifecycle.md` |
   | Variable scope, substitution, Evaluate, data contracts | `03-variables-and-expressions.md` |
   | Exact utility node fields, outputs, outcomes | `04-node-reference.md` plus the linked cached node page |
   | Channel setup, sends, receives, identities | `05-channels.md` |
   | HTTP/custom/prebuilt integrations and human handoff | `06-integrations-and-contact-center.md` |
   | Tests, logs, limits, recovery and diagnostics | `07-testing-and-operations.md` |
   | Complete business-flow patterns | `08-recipes.md` |
   | Video demonstrations and evidence status | `09-video-guide.md` |
   | External API authentication, payloads and callbacks | `10-api-contracts.md` |
   | Learning progression and competence checks | `11-mastery-path.md` |
   | Observed tenant UI and validation boundary | `12-tenant-observations.md` |

## Design or build a flow

Turn the business request into a concrete build brief using
`<KB>/templates/flow-build-brief.md` and the machine-readable
`<KB>/templates/agent-flow-build-packet.yaml`. The packet is planning data, not
an importable Cisco flow. Review the closest complete samples and preserve
producer → transformation → consumer bindings, exact outcome edges and terminal
return contracts. For requests to review all samples, enumerate the complete
applicable inventory and track each sample; do not silently sample a subset. Make reasonable routine design choices and
continue authorized work; ask only for information that materially blocks the
specific implementation. Record the channel, trigger, service/assets, external
system contracts, success condition and intended side effects.

Produce the useful parts of a build packet: topology, variable dictionary,
node-by-node fields, exact outcome connections, bounded failure/retry paths,
test fixtures and release status. Reuse the closest recipe, adapting its business
contract rather than treating its logical labels as vendor field names.

- Verify node availability in the actual tenant before promising a feature.
  Copy exact variable references from the configured node's picker. Node IDs,
  field case and channel-specific identities are not interchangeable.
- Use explicit custom-variable contracts across pages/flows. The references
  preserve conflicting vendor wording about cross-page visibility; inspect or
  test the actual boundary before relying on it. Do not assume Call Workflow is
  an ordinary synchronous function returning to its caller.
- Distinguish Send acceptance, delivery, customer reply and business completion.
  Give Receive/session correlation, timeout and late-event behavior a clear design.
- For external writes, handle duplicate events and ambiguous timeouts using the
  business system's actual idempotency/reconciliation contract. Cap retry attempts
  and elapsed time; connect technical failure and business rejection paths.
- Evaluate uses its documented runtime, not a general Node.js environment.
  When execution is authorized, validate variable substitution and escaping with
  real node tests. Do not invent
  APIs, native flow-export JSON, hidden node types, or unsupported script features.
- Preserve existing flow versions and user changes. Follow the authorization
  already present for editing, testing and publication; a knowledge/design request
  by itself does not authorize customer messages or making a flow live.

Report configured, tested, published and end-to-end verified status separately.
Use relevant cases from `<KB>/templates/test-cases.csv`; executed results need
actual transaction and business-boundary evidence. Keep sensitive payloads and
credentials out of the reusable KB. QA is constructive and proportionate: identify
material defects against the requested behavior, fix them, and deliver.

## Maintain evidence and transcribe video

Use `<KB>/docs/source-maintenance.md` and the `sources.py` CLI to refresh only
missing, stale or conflicting sources. Keep source URL, retrieval date, version,
content hash and acquisition status. Prefer current official product/node/API
documentation for semantics; use videos for demonstrations. Tenant observations
can resolve UI questions but do not establish untested runtime behavior.

Use `<KB>/docs/transcription-workflow.md` for the venv workflow. Start with
`<KB>/scripts/setup_venv.sh` (or `--with-asr`), then run
`<KB>/.venv/bin/python <KB>/scripts/transcribe.py --help` for the supported modes.
Caption acquisition and generated ASR are different evidence types. Preserve
timestamps and provenance, label machine-transcription uncertainty, and check
technical spelling/field names against the docs. Do not infer a video's content
from its title or count advertised captions as acquired transcripts. A failed
download is a recorded gap; use an available authorized media/transcript source
or leave the gap explicit after bounded attempts.

The local cache is research material, not a license to republish manuals or full
transcripts. Author compact attributed guidance and keep raw captures separate.
