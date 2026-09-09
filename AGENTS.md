# Webex Connect knowledge-base workspace

Read `/home/dgk/workspace/AGENTS.md` once if not already in context. Start with
`README.md`, `knowledge/00-map.md`, and the task-relevant chapter. This is a
knowledge-base/tooling project, not a deployed application.

The user's priority is **primarily AI Agent flows**, with **email and SMS** as
the unifying channels. Lead documentation, examples and retrieval from chapters
13/14. The mission is to document how to build flows, not deliver a production
flow. An explicitly allowed sample experiment is evidence gathering only.

## Current mission boundary

The user explicitly requires **READ-ONLY Webex Connect inspection**. Do not
change existing flows, service/asset/integration configuration, credentials,
logging settings, publication state or contact policies. Do not invoke flows,
send messages, or call mutation APIs as a test. A narrow exception allows a
temporary flow solely for sample/field inspection; avoid saving it where
possible. Record any temporary residue. Control Hub and AI Agent Studio are strictly
read-only; the Connect sample exception does not apply there. Local KB, skill and tooling edits are
authorized. A future explicit user instruction can define a different task scope.

## Evidence and implementation

- Search locally with `python scripts/search_kb.py`; exact fields and schemas
  are in `sources/cache/`. The source inventory records acquisition, version and
  hashes. Do not replace a missing file or unsuccessful fetch with a guessed fact.
- Keep general platform facts, engineering recommendations, historical video
  demonstrations and tenant UI observations distinguishable. Configuration
  visibility is not execution evidence. Never conflate Connect with Contact
  Center's separate voice Flow Designer.
- Cite primary source URLs for authored facts. Retain compact paraphrase and
  documented contradictions; raw source captures are research material rather
  than publishable original content.
- Use `.venv` and the locked requirements for transcription. Do not replace an
  existing environment or read browser cookies/credentials to bypass failed
  caption access. Local ASR, local files, and public vendor transcripts are
  supported alternatives with separate provenance.
- `skills/webex-connect-flows/` is canonical; the global skill is a symlink to
  it. Keep paths and the discoverable metadata coherent when moving it.
- Use constructive, proportionate, non-perfectionistic QA. Check material
  defects and practical behavior against this task, not speculative completeness.
  Preserve the same framing in any delegated QA. Avoid duplicate independent
  reviews of a unit already reviewed; the parent integrates and verifies fixes.
- If using the economical agent, first qualify it for the exact bounded task.
  Its prior task-specific qualification in `evidence/` did not establish
  sufficient technical synthesis capability; do not treat that as a permanent
  ban or a substitute for a new relevant qualification.
