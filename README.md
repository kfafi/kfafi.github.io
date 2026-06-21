# kefafi.dev — Kefafi studio site

Static site for **kefafi.dev**: the Kefafi studio homepage, plus a page and
privacy policy per product. Sayla is the first product; more slot in beside it.

Plain HTML + one stylesheet + self-hosted brand fonts. No build step.

```
index.html                  studio home  ->  https://kefafi.dev/
styles.css                  Kefafi tokens (clay-on-cream, light + dark)
favicon.svg                 Kefafi mark (studio)
fonts/                      self-hosted brand TTFs (no third-party font calls)
CNAME                       custom domain for GitHub Pages (kefafi.dev)
.nojekyll                   serve files as-is (skip Jekyll)

sayla/
  index.html                Sayla product page  ->  https://kefafi.dev/sayla/
  favicon.svg               Sayla mark
  privacy/
    index.html              Sayla privacy policy ->  https://kefafi.dev/sayla/privacy/
```

Adding a product later = a new `<product>/` folder with its own `index.html` and
`privacy/index.html`, plus a card in the studio `index.html`. Each product's
privacy policy is namespaced, so they never collide.

The canonical source of Sayla's policy text is
`docs/legal/sayla-privacy-policy.md` in the main (private) app repo. Keep the two
in sync when the wording changes.

---

## Deploy (GitHub Pages)

These files are meant to live in a **separate public repo** (e.g.
`kfafi/kefafi-site`), because GitHub Pages on a free plan must be served from a
public repo. The app code stays in the private repo.

1. Create a public repo `kefafi-site`.
2. Copy the **contents of this `site/` folder** into the repo root and push to
   `main`.
3. Repo → **Settings → Pages** → Source: *Deploy from a branch* → `main` / `/root`.
4. Under **Custom domain**, enter `kefafi.dev` and Save (the `CNAME` file already
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
