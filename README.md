# kefafi.dev — Kefafi studio site

**Arabic-first**, bilingual studio site for **kefafi.dev**: a home, Studio (about)
and Contact page, plus a page per product. Arabic (RTL) is the default at the root;
English mirrors it under `/en/`. The two are linked with `hreflang` and a header
language toggle, so each is a real, crawlable page (no JS needed to switch).

Plain HTML + one stylesheet + self-hosted brand fonts. Mirrors the shared
`kefafi_ui_kit` tokens (one clay accent, warm paper, Hanken/Reem Kufi/Plex Mono,
flat surfaces). The only JS is a tiny inline theme toggle — no third-party calls,
no trackers. No serve-time build step.

```
index.html / en/index.html        studio home      ->  / and /en/
about/ , contact/  (+ en/…)       Studio + Contact pages
<product>/ , en/<product>/        product page per language (ar root / en mirror)
<product>/privacy/                privacy policy (namespaced, bilingual where it applies)
styles.css                        Kefafi design tokens + components (light + dark)
favicon.svg                       studio mark; <product>/favicon.svg per product
fonts/                            self-hosted brand TTFs (no third-party font calls)
robots.txt / sitemap.xml          crawl hints (sitemap lists ar + en URLs)
CNAME / .nojekyll                 custom domain + serve-as-is
```

Products on the site: **Nasab** (نسب), **Daftar** (دفتر), **Sayla** (سيلة),
**Lumen** (لومن). The page copy (taglines, intros, features, principles, UI
strings) is the bilingual content from the shared design canvas; if it changes
there, update the matching `ar`/`en` strings here.

**Privacy policies** are bilingual/standalone documents (not under `/en/`):

- **Daftar** mirrors `docs/play-store/privacy-policy.md` in the Daftar app repo (`knkan`).
- **Sayla** is maintained here as its canonical copy.
- **Nasab** was drafted from the `family-tree` app's actual data model (Supabase
  backend, accounts, per-person RLS visibility, revocable email shares, not a
  social network) — unlike the offline apps it honestly states data is stored on
  a server. **Review it before relying on it** as the app evolves.
- **Lumen** has **no** privacy policy yet — it needs one authored from its real
  data practices (no repo access here), so its product page intentionally omits a
  privacy link.

---

## Deploy (GitHub Pages)

These files live in the public repo **`kfafi/kfafi.github.io`**, served by GitHub
Pages (free-plan Pages must be served from a public repo). Each product's app
code stays in its own private repo.

1. Push to `main` (this repo is already public).
2. Repo → **Settings → Pages** → Source: *Deploy from a branch* → `main` / `/root`.
3. Under **Custom domain**, enter `kefafi.dev` and Save (the `CNAME` file already
   sets this). Tick **Enforce HTTPS** once the cert is issued (can take a few
   minutes).

## DNS (at your registrar)

Point the domain at GitHub Pages. Add these records for the **apex** `kefafi.dev`:

```
A     @   185.199.108.153
A     @   185.199.109.153
A     @   185.199.110.153
A     @   185.199.111.153
```

(Optional `www` → repo: `CNAME  www  kfafi.github.io.`)

GitHub provisions a free Let's Encrypt certificate automatically once DNS
resolves.

## Verify the domain (Google Search Console)

Required before the domain can be an OAuth **authorized domain**.

1. Go to [Search Console](https://search.google.com/search-console) → Add
   property → **Domain** → `kefafi.dev`.
2. It gives you a `TXT` record — add it at your registrar's DNS.
3. Click **Verify**. Use the **same Google account that owns GCP project
   `292546653220`** (the OAuth project), or add it as an owner there.

## Publish the OAuth app to Production

In [Google Cloud Console](https://console.cloud.google.com) → project
`292546653220` → **APIs & Services → OAuth consent screen**:

1. **Authorized domains** → add `kefafi.dev`.
2. **App home page** → `https://kefafi.dev/en/sayla/` (English Sayla page; the
   Arabic page is at `https://kefafi.dev/sayla/`).
3. **Privacy policy link** → `https://kefafi.dev/sayla/privacy/`
4. (Skip the logo for now — uploading one triggers a separate brand-verification
   review. Add it later.)
5. **Publishing status** → **Publish app** → confirm to move to *In production*.

Because Sayla uses only the non-sensitive `drive.file` scope, this needs **no**
Google verification/CASA audit. Publishing removes the 100-test-user cap, the
"unverified app" warning, and the 7-day refresh-token expiry.
