# -*- coding: utf-8 -*-
"""Static-site generator for kefafi.dev.

Emits the bilingual (Arabic-first) MARKETING pages, product favicons, and
sitemap.xml from the content tables below — the single source for that copy.
Run it after editing PRODUCTS / PRINCIPLES / VOICE / T, then commit the output.
This is an OPTIONAL dev tool, NOT a serve-time build step: GitHub Pages serves
the generated .html directly.

It does NOT touch: styles.css, the privacy pages (hand-maintained legal docs),
the studio favicon, or CNAME/robots.txt/.nojekyll.

    python3 tools/build.py
"""
import html, os

# Repo root = parent of this tools/ directory, so the script is path-portable.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- content
PRODUCTS = [
    {"id": "nasab", "mono": "ن", "tile": "ink", "name": "Nasab", "ar": "نسب",
     "tagline": {"ar": "شجرة عائلتك — مِلكك.",
                 "en": "Your family tree, yours."},
     "line": {"ar": "تملك شجرة عائلتك؛ تشاركها وتسحبها متى شئت. ليست شبكة اجتماعية.",
              "en": "Own your family's tree; share it, revoke it. Not a social network."},
     "intro": {"ar": "نسب تطبيق لشجرة العائلة. كل شخص يملك شجرته بتحكّم كامل وقابل للسحب في المشاركة. ليست شبكة اجتماعية — مجرّد نسبك، لك.",
               "en": "Nasab is a family-tree app. Each person owns their own tree, with full, revocable control over sharing. Not a social network — just your lineage, yours."},
     "platforms": ["Flutter", "Web", "iOS", "Android"],
     "features": [
        {"ar": "أسماء النسب تُولَّد ولا تُخزّن.", "en": "Patrilineal nasab names, generated — never stored."},
        {"ar": "ثلاثة أجيال في لمحة واحدة.", "en": "Three generations at a glance."},
        {"ar": "تتحكّم بالمشاركة، وتسحبها متى شئت.", "en": "You control sharing — revocable anytime."},
        {"ar": "خصوصية محفوظة للأحياء.", "en": "Privacy for the living."},
     ], "privacy": True},
    {"id": "daftar", "mono": "د", "tile": "clay", "name": "Daftar", "ar": "دفتر",
     "tagline": {"ar": "سجّل اللعب بلا ورقة.", "en": "Score the game, no paper."},
     "line": {"ar": "تتبّع نقاط الكنكان والبلوت. بديل الدفتر الورقي. دون اتصال، بلا حسابات.",
              "en": "Track the score for Kankan and Baloot. Replaces the paper notebook. Offline, no accounts."},
     "intro": {"ar": "دفتر يسجّل نقاط الكنكان والبلوت بدل الدفتر الورقي. المجاميع تُحسب تلقائياً ويُنبَّه الأقرب للحد. يعمل دون اتصال، بلا حسابات ولا سحابة.",
               "en": "Daftar tracks the score for Kankan and Baloot, replacing the paper notebook. Totals compute automatically and the player nearest the limit is flagged. Offline, no accounts, no cloud."},
     "platforms": ["Flutter", "iOS", "Android", "Offline"],
     "features": [
        {"ar": "تسجيل الكنكان والبلوت.", "en": "Kankan & Baloot scoring."},
        {"ar": "مجاميع تلقائية، وتنبيه للأقرب للحد.", "en": "Auto totals; nearest-to-limit flagged."},
        {"ar": "إدخال سريع أو يدوي للجولة.", "en": "Quick or manual round entry."},
        {"ar": "دون اتصال، بلا حسابات، بلا سحابة.", "en": "Offline, no accounts, no cloud."},
     ], "privacy": True},
    {"id": "sayla", "mono": "س", "tile": "clay", "name": "Sayla", "ar": "سيلة",
     "tagline": {"ar": "مرِّر بين أجهزتك.", "en": "Push across your devices."},
     "line": {"ar": "مرِّر الملاحظات والروابط والملفات بين أجهزتك عبر Google Drive الخاص بك. بلا خادم.",
              "en": "Push notes, links and files between your devices through your own Google Drive. No server."},
     "intro": {"ar": "سيلة تمرِّر الملاحظات والروابط والملفات بين أجهزتك عبر Google Drive الخاص بك — بلا خادم وسيط. ما ترسله يظهر على جهازك الآخر.",
               "en": "Sayla pushes notes, links, and files between your own devices through your own Google Drive — no middle-man server. What you send shows up on your other device."},
     "platforms": ["Chrome", "Flutter", "Drive"],
     "features": [
        {"ar": "ملاحظات وروابط وملفات بين الأجهزة.", "en": "Notes, links and files across devices."},
        {"ar": "عبر Google Drive الخاص بك.", "en": "Through your own Google Drive."},
        {"ar": "لا خادم يرى بياناتك.", "en": "No server ever sees your data."},
        {"ar": "إضافة متصفّح + تطبيق جوال.", "en": "Browser extension + mobile app."},
     ], "privacy": True},
    {"id": "lumen", "mono": "ل", "tile": "ink", "name": "Lumen", "ar": "لومن",
     "tagline": {"ar": "هادئ على الشاشة الكبيرة.", "en": "Calm on the big screen."},
     "line": {"ar": "تطبيق لتلفاز أندرويد، مع محدِّث داخل التطبيق.",
              "en": "An Android-TV app with an in-app updater."},
     "intro": {"ar": "لومن تطبيق لتلفاز أندرويد، مع محدِّث داخل التطبيق وواجهة هادئة تناسب جهاز التحكم.",
               "en": "Lumen is an Android-TV app with an in-app updater and a calm, remote-friendly interface."},
     "platforms": ["Android TV"],
     "features": [
        {"ar": "مصمّم لتلفاز أندرويد.", "en": "Built for Android TV."},
        {"ar": "محدِّث داخل التطبيق.", "en": "In-app updater."},
        {"ar": "واجهة هادئة تناسب جهاز التحكم.", "en": "Calm, remote-friendly UI."},
     ]},
]

PRINCIPLES = [
    {"title": {"ar": "عربيٌّ أولاً", "en": "Arabic-first"},
     "body": {"ar": "عربيٌّ أولاً وRTL افتراضاً. الإنجليزية تعكسه.", "en": "Arabic-first, RTL by default. English mirrors it."}},
    {"title": {"ar": "بياناتك مِلكك", "en": "Your data is yours"},
     "body": {"ar": "دون اتصال حيثما أمكن. بلا حسابات لا لزوم لها، بلا قفل سحابي.", "en": "Offline where we can. No needless accounts, no cloud lock-in."}},
    {"title": {"ar": "هدوءٌ بالتصميم", "en": "Calm by design"},
     "body": {"ar": "ورقٌ دافئ، لونٌ واحد، بلا ضجيج.", "en": "Warm paper, one accent, no noise."}},
    {"title": {"ar": "ما يكفي فقط", "en": "Just enough"},
     "body": {"ar": "أدواتٌ تفعل ما يكفي — ولا شيء أكثر.", "en": "Tools that do just enough — and nothing more."}},
    {"title": {"ar": "كلامٌ واضح", "en": "Plain words"},
     "body": {"ar": "نذكر النتيجة، لا نصرخ بها.", "en": "We state the result; we don't shout it."}},
    {"title": {"ar": "طقمٌ واحد", "en": "One shared kit"},
     "body": {"ar": "كل أداة مبنية على نفس الطقم المشترك.", "en": "Every tool is built on the same shared kit."}},
]

VOICE = {
    "ar": {"do": ["«سجِّل كنكان بلا ورقة.»", "«احفظ الجولة.»", "«إنها على جهازك الآخر.»"],
           "dont": ["«🎉 حطّمت الرقم القياسي!!»", "«اكتملت العملية بنجاح.»"]},
    "en": {"do": ['"Score Kankan, no paper."', '"Save the round."', '"It\'s on your other device."'],
           "dont": ['"🎉 You crushed it! New high score!!"', '"Transfer completed successfully."']},
}

T = {
 "ar": {
  "navHome": "الرئيسية", "navProducts": "المنتجات", "navAbout": "الاستوديو", "navContact": "تواصل",
  "studioEyebrow": "استوديو برمجيات مستقل",
  "heroTitle": "أدواتٌ تفعل ما يكفي فقط.",
  "heroSub": "كفافي استوديو مستقل يصنع أدوات صغيرة دقيقة وهادئة للحياة اليومية. كلٌّ منها يفعل شيئاً واحداً جيداً، ثم يبتعد عن طريقك.",
  "heroCta": "شاهد المنتجات", "heroCta2": "عن الاستوديو",
  "productsEyebrow": "المنتجات", "productsTitle": "أربع أدوات.", "productsSub": "مبنيّة على نفس المبادئ ونفس الطقم المشترك.",
  "viewLabel": "اعرف أكثر",
  "principlesEyebrow": "كيف نبني", "principlesTitle": "مبادئ قليلة، نلتزم بها.",
  "closingEyebrow": "تواصل", "closingTitle": "فكرةٌ، أو سؤال؟", "closingSub": "نحب أن نسمع منك.",
  "backLabel": "كل المنتجات", "featuresTitle": "ماذا يفعل", "partOf": "جزء من كفافي", "partOfSub": "أداةٌ واحدة من أربع، مبنيّة بنفس الهدوء.", "ctaGithub": "على GitHub", "privacyLabel": "سياسة الخصوصية",
  "aboutEyebrow": "الاستوديو", "aboutTitle": "ما يكفي فقط.",
  "aboutP1": "كفافي استوديو برمجيات مستقل صغير. نصنع أدوات هادئة للحياة اليومية — أداةٌ تفعل شيئاً واحداً جيداً، ثم تبتعد عن طريقك.",
  "aboutP2": "نبني بلغةٍ عربية أولاً، ودون اتصال حيثما أمكن. بياناتك تبقى معك. واجهاتنا دافئة، بلونٍ واحد، بلا ضجيج.",
  "voiceEyebrow": "كيف نكتب", "voiceTitle": "كلامٌ واضح، بلا ضجيج.", "voiceDo": "هكذا نكتب", "voiceDont": "وليس هكذا",
  "contactEyebrow": "تواصل", "contactTitle": "سلِّم علينا.", "contactSub": "للأسئلة والتعاون والملاحظات.",
  "fName": "الاسم", "fNamePh": "مثال: ليلى الكفافي", "fEmail": "البريد", "fEmailPh": "you@example.com", "fMsg": "رسالتك", "fMsgPh": "اكتب رسالتك هنا…", "fSend": "إرسال",
  "cWeb": "الموقع", "cEmail": "البريد", "cGithub": "المستودعات",
  "footerTagline": "أدواتٌ صغيرة دقيقة وهادئة للحياة اليومية.", "footerStudio": "الاستوديو", "rights": "كفافي. أدواتٌ تفعل ما يكفي فقط.", "madeWith": "يعكس kefafi_ui_kit",
  "langOther": "EN", "themeLabel": "السمة",
 },
 "en": {
  "navHome": "Home", "navProducts": "Products", "navAbout": "Studio", "navContact": "Contact",
  "studioEyebrow": "Independent software studio",
  "heroTitle": "Tools that do just enough.",
  "heroSub": "Kefafi is an independent studio making small, precise, calm tools for everyday personal life. Each one does a single thing well, then gets out of your way.",
  "heroCta": "See the products", "heroCta2": "About the studio",
  "productsEyebrow": "Products", "productsTitle": "Four tools.", "productsSub": "Built on the same principles and the same shared kit.",
  "viewLabel": "Learn more",
  "principlesEyebrow": "How we build", "principlesTitle": "A few principles, kept.",
  "closingEyebrow": "Get in touch", "closingTitle": "An idea, or a question?", "closingSub": "We'd love to hear from you.",
  "backLabel": "All products", "featuresTitle": "What it does", "partOf": "Part of Kefafi", "partOfSub": "One of four tools, built with the same calm.", "ctaGithub": "On GitHub", "privacyLabel": "Privacy policy",
  "aboutEyebrow": "The studio", "aboutTitle": "Just enough.",
  "aboutP1": "Kefafi is a small, independent software studio. We make calm tools for everyday personal life — software that does one thing well, then gets out of your way.",
  "aboutP2": "We build Arabic-first and offline-where-we-can. Your data stays yours. Our interfaces are warm, single-accent, and quiet.",
  "voiceEyebrow": "How we write", "voiceTitle": "Plain words, no hype.", "voiceDo": "We write", "voiceDont": "Not this",
  "contactEyebrow": "Get in touch", "contactTitle": "Say hello.", "contactSub": "For questions, collaboration, and feedback.",
  "fName": "Name", "fNamePh": "e.g. Layla Kefafi", "fEmail": "Email", "fEmailPh": "you@example.com", "fMsg": "Message", "fMsgPh": "Write your message here…", "fSend": "Send",
  "cWeb": "Website", "cEmail": "Email", "cGithub": "Repositories",
  "footerTagline": "Small, precise, calm tools for everyday personal life.", "footerStudio": "Studio", "rights": "Kefafi. Tools that do just enough.", "madeWith": "Mirrors kefafi_ui_kit",
  "langOther": "ع", "themeLabel": "Theme",
 },
}

GITHUB = "https://github.com/kfafi"
EMAIL = "hello@kefafi.dev"
DOMAIN = "https://kefafi.dev"

THEME_HEAD = ('<script>(function(){try{var t=localStorage.getItem("kf-theme");'
              'if(t)document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>')
THEME_BODY = ('<script>(function(){var b=document.getElementById("theme-toggle");if(!b)return;'
              'b.addEventListener("click",function(){var c=document.documentElement.getAttribute("data-theme");'
              'var s=window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches;'
              'var d=c?c==="dark":s;var n=d?"light":"dark";'
              'document.documentElement.setAttribute("data-theme",n);'
              'try{localStorage.setItem("kf-theme",n);}catch(e){}});})();</script>')

THEME_SVG = ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 0 0 18z" fill="currentColor" stroke="none"/></svg>')
CHECK_SVG = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>')
GLOBE_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/>'
             '<line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>')
MAIL_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>')
GH_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>')

def e(s): return html.escape(s, quote=False)

def base(lang): return "/en" if lang == "en" else ""
def alt(lang): return "en" if lang == "ar" else "ar"
def arrow(lang): return "←" if lang == "ar" else "→"
def back_arrow(lang): return "→" if lang == "ar" else "←"

def prod_url(lang, pid): return base(lang) + "/" + pid + "/"
def by_id(pid): return next(p for p in PRODUCTS if p["id"] == pid)

def tile_cls(tile): return "mono-tile--ink" if tile == "ink" else "mono-tile--clay"

# ---------------------------------------------------------------- chrome
def head(lang, title, desc, canonical, alt_url, extra=""):
    dirr = "rtl" if lang == "ar" else "ltr"
    og_locale = "ar_SA" if lang == "ar" else "en_US"
    og_alt = "en_US" if lang == "ar" else "ar_SA"
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dirr}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="ar" href="{alt_url['ar']}">
  <link rel="alternate" hreflang="en" href="{alt_url['en']}">
  <link rel="alternate" hreflang="x-default" href="{alt_url['ar']}">
  <meta name="theme-color" content="#F5F1E8" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#161310" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Kefafi">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:locale:alternate" content="{og_alt}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(desc)}">
  {THEME_HEAD}
  <link rel="stylesheet" href="/styles.css">
  <link rel="icon" href="{extra or '/favicon.svg'}" type="image/svg+xml">
</head>
<body>"""

def header(lang, active, alt_url):
    t = T[lang]; b = base(lang)
    def nav(href, key, is_active):
        cur = ' aria-current="page"' if is_active else ''
        return f'<a href="{href}"{cur}>{e(t[key])}</a>'
    nav_html = "".join([
        nav(b + "/", "navHome", active == "home"),
        nav(b + "/#products", "navProducts", False),
        nav(b + "/about/", "navAbout", active == "about"),
        nav(b + "/contact/", "navContact", active == "contact"),
    ])
    lang_link = alt_url[alt(lang)]
    return f"""  <header class="site-header">
    <div class="site-header__inner">
      <a class="wordmark" href="{b}/">
        <span class="wordmark__latin">kefafi<span class="wordmark__dot">.</span></span>
        <span class="wordmark__ar">كفافي</span>
      </a>
      <nav class="site-nav">{nav_html}</nav>
      <div class="header-tools">
        <a class="tool-btn" href="{lang_link}" hreflang="{alt(lang)}" title="{e(t['langOther'])}">{e(t['langOther'])}</a>
        <button class="tool-btn tool-btn--icon" id="theme-toggle" type="button" aria-label="{e(t['themeLabel'])}" title="{e(t['themeLabel'])}">{THEME_SVG}</button>
      </div>
    </div>
  </header>
"""

def footer(lang):
    t = T[lang]; b = base(lang)
    prod_links = "".join(
        f'<a href="{prod_url(lang, p["id"])}">{e(p["name"])}</a>' for p in PRODUCTS)
    return f"""  <footer class="site-footer">
    <div class="site-footer__inner">
      <div class="site-footer__top">
        <div class="site-footer__brand">
          <a class="wordmark" href="{b}/">
            <span class="wordmark__latin">kefafi<span class="wordmark__dot">.</span></span>
            <span class="wordmark__ar">كفافي</span>
          </a>
          <p class="site-footer__tagline">{e(t['footerTagline'])}</p>
        </div>
        <div class="footer-cols">
          <div>
            <div class="footer-col__head">{e(t['navProducts'])}</div>
            <div class="footer-col__links">{prod_links}</div>
          </div>
          <div>
            <div class="footer-col__head">{e(t['footerStudio'])}</div>
            <div class="footer-col__links">
              <a href="{b}/about/">{e(t['navAbout'])}</a>
              <a href="{b}/contact/">{e(t['navContact'])}</a>
              <a href="/nasab/privacy/">Nasab {e(t['privacyLabel'])}</a>
              <a href="/daftar/privacy/">Daftar {e(t['privacyLabel'])}</a>
              <a href="/sayla/privacy/">Sayla {e(t['privacyLabel'])}</a>
            </div>
          </div>
        </div>
      </div>
      <div class="site-footer__bottom">
        <span>&copy; <span class="mono">2026</span> &middot; {e(t['rights'])}</span>
        <span class="mono">{e(t['madeWith'])}</span>
      </div>
    </div>
  </footer>
  {THEME_BODY}
</body>
</html>"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

# ---------------------------------------------------------------- pages
def page_home(lang):
    t = T[lang]; b = base(lang)
    alt_url = {"ar": "/", "en": "/en/"}
    canonical = DOMAIN + (b + "/")
    tiles = "".join(f"""        <a class="tile" href="{prod_url(lang, p['id'])}">
          <span class="mono-tile {tile_cls(p['tile'])} mono-tile--lg">{p['mono']}</span>
          <span class="tile__name">{e(p['name'])}</span>
        </a>""" for p in PRODUCTS)
    cards = "".join(f"""        <a class="card" href="{prod_url(lang, p['id'])}">
          <div class="card__row">
            <span class="mono-tile {tile_cls(p['tile'])} mono-tile--md">{p['mono']}</span>
            <div class="card__body">
              <div class="card__title"><span class="card__name">{e(p['name'])}</span><span class="card__ar">{p['ar']}</span></div>
              <p class="card__desc">{e(p['line'][lang])}</p>
              <span class="card__cta">{e(t['viewLabel'])}<span class="mono">{arrow(lang)}</span></span>
            </div>
          </div>
        </a>""" for p in PRODUCTS)
    principles = "".join(f"""        <div class="grid-rule__cell">
          <div class="grid-rule__num">{i+1:02d}</div>
          <h3>{e(pr['title'][lang])}</h3>
          <p>{e(pr['body'][lang])}</p>
        </div>""" for i, pr in enumerate(PRINCIPLES))
    title = "Kefafi — " + (t['heroTitle'] if lang == "ar" else "tools that do just enough")
    desc = t['heroSub']
    return head(lang, title, desc, canonical, alt_url) + header(lang, "home", alt_url) + f"""  <main>
    <section class="hero wrap">
      <div class="hero__grid">
        <div>
          <p class="eyebrow">{e(t['studioEyebrow'])}</p>
          <h1 class="display">{e(t['heroTitle'])}</h1>
          <p class="hero__sub">{e(t['heroSub'])}</p>
          <div class="btn-row">
            <a class="btn btn--primary btn--lg" href="{b}/#products">{e(t['heroCta'])}</a>
            <a class="btn btn--outline btn--lg" href="{b}/about/">{e(t['heroCta2'])}</a>
          </div>
        </div>
        <div class="tile-grid">
{tiles}
        </div>
      </div>
    </section>

    <section class="band" id="products">
      <div class="wrap section">
        <div class="section-head">
          <p class="eyebrow">{e(t['productsEyebrow'])}</p>
          <h2>{e(t['productsTitle'])}</h2>
          <p>{e(t['productsSub'])}</p>
        </div>
        <div class="cards">
{cards}
        </div>
      </div>
    </section>

    <section class="wrap section">
      <div class="section-head">
        <p class="eyebrow">{e(t['principlesEyebrow'])}</p>
        <h2>{e(t['principlesTitle'])}</h2>
      </div>
      <div class="grid-rule">
{principles}
      </div>
    </section>

    <section class="band-surface">
      <div class="wrap section closing">
        <div>
          <p class="eyebrow">{e(t['closingEyebrow'])}</p>
          <h2>{e(t['closingTitle'])}</h2>
          <p>{e(t['closingSub'])}</p>
        </div>
        <a class="btn btn--primary btn--lg" href="{b}/contact/">{e(t['navContact'])}</a>
      </div>
    </section>
  </main>
""" + footer(lang)

def page_product(lang, p):
    t = T[lang]; b = base(lang)
    pid = p["id"]
    alt_url = {"ar": "/" + pid + "/", "en": "/en/" + pid + "/"}
    canonical = DOMAIN + prod_url(lang, pid)
    badges = "".join(f'<span class="badge">{e(pf)}</span>' for pf in p["platforms"])
    features = "".join(f"""        <div class="feature">
          <span class="feature__check">{CHECK_SVG}</span>
          <span>{e(f[lang])}</span>
        </div>""" for f in p["features"])
    others = [o for o in PRODUCTS if o["id"] != pid]
    chips = "".join(f"""          <a class="chip" href="{prod_url(lang, o['id'])}">
            <span class="mono-tile {tile_cls(o['tile'])} mono-tile--sm">{o['mono']}</span>
            <span>{e(o['name'])}</span>
          </a>""" for o in others)
    privacy_link = ""
    if p.get("privacy"):
        privacy_link = f'\n            <a class="btn btn--ghost" href="/{pid}/privacy/">{e(t["privacyLabel"])}</a>'
    title = f"{p['name']} — {p['tagline'][lang]}"
    desc = p["line"][lang]
    return head(lang, title, desc, canonical, alt_url, extra=f"/{pid}/favicon.svg") + header(lang, None, alt_url) + f"""  <main class="wrap">
    <a class="back-link" href="{b}/#products"><span class="mono">{back_arrow(lang)}</span>{e(t['backLabel'])}</a>

    <section class="prod-hero">
      <span class="mono-tile {tile_cls(p['tile'])} mono-tile--xl">{p['mono']}</span>
      <div class="prod-hero__body">
        <div class="prod-hero__title"><h1>{e(p['name'])}</h1><span class="ar">{p['ar']}</span></div>
        <p class="prod-hero__tagline">{e(p['tagline'][lang])}</p>
        <p class="prod-hero__intro">{e(p['intro'][lang])}</p>
        <div class="badges">{badges}</div>
        <div class="btn-row">
          <a class="btn btn--primary" href="{GITHUB}" target="_blank" rel="noopener">{e(t['ctaGithub'])}</a>
          <a class="btn btn--ghost" href="{b}/contact/">{e(t['navContact'])}</a>{privacy_link}
        </div>
      </div>
    </section>

    <section class="section--tight">
      <p class="eyebrow">{e(t['featuresTitle'])}</p>
      <div class="features">
{features}
      </div>
    </section>

    <section class="section--tight">
      <div class="partof">
        <p class="partof__eyebrow">{e(t['partOf'])}</p>
        <p>{e(t['partOfSub'])}</p>
        <div class="chiprow">
{chips}
        </div>
      </div>
    </section>
  </main>
""" + footer(lang)

def page_about(lang):
    t = T[lang]
    alt_url = {"ar": "/about/", "en": "/en/about/"}
    canonical = DOMAIN + base(lang) + "/about/"
    do = "".join(f"<p>{e(v)}</p>" for v in VOICE[lang]["do"])
    dont = "".join(f"<p>{e(v)}</p>" for v in VOICE[lang]["dont"])
    principles = "".join(f"""        <div class="grid-rule__cell">
          <div class="grid-rule__num">{i+1:02d}</div>
          <h3>{e(pr['title'][lang])}</h3>
          <p>{e(pr['body'][lang])}</p>
        </div>""" for i, pr in enumerate(PRINCIPLES))
    title = f"{t['navAbout']} — Kefafi"
    return head(lang, title, t['aboutP1'], canonical, alt_url) + header(lang, "about", alt_url) + f"""  <main class="wrap section">
    <div class="text-col">
      <section>
        <p class="eyebrow">{e(t['aboutEyebrow'])}</p>
        <h1 class="display" style="font-size:clamp(36px,6vw,60px);margin:0 0 28px;">{e(t['aboutTitle'])}</h1>
        <p class="about-lede">{e(t['aboutP1'])}</p>
        <p class="about-lede">{e(t['aboutP2'])}</p>
      </section>

      <section style="margin-top:56px;padding-top:48px;border-top:1px solid var(--ink-100);">
        <p class="eyebrow">{e(t['voiceEyebrow'])}</p>
        <h2 class="display" style="font-size:clamp(26px,4vw,34px);margin:0 0 28px;">{e(t['voiceTitle'])}</h2>
        <div class="voice">
          <div class="voice__card">
            <div class="voice__tag voice__tag--do">{CHECK_SVG}<span>{e(t['voiceDo'])}</span></div>
            {do}
          </div>
          <div class="voice__card voice__card--dont">
            <div class="voice__tag voice__tag--dont"><span>{e(t['voiceDont'])}</span></div>
            {dont}
          </div>
        </div>
      </section>

      <section style="margin-top:48px;">
        <div class="grid-rule">
{principles}
        </div>
      </section>
    </div>
  </main>
""" + footer(lang)

def page_contact(lang):
    t = T[lang]
    alt_url = {"ar": "/contact/", "en": "/en/contact/"}
    canonical = DOMAIN + base(lang) + "/contact/"
    title = f"{t['navContact']} — Kefafi"
    return head(lang, title, t['contactSub'], canonical, alt_url) + header(lang, "contact", alt_url) + f"""  <main class="wrap section">
    <section class="text-col" style="margin-bottom:44px;">
      <p class="eyebrow">{e(t['contactEyebrow'])}</p>
      <h1 class="display" style="font-size:clamp(36px,6vw,58px);margin:0 0 16px;">{e(t['contactTitle'])}</h1>
      <p class="hero__sub" style="margin:0;">{e(t['contactSub'])}</p>
    </section>

    <div class="contact-grid text-col">
      <form class="form-card" action="mailto:{EMAIL}" method="post" enctype="text/plain">
        <div class="field">
          <label for="cf-name">{e(t['fName'])}</label>
          <input id="cf-name" name="name" type="text" placeholder="{e(t['fNamePh'])}" autocomplete="name">
        </div>
        <div class="field">
          <label for="cf-email">{e(t['fEmail'])}</label>
          <input id="cf-email" name="email" type="email" placeholder="{e(t['fEmailPh'])}" autocomplete="email">
        </div>
        <div class="field">
          <label for="cf-msg">{e(t['fMsg'])}</label>
          <textarea id="cf-msg" name="message" rows="5" placeholder="{e(t['fMsgPh'])}"></textarea>
        </div>
        <button class="btn btn--primary btn--lg" type="submit">{e(t['fSend'])}</button>
      </form>

      <div class="contact-cards">
        <a class="contact-card" href="{DOMAIN}">
          <span class="contact-card__icon">{GLOBE_SVG}</span>
          <span><span class="contact-card__label">{e(t['cWeb'])}</span><span class="contact-card__value" dir="ltr">kefafi.dev</span></span>
        </a>
        <a class="contact-card" href="mailto:{EMAIL}">
          <span class="contact-card__icon">{MAIL_SVG}</span>
          <span><span class="contact-card__label">{e(t['cEmail'])}</span><span class="contact-card__value" dir="ltr">{EMAIL}</span></span>
        </a>
        <a class="contact-card" href="{GITHUB}" target="_blank" rel="noopener">
          <span class="contact-card__icon">{GH_SVG}</span>
          <span><span class="contact-card__label">{e(t['cGithub'])}</span><span class="contact-card__value" dir="ltr">github.com/kfafi</span></span>
        </a>
      </div>
    </div>
  </main>
""" + footer(lang)

# ---------------------------------------------------------------- favicons
def favicon(mono, tile):
    bg = "#1C1815" if tile == "ink" else "#C0502A"
    fg = "#F5F1E8" if tile == "ink" else "#F8F4EC"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img">
  <rect width="64" height="64" rx="16" fill="{bg}"/>
  <text x="32" y="34" text-anchor="middle" dominant-baseline="central"
        font-family="'IBM Plex Sans Arabic','Reem Kufi','Segoe UI',sans-serif"
        font-size="40" font-weight="600" fill="{fg}">{mono}</text>
</svg>
"""

# ---------------------------------------------------------------- sitemap
def sitemap():
    urls = []
    def add(loc, freq, pri):
        urls.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>2026-06-23</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""")
    add(DOMAIN + "/", "monthly", "1.0")
    add(DOMAIN + "/en/", "monthly", "0.9")
    for sub in ["about", "contact"]:
        add(f"{DOMAIN}/{sub}/", "monthly", "0.6")
        add(f"{DOMAIN}/en/{sub}/", "monthly", "0.5")
    for p in PRODUCTS:
        add(f"{DOMAIN}/{p['id']}/", "monthly", "0.8")
        add(f"{DOMAIN}/en/{p['id']}/", "monthly", "0.7")
    add(DOMAIN + "/nasab/privacy/", "yearly", "0.4")
    add(DOMAIN + "/daftar/privacy/", "yearly", "0.4")
    add(DOMAIN + "/sayla/privacy/", "yearly", "0.4")
    body = "\n".join(urls)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""

# ---------------------------------------------------------------- emit
for lang in ("ar", "en"):
    pref = "en/" if lang == "en" else ""
    write(pref + "index.html", page_home(lang))
    write(pref + "about/index.html", page_about(lang))
    write(pref + "contact/index.html", page_contact(lang))
    for p in PRODUCTS:
        write(pref + p["id"] + "/index.html", page_product(lang, p))

write("nasab/favicon.svg", favicon("ن", "ink"))
write("lumen/favicon.svg", favicon("ل", "ink"))
write("sayla/favicon.svg", favicon("س", "clay"))
write("sitemap.xml", sitemap())
print("done")
