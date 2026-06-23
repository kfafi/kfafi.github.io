# kefafi.dev — Kefafi studio site

Static site for **kefafi.dev**: the Kefafi studio homepage, plus a page and
privacy policy per product. Sayla and Daftar ship today; more slot in beside them.

Plain HTML + one stylesheet + self-hosted brand fonts. No build step.

```
index.html                  studio home  ->  https://kefafi.dev/
styles.css                  Kefafi tokens (clay-on-cream, light + dark)
favicon.svg                 Kefafi mark (studio)
fonts/                      self-hosted brand TTFs (no third-party font calls)
robots.txt                  allow all + sitemap pointer
sitemap.xml                 the five public URLs
CNAME                       custom domain for GitHub Pages (kefafi.dev)
.nojekyll                   serve files as-is (skip Jekyll)

sayla/
  index.html                Sayla product page  ->  https://kefafi.dev/sayla/
  favicon.svg               Sayla mark
  privacy/
    index.html              Sayla privacy policy ->  https://kefafi.dev/sayla/privacy/

daftar/
  index.html                Daftar product page  ->  https://kefafi.dev/daftar/
  favicon.svg               Daftar mark
  privacy/
    index.html              Daftar privacy policy (AR + EN) -> https://kefafi.dev/daftar/privacy/
```

Adding a product later = a new `<product>/` folder with its own `index.html` and
`privacy/index.html`, plus a card in the studio `index.html` and a `<url>` in
`sitemap.xml`. Each product's privacy policy is namespaced, so they never collide.

Each policy here is the published copy. **Daftar**'s policy mirrors
`docs/play-store/privacy-policy.md` in the Daftar app repo (`knkan`) — keep the two
in sync when the wording changes. **Sayla**'s policy is currently maintained here
as its canonical copy (there is no separate doc in the app repo yet).

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
2. **App home page** → `https://kefafi.dev/sayla/`
3. **Privacy policy link** → `https://kefafi.dev/sayla/privacy/`
4. (Skip the logo for now — uploading one triggers a separate brand-verification
   review. Add it later.)
5. **Publishing status** → **Publish app** → confirm to move to *In production*.

Because Sayla uses only the non-sensitive `drive.file` scope, this needs **no**
Google verification/CASA audit. Publishing removes the 100-test-user cap, the
"unverified app" warning, and the 7-day refresh-token expiry.
