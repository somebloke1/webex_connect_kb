# Video library validation — 2026-09-08

The catalogue contains 15 unique video IDs and URLs: 13 official recordings and two secondary training sources. Evidence separates three acquired vendor transcripts, three acquired local ASR transcripts, and nine unreviewed recordings. The six transcript-backed recordings total 16,060.414 seconds (about 4 h 27 m 40 s), with 2,399 segments. Full-video transcription does not imply every passage or video frame was reviewed; review scopes are explicit.

The original video-library unit contained four transcript-backed recordings, 1,778 segments, and 10,969.414 seconds of media. Executed checks for that unit:

- All catalogue rows parse as JSON; required publisher/date/duration/evidence paths are present; every declared working transcript path exists.
- Current guide and integration-note local links resolve in this workspace. Raw working transcripts are intentionally ignored and are not prerequisites for the curated learning points.
- All three public Vidcast caption files successfully passed `scripts/transcribe.py` local subtitle import: Masterclass 554, Integrations Studio 483, RCS 344 segments.
- The reusable public Vidcast adapter independently retrieved RCS captions, validated 344 ordered nonempty segments, and recorded provenance/hash matching its VTT.
- Real official YouTube audio downloaded and local faster-whisper `small` ASR completed for Getting started, producing 397 segments. Model and package versions, input/output hashes, and timings are in `getting-started-asr-evidence.json`. YouTube caption attempts failed and remain separately recorded; the successful audio route does not erase that result.

One independent bounded QA pass reviewed the catalogue, guide, integration notes, and adapter. Titles, dates, durations, counts, hashes, evidence classification, and local links matched the recorded evidence. It identified two concrete adapter defects: failed-output directories could overwrite `failure.json`, and null caption text became the literal string `None`. Both were corrected. Targeted offline regressions then verified existing failure evidence remains unchanged without any network request, and non-string caption content fails without producing a VTT transcript.

## AI Agent and email priority extension

The November 2024 AI Agent session and November 2023 email session each acquired real audio and completed local faster-whisper `small` ASR: 379 and 242 segments respectively. Existing blocked-caption evidence remains distinct from those later successful audio acquisitions. The catalogue preserves their canonical publisher titles, session months, upload dates, and source-specific review scopes; user-supplied display titles are identified in the ASR evidence.

The guide now leads with AI Agent, email, and SMS. New curated notes contain ten substantive intervals per priority recording, with a short paraphrase budget and current-document comparisons. The AI Agent callback implementation is explicitly pre-release; the current AI Agent Start/Flow Outcomes fulfillment contract takes precedence. The email notes identify historical sender/recipient UI drift and link current channel and recipe detail.

Focused curator checks in [priority-source-validation.json](priority-source-validation.json) verify 15 unique IDs/URLs, all declared evidence/working paths, 33 local guide/note links, and all 20 new interval endpoints against actual transcript segment boundaries and media duration. This did not repeat the original full-unit QA. Initial timestamp-check code omitted the AI notes' trailing bold colon, yielding no matches; allowing that punctuation produced the recorded successful check without changing source intervals.

The AI Agent raw transcript's final endpoint exceeds reported media duration by 6.42 seconds. That uncertainty is retained and disclosed; all curated intervals end before 35:25. No whole-recording word-error rate, human review, video-frame review, or tenant acceptance result is claimed. Acquisition details, hashes, and runtime are recorded in [AI Agent evidence](ai-agent-asr-evidence.json) and [email evidence](email-asr-evidence.json).

Limits: no visual frame review, human accuracy certification, or live-tenant execution was performed. Historical demo shortcuts and future-feature statements are not treated as present product guarantees. The anonymous Vidcast endpoint is an observed public-player interface, not a promised stable developer API. Caption generation/editing provenance is unspecified by the retrieved vendor response.
