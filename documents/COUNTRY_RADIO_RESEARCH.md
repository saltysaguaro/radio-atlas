# Country-by-country radio discovery ledger

Created: 2026-09-06. Schedule: hourly, one country or territory per run.
Workspace: the local `radio-atlas` project folder. File paths below are relative to the repository root.

## Coverage and sources

The checklist contains 250 entries: the 249 ISO 3166-1 countries and territories plus Kosovo (`XK`, the project's non-ISO code). It uses the existing project catalog's names and codes so findings can be mapped directly to Radio Atlas. Palestine (`PS`) and Western Sahara (`EH`) have their own rows, as do Taiwan, Kosovo, dependencies, and uninhabited territories. Inclusion is for research coverage and does not express a position on sovereignty.

Reference lists: [ISO country-code browser](https://www.iso.org/obp/ui/#search/code/), [UN countries and areas](https://unstats.un.org/unsd/methodology/m49/), and the project's [country dataset](https://github.com/mledoze/countries). Local baseline: `website/public/data/catalog.json`; existing methodology: `documents/SOURCES.md`.

Search all constituent areas within grouped entries: Bonaire, Sint Eustatius and Saba under Caribbean Netherlands; Saint Helena, Ascension and Tristan da Cunha under SH; Svalbard and Jan Mayen under SJ; and the constituent islands under UM. South Georgia includes the South Sandwich Islands. Use local names and alternate names, including Côte d’Ivoire, Cabo Verde, Holy See, and State of Palestine. Record distinct local or disputed-area provenance within the relevant entry; do not silently assign a station to a neighboring country or infer origin from its server location. Add separately evidenced coverage gaps as explicit checklist entries with a documented catalog-code mapping rather than inventing ISO codes.

## Persistent progress

- Completed research runs: 162
- Current sweep: 1
- Next country: Niue (`NU`)
- Last run: Run 0116 — Kazakhstan (`KZ`), partial, ended 2026-09-11T22:45:38Z; no new ready candidates.
- Automation: `hourly-country-radio-discovery` — active hourly schedule attached to the research task.

The checklist and appended run logs are the source of truth, not conversation memory. Baseline station counts are a setup snapshot, not new discoveries or current availability claims. Dashes mean not yet researched, not zero.

## Hourly procedure

Cost controls revised on 2026-09-07 at the user's request. The hourly cadence and all 250 entries remain. Depth accumulates over bounded visits instead of an exhaustive search every hour.

1. Run `python3 scripts/research_country.py context`. Read this procedure and the selected country's latest short summary only; never load the archive, full catalog, whole ledger or conversation history for research. Resume an interrupted entry first; otherwise use the lowest Runs count, then checklist order. Mark it `in-progress` and create a timestamped run header before work.
2. Record the account-wide seven-day `usedPercent` and `resetsAt` from `get_usage_limits` at start and end, using `rateLimitsByLimitId.codex` when available. These are approximate account readings, not per-task billing; unavailable values stay unknown. Do not read or save account IDs or credits. If the same window rises by at least 1 percentage point during a run, save progress, pause this automation with `automation_update`, and report the readings for review. Do not redeem resets. This is a conservative cost guard; other account activity can trigger it.
3. Spend at most **4 minutes researching, 6 actual search queries, 8 source-page opens/fetches, and 10 unique stream-check inputs per hourly run**. Count all batches together. These are ceilings, not targets; stop early when useful progress stops. Check elapsed time after each batch; allow a short closeout to save results. Work serially without subagents, premium-model escalation, full catalog refreshes, or custom scripts generated anew each hour.
4. In the first visit, use a country overview and relevant local-language query to find strong leads. Prioritize public/national broadcasters and primary evidence; use a directory only for discovery. On later sweeps, follow saved leads and rotate commercial, community, regional/minority, university and internet-only categories. Skip categories already addressed unless new evidence warrants a revisit. Record unsearched categories; the cap is not evidence of exhaustive coverage. Keep country and territory provenance explicit, including Palestine and Western Sahara.
5. Verify identity and broadcasting country from an official source. Write only the most promising stream URLs into `documents/research/run-NNNN-CC-inputs.json` as an array of strings. Run `python3 scripts/research_country.py check documents/research/run-NNNN-CC-inputs.json --output documents/research/run-NNNN-CC-probes.json`. Reuse that output path throughout a run and across interruptions. The helper caps inputs at ten, skips exact catalog duplicates, reuses earlier run checks, checks resolved URLs against the global catalog and supplements, and identifies prior research mentions without loading history into model context. A prior mention may be a failed lead, so inspect a short matching excerpt before declaring a research duplicate. Similar names alone are insufficient.
6. Keep strict public HTTPS/TLS checks and the existing bounded MP3/AAC/Ogg probe. Do not retry failed hosts during the same run, bypass restrictions, or upgrade the model to chase a difficult lead. A ready candidate still requires primary identity/country evidence, a fresh successful probe and completed global duplicate review. A probe is not proof of worldwide availability or browser decoding. Unknowns remain `needs verification`.
7. Record a concise summary and candidate table in this Markdown file, with links to sources and the per-run evidence files. Store raw probe results and proposed supplemental JSON in `documents/research/`; never paste raw HTML, directory responses, large JSON or repeated metadata into the ledger/tool output. Preserve previous evidence. Save pending source URLs and the next specific research action for the country's next sweep.
8. Close the run as `partial`, `searched`, or `blocked` with actual counts and times. Increment Runs exactly once even for partial/blocked attempts; update the checklist and Persistent progress, then select the next country using the same rule. An interruption remains `in-progress` and resumes with the original counters/start time; do not restart its budget. Validate 250 unique country codes (including PS/EH/XK) and consistent counts with the context helper. Do not change the catalog, supplements, releases or deployment.

Statuses: `pending`, `in-progress`, `searched`, `partial`, `blocked`. Counts describe the latest finished attempt, not an exhaustive census. Historical research is linked from each checklist row; the archive is for targeted evidence lookup only.

## Country and territory checklist

| # | Code | Country / territory | Baseline feeds | Runs | Status | Last run (UTC) | Candidates | Ready | Latest log |
| --- | --- | --- | ---: | ---: | --- | --- | ---: | ---: | --- |
| 1 | AF | Afghanistan | 45 | 1 | partial | 2026-09-06T20:33:58Z | 17 | 2 | [Run 0001](research/archive/runs-0001-0020.md#run-0001-af) |
| 2 | AX | Åland Islands | 1 | 1 | partial | 2026-09-06T21:33:53Z | 12 | 1 | [Run 0002](research/archive/runs-0001-0020.md#run-0002-ax) |
| 3 | AL | Albania | 23 | 1 | partial | 2026-09-06T22:37:09.442219+00:00 | 85 | 14 | [Run 0003](research/archive/runs-0001-0020.md#run-0003-al) |
| 4 | DZ | Algeria | 48 | 1 | partial | 2026-09-06T23:38:44.340525+00:00 | 118 | 33 | [Run 0004](research/archive/runs-0001-0020.md#run-0004-dz) |
| 5 | AS | American Samoa | 5 | 1 | partial | 2026-09-07T00:34:55.642578+00:00 | 35 | 4 | [Run 0005](research/archive/runs-0001-0020.md#run-0005-as) |
| 6 | AD | Andorra | 6 | 1 | partial | 2026-09-07T01:37:54.095312+00:00 | 48 | 8 | [Run 0006](research/archive/runs-0001-0020.md#run-0006-ad) |
| 7 | AO | Angola | 8 | 1 | partial | 2026-09-07T02:43:04.907636+00:00 | 100 | 44 | [Run 0007](research/archive/runs-0001-0020.md#run-0007-ao) |
| 8 | AI | Anguilla | 2 | 1 | partial | 2026-09-07T03:36:48.497448+00:00 | 34 | 4 | [Run 0008](research/archive/runs-0001-0020.md#run-0008-ai) |
| 9 | AQ | Antarctica | 6 | 1 | partial | 2026-09-07T04:36:49.537007+00:00 | 30 | 0 | [Run 0009](research/archive/runs-0001-0020.md#run-0009-aq) |
| 10 | AG | Antigua and Barbuda | 2 | 1 | partial | 2026-09-07T05:46:35.698199+00:00 | 44 | 9 | [Run 0010](research/archive/runs-0001-0020.md#run-0010-ag) |
| 11 | AR | Argentina | 843 | 1 | partial | 2026-09-07T06:45:58.737884+00:00 | 129 | 19 | [Run 0011](research/archive/runs-0001-0020.md#run-0011-ar) |
| 12 | AM | Armenia | 8 | 1 | partial | 2026-09-07T07:44:12.010794+00:00 | 43 | 11 | [Run 0012](research/archive/runs-0001-0020.md#run-0012-am) |
| 13 | AW | Aruba | 3 | 1 | partial | 2026-09-07T08:42:35.795119+00:00 | 52 | 18 | [Run 0013](research/archive/runs-0001-0020.md#run-0013-aw) |
| 14 | AU | Australia | 753 | 1 | partial | 2026-09-07T09:47:46.055824+00:00 | 90 | 26 | [Run 0014](research/archive/runs-0001-0020.md#run-0014-au) |
| 15 | AT | Austria | 228 | 1 | partial | 2026-09-07T10:47:54.126796+00:00 | 324 | 11 | [Run 0015](research/archive/runs-0001-0020.md#run-0015-at) |
| 16 | AZ | Azerbaijan | 19 | 1 | partial | 2026-09-07T11:50:38.888147+00:00 | 48 | 8 | [Run 0016](research/archive/runs-0001-0020.md#run-0016-az) |
| 17 | BS | Bahamas | 4 | 1 | partial | 2026-09-07T12:53:09.162369+00:00 | 60 | 14 | [Run 0017](research/archive/runs-0001-0020.md#run-0017-bs) |
| 18 | BH | Bahrain | 4 | 1 | partial | 2026-09-07T13:47:48.335455+00:00 | 44 | 5 | [Run 0018](research/archive/runs-0001-0020.md#run-0018-bh) |
| 19 | BD | Bangladesh | 14 | 1 | partial | 2026-09-07T14:52:39.260035+00:00 | 82 | 13 | [Run 0019](research/archive/runs-0001-0020.md#run-0019-bd) |
| 20 | BB | Barbados | 7 | 1 | partial | 2026-09-07T15:51:03.206315+00:00 | 42 | 7 | [Run 0020](research/archive/runs-0001-0020.md#run-0020-bb) |
| 21 | BY | Belarus | 39 | 1 | partial | 2026-09-07T16:38:02Z | 4 | 0 | [Run 0021](#run-0021-by) |
| 22 | BE | Belgium | 295 | 1 | partial | 2026-09-07T17:39:33Z | 4 | 0 | [Run 0022](#run-0022-be) |
| 23 | BZ | Belize | 1 | 1 | partial | 2026-09-07T18:39:33Z | 4 | 0 | [Run 0023](#run-0023-bz) |
| 24 | BJ | Benin | 3 | 1 | partial | 2026-09-07T19:40:33Z | 3 | 0 | [Run 0024](#run-0024-bj) |
| 25 | BM | Bermuda | 5 | 1 | partial | 2026-09-07T22:18:50Z | 4 | 0 | [Run 0025](#run-0025-bm) |
| 26 | BT | Bhutan | 1 | 1 | partial | 2026-09-07T23:18:20Z | 1 | 0 | [Run 0026](#run-0026-bt) |
| 27 | BO | Bolivia | 55 | 1 | partial | 2026-09-08T00:21:50Z | 4 | 0 | [Run 0027](#run-0027-bo) |
| 28 | BA | Bosnia and Herzegovina | 50 | 1 | partial | 2026-09-08T01:22:21Z | 4 | 0 | [Run 0028](#run-0028-ba) |
| 29 | BW | Botswana | 0 | 1 | partial | 2026-09-08T02:24:21Z | 4 | 0 | [Run 0029](#run-0029-bw) |
| 30 | BV | Bouvet Island | 0 | 1 | searched | 2026-09-08T03:25:51Z | 0 | 0 | [Run 0030](#run-0030-bv) |
| 31 | BR | Brazil | 1008 | 1 | partial | 2026-09-08T04:26:21Z | 4 | 0 | [Run 0031](#run-0031-br) |
| 32 | IO | British Indian Ocean Territory | 6 | 1 | partial | 2026-09-08T05:27:52Z | 4 | 0 | [Run 0032](#run-0032-io) |
| 33 | VG | British Virgin Islands | 0 | 1 | partial | 2026-09-08T06:27:22Z | 4 | 0 | [Run 0033](#run-0033-vg) |
| 34 | BN | Brunei | 4 | 1 | partial | 2026-09-08T07:27:52Z | 4 | 0 | [Run 0034](#run-0034-bn) |
| 35 | BG | Bulgaria | 111 | 1 | partial | 2026-09-08T08:28:22Z | 4 | 0 | [Run 0035](#run-0035-bg) |
| 36 | BF | Burkina Faso | 4 | 1 | partial | 2026-09-08T09:30:22Z | 4 | 0 | [Run 0036](#run-0036-bf) |
| 37 | BI | Burundi | 0 | 1 | partial | 2026-09-08T10:31:23Z | 4 | 0 | [Run 0037](#run-0037-bi) |
| 38 | KH | Cambodia | 5 | 1 | partial | 2026-09-08T11:32:53Z | 4 | 0 | [Run 0038](#run-0038-kh) |
| 39 | CM | Cameroon | 1 | 1 | partial | 2026-09-08T12:33:23Z | 4 | 0 | [Run 0039](#run-0039-cm) |
| 40 | CA | Canada | 750 | 1 | partial | 2026-09-08T13:33:53Z | 4 | 0 | [Run 0040](#run-0040-ca) |
| 41 | CV | Cape Verde | 15 | 1 | partial | 2026-09-08T14:34:54Z | 4 | 0 | [Run 0041](#run-0041-cv) |
| 42 | BQ | Caribbean Netherlands | 8 | 1 | partial | 2026-09-08T15:35:54Z | 4 | 0 | [Run 0042](#run-0042-bq) |
| 43 | KY | Cayman Islands | 6 | 1 | partial | 2026-09-08T16:35:24Z | 4 | 0 | [Run 0043](#run-0043-ky) |
| 44 | CF | Central African Republic | 2 | 1 | partial | 2026-09-08T17:35:24Z | 4 | 0 | [Run 0044](#run-0044-cf) |
| 45 | TD | Chad | 1 | 1 | partial | 2026-09-08T18:38:24Z | 4 | 0 | [Run 0045](#run-0045-td) |
| 46 | CL | Chile | 392 | 1 | partial | 2026-09-08T19:38:55Z | 4 | 0 | [Run 0046](#run-0046-cl) |
| 47 | CN | China | 1080 | 1 | partial | 2026-09-08T20:39:25Z | 4 | 0 | [Run 0047](#run-0047-cn) |
| 48 | CX | Christmas Island | 1 | 1 | partial | 2026-09-08T21:39:55Z | 4 | 0 | [Run 0048](#run-0048-cx) |
| 49 | CC | Cocos (Keeling) Islands | 1 | 1 | partial | 2026-09-08T22:40:25Z | 4 | 0 | [Run 0049](#run-0049-cc) |
| 50 | CO | Colombia | 494 | 1 | partial | 2026-09-08T23:40:26Z | 4 | 0 | [Run 0050](#run-0050-co) |
| 51 | KM | Comoros | 0 | 1 | partial | 2026-09-09T00:40:56Z | 4 | 0 | [Run 0051](#run-0051-km) |
| 52 | CG | Congo | 1 | 1 | partial | 2026-09-09T01:40:56Z | 4 | 0 | [Run 0052](#run-0052-cg) |
| 53 | CK | Cook Islands | 0 | 1 | partial | 2026-09-09T02:40:26Z | 4 | 0 | [Run 0053](#run-0053-ck) |
| 54 | CR | Costa Rica | 38 | 1 | partial | 2026-09-09T03:43:57Z | 4 | 0 | [Run 0054](#run-0054-cr) |
| 55 | HR | Croatia | 107 | 1 | partial | 2026-09-09T04:44:57Z | 4 | 0 | [Run 0055](#run-0055-hr) |
| 56 | CU | Cuba | 12 | 1 | partial | 2026-09-09T05:44:27Z | 4 | 0 | [Run 0056](#run-0056-cu) |
| 57 | CW | Curaçao | 17 | 1 | partial | 2026-09-09T06:44:27Z | 4 | 0 | [Run 0057](#run-0057-cw) |
| 58 | CY | Cyprus | 26 | 1 | partial | 2026-09-09T07:45:28Z | 4 | 0 | [Run 0058](#run-0058-cy) |
| 59 | CZ | Czechia | 183 | 1 | partial | 2026-09-09T08:46:58Z | 4 | 0 | [Run 0059](#run-0059-cz) |
| 60 | DK | Denmark | 124 | 1 | partial | 2026-09-09T09:46:28Z | 4 | 0 | [Run 0060](#run-0060-dk) |
| 61 | DJ | Djibouti | 0 | 1 | partial | 2026-09-09T10:46:28Z | 4 | 0 | [Run 0061](#run-0061-dj) |
| 62 | DM | Dominica | 5 | 1 | partial | 2026-09-09T11:47:28Z | 5 | 0 | [Run 0062](#run-0062-dm) |
| 63 | DO | Dominican Republic | 81 | 1 | partial | 2026-09-09T12:48:59Z | 4 | 0 | [Run 0063](#run-0063-do) |
| 64 | CD | DR Congo | 11 | 1 | partial | 2026-09-09T13:48:29Z | 4 | 0 | [Run 0064](#run-0064-cd) |
| 65 | EC | Ecuador | 122 | 1 | partial | 2026-09-09T14:49:59Z | 4 | 0 | [Run 0065](#run-0065-ec) |
| 66 | EG | Egypt | 29 | 1 | partial | 2026-09-09T15:49:29Z | 4 | 0 | [Run 0066](#run-0066-eg) |
| 67 | SV | El Salvador | 40 | 1 | partial | 2026-09-09T16:49:30Z | 4 | 0 | [Run 0067](#run-0067-sv) |
| 68 | GQ | Equatorial Guinea | 0 | 1 | partial | 2026-09-09T17:50:30Z | 4 | 0 | [Run 0068](#run-0068-gq) |
| 69 | ER | Eritrea | 1 | 1 | partial | 2026-09-09T18:51:00Z | 4 | 0 | [Run 0069](#run-0069-er) |
| 70 | EE | Estonia | 86 | 1 | partial | 2026-09-09T19:52:30Z | 4 | 0 | [Run 0070](#run-0070-ee) |
| 71 | SZ | Eswatini | 0 | 1 | partial | 2026-09-09T20:53:31Z | 4 | 0 | [Run 0071](#run-0071-sz) |
| 72 | ET | Ethiopia | 22 | 1 | partial | 2026-09-09T21:53:31Z | 4 | 0 | [Run 0072](#run-0072-et) |
| 73 | FK | Falkland Islands | 4 | 1 | partial | 2026-09-09T22:53:31Z | 4 | 0 | [Run 0073](#run-0073-fk) |
| 74 | FO | Faroe Islands | 6 | 1 | partial | 2026-09-09T23:54:01Z | 4 | 0 | [Run 0074](#run-0074-fo) |
| 75 | FJ | Fiji | 6 | 1 | partial | 2026-09-10T00:55:32Z | 4 | 0 | [Run 0075](#run-0075-fj) |
| 76 | FI | Finland | 87 | 1 | partial | 2026-09-10T01:56:02Z | 4 | 0 | [Run 0076](#run-0076-fi) |
| 77 | FR | France | 1561 | 1 | partial | 2026-09-10T02:56:32Z | 4 | 0 | [Run 0077](#run-0077-fr) |
| 78 | GF | French Guiana | 3 | 1 | partial | 2026-09-10T03:57:20Z | 4 | 0 | [Run 0078](#run-0078-gf) |
| 79 | PF | French Polynesia | 6 | 1 | partial | 2026-09-10T04:57:50Z | 4 | 0 | [Run 0079](#run-0079-pf) |
| 80 | TF | French Southern and Antarctic Lands | 0 | 1 | partial | 2026-09-10T05:58:21Z | 4 | 0 | [Run 0080](#run-0080-tf) |
| 81 | GA | Gabon | 0 | 1 | partial | 2026-09-10T07:01:21Z | 4 | 0 | [Run 0081](#run-0081-ga) |
| 82 | GM | Gambia | 0 | 1 | partial | 2026-09-10T08:01:51Z | 4 | 0 | [Run 0082](#run-0082-gm) |
| 83 | GE | Georgia | 12 | 1 | partial | 2026-09-10T09:02:21Z | 4 | 0 | [Run 0083](#run-0083-ge) |
| 84 | DE | Germany | 4341 | 1 | partial | 2026-09-10T10:03:22Z | 4 | 0 | [Run 0084](#run-0084-de) |
| 85 | GH | Ghana | 75 | 1 | partial | 2026-09-10T11:03:22Z | 4 | 0 | [Run 0085](#run-0085-gh) |
| 86 | GI | Gibraltar | 6 | 1 | partial | 2026-09-10T12:04:52Z | 6 | 0 | [Run 0086](#run-0086-gi) |
| 87 | GR | Greece | 1227 | 1 | partial | 2026-09-10T13:05:52Z | 10 | 0 | [Run 0087](#run-0087-gr) |
| 88 | GL | Greenland | 5 | 1 | partial | 2026-09-10T14:05:52Z | 5 | 0 | [Run 0088](#run-0088-gl) |
| 89 | GD | Grenada | 3 | 1 | partial | 2026-09-10T15:05:53Z | 3 | 0 | [Run 0089](#run-0089-gd) |
| 90 | GP | Guadeloupe | 10 | 1 | partial | 2026-09-10T16:06:23Z | 10 | 0 | [Run 0090](#run-0090-gp) |
| 91 | GU | Guam | 3 | 1 | partial | 2026-09-10T17:07:23Z | 3 | 0 | [Run 0091](#run-0091-gu) |
| 92 | GT | Guatemala | 58 | 1 | partial | 2026-09-10T18:07:23Z | 10 | 0 | [Run 0092](#run-0092-gt) |
| 93 | GG | Guernsey | 1 | 1 | partial | 2026-09-10T19:08:24Z | 2 | 0 | [Run 0093](#run-0093-gg) |
| 94 | GN | Guinea | 4 | 1 | partial | 2026-09-10T20:09:24Z | 4 | 0 | [Run 0094](#run-0094-gn) |
| 95 | GW | Guinea-Bissau | 1 | 1 | partial | 2026-09-10T21:10:24Z | 1 | 0 | [Run 0095](#run-0095-gw) |
| 96 | GY | Guyana | 7 | 1 | partial | 2026-09-11T02:22:04Z | 7 | 0 | [Run 0096](#run-0096-gy) |
| 97 | HT | Haiti | 22 | 1 | partial | 2026-09-11T03:22:34Z | 10 | 0 | [Run 0097](#run-0097-ht) |
| 98 | HM | Heard Island and McDonald Islands | 0 | 1 | partial | 2026-09-11T04:26:04Z | 0 | 0 | [Run 0098](#run-0098-hm) |
| 99 | HN | Honduras | 31 | 1 | partial | 2026-09-11T05:27:04Z | 10 | 0 | [Run 0099](#run-0099-hn) |
| 100 | HK | Hong Kong | 20 | 1 | partial | 2026-09-11T06:28:35Z | 10 | 0 | [Run 0100](#run-0100-hk) |
| 101 | HU | Hungary | 188 | 1 | partial | 2026-09-11T07:30:05Z | 10 | 0 | [Run 0101](#run-0101-hu) |
| 102 | IS | Iceland | 6 | 1 | partial | 2026-09-11T08:31:05Z | 6 | 0 | [Run 0102](#run-0102-is) |
| 103 | IN | India | 537 | 1 | partial | 2026-09-11T09:31:35Z | 10 | 0 | [Run 0103](#run-0103-in) |
| 104 | ID | Indonesia | 365 | 1 | partial | 2026-09-11T10:33:06Z | 10 | 0 | [Run 0104](#run-0104-id) |
| 105 | IR | Iran | 17 | 1 | partial | 2026-09-11T11:34:36Z | 10 | 0 | [Run 0105](#run-0105-ir) |
| 106 | IQ | Iraq | 14 | 1 | partial | 2026-09-11T12:35:06Z | 10 | 0 | [Run 0106](#run-0106-iq) |
| 107 | IE | Ireland | 119 | 1 | partial | 2026-09-11T13:36:06Z | 10 | 0 | [Run 0107](#run-0107-ie) |
| 108 | IM | Isle of Man | 7 | 1 | partial | 2026-09-11T14:37:07Z | 7 | 0 | [Run 0108](#run-0108-im) |
| 109 | IL | Israel | 85 | 1 | partial | 2026-09-11T15:37:07Z | 10 | 0 | [Run 0109](#run-0109-il) |
| 110 | IT | Italy | 855 | 1 | partial | 2026-09-11T16:37:37Z | 10 | 0 | [Run 0110](#run-0110-it) |
| 111 | CI | Ivory Coast | 11 | 1 | partial | 2026-09-11T17:37:07Z | 10 | 0 | [Run 0111](#run-0111-ci) |
| 112 | JM | Jamaica | 33 | 1 | partial | 2026-09-11T18:39:07Z | 10 | 0 | [Run 0112](#run-0112-jm) |
| 113 | JP | Japan | 69 | 1 | partial | 2026-09-11T19:41:08Z | 10 | 0 | [Run 0113](#run-0113-jp) |
| 114 | JE | Jersey | 2 | 1 | partial | 2026-09-11T20:42:08Z | 2 | 0 | [Run 0114](#run-0114-je) |
| 115 | JO | Jordan | 8 | 1 | partial | 2026-09-11T21:44:08Z | 9 | 0 | [Run 0115](#run-0115-jo) |
| 116 | KZ | Kazakhstan | 17 | 1 | partial | 2026-09-11T22:45:38Z | 10 | 0 | [Run 0116](#run-0116-kz) |
| 117 | KE | Kenya | 33 | 2 | partial | 2026-09-11T23:45:47Z | 10 | 0 | [Run 0118](#run-0118-ke) |
| 118 | KI | Kiribati | 1 | 1 | partial | 2026-09-12T00:45:47Z | 1 | 0 | [Run 0119](#run-0119-ki) |
| 119 | XK | Kosovo | 6 | 1 | partial | 2026-09-12T01:45:48Z | 6 | 0 | [Run 0120](#run-0120-xk) |
| 120 | KW | Kuwait | 8 | 1 | partial | 2026-09-12T02:46:48Z | 8 | 0 | [Run 0121](#run-0121-kw) |
| 121 | KG | Kyrgyzstan | 6 | 1 | partial | 2026-09-12T03:46:48Z | 6 | 0 | [Run 0122](#run-0122-kg) |
| 122 | LA | Laos | 3 | 1 | partial | 2026-09-12T04:47:18Z | 3 | 0 | [Run 0123](#run-0123-la) |
| 123 | LV | Latvia | 50 | 1 | partial | 2026-09-12T05:47:49Z | 10 | 0 | [Run 0124](#run-0124-lv) |
| 124 | LB | Lebanon | 33 | 1 | partial | 2026-09-12T06:48:49Z | 10 | 0 | [Run 0125](#run-0125-lb) |
| 125 | LS | Lesotho | 1 | 1 | partial | 2026-09-12T07:48:19Z | 1 | 0 | [Run 0126](#run-0126-ls) |
| 126 | LR | Liberia | 0 | 1 | partial | 2026-09-12T08:48:49Z | 0 | 0 | [Run 0127](#run-0127-lr) |
| 127 | LY | Libya | 4 | 1 | partial | 2026-09-12T09:49:50Z | 4 | 0 | [Run 0128](#run-0128-ly) |
| 128 | LI | Liechtenstein | 1 | 1 | partial | 2026-09-12T10:49:50Z | 1 | 0 | [Run 0129](#run-0129-li) |
| 129 | LT | Lithuania | 47 | 1 | partial | 2026-09-12T11:50:20Z | 2 | 0 | [Run 0130](#run-0130-lt) |
| 130 | LU | Luxembourg | 20 | 1 | partial | 2026-09-12T12:50:50Z | 10 | 0 | [Run 0131](#run-0131-lu) |
| 131 | MO | Macau | 4 | 1 | partial | 2026-09-12T13:51:20Z | 4 | 0 | [Run 0132](#run-0132-mo) |
| 132 | MG | Madagascar | 8 | 1 | partial | 2026-09-12T14:51:21Z | 8 | 0 | [Run 0133](#run-0133-mg) |
| 133 | MW | Malawi | 7 | 1 | partial | 2026-09-12T15:51:51Z | 7 | 0 | [Run 0134](#run-0134-mw) |
| 134 | MY | Malaysia | 43 | 1 | partial | 2026-09-12T16:52:21Z | 2 | 0 | [Run 0135](#run-0135-my) |
| 135 | MV | Maldives | 3 | 1 | partial | 2026-09-12T17:53:21Z | 3 | 0 | [Run 0136](#run-0136-mv) |
| 136 | ML | Mali | 12 | 1 | partial | 2026-09-12T18:53:52Z | 10 | 0 | [Run 0137](#run-0137-ml) |
| 137 | MT | Malta | 6 | 1 | partial | 2026-09-12T19:55:22Z | 6 | 0 | [Run 0138](#run-0138-mt) |
| 138 | MH | Marshall Islands | 2 | 1 | partial | 2026-09-12T20:56:52Z | 2 | 0 | [Run 0139](#run-0139-mh) |
| 139 | MQ | Martinique | 6 | 1 | partial | 2026-09-12T21:58:22Z | 6 | 0 | [Run 0140](#run-0140-mq) |
| 140 | MR | Mauritania | 0 | 1 | partial | 2026-09-12T22:58:23Z | 0 | 0 | [Run 0141](#run-0141-mr) |
| 141 | MU | Mauritius | 9 | 1 | partial | 2026-09-13T00:00:23Z | 9 | 0 | [Run 0142](#run-0142-mu) |
| 142 | YT | Mayotte | 2 | 1 | partial | 2026-09-13T01:01:23Z | 2 | 0 | [Run 0143](#run-0143-yt) |
| 143 | MX | Mexico | 1217 | 1 | partial | 2026-09-13T02:02:53Z | 10 | 0 | [Run 0144](#run-0144-mx) |
| 144 | FM | Micronesia | 0 | 1 | partial | 2026-09-13T03:04:24Z | 0 | 0 | [Run 0145](#run-0145-fm) |
| 145 | MD | Moldova | 60 | 1 | partial | 2026-09-13T04:04:54Z | 1 | 0 | [Run 0146](#run-0146-md) |
| 146 | MC | Monaco | 5 | 1 | partial | 2026-09-13T05:04:24Z | 5 | 0 | [Run 0147](#run-0147-mc) |
| 147 | MN | Mongolia | 5 | 1 | partial | 2026-09-13T06:04:54Z | 5 | 0 | [Run 0148](#run-0148-mn) |
| 148 | ME | Montenegro | 35 | 1 | partial | 2026-09-13T07:05:55Z | 10 | 0 | [Run 0149](#run-0149-me) |
| 149 | MS | Montserrat | 0 | 1 | partial | 2026-09-13T08:05:55Z | 1 | 0 | [Run 0150](#run-0150-ms) |
| 150 | MA | Morocco | 43 | 1 | partial | 2026-09-13T09:05:25Z | 10 | 0 | [Run 0151](#run-0151-ma) |
| 151 | MZ | Mozambique | 5 | 1 | partial | 2026-09-13T10:05:55Z | 6 | 0 | [Run 0152](#run-0152-mz) |
| 152 | MM | Myanmar | 4 | 1 | partial | 2026-09-13T11:05:26Z | 4 | 0 | [Run 0153](#run-0153-mm) |
| 153 | NA | Namibia | 12 | 1 | partial | 2026-09-13T12:06:56Z | 10 | 0 | [Run 0154](#run-0154-na) |
| 154 | NR | Nauru | 0 | 1 | partial | 2026-09-13T13:07:26Z | 1 | 0 | [Run 0155](#run-0155-nr) |
| 155 | NP | Nepal | 19 | 1 | partial | 2026-09-13T14:07:26Z | 10 | 0 | [Run 0156](#run-0156-np) |
| 156 | NL | Netherlands | 799 | 1 | partial | 2026-09-13T15:07:27Z | 10 | 0 | [Run 0157](#run-0157-nl) |
| 157 | NC | New Caledonia | 6 | 1 | partial | 2026-09-13T16:08:57Z | 6 | 0 | [Run 0158](#run-0158-nc) |
| 158 | NZ | New Zealand | 118 | 1 | partial | 2026-09-13T17:09:27Z | 10 | 0 | [Run 0159](#run-0159-nz) |
| 159 | NI | Nicaragua | 18 | 1 | partial | 2026-09-13T18:09:57Z | 10 | 0 | [Run 0160](#run-0160-ni) |
| 160 | NE | Niger | 1 | 1 | partial | 2026-09-13T19:09:27Z | 1 | 0 | [Run 0161](#run-0161-ne) |
| 161 | NG | Nigeria | 55 | 1 | partial | 2026-09-13T20:10:28Z | 10 | 0 | [Run 0162](#run-0162-ng) |
| 162 | NU | Niue | 0 | 0 | pending | — | — | — | — |
| 163 | NF | Norfolk Island | 0 | 0 | pending | — | — | — | — |
| 164 | KP | North Korea | 3 | 0 | pending | — | — | — | — |
| 165 | MK | North Macedonia | 27 | 0 | pending | — | — | — | — |
| 166 | MP | Northern Mariana Islands | 0 | 0 | pending | — | — | — | — |
| 167 | NO | Norway | 102 | 0 | pending | — | — | — | — |
| 168 | OM | Oman | 2 | 0 | pending | — | — | — | — |
| 169 | PK | Pakistan | 40 | 0 | pending | — | — | — | — |
| 170 | PW | Palau | 1 | 0 | pending | — | — | — | — |
| 171 | PS | Palestine | 5 | 0 | pending | — | — | — | — |
| 172 | PA | Panama | 23 | 0 | pending | — | — | — | — |
| 173 | PG | Papua New Guinea | 0 | 0 | pending | — | — | — | — |
| 174 | PY | Paraguay | 22 | 0 | pending | — | — | — | — |
| 175 | PE | Peru | 190 | 0 | pending | — | — | — | — |
| 176 | PH | Philippines | 307 | 0 | pending | — | — | — | — |
| 177 | PN | Pitcairn Islands | 0 | 0 | pending | — | — | — | — |
| 178 | PL | Poland | 496 | 0 | pending | — | — | — | — |
| 179 | PT | Portugal | 172 | 0 | pending | — | — | — | — |
| 180 | PR | Puerto Rico | 32 | 0 | pending | — | — | — | — |
| 181 | QA | Qatar | 5 | 0 | pending | — | — | — | — |
| 182 | RE | Réunion | 30 | 0 | pending | — | — | — | — |
| 183 | RO | Romania | 586 | 0 | pending | — | — | — | — |
| 184 | RU | Russia | 1134 | 0 | pending | — | — | — | — |
| 185 | RW | Rwanda | 3 | 0 | pending | — | — | — | — |
| 186 | BL | Saint Barthélemy | 0 | 0 | pending | — | — | — | — |
| 187 | SH | Saint Helena, Ascension and Tristan da Cunha | 2 | 0 | pending | — | — | — | — |
| 188 | KN | Saint Kitts and Nevis | 0 | 0 | pending | — | — | — | — |
| 189 | LC | Saint Lucia | 8 | 0 | pending | — | — | — | — |
| 190 | MF | Saint Martin | 0 | 0 | pending | — | — | — | — |
| 191 | PM | Saint Pierre and Miquelon | 2 | 0 | pending | — | — | — | — |
| 192 | VC | Saint Vincent and the Grenadines | 11 | 0 | pending | — | — | — | — |
| 193 | WS | Samoa | 0 | 0 | pending | — | — | — | — |
| 194 | SM | San Marino | 1 | 0 | pending | — | — | — | — |
| 195 | ST | São Tomé and Príncipe | 0 | 0 | pending | — | — | — | — |
| 196 | SA | Saudi Arabia | 35 | 0 | pending | — | — | — | — |
| 197 | SN | Senegal | 27 | 0 | pending | — | — | — | — |
| 198 | RS | Serbia | 198 | 0 | pending | — | — | — | — |
| 199 | SC | Seychelles | 0 | 0 | pending | — | — | — | — |
| 200 | SL | Sierra Leone | 1 | 0 | pending | — | — | — | — |
| 201 | SG | Singapore | 31 | 0 | pending | — | — | — | — |
| 202 | SX | Sint Maarten | 1 | 0 | pending | — | — | — | — |
| 203 | SK | Slovakia | 71 | 0 | pending | — | — | — | — |
| 204 | SI | Slovenia | 53 | 0 | pending | — | — | — | — |
| 205 | SB | Solomon Islands | 0 | 0 | pending | — | — | — | — |
| 206 | SO | Somalia | 2 | 0 | pending | — | — | — | — |
| 207 | ZA | South Africa | 137 | 0 | pending | — | — | — | — |
| 208 | GS | South Georgia | 0 | 0 | pending | — | — | — | — |
| 209 | KR | South Korea | 9 | 0 | pending | — | — | — | — |
| 210 | SS | South Sudan | 2 | 0 | pending | — | — | — | — |
| 211 | ES | Spain | 834 | 0 | pending | — | — | — | — |
| 212 | LK | Sri Lanka | 39 | 0 | pending | — | — | — | — |
| 213 | SD | Sudan | 2 | 0 | pending | — | — | — | — |
| 214 | SR | Suriname | 5 | 0 | pending | — | — | — | — |
| 215 | SJ | Svalbard and Jan Mayen | 0 | 0 | pending | — | — | — | — |
| 216 | SE | Sweden | 150 | 0 | pending | — | — | — | — |
| 217 | CH | Switzerland | 383 | 0 | pending | — | — | — | — |
| 218 | SY | Syria | 18 | 0 | pending | — | — | — | — |
| 219 | TW | Taiwan | 36 | 0 | pending | — | — | — | — |
| 220 | TJ | Tajikistan | 0 | 0 | pending | — | — | — | — |
| 221 | TZ | Tanzania | 10 | 0 | pending | — | — | — | — |
| 222 | TH | Thailand | 39 | 0 | pending | — | — | — | — |
| 223 | TL | Timor-Leste | 0 | 0 | pending | — | — | — | — |
| 224 | TG | Togo | 3 | 0 | pending | — | — | — | — |
| 225 | TK | Tokelau | 0 | 0 | pending | — | — | — | — |
| 226 | TO | Tonga | 3 | 0 | pending | — | — | — | — |
| 227 | TT | Trinidad and Tobago | 17 | 0 | pending | — | — | — | — |
| 228 | TN | Tunisia | 31 | 0 | pending | — | — | — | — |
| 229 | TR | Türkiye | 367 | 0 | pending | — | — | — | — |
| 230 | TM | Turkmenistan | 1 | 0 | pending | — | — | — | — |
| 231 | TC | Turks and Caicos Islands | 0 | 0 | pending | — | — | — | — |
| 232 | TV | Tuvalu | 0 | 0 | pending | — | — | — | — |
| 233 | UG | Uganda | 94 | 0 | pending | — | — | — | — |
| 234 | UA | Ukraine | 172 | 0 | pending | — | — | — | — |
| 235 | AE | United Arab Emirates | 621 | 0 | pending | — | — | — | — |
| 236 | GB | United Kingdom | 1302 | 0 | pending | — | — | — | — |
| 237 | US | United States | 4595 | 0 | pending | — | — | — | — |
| 238 | UM | United States Minor Outlying Islands | 17 | 0 | pending | — | — | — | — |
| 239 | VI | United States Virgin Islands | 3 | 0 | pending | — | — | — | — |
| 240 | UY | Uruguay | 91 | 0 | pending | — | — | — | — |
| 241 | UZ | Uzbekistan | 3 | 0 | pending | — | — | — | — |
| 242 | VU | Vanuatu | 3 | 0 | pending | — | — | — | — |
| 243 | VA | Vatican City | 13 | 0 | pending | — | — | — | — |
| 244 | VE | Venezuela | 133 | 0 | pending | — | — | — | — |
| 245 | VN | Vietnam | 11 | 0 | pending | — | — | — | — |
| 246 | WF | Wallis and Futuna | 1 | 0 | pending | — | — | — | — |
| 247 | EH | Western Sahara | 0 | 0 | pending | — | — | — | — |
| 248 | YE | Yemen | 9 | 0 | pending | — | — | — | — |
| 249 | ZM | Zambia | 4 | 0 | pending | — | — | — | — |
| 250 | ZW | Zimbabwe | 3 | 0 | pending | — | — | — | — |

## Run-log format

Append a stable `<a id="run-NNNN-cc"></a>` anchor and `### Run NNNN — CC — Country` heading under Research results. Keep each run to **300 words of prose plus at most 10 concise candidate rows**. Include:

- Actual UTC start/end, sweep, status, query/page/probe counts, and actual query strings.
- Candidate name, official identity/country source link, stream URL or unknown, disposition/reason, and a link to the saved probe evidence. Classify as ready, already present, needs verification or excluded; counts must sum.
- Link `research/run-NNNN-CC-proposed.json` for schema-compatible ready records (`id`, `name`, `country`, `url`, `tags`, `languages`, `source`). Do not duplicate that JSON here.
- The next useful leads and categories still unsearched, with URLs; next scheduled country.
- Usage before/after, window reset timestamp and nonnegative percentage-point delta if comparable; otherwise unknown/reset. Label it account-wide and approximate.

## Research results

The first 20 country searches are preserved in the [historical archive](research/archive/runs-0001-0020.md). All checklist progress and evidence remain available. The next hourly run is Cambodia (`KH`), Run 0038.

<a id="run-0021-by"></a>
### Run 0021 — BY — Belarus — 2026-09-07T16:34:00Z

- Start/end: 2026-09-07T16:34:00Z–2026-09-07T16:38:02Z. Sweep 1. Final status: **partial**. Usage was 29% before and after (account-wide seven-day meter; no measurable percentage-point change; reset timestamp unchanged).
- Search scope: six queries in English, Belarusian and Russian; five source pages opened. Primary lead: [Radio Belarus](https://radiobelarus.by/). Directory discovery: [FreqTrail's Belarus list](https://www.freqtrail.com/stations/BY), which supplied candidate stream URLs and station names for follow-up.
- Evaluated 4 stream inputs; 0 ready, 1 already present, 3 needs verification because the bounded HTTPS probe could not resolve the host. Raw results: [inputs](research/run-0021-BY-inputs.json) and [probes](research/run-0021-BY-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL / resolved URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Belarus | Official station site identifies Belarus service | Belarusian, Russian, international news | [radiobelarus.by](https://radiobelarus.by/) | `https://media2.datacenter.by/stream/belarusru/stream` | DNS/address check failed | needs verification; retry on a later sweep |
| Radius FM | Directory identifies Belarus/Minsk | music | [FreqTrail](https://www.freqtrail.com/stations/BY) | `https://stream2.datacenter.by/radiusfm_main` | DNS/address check failed | needs verification; official identity page still needed |
| Русское радио Минск 98.9 FM | Directory identifies Minsk, Belarus | Russian, music | [FreqTrail](https://www.freqtrail.com/stations/BY) | `https://stream.rusradio.by:8443/live128` | already in catalog | already present |
| Новое радио | Directory identifies Belarus | pop/dance | [FreqTrail](https://www.freqtrail.com/stations/BY) | `https://live.novoeradio.by:444/live/novoeradio` | DNS/address check failed | needs verification; retry on a later sweep |

Remaining leads: official pages for Radius FM and Новое радио, plus Belarus regional stations listed by FreqTrail. The run stopped at the four-minute ceiling; it did not claim an exhaustive Belarus search. Next scheduled country: Belgium (`BE`).

<a id="run-0022-be"></a>
### Run 0022 — BE — Belgium — 2026-09-07T17:35:00Z

- Start/end: 2026-09-07T17:35:00Z–2026-09-07T17:39:33Z. Sweep 1. Final status: **partial**. Usage was 29% before and after (account-wide seven-day meter; no measurable percentage-point change; reset timestamp unchanged).
- Search scope: six queries in English, Dutch, French and German; five source pages opened. Primary sources: [RTBF stream links](https://support.rtbf.be/hc/fr-fr/articles/16393535008401-Liens-URL-des-cha%C3%AEnes-radio-et-webradios), [VRT streaming links](https://www.vrt.be/nl/ons-aanbod/streamingslinks-radio), and [Radio Mol](https://www.gemeentemol.be/radiomol). Community/university leads included [Radio Campus](https://www.radiocampus.be/) and Radio Sud.
- Evaluated 4 stream inputs; 0 ready, 1 already present, 3 needs verification because the bounded HTTPS probe could not resolve the host. Raw results: [inputs](research/run-0022-BE-inputs.json) and [probes](research/run-0022-BE-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL / resolved URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Classic 21 | RTBF's Belgian public radio service | French, rock/classic | [RTBF](https://support.rtbf.be/hc/fr-fr/articles/16393535008401-Liens-URL-des-cha%C3%AEnes-radio-et-webradios) | `https://radio.rtbf.be/c21/mp3-160/me` | DNS/address check failed | needs verification; retry later |
| VivaCité Bruxelles | RTBF regional Belgian service | French, regional/news | [RTBF](https://support.rtbf.be/hc/fr-fr/articles/16393535008401-Liens-URL-des-cha%C3%AEnes-radio-et-webradios) | `https://radio.rtbf.be/viva-bxl/mp3-160/me` | DNS/address check failed | needs verification; retry later |
| VRT Radio 1 | VRT Flemish public broadcaster | Dutch, news/culture | [VRT](https://www.vrt.be/nl/ons-aanbod/streamingslinks-radio) | `https://mp3.streampower.be/radio1-low.mp3` | DNS/address check failed | needs verification; retry later |
| BRF1 | German-speaking Belgian public service | German, general | [BRF](https://www.brf.be/) | `https://streaming.brf.be/brf1-high.mp3` | already in catalog | already present |

Remaining leads: Radio Mol, Radio Campus, Radio Sud, Radio Utopia, local Flemish streams, and official BRF/RTBF/VRT variants. The run stopped at the four-minute ceiling; it did not claim an exhaustive Belgium search. Next scheduled country: Belize (`BZ`).

<a id="run-0023-bz"></a>
### Run 0023 — BZ — Belize — 2026-09-07T18:35:00Z

- Start/end: 2026-09-07T18:35:00Z–2026-09-07T18:39:33Z. Sweep 1. Final status: **partial**. Usage was 29% before and after (account-wide seven-day meter; no measurable percentage-point change; reset timestamp unchanged).
- Search scope: six queries in English and Spanish; four source pages opened. Primary leads: [Estereo Amor](https://estereoamor.com/), [More FM](https://morefm.bz/more-fm-watch-our-live-stream-about-more-fm/), [Horizon Radio](https://www.horizonradio.bz/), and [Love FM](https://lovefm.com/91/). Estereo Amor documents Spanish-language national FM service and Belize City location; Horizon documents Belize coverage, frequencies, languages and online listening.
- Evaluated 4 stream inputs; 0 ready, 4 needs verification because the bounded HTTPS probe could not resolve the selected endpoints. Raw results: [inputs](research/run-0023-BZ-inputs.json) and [probes](research/run-0023-BZ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL / resolved URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Estereo Amor | Belize City; national frequencies listed | Spanish, news/music | [Estereo Amor](https://estereoamor.com/) | online player endpoint not exposed in page text | not tested | needs verification; locate stable HTTPS audio URL |
| More FM | Belize; 99.5 and 107.1 FM | English, youth/music | [More FM](https://morefm.bz/more-fm-watch-our-live-stream-about-more-fm/) | embedded player only | not tested | needs verification; player iframe requires follow-up |
| KREM Radio | Belize City; official broadcaster registry lead | English, news/pop/talk | [Belize Broadcasting Authority](https://belizebroadcastingauthority.org/index.php/broadcasters/) | `http://159.65.32.199:8016/stream` | unsafe/insecure endpoint rejected | needs verification; find HTTPS primary stream |
| Horizon Radio | Spanish Lookout and Mountain Pine Ridge; 97.3/103.5 FM | English, Spanish, German dialects; Christian | [Horizon Radio](https://www.horizonradio.bz/) | `https://horizonradio.bz/stream` | DNS/address check failed | needs verification; resolve official listen link later |

Remaining leads: Love FM, Wave Radio, Positive Vibes, Integrity Radio, Hitz 100/Oye FM, and local/regional stations. The run stopped at the four-minute ceiling; it did not claim an exhaustive Belize search. Next scheduled country: Benin (`BJ`).

<a id="run-0024-bj"></a>
### Run 0024 — BJ — Benin — 2026-09-07T19:35:00Z

- Start/end: 2026-09-07T19:35:00Z–2026-09-07T19:40:33Z. Sweep 1. Final status: **partial**. Usage was 29% before and after (account-wide seven-day meter; no measurable percentage-point change; reset timestamp unchanged).
- Search scope: six queries in French and English; four source pages opened. Primary sources: [SRTB](https://srtb.bj/a-propos/), the [HAAC legal radio directory](https://www.haac.bj/storage/uploads/repertoire_radio.pdf), and [FeRCAB's community-radio network](https://fercab.org/). These identify national, regional and community services, including 56 FeRCAB member stations.
- Evaluated 3 stream inputs; 0 ready, 3 already present. Raw results: [inputs](research/run-0024-BJ-inputs.json) and [probes](research/run-0024-BJ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Cotonou 94.3 | Existing catalog assignment to Benin | local radio | [SRTB/HAAC leads](https://srtb.bj/a-propos/) | `https://stream.zeno.fm/o9bspgm4y78vv` | already in catalog | already present |
| ORTB Radio Bénin | SRTB national public broadcaster | French and national languages | [SRTB](https://srtb.bj/a-propos/) | `https://listen.radioking.com/radio/47608/stream/84430` | already in catalog | already present |
| ORTB Radio Parakou | SRTB regional station; Parakou | regional/national languages | [SRTB](https://srtb.bj/radio-benin-70-ans-histoire-jubilee-platine/) | `https://listen.radioking.com/radio/51919/stream/88927` | already in catalog | already present |

Remaining leads: FeRCAB's 56 member stations, Radio Tonignon, Betsaleel FM, Peace FM and the HAAC directory's regional/community entries. The run stopped at the four-minute ceiling; it did not claim an exhaustive Benin search. Next scheduled country: Bermuda (`BM`).

<a id="run-0025-bm"></a>
### Run 0025 — BM — Bermuda — 2026-09-07T22:14:00Z

- Start/end: 2026-09-07T22:14:00Z–2026-09-07T22:18:50Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English; five source pages opened. Primary evidence came from [Bermuda Broadcasting](https://bbc.bm/power-95), [Magic 102.7](https://magic1027bermuda.com/), and [Bermuda Broadcasting's Ocean 89 page](https://bbc.bm/ocean-89). Directory discovery used [FreqTrail](https://www.freqtrail.com/stations/BM).
- Evaluated 4 stream inputs; 0 ready, 1 already present, 3 need verification. Raw results: [inputs](research/run-0025-BM-inputs.json) and [probes](research/run-0025-BM-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Dr. Dick’s Dub Shack | Hamilton, Bermuda in directory | dub/roots reggae | [FreqTrail](https://www.freqtrail.com/stations/BM) | `https://streamer.radio.co/s0635c8b0d/listen` | already in catalog | already present |
| Magic 102.7 FM | Hamilton, Bermuda; local station site | adult contemporary/talk | [Magic 102.7](https://magic1027bermuda.com/) | `https://stream.magic1027bermuda.com/live` | DNS/address check failed | needs verification |
| Power 95 | Bermuda Broadcasting page; local programming | hip-hop/R&B/soca | [Bermuda Broadcasting](https://bbc.bm/power-95) | endpoint not exposed in page text | not tested | needs verification |
| Ocean 89 | Bermuda Broadcasting page; local programming | music/talk | [Bermuda Broadcasting](https://bbc.bm/ocean-89) | endpoint not exposed in page text | not tested | needs verification |

Remaining leads: Bermuda Broadcasting iframe URLs, Inspire 105, Bermuda College Radio, VIBE 103, HOTT 107.5, and the government emergency 100.1 FM stream. The run stopped at the four-minute ceiling; it did not claim an exhaustive Bermuda search. Next scheduled country: Bhutan (`BT`).

<a id="run-0026-bt"></a>
### Run 0026 — BT — Bhutan — 2026-09-07T23:14:00Z

- Start/end: 2026-09-07T23:14:00Z–2026-09-07T23:18:20Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Dzongkha; one official page plus regulatory/community-radio references. [BBS radio streaming](https://www.bbs.bt/radio-streaming/) identifies the national broadcaster; [BICMA media services](https://www.bicma.gov.bt/?page_id=539) lists BBS and Lhop Community Radio; FeRCAB-style community discovery is deferred to the next sweep.
- Evaluated 1 stream input; 0 ready, 1 already present. Raw results: [inputs](research/run-0026-BT-inputs.json) and [probes](research/run-0026-BT-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| BBS Radio — Dzongkha | Bhutan Broadcasting Service national broadcaster | Dzongkha, news/culture | [BBS](https://www.bbs.bt/radio-streaming/) | `https://radio.bbs.bt/dz-ch` | already in catalog | already present |

Remaining leads: Lhop Community Radio and other community services listed by BICMA, plus BBS channels not yet represented in the catalog. The run stopped at the four-minute ceiling; it did not claim an exhaustive Bhutan search. Next scheduled country: Bolivia (`BO`).

<a id="run-0027-bo"></a>
### Run 0027 — BO — Bolivia — 2026-09-08T00:17:00Z

- Start/end: 2026-09-08T00:17:00Z–2026-09-08T00:21:50Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Spanish and English. Discovery sources included [radios.bolivia.bo](https://radios.bolivia.bo/), [Radio CEPRA](https://www.ceprabolivia.org/radio), [RTVU Oruro](https://rtvu.uto.edu.bo/en-vivo/) and the national regulator listing. Bolivia has substantial indigenous-language and community-radio coverage; follow-up is deferred.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0027-BO-inputs.json) and [probes](research/run-0027-BO-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Panamericana | Existing catalog assignment to Bolivia | news/music | [radios.bolivia.bo](https://radios.bolivia.bo/) | `https://stream.zeno.fm/pnwpbyfambruv` | already in catalog | already present |
| Radio Éxito (Bolivia) | Existing catalog assignment to Bolivia | news/music | [radios.bolivia.bo](https://radios.bolivia.bo/) | `https://cast6.my-control-panel.com/proxy/radiostr/;` | already in catalog | already present |
| Radio Disney — La Paz | Existing catalog assignment to Bolivia | pop | [radios.bolivia.bo](https://radios.bolivia.bo/) | `https://playerservices.streamtheworld.com/api/livestream-redirect/DISNEY_BOL_SCAAC.aac?dist=web-radiodisney` | already in catalog | already present |
| Radio Cumbia 90s | Existing catalog assignment to Bolivia | cumbia | [radios.bolivia.bo](https://radios.bolivia.bo/) | `https://emiteradio.com/proxy/cumbia90s?mp=/stream` | already in catalog | already present |

Remaining leads: CEPRA's Quechua and Aymara networks, Radio Universitaria, Radio Aclo, Radio Kawsachun Coca and regional stations from the regulator/listing sites. The run stopped at the four-minute ceiling; it did not claim an exhaustive Bolivia search. Next scheduled country: Bonaire, Sint Eustatius and Saba (`BQ`).

<a id="run-0028-ba"></a>
### Run 0028 — BA — Bosnia and Herzegovina — 2026-09-08T01:18:00Z

- Start/end: 2026-09-08T01:18:00Z–2026-09-08T01:22:21Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Bosnian/Croatian/Serbian and English. Discovery and primary leads included [BHRT](https://bhrt.ba/bht1/), [Radio Bosna](https://radiobosna.com/), and [Radio M](https://radiom.ba/); directories supplied further local-station leads.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0028-BA-inputs.json) and [probes](research/run-0028-BA-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Sehara | Existing catalog assignment to Bosnia and Herzegovina | folk/music | [Radio Bosnia directory](https://radiobosnia.com/) | `https://cast.name.ba:8000/;` | already in catalog | already present |
| Radio Busovača | Existing catalog assignment to Bosnia and Herzegovina | local radio | [Radio Bosnia directory](https://radiobosnia.com/) | `https://ec2s.crolive.com.hr:1510/stream` | already in catalog | already present |
| Esoterica Radio S2 | Existing catalog assignment to Bosnia and Herzegovina | electronic | [Radio Bosnia directory](https://radiobosnia.com/) | `https://esoterica.servemp3.com:444/listen/darkbasshouse_cyberpunk_hybridtrap/radio.mp3` | already in catalog | already present |
| Esoterica Radio S3 | Existing catalog assignment to Bosnia and Herzegovina | electronic | [Radio Bosnia directory](https://radiobosnia.com/) | `https://esoterica.servemp3.com:444/listen/darkclubbing_darkelectro/radio.mp3` | already in catalog | already present |

Remaining leads: BHRT Radio 1, Radio Sarajevo, Radio M, university/local stations, and the local-station directory's unresolved entries. The run stopped at the four-minute ceiling; it did not claim an exhaustive Bosnia and Herzegovina search. Next scheduled country: Bonaire, Sint Eustatius and Saba (`BQ`).

<a id="run-0031-br"></a>
### Run 0031 — BR — Brazil — 2026-09-08T04:22:00Z

- Start/end: 2026-09-08T04:22:00Z–2026-09-08T04:26:21Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Portuguese and English. Primary discovery included [Brazil's public radios](https://www.gov.br/pt-br/categorias/comunicacoes-e-transparencia-publica/comunicacao-publica/radios-e-tvs-publicas), [EBC Rádio Nacional](https://radionacional.ebc.com.br/sobre), [Radio CEPRA Comunitária](https://www.culturacomunitaria.com.br/) and indigenous-radio leads. Brazil has a very large existing catalog and community-radio landscape; this was a bounded pass.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0031-BR-inputs.json) and [probes](research/run-0031-BR-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Bossa Jazz Brasil | Existing catalog assignment to Brazil | jazz | [Public-radio discovery](https://www.gov.br/pt-br/categorias/comunicacoes-e-transparencia-publica/comunicacao-publica/radios-e-tvs-publicas) | `https://centova5.transmissaodigital.com:20104/live` | already in catalog | already present |
| Alpha FM São Paulo | Existing catalog assignment to Brazil | adult contemporary | [Brazil radio discovery](https://radios.ebc.com.br/) | `https://playerservices.streamtheworld.com/api/livestream-redirect/RADIO_ALPHAFM_ADP.aac` | already in catalog | already present |
| Rádio Antena 1 | Existing catalog assignment to Brazil | pop | [Brazil radio discovery](https://radios.ebc.com.br/) | `https://antenaone.crossradio.com.br/stream/1;` | already in catalog | already present |
| Rádio Mix São Paulo | Existing catalog assignment to Brazil | pop | [Brazil radio discovery](https://radios.ebc.com.br/) | `https://playerservices.streamtheworld.com/api/livestream-redirect/MIXFM_SAOPAULOAAC.aac` | already in catalog | already present |

Remaining leads: EBC public networks, Radio Nacional dos Povos, Yandê indigenous radio, university stations and community services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Brazil search. Next scheduled country: British Indian Ocean Territory (`IO`).

<a id="run-0032-io"></a>
### Run 0032 — IO — British Indian Ocean Territory — 2026-09-08T05:23:00Z

- Start/end: 2026-09-08T05:23:00Z–2026-09-08T05:27:52Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Spanish. Results identified military FM services (AFN/BFBS) and maritime/ham radio, but no public primary-source online stream beyond stations already attributed in the catalog. [GOV.UK](https://www.gov.uk/foreign-travel-advice/british-indian-ocean-territory/getting-help) confirms radio communications in Diego Garcia; [BFBS](https://www.bfbs.com/radio) provides general network streaming but no territory-specific endpoint.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0032-IO-inputs.json) and [probes](research/run-0032-IO-probes.json).

| Station / service | Location / country evidence | Language / genre | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- |
| Tick Tock Radio — 1993 | Existing catalog attribution to IO | oldies | `https://streaming.ticktock.radio/tt/1993/icecast.audio` | already in catalog | already present |
| Tick Tock Radio — 1992 | Existing catalog attribution to IO | oldies | `https://streaming.ticktock.radio/tt/1992/icecast.audio` | already in catalog | already present |
| Tick Tock Radio — 1994 | Existing catalog attribution to IO | oldies | `https://streaming.ticktock.radio/tt/1994/icecast.audio` | already in catalog | already present |
| Bollywood Radio | Existing catalog attribution to IO | Bollywood | `https://stream.zeno.fm/t961q1d0vp6vv` | already in catalog | already present |

Remaining leads: territory-specific AFN/BFBS relays if a public stream becomes available. The run stopped at the four-minute ceiling; it did not claim an exhaustive IO search. Next scheduled country: British Virgin Islands (`VG`).

<a id="run-0033-vg"></a>
### Run 0033 — VG — British Virgin Islands — 2026-09-08T06:23:00Z

- Start/end: 2026-09-08T06:23:00Z–2026-09-08T06:27:22Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. Primary leads included [ZBVI](https://www.zbvilivetower.com/), [CBN Radio 90.9](https://www.cbnvirginislands.com/css909fm), and directory evidence listing ZBVI, Isle 95, ZVCR and other local services.
- Evaluated 4 homepage/listen endpoints; 0 ready and 4 need verification because the bounded HTTPS probe could not resolve them. Raw results: [inputs](research/run-0033-VG-inputs.json) and [probes](research/run-0033-VG-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| ZBVI 780 | Road Town; principal commercial AM station | Caribbean/news/variety | [ZBVI](https://www.zbvilivetower.com/) | `https://www.zbvilivetower.com/` | DNS/address check failed | needs verification |
| CBN Radio 90.9 | BVI market covered by Caribbean Broadcast Network | Caribbean/news/sports | [CBN Virgin Islands](https://www.cbnvirginislands.com/css909fm) | `https://www.cbnvirginislands.com/css909fm` | DNS/address check failed | needs verification |
| Isle 95 | BVI station lead from directory evidence | island music | [directory lead](https://www.seakinglibrary.com/uploads/2/5/0/5/25052505/british_virging_islands.pdf) | `https://www.isle95.com/` | DNS/address check failed | needs verification |
| ZVCR 106.9 FM | BVI station lead from directory evidence | island music | [directory lead](https://www.seakinglibrary.com/uploads/2/5/0/5/25052505/british_virging_islands.pdf) | `https://www.zvcr1069fm.com/` | DNS/address check failed | needs verification |

Remaining leads: direct iframe/audio URLs for ZBVI and CBN, plus ZJoyVI, Soggy Dollar Radio, Tola Radio VI and Kool FM. The run stopped at the four-minute ceiling; it did not claim an exhaustive British Virgin Islands search. Next scheduled country: Brunei (`BN`).

<a id="run-0034-bn"></a>
### Run 0034 — BN — Brunei — 2026-09-08T07:23:00Z

- Start/end: 2026-09-08T07:23:00Z–2026-09-08T07:27:52Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Malay. Primary sources: [RTB Radio](https://www.rtb.gov.bn/radio/), [RTBGo](https://www.rtbgo.bn/live), and [RTB Nasional FM](https://www.rtb.gov.bn/nasional-fm/). RTB documents five public radio networks; UBD FM and BFBS Brunei were recorded as follow-up leads.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0034-BN-inputs.json) and [probes](research/run-0034-BN-probes.json).

| Station / service | Location / country evidence | Language / genre | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- |
| Asyil FM | Existing catalog assignment to Brunei | Malay/music | `https://playerservices.streamtheworld.com/api/livestream-redirect/ASYIK_FMAAC_SC` | already in catalog | already present |
| Rádio Água Azul | Existing catalog assignment to Brunei | music | `https://stm4.srvif.com:8460/stream` | already in catalog | already present |
| Kristal FM | Brunei private radio network | Malay/English | `https://play.thestreamtech.com:7038/` | already in catalog | already present |
| KRISTALfm | Duplicate web presentation of Kristal FM | Malay/English | `https://play.thestreamtech.com:7038/index.html` | already in catalog | already present |

Remaining leads: RTB Nasional, Pilihan, Pelangi, Harmoni and Nur Islam FM direct endpoints; UBD FM; and BFBS Brunei. The run stopped at the four-minute ceiling; it did not claim an exhaustive Brunei search. Next scheduled country: Bulgaria (`BG`).

<a id="run-0035-bg"></a>
### Run 0035 — BG — Bulgaria — 2026-09-08T08:24:00Z

- Start/end: 2026-09-08T08:24:00Z–2026-09-08T08:28:22Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Bulgarian and English. Primary lead: [Bulgarian National Radio](https://www.bnr.bg/). Discovery sources included Bulgarian radio directories and the Council for Electronic Media registry. Existing catalog coverage is broad; this pass focused on public and community leads.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0035-BG-inputs.json) and [probes](research/run-0035-BG-probes.json).

| Station / service | Location / country evidence | Language / genre | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- |
| Energy NRJ Bulgaria | Existing catalog assignment to Bulgaria | pop | `https://play.global.audio/nrj128` | already in catalog | already present |
| City HipHop R&B | Existing catalog assignment to Bulgaria | hip-hop/R&B | `https://play.global.audio/cityrabhi.aac` | already in catalog | already present |
| Extreme Deep House Radio | Existing catalog assignment to Bulgaria | electronic | `https://whsh4u-panel.com/proxy/yfryujzw/stream` | already in catalog | already present |
| Energy NRJ Bulgaria 90s Only | Existing catalog assignment to Bulgaria | 1990s pop | `https://play.global.audio/energy-90s` | already in catalog | already present |

Remaining leads: BNR regional services, Radio Bulgaria public streams, Alma Mater university radio, and community stations in the electronic-media registry. The run stopped at the four-minute ceiling; it did not claim an exhaustive Bulgaria search. Next scheduled country: Burkina Faso (`BF`).

<a id="run-0036-bf"></a>
### Run 0036 — BF — Burkina Faso — 2026-09-08T09:26:00Z

- Start/end: 2026-09-08T09:26:00Z–2026-09-08T09:30:22Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. Primary lead: [RTB Radio](https://rtb.bf/radio). Regulatory and community leads included [ARCEP frequency planning](https://demo.arcep.bf/plan-national-dattribution-des-frequences-pnaf/), CSC listings and Radio Palabre.
- Evaluated 4 stream inputs; 0 ready, 4 already present. Raw results: [inputs](research/run-0036-BF-inputs.json) and [probes](research/run-0036-BF-probes.json).

| Station / service | Location / country evidence | Language / genre | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- |
| Radio Balafon 102.7 | Bobo-Dioulasso; existing catalog attribution | local/music | `https://stream.zeno.fm/v3ddfda0cf9uv` | already in catalog | already present |
| Horizon FM 104.4 | Ouagadougou; existing catalog attribution | news/music | `https://stream.zeno.fm/0945crn4bf9uv` | already in catalog | already present |
| Radio Bizi Inter | Existing catalog attribution to Burkina Faso | community/news | `https://sonic.mediacp.eu/8040/;` | already in catalog | already present |
| Horizon FM Koudougou | Koudougou; existing catalog attribution | news/music | `https://stream.zeno.fm/s2ypmeg0cf9uv` | already in catalog | already present |

Remaining leads: RTB regional channels, Radio Palabre, Radio La Voix du Paysan, Radio Kawral, Ouaga FM, Savane FM, Radio Omega and stations broadcasting in national languages. The run stopped at the four-minute ceiling; it did not claim an exhaustive Burkina Faso search. Next scheduled country: Burundi (`BI`).

<a id="run-0037-bi"></a>
### Run 0037 — BI — Burundi — 2026-09-08T10:27:00Z

- Start/end: 2026-09-08T10:27:00Z–2026-09-08T10:31:23Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French, Kirundi and English. Regulatory source [ARCT](https://arct.gov.bi/) lists more than 40 FM services; primary leads included [RTNB](https://rtnb.bi/), [Bonesha FM](https://boneshafm.bi/), [Kazoza FM](https://www.kazozafm.com/) and Radio Télévision Térimbère.
- Evaluated 4 homepage/listen endpoints; 0 ready and 4 need verification because the bounded HTTPS probe could not resolve them. Raw results: [inputs](research/run-0037-BI-inputs.json) and [probes](research/run-0037-BI-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| RTNB | National Burundi broadcaster; Bujumbura | Kirundi/French/Swahili/news | [RTNB](https://rtnb.bi/) | `https://rtnb.bi/` | DNS/address check failed | needs verification |
| Bonesha FM | Burundi station; Kirundi live page | news/community | [Bonesha FM](https://boneshafm.bi/) | `https://boneshafm.bi/` | DNS/address check failed | needs verification |
| Kazoza FM | Bujumbura; economic/news programming | Kirundi/French | [Kazoza FM](https://www.kazozafm.com/) | `https://www.kazozafm.com/` | DNS/address check failed | needs verification |
| Radio Térimbère | Community-development station in Burundi | community/development | [Radio Térimbère](https://www.radio-tv-terimbere.com/) | `https://www.radio-tv-terimbere.com/` | DNS/address check failed | needs verification |

Remaining leads: direct audio endpoints for the ARCT-listed services, Radio Isanganiro, Radio Maria Burundi, RPA/Rondera FM and regional stations. The run stopped at the four-minute ceiling; it did not claim an exhaustive Burundi search. Next scheduled country: Cambodia (`KH`).

<a id="run-0038-kh"></a>
### Run 0038 — KH — Cambodia — 2026-09-08T11:28:00Z

- Start/end: 2026-09-08T11:28:00Z–2026-09-08T11:32:53Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Khmer-oriented terms. Primary or identity sources included [FEBCambodia](https://www.febcambodia.org/), [VOKK](https://vokk.net/) via its station page, and [Cambodia Community Radio](https://linktr.ee/cambodiacommunityradio). FEBC describes Phnom Penh-based Khmer FM and shortwave broadcasting and identifies Family FM 99.5 and Voice of Love; VOKK is identified as Khmer community radio in Phnom Penh.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0038-KH-inputs.json) and [probes](research/run-0038-KH-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Family FM 99.5 (Witthyu Krousar) | FEBCambodia; Phnom Penh / Cambodia | Khmer Christian radio | [FEBCambodia](https://www.febcambodia.org/) | `https://s14.myradiostream.com/10064/;.mp3` | already in catalog | existing catalog entry |
| Pop Radio 21 | Cambodia catalog entry | pop/music | [OnlineRadioBox lead](https://onlineradiobox.com/kh/) | `https://listen.radioking.com/radio/318317/stream/365846` | already in catalog | existing catalog entry |
| Sangkem Radio | Cambodia catalog entry | Khmer music/community | [Sangkem](https://live.sangkemtv.com/) | `https://live.sangkemtv.com/radio.mp3` | already in catalog | existing catalog entry |
| LDP Radio | Cambodia catalog entry | Khmer programming | [LDP](https://ldp-radio.com/) | `https://streaming.radio.co/sd48fd711d/listen` | already in catalog | existing catalog entry |

Remaining leads: FEBC's Voice of Love, VOKK, RNK National Radio of Kampuchea, Radio Love FM 97.5, Radio Samleng Khemara, Vayo FM and Cambodia Community Radio; direct HTTPS audio endpoints and ownership evidence need later verification. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cambodia search. Next scheduled country: Cameroon (`CM`).

<a id="run-0039-cm"></a>
### Run 0039 — CM — Cameroon — 2026-09-08T12:29:00Z

- Start/end: 2026-09-08T12:29:00Z–2026-09-08T12:33:23Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and French. Primary sources included [CRTV Radio](https://crtv.cm/tv/radio), which lists Poste National, Suellaba FM, CRTV237 Webradio and Mount Cameroon FM, plus [Radio Maria Cameroon](https://www.radiomaria.cm/) and [Ocean City Radio](https://ocrfm.online/) in Limbe.
- Evaluated 4 candidate inputs; the existing Mmuock stream is already cataloged and the three homepage probes were not usable audio endpoints. No new ready candidates were added. Raw results: [inputs](research/run-0039-CM-inputs.json) and [probes](research/run-0039-CM-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Mmuock Community Radio | Cameroon community station | community programming | [Mmuock](https://mmuock.org/) | `https://a7.asurahosting.com/listen/mmuock_community_radio_/radio.mp3` | already in catalog | existing catalog entry |
| CRTV radio channels | Yaoundé; Cameroon public broadcaster | national/regional news and general programming | [CRTV Radio](https://crtv.cm/tv/radio) | `https://crtv.cm/tv/radio` | not an audio endpoint | needs direct stream extraction |
| Radio Maria Cameroon | Cameroon Catholic radio | religious/programming in French and local languages | [Radio Maria Cameroon](https://www.radiomaria.cm/) | `https://www.radiomaria.cm/` | not an audio endpoint | needs direct stream extraction |
| Ocean City Radio | Limbe, Cameroon; FM 88.5 | faith, music and sports | [Ocean City Radio](https://ocrfm.online/) | `https://ocrfm.online/` | not an audio endpoint | needs direct stream extraction |

Remaining leads: CRTV Poste National, Suellaba FM, CRTV237 Webradio, Mount Cameroon FM, Radio Balafon, Balafon+, Radio Équinoxe, Radio Tamtam and direct Radio Maria/Ocean City audio URLs. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cameroon search. Next scheduled country: Canada (`CA`).

<a id="run-0040-ca"></a>
### Run 0040 — CA — Canada — 2026-09-08T13:29:00Z

- Start/end: 2026-09-08T13:29:00Z–2026-09-08T13:33:53Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and French. Primary evidence included [CBC Listen](https://solutionsmedia.cbcrc.ca/en/platforms/cbc-listen), which describes CBC Radio One and CBC Music services nationwide, and Radio-Canada's assistance page explaining that direct ICI stream URLs are no longer publicly posted and are provided on request.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0040-CA-inputs.json) and [probes](research/run-0040-CA-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| 101.9 ROCK | Canadian commercial station | rock | [Rogers stream](https://rogers-hls.leanstream.co/) | `https://rogers-hls.leanstream.co/rogers/nor1019.stream/icy?environment=tunein&args=tunein_01` | already in catalog | existing catalog entry |
| CJAD 800 | Montréal, Québec | news/talk | [CJAD](https://www.cjad.com/) | `https://14023.live.streamtheworld.com/CJADAM_SC` | already in catalog | existing catalog entry |
| CBC Radio One Ottawa | Ottawa, Ontario; CBC public broadcaster | English news/talk | [CBC Listen](https://solutionsmedia.cbcrc.ca/en/platforms/cbc-listen) | `https://26733.live.streamtheworld.com/CBOFM_CBC_SC` | already in catalog | existing catalog entry |
| ICI Première Montréal | Montréal, Québec; Radio-Canada | French general programming | [Radio-Canada assistance](https://assistance.radio-canada.ca/hc/fr/articles/15935829984276-O%C3%B9-puis-je-trouver-les-adresses-URL-de-ICI-Premi%C3%A8re-et-ICI-Musique) | `https://playerservices.streamtheworld.com/api/livestream-redirect/CBFFM_SRC.mp3` | already in catalog | existing catalog entry |

Remaining leads: CBC's other regional services, CBC Music, ICI Musique, campus/community stations, Indigenous broadcasters and the CRTC/NCRA station lists; prioritize new direct streams that are not already represented in the large Canadian catalog. The run stopped at the four-minute ceiling; it did not claim an exhaustive Canada search. Next scheduled country: Cape Verde (`CV`).

<a id="run-0041-cv"></a>
### Run 0041 — CV — Cape Verde — 2026-09-08T14:30:00Z

- Start/end: 2026-09-08T14:30:00Z–2026-09-08T14:34:54Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Portuguese and English. Primary evidence included the [Radio Educativa government service](https://radioeducativa.gov.cv/) with online broadcast, [RTC's RCV page](https://www.rtc.cv/rcv), and the [ARC media report](https://www.arc.cv/arc/upload/relatorio/relatorio_686bacfbc84581.4851416155.pdf), which lists national, regional and community radio services.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0041-CV-inputs.json) and [probes](research/run-0041-CV-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| RCV+ Rádio Cabo Verde Jovem | Praia; national youth service | Portuguese/Cape Verdean music | [ARC report](https://www.arc.cv/arc/upload/relatorio/relatorio_686bacfbc84581.4851416155.pdf) | `https://a8.my-control-panel.com:8670/radio.mp3` | already in catalog | existing catalog entry |
| RCV Rádio de Cabo Verde | Praia; national broadcaster | Portuguese/Cape Verdean general programming | [RTC RCV](https://www.rtc.cv/rcv) | `https://a3.asurahosting.com/listen/rcv/radio.mp3` | already in catalog | existing catalog entry |
| RTE – Rádio Educativa | Praia; Ministry of Education service | educational/public | [Radio Educativa](https://radioeducativa.gov.cv/) | `https://a13.my-control-panel.com/listen/rte/radio.mp3` | already in catalog | existing catalog entry |
| Rádio Atlântico | Cabo Verde online service | music, culture and news | [Radio Atlântico](https://radioatlantico.cv/sobre-nos/) | `https://stream.cvhosting.uk/listen/radio_atlantico/radio.mp3` | already in catalog | existing catalog entry |

Remaining leads: Radio Voz di Ponta d’Água, Voz di Bubista, Voz di Djabraba, Voz di Djarmai, Voz di Santa Cruz, Rádio DIA, Radio Cidade, Radio Alfa and other ARC-listed community services; seek direct endpoints and confirm island coverage. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cape Verde search. Next scheduled country: Caribbean Netherlands (`BQ`).

<a id="run-0042-bq"></a>
### Run 0042 — BQ — Caribbean Netherlands — 2026-09-08T15:31:00Z

- Start/end: 2026-09-08T15:31:00Z–2026-09-08T15:35:54Z. Sweep 1. Final status: **partial**.
- Search scope: six queries covering Bonaire, Sint Eustatius and Saba. Primary evidence included [Bon FM](https://bonfm.com/) on Bonaire, [Dolfijn's Bonaire service](https://dolfijngo.com/radio/), and [Empire Radio EUX](https://empireradioeux.com/) identifying an FM service in Oranjestad, St. Eustatius. Bon FM documents a Bonaire 102.7 FM station and Papiamentu programming.
- Evaluated 4 candidate inputs; three already exist in the catalog and one could not be resolved. No new ready candidates were added. Raw results: [inputs](research/run-0042-BQ-inputs.json) and [probes](research/run-0042-BQ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Alpha 93.1 FM Riscado | Bonaire service in project catalog | local music/general | [Bonaire station lead](https://bonfm.com/) | `https://kadushi.westream.cloud:8100/xstream` | already in catalog | existing catalog entry |
| Mega Hit FM | Bonaire listing | pop/hits | [Bonaire radio directory](https://radio.dubbeh.net/stations/mega-hit-fm-17217) | `https://megahitfm.krioyohosting.com:1012/stream` | already in catalog | existing catalog entry |
| TROPICAL SPICE RADIO | Caribbean Netherlands catalog service | tropical music | [Bonaire radio directory](https://www.radiotub.com/central_america/radios/Bonaire) | `https://auds1.intacs.com/tropicalspiceradio` | already in catalog | existing catalog entry |
| Solid FM 93.1 | Caribbean Netherlands catalog service | music | [Bonaire radio directory](https://www.radiotub.com/central_america/radios/Bonaire) | `https://caribspy.com/proxy/solidfm/stream/;?type=http&nocache=107036` | unresolved address | needs verification |

Remaining leads: Bon FM, Voz di Bonaire, Dolfijn FM Bonaire, Empire Radio EUX in Sint Eustatius, Radio Statia and any Saba community service; find direct HTTPS audio URLs and distinguish local island provenance from Curaçao or Netherlands relays. The run stopped at the four-minute ceiling; it did not claim an exhaustive Caribbean Netherlands search. Next scheduled country: Cayman Islands (`KY`).

<a id="run-0043-ky"></a>
### Run 0043 — KY — Cayman Islands — 2026-09-08T16:31:00Z

- Start/end: 2026-09-08T16:31:00Z–2026-09-08T16:35:24Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. Primary evidence included [Radio Cayman](https://www.radiocayman.gov.ky/schedule-radio-cayman-one), which documents government programming on Grand Cayman and the Sister Islands, [Breeze FM](https://www.radiocayman.gov.ky/breeze-fm), [Big Fish 95.5FM](https://bigfish955.ky/) and [Cayman Public Radio](https://www.caymanpublicradio.com/).
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0043-KY-inputs.json) and [probes](research/run-0043-KY-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Island FM - The Rhythm Of Cayman | Cayman Islands commercial service | reggae, soca and calypso | [Island FM lead](https://onlineradiobox.com/ky/irie/?lang=en) | `https://iriefm-hurleysmedia.radioca.st/stream?_=912521` | already in catalog | existing catalog entry |
| Z99 Grand Cayman | Grand Cayman; Compass Media service | popular music | [Compass Media](https://www.compassmedia.ky/) | `https://z99-hurleysmedia.radioca.st/stream` | already in catalog | existing catalog entry |
| X107.1 | Cayman Islands commercial service | music | [Cayman station list](https://en.wikipedia.org/wiki/List_of_radio_stations_in_the_Cayman_Islands) | `https://ice23.securenetsystems.net/X1071?playSessionID=C8803655-9BCC-E3A9-EB64CD924FCD83A6` | already in catalog | existing catalog entry |
| Rooster 101 | Cayman Islands country station | country/music | [Compass Media](https://www.compassmedia.ky/) | `https://rooster101-hurleysmedia.radioca.st/stream` | already in catalog | existing catalog entry |

Remaining leads: government Radio Cayman 89.9, Breeze FM, Big Fish 95.5, Cayman Public Radio, Star 92.7, CayRock, Gold 94.9, Hot 104.1, Kiss FM and Sister Islands services; locate direct audio endpoints and avoid duplicating the existing Compass catalog coverage. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cayman Islands search. Next scheduled country: Central African Republic (`CF`).

<a id="run-0044-cf"></a>
### Run 0044 — CF — Central African Republic — 2026-09-08T17:31:00Z

- Start/end: 2026-09-08T17:31:00Z–2026-09-08T17:35:24Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. Primary evidence included [Radio Ndeke Luka's diffusion page](https://www.radiondekeluka.org/diffusion), which documents a 24/7 100.9 FM network across Bangui and 12 other cities plus 20 community partners, and the UN [Radio Guira FM](https://minusca.unmissions.org/fr/radio-guira-fm-0) result describing MINUSCA coverage.
- Evaluated 4 candidate inputs; two already exist in the catalog and two source pages were not usable audio endpoints. No new ready candidates were added. Raw results: [inputs](research/run-0044-CF-inputs.json) and [probes](research/run-0044-CF-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Ndeke Luka | Bangui and 12 other CAR cities; 100.9 FM | news/current affairs | [Ndeke Luka](https://www.radiondekeluka.org/diffusion) | `https://stream.radiondekeluka.org/ndekeluka` | already in catalog | existing catalog entry |
| Mambokadzi DreamRadio | Central African Republic catalog service | music | catalog baseline | `https://cast3.asurahosting.com/proxy/dreamradio/stream.mp3` | already in catalog | existing catalog entry |
| Radio Guira FM | MINUSCA station covering Bangui and 13 localities | peacebuilding/news | [MINUSCA](https://minusca.unmissions.org/fr/radio-guira-fm-0) | `https://minusca.unmissions.org/fr/radio-guira-fm-0` | unresolved address | needs direct stream extraction |
| Radio Ndeke Luka web diffusion page | CAR broadcaster's online listening page | news/current affairs | [Ndeke Luka](https://www.radiondekeluka.org/diffusion) | `https://www.radiondekeluka.org/diffusion` | webpage, not audio endpoint | needs direct stream extraction |

Remaining leads: Guira FM direct audio, Radio Centrafrique, Radio Zereda in Obo, Hero Radio, Voice Radio, and Ndeke Luka's 20 partner community stations. The run stopped at the four-minute ceiling; it did not claim an exhaustive Central African Republic search. Next scheduled country: Chad (`TD`).

<a id="run-0045-td"></a>
### Run 0045 — TD — Chad — 2026-09-08T18:34:00Z

- Start/end: 2026-09-08T18:34:00Z–2026-09-08T18:38:24Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. Primary evidence included [Radio Ndarason International](https://ndarason.com/en/about-us/), which documents an N'Djamena headquarters, 107.1 FM and Kanembu/Kanuri programming, plus the ONAMA public media search result and Chad media directory leads.
- Evaluated 4 candidate inputs; the Radio Tchad stream already exists in the catalog and three institutional pages were not usable audio endpoints. No new ready candidates were added. Raw results: [inputs](research/run-0045-TD-inputs.json) and [probes](research/run-0045-TD-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Tchad | N'Djamena; public radio stream | French/Arabic/general | [ONAMA](https://www.onama.td/television-nationale/) | `https://strhls.streamakaci.tv/str_tchad_radio/str_tchad_radio/icecast.audio?fbclid=IwAR32Ir_eHaV-HSrh46OVT_VeTZt5KoNggoq8qzeSiAeZTJNBKKUtsSNUtcY` | already in catalog | existing catalog entry |
| Radio Ndarason International | N'Djamena and Lake Chad region; 107.1 FM | Kanembu/Kanuri, peacebuilding/news | [RNI](https://ndarason.com/en/about-us/) | `https://ndarason.com/en/about-us/` | not an audio endpoint | needs direct stream extraction |
| ONAMA / Télé Tchad radio | N'Djamena; national public media | French/Arabic | [ONAMA](https://www.onama.td/television-nationale/) | `https://www.onama.td/television-nationale/` | not an audio endpoint | needs direct stream extraction |
| Focus Média radio | Chad online news service | French and Chadian Arabic | [Focus Média](https://focusmedia-tchad.com/) | `https://focusmedia-tchad.com/` | unresolved address | needs verification |

Remaining leads: Radio Dja FM, NGATO FM, Radio ADMC, Radio Ndarason direct stream, FM Liberté, community stations in the Chad Community Radio Network and the public Radiodiffusion nationale tchadienne. The run stopped at the four-minute ceiling; it did not claim an exhaustive Chad search. Next scheduled country: Chile (`CL`).

<a id="run-0046-cl"></a>
### Run 0046 — CL — Chile — 2026-09-08T19:34:00Z

- Start/end: 2026-09-08T19:34:00Z–2026-09-08T19:38:55Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Spanish and English. Primary evidence included [Radio Cooperativa](https://www.cooperativa.cl/radioenvivo/), the Chile community radio directory [Radios Online](https://www.radiosonline.cl/genero/community/) and [Estaciones.cl](https://estaciones.cl/), which lists regional and community services.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0046-CL-inputs.json) and [probes](research/run-0046-CL-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| BioBio Chile | Chile network | Spanish news/talk | [BioBio directory lead](https://www.radiosonline.cl/genero/community/) | `https://unlimited3-cl.dps.live/biobiosantiago/aac/icecast.audio` | already in catalog | existing catalog entry |
| Pudahuel | Chile commercial service | Spanish pop/general | [Estaciones.cl](https://estaciones.cl/) | `https://26593.live.streamtheworld.com/PUDAHUEL_SC` | already in catalog | existing catalog entry |
| 100.9 Play FM | Chile FM service | music | [Estaciones.cl](https://estaciones.cl/) | `https://mdstrm.com/audio/5c8d6406f98fbf269f57c82c/icecast.audio` | already in catalog | existing catalog entry |
| Cooperativa | Santiago; national Chile broadcaster | Spanish news/sports/talk | [Radio Cooperativa](https://www.cooperativa.cl/radioenvivo/) | `https://unlimited3-cl.dps.live/cooperativafm/mp3/icecast.audio` | already in catalog | existing catalog entry |

Remaining leads: Radio Bomberos Chile, Radio Dinámica, Radio Puerta Norte, Radio Sol 108, Radio Sinaí, Radio Ríos de Agua Viva, regional community broadcasters and indigenous/community stations. The run stopped at the four-minute ceiling; it did not claim an exhaustive Chile search. Next scheduled country: China (`CN`).

<a id="run-0047-cn"></a>
### Run 0047 — CN — China — 2026-09-08T20:35:00Z

- Start/end: 2026-09-08T20:35:00Z–2026-09-08T20:39:25Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Chinese and English. Primary evidence included [云听 / radio.cn](https://www.radio.cn/pc-portal/erji/), a China Media Group audio platform with live radio categories, and [Radio5.cn](https://radio5.cn/), which exposes provincial and municipal streams. The catalog already has broad Chinese coverage.
- Evaluated 4 candidate stream inputs; three already exist in the catalog and one endpoint was unresolved. No new ready candidates were added. Raw results: [inputs](research/run-0047-CN-inputs.json) and [probes](research/run-0047-CN-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| CNR-1 中国之声 | China National Radio service | Mandarin news/general | [云听](https://www.radio.cn/pc-portal/erji/) | `https://lhttp.qtfm.cn/live/15318317/64k.mp3` | already in catalog | existing catalog entry |
| 上海新闻广播 | Shanghai municipal broadcaster | Mandarin news | [Radio5.cn](https://radio5.cn/) | `https://lhttp.qingting.fm/live/270/64k.mp3` | already in catalog | existing catalog entry |
| 广东珠江经济台 | Guangdong provincial broadcaster | Cantonese/Mandarin business/news | [Radio5.cn](https://radio5.cn/) | `https://lhttp.qtfm.cn/live/1259/64k.mp3` | already in catalog | existing catalog entry |
| 北京新闻广播 | Beijing municipal broadcaster | Mandarin news | [Radio5.cn](https://radio5.cn/) | `https://lhttp.qingting.fm/live/339/64k.mp3` | unresolved address | needs verification |

Remaining leads: China Radio International language services, CNR regional channels, provincial and municipal traffic/news/music stations, campus services, and Chinese-language diaspora stations; treat Hong Kong, Macao and Taiwan as separate project entries where applicable and avoid duplicate directory mirrors. The run stopped at the four-minute ceiling; it did not claim an exhaustive China search. Next scheduled country: Christmas Island (`CX`).

<a id="run-0048-cx"></a>
### Run 0048 — CX — Christmas Island — 2026-09-08T21:35:00Z

- Start/end: 2026-09-08T21:35:00Z–2026-09-08T21:39:55Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. Primary evidence included [6RCI](https://www.6rci.net/), the [Christmas Island tourism station page](https://christmasisland.squarespace.com/radio), and the Australian Government emergency plan, which confirms 6RCI as the volunteer community station on 102.1/105.3 FM with emergency broadcast duties and multilingual community coverage.
- Evaluated 4 candidate inputs; the existing catalog entry is unrelated to the local station, while 6RCI's direct Radio.co stream and pages could not be resolved by the bounded probe. No new ready candidates were added. Raw results: [inputs](research/run-0048-CX-inputs.json) and [probes](research/run-0048-CX-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| 6RCI Christmas Island Community Radio | Christmas Island, Indian Ocean; 102.1/105.3 FM | English, Chinese and Malay; community/emergency | [6RCI](https://www.6rci.net/) | `https://streams.radio.co/s254f35e58/listen` | unresolved address | strong candidate; needs verification |
| Navidad Grupera | Existing catalog service mapped to CX | grupera/music | catalog baseline | `https://radioforte.com/8006/stream` | already in catalog | existing catalog entry; provenance needs review |
| 6RCI station site | Christmas Island community station | community radio | [6RCI](https://www.6rci.net/) | `https://www.6rci.net/` | unresolved address | needs verification |
| 6RCI tourism page | Nursery Road, Christmas Island | community radio | [Christmas Island tourism](https://christmasisland.squarespace.com/radio) | `https://christmasisland.squarespace.com/radio` | unresolved address | needs verification |

Remaining leads: verify the Radio.co stream, review the existing Navidad Grupera country mapping, and distinguish Christmas Island's 6RCI from Australian ABC services rebroadcast to the territory. The run stopped at the four-minute ceiling; it did not claim an exhaustive Christmas Island search. Next scheduled country: Cocos (Keeling) Islands (`CC`).

<a id="run-0049-cc"></a>
### Run 0049 — CC — Cocos (Keeling) Islands — 2026-09-08T22:36:00Z

- Start/end: 2026-09-08T22:36:00Z–2026-09-08T22:40:25Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. Primary evidence from the Australian Government [territory information](https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/cocos-keeling-islands/travel-information) confirms volunteer community station 6CKI, Voice of the Cocos (Keeling) Islands, and rebroadcast ABC/FM services. [RadioStationWorld](https://radiostationworld.com/locations/cocos_keeling_islands/radio_stations/) lists 6CKI and regional repeaters.
- Evaluated 4 candidate inputs; no direct audio endpoint was verifiable and the unrelated CX catalog URL was detected as a prior mention. No new ready candidates were added. Raw results: [inputs](research/run-0049-CC-inputs.json) and [probes](research/run-0049-CC-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| 6CKI – Voice of the Cocos (Keeling) Islands | Cocos community volunteer station | local content/community | [Australian Government](https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/cocos-keeling-islands/travel-information) | `https://cbonline.org.au/index.cfm?pageId=13%2C8%2C6%2C3523` | unresolved address | strong candidate; needs verification |
| 6CKI repeater | West Island / Home Island community coverage | local community | [RadioStationWorld](https://radiostationworld.com/locations/cocos_keeling_islands/radio_stations/) | `https://radiostationworld.com/locations/cocos_keeling_islands/radio_stations/` | webpage, not audio endpoint | needs direct stream extraction |
| ABC Regional Radio | Cocos rebroadcast service | Australian news/talk | [Australian Government](https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/cocos-keeling-islands/travel-information) | `https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/cocos-keeling-islands/travel-information` | webpage, not audio endpoint | needs verification |
| LA OCHENTERA 91.9 FM | Existing catalog item mapped to CC | music | catalog baseline | `https://radioforte.com/8006/stream` | prior catalog/research mention | provenance needs review |

Remaining leads: locate a current 6CKI stream or cbonline player URL, verify the local frequency and language coverage, and separate Australian ABC/Red FM relays from locally originated services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cocos (Keeling) Islands search. Next scheduled country: Colombia (`CO`).

<a id="run-0050-co"></a>
### Run 0050 — CO — Colombia — 2026-09-08T23:36:00Z

- Start/end: 2026-09-08T23:36:00Z–2026-09-08T23:40:26Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Spanish and English. Primary evidence included [Caracol Radio](https://caracol.com.co/directorio/), [RCN Radio](https://www.rcnradio.com/), the Colombian community-radio directory at [Colombia.com](https://www.colombia.com/radio/emisoras-comunitarias-t2), and an RTVC public-radio presentation describing online services.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0050-CO-inputs.json) and [probes](research/run-0050-CO-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Caracol Radio Bogotá | Bogotá; national PRISA network | Spanish news/talk | [Caracol directory](https://caracol.com.co/directorio/) | `https://playerservices.streamtheworld.com/api/livestream-redirect/CARACOL_RADIOAAC.aac` | already in catalog | existing catalog entry |
| Olímpica Stereo Medellín | Medellín; national commercial network | Spanish music | [RCN/Colombia directory lead](https://www.emisorasdecolombia.com/) | `https://playerservices.streamtheworld.com/api/livestream-redirect/OLP_MEDELLINAAC.aac` | already in catalog | existing catalog entry |
| Blu Radio national | Bogotá and national transmitters | Spanish news/talk | [Blu/RCN directory lead](https://www.rcnradio.com/) | `https://23113.live.streamtheworld.com/BLURADIO_SC` | already in catalog | existing catalog entry |
| Radioacktiva Bogotá | Bogotá; PRISA network | Spanish rock/music | [Caracol directory](https://caracol.com.co/directorio/) | `https://playerservices.streamtheworld.com/api/livestream-redirect/RADIO_ACTIVAAAC.aac` | already in catalog | existing catalog entry |

Remaining leads: RTVC Radio Nacional and its regional/online services, indigenous and community stations listed by Colombia.com, university radio and local services across all departments. The run stopped at the four-minute ceiling; it did not claim an exhaustive Colombia search. Next scheduled country: Comoros (`KM`).

<a id="run-0051-km"></a>
### Run 0051 — KM — Comoros — 2026-09-09T00:36:00Z

- Start/end: 2026-09-09T00:36:00Z–2026-09-09T00:40:56Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. Primary or station sources included [Dounia Web](https://douniaweb.net/pages), a Comorian association radio broadcasting online since 2005, [Radio Kazi](https://radiokazi.fr/) at 107 MHz in Mkazi, and the ORTN/Radio Ngazidja live-radio lead.
- Evaluated 4 homepage/contact inputs; no direct audio endpoint was verifiable and no catalog baseline existed. No new ready candidates were added. Raw results: [inputs](research/run-0051-KM-inputs.json) and [probes](research/run-0051-KM-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Dounia Web | Comoros association radio; online since 2005 | Comorian/French; news, culture, music | [Dounia Web](https://douniaweb.net/pages) | `https://douniaweb.net/pages` | webpage, not audio endpoint | strong candidate; needs direct stream extraction |
| Radio Kazi | Mkazi, Comoros; 107 MHz | local news, music and community programming | [Radio Kazi](https://radiokazi.fr/) | `https://radiokazi.fr/` | webpage, not audio endpoint | needs direct stream extraction |
| ORTN / Radio Ngazidja | Union of the Comoros national/public radio lead | national programming | [ORTN contact](https://www.radio-ngazidja.com/contact) | `https://www.radio-ngazidja.com/contact` | unresolved address | needs verification |
| Hayba Jumla | Moroni digital African voice; 89.3 MHz listing | news/culture | [Hayba Jumla](https://www.hayba-jumla.com/) | `https://www.hayba-jumla.com/` | unresolved address | needs verification |

Remaining leads: direct player URLs for Dounia Web and Radio Kazi, ORTN/Radio Ngazidja streams, Radio Domoni Inter, Midayi FM, Zawiya FM, Star FM, Radio Malezi, Radio Océan Indien and community FM licenses in the ANRTIC list. The run stopped at the four-minute ceiling; it did not claim an exhaustive Comoros search. Next scheduled country: Congo (`CG`).

<a id="run-0052-cg"></a>
### Run 0052 — CG — Congo — 2026-09-09T01:36:00Z

- Start/end: 2026-09-09T01:36:00Z–2026-09-09T01:40:56Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English, explicitly separating Republic of the Congo (Brazzaville) from the Democratic Republic of the Congo. Primary evidence included [Radio Maria Congo](https://www.radiomaria.cg/), [DRTV Congo](https://www.drtv.cg/), and a station listing identifying RADIOKATIOPA in Brazzaville.
- Evaluated 4 station pages; all four were unavailable as direct audio endpoints in the bounded probe. No new ready candidates were added. Raw results: [inputs](research/run-0052-CG-inputs.json) and [probes](research/run-0052-CG-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Radio Maria Congo | Republic of the Congo; Pointe-Noire/Brazzaville Catholic service | French/religious | [Radio Maria Congo](https://www.radiomaria.cg/) | `https://www.radiomaria.cg/` | unresolved address | needs direct stream extraction |
| DRTV International | Brazzaville and Pointe-Noire news service | French/news | [DRTV Congo](https://www.drtv.cg/) | `https://www.drtv.cg/` | unresolved address | radio endpoint not exposed |
| RADIOKATIOPA | Brazzaville, Republic of the Congo;  Internet/FM | French news/talk | [RadioLy station page](https://radioly.app/radio/cg.radiokatiopa/) | `https://radioly.app/radio/cg.radiokatiopa/` | unresolved address | needs direct stream extraction |
| Top Congo FM lead | Search result is Democratic Republic of the Congo, not Republic of the Congo | French news | [Top Congo FM](https://www.topcongo.live/) | `https://www.topcongo.live/` | unresolved address | excluded from CG; belongs to CD |

Remaining leads: Radio Congo, Radio Brazzaville, Canal FM, Radio Liberté, Radio Katiopa direct audio, Radio Maria stream and local stations in Pointe-Noire and Dolisie. Keep Democratic Republic of the Congo stations in `CD`; the run stopped at the four-minute ceiling and did not claim an exhaustive Republic of the Congo search. Next scheduled country: Cook Islands (`CK`).

<a id="run-0053-ck"></a>
### Run 0053 — CK — Cook Islands — 2026-09-09T02:36:00Z

- Start/end: 2026-09-09T02:36:00Z–2026-09-09T02:40:26Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Cook Islands Māori context. Primary evidence included [Life FM Cook Islands](https://lifefmcookislands.org/life-fm-cook-islands-app/), [PMN Cook Islands](https://pmn.co.nz/radio-stations/531-pi/shows/pmn-cook-islands), and [RNZ's rebroadcaster list](https://www.rnz.co.nz/international/rebroadcasters), which identifies Cook Islands Broadcasting AM 630, Matariki FM 89.0 and Araura 88 FM.
- Evaluated 4 station pages; no direct audio endpoint was verifiable in the bounded probe. No new ready candidates were added. Raw results: [inputs](research/run-0053-CK-inputs.json) and [probes](research/run-0053-CK-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Life FM Cook Islands | Local Cook Islands station; app offers live stream | Christian/music; English and Cook Islands Māori | [Life FM Cook Islands](https://lifefmcookislands.org/life-fm-cook-islands-app/) | `https://lifefmcookislands.org/life-fm-cook-islands-app/` | unresolved address | needs direct stream extraction |
| PMN Cook Islands | Cook Islands Māori community programming on Pacific Media Network | Cook Islands Māori/community news | [PMN Cook Islands](https://pmn.co.nz/radio-stations/531-pi/shows/pmn-cook-islands) | `https://pmn.co.nz/radio-stations/531-pi/shows/pmn-cook-islands` | unresolved address | rebroadcast/service lead; needs stream URL |
| Cook Islands Broadcasting | Rarotonga AM 630; RNZ rebroadcaster | English/Cook Islands Māori | [RNZ rebroadcasters](https://www.rnz.co.nz/international/rebroadcasters) | `https://www.rnz.co.nz/international/rebroadcasters` | webpage, not audio endpoint | needs direct stream extraction |
| Matariki FM / Araura 88 FM | Rarotonga and Aitutaki services | local/community | [RNZ rebroadcasters](https://www.rnz.co.nz/international/rebroadcasters) | `https://www.rnz.co.nz/international/rebroadcasters` | webpage, not audio endpoint | needs direct stream extraction |

Remaining leads: current Life FM player URL, Cook Islands Broadcasting Corporation stream, Matariki FM 89.0, Araura 88 FM, Radio Cook Islands 630 AM and local commercial/community stations listed by island. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cook Islands search. Next scheduled country: Costa Rica (`CR`).

<a id="run-0054-cr"></a>
### Run 0054 — CR — Costa Rica — 2026-09-09T03:39:00Z

- Start/end: 2026-09-09T03:39:00Z–2026-09-09T03:43:57Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Spanish and English. Primary evidence included [Grupo Repretel's Radio Monumental](https://gruporepretel.com/radio/monumental), [Radios UCR](https://radios.ucr.ac.cr/) with Radio U, Radio Universidad and Radio 870, and [Radio María Costa Rica](https://www.radiomaria.cr/).
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0054-CR-inputs.json) and [probes](research/run-0054-CR-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Urbano 106 | San José, Costa Rica | Spanish urban/music | [Costa Rica radio directory](https://www.radioscostarica.org/radio/san-jose) | `https://usa18.fastcast4u.com/proxy/rmoohhrw?mp=/1` | already in catalog | existing catalog entry |
| Radio Musical 97.5 | Costa Rica FM service | Spanish music | [Costa Rica radio directory](https://www.radioscostarica.org/radio/san-jose) | `https://live.turadio.stream:7005/stream?type=http&nocache=596` | already in catalog | existing catalog entry |
| 95.5 Jazz Radio | Costa Rica online service | jazz | [Costa Rica radio directory](https://www.radioscostarica.org/radio/san-jose) | `https://streaming.radio.co/s36bd2a451/listen` | already in catalog | existing catalog entry |
| Azul 99.9 FM | Costa Rica commercial FM service | Spanish music | [Costa Rica radio directory](https://www.radioscostarica.org/radio/san-jose) | `https://playerservices.streamtheworld.com/api/livestream-redirect/CRC_999AAC.aac` | already in catalog | existing catalog entry |

Remaining leads: Radio Monumental, Radio UCR/Radio Universidad/Radio 870, Radio María, Radio Fides, community and Indigenous stations mapped by Red Radios Indígenas, Onda UNED and regional services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Costa Rica search. Next scheduled country: Côte d’Ivoire (`CI`).

<a id="run-0055-hr"></a>
### Run 0055 — HR — Croatia — 2026-09-09T04:39:00Z

- Start/end: 2026-09-09T04:39:00Z–2026-09-09T04:44:57Z. Sweep 1. Final status: **partial**.
- Search scope: bounded pass using the Croatian catalog context; the project already contains 107 Croatian stations. Existing identity coverage includes [HRT](https://radio.hrt.hr/) public services and Croatian commercial/community streams.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0055-HR-inputs.json) and [probes](research/run-0055-HR-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| Otvoreni radio | Croatia commercial service | Croatian pop | [Croatian radio directory](https://radiomap.eu/hr) | `https://stream.otvoreni.hr/otvoreni` | already in catalog | existing catalog entry |
| Yammat FM | Zagreb, Croatia | Croatian alternative/music | [Yammat FM](https://yammat.fm/) | `https://stream.yammat.fm/radio/8000/yammat.mp3` | already in catalog | existing catalog entry |
| Top Radio | Croatia commercial service | Croatian music | [Croatian radio directory](https://radiomap.eu/hr) | `https://c5.hostingcentar.com/streams/topradio/` | already in catalog | existing catalog entry |
| HRT HR 1 – Prvi program | Croatian public broadcaster | Croatian news/general | [HRT Radio](https://radio.hrt.hr/) | `https://28503.live.streamtheworld.com/PROGRAM1AAC_SC` | already in catalog | existing catalog entry |

Remaining leads: regional HRT services, university and community stations, island stations, and Croatian-language diaspora services; later sweeps should prioritize stations absent from the existing 107-entry catalog. The run stopped at the bounded procedure limit; it did not claim an exhaustive Croatia search. Next scheduled country: Cuba (`CU`).

<a id="run-0116-kz"></a>
### Run 0116 — Kazakhstan (`KZ`)

- **Completed:** 2026-09-11T22:45:38Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Kazakh/Russian/English queries using Qazaq Radiosy, Kazakh media sources, and radio directories; ten existing catalog inputs were checked.
- **Candidate review:** Radio 90s Eurodance, beu, Palmera Blanca, Qazaq Radiosy, NS-Rock, Radio Azamat, Radio Classic, Radio TMK, NS Pavlodar, and Radio 7 Semey all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0116-KZ-inputs.json), [probes](research/run-0116-KZ-probes.json).
- **Remaining leads:** Qazaq Radiosy regional channels, Shalqar, Darhan, SANA, Bulbul, and local FM services require direct endpoint verification.
- **Next scheduled country:** Kazakhstan (`KZ`) for follow-up because unresolved leads remain.

<a id="run-0115-jo"></a>
### Run 0115 — Jordan (`JO`)

- **Completed:** 2026-09-11T21:44:08Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/English queries using Hayat FM, Jordan Media Commission, JRTV, and station directories; nine stream inputs were checked.
- **Candidate review:** A JRTV Jordan Radio HLS endpoint was unreachable/unsafe; Hayat FM, Mazaj FM, Ain FM, Yarmouk University FM, Mood, Beat, Radio Dahab, and Alnas all matched existing catalog entries. Raw evidence: [inputs](research/run-0115-JO-inputs.json), [probes](research/run-0115-JO-probes.json).
- **Remaining leads:** Radio Jordan, Hawa Dijlah, Radio Fann, university/community stations, and licensed local services require stable HTTPS endpoint verification.
- **Next scheduled country:** Jordan (`JO`) for follow-up because unresolved leads remain.

<a id="run-0114-je"></a>
### Run 0114 — Jersey (`JE`)

- **Completed:** 2026-09-11T20:42:08Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Channel 103, Soleil Radio, BBC, and Channel Islands directories; two existing catalog inputs were checked.
- **Candidate review:** Soleil Radio and Channel 103 matched existing catalog entries. Official pages confirm both local services; BBC Radio Jersey and community/online stations were identified but no additional stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0114-JE-inputs.json), [probes](research/run-0114-JE-probes.json).
- **Remaining leads:** BBC Radio Jersey, Bailiwick Radio, and SouledOutCI require direct endpoint verification.
- **Next scheduled country:** Jersey (`JE`) for follow-up because unresolved leads remain.

<a id="run-0113-jp"></a>
### Run 0113 — Japan (`JP`)

- **Completed:** 2026-09-11T19:41:08Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Japanese/English queries using radiko, NHK, CSRA, and Japanese station directories; ten existing catalog inputs were checked.
- **Candidate review:** Gotanno FM, Japan Hits, Anime Para Ti, Jazz Sakura, Japan City Pop, J-Club, Shonan Beach FM, Hitsujikai, NFRS, and Stereo Anime all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0113-JP-inputs.json), [probes](research/run-0113-JP-probes.json).
- **Remaining leads:** NHK/Radiko services, CSRA community stations, and regional FM broadcasters require direct endpoint verification.
- **Next scheduled country:** Japan (`JP`) for follow-up because unresolved leads remain.

<a id="run-0112-jm"></a>
### Run 0112 — Jamaica (`JM`)

- **Completed:** 2026-09-11T18:39:07Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using RadioJM, Jamaica station directories, FreqTrail, and BCJ licensing sources; ten existing catalog inputs were checked.
- **Candidate review:** Radio Jamaica, Alpha Boys School Radio, Gospel FM, Irie FM, Ghetto Vibes, Fyah 105, Omega KLAS, and SunCity all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0112-JM-inputs.json), [probes](research/run-0112-JM-probes.json).
- **Remaining leads:** Mello FM, NCU, FAME, Kool 97, Hitz 92, community and online-only stations require direct endpoint verification.
- **Next scheduled country:** Jamaica (`JM`) for follow-up because unresolved leads remain.

<a id="run-0111-ci"></a>
### Run 0111 — Ivory Coast (`CI`)

- **Completed:** 2026-09-11T17:37:07Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using HACA, TRACE FM, RTI, and Ivorian radio directories; ten stream inputs were checked.
- **Candidate review:** A HACA-listed Ivoire Sports Radio endpoint was unreachable/unsafe; nine baseline feeds (Trace FM, Africa Radio, Skyrock, Life Radio, Radio Jam, Afrobeat, RadioAgonshu, WaveMaster, and Radio Maria) matched existing catalog entries. Raw evidence: [inputs](research/run-0111-CI-inputs.json), [probes](research/run-0111-CI-probes.json).
- **Remaining leads:** HACA directory entries, Radio Côte d’Ivoire/RTI, and regional/community stations require stable HTTPS endpoint verification.
- **Next scheduled country:** Ivory Coast (`CI`) for follow-up because unresolved leads remain.

<a id="run-0110-it"></a>
### Run 0110 — Italy (`IT`)

- **Completed:** 2026-09-11T16:37:37Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Italian/English queries using Rai, AGCOM, and Italian radio directories; ten existing catalog inputs were checked.
- **Candidate review:** Rai Radio 1, Radio 105, RMC, Radio Sportiva, RDS relax, Virgin Radio Italia, NEU RADIO, and 70/80/90 feeds all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0110-IT-inputs.json), [probes](research/run-0110-IT-probes.json).
- **Remaining leads:** Rai specialty channels, licensed community radio, and independent regional stations require direct endpoint verification.
- **Next scheduled country:** Italy (`IT`) for follow-up because unresolved leads remain.

<a id="run-0109-il"></a>
### Run 0109 — Israel (`IL`)

- **Completed:** 2026-09-11T15:37:07Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Hebrew/English queries using KAN, Israeli radio directories, and public broadcaster sources; ten existing catalog inputs were checked.
- **Candidate review:** Kan Bet, Galgalatz, Joint Radio, 103FM, KAN Gimel, A-Shams, Galei Zahal, KAN 88, and duplicate Galgalatz feeds all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0109-IL-inputs.json), [probes](research/run-0109-IL-probes.json).
- **Remaining leads:** KAN Moreshet, Kan Reka, regional stations, and community services require direct endpoint verification.
- **Next scheduled country:** Israel (`IL`) for follow-up because unresolved leads remain.

<a id="run-0108-im"></a>
### Run 0108 — Isle of Man (`IM`)

- **Completed:** 2026-09-11T14:37:07Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using Manx Radio, Energy FM, 3FM, and Isle of Man station directories; seven existing catalog inputs were checked.
- **Candidate review:** Alive, Manx Radio FM, Energy FM, Isle of Man Free Radio, and both 3FM encodings all matched existing catalog entries. Official station pages confirm the island’s three principal broadcasters; no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0108-IM-inputs.json), [probes](research/run-0108-IM-probes.json).
- **Remaining leads:** Manx Radio AM/Gold/Digital, Radio TT, and temporary or community services require direct endpoint verification.
- **Next scheduled country:** Isle of Man (`IM`) for follow-up because unresolved leads remain.

<a id="run-0107-ie"></a>
### Run 0107 — Ireland (`IE`)

- **Completed:** 2026-09-11T13:36:06Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Irish/English queries using RTÉ, Coimisiún na Meán, RadioFeeds, and community-radio directories; ten existing catalog inputs were checked.
- **Candidate review:** RTÉ 1, Newstalk, Classic Hits, Today FM, RTÉ lyric, Raidió Rí-Rá, RTÉ 2fm, Newstalk AAC, and Gem Radio all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0107-IE-inputs.json), [probes](research/run-0107-IE-probes.json).
- **Remaining leads:** Licensed community broadcasters, regional stations, and Irish-language services require direct endpoint verification.
- **Next scheduled country:** Ireland (`IE`) for follow-up because unresolved leads remain.

<a id="run-0106-iq"></a>
### Run 0106 — Iraq (`IQ`)

- **Completed:** 2026-09-11T12:35:06Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/English queries using Iraqi station sources and directories; ten existing catalog inputs were checked.
- **Candidate review:** SumerFM, Waar, Alseraj, Speda, Darusalam, FM المستقبل, Al-bilad, Turkmen FM, Radio Shanasheel, and Kurdistan 24 all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0106-IQ-inputs.json), [probes](research/run-0106-IQ-probes.json).
- **Remaining leads:** Radio Maria Iraq, Babylon FM, Kirkuk FM, Al Rasheed, Al-Mirbad, and Kurdish/community services require direct endpoint verification.
- **Next scheduled country:** Iraq (`IQ`) for follow-up because unresolved leads remain.

<a id="run-0105-ir"></a>
### Run 0105 — Iran (`IR`)

- **Completed:** 2026-09-11T11:34:36Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English/Persian queries using FreqTrail, Radio Faaz/Yar, and Iranian radio directories; ten existing catalog inputs were checked.
- **Candidate review:** Radio Navahang, Radio Liberty, Gachsaran, RadioSimorgh, Caltex, Radio Yar, Iran On Air, uploadkon, and Radio Mojdeh all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0105-IR-inputs.json), [probes](research/run-0105-IR-probes.json).
- **Remaining leads:** IRIB live services, Radio Donya, Radio Faaz, and independent Persian-language broadcasters require direct endpoint and country-provenance verification.
- **Next scheduled country:** Iran (`IR`) for follow-up because unresolved leads remain.

<a id="run-0104-id"></a>
### Run 0104 — Indonesia (`ID`)

- **Completed:** 2026-09-11T10:33:06Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Indonesian/English queries using RRI, Prasar Bharati-style public sources, and radio directories; ten existing catalog inputs were checked.
- **Candidate review:** I-Radio Jakarta, Elshinta, Radio Sholawat, Mettaswara Koplo, Hardrock Jakarta, Suara Surabaya, Sonora, Suara Giri, Campursari, and Anime FM all matched existing catalog entries. RRI’s official streaming page confirms nationwide public channels; no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0104-ID-inputs.json), [probes](research/run-0104-ID-probes.json).
- **Remaining leads:** Regional RRI services, community stations, and independent city broadcasters require direct endpoint verification.
- **Next scheduled country:** Indonesia (`ID`) for follow-up because unresolved leads remain.

<a id="run-0103-in"></a>
### Run 0103 — India (`IN`)

- **Completed:** 2026-09-11T09:31:35Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Prasar Bharati, Indian radio directories, and public-service sources; ten existing catalog inputs were checked.
- **Candidate review:** Radio Mirchi, Red FM, Bollywood Gaane Purane, Rafi hits, Mirchi Top 20, Hindi Gold, Nostalgic Bollywood, Lata Mangeshkar Radio, and BIG 92.7 all matched existing catalog entries. Prasar Bharati confirms 17 AIR live channels, but no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0103-IN-inputs.json), [probes](research/run-0103-IN-probes.json).
- **Remaining leads:** AIR regional services, community radio, and independent city stations require direct endpoint verification.
- **Next scheduled country:** India (`IN`) for follow-up because unresolved leads remain.

<a id="run-0102-is"></a>
### Run 0102 — Iceland (`IS`)

- **Completed:** 2026-09-11T08:31:05Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Icelandic/English queries using RÚV and Iceland radio directories; six existing catalog inputs were checked.
- **Candidate review:** Útvarp Saga, 80s Flash Back, K 100, Flashback 60s, Retro 89.5, and Fred Film Radio all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0102-IS-inputs.json), [probes](research/run-0102-IS-probes.json).
- **Remaining leads:** RÚV Rás 1/2, Bylgjan, Lindin, and regional/community services require direct stream endpoint verification.
- **Next scheduled country:** Iceland (`IS`) for follow-up because unresolved leads remain.

<a id="run-0101-hu"></a>
### Run 0101 — Hungary (`HU`)

- **Completed:** 2026-09-11T07:30:05Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Hungarian/English queries using NMHH licensing and Hungarian radio directories; ten existing catalog inputs were checked.
- **Candidate review:** Retro Rádió, Rádió 1, Klubrádió, Inforádió, Petőfi, Radio1, 103.9 rock, COOLFM, Oxygen Classic Rock, and Hír FM all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0101-HU-inputs.json), [probes](research/run-0101-HU-probes.json).
- **Remaining leads:** Local/community services listed by NMHH and independent directories require direct stream endpoint verification.
- **Next scheduled country:** Hungary (`HU`) for follow-up because unresolved leads remain.

<a id="run-0100-hk"></a>
### Run 0100 — Hong Kong (`HK`)

- **Completed:** 2026-09-11T06:28:35Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English/Chinese queries using RTHK, government, and Hong Kong community-radio sources; ten existing catalog inputs were checked.
- **Candidate review:** RTHK Radio 1/2, 良友 channels, Universal Health Radio, Fing Radio, 台山電台, Radio Lantau, AXR, and Shenzhen traffic radio all matched existing catalog entries. Official RTHK sources confirm public live services; no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0100-HK-inputs.json), [probes](research/run-0100-HK-probes.json).
- **Remaining leads:** HKCR, Apple-FM, Digital Radio HK, and other independent/community stations need direct endpoint verification.
- **Next scheduled country:** Hong Kong (`HK`) for follow-up because unresolved leads remain.

<a id="run-0099-hn"></a>
### Run 0099 — Honduras (`HN`)

- **Completed:** 2026-09-11T05:27:04Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Spanish/English queries using CONATEL, Radio Nacional de Honduras, and station directories; ten existing catalog inputs were checked.
- **Candidate review:** The ten tested feeds (Stereo Éxitos, XY, Vox, Musiquera, Exa, Suave, Radio Activa, 94 SU, and DCR) all matched existing catalog entries. Official licensing and RNH sources identify additional stations, but no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0099-HN-inputs.json), [probes](research/run-0099-HN-probes.json).
- **Remaining leads:** Radio Nacional regional services, HRN, community and departmental stations require direct stream endpoint verification.
- **Next scheduled country:** Honduras (`HN`) for follow-up because unresolved leads remain.

<a id="run-0098-hm"></a>
### Run 0098 — Heard Island and McDonald Islands (`HM`)

- **Completed:** 2026-09-11T04:26:04Z
- **Status:** partial; no new ready candidates.
- **Search scope:** five targeted queries covering local broadcasting, communications, and amateur-radio references; no online broadcast stream was identified.
- **Candidate review:** Heard Island and McDonald Islands are uninhabited and sources describe only expedition/amateur-radio activity, not a resident online radio station. No stream inputs were available. Raw evidence: [inputs](research/run-0098-HM-inputs.json), [probes](research/run-0098-HM-probes.json).
- **Remaining leads:** Revisit only if a future expedition establishes an attributable public stream.
- **Next scheduled country:** Heard Island and McDonald Islands (`HM`) for follow-up if evidence changes.

<a id="run-0097-ht"></a>
### Run 0097 — Haiti (`HT`)

- **Completed:** 2026-09-11T03:22:34Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using Haitian station pages, directories, and regulatory sources; ten existing catalog inputs were checked.
- **Candidate review:** The ten tested feeds (BBC News Haiti, Vision 2000, RFI, 4VEH, Ananda Marga, Radio Lumiere, Radio St Charles, RTVS, Intermix, and Radio Jamesen Show) all matched existing catalog entries. Official station pages identify additional local services, but no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0097-HT-inputs.json), [probes](research/run-0097-HT-probes.json).
- **Remaining leads:** Fondènèg FM, Radio Caraïbes, DodorVibe, Planet Kreyol, and directory-listed regional/community stations require direct endpoint verification.
- **Next scheduled country:** Haiti (`HT`) for follow-up because unresolved leads remain.

<a id="run-0096-gy"></a>
### Run 0096 — Guyana (`GY`)

- **Completed:** 2026-09-11T02:22:04Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using the Guyana National Broadcasting Authority, NCN, and station directories; seven existing catalog stream inputs were checked.
- **Candidate review:** All seven tested feeds (Voice of Guyana, Radio Guyana, GoMoseley, 88.5 Rock, MAAD, NTN, and chwitiweb) matched existing catalog entries. GNBA and NCN sources identify additional licensed services, but no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0096-GY-inputs.json), [probes](research/run-0096-GY-probes.json).
- **Remaining leads:** I Radio, NCN regional services, and GNBA-listed local stations require direct endpoint verification.
- **Next scheduled country:** Guyana (`GY`) for follow-up because unresolved leads remain.

<a id="run-0095-gw"></a>
### Run 0095 — Guinea-Bissau (`GW`)

- **Completed:** 2026-09-10T21:10:24Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Portuguese/English queries using Bissau.Radio, RDN, community-radio directories, and station sources; one catalog stream was checked.
- **Candidate review:** Rádio Voz da Guiné matched the existing `GW` catalog entry. Sources identify RDN, Rádio Sol Mansi, Rádio Jovem, and many community services, but no additional stable HTTPS stream was verified within the run limit. Raw evidence: [inputs](research/run-0095-GW-inputs.json), [probes](research/run-0095-GW-probes.json).
- **Remaining leads:** Rádio Sol Mansi, RDN, Rádio Jovem, Voz de Esperança, Rádio Transparência, and regional community stations require direct stream endpoint verification.
- **Next scheduled country:** Guinea-Bissau (`GW`) for follow-up because unresolved leads remain.

<a id="run-0094-gn"></a>
### Run 0094 — Guinea (`GN`)

- **Completed:** 2026-09-10T20:09:24Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using RTG, Bonheur FM, Djoma FM, Littoral FM, and regulator sources; four existing catalog inputs were checked.
- **Candidate review:** Bonheur FM, LGF Talk, LGF Fun, and Littoral FM all matched existing Guinea catalog entries. Official RTG and HAC sources confirm national and private radio identity; no distinct stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0094-GN-inputs.json), [probes](research/run-0094-GN-probes.json).
- **Remaining leads:** RTG, Djoma FM, Espace, regional and community stations require direct stable stream endpoint verification in later sweeps.
- **Next scheduled country:** Guinea (`GN`) for follow-up because unresolved leads remain.

<a id="run-0093-gg"></a>
### Run 0093 — Guernsey (`GG`)

- **Completed:** 2026-09-10T19:08:24Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using Guernsey station sites and directories; two candidate stream inputs were checked.
- **Candidate review:** Riduna-radio.com matched the existing catalog entry. A BBC Radio Guernsey stream URL from a directory was unreachable/unsafe under HTTPS validation. Official sources identify Guernsey Community Radio, GNetRadio, and Island FM, while directories list BBC and Jubilee Hospital Radio; no distinct verified stream was added. Raw evidence: [inputs](research/run-0093-GG-inputs.json), [probes](research/run-0093-GG-probes.json).
- **Remaining leads:** Resolve official GCR, GNetRadio, Island FM, BBC Radio Guernsey, and Jubilee Hospital Radio stream URLs in later sweeps.
- **Next scheduled country:** Guernsey (`GG`) for follow-up because unresolved leads remain.

<a id="run-0092-gt"></a>
### Run 0092 — Guatemala (`GT`)

- **Completed:** 2026-09-10T18:07:23Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Spanish/English queries using Emisoras Unidas and Guatemalan station directories; ten existing catalog stream inputs were checked.
- **Candidate review:** The ten tested feeds (including Exa FM, Emisoras Unidas, Globo, Clásica, Radio Cultural TGN, Mía, Radio Punto, Estéreo Alegre, La Red, and Radio Viva) all matched existing `GT` catalog entries. Raw evidence: [inputs](research/run-0092-GT-inputs.json), [probes](research/run-0092-GT-probes.json).
- **Remaining leads:** Emisoras Unidas regional services, indigenous/community broadcasters, and directory-listed independent stations need stable HTTPS endpoint verification in later sweeps.
- **Next scheduled country:** Guernsey (`GG`).

<a id="run-0091-gu"></a>
### Run 0091 — Guam (`GU`)

- **Completed:** 2026-09-10T17:07:23Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using Guam station sites and directories; three candidate URLs were checked.
- **Candidate review:** Existing catalog entries cover 104.3 Boss FM, KUSG, and Harvest Family Radio. The official Harvest Family Radio page confirms local Guam programming; directories identify The Kat, Isla 63, Wave 105.1, KPRG, Power 98, and other leads, but no distinct stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0091-GU-inputs.json), [probes](research/run-0091-GU-probes.json).
- **Remaining leads:** Follow official pages for The Kat/KGUM-FM, Isla 63/KUAM, Wave 105.1, KPRG, and Power 98 in a later sweep.
- **Next scheduled country:** Guernsey (`GG`).

<a id="run-0090-gp"></a>
### Run 0090 — Guadeloupe (`GP`)

- **Completed:** 2026-09-10T16:06:23Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French and English queries using local directories and station sources; ten candidate stream inputs were checked.
- **Candidate review:** Guadeloupe 1ère, Radio Shatta Movement, Nostalgie Guadeloupe, Antilles Média, Massabielle, Bel Radio, NRJ Guadeloupe, RCI Guadeloupe, Sofaia Altitude, and Madras all matched existing catalog entries. Raw evidence: [inputs](research/run-0090-GP-inputs.json), [probes](research/run-0090-GP-probes.json).
- **Remaining leads:** Local directories list Radio Souffle de vie, RHT, Trace FM, Saphir FM, Radio Kariba, and other services; later sweeps should verify official stable HTTPS streams and distinct Guadeloupe provenance.
- **Next scheduled country:** Guam (`GU`).

<a id="run-0089-gd"></a>
### Run 0089 — Grenada (`GD`)

- **Completed:** 2026-09-10T15:05:53Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using Grenada station sites, directories, and the NTRC broadcast register; three stream inputs were checked.
- **Candidate review:** Boss FM, Wee FM, and Star FM were all existing catalog entries. Directory sources identify additional leads such as Hott FM, Fresh FM, Real FM, Power FM, Harbour Light Radio, and City Sound FM, but no distinct stable HTTPS stream was verified within the run limit. Raw evidence: [inputs](research/run-0089-GD-inputs.json), [probes](research/run-0089-GD-probes.json).
- **Remaining leads:** Follow official pages for Hott FM, Fresh FM, Real FM, Power FM, Harbour Light Radio, and City Sound FM in a later sweep.
- **Next scheduled country:** Guadeloupe (`GP`).

<a id="run-0088-gl"></a>
### Run 0088 — Greenland (`GL`)

- **Completed:** 2026-09-10T14:05:52Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using KNR and Greenland station directories; five candidate stream inputs were checked.
- **Candidate review:** Nanoq FM, KNR Live Radio, and three other baseline feeds all matched existing catalog entries. KNR’s official site confirms the national radio service; local directories list additional town services, but no distinct stable HTTPS stream was verified in this run. Raw evidence: [inputs](research/run-0088-GL-inputs.json), [probes](research/run-0088-GL-probes.json).
- **Remaining leads:** Tusaat Uummannaq, Tusaat Aasiaat, Tasiilap Tusaalaa, Sisimiut Tusaataat, Radio Grønnedal, Radio 5OZ20, Qaanaaq Radiunga, and Inuunerup Nipaa require direct station pages or stable stream URLs.
- **Next scheduled country:** Grenada (`GD`).

<a id="run-0087-gr"></a>
### Run 0087 — Greece (`GR`)

- **Completed:** 2026-09-10T13:05:52Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using ERT and Greek radio directories, plus ten candidate stream inputs checked within the run limits.
- **Candidate review:** Most tested endpoints were unreachable, unsafe, or failed HTTPS validation; one Yammat FM endpoint was already cataloged under Croatia and was excluded from Greek additions. Raw inputs and probe outcomes: [inputs](research/run-0087-GR-inputs.json), [probes](research/run-0087-GR-probes.json).
- **Remaining leads:** ERT’s live service page and Greek directories list many stations; future sweeps should resolve stable HTTPS audio endpoints and verify local identity before proposing additions.
- **Next scheduled country:** Greenland (`GL`).

<a id="run-0086-gi"></a>
### Run 0086 — Gibraltar (`GI`)

- **Completed:** 2026-09-10T12:04:52Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted web queries covering official Gibraltar radio, BFBS Gibraltar, community radio, directories, and station websites; six catalog baseline stream URLs were checked within the four-minute budget.
- **Candidate review:** GBC Radio Gibraltar, BFBS Gibraltar, Alpha FM, RadioSeu, Radio Gibraltar Plus 100.5, and RadioGibraltar MW all matched existing `GI` catalog entries. Probe results are recorded in `documents/research/run-0086-GI-probes.json`.
- **Remaining leads:** No additional station with a distinct, directly attributable Gibraltar stream was verified in this run. Revisit official station pages or local directories if later evidence indicates a new feed.
- **Next scheduled country:** Greece (`GR`).

<a id="run-0085-gh"></a>
### Run 0085 — GH — Ghana — 2026-09-10T10:40:00Z

- Start/end: 2026-09-10T10:40:00Z–2026-09-10T11:03:22Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. Ghanaian directories and the [NCA authorised-stations report](https://nca.org.gh/wp-content/uploads/2022/11/SUMMARY-OF-RADIO-BROADCASTING-STATIONS-IN-GHANA.pdf) supplied national/regional identity; Ghana Radio and FM-RADIO supported stream discovery.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0085-GH-inputs.json) and [probes](research/run-0085-GH-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Citi FM | Accra, Ghana; independent national service | English / news and talk | [Ghana Summary](https://www.ghanasummary.com/radio) | `https://citi973fm.radioca.st/index.html:80/;stream.mp3` | catalog duplicate | Already cataloged |
| Joy FM | Accra, Ghana; Multimedia Group service | English / news and entertainment | [Ghana Summary](https://www.ghanasummary.com/radio) | `https://mmg.streamguys1.com/JoyFM-mp3` | catalog duplicate | Already cataloged |
| Adom FM | Accra, Ghana; Multimedia Group Akan-language service | Akan/Twi / talk and music | [Ghana Summary](https://www.ghanasummary.com/radio) | `https://mmg.streamguys1.com/AdomFM-mp3` | catalog duplicate | Already cataloged |
| Peace FM | Accra, Ghana; Despite Media service | Akan/English / talk and news | [Ghana Summary](https://www.ghanasummary.com/radio) | `https://peacefm-atunwadigital.streamguys1.com/peacefm` | catalog duplicate | Already cataloged |

Remaining leads: GBC Uniiq, Asempa FM, Angel FM, Starr FM, Radio Universe campus service, regional Kumasi/Tamale/Cape Coast broadcasters, community stations and the many online-only African music services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Ghana search. Next scheduled country: Gibraltar (`GI`).

<a id="run-0084-de"></a>
### Run 0084 — DE — Germany — 2026-09-10T09:40:00Z

- Start/end: 2026-09-10T09:40:00Z–2026-09-10T10:03:22Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and German. [Deutschlandfunk's official stream page](https://www.deutschlandfunk.de/livestream-100.html) supplied direct public-service stream evidence; [ARD's radio overview](https://hilfe.ard.de/artikel/alle-ard-radiosender-im-ueberblick/) and radio.de supported the national/regional landscape.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0084-DE-inputs.json) and [probes](research/run-0084-DE-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Deutschlandfunk | Germany; Deutschlandradio national public service | German / news and current affairs | [Deutschlandfunk](https://www.deutschlandfunk.de/livestream-100.html) | `https://st01.sslstream.dlf.de/dlf/01/128/mp3/stream.mp3?aggregator=web` | catalog duplicate | Already cataloged |
| SWR3 | Baden-Württemberg/Rhineland-Palatinate, Germany; ARD regional service | German / pop | [ARD radio overview](https://hilfe.ard.de/artikel/alle-ard-radiosender-im-ueberblick/) | `https://liveradio.swr.de/sw282p3/swr3/play.mp3` | catalog duplicate | Already cataloged |
| 1LIVE | North Rhine-Westphalia, Germany; WDR/ARD service | German / pop and youth | [ARD radio overview](https://hilfe.ard.de/artikel/alle-ard-radiosender-im-ueberblick/) | `https://wdr-1live-live.icecast.wdr.de/wdr/1live/live/mp3/128/stream.mp3` | catalog duplicate | Already cataloged |
| WDR 5 | North Rhine-Westphalia, Germany; WDR/ARD service | German / talk and culture | [ARD radio overview](https://hilfe.ard.de/artikel/alle-ard-radiosender-im-ueberblick/) | `https://wdr-wdr5-live.icecast.wdr.de/wdr/wdr5/live/mp3/128/stream.mp3` | catalog duplicate | Already cataloged |

Remaining leads: the full ARD regional networks, Deutschlandradio Kultur/Nova, Bayern 1–3, SWR1/2/4, WDR 2/3/4, NDR, MDR, HR, RBB, Radio Eins, Rock Antenne, Sunshine Live, local/community stations and DAB-only services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Germany search. Next scheduled country: Ghana (`GH`).

<a id="run-0083-ge"></a>
### Run 0083 — GE — Georgia — 2026-09-10T08:40:00Z

- Start/end: 2026-09-10T08:40:00Z–2026-09-10T09:02:21Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Georgian-oriented terms. [Radio Palitra](https://www.radiopalitra.ge/programs/) and its [live stream](https://livestream.palitra.ge/) supplied primary identity; Georgian directories listed Tbilisi and regional stations.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0083-GE-inputs.json) and [probes](research/run-0083-GE-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio Amra | Tbilisi, Georgia; station directory identity | Georgian / classical | [OpenTune Georgia](https://opentune.net/radio/ge) | `https://streamer.radio.co/s34b5469e0/listen` | catalog duplicate | Already cataloged |
| Radio Palitra | Georgia; official station/program site | Georgian / news and talk | [Radio Palitra](https://www.radiopalitra.ge/programs/) | `https://radiostream.palitra.ge/stream.mp3` | catalog duplicate | Already cataloged |
| Radio Sivrce | Georgia; Tbilisi directory identity | Georgian / general | [OpenTune Georgia](https://opentune.net/radio/ge) | `https://proxy.streamer.mediabox.ge/ice/8000/sivrce` | catalog duplicate | Already cataloged |
| Radio Adjara | Batumi/Adjara, Georgia; regional service | Georgian / regional news and culture | [OpenTune Georgia](https://opentune.net/radio/ge) | `https://edge.mixlr.com/channel/bzorq` | catalog duplicate | Already cataloged |

Remaining leads: Georgian Public Broadcaster services, Radio Imedi, Fortuna, Avtoradio, Ar Daidardo, Green Wave, Marneuli FM, LF Radio, Rioni FM, Jukebox 94.3, Sputnik Abkhazia and community/regional broadcasters in Adjara and other regions. The run stopped at the four-minute ceiling; it did not claim an exhaustive Georgia search. Next scheduled country: Germany (`DE`).

<a id="run-0082-gm"></a>
### Run 0082 — GM — Gambia — 2026-09-10T07:40:00Z

- Start/end: 2026-09-10T07:40:00Z–2026-09-10T08:01:51Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. [PURA's broadcasting register](https://pura.gm/ict/sub-sectors/broadcasting/) provided official frequencies and community/commercial station identity; [West Coast Radio](https://westcoast.gm/main/) supplied primary station information; OptiRadio and The Gambia Radio supplied discovery.
- Evaluated 4 page inputs; all failed the HTTPS/audio probe as unsafe or unresolvable, so 0 ready candidates were added. Raw results: [inputs](research/run-0082-GM-inputs.json) and [probes](research/run-0082-GM-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| West Coast Radio | Serrekunda, The Gambia; commercial station and 92.1/95.3 streams | English / news and entertainment | [West Coast Radio](https://westcoast.gm/main/) | `https://westcoast.gm/main/` | unsafe/unresolvable | Needs direct audio endpoint |
| Gambia Radio & Television Service | Bakau/Banjul; public broadcaster | English/local languages / news and ethnic programming | [PURA register](https://pura.gm/ict/sub-sectors/broadcasting/) | `https://pura.gm/ict/sub-sectors/broadcasting/` | unsafe/unresolvable | Needs direct audio endpoint |
| AfriRadio Gambia | Banjul; licensed commercial station | English / international | [OptiRadio Gambia](https://www.optiradio.com/radio-stations/Gambia) | `https://www.optiradio.com/radio-stations/Gambia` | unsafe/unresolvable | Directory only |
| The Gambia Radio online leads | Gambia-associated online services | mixed / music and talk | [The Gambia Radio](https://thegambiaradio.com/genre/music/) | `https://thegambiaradio.com/genre/music/` | unsafe/unresolvable | Directory/player page only |

Remaining leads: GRTS Radio direct stream, West Coast 92.1/95.3 audio endpoints, Star FM, Capital FM, Unique FM, Paradise FM, Taranga FM, Freedom Radio, QRadio and PURA-listed community stations in Soma, Bwiam, Kerewan, Bansang, Brikamaba and Brikama. The run stopped at the four-minute ceiling; it did not claim an exhaustive Gambia search. Next scheduled country: Georgia (`GE`).

<a id="run-0081-ga"></a>
### Run 0081 — GA — Gabon — 2026-09-10T06:40:00Z

- Start/end: 2026-09-10T06:40:00Z–2026-09-10T07:01:21Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. Gabon's [Ministry of Communication announcement](https://www.communication.gouv.ga/9-actualites/2177-lancement-officiel-du-site-internet-de-radio-gabon-et-inauguration-du-studio-d-enregistrement-agathe-okoumba/) provided national Radio Gabon identity; RadioDirectory, GoAfrica and oiRadio supplied discovery leads for NRJ 241, TOP FM, Urban FM and community services.
- Evaluated 4 page inputs; all failed the HTTPS/audio probe as unsafe or unresolvable, so 0 ready candidates were added. Raw results: [inputs](research/run-0081-GA-inputs.json) and [probes](research/run-0081-GA-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio Gabon | Libreville, Gabon; national broadcaster | French / news, talk and culture | [Gabon Ministry](https://www.communication.gouv.ga/9-actualites/2177-lancement-officiel-du-site-internet-de-radio-gabon-et-inauguration-du-studio-d-enregistrement-agathe-okoumba/) | `https://www.communication.gouv.ga/9-actualites/2177-lancement-officiel-du-site-internet-de-radio-gabon-et-inauguration-du-studio-d-enregistrement-agathe-okoumba/` | unsafe/unresolvable | Needs direct audio endpoint |
| NRJ 241 | Gabon; station directory identity | French / pop | [RadioDirectory](https://radiodirectory.com/Radio_Stations/Africa/Gabon/index.html) | `https://radiodirectory.com/Radio_Stations/Africa/Gabon/index.html` | unsafe/unresolvable | Player page only |
| TOP FM 105.5 | Gabon; station directory identity | French / general | [RadioDirectory](https://radiodirectory.com/Radio_Stations/Africa/Gabon/index.html) | `https://radiodirectory.com/Radio_Stations/Africa/Gabon/index.html` | unsafe/unresolvable | Player page only |
| Urban FM 104.5 | Libreville, Gabon; local station identity | French / urban music | [oiRadio Gabon](https://www.oiradio.co/gabon) | `https://www.oiradio.co/gabon` | unsafe/unresolvable | Directory/player page only |

Remaining leads: Radio Gabon direct stream, RTG 1/2, Africa Radio/Africa No.1, Urban FM, NRJ 241, TOP FM, Radio Génération Nouvelle, Radio Bonne Nouvelle, Hero Radio Gabon and Eben Radio services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Gabon search. Next scheduled country: Gambia (`GM`).

<a id="run-0080-tf"></a>
### Run 0080 — TF — French Southern and Antarctic Lands — 2026-09-10T05:40:00Z

- Start/end: 2026-09-10T05:40:00Z–2026-09-10T05:58:21Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. The [French overseas ministry](https://www.outre-mer.gouv.fr/territoires/terres-australes-et-antarctiques-francaises) confirms the TAAF districts; TAAF communications material and radio-communications references were reviewed. These remote, largely uninhabited scientific territories have no public online radio station found in this pass.
- Evaluated 4 source/page inputs; all failed the HTTPS/audio probe as unsafe or unresolvable, so 0 ready candidates were added. Raw results: [inputs](research/run-0080-TF-inputs.json) and [probes](research/run-0080-TF-probes.json).

| Station / service | Location / territory evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| TAAF radio communications bureau | Crozet, Kerguelen, Saint-Paul/Amsterdam, Terre Adélie and Éparses; operational communications only | French / HF, VHF and satellite communications | [TAAF](https://taaf.fr/content/uploads/2021/05/20210517-guidedemission.pdf) | `https://taaf.fr/content/uploads/2021/05/20210517-guidedemission.pdf` | unsafe/unresolvable | Not a public audio stream |
| Kerguelen–Crozet links | TAAF bases; historical radio-telephone links | operational communications | [AMAEFP](https://www.amaepf.fr/ker18N/rubriques/frame.php?LG=fr&PG=05&RUB=02) | `https://www.amaepf.fr/ker18N/rubriques/frame.php?LG=fr&PG=05&RUB=02` | unsafe/unresolvable | Not a public audio stream |
| TAAF territory information | French Southern and Antarctic Lands | n/a | [Outre-mer ministry](https://www.outre-mer.gouv.fr/territoires/terres-australes-et-antarctiques-francaises) | `https://www.outre-mer.gouv.fr/territoires/terres-australes-et-antarctiques-francaises` | unsafe/unresolvable | No station identified |
| Directory aggregate lead | TAAF-associated listings | mixed | [AllRadio](https://www.allradio.net/country/204) | `https://allradio.net/country/204` | unsafe/unresolvable | No verifiable direct stream |

Remaining leads: any station-base internal audio, expedition or science webcast, and future public streams from TAAF or French polar agencies. The run stopped at the four-minute ceiling; it did not claim an exhaustive French Southern and Antarctic Lands search. Next scheduled country: Gabon (`GA`).

<a id="run-0079-pf"></a>
### Run 0079 — PF — French Polynesia — 2026-09-10T04:40:00Z

- Start/end: 2026-09-10T04:40:00Z–2026-09-10T04:57:50Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. [Tiare FM](https://www.tiarefm.pf/), [Radio 1 Tahiti](https://www.radio1.pf/) and [Polynésie La 1ère](https://la1ere.franceinfo.fr/) supplied local and public-service identity; directories covered island stations.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0079-PF-inputs.json) and [probes](research/run-0079-PF-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Tiare FM | Tahiti, French Polynesia; official site | French/Tahitian / local music | [Tiare FM](https://www.tiarefm.pf/) | `https://live.tiarefm.pf:8443/tiarefm` | catalog duplicate | Already cataloged |
| Hiti FM | Tahiti, French Polynesia; local directory | French/Tahitian / music | [Radio directories](https://streema.com/radios/country/French_Polynesia) | `https://n01.radiojar.com/u0yz7p0mb.mp3` | catalog duplicate | Already cataloged |
| Radio 1 Tahiti | Papeete, French Polynesia; official site | French/Tahitian / news and entertainment | [Radio 1](https://www.radio1.pf/) | `https://live.radio1.pf:8443/radio1` | catalog duplicate | Already cataloged |
| Polynésie 1ère | French Polynesia; France Télévisions public service | French/Tahitian / news and culture | [La 1ère](https://la1ere.franceinfo.fr/) | `https://polynesie.ice.infomaniak.ch/polynesie-128.mp3` | catalog duplicate | Already cataloged |

Remaining leads: Tahiti Web Radio, Radio Mā‘ohi, Radio LVDL, Radio Maria No Te Hau, Marevareva Radio, local island relays and community services across Moorea, Raiatea, Bora Bora and the Austral/Gambier islands. The run stopped at the four-minute ceiling; it did not claim an exhaustive French Polynesia search. Next scheduled country: Gabon (`GA`).

<a id="run-0078-gf"></a>
### Run 0078 — GF — French Guiana — 2026-09-10T03:40:00Z

- Start/end: 2026-09-10T03:40:00Z–2026-09-10T03:57:20Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in French and English. [Guyane.fm](https://guyane.fm/) listed the local FM market; [Guyane La 1ère](https://la1ere.franceinfo.fr/guyane/programme-audio/) and NRJ Guyane supplied primary/local identity evidence.
- Evaluated 4 candidate inputs; 3 were catalog duplicates and the NRJ Guyane homepage failed the bounded audio probe, so 0 ready candidates were added. Raw results: [inputs](research/run-0078-GF-inputs.json) and [probes](research/run-0078-GF-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Chérie FM Guyane | Cayenne/French Guiana; local network stream | French / pop | [Guyane.fm](https://guyane.fm/) | `https://cheriefmguyane.ice.infomaniak.ch/cheriefmguyane-64.aac` | catalog duplicate | Already cataloged |
| Guyane 1ère | French Guiana; France Télévisions local public service | French / news and culture | [Guyane La 1ère](https://la1ere.franceinfo.fr/guyane/programme-audio/) | `https://guyane.ice.infomaniak.ch/guyane-128.mp3` | catalog duplicate | Already cataloged |
| Métis FM | French Guiana; local FM listing | French / local music | [Guyane.fm](https://guyane.fm/) | `https://str0.creacast.com/metisfm.mp3` | catalog duplicate | Already cataloged |
| NRJ Guyane | French Guiana; official local site | French / contemporary pop | [NRJ Guyane](https://www.nrjguyane.fm/) | `https://www.nrjguyane.fm/` | unsafe/unresolvable | Needs direct audio endpoint |

Remaining leads: Hit Radio Guyane, Radio Voix dans le Désert, Vibes Radio, Joie de Vivre, Nostalgie, RFM Guyane, Radio Classica, Mosaïque, Ghetto Black Radio, Radio Tout’Moune, Trace FM, Radio des Îles, Lumière, Radio Saint-Gabriel, KFM, Radio Rossignol, Péyi Guyane and RTL2 Guyane. The run stopped at the four-minute ceiling; it did not claim an exhaustive French Guiana search. Next scheduled country: Gabon (`GA`).

<a id="run-0077-fr"></a>
### Run 0077 — FR — France — 2026-09-10T02:40:00Z

- Start/end: 2026-09-10T02:40:00Z–2026-09-10T02:56:32Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and French. [Arcom's national FM/DAB list](https://www.arcom.fr/radio-et-audio-numerique/radio-fm-dab/radios) established broad station coverage; [Radio France](https://www.radiofrance.com/frequences) supplied public-service identity and direct-stream information; NRJ's official site was checked.
- Evaluated 4 candidate stream inputs; 3 were catalog duplicates and 1 NRJ URL failed the bounded probe, so 0 ready candidates were added. Raw results: [inputs](research/run-0077-FR-inputs.json) and [probes](research/run-0077-FR-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| France Info | France; Radio France national news service | French / news | [Radio France](https://www.radiofrance.com/frequences) | `https://direct.franceinfo.fr/live/franceinfo-midfi.mp3` | catalog duplicate | Already cataloged |
| RMC | France; national commercial service | French / talk and sport | [Arcom radio list](https://www.arcom.fr/radio-et-audio-numerique/radio-fm-dab/radios) | `https://audio.bfmtv.com/rmcradio_128.mp3` | catalog duplicate | Already cataloged |
| Nostalgie | France; national commercial network | French / oldies | [NRJ](https://www.nrj.fr/) | `https://streaming.nrjaudio.fm/oua8a3w2dqao` | unsafe/unresolvable | Needs refreshed stream URL |
| Europe 1 | France; national commercial service | French / news and talk | [Arcom radio list](https://www.arcom.fr/radio-et-audio-numerique/radio-fm-dab/radios) | `https://stream.europe1.fr/europe1.aac` | catalog duplicate | Already cataloged |

Remaining leads: the full Radio France network (France Inter, France Culture, FIP, France Musique, Mouv’, France Bleu locals), RTL, Europe 2, Skyrock, Fun Radio, regional/community stations in the Arcom list, overseas departments and French-language web radios. The run stopped at the four-minute ceiling; it did not claim an exhaustive France search. Next scheduled country: French Guiana (`GF`).

<a id="run-0076-fi"></a>
### Run 0076 — FI — Finland — 2026-09-10T01:40:00Z

- Start/end: 2026-09-10T01:40:00Z–2026-09-10T01:56:02Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Finnish/Swedish-oriented terms. [Yle's corporate overview](https://yle.fi/a/20-10006621) confirmed the national public-radio portfolio; Finnish directories and Radio Suomi supplied commercial and regional discovery.
- Evaluated 4 candidate stream inputs; 2 were catalog duplicates and 2 Bauer redirect URLs failed the bounded probe, so 0 ready candidates were added. Raw results: [inputs](research/run-0076-FI-inputs.json) and [probes](research/run-0076-FI-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| YleX | Finland; Yle national youth channel | Finnish / pop and youth | [Yle](https://yle.fi/a/20-10006621) | `https://icecast.live.yle.fi/radio/YleX/icecast.audio` | catalog duplicate | Already cataloged |
| NRJ Finland | Finland; commercial directory identity | Finnish / pop | [Suomi Radio](https://suomi-radio.com/) | `https://stream-redirect.bauermedia.fi/nrj/nrj_64.aac` | unsafe/unresolvable | Needs refreshed redirect URL |
| Radio Nova | Finland; commercial directory identity | Finnish / pop | [Suomi Radio](https://suomi-radio.com/) | `https://stream-redirect.bauermedia.fi/radionova/radionova_64.aac` | unsafe/unresolvable | Needs refreshed redirect URL |
| Yle Radio 1 | Finland; Yle national channel | Finnish / culture and classical | [Yle](https://yle.fi/a/20-10006621) | `https://icecast.live.yle.fi/radio/YleRadio1Hifi/icecast.audio` | catalog duplicate | Already cataloged |

Remaining leads: Yle Radio Suomi regional feeds, Yle Vega, Yle X3M, Yle Sámi Radio, Radio Helsinki, Radio Rock, Suomipop, Iskelmä, Radio City, Basso and local Finnish/Swedish-language community services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Finland search. Next scheduled country: France (`FR`).

<a id="run-0075-fj"></a>
### Run 0075 — FJ — Fiji — 2026-09-10T00:40:00Z

- Start/end: 2026-09-10T00:40:00Z–2026-09-10T00:55:32Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Fijian/Hindi-oriented terms. [Fiji Broadcasting Corporation](https://www.fbcnews.com.fj/news/fbc-radio-available-now-worldwide/) confirmed six live streams migrated to the official SERE+ platform; regional directories supported station and language identity.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog (duplicate catalog rows are reported by the helper), so 0 new ready candidates were added. Raw results: [inputs](research/run-0075-FJ-inputs.json) and [probes](research/run-0075-FJ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| 2Day FM | Fiji; FBC commercial network | English / contemporary pop | [FBC News](https://www.fbcnews.com.fj/news/fbc-radio-available-now-worldwide/) | `https://icecast1.sere.plus/2Day` | catalog duplicate | Already cataloged |
| Bula FM | Fiji; FBC iTaukei service | iTaukei / music and talk | [FBC News](https://www.fbcnews.com.fj/news/fbc-radio-available-now-worldwide/) | `https://icecast1.sere.plus/Bula` | catalog duplicate | Already cataloged |
| Radio Fiji One | Fiji; FBC public service | iTaukei / news and culture | [FBC News](https://www.fbcnews.com.fj/news/fbc-radio-available-now-worldwide/) | `https://icecast1.sere.plus/RFOne` | catalog duplicate | Already cataloged |
| Radio Fiji Two | Fiji; FBC multilingual service | Fiji Hindi / music and community | [FBC News](https://www.fbcnews.com.fj/news/fbc-radio-available-now-worldwide/) | `https://icecast1.sere.plus/RFTwo` | catalog duplicate | Already cataloged |

Remaining leads: Gold FM, Mirchi FM, Navtarang, Radio Fiji One/Two regional variants, Legend FM, FM96, Viti FM, community and island stations, and the new SERE+ channel lineup. The run stopped at the four-minute ceiling; it did not claim an exhaustive Fiji search. Next scheduled country: Finland (`FI`).

<a id="run-0074-fo"></a>
### Run 0074 — FO — Faroe Islands — 2026-09-09T23:40:00Z

- Start/end: 2026-09-09T23:40:00Z–2026-09-09T23:54:01Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Danish/Faroese terms. [Kringvarp Føroya netvarp](https://kvf.fo/netvarp) supplied national public-radio stream evidence; Faroese directories and local listings supported FM1, Norðlýsið, VoxPop and Aldan identities.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0074-FO-inputs.json) and [probes](research/run-0074-FO-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| FM1 88.7 | Faroe Islands; local mixed-program service | Faroese / mixed | [Faroese listings](https://www.worldsradio.com/country/fo) | `https://stream-secure.midlar.fo/fm1-128` | catalog duplicate | Already cataloged |
| Norðlýsið | Faroe Islands; local service | Faroese / news and local | [Faroese listings](https://www.worldsradio.com/country/fo) | `https://liveradio.stream.fo/listen/nordlysid/web` | catalog duplicate | Already cataloged |
| VoxPop | Faroe Islands; local popular-music service | Faroese / pop | [Faroese listings](https://www.worldsradio.com/country/fo) | `https://stream-secure.midlar.fo/voxpop-128` | catalog duplicate | Already cataloged |
| Aldan: Hitt Radio | Faroe Islands; online/local service | Faroese / hits | [Faroese listings](https://www.worldsradio.com/country/fo) | `https://streaming.radio.co/s4d14b9fcc/listen` | catalog duplicate | Already cataloged |

Remaining leads: KVF/Útvarp Føroya direct variants, Rás 2, Sjey Christian Radio, Lindin, FM1 genre variants, Stream.fo and local island/community services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Faroe Islands search. Next scheduled country: Fiji (`FJ`).

<a id="run-0073-fk"></a>
### Run 0073 — FK — Falkland Islands — 2026-09-09T22:40:00Z

- Start/end: 2026-09-09T22:40:00Z–2026-09-09T22:53:31Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. [Falklands Radio](https://radio.co.fk/) supplied local identity and community programming; the [Falkland Islands Government MiPlayer page](https://www.gov.fk/commercialservices/tv-and-radio/miplayer/) and [BFBS Falklands](https://www.bfbs.com/radio/stations/bfbs-falklands) provided official online listening evidence.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0073-FK-inputs.json) and [probes](research/run-0073-FK-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Falklands Radio 530 Stanley | Stanley, Falkland Islands; local service | English / news and community | [Falklands Radio](https://radio.co.fk/) | `https://streaming.broadcastradio.com:8332/flklnd` | catalog duplicate | Already cataloged |
| Falklands Radio | Falkland Islands; local service | English / pop and community | [Falklands Radio](https://radio.co.fk/) | `https://streaming.broadcastradio.com:8330/flklnd` | catalog duplicate | Already cataloged |
| BFBS Falklands | Falkland Islands; official BFBS local station | English / forces and pop | [BFBS](https://www.bfbs.com/radio/stations/bfbs-falklands) | `https://listen-ssvcbfbs.sharp-stream.com/ssvcbfbs6.aac` | catalog duplicate | Already cataloged |
| Falklands Radio alternate endpoint | Falkland Islands; same local service | English / community | [Falklands Radio](https://radio.co.fk/) | `https://streaming.broadcastradio.com:8332/flklnd?1721893143541=` | catalog duplicate | Already cataloged |

Remaining leads: Falklands Radio program-specific streams, BFBS Radio 1/2 variants, local emergency/community announcements and any short-lived internet-only services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Falkland Islands search. Next scheduled country: Faroe Islands (`FO`).

<a id="run-0072-et"></a>
### Run 0072 — ET — Ethiopia — 2026-09-09T21:40:00Z

- Start/end: 2026-09-09T21:40:00Z–2026-09-09T21:53:31Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Amharic-oriented terms. [Ahadu Radio](https://www.ahaduradio.com/), [Sheger FM](https://www.shegerfm.com/) and EBC's digital-platform announcement supplied primary station identity; Tuninga, Streema and Radio Ethiopia directories supplied broader discovery.
- Evaluated 4 candidate stream inputs; 3 were catalog duplicates and 1 required verification after a bounded URL probe, so 0 ready candidates were added. Raw results: [inputs](research/run-0072-ET-inputs.json) and [probes](research/run-0072-ET-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Ethio FM 107.8 | Addis Ababa, Ethiopia; station directory identity | Amharic / music and talk | [Tuninga Addis](https://tuningaradio.com/en/stations/ethiopia/addis-ababa/) | `https://stream.zeno.fm/72y045deqeruv` | catalog duplicate | Already cataloged |
| Sheger FM 102.1 | Addis Ababa, Ethiopia; official site | Amharic / news and entertainment | [Sheger FM](https://www.shegerfm.com/) | `https://stream.zenolive.com/y91n1vtbaw5tv` | catalog duplicate | Already cataloged |
| Ahadu Radio 94.3 | Addis Ababa, Ethiopia; official site | Amharic / news and talk | [Ahadu Radio](https://www.ahaduradio.com/) | `https://stream-155.zeno.fm/txxpndf1wwzuv` | unsafe/unresolvable (catalog URL has expiring token) | Needs refreshed direct endpoint |
| EBC Radio 104.7 | Addis Ababa, Ethiopia; EBC public broadcaster | Amharic / public news | [EBC](https://www.ebc.et/english/Home/NewsDetails?NewsId=528) | `https://stream-25.zeno.fm/2xguamap7yzuv` | catalog duplicate | Already cataloged |

Remaining leads: Fana Broadcasting, EBC regional services, Bisrat FM, FM Addis, Jano FM, TIRITA, Walta Radio, Mirt Internet Radio, Oromo/Afar/Somali-language services and community stations outside Addis Ababa. The run stopped at the four-minute ceiling; it did not claim an exhaustive Ethiopia search. Next scheduled country: Falkland Islands (`FK`).

<a id="run-0071-sz"></a>
### Run 0071 — SZ — Eswatini — 2026-09-09T20:40:00Z

- Start/end: 2026-09-09T20:40:00Z–2026-09-09T20:53:31Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. [ESCCOM](https://esccom.org.sz/broadcasting/) provided regulatory/broadcasting context; RadioDirectory identified official EBIS and online BremaFM/Blue Sky FM pages; JeleleFM supplied an online station lead.
- Evaluated 4 candidate page inputs; all failed the HTTPS/audio probe as unsafe or unresolvable, so 0 ready candidates were added. Raw results: [inputs](research/run-0071-SZ-inputs.json) and [probes](research/run-0071-SZ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| EBIS Radio 1/2 | Eswatini; official national broadcasting service | English/siSwati / public radio | [EBIS](https://ebis.co.sz/) | `https://ebis.co.sz/` | unsafe/unresolvable | Needs direct audio endpoint |
| JeleleFM | Eswatini; online station branding | English/siSwati / music | [JeleleFM](https://radio.jelele.com/) | `https://radio.jelele.com/` | unsafe/unresolvable | Needs direct audio endpoint |
| BremaFM | Manzini, Eswatini; directory identity | English / general | [RadioDirectory](https://radiodirectory.com/Radio_Stations/Africa/Eswatini/index.html) | `https://zeno.fm/radio/bremafm/` | unsafe/unresolvable | Player page only |
| Blue Sky FM Ambient | Eswatini-associated online station | ambient/world/tribal | [RadioDirectory](https://radiodirectory.com/Radio_Stations/Africa/Eswatini/index.html) | `https://zeno.fm/radio/blue-sky-fm-ambient/` | unsafe/unresolvable | Player page only |

Remaining leads: EBIS Radio 1/2 direct streams, Voice of the Church, TWR Africa, Hero Radio Swaziland, LRCM Radio, Antenna Web Mbabane, JeleleFM direct audio and community broadcasters. The run stopped at the four-minute ceiling; it did not claim an exhaustive Eswatini search. Next scheduled country: Ethiopia (`ET`).

<a id="run-0070-ee"></a>
### Run 0070 — EE — Estonia — 2026-09-09T19:40:00Z

- Start/end: 2026-09-09T19:40:00Z–2026-09-09T19:52:30Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Estonian. [ERR Vikerraadio](https://vikerraadio.err.ee/) supplied primary public-broadcaster identity; Sky Plus and Estonia station directories supported commercial and regional discovery.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0070-EE-inputs.json) and [probes](research/run-0070-EE-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Vikerraadio | Tallinn/Estonia; ERR public service | Estonian / news and culture | [ERR Vikerraadio](https://vikerraadio.err.ee/) | `https://icecast.err.ee/vikerraadio.mp3` | catalog duplicate | Already cataloged |
| ERR Raadio 4 | Estonia; ERR Russian-language service | Russian / news and talk | [ERR](https://vikerraadio.err.ee/) | `https://icecast.err.ee/raadio4.mp3?type=.mp3/;stream.mp3` | catalog duplicate | Already cataloged |
| MyHits | Estonia; commercial station directory | Estonian / pop | [Raadiod.com](https://raadiod.com/) | `https://router.euddn.net/8103046e16b71d15d692b57c187875c7/myhits.aac` | catalog duplicate | Already cataloged |
| Star FM Eesti | Estonia; commercial station directory | Estonian / adult contemporary | [Radio Eesti](https://radio-eesti.com/) | `https://ice.leviracloud.eu/starFMEesti96-aac` | catalog duplicate | Already cataloged |

Remaining leads: ERR Raadio 2, Klassikaraadio, Raadio Tallinn, Raadio Kuku, Raadio Elmar, Sky Plus, Rock FM, Retro FM, Duo Rock, Võmba FM, Russian-language DFM and local/community stations. The run stopped at the four-minute ceiling; it did not claim an exhaustive Estonia search. Next scheduled country: Eswatini (`SZ`).

<a id="run-0069-er"></a>
### Run 0069 — ER — Eritrea — 2026-09-09T18:40:00Z

- Start/end: 2026-09-09T18:40:00Z–2026-09-09T18:51:00Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Tigrinya/Arabic-oriented terms. Radio Erena, MaEzer Semay, TingFM and radio directories supplied diaspora and community leads; sources note that little Eritrean radio streams live online. No direct public audio endpoint was found beyond the existing music stream.
- Evaluated 4 candidate inputs; 1 was already in the catalog and 3 page inputs failed the HTTPS/audio probe, so 0 ready candidates were added. Raw results: [inputs](research/run-0069-ER-inputs.json) and [probes](research/run-0069-ER-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Eritrean/Ethiopian music | Eritrea-associated online service; catalog identity | Tigrinya/Amharic / music | [catalog baseline](../website/public/data/catalog.json) | `https://linuxfreelancer.com:8443/test.mp3` | catalog duplicate | Already cataloged |
| Radio Erena | Eritrean diaspora broadcaster serving Eritrea | Tigrinya/Arabic / news | [Radio Erena](https://linktr.ee/radioerena) | `https://linktr.ee/radioerena` | unsafe/unresolvable | Needs direct audio endpoint |
| MaEzer Semay Broadcasting Network | Eritrean community ministry | Tigrinya/English / Christian | [MaEzer Semay](https://maezersemay.org/) | `https://maezersemay.org/` | unsafe/unresolvable | Needs direct audio endpoint |
| Hero Radio (Eritrea) | Eritrea-associated online service | Tigrinya / gospel | [TingFM](https://tingfm.com/radio/88654) | `https://www.tingfm.com/radio/88654` | unsafe/unresolvable | Directory/player page only |

Remaining leads: Dimtsi Hafash/Voice of the Broad Masses, Radio Zara, Radio Erena direct player, Hero Radio direct audio, MaEzer Semay stream, and other Tigrinya, Arabic, Tigre, Afar and diaspora services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Eritrea search. Next scheduled country: Estonia (`EE`).

<a id="run-0068-gq"></a>
### Run 0068 — GQ — Equatorial Guinea — 2026-09-09T17:40:00Z

- Start/end: 2026-09-09T17:40:00Z–2026-09-09T17:50:30Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Spanish. The [Ministry of Information radio directorate](https://minfopressyculturage.com/direccion-general-de-la-radio/) identifies Radio Nacional/Radio Malabo; RadioDirectory, Tissef and Rádios Lusófonas supplied discovery. No direct public audio endpoint was exposed.
- Evaluated 4 candidate page inputs; all failed the HTTPS/audio probe as unsafe or unresolvable, so 0 ready candidates were added. Raw results: [inputs](research/run-0068-GQ-inputs.json) and [probes](research/run-0068-GQ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio Nacional de Guinea Ecuatorial / Radio Malabo | Malabo, Equatorial Guinea; ministry directorate | Spanish / national news and talk | [Ministry radio directorate](https://minfopressyculturage.com/direccion-general-de-la-radio/) | `https://minfopressyculturage.com/direccion-general-de-la-radio/` | unsafe/unresolvable | Needs direct audio endpoint |
| Asonga Radio | Malabo, Equatorial Guinea; station directory listing | Spanish / general | [RadioDirectory](https://radiodirectory.com/Radio_Stations/Africa/Equatorial_Guinea/index.html) | `https://radiodirectory.com/Radio_Stations/Africa/Equatorial_Guinea/index.html` | unsafe/unresolvable | Directory only |
| Radio María Guinea Ecuatorial | Equatorial Guinea; official `.gq` site | Spanish / Catholic | [Radio María](https://www.radiomaria.gq/) | `https://www.radiomaria.gq/` | unsafe/unresolvable | Needs direct audio endpoint |
| Equatoguinean online directory leads | Malabo/Bata and online services | mixed / gospel and community | [Rádios Lusófonas](https://radios-lusofonas.com/en/radio-stations/equatorial-guinea/) | `https://radios-lusofonas.com/en/radio-stations/equatorial-guinea/` | unsafe/unresolvable | Directory only |

Remaining leads: Radio Bata, national FM relays, Hero Radio, Guiné Equatorial Live, La Voz De Los Sin Voz, Antenna Web Malabo and Radio Cristiana Guinea Ecuatorial. The run stopped at the four-minute ceiling; it did not claim an exhaustive Equatorial Guinea search. Next scheduled country: Eritrea (`ER`).

<a id="run-0067-sv"></a>
### Run 0067 — SV — El Salvador — 2026-09-09T16:40:00Z

- Start/end: 2026-09-09T16:40:00Z–2026-09-09T16:49:30Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Spanish. [Radios El Salvador](https://www.radioselsalvador.org/) and [EmisorasElSalvador](https://emisoraselsalvador.com/) supplied national station discovery; an academic station profile and catalog identity supported YSKL/YSUCA/ABC/Bautista provenance.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0067-SV-inputs.json) and [probes](research/run-0067-SV-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio YSKL 104.1 FM | San Salvador, El Salvador; national station profile | Spanish / news and sport | [Radios El Salvador](https://www.radioselsalvador.org/) | `https://media.dominiocreativo.com:8000/stream/1/` | catalog duplicate | Already cataloged |
| Radio YSUCA 91.7 FM | San Salvador, El Salvador; university/cultural station | Spanish / news and culture | [Radios El Salvador](https://www.radioselsalvador.org/) | `https://fast.citrus3.com:8314/stream` | catalog duplicate | Already cataloged |
| ABC 100.1 | El Salvador; national listing | Spanish / pop | [EmisorasElSalvador](https://emisoraselsalvador.com/) | `https://streaming.rcs.com.sv/proxy/abc/stream` | catalog duplicate | Already cataloged |
| Radio Bautista | El Salvador; local religious station listing | Spanish / Christian | [Radios El Salvador](https://www.radioselsalvador.org/) | `https://s2.radio.co/s3a7dc3d82/listen` | catalog duplicate | Already cataloged |

Remaining leads: Radio Nacional El Salvador, Cadena Cuscatlán, FM Globo, Scan, Radio Chaparrastique, Exa, Radio María, Radio Sonora, Radio Astral, Radio Guazapa, indigenous/community stations, and departmental services outside San Salvador. The run stopped at the four-minute ceiling; it did not claim an exhaustive El Salvador search. Next scheduled country: Equatorial Guinea (`GQ`).

<a id="run-0066-eg"></a>
### Run 0066 — EG — Egypt — 2026-09-09T15:40:00Z

- Start/end: 2026-09-09T15:40:00Z–2026-09-09T15:49:29Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Arabic-oriented terms. [Radio Egypt](https://radio-egypt.com/) and [Egyptradio.net](https://egyptradio.net/) provided Egyptian station discovery; the official [El Radio 9090 site](https://www.9090.fm/) and catalog identity were checked for major Cairo services.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0066-EG-inputs.json) and [probes](research/run-0066-EG-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio 9090 90.9 | Cairo, Egypt; official site and directory identity | Arabic / pop and talk | [El Radio 9090](https://www.9090.fm/) | `https://9090streaming.mobtada.com/9090FMEGYPT` | catalog duplicate | Already cataloged |
| Nogoum FM | Cairo, Egypt; Egyptian station directory | Arabic / pop and entertainment | [Radio Egypt](https://radio-egypt.com/) | `https://stream-159.zeno.fm/qb1zvsykm98uv` | catalog duplicate | Already cataloged |
| NRJ Egypt | Cairo, Egypt; Egyptian station directory | Arabic/English / contemporary pop | [Egyptradio.net](https://egyptradio.net/) | `https://nrjstreaming.ahmed-melege.com/nrjegypt` | catalog duplicate | Already cataloged |
| 90s FM | Egypt; Egyptian internet-radio directory | Arabic / 1990s music | [Egyptradio.net](https://egyptradio.net/) | `https://eu1.fastcast4u.com/proxy/prontofm` | catalog duplicate | Already cataloged |

Remaining leads: ERTU public services, Quran FM Cairo, Mega FM, Nagham FM, Nile FM, ONsport FM, Radio Masrawy, Egyptian regional stations, Arabic religious services and Alexandria/Hurghada broadcasters. The run stopped at the four-minute ceiling; it did not claim an exhaustive Egypt search. Next scheduled country: El Salvador (`SV`).

<a id="run-0065-ec"></a>
### Run 0065 — EC — Ecuador — 2026-09-09T14:40:00Z

- Start/end: 2026-09-09T14:40:00Z–2026-09-09T14:49:59Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Spanish. Ecuadorian directories [Radios593](https://radios593.com/directorio.html), [Emisoras.ec](https://emisoras.ec/) and [Radio Ecuador](https://radioecuador.org/) supplied nationwide and provincial discovery; catalog identity was checked for Quito, Guayaquil and Santo Domingo services.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0065-EC-inputs.json) and [probes](research/run-0065-EC-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio La Otra 91.3 FM | Quito, Ecuador; Ecuador directory identity | Spanish / pop | [Radios593](https://radios593.com/directorio.html) | `https://laotrafm.makrodigital.com/stream/laotrafmquito` | catalog duplicate | Already cataloged |
| Radio América 104.5 FM | Ecuador; national directory identity | Spanish / general | [Emisoras.ec](https://emisoras.ec/) | `https://streamingecuador.com:7030/stream?1657848016283` | catalog duplicate | Already cataloged |
| Radio Zaracay 100.5 FM | Santo Domingo, Ecuador; provincial listing | Spanish / local music and news | [Radios593](https://radios593.com/directorio.html) | `https://stream-36.zeno.fm/as3xhhc0ts8uv?_=1` | catalog duplicate | Already cataloged |
| Los 40 Ecuador | Ecuador; national commercial service | Spanish / pop | [Radio Ecuador](https://radioecuador.org/) | `https://streamingecuador.com:7051/stream` | catalog duplicate | Already cataloged |

Remaining leads: Radio Pública Ecuador, HCJB, Radio Quito, Radio Sucre, Radio Centro, Radio Disney Ecuador, provincial community stations, indigenous/Kichwa services and the extensive online-only catalog. The run stopped at the four-minute ceiling; it did not claim an exhaustive Ecuador search. Next scheduled country: Egypt (`EG`).

<a id="run-0064-cd"></a>
### Run 0064 — CD — DR Congo — 2026-09-09T13:40:00Z

- Start/end: 2026-09-09T13:40:00Z–2026-09-09T13:48:29Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and French. [Radio Okapi](https://www.radiookapi.net/page/ecouter-radio-okapi-en-ligne) and the Congolese government [RTNC live page](https://communication.gouv.cd/live-rtnc) supplied primary national-broadcaster evidence; Tissef and drcongoradio directories supplied regional discovery.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0064-CD-inputs.json) and [probes](research/run-0064-CD-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Top Congo FM | Kinshasa, DR Congo; local directory identity | French / news and talk | [drcongoradio](https://drcongoradio.com/) | `https://topcongofm2.ice.infomaniak.ch/topcongofm2-64.mp3` | catalog duplicate | Already cataloged |
| Radio Mix Congolaise | DR Congo; online directory identity | French/Lingala / Congolese music | [Tissef DRC](https://tissef.com/democratic-republic-congo) | `https://stream.zeno.fm/qe5g83upga0uv` | catalog duplicate | Already cataloged |
| Gospel FM | Kinshasa, DR Congo; local directory identity | French/Lingala / gospel | [drcongoradio](https://drcongoradio.com/) | `https://stream.zeno.fm/n3sgwrm2mg8uv` | catalog duplicate | Already cataloged |
| Watoto Radio | DR Congo-associated online service | English/French / Christian | [Tissef DRC](https://tissef.com/democratic-republic-congo) | `https://stream-47.zeno.fm/xwx18us91k8uv?zs=D6hP5IeET_CVAjQuCUtmkg` | catalog duplicate | Already cataloged |

Remaining leads: RTNC/La Voix du Congo, Radio Okapi direct audio, Radio Maria Congo, Congo Planète Radio, Radio Ngoma, Radio Bendele, Radio Lisolo, Réveil FM, Radio Maendeleo and provincial stations in Goma, Bukavu, Lubumbashi and Kisangani. The run stopped at the four-minute ceiling; it did not claim an exhaustive DR Congo search. Next scheduled country: Ecuador (`EC`).

<a id="run-0063-do"></a>
### Run 0063 — DO — Dominican Republic — 2026-09-09T12:40:00Z

- Start/end: 2026-09-09T12:40:00Z–2026-09-09T12:48:59Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Spanish. Dominican directories [Radios 24x7](https://radios247.com/dominican-republic), [RadioTune](https://www.radiotune.fm/en-us/?region=dominican-republic) and the [Dominican Republic directory](https://www.dd.com.do/news-and-media/dominican-radio/) supplied national and city-level discovery; identity was cross-checked against catalog entries.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0063-DO-inputs.json) and [probes](research/run-0063-DO-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Ritmo 96.5 FM | Santo Domingo, Dominican Republic; directory and catalog identity | Spanish / tropical and pop | [RadioTune Dominican Republic](https://www.radiotune.fm/en-us/?region=dominican-republic) | `https://stream-49.zeno.fm/y0br5ck4ququv?zs=2R5Njz6XShSzNF_ProbdIA` | catalog duplicate | Already cataloged |
| Los 40 República Dominicana | Dominican Republic; national directory listing | Spanish / pop | [Radios 24x7](https://radios247.com/dominican-republic) | `https://stream.zeno.fm/sse58hcighnvv?dist=los40-web-live_streaming_play` | catalog duplicate | Already cataloged |
| Radio Cimarrona | Dominican Republic; local online service | Spanish / community | [Dominican directory](https://www.dd.com.do/news-and-media/dominican-radio/) | `https://radiocimarrona.out.airtime.pro:8000/radiocimarrona_a` | catalog duplicate | Already cataloged |
| La Z101 FM | Santo Domingo, Dominican Republic; established news/talk service | Spanish / news and talk | [Dominican Republic directory](https://www.dd.com.do/news-and-media/dominican-radio/) | `https://streaming.z101digital.com/z101?cb=1779372229211` | catalog duplicate | Already cataloged |

Remaining leads: CDN Radio, Radio Monumental, Radio Cima, Radio Guarachita, Radio Dial, Radio Nacional Cristiana, Suave 107.3, Latina 104, regional Santiago and Puerto Plata stations, and the many online-only merengue, bachata and Christian services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Dominican Republic search. Next scheduled country: Ecuador (`EC`).

<a id="run-0062-dm"></a>
### Run 0062 — DM — Dominica — 2026-09-09T11:40:00Z

- Start/end: 2026-09-09T11:40:00Z–2026-09-09T11:47:28Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English. [Voice of Life Radio](https://voiceofliferadio.dm/) and [Dominica Catholic Radio](https://dominicacatholicradio.org/) provided primary station identity; MyTuner and the Dominica directory supplied frequency and national-station context.
- Evaluated 5 candidate stream inputs; all 5 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0062-DM-inputs.json) and [probes](research/run-0062-DM-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| DBS Radio | Dominica; national government-owned station | English / general | [Dominica directory](https://thedominican.net/broadcasts.htm) | `https://stream.dbcradio.net:8005/live` | catalog duplicate | Already cataloged |
| Fabulosa 96.7 | Dominica; local FM listing | English / music | [MyTuner Dominica](https://mytuner-radio.com/radio/country/dominica-stations/frequency/fm) | `https://bostonstreaminge.net/8006/stream` | catalog duplicate | Already cataloged |
| Dominica Catholic Radio 96.1 | Roseau/Dominica; official station site | English / Catholic programming | [Dominica Catholic Radio](https://dominicacatholicradio.org/) | `https://cdn.comeseetv.com:8010/dominicacatholicradio?1740579480509` | catalog duplicate | Already cataloged |
| Voice of Life Radio | Dominica; official station site and FM broadcast | English / Christian and gospel | [Voice of Life](https://voiceofliferadio.dm/) | `https://cdn.comeseetv.com:8000/vol` | catalog duplicate | Already cataloged |
| En Ba Mango | Dominica; local FM listing | English / local music | [MyTuner Dominica](https://mytuner-radio.com/radio/country/dominica-stations/frequency/fm) | `https://s10.myradiostream.com/:4212/listen.mp3` | catalog duplicate | Already cataloged |

Remaining leads: Kairi FM, Q95/WICE QFM, My Worship FM, Portsmouth and community stations, and any new internet-only services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Dominica search. Next scheduled country: Dominican Republic (`DO`).

<a id="run-0061-dj"></a>
### Run 0061 — DJ — Djibouti — 2026-09-09T10:40:00Z

- Start/end: 2026-09-09T10:40:00Z–2026-09-09T10:46:28Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and French. [RTD](https://rtd.dj/) confirms Radio Télévision de Djibouti as the national broadcaster and its direct page was reviewed; TuneAll, Online Radio Box and RadioSpinner supplied discovery leads. No primary stream URL was exposed in the bounded pass.
- Evaluated 4 candidate page inputs; all failed the HTTPS/audio probe as unsafe or unresolvable, so 0 ready candidates were added. Raw results: [inputs](research/run-0061-DJ-inputs.json) and [probes](research/run-0061-DJ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream/page URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio Djibouti / RTD | Djibouti; state broadcaster, Arabic/French/Somali/Afar services | Public radio | [RTD](https://rtd.dj/) | `https://rtd.dj/rtd-en-direct/` | unsafe/unresolvable | Needs direct audio endpoint |
| Djibouti directory leads | Djibouti-associated stations | mixed | [TuneAll](https://www.tuneallradio.com/country/djibouti) | `https://www.tuneallradio.com/country/djibouti` | unsafe/unresolvable | Directory only |
| Djibouti station directory | Djibouti listings including Antenna Web Gibuti and LRCM Radio | mixed | [Online Radio Box](https://onlineradiobox.com/dj/) | `https://onlineradiobox.com/dj/` | unsafe/unresolvable | Directory only |
| Hero Radio / regional leads | Djibouti-associated online stations | mixed | [RadioSpinner](https://radiospinner.com/dj/) | `https://radiospinner.com/dj/` | unsafe/unresolvable | Needs direct audio endpoint |

Remaining leads: RTD's embedded player/audio URL, Radio Djibouti domestic services, Hero Radio, Antenna Web Gibuti, LRCM Radio and any French, Somali or Afar community services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Djibouti search. Next scheduled country: Dominican Republic (`DO`).

<a id="run-0060-dk"></a>
### Run 0060 — DK — Denmark — 2026-09-09T09:40:00Z

- Start/end: 2026-09-09T09:40:00Z–2026-09-09T09:46:28Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Danish. [DR's transmitter page](https://portal.rozhlas.cz/vysilace/vysilace) was not applicable to Denmark; the Danish discovery sources [radio.dk](https://www.radio.dk/country/denmark), [dabplus.live](https://dabplus.live/dk?lang=en) and [FreqTrail](https://www.freqtrail.com/stations/DK) identified national and local streams, with DR and Radio Alfa identity cross-checked against catalog entries.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0060-DK-inputs.json) and [probes](research/run-0060-DK-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| DR P3 | Denmark; Danmarks Radio public service | Danish / pop and current affairs | [FreqTrail Denmark](https://www.freqtrail.com/stations/DK) | `https://live-icy.dr.dk/A/A05H.mp3` | catalog duplicate | Already cataloged |
| DR P1 | Denmark; Danmarks Radio public service | Danish / talk and news | [FreqTrail Denmark](https://www.freqtrail.com/stations/DK) | `https://live-icy.dr.dk/A/A03H.mp3` | catalog duplicate | Already cataloged |
| Nova FM | Denmark; Bauer Media Danish station | Danish / commercial pop | [FreqTrail Denmark](https://www.freqtrail.com/stations/DK) | `https://live-bauerdk.sharp-stream.com/nova_dk_mp3` | catalog duplicate | Already cataloged |
| Radio Alfa | Denmark; Danish local/national service listing | Danish / pop and talk | [dabplus.live Denmark](https://dabplus.live/dk?lang=en) | `https://radioserver.dk/alfa` | catalog duplicate | Already cataloged |

Remaining leads: DR P2/P4/P5/P6/P8, DR Nyheder, Radio4, The Voice, Radio Soft, Pop FM, Skala FM, Radio ABC, Radio Viborg, Radio Nordjyske, Radio Silkeborg, community and DAB-only services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Denmark search. Next scheduled country: Dominican Republic (`DO`).

<a id="run-0059-cz"></a>
### Run 0059 — CZ — Czechia — 2026-09-09T08:40:00Z

- Start/end: 2026-09-09T08:40:00Z–2026-09-09T08:46:58Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Czech. [Czech Radio's transmitter page](https://portal.rozhlas.cz/vysilace/vysilace) provided public-service station identity and online stream references; [ČTÚ's transmitter database](https://ctu.gov.cz/vyhledavaci-databaze/prehled-rozhlasovych-vysilacu/) supported national frequency identity; [Radio Wave](https://wave.rozhlas.cz/o-stanici-5675004) confirmed continuous online service.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0059-CZ-inputs.json) and [probes](research/run-0059-CZ-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| ČRo Radiožurnál | Czechia; Czech Radio public-service network | Czech / news and general | [Czech Radio](https://portal.rozhlas.cz/vysilace/vysilace) | `https://icecast8.play.cz/cro1-128.mp3` | catalog duplicate | Already cataloged |
| ČRo Dvojka | Czechia; Czech Radio public-service network | Czech / talk and culture | [Czech Radio](https://portal.rozhlas.cz/vysilace/vysilace) | `https://icecast6.play.cz/cro2-128.mp3` | catalog duplicate | Already cataloged |
| ČRo Vltava | Czechia; Czech Radio public-service network | Czech / culture and classical | [Czech Radio](https://portal.rozhlas.cz/vysilace/vysilace) | `https://icecast5.play.cz/cro3-128.mp3` | catalog duplicate | Already cataloged |
| Rock Radio | Czechia; national commercial network listing | Czech / rock | [FM-RADIO Czechia](https://fm-radio.live/czechia) | `https://playerservices.streamtheworld.com/api/livestream-redirect/ROCK_RADIO_128.mp3` | catalog duplicate | Already cataloged |

Remaining leads: Radio Wave, Plus, D-dur, Jazz, Junior, Rádio Praha, regional Czech Radio services, Country Radio, Evropa 2, Frekvence 1, Fajn Rádio, Radio 1, Expres FM and local/community stations. The run stopped at the four-minute ceiling; it did not claim an exhaustive Czechia search. Next scheduled country: Côte d’Ivoire (`CI`).

<a id="run-0058-cy"></a>
### Run 0058 — CY — Cyprus — 2026-09-09T07:40:00Z

- Start/end: 2026-09-09T07:40:00Z–2026-09-09T07:45:28Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Greek-oriented terms. The [Cyprus government media directory](https://www.gov.cy/pio/mme/katalogos-mme-praktoreion-2/pagkyprioi-radiostathmoi/) provided official station identity; [Cyprus Radio Stations](https://www.cyprusradiostations.com/) and [Radio-Cyprus](https://radio-cyprus.com/stations) supplied discovery lists; [Radio Sfera](https://sfera.com.cy/) was checked as a station site.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0058-CY-inputs.json) and [probes](research/run-0058-CY-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Diesi Cyprus 101.1 | Cyprus; catalog identity and local directory | Greek / pop and ballads | [Cyprus Radio Stations](https://www.cyprusradiostations.com/) | `https://r1.cloudskep.com/radio/diesi/icecast.audio` | catalog duplicate | Already cataloged |
| Trito Live (CyBC) | Cyprus; public broadcaster stream identity | Greek / public-service culture | [Cyprus Radio Stations](https://www.cyprusradiostations.com/) | `https://r1.cloudskep.com/cybcr/cybc3/icecast.audio` | catalog duplicate | Already cataloged |
| Active 107.4 | Cyprus; official government media directory | Greek / contemporary | [Cyprus government directory](https://www.gov.cy/pio/mme/katalogos-mme-praktoreion-2/pagkyprioi-radiostathmoi/) | `https://securestreams3.autopo.st:1417/active` | catalog duplicate | Already cataloged |
| Radio Sfera 102.2 | Cyprus; official Sfera site and local directory | Greek / pop | [Radio Sfera](https://sfera.com.cy/) | `https://securestreams3.autopo.st:1417/sfera` | catalog duplicate | Already cataloged |

Remaining leads: Proto, Tetarto, Super Sport FM, Mix FM, Dance FM, Zenith, KISS FM, Cool Radio, VIVA FM, Cyprus Chinese Radio, Russian Radio Cyprus, Rock FM, Radio ReyMod, Radio T.O.A., Sport FM, Politis 107.6, Radio Turbo21, stations in Northern Cyprus, and BFBS services on sovereign bases. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cyprus search. Next scheduled country: Czechia (`CZ`).

<a id="run-0057-cw"></a>
### Run 0057 — CW — Curaçao — 2026-09-09T06:40:00Z

- Start/end: 2026-09-09T06:40:00Z–2026-09-09T06:44:27Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Dutch/Papiamentu-oriented terms. The [Curaçao Film Office local-media directory](https://curacaofilmoffice.com/about-us/local-media) lists local stations and frequencies; [Brien's Curaçao Radio Guide](https://www.caribbean-radio.com/country/curacao.html) supplies stream/listening coverage; official pages for [Radio Mas99](https://www.mas99.cw/) and [Dolfijn](https://dolfijngo.com/radio/) were also reviewed.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0057-CW-inputs.json) and [probes](research/run-0057-CW-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio Mas 99.7 FM | Curaçao; local-media directory and `.cw` site | Papiamentu / local music and talk | [Radio Mas99](https://www.mas99.cw/) | `https://kadushi.westream.cloud/listen/mas99/live` | catalog duplicate | Already cataloged |
| Radio Active 104.5 FM | Curaçao; local-media directory | Local / contemporary | [Curaçao Film Office](https://curacaofilmoffice.com/about-us/local-media) | `https://kadushi.westream.cloud/listen/radioactive/RadioActive` | catalog duplicate | Already cataloged |
| Paradise FM 103.1 | Curaçao; local-media directory | Dutch/Papiamentu / pop | [Curaçao Film Office](https://curacaofilmoffice.com/about-us/local-media) | `https://stream.paradisefm.cw/ParadiseFM` | catalog duplicate | Already cataloged |
| Dolfijn FM 97.3 | Curaçao; local-media directory and Dolfijn online page | Dutch/Papiamentu / pop and hits | [Dolfijn](https://dolfijngo.com/radio/) | `https://radiostreamfm.com:8130/radio.mp3` | catalog duplicate | Already cataloged |

Remaining leads: Z86 Radio, 88 RocKòrsou, Curaçao News Radio, Radio Krioyo, Telecuracao FM, Korsou FM, Radio 94 Korsou, Clazz FM, Radio Mi 95, Radio New Song, Easy FM, Radio Semiya, Radio Lighthouse, Laser 101, Radio Hoyer 1/2, Fiesta FM and Rumbera Network. The run stopped at the four-minute ceiling; it did not claim an exhaustive Curaçao search. Next scheduled country: Cyprus (`CY`).

<a id="run-0056-cu"></a>
### Run 0056 — CU — Cuba — 2026-09-09T05:40:00Z

- Start/end: 2026-09-09T05:40:00Z–2026-09-09T05:44:27Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in Spanish and English. Primary/identity evidence included [Domiplay Cuba](https://domiplay.net/en/country/cuba) and [Directorio Cubano](https://www.directoriocubano.info/en/radio/) lists of 80–100 live Cuban stations, plus [Radio Progreso](https://www.radioscuba.com/radio-progreso) identifying its national 24/7 broadcast from La Habana.
- Evaluated 4 candidate stream inputs; all 4 already exist in the catalog, so 0 new ready candidates were added. Raw results: [inputs](research/run-0056-CU-inputs.json) and [probes](research/run-0056-CU-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
|---|---|---|---|---|---|---|
| Radio Habana Cuba 102.5 FM | Cuba; catalog identity | Spanish / public radio | [catalog](../website/public/data/catalog.json) | `https://securestreams7.autopo.st/?uri=https://icecast.teveo.cu/McW3fLhs` | catalog duplicate | Already cataloged |
| Radio Rebelde 1180 AM | Cuba; catalog identity | Spanish / news and music | [catalog](../website/public/data/catalog.json) | `https://securestreams7.autopo.st/?uri=https://icecast.teveo.cu/kHKL7tWd` | catalog duplicate | Already cataloged |
| Radio Reloj Cuba 950 AM | Cuba; catalog identity | Spanish / news and time service | [catalog](../website/public/data/catalog.json) | `https://securestreams7.autopo.st/?uri=https://icecast.teveo.cu/b3jbfThq` | catalog duplicate | Already cataloged |
| Radio Progreso 90.3 FM | La Habana, Cuba; national 24/7 evidence | Spanish / music, drama, news and culture | [Radio Progreso](https://www.radioscuba.com/radio-progreso) | `https://securestreams7.autopo.st/?uri=https://icecast.teveo.cu/XjfW7qWN` | catalog duplicate | Already cataloged |

Remaining leads: Radio Taíno, Radio Enciclopedia, CMBF Radio Musical Nacional, Radio Cadena Agramonte, Radio Bayamo, Radio Ciudad del Mar, Radio Mayabeque, local provincial stations and independent online services. The run stopped at the four-minute ceiling; it did not claim an exhaustive Cuba search. Next scheduled country: Curaçao (`CW`).

<a id="run-0029-bw"></a>
### Run 0029 — BW — Botswana — 2026-09-08T02:20:00Z

- Start/end: 2026-09-08T02:20:00Z–2026-09-08T02:24:21Z. Sweep 1. Final status: **partial**.
- Search scope: six queries in English and Setswana. Primary sources included [University of Botswana Radio](https://www.ub.bw/ub-radio-home?page=1), [BOCRA broadcasting information](https://www.bocra.org.bw/broadcasting-0), [Duma FM](https://dumafm.co.bw/) and [Talk BW](https://talk.co.bw/). UB Radio documents FM and online service; BOCRA identifies Yarona, Duma and Gabz FM as commercial stations.
- Evaluated 4 candidate homepage/listen endpoints; 0 ready and 4 need verification because the bounded HTTPS probe could not resolve them. Raw results: [inputs](research/run-0029-BW-inputs.json) and [probes](research/run-0029-BW-probes.json).

| Station / service | Location / country evidence | Language / genre | Official site / source | Stream URL | Probe result | Disposition / reason |
| --- | --- | --- | --- | --- | --- | --- |
| UB Radio | University of Botswana; Gaborone, Francistown and Maun frequencies | urban hits/youth; Setswana/English | [University of Botswana](https://www.ub.bw/ub-radio-home?page=1) | `https://radio.ub.bw` | DNS/address check failed | needs verification; locate direct audio endpoint |
| Talk BW | Botswana station identity on official site | talk/music | [Talk BW](https://talk.co.bw/) | `https://talk.co.bw` | DNS/address check failed | needs verification |
| Duma FM | Botswana private station identity on official site | news/community/music | [Duma FM](https://dumafm.co.bw/) | `https://dumafm.co.bw` | DNS/address check failed | needs verification |
| Mass Media Botswana / Radio Botswana lead | Botswana media source | public radio lead | [Mass Media Botswana](https://massmedia.co.bw/) | `https://www.massmedia.co.bw/` | DNS/address check failed | needs verification; identify direct radio service |

Remaining leads: Radio Botswana 1/2, Yarona FM, Gabz FM, community licences and direct player URLs from UB Radio and Duma FM. The run stopped at the four-minute ceiling; it did not claim an exhaustive Botswana search. Next scheduled country: Bouvet Island (`BV`).

<a id="run-0030-bv"></a>
### Run 0030 — BV — Bouvet Island — 2026-09-08T03:21:00Z

- Start/end: 2026-09-08T03:21:00Z–2026-09-08T03:25:51Z. Sweep 1. Final status: **searched**.
- Search scope: six queries in English and Norwegian. Results concerned amateur-radio expeditions, weather or maritime communications; no locally operated online broadcast station or public audio stream was identified. The [3Y0K expedition site](https://3y0k.com/) and Norwegian radio references are not station candidates.
- Evaluated 0 candidate stream inputs; 0 ready, 0 already present, 0 needs verification. Raw empty input/probe records: [inputs](research/run-0030-BV-inputs.json), [probes](research/run-0030-BV-probes.json).

Bouvet Island is an uninhabited Norwegian dependency. This is a documented coverage search, not a claim that no future expedition stream could exist. Remaining lead: revisit only if a future expedition advertises a public audio broadcast. Next scheduled country: Brazil (`BR`).
<a id="run-0117-ke"></a>
### Run 0117 — Kenya (`KE`)

- **Completed:** 2026-09-11T22:45:38Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English/Swahili queries using Kenyan radio directories, official broadcasters, and community-radio sources; ten existing catalog inputs were checked.
- **Candidate review:** Kameme FM, JESUS IS LORD radio, Taach FM, ghetto kenya, Radio47, GHETTOO KENYA, At254 Radio, Juja FM, Radio Generation Kenya 88.8, and KBC all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0117-KE-inputs.json), [probes](research/run-0117-KE-probes.json).
- **Remaining leads:** Radio.co.ke and RadioLive.ke directories expose additional national and community stations requiring direct endpoint verification.
- **Next scheduled country:** Kenya (`KE`) for follow-up because unresolved leads remain.
<a id="run-0118-ke"></a>
### Run 0118 — Kenya (`KE`)

- **Completed:** 2026-09-11T23:45:47Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries followed up on Kenyan national and community-radio leads. The ten-stream verification cap was already consumed by Run 0117, so no additional stream probes were issued.
- **Candidate review:** Radio Kaya, Simbanest Radio, Mutongoi FM, Radio Citizen, Hali Radio, Radio Maisha, and directory listings produced identity evidence but no new stream endpoint that could be safely verified within this run.
- **Remaining leads:** obtain direct HTTPS audio endpoints for Radio Kaya, Simbanest, Mutongoi, Radio Citizen, Hali Radio, and other directory listings during a later sweep.
- **Next scheduled country:** Kenya (`KE`) for follow-up because unresolved leads remain.
<a id="run-0119-ki"></a>
### Run 0119 — Kiribati (`KI`)

- **Completed:** 2026-09-12T00:45:47Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries across official BPA, Pacific broadcasters, and radio directories; one candidate endpoint was checked.
- **Candidate review:** BPA Radio Kiribati identifies AM 1440 and FM 89.9 streams, but the public page URL did not resolve as a safe direct audio endpoint. Existing Radio Kiribati catalog coverage remains unchanged. Raw evidence: [inputs](research/run-0119-KI-inputs.json), [probes](research/run-0119-KI-probes.json).
- **Remaining leads:** extract and verify the BPA page’s embedded AM/FM audio URLs in a later sweep.
- **Next scheduled country:** Kosovo (`XK`).
<a id="run-0120-xk"></a>
### Run 0120 — Kosovo (`XK`)

- **Completed:** 2026-09-12T01:45:48Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Albanian/English queries using Kosovo station directories and official broadcaster pages; six existing catalog streams were checked.
- **Candidate review:** KLAN Kosova FM, Radio Zëri i Shtimes, GlamRADIO, Urban FM 103.5, Kolektiv Radio, and Radyo Hisar all matched existing catalog entries. Directory leads such as Radio Kosova e Lire and Radio Maria Kosovo exposed HTTP-only endpoints or identity pages without a verified new HTTPS audio stream. Raw evidence: [inputs](research/run-0120-XK-inputs.json), [probes](research/run-0120-XK-probes.json).
- **Remaining leads:** verify HTTPS replacements for Radio Kosova e Lire, Radio Maria Kosovo, Radio Dukagjini, and other local stations.
- **Next scheduled country:** Kuwait (`KW`).
<a id="run-0121-kw"></a>
### Run 0121 — Kuwait (`KW`)

- **Completed:** 2026-09-12T02:46:48Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/English queries using Kuwait Ministry of Information references and radio directories; eight existing catalog streams were checked.
- **Candidate review:** all eight checked Quran Radio Kuwait feeds matched existing catalog entries. Ministry and directory sources identified Super Station, Marina FM, COKO Radio, and other services, but no new stable HTTPS audio endpoint was verified. Raw evidence: [inputs](research/run-0121-KW-inputs.json), [probes](research/run-0121-KW-probes.json).
- **Remaining leads:** verify direct HTTPS streams for Super Station, Marina FM, COKO Radio, and Radio Kuwait services.
- **Next scheduled country:** Kyrgyzstan (`KG`).
<a id="run-0122-kg"></a>
### Run 0122 — Kyrgyzstan (`KG`)

- **Completed:** 2026-09-12T03:46:48Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Kyrgyz/Russian/English queries using RadioPlayerKG, official station pages, and directories; six existing catalog streams were checked.
- **Candidate review:** Кыргызстан Обондору, ColdStar low/high, Radio Tumar FM, Биринчи Radio, and Сүйүнчү FM all matched existing catalog entries. Asia FM, Avtoradio, Мекендеш Радиосу, and Retro FM produced identity/stream leads but no newly verified candidate in this run. Raw evidence: [inputs](research/run-0122-KG-inputs.json), [probes](research/run-0122-KG-probes.json).
- **Remaining leads:** verify direct HTTPS endpoints for Asia FM, Avtoradio Bishkek, Мекендеш Радиосу, and Retro FM.
- **Next scheduled country:** Laos (`LA`).
<a id="run-0123-la"></a>
### Run 0123 — Laos (`LA`)

- **Completed:** 2026-09-12T04:47:18Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Lao/English queries using Lao National Radio references and regional radio directories; three existing catalog streams were checked.
- **Candidate review:** Lao National Radio 103.7, Lao National Radio 94.3, and Toki Pona Radio matched existing catalog entries. Asia/regional directories did not provide a newly verified HTTPS audio endpoint. Raw evidence: [inputs](research/run-0123-LA-inputs.json), [probes](research/run-0123-LA-probes.json).
- **Remaining leads:** verify FEBC Lao, MMK, and Vientiane/regional stations for stable HTTPS streams.
- **Next scheduled country:** Latvia (`LV`).
<a id="run-0124-lv"></a>
### Run 0124 — Latvia (`LV`)

- **Completed:** 2026-09-12T05:47:49Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Latvian/English queries using Latvijas Radio, Latvian station directories, and regulator listings; ten existing catalog streams were checked.
- **Candidate review:** all ten checked Latvian feeds matched existing catalog entries. Latvijas Radio 5 and directory listings identified additional services, but no new stable HTTPS audio endpoint was verified. Raw evidence: [inputs](research/run-0124-LV-inputs.json), [probes](research/run-0124-LV-probes.json).
- **Remaining leads:** verify Latvijas Radio network channels, NABA, Kurzemes Radio, and smaller regional stations.
- **Next scheduled country:** Lebanon (`LB`).
<a id="run-0125-lb"></a>
### Run 0125 — Lebanon (`LB`)

- **Completed:** 2026-09-12T06:48:49Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/English queries using Radio Liban, Ministry references, and Lebanese radio directories; ten existing catalog streams were checked.
- **Candidate review:** the ten checked Lebanese streams matched existing catalog entries. Directory evidence identified Nidaa FM, One FM, Radio Reve, Radio Maria Arabic, and others, but no new stable HTTPS endpoint was verified. Raw evidence: [inputs](research/run-0125-LB-inputs.json), [probes](research/run-0125-LB-probes.json).
- **Remaining leads:** verify direct HTTPS streams for Nidaa FM, One FM, Radio Reve, Radio Maria Arabic, and smaller regional services.
- **Next scheduled country:** Lesotho (`LS`).
<a id="run-0126-ls"></a>
### Run 0126 — Lesotho (`LS`)

- **Completed:** 2026-09-12T07:48:19Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Lesotho station sites, regulator listings, and directories; one existing catalog stream was checked.
- **Candidate review:** Radio Maria Lesotho matched the existing catalog. KEL Radio, PMR FM, Harvest FM, PC FM, Moafrika FM, and Mapholi FM were identified, but no new stable HTTPS audio endpoint was verified. Raw evidence: [inputs](research/run-0126-LS-inputs.json), [probes](research/run-0126-LS-probes.json).
- **Remaining leads:** extract and verify direct HTTPS streams from KEL Radio, PMR FM, Harvest FM, PC FM, Moafrika FM, and Mapholi FM.
- **Next scheduled country:** Liberia (`LR`).
<a id="run-0127-lr"></a>
### Run 0127 — Liberia (`LR`)

- **Completed:** 2026-09-12T08:48:49Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Liberian broadcaster pages, regulator/media sources, and station directories; no direct stream endpoint was safely available for probing.
- **Candidate review:** Liberia Broadcasting System/ELBC, Voice of Liberia, Liberia Tribune Radio, DVC Radio, Truth FM, HOTTFM, and community stations were identified, but no new stable HTTPS audio stream was verified. Raw evidence: [inputs](research/run-0127-LR-inputs.json), [probes](research/run-0127-LR-probes.json).
- **Remaining leads:** extract direct audio URLs from ELBC, Voice of Liberia, Liberia Tribune, DVC Radio, Truth FM, and HOTTFM pages.
- **Next scheduled country:** Libya (`LY`).
<a id="run-0128-ly"></a>
### Run 0128 — Libya (`LY`)

- **Completed:** 2026-09-12T09:49:50Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/English queries using Libyan station pages and directories; four existing catalog streams were checked.
- **Candidate review:** Radio Arts Tripoli, Hala Sabratha, and both Almunir Radio feeds matched existing catalog entries. Tripoli FM and Alwasat FM provided identity pages but no newly verified endpoint. Raw evidence: [inputs](research/run-0128-LY-inputs.json), [probes](research/run-0128-LY-probes.json).
- **Remaining leads:** verify Tripoli FM, Alwasat FM, Libyana Hits, and other local services for stable HTTPS streams.
- **Next scheduled country:** Liechtenstein (`LI`).
<a id="run-0129-li"></a>
### Run 0129 — Liechtenstein (`LI`)

- **Completed:** 2026-09-12T10:49:50Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted German/English queries using Radio Vaterland, Radio Liechtenstein, and local directories; one existing catalog stream was checked.
- **Candidate review:** Radio Vaterland matched the existing catalog. Radio Liechtenstein ceased live broadcasting in 2025; Radio 2Go and other directory leads did not expose a newly verified HTTPS audio endpoint. Raw evidence: [inputs](research/run-0129-LI-inputs.json), [probes](research/run-0129-LI-probes.json).
- **Remaining leads:** verify Radio 2Go’s current stream and any successor Radio Liechtenstein service.
- **Next scheduled country:** Lithuania (`LT`).
<a id="run-0130-lt"></a>
### Run 0130 — Lithuania (`LT`)

- **Completed:** 2026-09-12T11:50:20Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Lithuanian/English queries using Lithuanian radio directories, LRT references, and station pages; two candidate URLs were checked.
- **Candidate review:** PMR’s published MP3 URL was unsafe or unresolvable; Radio R matched the existing catalog. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0130-LT-inputs.json), [probes](research/run-0130-LT-probes.json).
- **Remaining leads:** verify PMR, LRT Radijas/Klasika/Opus, Radio Vilnius, and smaller regional services.
- **Next scheduled country:** Luxembourg (`LU`).
<a id="run-0131-lu"></a>
### Run 0131 — Luxembourg (`LU`)

- **Completed:** 2026-09-12T12:50:50Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/German/English queries using Luxembourg broadcaster pages, regulator listings, and directories; ten existing catalog streams were checked.
- **Candidate review:** all ten checked feeds matched existing catalog entries. L’essentiel, Radio ARA, Radio Puls, and other sources produced identity leads but no newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0131-LU-inputs.json), [probes](research/run-0131-LU-probes.json).
- **Remaining leads:** verify Radio ARA, Radio Puls, L’essentiel secondary feeds, and Luxembourg Global Radio.
- **Next scheduled country:** Macao (`MO`).
<a id="run-0132-mo"></a>
### Run 0132 — Macao (`MO`)

- **Completed:** 2026-09-12T13:51:20Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Portuguese/Chinese/English queries using TDM Macau references and radio directories; four existing catalog streams were checked.
- **Candidate review:** RTP Macau, Lotus FM Macau, YW City Radio, and Record FM all matched existing catalog entries. CityFM and M80 directory leads did not yield a new verified HTTPS stream in this run. Raw evidence: [inputs](research/run-0132-MO-inputs.json), [probes](research/run-0132-MO-probes.json).
- **Remaining leads:** verify CityFM Macau, M80 Radio Macau, and TDM’s Chinese/Portuguese channels for stable HTTPS endpoints.
- **Next scheduled country:** Madagascar (`MG`).
<a id="run-0133-mg"></a>
### Run 0133 — Madagascar (`MG`)

- **Completed:** 2026-09-12T14:51:21Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using Malagasy station pages and directories; eight existing catalog streams were checked.
- **Candidate review:** all eight checked Madagascar feeds matched existing catalog entries. RDJ, Radio Don Bosco, Tiako Be, and other directory leads lacked a newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0133-MG-inputs.json), [probes](research/run-0133-MG-probes.json).
- **Remaining leads:** verify RDJ, Radio Don Bosco, Tiako Be, and regional Malagasy stations for stable HTTPS streams.
- **Next scheduled country:** Malawi (`MW`).
<a id="run-0134-mw"></a>
### Run 0134 — Malawi (`MW`)

- **Completed:** 2026-09-12T15:51:51Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Malawian broadcaster and community-radio sources; seven existing catalog streams were checked.
- **Candidate review:** all seven checked feeds matched existing catalog entries. Lilongwe FM, Love FM, Yetu Radio, Mzimba Community Radio, and other sources identified additional services, but no new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0134-MW-inputs.json), [probes](research/run-0134-MW-probes.json).
- **Remaining leads:** verify Lilongwe FM, Love FM, Yetu Radio, Mzimba Community Radio, and MBC/Times Radio endpoints.
- **Next scheduled country:** Malaysia (`MY`).
<a id="run-0135-my"></a>
### Run 0135 — Malaysia (`MY`)

- **Completed:** 2026-09-12T16:52:21Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Malay/English queries using RTM and Malaysian station directories; two candidate endpoints were checked.
- **Candidate review:** Hot FM and RTM portal URLs were unsafe or unresolvable. Existing catalog coverage was not probed further in this run. Raw evidence: [inputs](research/run-0135-MY-inputs.json), [probes](research/run-0135-MY-probes.json).
- **Remaining leads:** extract direct HTTPS feeds from RTM Portal Radio, Hot FM, Astro Audio, and state services.
- **Next scheduled country:** Maldives (`MV`).
<a id="run-0136-mv"></a>
### Run 0136 — Maldives (`MV`)

- **Completed:** 2026-09-12T17:53:21Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Dhivehi/English queries using Public Service Media references and radio directories; three existing catalog streams were checked.
- **Candidate review:** Dhivehi Raajjeyge Adu, Dheenuge Adu, and Dhivehi FM matched existing catalog entries. Directory leads for VFM99, Sun FM, Capital Radio, and Radio Atoll did not yield newly verified HTTPS endpoints. Raw evidence: [inputs](research/run-0136-MV-inputs.json), [probes](research/run-0136-MV-probes.json).
- **Remaining leads:** verify VFM99, Sun FM, Capital Radio, Radio Atoll, and Voice of Maldives secondary channels.
- **Next scheduled country:** Mali (`ML`).
<a id="run-0137-ml"></a>
### Run 0137 — Mali (`ML`)

- **Completed:** 2026-09-12T18:53:52Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using ORTM, Mali regulator, and radio directories; ten existing catalog streams were checked.
- **Candidate review:** the ten checked Mali feeds matched existing catalog entries. ORTM, Radio Bamakan, Joliba FM, and other directories supplied identity leads without a newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0137-ML-inputs.json), [probes](research/run-0137-ML-probes.json).
- **Remaining leads:** verify ORTM services, Joliba FM, Radio Bamakan, and additional community stations.
- **Next scheduled country:** Malta (`MT`).
<a id="run-0138-mt"></a>
### Run 0138 — Malta (`MT`)

- **Completed:** 2026-09-12T19:55:22Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Maltese/English queries using Broadcasting Authority records and station directories; six existing catalog streams were checked.
- **Candidate review:** Bay Easy, 89.7 Bay, Campus 103.7, Calypso Radio, Bay 89.7, and MALTIN BISS matched existing catalog entries. One Radio and Radio 105 Malta leads did not yield a new verified HTTPS endpoint. Raw evidence: [inputs](research/run-0138-MT-inputs.json), [probes](research/run-0138-MT-probes.json).
- **Remaining leads:** verify One Radio, Radio 105 Malta, Radju Malta, and community stations such as Mics FM.
- **Next scheduled country:** Marshall Islands (`MH`).
<a id="run-0139-mh"></a>
### Run 0139 — Marshall Islands (`MH`)

- **Completed:** 2026-09-12T20:56:52Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Marshall Islands station references and directories; two existing catalog streams were checked.
- **Candidate review:** Offshore Radio and Offworld Radio matched existing catalog entries. V7AB/Radio Marshalls and Power 103.5 were identified, but available URLs were inactive or lacked a newly verified HTTPS audio endpoint. Raw evidence: [inputs](research/run-0139-MH-inputs.json), [probes](research/run-0139-MH-probes.json).
- **Remaining leads:** verify current V7AB/Radio Marshalls and Power 103.5 streams.
- **Next scheduled country:** Mauritania (`MR`).
<a id="run-0140-mq"></a>
### Run 0140 — Martinique (`MQ`)

- **Completed:** 2026-09-12T21:58:22Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using Martinique la 1ère, RCI, and radio directories; six existing catalog streams were checked.
- **Candidate review:** Martinique 1ère, Radio Zoukla, Bel Radio Martinique, Radio Mojito, RCI Dancehall, and NRJ Martinique all matched existing catalog entries. No new stable HTTPS stream was verified. Raw evidence: [inputs](research/run-0140-MQ-inputs.json), [probes](research/run-0140-MQ-probes.json).
- **Remaining leads:** verify Radio Actif, Nord FM, Identité Radio, Mouv FM, and other regional services.
- **Next scheduled country:** Mauritania (`MR`).
<a id="run-0141-mr"></a>
### Run 0141 — Mauritania (`MR`)

- **Completed:** 2026-09-12T22:58:23Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/French/English queries using Radio Mauritanie references, regulator/media sources, and directories; no direct stream endpoint was safely available for probing.
- **Candidate review:** Radio Mauritanie national/regional services, Radio Sahara Media, and Radio Assalamalekoum were identified, but no new stable HTTPS audio endpoint was verified. Raw evidence: [inputs](research/run-0141-MR-inputs.json), [probes](research/run-0141-MR-probes.json).
- **Remaining leads:** extract direct HTTPS feeds for Radio Mauritanie, Sahara Media, Radio Assalamalekoum, and regional services.
- **Next scheduled country:** Mauritius (`MU`).
<a id="run-0142-mu"></a>
### Run 0142 — Mauritius (`MU`)

- **Completed:** 2026-09-13T00:00:23Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using MBC and Mauritian station directories; nine existing catalog streams were checked.
- **Candidate review:** all nine checked feeds matched existing catalog entries. MBC Radio Mauritius and Top FM/other directory leads supplied identity evidence without a newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0142-MU-inputs.json), [probes](research/run-0142-MU-probes.json).
- **Remaining leads:** verify MBC Radio Mauritius, Top FM, Wazaa FM, Kool FM, and other MBC channels for stable HTTPS streams.
- **Next scheduled country:** Mayotte (`YT`).
<a id="run-0143-yt"></a>
### Run 0143 — Mayotte (`YT`)

- **Completed:** 2026-09-13T01:01:23Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using Mayotte la 1ère, local station pages, and directories; two existing catalog streams were checked.
- **Candidate review:** Radio Dziani and Mayotte La 1ère matched existing catalog entries. RMV, Mayotte Streaming, and other local leads did not yield a newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0143-YT-inputs.json), [probes](research/run-0143-YT-probes.json).
- **Remaining leads:** verify RMV, Mayotte Streaming, and additional community stations.
- **Next scheduled country:** Mexico (`MX`).
<a id="run-0144-mx"></a>
### Run 0144 — Mexico (`MX`)

- **Completed:** 2026-09-13T02:02:53Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Spanish/English queries using IMER, SPR, and Mexican radio directories; ten existing catalog streams were checked.
- **Candidate review:** all ten checked Mexico feeds matched existing catalog entries. IMER’s Radio México Internacional and public-radio directories supplied identity leads but no newly verified endpoint. Raw evidence: [inputs](research/run-0144-MX-inputs.json), [probes](research/run-0144-MX-probes.json).
- **Remaining leads:** verify IMER digital stations, SPR regional broadcasters, and community radio endpoints.
- **Next scheduled country:** Micronesia (`FM`).
<a id="run-0145-fm"></a>
### Run 0145 — Micronesia (`FM`)

- **Completed:** 2026-09-13T03:04:24Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using FSM state-radio references and directories; no direct stream endpoint was safely available for probing.
- **Candidate review:** V6AH Pohnpei, V6AK Chuuk, V6AJ Kosrae, V6AI Yap, and other FSM stations were identified, but no newly verified HTTPS audio endpoint was found. Raw evidence: [inputs](research/run-0145-FM-inputs.json), [probes](research/run-0145-FM-probes.json).
- **Remaining leads:** obtain direct HTTPS endpoints for the four state broadcasters, Bible Baptist Radio, Joy FM, and Paradise Radio.
- **Next scheduled country:** Moldova (`MD`).
<a id="run-0146-md"></a>
### Run 0146 — Moldova (`MD`)

- **Completed:** 2026-09-13T04:04:54Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Romanian/Russian/English queries using Radio Moldova, IMER-style public media sources, and directories; one direct candidate was checked.
- **Candidate review:** Radio LOGOS published an MP3 stream, but it is HTTP-only and failed safe endpoint verification. Existing catalog feeds were not duplicated in this run. Raw evidence: [inputs](research/run-0146-MD-inputs.json), [probes](research/run-0146-MD-probes.json).
- **Remaining leads:** verify Radio LOGOS over HTTPS, Radio Moldova channels, and Radio Studentus, Eco FM, and other directory leads.
- **Next scheduled country:** Monaco (`MC`).
<a id="run-0147-mc"></a>
### Run 0147 — Monaco (`MC`)

- **Completed:** 2026-09-13T05:04:24Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using Radio Monaco, MMD, and radio directories; five existing catalog streams were checked.
- **Candidate review:** Radio Monaco, Yellow.radio, Yellow Riviera, Yellow Party, and Radio Monte Carlo Italia matched existing catalog entries. Radio Ethic, MC One, and Riviera Radio were identified as leads without newly verified endpoints. Raw evidence: [inputs](research/run-0147-MC-inputs.json), [probes](research/run-0147-MC-probes.json).
- **Remaining leads:** verify Radio Ethic, MC One, Riviera Radio, and current Radio Monaco secondary feeds.
- **Next scheduled country:** Mongolia (`MN`).
<a id="run-0148-mn"></a>
### Run 0148 — Mongolia (`MN`)

- **Completed:** 2026-09-13T06:04:54Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Mongolian/English queries using CRC, MNB, and radio directories; five existing catalog streams were checked.
- **Candidate review:** Ehlelradio, Family Radio FM, Inner Mongolia Voice of Grassland, Xadun 107.5, and Elgen Nutag matched existing catalog entries. MNB P3, MGL Radio, and Wind FM were identified as leads without newly verified endpoints. Raw evidence: [inputs](research/run-0148-MN-inputs.json), [probes](research/run-0148-MN-probes.json).
- **Remaining leads:** verify MNB P3, MGL Radio, Wind FM, and other Ulaanbaatar services.
- **Next scheduled country:** Montenegro (`ME`).
<a id="run-0149-me"></a>
### Run 0149 — Montenegro (`ME`)

- **Completed:** 2026-09-13T07:05:55Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Montenegrin/Serbian/English queries using RTCG/MNE Play, regulator sources, and directories; ten existing catalog streams were checked.
- **Candidate review:** all ten checked Montenegro feeds matched existing catalog entries. MNE Play and RTCG identified additional web channels, but no newly verified HTTPS endpoint was found. Raw evidence: [inputs](research/run-0149-ME-inputs.json), [probes](research/run-0149-ME-probes.json).
- **Remaining leads:** verify RTCG/MNE Play web channels, Radio DUX, City Radio, and smaller local stations.
- **Next scheduled country:** Morocco (`MA`).

<a id="run-0151-ma"></a>
### Run 0151 — Morocco (`MA`)

- **Completed:** 2026-09-13T09:05:25Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Arabic/French/English queries using SNRT, Moroccan broadcasters, and radio directories; ten existing catalog streams were checked.
- **Candidate review:** the ten checked Morocco feeds matched existing catalog entries. SNRT Radio Maroc, Radio Aswat, Luxe Radio, Medi1, Atlantic, and community-directory leads produced identity evidence but no newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0151-MA-inputs.json), [probes](research/run-0151-MA-probes.json).
- **Remaining leads:** verify direct HTTPS streams for SNRT Radio Maroc, Radio Aswat, Luxe Radio, Medi1, Atlantic Radio, and regional/community stations.
- **Next scheduled country:** Mozambique (`MZ`).

<a id="run-0153-mm"></a>
### Run 0153 — Myanmar (`MM`)

- **Completed:** 2026-09-13T11:05:26Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Burmese/English queries using MRTV and Myanmar radio directories; four catalog streams were checked.
- **Candidate review:** all four checked feeds matched existing catalog entries. MRTV Radio and Yangon City FM sources provided identity evidence but no newly verified direct HTTPS audio endpoint. Raw evidence: [inputs](research/run-0153-MM-inputs.json), [probes](research/run-0153-MM-probes.json).
- **Remaining leads:** locate direct HTTPS endpoints for MRTV Radio, Yangon City FM, and other licensed Myanmar services.
- **Next scheduled country:** Namibia (`NA`).

<a id="run-0162-ng"></a>
### Run 0162 — Nigeria (`NG`)

- **Completed:** 2026-09-13T20:10:28Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using Nigerian broadcaster directories and FRCN references; ten catalog streams were checked.
- **Candidate review:** all ten checked feeds matched existing catalog entries. FRCN Radio Nigeria and other directory leads did not yield additional verified HTTPS endpoints within the run. Raw evidence: [inputs](research/run-0162-NG-inputs.json), [probes](research/run-0162-NG-probes.json).
- **Remaining leads:** investigate FRCN regional stations, Voice of Nigeria, campus, and community broadcasters for direct HTTPS streams.
- **Next scheduled country:** Niue (`NU`).

<a id="run-0161-ne"></a>
### Run 0161 — Niger (`NE`)

- **Completed:** 2026-09-13T19:09:27Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using Niger radio directories and ORTN references; one catalog stream was checked.
- **Candidate review:** Wadata Radio was already cataloged. Other Niger leads were directories or station identities without a newly verified HTTPS audio endpoint. Raw evidence: [inputs](research/run-0161-NE-inputs.json), [probes](research/run-0161-NE-probes.json).
- **Remaining leads:** investigate ORTN/Radio Voix du Sahel, Radio Anfani, community stations, and LRCM Radio for direct HTTPS streams.
- **Next scheduled country:** Nigeria (`NG`).

<a id="run-0160-ni"></a>
### Run 0160 — Nicaragua (`NI`)

- **Completed:** 2026-09-13T18:09:57Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Spanish/English queries using Nicaraguan directories and station sources; ten catalog streams were checked.
- **Candidate review:** all ten checked feeds matched existing catalog entries. Directory leads for Radio Corporación, Radio Ya, Radio La Primerísima, and Radio Éxodos did not yield additional verified HTTPS streams in this run. Raw evidence: [inputs](research/run-0160-NI-inputs.json), [probes](research/run-0160-NI-probes.json).
- **Remaining leads:** investigate those stations and community broadcasters for direct HTTPS audio endpoints.
- **Next scheduled country:** Niger (`NE`).

<a id="run-0159-nz"></a>
### Run 0159 — New Zealand (`NZ`)

- **Completed:** 2026-09-13T17:09:27Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using RNZ, community-radio associations, and station directories; ten stream inputs were checked.
- **Candidate review:** nine checked feeds matched existing catalog entries; World FM’s published HTTP stream was unsafe or unresolvable. Radio Aotearoa, Free FM, and other community leads had no newly verified HTTPS endpoint. Raw evidence: [inputs](research/run-0159-NZ-inputs.json), [probes](research/run-0159-NZ-probes.json).
- **Remaining leads:** investigate Radio Aotearoa, Free FM, World FM, and ACAB member stations for direct HTTPS streams.
- **Next scheduled country:** Nicaragua (`NI`).

<a id="run-0158-nc"></a>
### Run 0158 — New Caledonia (`NC`)

- **Completed:** 2026-09-13T16:08:57Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted French/English queries using local broadcasters and directories; six catalog streams were checked.
- **Candidate review:** all six checked feeds matched existing catalog entries. Radio Djiido, Océane FM, NRJ Nouvelle-Calédonie, and Café’in were identified, but no additional direct HTTPS endpoint was verified. Raw evidence: [inputs](research/run-0158-NC-inputs.json), [probes](research/run-0158-NC-probes.json).
- **Remaining leads:** extract Radio Djiido, Océane FM, NRJ NC, and Café’in stream URLs from official players.
- **Next scheduled country:** New Zealand (`NZ`).

<a id="run-0157-nl"></a>
### Run 0157 — Netherlands (`NL`)

- **Completed:** 2026-09-13T15:07:27Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Dutch/English queries using NPO, commercial broadcasters, and radio directories; ten catalog streams were checked.
- **Candidate review:** all ten checked feeds matched existing catalog entries. Directory leads (including Radio Discovery’s local stations) did not provide newly verified endpoints within the run. Raw evidence: [inputs](research/run-0157-NL-inputs.json), [probes](research/run-0157-NL-probes.json).
- **Remaining leads:** sample regional and community broadcasters for distinct streams in a later sweep.
- **Next scheduled country:** New Caledonia (`NC`).

<a id="run-0156-np"></a>
### Run 0156 — Nepal (`NP`)

- **Completed:** 2026-09-13T14:07:26Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Nepali/English queries using Radio Nepal, ACORAB, and radio directories; ten catalog streams were checked.
- **Candidate review:** all ten checked feeds matched existing catalog entries. Radio Nepal’s official stream and community-radio directories yielded no additional verified HTTPS endpoint within the run. Raw evidence: [inputs](research/run-0156-NP-inputs.json), [probes](research/run-0156-NP-probes.json).
- **Remaining leads:** review ACORAB member stations and local FM sites for distinct direct streams.
- **Next scheduled country:** Netherlands (`NL`).

<a id="run-0155-nr"></a>
### Run 0155 — Nauru (`NR`)

- **Completed:** 2026-09-13T13:07:26Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted queries using Nauru government and radio sources; one historical stream URL was checked.
- **Candidate review:** Radio Nauru’s published `http://radionauru.nr:8000/live` endpoint was unsafe or unresolvable. Life FM Nauru offers app listening but no direct HTTPS audio endpoint was exposed. Raw evidence: [inputs](research/run-0155-NR-inputs.json), [probes](research/run-0155-NR-probes.json).
- **Remaining leads:** locate a current HTTPS stream for Radio Nauru or Life FM.
- **Next scheduled country:** Nepal (`NP`).

<a id="run-0154-na"></a>
### Run 0154 — Namibia (`NA`)

- **Completed:** 2026-09-13T12:06:56Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English/Afrikaans queries using NBC and Namibian broadcaster directories; ten catalog streams were checked.
- **Candidate review:** all ten checked feeds matched existing catalog entries. NBC’s eleven services and 99FM were identified, but no new direct HTTPS endpoint was verified. Raw evidence: [inputs](research/run-0154-NA-inputs.json), [probes](research/run-0154-NA-probes.json).
- **Remaining leads:** extract NBC radio stream endpoints and investigate 99FM, community stations, and regional services.
- **Next scheduled country:** Nauru (`NR`).

<a id="run-0152-mz"></a>
### Run 0152 — Mozambique (`MZ`)

- **Completed:** 2026-09-13T10:05:55Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted Portuguese/English queries using Rádio Moçambique, 99FM, and station directories; six stream inputs were checked.
- **Candidate review:** 99FM and Rádio Cidade Maputo endpoints were unsafe or unresolvable; the remaining four checked feeds matched existing catalog entries. Raw evidence: [inputs](research/run-0152-MZ-inputs.json), [probes](research/run-0152-MZ-probes.json).
- **Remaining leads:** retry 99FM and Rádio Cidade Maputo endpoints and investigate Super FM, Radio Maria, Miramar, Rádio Vida Nampula, and other regional/community stations.
- **Next scheduled country:** Namibia (`NA`).
<a id="run-0150-ms"></a>
### Run 0150 — Montserrat (`MS`)

- **Completed:** 2026-09-13T08:05:55Z
- **Status:** partial; no new ready candidates.
- **Search scope:** six targeted English queries using ZJB Radio and Montserrat community-radio sources; one candidate URL was checked.
- **Candidate review:** One Montserrat Radio’s published HTTPS URL was unsafe or unresolvable. ZJB Radio is the government-owned community broadcaster, but no direct verified HTTPS endpoint was found. Raw evidence: [inputs](research/run-0150-MS-inputs.json), [probes](research/run-0150-MS-probes.json).
- **Remaining leads:** extract ZJB Radio’s current player endpoint and revisit One Montserrat Radio.
- **Next scheduled country:** Morocco (`MA`).
