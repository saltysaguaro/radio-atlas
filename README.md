# Radio Atlas

Explore public radio streams on an interactive world map. Choose a country, search stations by name, genre, language or region, and listen directly in the browser—or use **Take me anywhere** to discover a random station.

The bundled September 5, 2026 catalog contains **32,605 HTTPS feeds across 212 countries and territories**, with 250 selectable country/territory entries. Stream checks are point-in-time evidence; availability and browser compatibility can vary.

Built with React, TypeScript, Vite and Leaflet. The website is entirely static: no server, database, API key, paid map tiles or login is required. Map geometry and station metadata are bundled; audio connects directly to broadcasters.

## Run locally

Use Node.js 22.13+ (the `.nvmrc` selects Node 22) and npm. Python 3.10+ is needed for catalog/release checks; curl is needed only for data refresh and license collection.

From the repository root:

```sh
npm ci --prefix website
npm run dev --prefix website
```

Open the local address printed by Vite. To preview a production build:

```sh
npm run build --prefix website
npm run preview --prefix website
```

Do not open `index.html` as a local file: catalog loading requires HTTP.

## Publish with GitHub Pages

1. Push this project to a GitHub repository using `main` as the default branch.
2. In the repository, open **Settings → Pages → Build and deployment → Source** and choose **GitHub Actions**.
3. Open **Actions → Build and deploy Radio Atlas → Run workflow**, selecting `main` for the first deployment. Later pushes to `main` deploy automatically after checks pass.
4. Open the URL shown by the `github-pages` deployment: [saltysaguaro.github.io/radio-atlas/](https://saltysaguaro.github.io/radio-atlas/).

Pull requests run validation without publishing. Deployment uses only `website/dist/`; research files, source code and endpoint logs are not part of the hosted site. The repository can be named anything: asset and data URLs are relative. See [deployment instructions](documents/DEPLOYMENT.md) for first-push commands, custom domains, and troubleshooting.

The workflow follows [GitHub's custom Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [Vite's static deployment guidance](https://vite.dev/guide/static-deploy.html). It uses the built-in GitHub token and requires no deployment secret.

## Validate changes

Run these commands from the repository root; they are also run in GitHub Actions:

```sh
npm run lint --prefix website
npm test --prefix website
python3 scripts/test_catalog.py
npm run build --prefix website
python3 scripts/validate_release.py
```

The checks cover player switching and failures, safe stream probing, catalog consistency, recorded verification evidence, production assets, and HTTP delivery at `/`, `/radio-atlas/`, and a renamed repository path. They do not contact broadcasters or refresh the catalog. See [validation notes](documents/VALIDATION.md) and [contributor guidance](CONTRIBUTING.md).

## Project layout

| Path | Purpose |
| --- | --- |
| `website/app/`, `website/lib/` | Atlas interface and audio player |
| `website/components/`, `website/hooks/` | Bundled UI primitives |
| `website/public/data/` | Committed station catalog and world map |
| `website/public/THIRD-PARTY-NOTICES.txt` | Dependency and data license texts |
| `website/scripts/` | Offline player tests |
| `scripts/` | Catalog research, refresh, validation and license collection |
| `documents/` | Coverage, provenance, check evidence and research ledger |
| `.github/` | Build/deploy workflow, dependency updates and contribution templates |

This repository is the working project and the source for GitHub Pages. GitHub Actions builds `website/dist/` and publishes it directly; no upload folder or ZIP package is needed. Installed `website/node_modules/`, generated builds, caches, local hosting metadata and the large raw directory download are ignored by Git. The processed catalog, map and endpoint evidence are committed so clean clones can build and validate without downloading source data.

## Refresh station data

A normal build uses the committed data. To perform a new live verification sweep, run:

```sh
python3 scripts/build_catalog.py
python3 scripts/finalize_catalog.py
python3 scripts/test_catalog.py
```

Review the changed catalog, [coverage](documents/COVERAGE.md), discovery report, location audit and endpoint evidence, then run the full validation sequence above before committing. Publishing updated data requires a push to `main`.

A refresh can take tens of minutes and probes all distinct candidates from Radio Browser and the maintained broadcaster supplements. There is no per-country limit. Evidence younger than 24 hours is reused; `--fresh-checks` forces new probes. `--cached-source` requires the locally downloaded `documents/source-snapshot.json`, which is deliberately not committed.

The [country research ledger](documents/COUNTRY_RADIO_RESEARCH.md) records candidates and unresolved leads. A separate local Codex schedule was used to produce it; cloning this repository does not install that schedule. GitHub Actions does not run station research or a live refresh.

## Sources and rights

Map boundaries come from Natural Earth; country metadata comes from mledoze/countries; station metadata comes from Radio Browser and credited broadcaster sources. Audio remains with its rights holders. See [sources](documents/SOURCES.md), [third-party notices](website/public/THIRD-PARTY-NOTICES.txt), and [licensing status](LICENSE.md). An open-source license for original project code has not yet been selected.
