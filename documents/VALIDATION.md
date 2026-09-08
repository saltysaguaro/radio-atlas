# Validation and known limits

The production build includes a successful TypeScript check. The standalone player test suite passes seven behavioral checks: immediate unloading when switching, ignoring old stream events, reconnecting after pause, stopping failed audio, handling browser gesture rejection, volume/mute persistence during switching, and an 18-second connection deadline that repeated stalled events cannot postpone.

The release validator checks station/URL uniqueness, uncapped country totals, all country counts, secure stream URLs, recorded audio samples, map country references, relative asset links, and completeness of the static build. It also serves and fetches the built page, scripts, styles, map, catalog and icon at both `/` and `/radio/` using a local HTTP server. The package is checked against the exact built files.

The package registry audit reported zero known vulnerabilities after compatible dependency updates on September 5, 2026. No server framework or server process is needed in the uploaded release.

## Stream verification

Every catalog entry passed a live HTTPS audio-response check with a 4,096-byte sample. Each record stores its timestamp, MIME type, sample size and pinned-public-address evidence. Eleven offline regression checks cover private/mixed DNS and multicast rejection, credentials and malformed URLs, DNS pinning, redirect safety, response rejection, endpoint fallbacks HTTPS upgrades, and an uncapped 130-feed country with cached resume and duplicate handling. They also check that geographic audits are repeatable and do not resurrect obsolete coordinates from an earlier refresh. Supplemental official broadcaster feeds use the same check. No login, subscription, proxy, rebroadcast or insecure TLS bypass is used.

These are network-level checks, not a listening test or proof that every browser can decode every station. No full browser interaction, visual, mobile-device or every-stream decoding test was performed. Search and 50-result pages keep large country lists bounded; map popup lists load on demand. A local preview was requested in Codex. The optional experimental `select_radio_country` WebMCP integration is feature-detected; a supported WebMCP test context was unavailable, so its runtime contract is unverified. Normal use does not depend on it.

## Coverage and hosting

There is no longer a 10–25 station target or country ceiling. The sweep covers the full available directory, but worldwide completeness is not verifiable. Some countries and territories have no qualifying stream in the checked sources. `COVERAGE.md` contains the actual totals and all gaps. Stations without reliable coordinates appear in a dashed country-level group. These are not fabricated studio locations. Directory click counts are a popularity proxy, not national audience ratings.

The site has been built and packaged locally. It has not been uploaded or tested on the user's hosting. Broadcasters can change URLs, restrict regions or stop broadcasting after verification. Station switching stops the old stream immediately; playback of the new one depends on connection and buffering time.

## Expanded release result

The September 5 expansion checked 54,765 distinct endpoint URLs from 64,171 directory records and seven maintained broadcaster additions. The finalized release contains 32,605 streams across 212 countries and territories. All 11 catalog regression tests, seven player tests, the production build, and root/subfolder HTTP release checks passed. The upload folder and ZIP were compared byte-for-byte with the built files. See `catalog-change-report.json` for changes from the previous 2,868-stream release.


## GitHub Pages preparation — September 8, 2026

Validated the GitHub-ready source in an isolated copy containing only Git-eligible files, with no existing `node_modules`, build output or raw directory snapshot. A fresh `npm ci` completed against the committed lockfile using Node 22.22.2. Application lint, seven player tests, 11 catalog tests, TypeScript checking and the Vite production build passed in that clean copy. Python checks ran on Python 3.14.6; GitHub's Ubuntu runner provides Python 3 for the same standard-library-only tooling.

The release validator matched all 32,605 streams against committed endpoint evidence, checked 250 country/territory entries and 212 with streams, and fetched HTML, JavaScript, CSS, catalog, map, icon and license notices over real local HTTP at `/`, `/radio-atlas/` and `/renamed-repository/`. The built catalog, map and notices match the committed public inputs. `.nojekyll` is included. The updated upload folder and ZIP were regenerated and checked byte-for-byte against the build.

The application lint fixes move map callback ref updates out of render, initialize saved volume without an effect state update, retain the exact map collection for cleanup, associate the country label with its control, and use native status elements. Vendored UI primitives/hooks are excluded from lint; TypeScript checks still include them. The production JavaScript bundle is approximately 527 kB before gzip (168 kB gzipped), so Vite emits its existing advisory chunk-size warning. This does not fail the build.

GitHub workflow and Dependabot YAML were parsed locally; workflow triggers, build dependency and pinned action references were checked. CI validates pull requests and deploys only successful `main` builds. The workflow itself has not yet run on GitHub, and no live Pages URL or browser interaction test is claimed. GitHub CLI authentication for the configured account was verified with network access. The project is prepared locally; no GitHub repository was created or pushed and no Pages deployment was performed in this preparation step.
