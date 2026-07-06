# HANDOFF — kefafi.dev

Operational handoff for the Kefafi studio site. Pairs with `README.md` (structure)
and `tools/build.py` (the generator). Last updated 2026-07-06.

## What this is

Static site for **kefafi.dev** — the Kefafi studio home plus a page (and legal /
beta pages) per product. Hosted on **GitHub Pages** from `main` in
`kfafi/kfafi.github.io`, **behind Cloudflare**, on the custom domain `kefafi.dev`.
Bilingual, **Arabic-first at the root**, English mirror under `/en/`.

## Current state (live)

- **Products:** Nasab (نسب), Daftar (دفتر), Sayla (سيلة), Lumen (لومن).
- **Pages:** home · Studio (`/about/`) · Contact (`/contact/`) · a page per product ·
  Nasab legal (`/nasab/privacy/`, `/nasab/terms/`, `/nasab/support/`, with `#delete`) ·
  per-app beta pages (`/<app>/test/`) · Daftar & Sayla privacy (bilingual single files).
- **Download / beta story (consistent end to end):**
  - **Home cards** show availability hints — Nasab `Beta`, Daftar `App Store · Beta`,
    Sayla `Chrome · Beta`, Lumen `Soon`.
  - **Product pages** show real store **download badges** for released apps
    (Daftar → App Store, Sayla → Chrome Web Store) with a secondary "Android beta"
    link; not-yet-public apps (Nasab) lead with **Join the beta**; Lumen leads with GitHub.
  - **Beta pages** = "how to join the testing group" (Request to join → Join the test).
- **Deep links:** `/.well-known/assetlinks.json` (Android App Links, Nasab) and
  `/.well-known/apple-app-site-association` (iOS Universal Links, Nasab).

## Architecture

- Plain **static HTML + one stylesheet** (`styles.css`) + **self-hosted fonts**.
  No serve-time build, no JS framework. The only JS is a tiny inline theme toggle.
- **`tools/build.py`** is the generator AND the single source for the bilingual
  marketing/product/beta/legal **copy**, product favicons, and `sitemap.xml`.
  Edit its content tables, then `python3 tools/build.py`, then commit the output.
  It is **idempotent** (re-running with no content change produces no diff).
- **Hand-maintained (NOT generated):** `styles.css`; `sayla/privacy/` &
  `daftar/privacy/` (legal text); `.well-known/*`; `CNAME`; `robots.txt`;
  `.nojekyll`; studio `favicon.svg`.

## How to make common changes

- **Add a store link** (e.g. Google Play once public): in `build.py`, add to that
  product's `stores` list — `{"kind": "appstore|play|chrome|web", "url": "..."}`.
  Run the generator. The product-page badge **and** the home-card chip update
  automatically (Google Play/App Store/Chrome/Web icons already exist).
- **Give Lumen a beta page:** add `"android": "<play.package>"` to `lumen` in PRODUCTS.
- **Edit copy:** change the content tables (`PRODUCTS` / `PRINCIPLES` / `VOICE` / `T`,
  or `NASAB_PAGES` for the legal pages), run the generator.
- **Add a product:** append to `PRODUCTS` (id, mono, tile, name, ar, tagline, line,
  intro, platforms, features; optional `android` / `stores` / `privacy`), run generator.

## Deploy — and the gotchas we hit

Merging to `main` triggers the **"pages build and deployment"** workflow → live in
~1–2 min. Things that bit us and how to handle them:

1. **GitHub Pages deploy flakiness.** The *build/artifact* is reliable, but the
   *deploy step* intermittently fails ("Deployment failed, try again later") or
   wedges in `queued`. If a merge doesn't go live: check Actions → the run's
   conclusion. If it failed/wedged, **push a trivial commit** (or re-run the run)
   to kick a fresh deploy. We once had to push a no-op change to unstick it.
2. **Fastly stale-404 cache (~10 min).** If you `curl` a URL *before* it deploys,
   GitHub caches that 404 for up to 10 min — so a page can 404 even after it
   publishes. Verify the **origin** with a cache-busting query, e.g.
   `curl "https://kefafi.dev/<path>/?cb=$RANDOM"`.
3. **Cloudflare is in front.** A **Transform Rule** sets
   `Content-Type: application/json` on `/.well-known/apple-app-site-association`
   (GitHub Pages serves the extensionless file as `application/octet-stream`).
   Do **not** cache-transform or redirect the two `.well-known` paths.
4. **`.nojekyll`** at the root must stay — it lets the `.well-known` dot-folder publish.

## Branch / merge workflow (important)

Work happens on branch `claude/beautiful-mccarthy-5t83p3` and is **squash-merged**
to `main`. Because squash rewrites history, **restart the branch from `main` before
each new change**, or you get squash-divergence conflicts:

```
git fetch origin main
git checkout -B claude/beautiful-mccarthy-5t83p3 origin/main
# ...edit build.py / styles.css, then: python3 tools/build.py
git add -A && git commit -m "..."
git push --force-with-lease -u origin claude/beautiful-mccarthy-5t83p3
# open PR -> squash merge
```

## Open items / pending inputs

- **Google Play** links for the public apps (Daftar / Sayla, and Nasab when live) →
  add as `stores` kind `"play"`.
- **Sayla on iOS** — App Store link, if it ships there.
- **Lumen** — Play package (to generate its beta page) and any store links; **Lumen
  still has no privacy policy** (needs authoring from its real data practices).
- **Nasab** — production store links once public. Its privacy/terms were drafted from
  the `family-tree` implementation; **have them legal-reviewed** before a wide release.
- **Google Search Console** "Page with redirect" on `http://kefafi.dev/` is benign
  (http→https on the root); validate/ignore.

## Key facts

- Support: `support@kefafi.dev` · studio contact: `hello@kefafi.dev`.
- Governing law (Nasab Terms): Kingdom of Saudi Arabia.
- Packages / store IDs:
  - Nasab — Android `dev.kefafi.family_tree`, iOS `dev.kefafi.familyTree`
    (AASA appID `X8YHXF2LK2.dev.kefafi.familyTree`, App Links SHA256 in
    `.well-known/assetlinks.json`).
  - Daftar — `dev.kefafi.daftar`; App Store `id6781765878`.
  - Sayla — **published** Android `com.kefafi.sayla` (the repo's internal
    `applicationId` is `com.kfafi.sharebullet`); Chrome Web Store extension
    `njnafbnpbnjnlfeeaedpedlloecmoilp`.
- Design mirrors the `kefafi_ui_kit` tokens (one clay accent, warm paper, Hanken /
  Reem Kufi / IBM Plex Mono); motion aligned to `tokens.json` (180ms).
