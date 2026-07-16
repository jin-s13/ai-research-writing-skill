# Venue Template Sources

This repository does not redistribute conference author kits when redistribution terms are unclear. It keeps an audited manifest and downloads pinned official archives into the user's paper project.

## Fetch a Pinned Template

```bash
python3 scripts/fetch_template.py --list
python3 scripts/fetch_template.py icml2026 --output /path/to/paper
```

The downloader:

- accepts only template ids from `manifest.json`;
- downloads from the recorded official source;
- verifies the audited SHA-256 before extraction;
- rejects path traversal, symbolic links, and existing output directories;
- fails explicitly when no pinned archive has been audited.

When a hash changes, do not bypass the check. Inspect the new official package, update its source/license record, run template compilation checks, and then update the manifest.

## Current Coverage

Pinned downloads are available for ICML 2026, ICLR 2026, CVPR 2026, ICCV 2025, and the rolling ACL style package. NeurIPS 2025, ECCV 2026, AAAI 2026, and COLM 2025 remain manual downloads because this audit did not establish both a stable archive and sufficiently clear redistribution/source conditions.

Always verify current page limits, anonymity rules, checklist requirements, and camera-ready instructions on the `official_page` recorded in `manifest.json`.
