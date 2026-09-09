# AI Agent recording: action and knowledge design

Source: [Webex CPaaS Solutions, November 2024 session](https://www.youtube.com/watch?v=AGDmhRoNFT4), published 2024-12-03. Reviewed from locally generated ASR on 2026-09-08. The [working transcript](../../transcripts/ai-agent-ask-expert-asr/transcript.md) contains 379 segments; exact interval endpoints below match [segment JSON](../../transcripts/ai-agent-ask-expert-asr/transcript.json). No video frames or tenant execution were inspected.

## Video-derived learning points

**Pre-release demonstration.** Configuration names and roadmap claims are historical.

1. **09:22.900–10:17.300:** The knowledge-versus-actions split is described as temporary.
2. **11:09.380–12:39.060:** Knowledge combines edited articles and an imported PDF.
3. **12:48.180–13:30.980:** Configure goal, welcome, knowledge selection; preview.
4. **13:43.350–16:08.390:** Compare generated answers against their source material.
5. **19:10.200–19:58.920:** Action descriptions explain when invocation is appropriate.
6. **20:49.240–21:35.480:** Define attribute meaning, type, date format, and requiredness.
7. **21:47.960–22:31.000:** Connect maps collected inputs into an integration and returns its outcome.
8. **23:18.860–25:06.520:** Retained context supplies prior identity; cancellation still requests a required reason and checks the changed appointment list.
9. **31:32.940–33:10.580:** Demonstration manually returns results to a supplied callback URL; automation is future work.
10. **34:49.740–35:24.840:** Action/flow granularity follows the backend operations.

## Apply using the current reference

Read [AI Agent flow contracts](../../knowledge/13-ai-agent-flows.md) and [action/SMS/email recipes](../../knowledge/14-agent-email-sms-recipes.md). The current [fulfillment guide](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions) uses the AI Agent Start category and Flow Outcomes notification. Follow that documented mechanism for a new fulfillment flow; do not copy the recording's pre-release callback arrangement. The dedicated [AI Agent node reference](https://help.webexconnect.io/docs/ai-agent-node) separately governs invoking an agent from a conversation flow.

The demonstration's patient identifiers, example operations, deletion choices, throughput remarks, and launch forecasts do not establish requirements or guarantees for another system. Use the action's actual authorization, identifier, required-input, and outcome contracts. The recording illustrates source checks and business-result checks; it is not an executed acceptance test of this KB's recipes.

## ASR boundary

Technical names may be mistranscribed. The raw final ASR segment ends 6.42 seconds beyond the video's reported 43:17 duration; it is preserved as uncertain evidence. All intervals used above occur before 35:25 and within the reported media duration. No whole-recording accuracy or human review claim is made.
