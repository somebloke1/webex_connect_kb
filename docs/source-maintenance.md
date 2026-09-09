# Source corpus and maintenance

This workspace contains authored guidance plus a local research cache of official Webex Connect documentation. Start with [the knowledge map](../knowledge/00-map.md), use [the source catalog](../sources/catalog.md) for exact fields and examples, and use [coverage.json](../sources/coverage.json) for measured scope. The cache carries the publisher's text; it is not newly authored guidance or a promise that every tenant exposes every documented feature.

## What is captured

The first complete retrieval on 2026-09-08 captured **523 official sources**: all **336 visible platform-help navigation pages**, **176 developer pages** (171 API references and 5 app asset/profile prerequisites), **10 current-page release/policy notices**, and **1 Cisco developer tutorial**. The developer navigation audit records all 423 entries, with 247 excluded SDK implementation pages and explicit reasons. Asset onboarding, channel policies, contact-center integration, operations, administrative prerequisites, error catalogs and deprecated integrations are included because they affect whether a flow can work.

The AI Agent focus added **11 directly relevant sources**, bringing the current corpus to **534**: the full Studio administration book, nine essential linked Studio articles, and the Connect AI Agent flow-template guide. The book contains all **seven chapters and 56 tables**; the Studio set contains **64 tables**. Use the [Studio source index](../sources/studio-index.md) for exact section jumps and linked local articles. Instructions, actions/tools, knowledge sources, scripted intents/entities/responses, guardrails, fulfillment, languages, digital deployment and actual flow-template guidance are now available offline.

The local default help/developer SSR metadata reports documentation version **6.20.0**. The current changelog contains a [v6.22.0 September 2026 release notice](https://help.webexconnect.io/changelog/product-update-v6220-september-2026), published September 3. Documentation version, release-notice version and a tenant's deployed version are different facts. Read current release notices when resolving a conflict and check the tenant's actual fields read-only. Version-prefixed web-search results can disagree with default navigation; never silently relabel a source.

The maintained inputs are:

| File | Purpose |
| --- | --- |
| [help-seeds.json](../sources/help-seeds.json) | Current visible platform navigation and discovered default version |
| [api-seeds.json](../sources/api-seeds.json) | Selected developer pages |
| [api-navigation.json](../sources/api-navigation.json) | Full developer navigation, selection/exclusion reasons and deprecated/legacy labels |
| [changelog-seeds.json](../sources/changelog-seeds.json) | Release and policy notices selected from the current changelog page |
| [supplemental-seeds.json](../sources/supplemental-seeds.json) | Individually identified official articles: explicit HTML element or Webex Help chapter/article data |
| [inventory.jsonl](../sources/inventory.jsonl) | One URL record per source: identity, title, family, category, date/version, hashes, status and local paths |
| [catalog.md](../sources/catalog.md) | Human-readable URL and local-source index, grouped by category |
| [coverage.json](../sources/coverage.json) | Computed scope, successes, word totals, schema counts and limits |
| [source-qa.json](../sources/source-qa.json) | Independent source-workflow QA and concrete repair evidence |
| [studio-index.md](../sources/studio-index.md) | AI Agent Studio book section jumps and essential linked references |
| [studio-validation.json](../sources/studio-validation.json) | Executed Studio extraction, table, local-link and source-hash checks |

## Extraction and fidelity

`scripts/sources.py` uses Python's standard library and public HTTPS requests. The useful platform URL is `https://help.webexconnect.io/docs/introduction`, which redirects to the services introduction and includes full ReadMe SSR page data. This site's guessed `/docs/flow-builder`, `/sitemap.xml` and `/llms.txt` routes are not discovery requirements. Real navigation slugs are discovered from the page. A browser-compatible User-Agent and `Accept: text/html` worked; there is no credential, cookie, tenant or access-control bypass.

Each successful source normally has four files in `sources/cache/<family>/`:

- `<slug>.source.md`: exact public `doc.body` source, before normalization.
- `<slug>.md`: readable Markdown with ReadMe table/code/callout blocks normalized, variables substituted, known current/previous navigation slugs resolved, and source provenance at the top.
- `<slug>.txt`: body-only search material; navigation is excluded. Some publisher SSR bodies are Markdown rather than HTML, so their ReadMe blocks are normalized too.
- `<slug>.metadata.json`: document identity, observed version, headings, source dates, extraction method and hashes.

For Webex Help books, the extractor reads public Next.js `pageProps.chapters[*].divHtml`; using only `UIData` would capture an empty wrapper for the Studio book. Standalone articles use `UIData`. The original chapter/article HTML is retained in `.source.md` with `source_body_format: html`. Readable Markdown preserves publisher section anchors, links, headings, field tables and lists; nested or merged-cell tables retain HTML to preserve their relationships. Search text excludes in-document navigation. Publisher title markup is normalized, while raw title and chapter names remain in metadata. These pages provide publisher creation/modification timestamps but no product documentation version; the cache labels that fact rather than inheriting Connect's version.

API reference pages also retain `.api.json`: raw ReadMe API parameters/examples plus the selected OpenAPI operation and component schemas. Full OpenAPI documents are preserved once per content hash under `sources/cache/openapi/`. API schemas are often outside the narrative body; a short page is not evidence that the endpoint has few fields. The extractor falls back from stale `swagger.path` to a valid `api.url` or matching `operationId`. Four basic SMS narrative pages provide no OpenAPI operation; they explicitly say `not_present_in_supplied_openapi`, while preserving the available narrative/parameters/examples. ReadMe `api.auth` values describe publisher metadata; use documented headers/security schemes to establish authentication.

Hashes cover the exact author body, fetched HTML response, normalized files, API metadata and full OpenAPI where available. Raw HTML is not retained, but its response hash is. Figures are linked to official originals instead of downloaded in bulk; screen-only settings still require opening the figure or checking the tenant UI. Unknown `doc:` aliases remain unmodified rather than inventing a destination. The optional Cisco support article 222936 returned HTTP 403 to direct retrieval; authored knowledge retains the separately reviewed citation, but it is outside this cached manifest. Webex Contact Center Flow Designer is a separate product surface and its large activity reference is not imported as Connect-node evidence.

Cache files are research material retained in this private repository so a clone supports offline field lookup and content-hash verification. Publisher rights remain with their owners. Keep authored summaries concise and cite the exact source; do not present the complete research cache as original documentation. Raw workflow imports, media and private browser captures remain excluded; acquisition checks and inventory regeneration that read those imports require the local research files or reacquisition.

## Search before researching again

All commands run from the repository root. The source/search tools have no third-party dependencies and also work with `.venv/bin/python`.

```bash
python3 scripts/search_kb.py 'receive timeout' --limit 5
python3 scripts/search_kb.py evtid correlationid --scope sources --all
python3 scripts/search_kb.py 'Resume Key' --scope sources --phrase
python3 scripts/search_kb.py thread --family developer --version 6.20.0 --json
python3 scripts/search_kb.py handoff --scope knowledge
python3 scripts/search_kb.py integrations --scope transcripts
```

Search is local BM25 with title/path boosts. It returns source URLs, paths, exact local line numbers and matched snippets. `--all` requires every token, `--phrase` requires a literal case-insensitive phrase, and `--json` supplies structured results to an agent. `--version` filters recorded source documentation, not deployment compatibility. Read surrounding rows and the full selected source before using a field or branch name.

Authored Markdown is searched in `knowledge`, `docs`, `patterns`, `templates`, `examples`, and `skills`. Transcript search reads only normalized `transcripts/**/transcript.srt` files with sibling `metadata.json`, avoiding duplicate raw captions and review notes. It excludes `fixtures`, `local-asr-validation`, and metadata marked `evidence_type: synthetic_fixture`. It carries the source title, URL, processing method and review status, and snippets include SRT timestamps. A transcript is speech evidence; confirm exact UI labels, types and limits against text sources or read-only tenant inspection.

## Refresh procedure

Discovery is read-only and does not touch tenant configuration. Ingest replaces generated cache files for the selected sources and updates the local manifest. If preserving historical generated snapshots matters, copy the cache and inventory into a dated local archive before `--refresh`; previous content hashes alone do not preserve old content.

```bash
python3 scripts/sources.py discover
python3 scripts/sources.py discover-changelog --pages 1
python3 scripts/sources.py ingest --seeds sources/help-seeds.json sources/api-seeds.json sources/changelog-seeds.json sources/supplemental-seeds.json
python3 scripts/sources.py verify
python3 scripts/sources.py catalog
```

The default ingest resumes successful cached records. To actually fetch existing pages again, add `--refresh`, optionally with `--match` to constrain scope:

```bash
python3 scripts/sources.py ingest --seeds sources/help-seeds.json --refresh --match receive-node
python3 scripts/sources.py ingest --seeds sources/api-seeds.json --refresh --match custom-event-v1
```

Use `--workers 4` for moderate concurrency (the tool caps at 8). Failures are recorded and produce a nonzero exit. Do not repeatedly retry an unchanged access failure. Fix an identified extraction/URL problem or use an authorized alternate source; retain the limitation if the source stays inaccessible. If the supplemental article's explicit HTML selector changes, extraction fails rather than ingesting page navigation.

Developer navigation selection is deliberately explicit. When releases add API categories or move pages, revisit `api-navigation.json` and regenerate selected seeds from the public developer SSR `sidebars` data, preserving SDK exclusions. The current ingest automatically resolves page versions, but it does not silently expand a curated API scope. New release notices are discovered separately; the first page currently covers 2026, and older pages can be added with `--pages` when a migration question needs them.

After refresh, inspect source/hash changes and release notices for changed fields, removals, channel policies, error meanings and deployment constraints. Update the relevant authored chapter and recipes, including its source date and any unresolved conflict. `sources.py verify` hashes the actual bytes of every referenced body/schema file, including publisher CRLF line endings, against its stored hash; it does not validate tenant behavior, execute payload examples, or certify publisher example code. The verified source workflow performed no tenant mutation, flow test, message send or deployment.

## Sample graph retrieval

`python scripts/search_kb.py 'packageNum' --scope samples --json --limit 3`
searches the sanitized per-sample relationship summaries. It excludes duplicate
raw captures and vendor imports. Follow `source_path` to the observed model and
`authored_walkthrough` for its coherent interpretation; runtime status remains
explicit. Refresh the sample inventory after summaries change with
`python scripts/update_sample_inventory.py`.

The read-only captured canvases and authored narrative inputs are separate from
the public documentation cache. Regenerate relationship JSON and both walkthrough
reports after captures or narratives change:

```bash
python3 scripts/summarize_sample_graphs.py
python3 scripts/update_sample_inventory.py
```

Narrative inputs are `observed-narratives.json`, `native-narratives.json`,
`wxcc-selected-narratives.json`, `wxcc-narratives.json` and
`wxcc-social-narratives.json` under `evidence/sample-flows/`. Their keys match
observed filenames. The generator counts operative vertex nodes separately from
edges and End records, preserves node/event/field relationships, and flags End
parents absent from the capture and duplicated bindings. It does not repair
sample wiring or infer an unseen producer. Cyclic node groups are unordered
graph components, not an execution trace.

The current bounded sample collection is 59: nine tenant gallery examples,
17 native AI fulfillment workflows, and all 33 workflows in the current WxCC
v3.5 collection. Only after the capturing agent confirms that scope is complete
and every narrative exists, run
`python3 scripts/summarize_sample_graphs.py --capture-complete --expected-count 59`.
The completion flag requires both the expected count and authored narratives;
it does not claim runtime testing or completeness across historical versions.
Recapture hashes invalidate previous inventory summary status until regeneration.
