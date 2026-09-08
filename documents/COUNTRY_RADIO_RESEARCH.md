# Country-by-country radio discovery ledger

Created: 2026-09-06. Schedule: hourly, one country or territory per run.
Workspace: `/Users/chouette/Documents/radio-atlas`.

## Coverage and sources

The checklist contains 250 entries: the 249 ISO 3166-1 countries and territories plus Kosovo (`XK`, the project's non-ISO code). It uses the existing project catalog's names and codes so findings can be mapped directly to Radio Atlas. Palestine (`PS`) and Western Sahara (`EH`) have their own rows, as do Taiwan, Kosovo, dependencies, and uninhabited territories. Inclusion is for research coverage and does not express a position on sovereignty.

Reference lists: [ISO country-code browser](https://www.iso.org/obp/ui/#search/code/), [UN countries and areas](https://unstats.un.org/unsd/methodology/m49/), and the project's [country dataset](https://github.com/mledoze/countries). Local baseline: `website/public/data/catalog.json`; existing methodology: `documents/SOURCES.md`.

Search all constituent areas within grouped entries: Bonaire, Sint Eustatius and Saba under Caribbean Netherlands; Saint Helena, Ascension and Tristan da Cunha under SH; Svalbard and Jan Mayen under SJ; and the constituent islands under UM. South Georgia includes the South Sandwich Islands. Use local names and alternate names, including Côte d’Ivoire, Cabo Verde, Holy See, and State of Palestine. Record distinct local or disputed-area provenance within the relevant entry; do not silently assign a station to a neighboring country or infer origin from its server location. Add separately evidenced coverage gaps as explicit checklist entries with a documented catalog-code mapping rather than inventing ISO codes.

## Persistent progress

- Completed research runs: 43
- Current sweep: 1
- Next country: Central African Republic (`CF`)
- Last run: Run 0043 — Cayman Islands (`KY`), partial, ended 2026-09-08T16:35:24Z; no new ready candidates.
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
| 44 | CF | Central African Republic | 2 | 0 | pending | — | — | — | — |
| 45 | TD | Chad | 1 | 0 | pending | — | — | — | — |
| 46 | CL | Chile | 392 | 0 | pending | — | — | — | — |
| 47 | CN | China | 1080 | 0 | pending | — | — | — | — |
| 48 | CX | Christmas Island | 1 | 0 | pending | — | — | — | — |
| 49 | CC | Cocos (Keeling) Islands | 1 | 0 | pending | — | — | — | — |
| 50 | CO | Colombia | 494 | 0 | pending | — | — | — | — |
| 51 | KM | Comoros | 0 | 0 | pending | — | — | — | — |
| 52 | CG | Congo | 1 | 0 | pending | — | — | — | — |
| 53 | CK | Cook Islands | 0 | 0 | pending | — | — | — | — |
| 54 | CR | Costa Rica | 38 | 0 | pending | — | — | — | — |
| 55 | HR | Croatia | 107 | 0 | pending | — | — | — | — |
| 56 | CU | Cuba | 12 | 0 | pending | — | — | — | — |
| 57 | CW | Curaçao | 17 | 0 | pending | — | — | — | — |
| 58 | CY | Cyprus | 26 | 0 | pending | — | — | — | — |
| 59 | CZ | Czechia | 183 | 0 | pending | — | — | — | — |
| 60 | DK | Denmark | 124 | 0 | pending | — | — | — | — |
| 61 | DJ | Djibouti | 0 | 0 | pending | — | — | — | — |
| 62 | DM | Dominica | 5 | 0 | pending | — | — | — | — |
| 63 | DO | Dominican Republic | 81 | 0 | pending | — | — | — | — |
| 64 | CD | DR Congo | 11 | 0 | pending | — | — | — | — |
| 65 | EC | Ecuador | 122 | 0 | pending | — | — | — | — |
| 66 | EG | Egypt | 29 | 0 | pending | — | — | — | — |
| 67 | SV | El Salvador | 40 | 0 | pending | — | — | — | — |
| 68 | GQ | Equatorial Guinea | 0 | 0 | pending | — | — | — | — |
| 69 | ER | Eritrea | 1 | 0 | pending | — | — | — | — |
| 70 | EE | Estonia | 86 | 0 | pending | — | — | — | — |
| 71 | SZ | Eswatini | 0 | 0 | pending | — | — | — | — |
| 72 | ET | Ethiopia | 22 | 0 | pending | — | — | — | — |
| 73 | FK | Falkland Islands | 4 | 0 | pending | — | — | — | — |
| 74 | FO | Faroe Islands | 6 | 0 | pending | — | — | — | — |
| 75 | FJ | Fiji | 6 | 0 | pending | — | — | — | — |
| 76 | FI | Finland | 87 | 0 | pending | — | — | — | — |
| 77 | FR | France | 1561 | 0 | pending | — | — | — | — |
| 78 | GF | French Guiana | 3 | 0 | pending | — | — | — | — |
| 79 | PF | French Polynesia | 6 | 0 | pending | — | — | — | — |
| 80 | TF | French Southern and Antarctic Lands | 0 | 0 | pending | — | — | — | — |
| 81 | GA | Gabon | 0 | 0 | pending | — | — | — | — |
| 82 | GM | Gambia | 0 | 0 | pending | — | — | — | — |
| 83 | GE | Georgia | 12 | 0 | pending | — | — | — | — |
| 84 | DE | Germany | 4341 | 0 | pending | — | — | — | — |
| 85 | GH | Ghana | 75 | 0 | pending | — | — | — | — |
| 86 | GI | Gibraltar | 6 | 0 | pending | — | — | — | — |
| 87 | GR | Greece | 1227 | 0 | pending | — | — | — | — |
| 88 | GL | Greenland | 5 | 0 | pending | — | — | — | — |
| 89 | GD | Grenada | 3 | 0 | pending | — | — | — | — |
| 90 | GP | Guadeloupe | 10 | 0 | pending | — | — | — | — |
| 91 | GU | Guam | 3 | 0 | pending | — | — | — | — |
| 92 | GT | Guatemala | 58 | 0 | pending | — | — | — | — |
| 93 | GG | Guernsey | 1 | 0 | pending | — | — | — | — |
| 94 | GN | Guinea | 4 | 0 | pending | — | — | — | — |
| 95 | GW | Guinea-Bissau | 1 | 0 | pending | — | — | — | — |
| 96 | GY | Guyana | 7 | 0 | pending | — | — | — | — |
| 97 | HT | Haiti | 22 | 0 | pending | — | — | — | — |
| 98 | HM | Heard Island and McDonald Islands | 0 | 0 | pending | — | — | — | — |
| 99 | HN | Honduras | 31 | 0 | pending | — | — | — | — |
| 100 | HK | Hong Kong | 20 | 0 | pending | — | — | — | — |
| 101 | HU | Hungary | 188 | 0 | pending | — | — | — | — |
| 102 | IS | Iceland | 6 | 0 | pending | — | — | — | — |
| 103 | IN | India | 537 | 0 | pending | — | — | — | — |
| 104 | ID | Indonesia | 365 | 0 | pending | — | — | — | — |
| 105 | IR | Iran | 17 | 0 | pending | — | — | — | — |
| 106 | IQ | Iraq | 14 | 0 | pending | — | — | — | — |
| 107 | IE | Ireland | 119 | 0 | pending | — | — | — | — |
| 108 | IM | Isle of Man | 7 | 0 | pending | — | — | — | — |
| 109 | IL | Israel | 85 | 0 | pending | — | — | — | — |
| 110 | IT | Italy | 855 | 0 | pending | — | — | — | — |
| 111 | CI | Ivory Coast | 11 | 0 | pending | — | — | — | — |
| 112 | JM | Jamaica | 33 | 0 | pending | — | — | — | — |
| 113 | JP | Japan | 69 | 0 | pending | — | — | — | — |
| 114 | JE | Jersey | 2 | 0 | pending | — | — | — | — |
| 115 | JO | Jordan | 8 | 0 | pending | — | — | — | — |
| 116 | KZ | Kazakhstan | 17 | 0 | pending | — | — | — | — |
| 117 | KE | Kenya | 33 | 0 | pending | — | — | — | — |
| 118 | KI | Kiribati | 1 | 0 | pending | — | — | — | — |
| 119 | XK | Kosovo | 6 | 0 | pending | — | — | — | — |
| 120 | KW | Kuwait | 8 | 0 | pending | — | — | — | — |
| 121 | KG | Kyrgyzstan | 6 | 0 | pending | — | — | — | — |
| 122 | LA | Laos | 3 | 0 | pending | — | — | — | — |
| 123 | LV | Latvia | 50 | 0 | pending | — | — | — | — |
| 124 | LB | Lebanon | 33 | 0 | pending | — | — | — | — |
| 125 | LS | Lesotho | 1 | 0 | pending | — | — | — | — |
| 126 | LR | Liberia | 0 | 0 | pending | — | — | — | — |
| 127 | LY | Libya | 4 | 0 | pending | — | — | — | — |
| 128 | LI | Liechtenstein | 1 | 0 | pending | — | — | — | — |
| 129 | LT | Lithuania | 47 | 0 | pending | — | — | — | — |
| 130 | LU | Luxembourg | 20 | 0 | pending | — | — | — | — |
| 131 | MO | Macau | 4 | 0 | pending | — | — | — | — |
| 132 | MG | Madagascar | 8 | 0 | pending | — | — | — | — |
| 133 | MW | Malawi | 7 | 0 | pending | — | — | — | — |
| 134 | MY | Malaysia | 43 | 0 | pending | — | — | — | — |
| 135 | MV | Maldives | 3 | 0 | pending | — | — | — | — |
| 136 | ML | Mali | 12 | 0 | pending | — | — | — | — |
| 137 | MT | Malta | 6 | 0 | pending | — | — | — | — |
| 138 | MH | Marshall Islands | 2 | 0 | pending | — | — | — | — |
| 139 | MQ | Martinique | 6 | 0 | pending | — | — | — | — |
| 140 | MR | Mauritania | 0 | 0 | pending | — | — | — | — |
| 141 | MU | Mauritius | 9 | 0 | pending | — | — | — | — |
| 142 | YT | Mayotte | 2 | 0 | pending | — | — | — | — |
| 143 | MX | Mexico | 1217 | 0 | pending | — | — | — | — |
| 144 | FM | Micronesia | 0 | 0 | pending | — | — | — | — |
| 145 | MD | Moldova | 60 | 0 | pending | — | — | — | — |
| 146 | MC | Monaco | 5 | 0 | pending | — | — | — | — |
| 147 | MN | Mongolia | 5 | 0 | pending | — | — | — | — |
| 148 | ME | Montenegro | 35 | 0 | pending | — | — | — | — |
| 149 | MS | Montserrat | 0 | 0 | pending | — | — | — | — |
| 150 | MA | Morocco | 43 | 0 | pending | — | — | — | — |
| 151 | MZ | Mozambique | 5 | 0 | pending | — | — | — | — |
| 152 | MM | Myanmar | 4 | 0 | pending | — | — | — | — |
| 153 | NA | Namibia | 12 | 0 | pending | — | — | — | — |
| 154 | NR | Nauru | 0 | 0 | pending | — | — | — | — |
| 155 | NP | Nepal | 19 | 0 | pending | — | — | — | — |
| 156 | NL | Netherlands | 799 | 0 | pending | — | — | — | — |
| 157 | NC | New Caledonia | 6 | 0 | pending | — | — | — | — |
| 158 | NZ | New Zealand | 118 | 0 | pending | — | — | — | — |
| 159 | NI | Nicaragua | 18 | 0 | pending | — | — | — | — |
| 160 | NE | Niger | 1 | 0 | pending | — | — | — | — |
| 161 | NG | Nigeria | 55 | 0 | pending | — | — | — | — |
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
