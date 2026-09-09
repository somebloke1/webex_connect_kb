# Webex Connect flow knowledge base

A local, source-backed working library primarily for **AI Agent flows**, with
**email and SMS** as the main communication channels. It supports documenting,
designing and later building Cisco Webex Connect CPaaS flows. Agents should start with the [ingestion guide](docs/agent-ingestion.md) and
[structured build packet](templates/agent-flow-build-packet.yaml). Start with the
[AI Agent playbook](knowledge/13-ai-agent-flows.md),
[agent email/SMS recipes](knowledge/14-agent-email-sms-recipes.md), or the [knowledge map](knowledge/00-map.md)
or invoke **`$webex-connect-flows`**. The skill is installed at
`~/.codex/skills/webex-connect-flows`, linked to the canonical skill in this repo.

The library supplies design methods, exact node/field references, variable and
API contracts, channel behavior, integration lifecycles, failure strategies,
worked recipes, video evidence and reusable build/test templates. Routine work
can be researched locally. Missing tenant bindings, new release behavior and
documented contradictions remain explicit verification points.

## What is here

| Resource | Purpose |
|---|---|
| [Agent ingestion guide](docs/agent-ingestion.md) | Deterministic retrieval, structured graph contracts and implementation handoff |
| [Agent route manifest](knowledge/agent-index.json) | Machine-readable task routing and exact evidence paths |
| [AI Agent flow playbook](knowledge/13-ai-agent-flows.md) | Primary guide: conversational orchestration, Studio tools and fulfillment |
| [Agent email/SMS recipes](knowledge/14-agent-email-sms-recipes.md) | Primary channel plans, turn/session context, replies and business actions |
| [All sample graphs and walkthroughs](evidence/tenant-samples.md) | Full current gallery, AI fulfillment and digital-channel collection |
| [Sample coverage inventory](evidence/sample-flows/sample-inventory.json) | Every collection entry and its actual review/evidence status |
| [Additional source samples](knowledge/16-additional-sample-walkthroughs.md) | SMS/email, task-event and CCE documentation |
| [Connected sample walkthroughs](knowledge/15-sample-flow-walkthroughs.md) | Native samples, documented sequences, node relations and evidence limits |
| [Knowledge map](knowledge/00-map.md) | Route a task to the right chapter and evidence |
| [Platform and design](knowledge/01-platform-and-design.md) | Services/assets, product boundaries and architecture |
| [Lifecycle](knowledge/02-flow-lifecycle.md) | Creating, validating, versioning, migration and publication |
| [Variables and expressions](knowledge/03-variables-and-expressions.md) | Scope, substitution, data types and Evaluate |
| [Node reference](knowledge/04-node-reference.md) | Utility-node fields, outputs, outcomes and constraints |
| [Channels](knowledge/05-channels.md) | Messaging, voice, identities, delivery and receive behavior |
| [Integrations and contact center](knowledge/06-integrations-and-contact-center.md) | Custom/prebuilt integrations, WxCC, CCE and Engage |
| [Testing and operations](knowledge/07-testing-and-operations.md) | Logs, failure diagnosis, retries, limits and evidence |
| [12 worked recipes](knowledge/08-recipes.md) | Node plans, contracts, failure paths and acceptance cases |
| [Video guide](knowledge/09-video-guide.md) | Demonstrations with provenance and timestamps |
| [API contracts](knowledge/10-api-contracts.md) | Auth, event envelopes, callbacks, errors and schema conflicts |
| [Mastery path](knowledge/11-mastery-path.md) | Progressive practical exercises and competence checks |
| [Tenant observations](knowledge/12-tenant-observations.md) | What the authenticated UI actually established |
| [Official source catalog](sources/catalog.md) | Exact cached documentation and API schemas |
| [Coverage manifest](sources/coverage.json) | Machine-readable acquisition counts and scope |
| [Build brief](templates/flow-build-brief.md), [test cases](templates/test-cases.csv) | Reusable implementation handoff and verification |
| [Skill](skills/webex-connect-flows/SKILL.md) | Agent workflow and reference routing |

Captured **2026-09-08**: **534 official sources** — 337 platform-help pages,
176 developer references/prerequisites, 10 AI Agent Studio sources, 10 release/policy
notices, and one Cisco developer tutorial. Full field tables, API schemas and examples are cached
locally alongside URL, version, retrieval time and content hashes. The scope
includes the visible help navigation and selected API/prerequisite navigation;
mobile SDK implementation detail is intentionally outside the flow-building core.
See the manifest for actual acquisition state, not just planned coverage.

The current sample collection has **59 inspected graphs and 59 walkthroughs**:
all 9 gallery templates, all 17 linked AI fulfillment files, and all 33 current
v3.5 digital-channel samples. The inventory preserves **95 evidence entries**,
including source-only tutorials and the separately access-controlled CCE bundle.
The native CCE files require a Cisco.com login/service contract; all 15 named
CCE examples are covered at the published-documentation level.

Default help/API documentation reported version **6.20.0** during capture; the
release catalog includes the **v6.22.0 September 2026 announcement**. Neither
establishes the deployed version of a tenant. Historical demonstrations also
need that distinction. [Release baseline](knowledge/01-platform-and-design.md#release-and-capability-baseline).

## Search offline

The search and source-capture tools use the Python standard library. No API key,
embedding service or database is required.

```bash
gh repo clone somebloke1/webex_connect_kb
cd webex_connect_kb
python scripts/search_kb.py 'packageNum' --scope samples --limit 3
python scripts/search_kb.py 'Receive timeout' --scope sources --limit 5
python scripts/search_kb.py 'https.responseBody' --scope sources --limit 3
python scripts/search_kb.py 'human handoff' --scope knowledge --limit 4
python scripts/search_kb.py 'flow builder' --scope transcripts --limit 3
python scripts/search_kb.py 'Custom Event' --scope sources --json --limit 3
```

Open the matched `.md` reference for a complete table; use `.txt` line numbers
for quick exact-field lookup. Search results distinguish authored guidance,
source documentation and transcripts. Some official pages contain inconsistent
examples: the chapters identify material conflicts and practical working rules.

## Transcribe instructional videos

```bash
scripts/setup_venv.sh --with-asr
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --allow-asr --model small \
  --output-dir transcripts/new-video-run
```

The workflow prefers manual captions, then automatic captions, with a bounded
alternate downloader route and optional local speech recognition. It also imports
local subtitles/media and produces timestamped JSON, Markdown, SRT and provenance.
Dependencies are hash-locked; CPU ASR works without a paid transcription service.
Full setup, refresh, error meanings and commands are in
[transcription workflow](docs/transcription-workflow.md), with actual results in
[transcription validation](docs/transcription-validation.md).

The corpus includes **six real video transcripts** (2,399 timestamped segments,
about **4 hours 28 minutes**) from the 15-source video library; a catalog entry or advertised caption
track is not counted as an acquired transcript. Raw ASR retains technical-name
errors and is not labeled human-reviewed. The video guide separates these
evidence levels and provides verified learning points.

## Maintain and validate

```bash
python scripts/sources.py verify
.venv/bin/python -m pytest tests/test_transcribe.py -q
uv pip check --python .venv/bin/python
```

Use [source maintenance](docs/source-maintenance.md) for targeted refresh and
rebuilding a missing cache. The independent [AI Agent email/SMS build packet](evidence/qa/forward-test-ai-email-sms.md)
shows how an agent used the skill, structured template and local references
without broad research. A [general flow packet](evidence/qa/forward-test-order-status.md)
provides an additional example.
See [validation](docs/validation.md) for final checks and limits.

This project is a **documentation/KB mission**. It does not authorize changes to
existing Webex Connect configurations, messages, API writes or flow publication.
The user's narrow exception permits a temporary flow solely for inspection,
preferably unsaved. Tenant observations document what actually happened.

This private repository includes the official documentation cache, sanitized
sample observations and summaries, and six normalized transcript sets so a
fresh clone supports offline retrieval. Rights remain with their publishers;
the authored guides provide attributed synthesis. These source materials are
research references, not newly authored documentation or a redistribution license.

The venv, downloaded audio/video, intermediate caption files, opaque original
workflow imports, private captures and temporary test output are ignored.
Original-acquisition checks require those local files or reacquisition from the
recorded sources; source-cache verification and sample-summary regeneration work
from a clone. Credentials, browser profiles and customer payloads do not belong
in this library.
