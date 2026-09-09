# Reproducible local transcription workflow

Run commands from the repository root. Python dependencies live in `.venv`; audio decoding uses the installed `ffmpeg`. The setup script preserves the existing venv and installs hash-locked packages. Tested versions are recorded in [validation evidence](transcription-validation.md).

```bash
scripts/setup_venv.sh                 # captions and subtitle import only
scripts/setup_venv.sh --with-asr      # add local faster-whisper and pytest
.venv/bin/python scripts/transcribe.py --help
```

If creating a new environment, the script uses `uv venv --python 3.13 .venv`. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and your platform's ffmpeg package first. Python 3.11–3.13 is declared; execution evidence currently covers Python 3.13 on Linux. CPU/int8 is the default; a CUDA installation is unnecessary.

## Retrieve a YouTube transcript

```bash
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --languages en,en-GB \
  --title 'Getting started with Webex Connect' \
  --output-dir transcripts/getting-started-new-run
```

The workflow accepts a single YouTube URL or video ID. It first uses `youtube-transcript-api`: original manual captions are preferred across the requested languages, followed by original automatic captions. If that route fails, it makes one causally different `yt-dlp` caption attempt. It does not automatically translate. Region variants such as `en-GB` are accepted for `en`.

Each network route has a 120-second outer deadline and 15-second request socket timeout; downloader retry counts are zero. No paid transcription API, residential proxy, browser-cookie copying, or credentials are required. The wrappers follow the maintainers' [transcript API](https://github.com/jdepoix/youtube-transcript-api#api) and [yt-dlp subtitle options](https://github.com/yt-dlp/yt-dlp#subtitle-options).

## Local speech recognition when captions fail

```bash
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --allow-asr --model small \
  --output-dir transcripts/getting-started-with-asr
```

With `--allow-asr`, failure of both caption paths permits downloading audio and running [faster-whisper](https://github.com/SYSTRAN/faster-whisper#usage). Audio remains local to the machine; model weights may be downloaded from Hugging Face on first use. Temporary audio is deleted after the run. Metadata retains its SHA-256. Default ASR is CPU, int8, four threads, beam size five, VAD enabled, and the first requested language. Regional language tags map to their base language for ASR.

If captions already failed in a recorded run, skip repeated caption requests:

```bash
.venv/bin/python scripts/transcribe.py \
  'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --allow-asr --asr-only --model small --timeout 180 \
  --output-dir transcripts/getting-started-audio-only
```

`--timeout` bounds each network operation; `--asr-timeout` defaults to 3,600 seconds including model loading. YouTube audio download refuses live streams, unknown duration, recordings longer than `--max-video-minutes` (180 by default), and downloads above the 512 MiB compressed-file limit. Avoid raising these limits without considering disk and CPU needs. `.wav` conversion can occupy more disk space than compressed audio.

Use `--model /path/to/local/faster-whisper-model --offline` for a fully local model, or `--model-cache /path/to/model-cache` to choose a cache. The `small` model is a practical default; ASR accuracy for product names, code, numbers and accented speech still needs review. `--initial-prompt 'Webex Connect, webhook, service, flow, node'` can supply vocabulary, and the hint is recorded. Do not silently correct transcript wording: put verified corrections in separate source notes.

## Import legitimately obtained local captions or media

```bash
.venv/bin/python scripts/transcribe.py /path/to/tutorial.vtt \
  --source-url 'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --title 'Getting started with Webex Connect' \
  --output-dir transcripts/imported-tutorial

.venv/bin/python scripts/transcribe.py /path/to/tutorial.mp4 \
  --allow-asr --model small \
  --source-url 'https://www.youtube.com/watch?v=I041FVBzU_s' \
  --output-dir transcripts/local-media-tutorial
```

Subtitle inputs: UTF-8 SRT, WebVTT, YouTube JSON3, a JSON list of `{start, end, text}` / `{start, duration, text}` objects, or this tool's `transcript.json`. Millisecond precision is preserved. Identical adjacent overlapping captions are merged; distinct phrases and repetitions separated by a gap are retained. Partial rolling-caption overlap is intentionally retained in the evidence rather than guessed away. Empty, nonfinite, negative, reversed, or out-of-order timestamps fail.

Local subtitle origin is marked `local-unverified`; a file extension alone cannot establish whether captions were human authored or automatic. Add independently established publisher/method details in a companion source note. For vendor-hosted transcripts, retain the source JSON and the conversion command. Local media uses any audio/video format that faster-whisper's PyAV decoder supports.

## Artifacts and failure meanings

| Artifact | Meaning |
|---|---|
| `transcript.json` | Schema version plus normalized timestamped segments; preferred programmatic input |
| `transcript.md` | Readable transcript; YouTube-source runs include timestamp links |
| `transcript.srt` | Subtitle interchange with millisecond timestamps |
| `metadata.json` | Source, supplied/publisher title, retrieval time, method, language, caption kind, versions, attempts, input hash where available, artifact hashes, and ASR settings |
| `failure.json` | Failed attempt evidence; this is not a transcript |

Exit status `0` means a nonempty transcript was written; `1` means retrieval/import/ASR failed; `2` means a usage error. Existing artifacts are protected by default. Choose a new output directory for a new run; `--overwrite` explicitly replaces prior transcript artifacts after success. Writes are staged in a sibling directory, then committed as a complete directory bundle while preserving companion source/review files. A failed write leaves originals untouched; a failed commit restores the previous directory. If restoration itself fails, the error names a retained backup directory containing the originals. Use one writer per output directory; this is not a concurrent-write or power-loss transaction guarantee.

HTTP 403/429, `IpBlocked`, or a YouTube bot challenge may affect captions while video metadata or audio still work. The maintainer describes [YouTube IP blocking](https://github.com/jdepoix/youtube-transcript-api#working-around-ip-bans-requestblocked-or-ipblocked-exception). This tool reports the affected route, stops its retries, and leaves a local-subtitle/media path. An audio attempt is useful only when media access is permitted; repeated blocked requests are not useful. A vendor's public alternate transcript is also a valid source when its identity is documented.

An ASR error saying no nonempty segments were returned can mean silence/music-only content, language/model mismatch, or a decoder/VAD limitation. Do not infer that a video was understood. Inspect/listen to the source and its visual walkthrough before deciding the next step. Tool errors do not supply flow-building knowledge.

## Turn transcripts into trustworthy flow knowledge

1. Record the exact video identity, publisher, publication date and retrieval method in the source catalog.
2. Read relevant timestamped sections and note demonstrated behaviors, required fields and prerequisites.
3. Verify exact current field names, API signatures, limits and tenant availability against the official text references.
4. Preserve separate labels for source observation, interpretation, and your recommended implementation.
5. Cite the source timestamp in the resulting guide or recipe; distinguish historical demonstrations from current behavior.

An ASR transcript omits screen-only settings, wiring and UI state. Pair spoken material with the official text and relevant visual inspection. `human_reviewed: false` remains the default; neither a successful command nor accurate synthetic speech establishes a fully verified tutorial.

## Verify and refresh

```bash
.venv/bin/python -m pytest tests/test_transcribe.py -q
uv pip check --python .venv/bin/python
```

The tests exercise language/manual preference, URL identity validation, timestamp precision, subtitle round trips, provenance hashes, duplicate-caption handling, timeout reporting, and artifact protection under injected write/commit/rollback failures. Actual network/ASR results are separate in [transcription-validation.md](transcription-validation.md).

YouTube interfaces change. Update direct versions in `pyproject.toml` after checking maintainer releases, then regenerate both locks and rerun validation:

```bash
uv pip compile pyproject.toml --generate-hashes -o requirements.txt
uv pip compile pyproject.toml --extra asr --extra dev --generate-hashes -o requirements-asr.txt
scripts/setup_venv.sh --with-asr
```

The lock files record dependency distributions; model names alone do not freeze upstream model revisions. For repeatable research comparisons, retain a known local model snapshot and use its path with `--offline`, alongside source-audio and output hashes.
