# Tenant UI observations

Observed **2026-09-08**, using a visible Playwright browser authenticated by the
user. This is a configuration-inspection record, not a runtime validation. The
user's mission is documentation/KB work; a narrow exception permits a temporary
sample experiment. No existing flow, asset, authorization, service setting,
logging setting or publication state was changed. No node Test, flow execution,
customer message or business API request was invoked.

## Existing read-only views

- The authenticated portal provides Services, Assets, Integrations, Tools,
  Debug/Watchtower, Event Scheduler and AI Agent Studio navigation.
- An existing live flow opened with an **Edit** control, rather than immediately
  entering a working draft. Its Evaluate configuration could be opened for
  inspection; existing configuration controls were disabled. The dialog was
  cancelled without edits.
- The visible utility palette included Evaluate, Branch, HTTP Request, Delay,
  Data Parser, Data Transform, Call Flow, Page Connector, Profile, Generate OTP,
  Validate OTP, Social Hour Check, Cryptographic Hash, Decryption and Encryption.
- The visible channel palette included SMS, Email, Push, Live Chat/In-App,
  Messenger, WhatsApp, Apple Messages for Business and Receive. It also rendered
  a Google Business Messages entry. **A rendered legacy entry does not prove
  current service support or successful operation.** No entitlement/availability
  claim is made from the palette alone.
- Integrations included AI Agent, legacy QnA/Task Bot entries, conversation/task
  operations and other enabled integrations. Seeing an entry establishes neither
  usable authorization nor successful execution.

## Temporary sample and naming

The test service initially had no flows. The creation dialog offered scratch,
copy and upload methods, and templates including AI Agent Scripted Doctor
Appointment, AI Agent Livechat Generic, AI Agent Fulfilment - Track Package,
WebhooktoSMSalerts, SMSSurvey, Autoresponder and AppointmentReminder.

A proposed name containing spaces/hyphens was rejected with an alphanumeric-name
validation message; no draft was created by that failed attempt. After a browser
tool reset and user reauthentication, the empty flow list was verified again.

An alphanumeric temporary sample, `KBInspection20260908`, was then created under
the user's exception. **Create itself allocated a Draft record before any Save
action.** This matters for future read-only inspections: avoiding Save does not
guarantee that no temporary record exists. A newly added AI Agent node was used
only to inspect its unsaved property form; no actual agent, channel recipient,
trigger payload or integration authorization was configured.

## AI Agent node: actual preliminary field view

The sample's default AI Agent node version was **b1.4**. The selector also listed
b1.2, b1.1 and b1.0. This is a **node integration version**, not evidence of the
tenant's overall Webex Connect release.

| UI area | Observed labels |
|---|---|
| Method Name | `Process message`, `Close session` |
| Process message inputs | AGENT TYPE, AGENT, MESSAGE, LANGUAGE |
| Customer Details | CHANNEL, channel-dependent identifier; default Live Chat/In-App displayed UNIQUE ID |
| Additional data | Customer Parameters (Optional), Message Parameters (Optional) |
| Side panels | Input Variables, Output Variables, Node Outcomes |
| Availability note | Agent selection is limited to agents accessible to the user in AI Agent Studio |
| Language help | Expected input language; Auto-detect mentioned for unknown/multiple languages |

With `Process message` selected and no specific agent chosen, the outcome panel
rendered `onInvalidData`, `onError`, `onInvalidChoice`, `onTimeout`, `onFailure`,
`onAgentHandover`, and `onSuccess`. This is a preliminary unconfigured-node
observation. The public node page instead documents some labels as
`onInvalidCustomerID`, `onInvalidMessage` and `onTimeOut`. Preserve the exact
labels shown after configuration for the selected version; do not silently mix
case or assume this sample's list applies to all versions.

The Output Variables panel was present, but the session did not establish a
fully configured agent's output-variable picker references. Use the
[AI Agent playbook](13-ai-agent-flows.md), cached official node page and actual
configured picker in a future authorized build. No observed behavior resolves
the documentation's 15-second message-response versus 30-second fulfillment
execution limits; these remain separate contracts to design around.

## Complete sample inspection and cleanup

The [sample inventory](../evidence/sample-flows/sample-inventory.json) records all
**59 native graphs** inspected: 9 gallery templates, 17 AI fulfillment files and
33 current v3.5 digital-channel templates. Each has a sanitized loaded-canvas
capture, exact node/edge/variable summary and a coherent
[walkthrough](../evidence/tenant-samples.md). Supported UI imports resolved the
native files' previously opaque representation. Their internal model is evidence,
not an invented public import API. Embedded sample responses and historical test
flags are not new execution evidence.

Because Create immediately persists a Draft, inspection produced **60 temporary
records**: the original blank `KBInspection20260908` and 59 `KBSample...` drafts.
All 60 were removed individually. Before each deletion, the exact recorded flow
ID and name, Draft status and **Executions = 0** were checked. No bulk selection
or name-prefix-only deletion was used. The test service's Flows tab was reopened
after reload; the selected Flows tab's named table showed zero flow records.
The [cleanup audit](../evidence/sample-flows/temporary-cleanup-summary.json) and
[per-record log](../evidence/sample-flows/temporary-cleanup.json) preserve the
IDs and verification. **No temporary flow remains. No pre-existing flow was
deleted or modified.**

## Control Hub and AI Agent Studio: read-only agent-side inspection

The authenticated Control Hub Contact Center overview linked to Webex AI Agent
Studio and Webex Connect as separate applications. The Studio agent list exposed
autonomous and scripted agents. Opening an existing published autonomous agent
showed Profile, Instructions, Knowledge, Actions and Conversation tabs; its Save
changes control was disabled. No Preview, new-agent action or configuration
mutation was used.

The Actions table distinguished System, Event and Transfer action types and
displayed enabled state independently from the action description. An existing
Event action's detail page exposed Action name, Action description, slot-filling
entities and Fulfillment. The input table columns were Entity Name, Type, Value,
Description, Example and Required; this particular action had no input rows.
The page offered **Use Webex Connect Flow Builder** and **Manage in the source
flow (voice only)**. The latter was already selected. The radio selection was
not changed; Save remained disabled and the page was cancelled.

This observation establishes the visible distinction between Connect fulfillment
and a voice source-flow event. It does **not** establish an existing digital
Connect binding, a configured flow-selector value, or successful tool execution.
The exact current setup procedure remains in the cached Studio documentation and
[AI Agent playbook](13-ai-agent-flows.md). Private agent prompts, names and
business configuration are not copied into this reusable guide.

**No Control Hub or AI Agent Studio configuration was changed.** The Connect
sample exception was not applied to either application.

## Remaining evidence limits

This record intentionally excludes customer content, credential values, private
integration configurations and raw browser snapshots. It captures useful UI
facts and field labels. No tenant release number, runtime session isolation,
agent response, email thread behavior, SMS delivery or fulfillment execution was
verified. The knowledge base's executed checks are local tooling checks and
video-transcription acquisition; they are not Webex flow tests.
