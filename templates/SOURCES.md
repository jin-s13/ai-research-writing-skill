# Template Audit Policy

The machine-readable source of truth is `manifest.json`.

Audit rules:

1. Use only official venue pages, official organization repositories, or author-kit archives directly linked by them.
2. Record the exact archive URL and SHA-256 when a stable download is available.
3. Treat permission to use a submission template as distinct from permission to redistribute it.
4. Do not vendor template files when an explicit redistribution license cannot be established.
5. Mark unresolved packages `manual-download-required`; never substitute an unofficial mirror silently.
6. Re-audit yearly editions before updating a venue id or archive hash.

Audit date: 2026-07-16.
