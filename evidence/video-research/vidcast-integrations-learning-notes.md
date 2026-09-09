# Integrations Studio webinar: operational notes

Source: [official Vidcast recording](https://app.vidcast.io/share/31b01641-f081-4163-886b-5f0612b37033). Reviewed 2026-09-08 using [vendor transcript](../../transcripts/vidcast-integrations/review.txt); interval endpoints come from the first/last included caption's exact `start_time_ms`/`end_time_ms` in [transcript JSON](../../transcripts/vidcast-integrations/transcript.raw.json), not inferred utterance durations. No video-frame inspection or tenant execution was performed.

## Video-derived learning points

Beta/staging demonstration. Flags: C=corroborated; D=demo-specific; U=unverified; T=transcript-only.

1. **00:23:31.169–00:24:15.429** Nodes group methods; at least one is required. [U]
2. **00:25:46.219–00:26:19.438** Public integrations require request/approval before access. [U]
3. **00:27:49.269–00:28:53.979** Separate shared environment variables from tenant-specific values. [U]
4. **00:32:34.149–00:33:41.398** Configure method, URL, connection/request timeouts; demo: POST, 10,000 milliseconds. [C,D]
5. **00:34:18.038–00:35:28.619** Send JSON with static Content-Type and dynamic body inputs. [C]
6. **00:35:57.898–00:37:55.509** Preserve thread identity; require thread/message inputs; configure validation. [C,D]
7. **00:38:29.668–00:39:19.420** Extract bot response from response-body path `$.response`. [C,D,T]
8. **00:39:19.700–00:40:40.190** Define outcomes; demo accepts only HTTP 200. [C,D]
9. **00:41:04.259–00:43:08.019** Inspect raw/output/outcome test results; save reusable test profile before UAT. [U]
10. **00:43:24.919–00:44:17.969** Validate integration, then publish to UAT. [U]
11. **00:46:20.910–00:47:04.080** Map node inputs; capture output through transition actions. [C]
12. **00:47:04.880–00:47:35.079** Send bot reply, receive WhatsApp response, update message input, loop. [D]

## Separate current-document corroboration and clarification

The local official-document cache identifies version **6.20.0**, retrieved **2026-09-08**. Custom Node documentation corroborates shared concepts, not every Integrations Studio beta screen or distribution rule.

1. **Method and timeout fields (point 4).** Request Timeout and Connection Timeout are separate millisecond fields. Resource URLs support `$(param1)`. Choose values from the target API's behavior; 10,000 ms is not a documented default here. [Official reference](https://help.webexconnect.io/docs/custom-nodes-integration), [local cache](../../sources/cache/help/custom-nodes-integration.md).
2. **Inputs and UI (points 5–6).** The official tutorial configures a static `Content-Type: application/json` header and dynamic JSON body fields. The reference permits mandatory fields, regex validation, tooltips, and text/selection/date-time inputs. This corroborates configuration mechanics, not the bot's thread-ID contract. [Official tutorial](https://help.webexconnect.io/docs/using-custom-node-to-configure-your-own-integrations), [local tutorial](../../sources/cache/help/using-custom-node-to-configure-your-own-integrations.md), [official reference](https://help.webexconnect.io/docs/custom-nodes-integration).
3. **Outputs and outcomes (points 7–8, 11).** Response mappings select Body, HTTP Status, or HTTP Header. Body/header extraction needs a response path; HTTP Status does not. Returned node variables can map to session variables. Status/response-path conditions define node events; the tutorial's 200/non-200 split is an example, not every API's success contract. Confirm `$.response` against the actual payload. [Official reference](https://help.webexconnect.io/docs/custom-nodes-integration), [official tutorial](https://help.webexconnect.io/docs/using-custom-node-to-configure-your-own-integrations).
4. **Authentication boundary.** Current custom-node documentation supports Basic, Digest, AWS Signature, and OAuth 2.0, including authorization-code and client-credentials grants. Select authentication from the API contract. This reference does not establish Studio authentication setup or UAT publishing requirements. [Official reference](https://help.webexconnect.io/docs/custom-nodes-integration).

## Verification limits

This is caption-grounded source analysis, not proof that an imported node or flow runs. The four documentation checks cover configuration semantics. Studio distribution, test-profile gates, and current entitlement require their own current documentation or tenant evidence. Transcript-derived field spellings are provisional until inspected in UI, exported configuration, or the API contract.
