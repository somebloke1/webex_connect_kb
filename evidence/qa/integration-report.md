# Independent integration QA — 2026-09-08

## Result

The installed skill and local KB support the requested order-status design without broad research. The completed [independent forward-test build packet](forward-test-order-status.md) covers exact documented fields, variable/source mapping, identity verification, SMS correlation, bounded input/dependency retries, durable duplicate handling and a concrete candidate WxCC handoff lifecycle. Unknown tenant assets, actual business APIs, approved identity policy and version-specific picker values are explicitly unbound. No deployment or runtime claim was inferred from documentation.

One independent, constructive and proportionate QA pass was performed. Two material defects were found and reported to the parent. The parent reports the retry correction applied and the transcription author is fixing overwrite preservation; the parent owns focused final verification. No additional technical finding arose from this bounded pass.

## Material findings

| Finding at reviewed snapshot | Evidence and impact | Practical correction / disposition |
|---|---|---|
| Retry example in `knowledge/04-node-reference.md`, original lines 135–145, initialized `RequestAttempt=0`, tested `< MaximumAttempts` after execution, and incremented only on retry | With `MaximumAttempts=3`, calls occur at counts 0, 1, 2, 3: four actual calls. This conflicts with the recipe's once-per-attempt convention and can exceed the chosen dependency budget. | Increment before each request, define maximum as including the first attempt, and test remaining time before starting each attempt. Parent reports this correction applied. |
| `scripts/transcribe.py`, snapshot lines 408–411, deleted existing output artifacts before `write_artifacts` completed | Injecting an output-write `OSError` after a valid subtitle import caused exit 1 and left only `failure.json`; all four prior transcript/metadata artifacts were lost. [Reproduction result](overwrite-io-failure-result.json). This contradicts the workflow's stated failed-overwrite preservation contract. | Generate replacement artifacts completely in staging; promote them with prior-output preservation and rollback on failure. Add a write-failure regression case. Fix delegated by parent to transcription author, in progress at report time. |

The write-failure probe altered only a dedicated synthetic QA output directory. It neither damaged a real transcript nor changed implementation or test files. Ordinary retrieval/import failure before output writing already preserves existing artifacts successfully.

## Executed local checks

| Check | Observed result |
|---|---|
| `.venv/bin/python -m pytest tests/test_transcribe.py -q` | **22 passed in 0.14 seconds** at the reviewed snapshot. |
| `uv pip check --python .venv/bin/python` | **41 packages compatible.** |
| Fresh independent WebVTT CLI import | Success; millisecond times, leading-zero identifier text, angle-bracket comparisons, and decoded entity text preserved. |
| Provenance and hashes | Source-file and all three artifact SHA-256 values matched; user-supplied title was labeled; local captions stayed `local-unverified`, with `human_reviewed=false`. |
| Refusal to replace output implicitly | Repeating the command without `--overwrite` returned usage status 2. |
| Invalid import with explicit overwrite | Returned status 1; original transcript/metadata bytes remained unchanged beside failure evidence. |
| Fresh offline local ASR | `small`, CPU/int8, cached model, no network route; completed in **2.576 seconds**, two segments from 10.464 seconds of fixture audio. Output exactly matched all four authored fixture sentences. |
| Real-video artifact integrity | Verified segment counts and all artifact hashes for the 397-segment YouTube ASR transcript and 554/483/344-segment Vidcast imports. This checked retained artifacts, not fresh network retrieval or full transcription accuracy. |
| Search interface | Exact HTTP Request query ranked the correct local reference first; `sms.mo` retrieved Receive; handoff query retrieved recipes/design. Search resolves repo root independently of caller cwd. |
| Synthetic-evidence separation | Transcript search excluded the known synthetic ASR fixture; only normalized real-source transcript artifacts are included. |
| Global skill installation | Global `/home/dgk/.codex/skills/webex-connect-flows` symlink resolves to the repository skill; `agents/openai.yaml` is present and invokes the skill. |

Detailed results: [local tool checks](local-tool-checks.json), [artifact/provenance checks](provenance-checks.json), [fresh offline ASR metadata](local-asr/metadata.json), [fresh offline ASR output](local-asr/transcript.json).

The subtitle fixture's YouTube URL is deliberately supplied test metadata, not a claim that its two authored sentences came from that video. Its title and location identify it as synthetic independent QA material; it is outside the searched `transcripts/` corpus.

## Review coverage and limits

Reviewed the installed skill, chapters 00–04, 08 and 11, build-brief template, transcription workflow/docs/code/tests, source/search interfaces, and the exact cached fields needed for the forward test. Chapters 05–07 were used for interface integration and task design; their completed independent content review was not repeated. Chapter 10 was read for orientation but its technical review was left to the already-running dedicated API QA pass. The detailed source crawler was not re-reviewed.

At the relative-link check, `knowledge/12-tenant-observations.md` and `docs/transcription-validation.md` were in flight. The validation document subsequently arrived and was read. README subsequently arrived. The parent owns the final whole-repo link/entrypoint check after the tenant chapter arrives; temporary missing files were not reported as completed-deliverable defects.

No Webex Connect browser, tenant API, configuration, flow, message or test was touched during this QA pass. No external requests, messages or economic-agent delegation were used. Fresh ASR execution used the existing local speech fixture and cached model. No claims are made about GPU behavior, successful direct YouTube caption acquisition, screen-only video content, general ASR accuracy, or any live flow execution.

The subsequent user emphasis on AI Agent, email and SMS introduces additional material units outside this bounded pass. This report does not claim to review newly arriving chapters or ASR additions for that scope.
