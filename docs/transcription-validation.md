# Transcription validation — 2026-09-08

The workflow produced transcripts from three complete official YouTube recordings, including the requested AI Agent and email focus. YouTube captions were blocked from this machine, while audio download followed by local ASR worked. Separate official Vidcast transcripts were also imported successfully by the video-curation workflow. Synthetic speech was used only to validate a known-answer ASR fixture.

## Executed environment

| Component | Observed version |
|---|---|
| Python | 3.13.12, existing `.venv` preserved |
| youtube-transcript-api | 1.2.4 |
| yt-dlp | 2026.8.19 |
| webvtt-py | 0.5.1 |
| faster-whisper | 1.2.1 |
| CTranslate2 | 4.8.2 |
| ASR settings | `small`, CPU, int8, four threads, beam size 5, VAD enabled, English |

`scripts/setup_venv.sh --with-asr` completed using the generated SHA-256-locked requirements. `uv pip check --python .venv/bin/python` reported all installed packages compatible. `ffmpeg` and `espeak` were present on the machine; the workflow did not install system packages or modify another project.

## Real YouTube recording

Source: [Getting started with Webex Connect](https://www.youtube.com/watch?v=I041FVBzU_s), Webex CPaaS Solutions, published 2023-09-19. Downloader metadata established publisher, publication date and duration. The source video is **1,828 seconds (30:28)**.

Initial captions-only command:

```bash
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --title 'Getting started with Webex Connect' \
  --languages en,en-GB \
  --output-dir transcripts/getting-started-webex-connect
```

It failed with `IpBlocked` on `youtube-transcript-api` after 1.319 seconds, then HTTP blocking on the alternate `yt-dlp` caption route after 2.179 seconds. Both failures are retained in [failure.json](../transcripts/getting-started-webex-connect/failure.json). No transcript was invented from title/description metadata.

The subsequent audio route changed the acquisition method and skipped those already-failed caption paths:

```bash
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --title 'Getting started with Webex Connect' \
  --allow-asr --asr-only --model small --timeout 180 \
  --output-dir transcripts/getting-started-webex-connect-asr
```

This succeeded: **8.081 seconds for audio download, 233.389 seconds for ASR, and 397 nonempty timestamped segments**. The last speech segment ends at 1,809.780 seconds. The entire recording was provided to the ASR engine with VAD; silence/non-speech spans need not have output segments. The temporary audio was removed after completion; its SHA-256 is retained in metadata.

- [Readable transcript](../transcripts/getting-started-webex-connect-asr/transcript.md)
- [JSON segments](../transcripts/getting-started-webex-connect-asr/transcript.json)
- [SRT](../transcripts/getting-started-webex-connect-asr/transcript.srt)
- [Metadata and hashes](../transcripts/getting-started-webex-connect-asr/metadata.json)

The transcript is useful source evidence, with visible errors in product/proper names (for example, “CPaaS” is rendered as “see-pass”). Those words remain unedited. There was no full reference transcript against which to measure this recording's word-error rate, and the result is **not marked human reviewed**. Exact field names, screen-only configurations and numbers still require the official text or visual source.

## AI Agent and email priority recordings

Both official Webex CPaaS Solutions webinars were downloaded in full and transcribed locally with the same `small` CPU/int8 settings. Runs proceeded concurrently with four CPU threads each on the observed 32-core machine. Previously blocked caption methods were skipped; no tenant interactions occurred.

| Source | Published | Duration | Segments | Download / ASR time | Artifact |
|---|---|---:|---:|---|---|
| [AI Agent Ask the Expert](https://www.youtube.com/watch?v=AGDmhRoNFT4) | 2024-12-03 | 43:17 | 379 | 15.046 / 430.296 seconds | [transcript](../transcripts/ai-agent-ask-expert-asr/transcript.md) |
| [Email Ask the Expert](https://www.youtube.com/watch?v=5TzxFpDzIPs) | 2023-12-19 | 41:34 | 242 | 11.220 / 436.343 seconds | [transcript](../transcripts/email-ask-expert-asr/transcript.md) |

Their canonical downloader titles were `CPaaS Ask the Expert 202411` and `CPaaS Ask the Expert 202311`. Transcript display titles are topical labels supplied to the CLI, explicitly marked `title_provenance: user-supplied` in metadata. The catalog records the source identity and historical context.

```bash
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=AGDmhRoNFT4' \
  --title 'Webex AI Agent — Ask the Expert' \
  --allow-asr --asr-only --model small --timeout 180 \
  --output-dir transcripts/ai-agent-ask-expert-asr
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=5TzxFpDzIPs' \
  --title 'Webex Connect Email — Ask the Expert' \
  --allow-asr --asr-only --model small --timeout 180 \
  --output-dir transcripts/email-ask-expert-asr
```

Artifact SHA-256 checks and JSON↔SRT millisecond round trips passed for both. The AI Agent recording has one explicit timing limitation: its final closing segment ends at **2,603.420 seconds**, exceeding downloader-reported duration **2,597 seconds by 6.420 seconds**. Its start is within the video. Raw output was preserved; no silent clipping or correction was applied. The precise cause is unverified, and this final ASR boundary must not be treated as an exact source time. Curated technical sections occur earlier. Email's last segment ends at 2,482.520 seconds, within its 2,494-second source duration. See [artifact-validation.json](../transcripts/artifact-validation.json) for the checks and warning.

These recordings are historical demonstrations. The AI Agent session precedes later release changes; use current official text for current builder fields and availability. Neither recording has a full human-corrected transcript or measured whole-video word-error rate.

## Other real-video execution evidence

The short official [bot/agent chat summarization demo](https://www.youtube.com/watch?v=Yc7ihG6PjKk) was attempted with captions followed by audio. Caption routes were blocked; audio downloaded successfully, but ASR returned no nonempty speech. [Failure evidence](../transcripts/bot-agent-chat-summarization/failure.json) records both facts. This is not counted as a transcript. Silence/music, a visual-only demonstration, or ASR/VAD limitations could explain that result; the transcript tool alone cannot determine which.

Video curation independently retrieved public vendor-hosted transcript JSON and used this tool's local VTT ingestion on three technical webinars:

| Imported source | Segments | Artifact |
|---|---:|---|
| Webex Connect APIs and flows for CX automation | 554 | [transcript](../transcripts/vidcast-api-flows/normalized/transcript.md) |
| Webex Connect integrations | 483 | [transcript](../transcripts/vidcast-integrations/normalized/transcript.md) |
| RCS messaging | 344 | [transcript](../transcripts/vidcast-rcs/normalized/transcript.md) |

Their source JSON, VTT and metadata are retained alongside the normalized outputs. Their acquisition is separate from the blocked YouTube caption endpoints and does not establish that the YouTube caption routes worked. See the video source catalog and `evidence/video-research/fetch_vidcast.py` for that source adapter.

## Known-answer local speech test

The fixture contains four short engineering instructions, authored for validation and spoken by `espeak`. It is **not source material about Webex Connect** and must not be included as tutorial evidence.

```bash
espeak -s 135 -v en-us -w transcripts/fixtures/local-speech.wav \
  'A flow starts with an event. Validate the input before sending a message. Route errors to a fallback. Test the flow before publishing.'
.venv/bin/python scripts/transcribe.py transcripts/fixtures/local-speech.wav \
  --allow-asr --model small \
  --title 'Synthetic speech ASR validation fixture' \
  --output-dir transcripts/local-asr-validation
```

The initial run completed in 14.890 seconds, produced two segments from 10.464 seconds of audio, and reproduced all **23 normalized reference words exactly**: Levenshtein word distance 0, WER 0.0. A later run used `--offline --overwrite` to exercise the cached model and final subprocess wrapper. The retained [accuracy.json](../transcripts/local-asr-validation/accuracy.json) records reference, hypothesis and calculation. This validates local ASR functionality on that fixture, not general speech-recognition accuracy.

## Offline component checks

```bash
.venv/bin/python -m pytest tests/test_transcribe.py -q
```

**27 tests passed.** Tests cover known single-video URL shapes and host validation; manual-caption and requested-language selection; VTT→JSON→SRT millisecond round trips; preservation of technical angle-bracket text; SHA-256 provenance; duplicate-caption behavior; invalid timestamps; timeout failure records and process-group termination; output protection; and no false transcript after failure. Five added regression cases cover staged-write failure, commit failure with successful rollback, commit and rollback failure with retained backup, successful replacement preserving companion review files, and an interrupted commit restoring originals. Tests use offline fixtures and mocks where appropriate. They do not substitute for the real execution evidence above.

Independent QA found that the initial overwrite implementation deleted prior files before writing replacements; the controlled failure is preserved in `evidence/qa/overwrite-io-failure-result.json`. The implementation now stages the complete bundle before moving originals and restores their directory on a caught commit error. If restoration itself fails, the backup is retained and its path reported. The regression cases verify byte-for-byte preservation. Parent integration owns the fix readback; no second independent QA pass was launched.

Limits of verification: no successful direct YouTube-caption download, no GPU/CUDA run, no full human correction or word-error benchmark of the Webex recording, and no verified image/OCR interpretation of its screen-only settings. Current documentation and visible source evidence govern exact flow configuration.
