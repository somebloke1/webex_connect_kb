# Webex Connect flow lifecycle

Evidence checked: **2026-09-08**. These procedures concern **Webex Connect Flow Builder**. See [Platform and design](01-platform-and-design.md) before using a Contact Center Flow Designer tutorial. Recommendations below are explicitly marked; they are not undocumented platform guarantees.

## State and version model

| Action/state | Documented effect |
| --- | --- |
| Save | Preserves a Working Draft; drafts can contain configuration errors |
| Working Draft | Can be edited repeatedly without changing the running live version |
| Make Live | Requires no flow errors and creates the next numbered version |
| View older version | Loads it read-only initially |
| Edit older version | Creates a working draft based on that historical version |
| Rollback | Edit the desired old version, then make that draft live |

Version history is available from the upper-left version selector. A historical-version edit receives a comment identifying the version it was forked from. Rollback follows the same publication lifecycle as other edits; selecting an old version merely to view it is not rollback. [Flow Version History](https://help.webexconnect.io/docs/flow-version-history).

## Create a new flow

1. Open the intended service.
2. Under **Flows**, choose **Create Blank Flow** or **Create Flow**, depending on the entry point.
3. Enter **Flow Name**; choose the workflow type supported by the target tenant.
4. Choose **Method → New Flow**.
5. Select **Start from Scratch**, or a suitable displayed template; choose **Create**.
6. At **Select Trigger Category**, select the channel, system, or custom trigger that matches the design contract.

The creation guide still mentions a separate Voice Flow type; use the deprecation and tenant-capability distinction in the platform chapter when following older screenshots. Templates such as survey, appointment, and autoresponder flows are starting points whose configuration must be reviewed. [Creating a Flow](https://help.webexconnect.io/docs/create-a-new-flow).

**Engineering recommendation:** name the flow so its journey and role are clear. For example, `appointment-reminder-entry` and `appointment-response-handler` convey more than `Flow 2`. Record environment separately if naming alone could be confused with actual isolation.

## Build and configure the canvas

The node palette groups **Utilities**, **Channels**, and **Integrations**. Search it, drag a node onto the canvas, then configure the node and its connectors. Canvas controls include undo/redo, delete, auto-arrange, fit, zoom, and actual size. The top-right settings control opens General, Custom Logs, Flow Outcomes, and Custom Variables. **Save** reports configuration errors/warnings; **Make Live** appears for a working draft. Version comments have a **250-character** limit. Notes and Flow Debug are on the right toolbar. [Navigating Flow Builder Canvas](https://help.webexconnect.io/docs/navigate-flow-builder-canvas).

**Engineering build sequence:**

1. Configure the Start node against a real sample event and the intended source asset. Check the fields offered by that specific trigger.
2. Add the shortest useful path from entry to a named terminal outcome.
3. Open every node and complete its required fields, bindings, outputs, and available outcomes using its reference entry in this knowledge base.
4. Connect the success path and every relevant error, timeout, invalid-data, and fallback outcome. Make unhandled cases explicit rather than leaving accidental gaps.
5. Add correlation, environment variables, logbook mappings, and outcomes according to the design contract and [operational settings](07-testing-and-operations.md).
6. Save, inspect the affected nodes, resolve errors, and assess each warning before proceeding. Repeat after meaningful edits.

Cisco's first-flow tutorial shows that clicking a save error selects the associated node so its configuration can be corrected and saved again. Validation establishes configuration consistency; the tutorial separately triggers the live flow to test actual behavior. [First-flow tutorial, 2024-08-01](https://developer.webex.com/blog/build-your-first-webex-connect-flow-a-step-by-step-guide).

Connect signs users out after **30 minutes of inactivity**, with no warning notification documented. Save meaningful progress frequently. [Accessing Webex Connect](https://help.webexconnect.io/docs/accessing-the-product).

## Test at the correct boundary

**Engineering recommendation:** use designated test assets, inputs, recipients, and downstream systems. Publishing for a test is still publication into the selected environment. Establish a safe trigger boundary before making the candidate live.

For the documented webhook example:

1. Retrieve the generated webhook URL from the Start configuration.
2. Make the configured candidate live in the intended test environment.
3. In Postman, select **POST**, set that URL, and use **Body → raw → JSON** with the trigger's sample structure populated with test values.
4. Send the request; observe the actual message, the reply-dependent behavior, and the configured downstream callback.
5. Use Flow Debug to investigate the run when an expected observation is absent.

This is an example of end-to-end testing; apply the authentication requirements of the actual webhook configuration. Do not copy an example's omission of authorization into another integration. [First-flow tutorial, 2024-08-01](https://developer.webex.com/blog/build-your-first-webex-connect-flow-a-step-by-step-guide).

**Engineering recommendation:** a node's successful local Test result, a saved canvas, an accepted API request, and a completed business journey establish different facts. Preserve evidence of the appropriate fact for each acceptance criterion. The full matrix, log controls, and failure diagnosis are in [Testing and operations](07-testing-and-operations.md).

## Make live and observe the transition

Choose **Make Live** after resolving errors. In its wizard, select the required apps/numbers, supply externalized custom-variable values, and add a release comment. The documented flow-size ceiling is **10 MB**. Existing runs retain the previously published configuration; runs triggered after publication use the new one. [Flows](https://help.webexconnect.io/docs/flows-introduction).

**Engineering release checklist:**

- Confirm tenant, workspace view, service, flow, candidate version, and release operator.
- Read back all launch bindings: sender/app/number, webhook/integration, authorization reference, template/media, endpoint, and environment variables.
- Confirm branch tests and expected business-system effects against the candidate.
- Record the last known-good version and which external dependencies it still requires.
- Publish; capture the resulting version and time.
- Trigger an authorized verification event and confirm the expected new-version path and downstream outcome.
- Observe a representative operating interval, including delayed paths relevant to the change.

Do not call a release verified solely because the editor reports Live. If old and new runs overlap, correlate each observation to its originating run/version. External configuration may need separate restoration during rollback; version history by itself is not a backup of every dependency.

## Pause, resume, rollback, and protect the service

The flow list has a **State** toggle used to temporarily pause a live flow. The cited documentation does not specify whether pause cancels existing waits, drains runs, or queues new triggers; treat those as unverified, not guaranteed pause semantics. [Flows](https://help.webexconnect.io/docs/flows-introduction).

**Engineering procedure:** record the current version/state, identify the upstream event source, use the State control for the intended pause/resume, and verify its displayed state. Test the required behavior in the target environment before using pause as a production drain or recovery mechanism. For an incident, decide explicitly whether the aim is to stop new triggers, restore earlier logic, or reconcile already executed side effects.

For rollback, open version history, select the known-good version, choose **Edit**, inspect the draft and launch values, and make it live. [Flow Version History](https://help.webexconnect.io/docs/flow-version-history).

Under **Service Settings**, locking prevents other users from modifying the service while allowing read-only access; the owner can still edit it. Deleting a service permanently removes its flows and reports and affects integrations using its credentials. Service deletion is therefore not a pause or rollback mechanism. [Locking, Deleting, and Other Settings](https://help.webexconnect.io/docs/service-settings).

## Copy, export, and import

### Export an existing flow

In the service's **Flows** list, open the selected row's **Actions** menu and choose **Export**. This location is visible in Cisco's Webex Connect portal screenshot in document 222936, updated **2025-04-17**; check the current tenant if its UI differs. Preserve the exported file and record its source flow/version. [Cisco portal screenshot and context](https://www.cisco.com/c/en/us/support/docs/contact-center/unified-contact-center-enterprise-1262/222936-troubleshoot-common-issues-seen-in-a.html).

**Evidence limit:** that screenshot identifies the Export action but does not define which version a row export chooses or whether credentials are included. Inspect the resulting artifact rather than assuming either behavior. Do not hand-author an allegedly importable Connect flow file from an invented schema.

### Import a flow file

1. Open the destination service → **Flows → Create Flow**.
2. Enter the new name.
3. Select **Method → Upload a flow**.
4. Choose **Choose File**, select the flow artifact, then **Create**.
5. **Save the imported flow before further work.** Cisco documents that skipping this save can lose Evaluate script formatting.

These steps are documented for Connect sample-flow imports used with Contact Center; review the template's integration-specific dependencies separately. [Flow Configuration using Sample Templates](https://help.webexconnect.io/docs/wxcc-flow-configuration-using-sample-templates).

The flow-creation method also supports copying an existing flow. For a copy, select that method and review the source and resulting draft before configuration. The cited AI Agent fulfillment guide describes New Flow, Copy, and Upload as creation choices; it does not establish a universal unattended-copy API. [Configure fulfillment flows](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions).

The **v6.3.0, July 2023** release increased import/export size from 4 MB to **10 MB**. It also states that descriptive logging starts disabled in imported/copied flows regardless of the source setting. [v6.3.0 release notes](https://help.webexconnect.io/changelog/product-update-v630-july-2023-1).

### Respect integration portability

Custom-integration flows can move between services and permitted group/team scopes when the integration is available there. They cannot be imported directly across tenants. Cisco's documented workaround removes those nodes for export, restores the source's prior version, imports the file, and recreates the destination nodes. [Flows](https://help.webexconnect.io/docs/flows-introduction).

**Engineering recommendation:** perform that preparation on a preserved copy/draft rather than dismantling a production flow. Keep the original export, a dependency manifest, and the source configuration. Recreate missing integrations and authorization using the destination's supported setup; then rebind and test the candidate. Do not regard a file that imports successfully as an operationally equivalent deployment.

### Migration review matrix — engineering recommendation

| Inspect after copy/import | Why |
| --- | --- |
| Trigger and source asset | Avoid consuming the wrong event stream or leaving a flow untriggerable |
| Node version and required entitlement | A recognizable node may still be unavailable or use different authorization |
| App, number, template, bot, media | Local identifiers and enabled resources may differ |
| Credentials, endpoint, certificates | Correct source settings may be wrong for the destination |
| Custom variables and expressions | Confirm exact bindings and saved script formatting |
| Logbook and outcome notifications | Ensure evidence and callbacks reach the intended environment |
| Active state and launch values | Prevent accidental customer traffic before readiness checks |
| Representative event and every material branch | Establish behavioral equivalence, including failures and timeouts |

## Share a review view

The canvas Share feature produces a password-protected, read-only link. Analyze Mode can be included when enabled by an administrator. A shared diagram is a review surface; it is not an exported deployable artifact. [Navigating Flow Builder Canvas](https://help.webexconnect.io/docs/navigate-flow-builder-canvas).

**Engineering recommendation:** inspect the diagram and analytics content before sharing it externally. Record review findings against the candidate version and retest changes that affect an accepted branch.

## Minimal durable release record — engineering recommendation

```yaml
journey: appointment-reminder
tenant: <verified-tenant>
workspace: <client-or-group-or-team>
service: <service-name-and-id>
flow: <flow-name-and-id>
source_version: <previous-live-version>
released_version: <resulting-live-version>
published_at: <timestamp-with-timezone>
operator: <authorized-operator>
change: <concrete-behavior-change>
artifact: <export-path-and-checksum-if-created>
bindings: <reviewed-nonsecret-dependency-manifest>
verification: <test-case-and-run-evidence-locations>
rollback: <known-good-version-and-dependency-restoration>
remaining_limitations: <specific-unverified-facts-or-none>
```

No authenticated publication, export/import, or pause operation was performed while writing this chapter. The procedures are source-grounded; target-tenant execution remains the verification boundary. All linked sources were accessed **2026-09-08**.
