# Hosting and deployment

## GitHub Pages: first publication

The repository includes `.github/workflows/pages.yml`, which installs locked dependencies, lints the application, runs offline player/catalog tests, builds the site and validates the release. Only a successful `main` build can deploy; pull requests cannot publish or obtain Pages write permissions.

The repository is [saltysaguaro/radio-atlas](https://github.com/saltysaguaro/radio-atlas), and the local project uses `main`. Its `origin` remote is already configured. In GitHub Desktop:

1. Choose **File → Add Local Repository** and select `/Users/chouette/Documents/radio-atlas`.
2. Review and commit any intended changes on `main`.
3. Click **Publish branch** or **Push origin** to upload the commits.

Use this existing project folder; cloning the empty GitHub repository into it creates a separate nested repository without the website files. From the project root, the terminal equivalent of the push is:

```sh
git push -u origin main
```

For future work on another computer, clone `https://github.com/saltysaguaro/radio-atlas.git` and follow the README's local setup instructions.

In GitHub:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Open **Actions → Build and deploy Radio Atlas → Run workflow**, selecting `main`. The initial push can reach deployment before Pages is enabled; rerun after changing the setting.
4. Wait for both **Test and build** and **Deploy to GitHub Pages** to succeed.
5. Open the URL in the `github-pages` environment: [saltysaguaro.github.io/radio-atlas/](https://saltysaguaro.github.io/radio-atlas/).

Later pushes to `main` validate and deploy automatically. If branch protection is enabled, require the **Test and build** check before merging. Protect the `github-pages` environment so only `main` can deploy. The workflow also checks the branch explicitly, including manual runs.

No personal access token or hosting secret belongs in this repository. GitHub's workflow token supplies deployment permissions. Action versions are pinned by commit; Dependabot proposes updates monthly.

References: [GitHub custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), [Vite static deployment](https://vite.dev/guide/static-deploy.html).

## Paths and custom domains

The app is a single page without pathname-based routes. Vite's `base: './'`, relative catalog/map requests, and relative links support repository names without configuration changes. Keep the trailing slash on a repository URL. No SPA rewrite or `404.html` fallback is needed.

For a custom domain, configure the domain in **Settings → Pages**, follow GitHub's DNS instructions, and enable **Enforce HTTPS** once the certificate is ready. The same build works at a custom domain root. With an Actions publishing source, GitHub manages the custom domain through settings; a `CNAME` file is not required. See [GitHub custom domain management](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## What is published

Only `website/dist/` is uploaded as the Pages artifact: HTML, hashed JavaScript/CSS, icon, `.nojekyll`, catalog, map and third-party notices. Keep source documents and endpoint logs out of the web artifact. No Node.js, Python, database, proxy or server process runs on Pages.

The build uses committed data and does not make live API or stream requests. Catalog checks compare every station with committed endpoint evidence. A refresh is a separate maintainer operation; see the README. The notices are committed too. When changing dependencies, run `python3 scripts/collect_licenses.py`, review the notices and rebuild before publishing.

## Smoke check after deployment

- Open the live address and confirm the map and catalog load.
- Select a country and search for a station.
- Start playback, switch stations, pause, and try the random button. The former stream should stop immediately.
- Open **About & sources** and check the catalog and license links.
- Check a phone browser; playback needs a user gesture and may need time to buffer.

The CI checks validate assets over HTTP at a domain root and two repository paths. They do not establish that every third-party stream decodes or is reachable from every location.

## Updates and rollback

Change source or reviewed data, run the README's validation commands, commit and push to `main`. Keep `website/package-lock.json` committed. Do not commit `website/dist/`, dependencies, downloaded snapshots or caches. GitHub Actions creates the deployment artifact directly from the build; the former upload folder, release ZIPs and packaging script are retired. To roll back, revert the offending commit on `main` and push; the workflow rebuilds that source and data snapshot.

Audio connects directly to the selected broadcaster, which sees the listener's IP address. There are no remote scripts, fonts or map tile requests. Station volume is stored locally in the browser.

## Troubleshooting

- **Pages deployment fails:** confirm Pages uses **GitHub Actions**, that the account's plan supports the repository's visibility, and that the `github-pages` environment permits `main`. Rerun after changing settings.
- **Build fails:** inspect the failed Actions step and reproduce its command locally with Node 22 and `npm ci --prefix website`.
- **Blank page or missing map:** check the complete artifact was deployed, the URL ends in `/`, and `data/catalog.json` and `data/world.geojson` return successfully.
- **A station fails:** streams can move, go offline, restrict locations, or use an unsupported codec. Select another station or retry. Failed connections time out after 18 seconds.
- **Volume on iOS:** some versions require the physical device volume buttons. Mute also uses the audio element's muted property.
