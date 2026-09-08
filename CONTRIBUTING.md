# Contributing

Read the README for installation and [LICENSE.md](LICENSE.md) for the current rights status. The original code does not yet carry an open-source license.

## Application changes

Create a branch from `main`, keep changes focused, and run all five validation commands in the README before opening a pull request. Include a short description of the problem, the resulting behavior and the checks performed. For interface changes, check the production preview with keyboard navigation and a narrow viewport.

Lint covers the atlas app, player, scripts and configuration. Bundled `website/components/ui/` and `website/hooks/` primitives are excluded from lint because the existing generated component library has separate lint issues; all TypeScript remains checked by the build. If you change those primitives, review their accessibility and behavior explicitly.

Use `npm ci --prefix website` for reproducible installation. Commit dependency changes together with the lockfile and regenerated `website/public/THIRD-PARTY-NOTICES.txt`. License collection requires curl/network access; ordinary builds use the committed notices. Preserve attribution links and the distinction between application code, database licenses and audio rights.

## Station and map corrections

Use the station-update issue template to provide an official source page, public HTTPS stream URL, country assignment and evidence for any geographic correction. No embedded credentials, access bypasses or invented studio locations. A successful audio probe does not prove editorial legitimacy or rights ownership.

Maintained additions belong in `documents/supplemental-stations.json`; regenerate and finalize the catalog using the README commands. Keep the changed catalog, endpoint evidence, coverage, discovery report and location audit together. Review changes before publishing. New research ledger entries are candidates, not automatically approved catalog additions.

Do not regenerate tens of thousands of network checks for a UI-only change. Offline regression tests exercise the probe's safety behavior. Live refreshes are deliberate maintainer operations and do not run in pull-request CI.

## Repository boundaries

Commit source, locked dependencies, processed public data and validation evidence. Do not commit dependencies, credentials, local `.openai` state, generated builds, raw downloaded directory snapshots, caches or release ZIP files. The Pages workflow publishes only the built static site.
