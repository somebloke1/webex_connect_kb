# Email demo learning notes

Source: [official November 2023 recording](https://www.youtube.com/watch?v=5TzxFpDzIPs), published December 19, 2023. Reviewed the email teaching/demo portion, 11:24–40:26, in the [local ASR transcript](../../transcripts/email-ask-expert-asr/transcript.md); sales enablement is excluded. Exact interval boundaries below match segment starts/ends in [transcript JSON](../../transcripts/email-ask-expert-asr/transcript.json). ASR misrecognizes terminology, including SES; current documentation supplies verified spellings. No video-frame inspection or tenant execution occurred.

## Video-derived lessons

Historical ASR evidence. C=corroborated concept; A=ASR-only. Exact UI/spellings remain unverified.

1. **00:13:22.010–00:13:45.010** Choose SES or SMTP during tenant provisioning. [C]
2. **00:16:08.500–00:16:40.500** SMTP inbound delivery requires forwarding to Connect. [C]
3. **00:18:21.820–00:19:26.820** SES setup connects credentials, domain verification, DKIM, and inbound MX records. [C]
4. **00:22:15.380–00:22:57.380** Correlate notification callbacks; SMTP exposes fewer statuses than SES. [C]
5. **00:27:54.910–00:29:01.340** Combine header/body templates and inject recipient-specific variables. [C]
6. **00:31:15.150–00:31:49.150** Webhook fields supply recipient, name, transaction date, and merchant. [A]
7. **00:32:09.150–00:33:00.150** Configure templates, HTML fallback, tracking, and status notifications. [C]
8. **00:33:37.150–00:34:39.150** Webhook acceptance returns queued status/transaction ID; receipt confirmation is separate. [A]
9. **00:36:33.150–00:37:10.150** Event Scheduler can invoke personalized flows for individual file rows. [A]
10. **00:37:50.900–00:39:52.780** API examples vary templates/substitutions, text/HTML, and attachment MIME/media URLs. [A]

## Separate current-document clarification

Official cached documentation: version **6.20.0**, retrieved **2026-09-08**.

Current **From Email** is asset-derived and disabled in the node; **Destination ID** accepts comma-separated values. These instructions supersede the historical editable-sender and single-destination remarks. The [Email node reference](https://help.webexconnect.io/docs/email-node) also corroborates template composition and route-specific receipt behavior; [channel documentation](https://help.webexconnect.io/docs/email) corroborates provisioning, DNS setup, and SMTP forwarding.

Use the detailed [email contract](../../knowledge/05-channels.md#email) and [email agent recipe](../../knowledge/14-agent-email-sms-recipes.md#recipe-2-email-triage-and-reply-agent) for implementation. They cover current attachment limits, reply metadata, recipient policy, and subscription handling. Do not reinterpret an overall-message-size example as an attachment limit or a queued response as proof of delivery. Cached source bodies remain [email](../../sources/cache/help/email.md) and [Email node](../../sources/cache/help/email-node.md).

## Limits

ASR-derived examples establish instructional intent, not current endpoint syntax, runtime entitlement, or successful delivery in another tenant. The current-document comparison above is limited to email channel/node behavior; Event Scheduler and Send API examples remain demonstrations requiring their own current references before implementation.
