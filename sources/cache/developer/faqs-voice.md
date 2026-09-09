# Voice FAQs

Source: https://developers.webexconnect.io/reference/faqs-voice
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:52+00:00

## Do you support Text to Speech?

Yes, we do support Text to Speech for playing voice messages/prompts. We have integrated with Azure for TTS. 

## How many different voices do you support? Do you have accents for UK, IE & HU?

Please refer to [Supported Languages for Voice TTS](https://help.imiconnect.io/docs/supported-languages-for-voice) for the list of voices that we support.

## Do you support SSML?

Yes, we do support SSML within voice nodes such as Play Node, IVR Node, Collect Input, etc. Please refer nodes documentation for more details. SSML is supported only in v1 voice APIs.

## Do you support Answering Machine Detection?

Yes, we support Answering Machine Detection (AMD) for outbound calls. This feature can be configured from within Voice Node Group settings interface.



![Screenshot of VoiceNode Group Configuration Page.](https://files.readme.io/3d8e407-Screenshot_2021-09-27_at_2.11.50_PM.png)




AMD is based on the audio from the recipient end after a call is connected. Webex Connect  captures and analyzes the initial few seconds of audio to assess whether the call has been answered by a human or an answering machine. Given answering machine detection is based on audio patterns, the result is dependent on the audio quality, message length, etc. from the recipient end and hence the detection may not be accurate in some cases. Currently, we do not claim AMD support for custom voice messages and Google answering machine.

Usage of answering machine detection is subject to regulatory guidelines. E.g., in the UK, Ofcom provides detailed guidelines on when and how AMD can be used. Please refer to your regional guidelines on AMD to ensure compliance.

## Do you Support STIR/SHAKEN?

For U.S. telephone numbers, including landline, VoIP, or toll-free numbers (TFNs) obtained directly from Cisco, outbound calls will receive the highest level of attestation from the downstream provider responsible for ensuring compliance with STIR/SHAKEN regulations. However, please note that Cisco's CPaaS product does not attest outbound calls, nor does it support receiving attestation information from customers for calls routed to downstream providers.

## What is SPAM RISK Caller ID?

When a call comes in, spam ID technology automatically runs the number through the phone carrier’s database of reported scam numbers. If the number calling matches a reported scam number, your calls will display nuisance call labels, such as “Scam Likely”, “Fraud Risk”, “Spam Risk” or some other variant depending on the carrier, device, or app. The call recipient can then decide whether or not to answer the call.

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [],
  "examples": {
    "codes": []
  }
}
```
