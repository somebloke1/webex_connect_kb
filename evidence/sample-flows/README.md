# Sample evidence index

Start with [sample-inventory.json](sample-inventory.json), then the source-specific manifests and observed graph summaries. The inventory has **95 entries**, not 95 unique flows: gallery entries, repository versions, tutorials and older documentation occurrences remain separate to preserve provenance.

The native graph inspection collection is **59 samples**: the tenant gallery's 9 templates, all 17 published AI fulfillment workflows, and all 33 workflow ZIPs in the linked digital-channel repository's current v3.5 collection. The 17 workflows and 33 ZIPs were acquired locally; the 9 gallery templates come from the observed tenant gallery. Older repository releases are excluded as historical versions, not silently counted as new samples.

| Evidence | Purpose |
|---|---|
| [Public AI manifest](public-native-manifest.json) | All doctor, banking and airline workflow acquisitions, hashes and separate later UI inspection evidence |
| [Digital-channel manifest](public-wxcc-manifest.json) | All 33 v3.5 archives and source README captures; ZIP-member identities and later UI evidence |
| [Additional import plan](additional-wxcc-import-plan.json) | The final 20 archives added after the initial 13; not a full collection list |
| [Observed captures](observed/) | Sanitized configured canvas models gathered through temporary sample inspection |
| [Derived summaries](summaries/) | Node IDs, connections, variable bindings and terminal outcomes extracted from captures |
| [Tenant walkthroughs](../tenant-samples.md) | Coherent graph explanations based on observed models |
| [Public walkthroughs](../../knowledge/15-sample-flow-walkthroughs.md) | AI, EPIC and initial SMS samples |
| [Additional public walkthroughs](../../knowledge/16-additional-sample-walkthroughs.md) | Remaining email/SMS, bot, task-context, survey and queue-estimate relationships |
| [CCE acquisition](cce-acquisition-status.json) | HTTP capture returned 403; browser follow-up displayed a Cisco.com login/service-contract gate. All 15 documented bundle entries remain inventoried without native graph claims |

Run `python scripts/update_sample_inventory.py` from the workspace root after adding captures or summaries. This only reads/writes local evidence. It refreshes inspection statuses and appends supported UI inspection records to the acquisition manifests while retaining the earlier unsuccessful static decoding checks as history.

`in_priority_scope` is an AI/email/SMS retrieval tag. Every sample in a selected collection has `in_collection_scope: true`, including other-channel variants. A downloaded file, a diagram, a configured canvas and an executed flow are different evidence levels; none of these samples was executed by this research workflow. The JSON counts are the current status, and no fixed progress count in this README should substitute for them.

Raw vendor files and images live in the ignored `raw/` folder. Authored walkthroughs are compact paraphrases, not redistributions of vendor workflow code. Paths to raw evidence are local research dependencies and may not exist in a copy that omits ignored material.

A fresh clone retains the sanitized observations, derived summaries, narratives
and provenance manifests. Regenerate summaries with
`python scripts/summarize_sample_graphs.py --capture-complete --expected-count 59`.
The separate inventory refresh above requires acquisition metadata from `raw/`;
use the committed inventory when those local research files are unavailable.
