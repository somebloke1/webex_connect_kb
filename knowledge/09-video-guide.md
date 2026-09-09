# Video learning track and evidence guide

Verified **2026-09-08**. [Machine-readable catalogue](../sources/videos.jsonl) contains 15 selected recordings with publisher, date, duration, topic, evidence status, and provenance. **Six official recordings have acquired transcripts and reviewed timecoded notes:** three vendor-captioned webinars and three locally transcribed YouTube videos, including AI Agent and email. They total 2,399 segments across about 4 h 27 m 40 s of recordings. YouTube metadata and caption availability were checked separately; an advertised caption track is not a downloaded transcript.

For the current priority, follow **AI Agent → email → SMS**. Start with the AI Agent learning route below, then the email demonstration and the SMS-oriented historical tutorial. Use the Masterclass and Integrations Studio recordings for supporting API, variable, response, and debugging techniques; RCS is an optional channel extension. Read [node reference](04-node-reference.md), [channel rules](05-channels.md), [integration guidance](06-integrations-and-contact-center.md), and [testing/operations](07-testing-and-operations.md) for implementation details. Historical video UI, sample credentials, hardcoded values, entitlements, future-feature statements, and demo shortcuts are not current configuration authority.

## Priority route: AI Agent, email, then SMS

1. **AI Agent:** Start with the [AI Agent flow contract](13-ai-agent-flows.md) and [AI Agent/email/SMS recipes](14-agent-email-sms-recipes.md), then the [timecoded action and knowledge design notes](../evidence/video-research/ai-agent-ask-expert-learning-notes.md) from November 2024. Use [AI Agent node](https://help.webexconnect.io/docs/ai-agent-node) for the conversation contract and [AI Agent fulfillment](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions) for actions that invoke Connect. They are different flow roles. The recording is a pre-release demonstration: its manual callback return path is superseded by the current fulfillment reference.
2. **Email:** Follow the November 2023 [timecoded email demonstration notes](../evidence/video-research/email-ask-expert-learning-notes.md) with the current [Email node contract](https://help.webexconnect.io/docs/email-node). Separate asset setup, composing the message, receiving a reply, and interpreting delivery status. The notes identify historical sender and recipient-field differences.
3. **SMS:** Read [channel guidance](05-channels.md) and the [AI Agent SMS support recipe](14-agent-email-sms-recipes.md), then use Bucher + Suter's [SMS survey/reminder chapter cues](https://www.youtube.com/watch?v=It3Zq0wdxHg) as supplementary orientation. The latter remains description-only unless a transcript is later acquired.

Avoid deriving modern AI Agent field names from the misleadingly titled [Configuring flows with AI Agent Node](https://help.webexconnect.io/docs/configuring-flows-with-ai-agent-node) page alone: the cached body largely describes older QnA/Task Bot loops and legacy `taskbot`/`bot` variables. The dedicated AI Agent node and fulfillment references above supply the relevant contracts.

## Transcript-backed recordings

| Recording | Publisher | Session or publication date; recording length | What was actually inspected |
|---|---|---|---|
| [AI Agent Ask the Expert](https://www.youtube.com/watch?v=AGDmhRoNFT4) | Webex CPaaS Solutions | 2024-11 session; 43:17 | 379 local ASR segments; knowledge/action demonstration and implementation Q&A reviewed; [ten intervals](../evidence/video-research/ai-agent-ask-expert-learning-notes.md) |
| [Email Ask the Expert](https://www.youtube.com/watch?v=5TzxFpDzIPs) | Webex CPaaS Solutions | 2023-11 session; 41:34 | 242 local ASR segments; email portion 11:24–40:26 reviewed; [ten intervals](../evidence/video-research/email-ask-expert-learning-notes.md), excluding sales introduction |
| [Webex Connect Masterclass](https://app.vidcast.io/share/debc5583-a8ff-4a54-9a2e-c40b867f7be3) | Webex Developer Evangelism | 2024-02-28; 59:01 | 554 timestamped captions; build/debug portion 29:29–54:42 reviewed in detail |
| [Reusable integrations with Integrations Studio](https://app.vidcast.io/share/31b01641-f081-4163-886b-5f0612b37033) | Webex Developer Evangelism | 2025-02-26; 53:48 | 483 timestamped captions; operational passages checked against current custom-node docs |
| [Branded RCS messaging](https://app.vidcast.io/share/1b8cf04c-353a-4dda-a515-2c1fb9b9b483) | Webex Developer Evangelism | 2024-06-26; 39:31 | 344 timestamped captions; 11:54–39:22 reviewed, especially 21:05–33:09 demonstration |
| [Getting started](https://www.youtube.com/watch?v=I041FVBzU_s) | Webex CPaaS Solutions | Published 2023-09-19; 30:28 | 397 local ASR segments; custom integration and appointment demonstration passages reviewed |

Vidcast session dates come from the [official webinar index](https://developer.webex.com/webinars); Ask the Expert session months come from the [Cisco index](https://developer.cisco.com/docs/webex-connect-partner-resources/ask-the-expert/). Upload timestamps are separate in the catalogue. Vidcast captions came from public player endpoints; the three YouTube transcripts use faster-whisper `small`, CPU/int8, after caption access failed. No video-frame inspection or tenant execution is implied. Raw technical-name mistakes remain. The AI Agent transcript's final boundary overshoots reported media duration by 6.42 seconds; curated passages are within the recording and that tail is not used.

### Masterclass: implementation observations

Source: [recording](https://app.vidcast.io/share/debc5583-a8ff-4a54-9a2e-c40b867f7be3). Times identify reviewed caption passages.

- **32:28–34:18:** Select the trigger, supply sample webhook JSON/XML, and parse customer ID into downstream variables.
- **34:29–37:27:** Test an external lookup, import its response, and name fields before using them in messages or decisions.
- **37:27–41:49:** The timezone lookup fails in the demo; a fixed timezone replaces it. Production needs a deliberate lookup-failure path.
- **42:28–43:49:** Correlation/notification data accompanies sending; Receive waits for a response. Late responses need a separate routing design.
- **45:29–46:23:** Parse only useful API outputs, then reference them in subsequent messages.
- **48:17–49:59:** Branch handles the reply; Evaluate is discussed for JavaScript transformations.
- **50:24–51:22:** Saving surfaces unconnected error/timeout paths. The demonstration publishes with warnings; production handling remains unfinished.
- **52:45–54:42:** A hardcoded ticker produces the wrong result. Replace it with the received-message variable, republish, and test again.

These observations are also useful review questions: which inputs remain hardcoded, which failure paths are missing, and whether the actual inbound variable reaches the API request. Use the [variables](03-variables-and-expressions.md) and [lifecycle](02-flow-lifecycle.md) chapters for the current mechanics.

### Integrations Studio: reusable method design

[Timecoded operational notes](../evidence/video-research/vidcast-integrations-learning-notes.md) cover method inputs, response mapping, outcomes, testing, publishing, and conversational state, with explicit demo-specific limits.

### RCS: response and fallback design

Source: [recording](https://app.vidcast.io/share/1b8cf04c-353a-4dda-a515-2c1fb9b9b483).

- **26:16–26:42:** Capability check precedes a Branch selecting RCS or SMS.
- **26:47–27:45:** Configure destination/message type and accessible media.
- **27:50–28:48:** A suggestion's displayed title differs from its postback value; Receive reads the postback before branching.
- **29:02–29:49:** Carousel selections also return postback values.
- **30:13–31:15:** The example obtains a hosted payment link through an API and separately receives completion.
- **31:37–32:52:** Asset creation includes branding, policy links, and testing numbers.

The video is historical; its Apple-support forecasts, pricing examples, and broad security claims are not current guarantees. Current [RCS Capability](https://help.webexconnect.io/docs/rcs-capability-node) and [Receive](https://help.webexconnect.io/docs/receive-node) documentation distinguish capability flags and `rcs.postbackData`. See [channel guidance](05-channels.md) before implementation.

## YouTube ASR: Getting started

[Local ASR of the official recording](https://www.youtube.com/watch?v=I041FVBzU_s) succeeded after caption access failed: 397 segments using faster-whisper `small`, CPU/int8. Raw recognition errors remain in the working transcript; exact field names require the text reference.

- **13:16–14:23:** Custom integration example configures a POST method, authorization, parameters, response mapping, and success/error/timeout outcomes.
- **14:26–14:58:** The reusable node consumes the customer's inbound-message variable in a flow.
- **19:31–20:16:** Appointment journey combines Apple messaging, a supplied number, OTP verification, CRM lookup, and rich responses.
- **20:25–21:18:** Natural-language date interpretation feeds a scheduling lookup; confirmation precedes a demonstrated payment option.

[ASR evidence](../evidence/video-research/getting-started-asr-evidence.json) records hashes, runtime, and review scope. This validates the real YouTube transcription route; it does not prove the demonstrated integrations work in another tenant.

## Selected YouTube library

These are useful learning routes, not claims that their full content has been watched. **Description-only** means the topic or chapter comes from publisher metadata. **Blocked** means caption access was attempted and failed. Watch-page metadata was available even where timed captions were rejected.

| Priority/topic | Recording and publisher | Published; length | Evidence status |
|---|---|---|---|
| AI Agent | [November 2024 Ask the Expert](https://www.youtube.com/watch?v=AGDmhRoNFT4), Webex CPaaS Solutions | 2024-12-03; 43:17 | 379 local ASR segments acquired; selected passages reviewed; pre-release UI |
| Email | [November 2023 Ask the Expert](https://www.youtube.com/watch?v=5TzxFpDzIPs), Webex CPaaS Solutions | 2023-12-19; 41:34 | 242 local ASR segments acquired; email portion reviewed |
| Secondary tutorial | [Set Up (English)](https://www.youtube.com/watch?v=It3Zq0wdxHg), Bucher + Suter | 2022-02-24; 10:59 | Description chapters only; older UI |
| Core platform | [Getting started](https://www.youtube.com/watch?v=I041FVBzU_s), Webex CPaaS Solutions | 2023-09-19; 30:28 | 397 local ASR segments acquired; selected passages reviewed |
| Core build | [Flow Builder developer workshop](https://www.youtube.com/watch?v=3vlMJ0SInr4), Webex CPaaS Solutions | 2024-05-16; 33:37 | Description-only; caption API and yt-dlp blocked |
| Core APIs | [APIs and flows for CX automation](https://www.youtube.com/watch?v=6cYabXkFaas), Webex CPaaS Solutions | 2024-05-16; 54:53 | Description-only; English ASR track advertised |
| Orientation | [Developer introduction](https://www.youtube.com/watch?v=IxEA3uPZA50), Webex CPaaS Solutions | 2024-05-16; 17:32 | Description-only; English ASR track advertised |
| Architecture | [Get to know Connect](https://www.youtube.com/watch?v=CUi_pTCI-ls), Webex CPaaS Solutions | 2023-09-19; 26:43 | Description chapters verified |
| Handoff | [Bot/agent summarization demo](https://www.youtube.com/watch?v=Yc7ihG6PjKk), Webex CPaaS Solutions | 2023-04-28; 2:25 | Audio acquired; local ASR found no nonempty speech; content unreviewed |
| Example flow | [Coffee Bar](https://www.youtube.com/watch?v=rj6KsqT9LOo), Webex CPaaS Solutions | 2024-02-21; 29:42 | Official index topic; captions blocked |
| Engage/security | [October 2023 Ask the Expert](https://www.youtube.com/watch?v=Hupt-VJE27Y), Webex CPaaS Solutions | 2023-12-19; 44:12 | Official index topic; captions blocked |
| Secondary training | [Features, Use Cases, and Live Demo](https://www.youtube.com/watch?v=joFiyWFJhl0), Sunset Learning Institute | 2025-07-23; 61:59 | Description-only; publisher page rounds to 60 minutes |

The [official Cisco Ask the Expert index](https://developer.cisco.com/docs/webex-connect-partner-resources/ask-the-expert/) establishes the topics for its recordings. Its fiscal-year headings differ from calendar session/upload dates. The [Sunset publisher page](https://www.sunsetlearning.com/webex-connect-features-use-cases-and-live-demo/) establishes the secondary training's announced scope, not current Cisco specifications.

Publisher chapter cues in Getting started: **04:18** channels, **08:16** NLP/NLU, **11:32** integrations, **19:05** appointment demonstration, **21:30** controls. These timestamps originally came from the description; do not label them transcript-derived. Bucher + Suter's older tutorial lists **02:00** flow creation, **05:50** webhook triggers, **06:35** branching, and **08:20** appointment reminders; use it for historical orientation.

## Reproduce ingestion and maintain evidence

Use the [transcription workflow](../docs/transcription-workflow.md) for venv setup, YouTube captions, local media ASR, subtitle import, and failure records. Keep raw copyrighted transcripts/media under ignored `transcripts/`; the curated KB stores short paraphrases with timestamps and source links.

For an official public Vidcast fallback, the checked adapter uses two read-only public-player endpoints. Their shape is not a supported API compatibility promise:

```bash
.venv/bin/python evidence/video-research/fetch_vidcast.py \
  https://app.vidcast.io/share/debc5583-a8ff-4a54-9a2e-c40b867f7be3 \
  --output-dir transcripts/masterclass-refresh

.venv/bin/python scripts/transcribe.py \
  transcripts/masterclass-refresh/source.en.vtt \
  --source-url https://app.vidcast.io/share/debc5583-a8ff-4a54-9a2e-c40b867f7be3 \
  --title 'Webex Connect Masterclass' \
  --output-dir transcripts/masterclass-refresh/normalized
```

The fetch adapter preserves provenance and validates nonempty ordered caption intervals; it stops on access or format errors. The shared importer classifies these as **local-subtitle-import**, with origin unverified by that generic parser. The accompanying public endpoint/publisher evidence establishes their origin; do not relabel them as manually authored captions or human reviewed.

Validation completed: all three vendor VTT files imported successfully with **554 + 483 + 344 = 1,381** segments. The reusable Vidcast adapter independently fetched and validated the 344-segment RCS transcript. [Evidence metadata](../evidence/video-research/) records source URLs, review boundaries, duration, retrieval dates, and hashes. Recording availability and product behavior can change independently.

The three successful YouTube ASR runs add **397 + 379 + 242 = 1,018** segments. See [AI Agent acquisition evidence](../evidence/video-research/ai-agent-asr-evidence.json), [email acquisition evidence](../evidence/video-research/email-asr-evidence.json), and [Getting started evidence](../evidence/video-research/getting-started-asr-evidence.json). Earlier caption failures remain recorded separately. Neither successful transcription nor timestamp validation certifies whole-recording word accuracy.

The [Cisco learning module](https://developer.cisco.com/learning/modules/webex-connect/) is an additional practice route for flow deployment and Meraki webhooks, linked from [Cisco's developer page](https://developer.cisco.com/webex-connect/). The lab application required JavaScript in the static fetch, so its full body was not ingested or treated as completed practice.
