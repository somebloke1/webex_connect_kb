# Private Git repository packaging validation

Checked 2026-09-09 UTC before the initial commit to
`somebloke1/webex_connect_kb`. This check involved local files and Git only;
it made no Webex Connect or Control Hub configuration changes.

An independent review of the candidate payload found seven JWT-shaped values
in nested parameter descriptions across five sanitized sample observations.
Those values were redacted before the first commit. Original captures remain
only in ignored private local storage. The capture helper now redacts this
pattern in ordinary strings and JSON-encoded strings, including descriptions.
A synthetic in-memory check passed without browser access or file writes.

Parent verification established:

- All 59 summary hashes match their source captures. The five affected captures
  preserve their topology and configuration except for the redacted values and
  the updated redaction notice.
- The staged payload has no JWT-shaped residue, ignored private captures, opaque
  workflow imports, media, virtual environments or transient validation output.
- All six normalized transcript sets are included, with four files per set and
  a shared artifact-validation record.
- A clean export of the Git index passed source verification: 534 records,
  1,868 file checks and zero errors. Local search returned results in the
  knowledge, source, sample and transcript scopes.
- The exported copy regenerated all 59 sample summaries and walkthroughs
  successfully. Acquisition checks and inventory refreshes that use ignored
  raw artifacts still require the original local files or reacquisition.

The repository includes publisher-owned reference material for private research.
Attribution and provenance remain attached; repository inclusion grants no
additional redistribution rights.
