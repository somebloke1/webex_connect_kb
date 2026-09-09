# Channels: configuration, identity, replies, and delivery

Reviewed 2026-09-08. This chapter describes Webex Connect flow nodes. A channel listed in public documentation is not proof that it is provisioned, commercially enabled, or supported in your tenant/region. Use the exact channel asset and node version when filling the fields below. Examples use illustrative node IDs; select variables from the actual node's picker.

## Select the channel contract before drawing the flow

**Design recommendation.** Record business asset, customer identifier, consent/purpose, message type, reply event, delivery evidence, timeout, and fallback for each channel. Keep customer identity, conversation identity, and message transaction identity separate. Choose fallback channels only where identity mapping and consent actually exist. A timeout means the expected evidence did not arrive by the deadline; do not automatically interpret it as nondelivery.

| Channel | Key configuration and constraint | Primary reference |
|---|---|---|
| SMS | Destination type `msisdn` or customer profile ID; destination, sending number/ID, content/type. Include country code; honor tenant `+E.164` setting. Node permits 4,000 characters but its counter is not final segment count. | [SMS node](https://help.webexconnect.io/docs/sms-node) |
| MMS | Destination and sending asset, subject (80 characters), message (4,096), media type and slide URL; up to nine media items documented. Carrier restrictions apply. | [MMS node](https://help.webexconnect.io/docs/mms-node) |
| WhatsApp | WhatsApp app/WABA, recipient identity, permitted free-form or approved-template message; persist business scope with identity. | [WhatsApp asset](https://help.webexconnect.io/docs/whatsapp) |
| Email | Email/customer ID destination, provisioned app sender, subject, content, reply address, recipients, attachments. SES and SMTP tenant configurations differ. | [Email node](https://help.webexconnect.io/docs/email-node) |
| Live Chat/In-App | SDK-enabled app asset and registered user; destination, thread ID, message/form/template/quick replies. | [Live Chat/In-App node](https://help.webexconnect.io/docs/in-app-messaging) |
| Push | SDK-enabled app and registered user/device; platform-specific notification fields. | [Push node](https://help.webexconnect.io/docs/push) |
| Messenger | Authorized Facebook Page/app plus that page's customer PSID. | [Messenger node](https://help.webexconnect.io/docs/messenger) |
| RCS | Configured RCS app and capability result suitable for chosen content. | [RCS message node](https://help.webexconnect.io/docs/rcs-message-node) |
| Apple Messages for Business | Configured business asset and opaque AMB user ID for ordinary messages. | [AMB node](https://help.webexconnect.io/docs/apple-messages-for-business-node) |
| Voice | Provisioned caller number, destination and expiry; ongoing-call logic in a Voice Node Group. | [Call User](https://help.webexconnect.io/docs/call-user-node) |

## Sending and receiving are separate contracts

**Documented examples.** SMS supports waiting for gateway submission or a delivery report. Correlation ID returns with delivery reporting; Notify URL receives receipts, while Callback Data adds application context. Invalid callback authorization can park receipt payloads without preventing the message itself from being sent. Configure receipt delivery and message delivery as separate checks. [SMS node](https://help.webexconnect.io/docs/sms-node)

**Design recommendation.** Use a business operation ID for a send intent and retain the resulting message transaction ID. Log acceptance, provider submission, delivery, read, reply, and business completion independently. Do not reuse a customer ID as a unique operation ID. Handle late and repeated receipts without sending twice or moving completed business work backward.

**Receive configuration.** Use the event-specific field and outcome contract in [core nodes](04-node-reference.md). **Design recommendation:** bind the wait to the intended asset, customer and conversation; distinguish text replies from interactive selections and thread-close events. Test a repeated event, a late response, and a response from another user before relying on a wait in production.

## SMS and MMS implementation notes

**SMS.** Select the sender associated with the service. Template messages require mappings for their variables. Shortened-link click tracking requires both the node option and the webhook's click event; node shortening and the prebuilt Link Shortener have different reporting capabilities. Separate gateway and delivery outcomes before selecting a fallback. [SMS node](https://help.webexconnect.io/docs/sms-node)

**MMS.** Media is supplied through slide URLs. The public page presents a `Read` wait option and describes timeout via `onDeliveryReportFail`; that is not evidence that every carrier provides read receipts. Verify your tenant's actual outcomes and network support with a controlled device test. Preserve the observed outcome instead of substituting SMS semantics. [MMS node](https://help.webexconnect.io/docs/mms-node)

**Design recommendation.** Test expanded text, non-ASCII characters, long URLs, unsubscribe keywords, and media access using real representative destinations. Do not calculate final SMS segmentation from the canvas character counter. Treat country-specific registration and sender restrictions as asset/onboarding checks rather than universal flow defaults.

## WhatsApp: session, template, and identity decisions

**Send configuration.** Inside the rolling 24-hour customer-message window, supported free-form messages include text, media, location, contact, list and reply buttons; outside it use an approved template and appropriate opt-in. Text is limited to 4,096 characters; list menus allow ten choices and reply buttons three. Template sends map header/body parameters, media and button values. Currency uses thousandths of a unit; datetime values use Unix seconds with fallback display values. Preserve `send.gatewayTid` for message traceability. [WhatsApp node](https://help.webexconnect.io/docs/whatsapp-node)

| Template decision | What to capture |
|---|---|
| Registration | Name, category, language, WABA, approval/quality status |
| Content | Header/media, body variables, footer, CTA or reply payloads; sample values for registration |
| Runtime | Exact approved template and complete parameter mapping; do not build a new template by changing free-form text |
| Authentication | Matching Android package/signature for autofill, or copy-code delivery; application validates the code |

Templates are registered in Tools → Templates. Changes made directly in WhatsApp Manager are not synchronized into Connect template content. Dynamic parameters cannot contain newlines or more than four consecutive spaces. Approved templates can later become disabled. Cisco's current page documents verifiable HTTPS URLs for templates that contain links and a US marketing restriction associated with error `131049`; verify active account/provider policy before launch because these rules change. [WhatsApp templates](https://help.webexconnect.io/docs/templates-whatsapp)

**Identity update.** `whatsapp.bsuid` and `whatsapp.userHandle` are documented inbound fields. BSUID belongs to a user/business-portfolio pairing; it is opaque, not a phone number. Cisco describes preferring WAID when both identifiers are supplied, and withholding phone numbers in some cases. The same page mixes deployed fields with a future automatic-normalization roadmap: do not assume that every tenant already substitutes BSUID into legacy WAID. Preserve both fields when available and test a phone-number-absent event. [BSUID reference](https://help.webexconnect.io/docs/whatsapp-usernames-and-business-scoped-user-ids-bsuid)

**Preference/identity failures.** The asset UI exposes account/number status, quality and throughput. Marketing opt-out can yield `131050`; record preference events and suppress future marketing accordingly. Identity-hash mismatch can reject sending; inspect the new hash delivered in inbound/receipt data before following the business's identity-verification procedure. Do not silently discard identity checks merely to force a send. [WhatsApp asset](https://help.webexconnect.io/docs/whatsapp)

**Design recommendation.** Persist last customer-message time separately from flow start time. Send a stable option identifier and route on the identifier rather than the translated button title. Correlate interactive responses with the originating question/message where supported. Enforce maximum invalid replies and an explicit human-handoff path. Delivery/read receipts do not themselves renew a customer-message window.

## Email

The sender comes from the selected app asset. Choose text, HTML or template; HTML/template can include fallback text. Full templates render an entire email; partial templates compose sections. Map CC/BCC and Reply-To intentionally; SMTP configurations support `In-Reply-To`. Overriding unsubscribe headers transfers unsubscribe handling away from Connect's default handling, so use those overrides only with an implemented subscription workflow. SES has address internationalization limits. Waiting for a delivery report does not establish that a person read the email. [Email node](https://help.webexconnect.io/docs/email-node)

**Design recommendation.** Preserve Message-ID/reply-chain context through the conversation layer; sanitize content before agent display, carry plain and HTML bodies separately, and test attachment-only messages, multiple recipients, forwarded mail and duplicate deliveries. Do not use subject alone as a durable conversation key. Contact-center email mappings and attachment handling are in [integrations](06-integrations-and-contact-center.md).

## Live Chat/In-App and Push

Live Chat/In-App needs the correct app ID/client key in the SDK and at least one registered user. Sending supports message, form, generic template and quick replies; thread ID and notification text/title can be configured. Generic-template buttons distinguish postback from URL navigation. Delivery/read waits are available. **Design recommendation:** keep the thread-to-user binding through each turn, validate form fields, and handle thread closure independently of message receipt. [Live Chat/In-App node](https://help.webexconnect.io/docs/in-app-messaging)

Push requires its own user/device registration and platform notification configuration. Its documented waits include submission, delivery, read, and a user-ID-only success-delivery option that ignores failed receipts until success or timeout. **Design recommendation:** test multiple devices, expired registrations, foreground/background behavior and notification permission denial; a push notification should deep-link to durable application state, not be the only copy of important information. [Push node](https://help.webexconnect.io/docs/push)

## Messenger, RCS, and Apple Messages for Business

**Messenger.** PSID is page-scoped; the same person has a different PSID on another Page. Customer ID works only when correctly associated with that identifier. The node exposes response/update/tag messaging choices, text/media/templates, and notification modes. Cisco's page retains historical policy wording such as “24+1”; do not use that wording as current authorization to message. Validate the currently supported purpose/window/tag and region with the active asset/provider contract. [Messenger node](https://help.webexconnect.io/docs/messenger)

**RCS.** Run capability lookup before choosing rich content: `rcs.enabled` alone is insufficient; the documented `rcs.version` distinguishes basic and richer support. Branch to an authorized fallback if the required feature is absent. [RCS capability](https://help.webexconnect.io/docs/rcs-capability-node) The send node supports text, file, card, carousel and typing indicator. Configure file URL/byte size, card orientation/media height, title/description and suggestions. Carousels contain 2–10 cards with consistent media height. Receipt waits can include submission, delivery and read. **Design recommendation:** test capability unknown/error separately from false and preserve a text equivalent of the rich interaction. [RCS message node](https://help.webexconnect.io/docs/rcs-message-node)

**Video demonstration (2024-06-26, historical).** Cisco demonstrates capability branching at 26:16, separate button labels/postback values at 28:21, and response routing at 28:09. Use current node documentation for implementation details. [RCS webinar](https://app.vidcast.io/share/1b8cf04c-353a-4dda-a515-2c1fb9b9b483)

**Apple Messages for Business.** Ordinary messages target User ID and support text/attachments, rich links, quick replies, lists, time pickers, forms, payment and authentication message types. The documented general wait settings are None or Gateway Submit; do not infer delivery/read success from submission. Classical Authentication is deprecated; use the supported newer path. App Clips have device constraints. **Design recommendation:** maintain option IDs, locale and selected time zone separately from labels, and test supported devices for repeated interaction events. [AMB node](https://help.webexconnect.io/docs/apple-messages-for-business-node)

## Webex Connect voice and IVR

These are Connect voice nodes. For contact-center digital handoff, use the distinct task/conversation lifecycle in [chapter 06](06-integrations-and-contact-center.md); a Connect Call Patch is not a WxCC Queue Task.

| Node | Inputs to decide | Result/edges to handle |
|---|---|---|
| Call User | E.164 destination, caller number, expiry, callback context | `call.transId`, `call.destination`, `call.fromNumber`; answer, no-answer, busy, rejection, failure, policy and expiry paths |
| Play | Media or TTS; voice/language; plain text or SSML | Playback success/error; no output variables |
| IVR Menu | Single-digit choices or speech keywords; prompt; input timeout | `ivr.input`; success, `oninputTimeout`, `onwrongInput`, error |
| Collect Input | Digit count/terminator or speech engine/language; input/silence timeout | `collect.input`; success, input timeout, invalid/error |
| Record | Duration, stop key, filename prefix, optional beep | `record.recordingFilePath`; success, recording timeout, error |
| Call Patch | B-party E.164 number, display number and transfer prompt | `patch.APartyNumber`, `patch.BPartyNumber`; success, no-answer, error |

Each row is expanded with its own source below; copy exact outcome spelling from the installed node.

**Call User.** Lives outside the Voice Node Group, connecting its answer edge to the group. Callback Data is limited to 2 KB; exceeding it can cause policy failure before dialing. Configure expiry to avoid stale calls. Older untouched flows may use the error path for expiry, while new/edited flows use `onExpiry`. [Call User](https://help.webexconnect.io/docs/call-user-node)

**Voice Node Group.** Holds ongoing-call operations, and can contain certain digital send nodes without their wait-for-event options. Answering-machine detection is optional and tenant/feature dependent. [Voice Node Group](https://help.webexconnect.io/docs/voice-node-group)

**Play.** Supports prerecorded media, upload, URL and TTS. Current documentation specifies neural Azure voices; legacy standard voices will fail. SSML can override dropdown settings. Limits documented are 3,000 text or 6,000 XML characters; uploads support WAV/MP3 up to 20 MB. The page restricts URL playback to HTTP: prefer managed media if HTTPS behavior is unverified rather than downgrading sensitive media transport. Listen to the actual synthesized prompt before release. [Play](https://help.webexconnect.io/docs/play-node)

**IVR Menu.** Use for a one-digit choice; configure DTMF or speech, option routes and timeout. Speech requires enablement and has pricing implications. Its wrong-input outcome is distinct from no input. [IVR Menu](https://help.webexconnect.io/docs/ivr-menu-node) **Collect Input.** Use for multi-character input or speech. Speech silence timeout ends capture after speech starts; it is different from the initial input timeout. Optional recordings support diagnosis. [Collect Input](https://help.webexconnect.io/docs/collect-input-node)

**Record.** The maximum documented recording duration is 300 seconds. A configured stop key and no keypress may produce the timeout edge. Store the resulting recording path as restricted data. [Record](https://help.webexconnect.io/docs/record-node) **Call Patch.** Joins an ongoing call with a B-party, inside the voice group. Validate destination and implement no-answer recovery before attempting another destination. [Call Patch](https://help.webexconnect.io/docs/call-patch-node)

**Design recommendation.** Every IVR menu needs bounded reprompts, invalid-input handling, a caller exit and a disposition for hang-up. Validate digit strings without converting account numbers to numbers (leading zeroes matter). Avoid placing collected secrets in descriptive logs. Verify all TTS languages and any fallback engine with your prompts, especially SSML. Use recording only with the approved disclosure/retention policy.

## Channel failure playbook

| Symptom | First useful evidence | Practical response |
|---|---|---|
| Send node succeeds, customer sees nothing | Wait setting, transaction ID, provider receipt, asset status | Distinguish accepted/submitted/delivered; follow the receipt/error path before resend |
| Delivery webhook missing | Notify URL, selected event, authorization ID, receiver logs | Repair receipt transport; do not treat its failure as proof of message failure |
| Receive times out after button tap | Event type, user/asset/thread filter, originating message | Align postback/list/button event and identity; keep late-reply handling |
| WhatsApp template absent/rejected | WABA/language/template status and parameter mapping | Select approved matching asset/template; classify policy errors instead of looping |
| Agent misses attachment or rich reply | Incoming payload, security-scan result, append mapping | Use the channel's contact-center schema; provide safe text substitute where documented |
| Voice falls through or plays nothing | Call milestone, node edge, voice/language/media access | Separate no-answer from prompt/format failure; test the selected prompt directly |
| Rich message fails on one device | Device capability, payload/media constraints and receipts | Use a tested equivalent format; preserve business intent and correlation |

The playbook is a design diagnostic sequence, not a claim of automatic platform retries. See [operations](07-testing-and-operations.md) for observability and retry rules.
