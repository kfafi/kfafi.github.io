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
  "backLabel": "كل المنتجات", "featuresTitle": "ماذا يفعل", "partOf": "جزء من كفافي", "partOfSub": "أداةٌ واحدة من أربع، مبنيّة بنفس الهدوء.", "ctaGithub": "على GitHub", "privacyLabel": "سياسة الخصوصية", "termsLabel": "شروط الاستخدام", "supportLabel": "الدعم",
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
  "backLabel": "All products", "featuresTitle": "What it does", "partOf": "Part of Kefafi", "partOfSub": "One of four tools, built with the same calm.", "ctaGithub": "On GitHub", "privacyLabel": "Privacy policy", "termsLabel": "Terms of Service", "supportLabel": "Support",
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
              <a href="{b}/nasab/privacy/">Nasab {e(t['privacyLabel'])}</a>
              <a href="{b}/nasab/terms/">Nasab {e(t['termsLabel'])}</a>
              <a href="{b}/nasab/support/">Nasab {e(t['supportLabel'])}</a>
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
    legal_row = ""
    if pid == "nasab":
        legal_row = (f'\n        <p class="legal-links">'
                     f'<a href="{b}/nasab/privacy/">{e(t["privacyLabel"])}</a>'
                     f'<span class="sep">&middot;</span>'
                     f'<a href="{b}/nasab/terms/">{e(t["termsLabel"])}</a>'
                     f'<span class="sep">&middot;</span>'
                     f'<a href="{b}/nasab/support/">{e(t["supportLabel"])}</a></p>')
    elif p.get("privacy"):
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
        </div>{legal_row}
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

# ---------------------------------------------------------------- nasab legal/support
# %%B%% is replaced with the language base ("" for AR, "/en" for EN) at render time.
NASAB_PAGES = {
 "privacy": {
  "eyebrow": {"ar": "سياسة الخصوصية", "en": "Privacy Policy"},
  "h1": {"ar": "سياسة الخصوصية — نسب", "en": "Privacy Policy — Nasab"},
  "title": {"ar": "سياسة الخصوصية — نسب", "en": "Privacy Policy — Nasab"},
  "desc": {"ar": "سياسة خصوصية تطبيق نسب: خاص افتراضياً، الأحياء خاصون، لا إعلانات ولا تتبّع، والبيانات لا تُباع.",
           "en": "Nasab's privacy policy: private by default, living people private, no ads or tracking, data never sold."},
  "meta": {"ar": "آخر تحديث 23 يونيو 2026", "en": "Last updated 23 June 2026"},
  "body": {"ar": """
      <p>
        نسب من صناعة <strong>الكفافي</strong> («نحن»). نسب تطبيق <strong>خاص</strong>
        لشجرة العائلة موجّه للعائلات العربية، و<strong>ليس شبكة اجتماعية</strong>: لا
        موجز عام، ولا اكتشاف، ولا دليل مشترك. توضّح هذه السياسة ما الذي نجمعه وكيف
        نستخدمه ونحميه.
      </p>
      <p>
        حتى تصل إلى شجرتك من أجهزتك وتشاركها مع من تختار، يحفظ نسب بياناتك على خادم
        آمن لدى مزوّد الخدمة، <strong>تحت تحكّمك</strong>. المبدأ الأساسي: أنت تملك
        شجرتك، وتتحكّم بمن يراها، وتسحب الوصول متى شئت.
      </p>

      <h2>ما الذي نجمعه</h2>
      <ul>
        <li><strong>حسابك:</strong> بريدك الإلكتروني وكلمة المرور (تُخزَّن مُجزّأة hashed، ولا نراها)، واسم عرض ولغة مفضّلة اختياريان.</li>
        <li><strong>ملاحظة حول البريد:</strong> لا يتحقّق التطبيق من ملكيتك للبريد الإلكتروني. <strong>استخدم بريداً تملكه</strong>، فهو وسيلتك لاستعادة كلمة المرور ولاستقبال الدعوات.</li>
        <li><strong>محتوى الشجرة الذي تُدخله:</strong> أسماء الأقارب (بالعربية واللاتينية)، والجنس، وصلات القرابة والزواج، وتواريخ الميلاد والوفاة (هجري وميلادي)، والأماكن، والنبذ التعريفية، و<strong>روابط الصور التي تزوّدنا بها</strong> (نخزّن الرابط الذي تكتبه، لا ملفات صور مرفوعة)، والانتماءات القبلية، وإعدادات الخصوصية لكل سجل.</li>
        <li><strong>بيانات المشاركة:</strong> عناوين البريد التي تدعوها والأدوار التي تمنحها.</li>
        <li><strong>سجلات تقنية:</strong> سجلات خادم اعتيادية (عنوان IP وطوابع زمنية) يحتفظ بها مزوّد البنية التحتية.</li>
      </ul>

      <h2>كيف نستخدم بياناتك</h2>
      <p>
        نستخدمها لتشغيل التطبيق فقط: للتحقق من دخولك، وحفظ شجرتك وعرضها، وفرض إعدادات
        الخصوصية والمشاركة التي تختارها، والحفاظ على أمان الخدمة. لا نستخدمها لأي غرض آخر.
      </p>

      <h2>ما لا نفعله</h2>
      <ul>
        <li><strong>لا إعلانات.</strong></li>
        <li><strong>لا تتبّع ولا تحليلات من طرف ثالث.</strong></li>
        <li><strong>لا نبيع بياناتك أبداً.</strong></li>
      </ul>

      <h2>أين تُخزَّن بياناتك وأمنها</h2>
      <p>
        تُخزَّن بياناتك في قاعدة بيانات <strong>Supabase</strong> (Postgres) مع أمان على
        مستوى الصف (Row-Level Security)، وهي <strong>خاصة افتراضياً</strong>.
        <strong>الأشخاص الأحياء خاصون افتراضياً.</strong> تنتقل البيانات عبر اتصالات
        مشفّرة (HTTPS)، وكلمات المرور تُخزَّن مُجزّأة.
      </p>

      <h2>المشاركة والخصوصية</h2>
      <p>
        المشاركة بيدك وعلى مستوى كل شجرة: تدعو شخصاً برابط وتمنحه دور
        <strong>مُطّلِع</strong> (قراءة) أو <strong>محرِّر</strong>، ويمكنك سحب الوصول في
        أي وقت. ولكل سجلٍّ مستوى ظهوره الخاص، والأحياء خاصون افتراضياً.
      </p>

      <h2>بيانات عن أشخاص آخرين</h2>
      <p>
        بطبيعته، يسجّل نسب أفراد العائلة، وقد يكون بينهم قُصّر. أنت مسؤول عمّا تُدخله،
        وعليك أن تملك الحق أو الإذن في تسجيل بيانات غيرك. الإعدادات الافتراضية تحمي
        الأحياء، ويمكن لأي شخص مراسلتنا لمراجعة بياناته أو إزالتها.
      </p>

      <h2>حقوقك</h2>
      <ul>
        <li><strong>الاطلاع والتصحيح:</strong> تعرض بياناتك وتعدّلها داخل التطبيق.</li>
        <li><strong>التصدير:</strong> تصدّر شجرتك بصيغة <strong>GEDCOM</strong>.</li>
        <li><strong>الحذف:</strong> تحذف حسابك وكل بياناتك — انظر <a href="%%B%%/nasab/support/#delete">حذف الحساب</a>.</li>
      </ul>

      <h2>حذف الحساب والبيانات</h2>
      <p>
        يمكنك حذف حسابك من داخل التطبيق في أي وقت: القائمة ← «حذف الحساب» ← تأكيد. يحذف
        ذلك حسابك، وكل شجرة تملكها وما فيها من أشخاص وزيجات، وكل صلاحيات المشاركة من
        حسابك وإليه — <strong>فوراً وبلا رجعة</strong>. تبقى القبائل التي أنشأتها مرجعاً
        مشتركاً لغيرك. إن تعذّر عليك الدخول، راسلنا على
        <a href="mailto:support@kefafi.dev">support@kefafi.dev</a> لإتمام الحذف.
        التفاصيل في <a href="%%B%%/nasab/support/#delete">صفحة الدعم</a>.
      </p>

      <h2>مزوّدو الخدمة</h2>
      <p>
        نعتمد على <strong>Supabase</strong> للاستضافة والمصادقة وقاعدة البيانات؛ تُخزَّن
        بياناتك على بنيتها التحتية المُدارة، ويحكم ذلك
        <a href="https://supabase.com/privacy">سياسة خصوصية Supabase</a>. لا يدمج نسب أي
        مزوّد إعلانات أو تحليلات أو تتبّع.
      </p>

      <h2>الأطفال</h2>
      <p>
        التطبيق ليس موجَّهاً للأطفال كمستخدمين. قد تتضمّن الشجرة قُصّراً يُدخلهم مالكها،
        وتحميهم إعدادات خصوصية الأحياء الافتراضية. لطلب إزالة بيانات قاصر، راسلنا.
      </p>

      <h2>التغييرات على هذه السياسة</h2>
      <p>إذا غيّرنا هذه السياسة، سنحدّث التاريخ في الأعلى وننشر النسخة الجديدة على العنوان نفسه.</p>

      <h2>للتواصل</h2>
      <p><strong>الكفافي</strong> &mdash; <a href="mailto:support@kefafi.dev">support@kefafi.dev</a></p>
""", "en": """
      <p>
        Nasab is made by <strong>Kefafi</strong> (&ldquo;we&rdquo;, &ldquo;us&rdquo;).
        Nasab is a <strong>private</strong> family-tree app for Arab families. It is
        <strong>not a social network</strong>: there is no public feed, no discovery,
        and no shared directory. This policy explains what we collect and how we use
        and protect it.
      </p>
      <p>
        So you can reach your tree from your devices and share it with people you
        choose, Nasab stores your data on a secure server with our service provider,
        <strong>under your control</strong>. The core principle: you own your tree, you
        control who sees it, and you can revoke access at any time.
      </p>

      <h2>What we collect</h2>
      <ul>
        <li><strong>Your account:</strong> your email address and password (stored hashed — we never see it), and an optional display name and preferred language.</li>
        <li><strong>About email:</strong> the app does <strong>not</strong> verify that you own the email address. <strong>Use an email you control</strong> — it is how you reset your password and receive invitations.</li>
        <li><strong>The tree content you enter:</strong> relatives' names (Arabic and Latin), gender, relationships and marriages, birth/death dates (Hijri and Gregorian), places, biographies, <strong>photo URLs you provide</strong> (we store the link you enter, not uploaded image files), tribe affiliations, and per-record privacy settings.</li>
        <li><strong>Sharing data:</strong> the email addresses you invite and the roles you grant them.</li>
        <li><strong>Technical logs:</strong> standard server logs (IP address, timestamps) kept by our infrastructure provider.</li>
      </ul>

      <h2>How we use it</h2>
      <p>
        We use it only to run the app: to sign you in, store and display your tree,
        enforce the privacy and sharing settings you choose, and keep the service
        secure. Nothing else.
      </p>

      <h2>What we don't do</h2>
      <ul>
        <li><strong>No advertising.</strong></li>
        <li><strong>No third-party analytics or tracking.</strong></li>
        <li><strong>We never sell your data.</strong></li>
      </ul>

      <h2>Where your data is stored, and security</h2>
      <p>
        Your data is stored in a <strong>Supabase</strong> (Postgres) database with
        Row-Level Security and is <strong>private by default</strong>.
        <strong>Living people are private by default.</strong> Data travels over
        encrypted connections (HTTPS), and passwords are stored hashed.
      </p>

      <h2>Sharing and privacy</h2>
      <p>
        Sharing is yours to control, per tree: you invite someone with a link and grant
        a <strong>viewer</strong> (read) or <strong>editor</strong> role, and you can
        revoke access at any time. Every record has its own visibility, and living
        people are private by default.
      </p>

      <h2>Data about other people</h2>
      <p>
        By its nature, Nasab records family members, who may include minors. You are
        responsible for what you enter and must have the right or consent to record
        other people's information. Defaults protect the living, and anyone may contact
        us to review or remove their data.
      </p>

      <h2>Your rights</h2>
      <ul>
        <li><strong>Access and correction:</strong> view and edit your data in the app.</li>
        <li><strong>Export:</strong> export your tree as <strong>GEDCOM</strong>.</li>
        <li><strong>Deletion:</strong> delete your account and all your data — see <a href="%%B%%/nasab/support/#delete">Account deletion</a>.</li>
      </ul>

      <h2>Account and data deletion</h2>
      <p>
        You can delete your account from inside the app at any time: menu &rarr;
        &ldquo;Delete account&rdquo; &rarr; confirm. This deletes your account, every
        tree you own and all the people and marriages in them, and all sharing grants to
        and from your account &mdash; <strong>immediately and permanently</strong>.
        Tribes you created remain as shared reference for others. If you cannot sign in,
        email <a href="mailto:support@kefafi.dev">support@kefafi.dev</a> and we will do
        it for you. Full details on the <a href="%%B%%/nasab/support/#delete">support page</a>.
      </p>

      <h2>Service providers</h2>
      <p>
        We rely on <strong>Supabase</strong> for hosting, authentication, and the
        database; your data is stored on its managed infrastructure, governed by
        <a href="https://supabase.com/privacy">Supabase's Privacy Policy</a>. Nasab
        integrates no advertising, analytics, or tracking provider.
      </p>

      <h2>Children</h2>
      <p>
        The app is not directed at children as users. A tree may include minors entered
        by its owner; the living-person privacy defaults protect them. To request
        removal of a minor's data, contact us.
      </p>

      <h2>Changes to this policy</h2>
      <p>If we change this policy, we will update the date above and post the new version at the same address.</p>

      <h2>Contact</h2>
      <p><strong>Kefafi</strong> &mdash; <a href="mailto:support@kefafi.dev">support@kefafi.dev</a></p>
"""}},

 "terms": {
  "eyebrow": {"ar": "شروط الاستخدام", "en": "Terms of Service"},
  "h1": {"ar": "شروط الاستخدام — نسب", "en": "Terms of Service — Nasab"},
  "title": {"ar": "شروط الاستخدام — نسب", "en": "Terms of Service — Nasab"},
  "desc": {"ar": "شروط استخدام تطبيق نسب لشجرة العائلة.",
           "en": "Terms of Service for the Nasab family-tree app."},
  "meta": {"ar": "آخر تحديث 23 يونيو 2026", "en": "Last updated 23 June 2026"},
  "body": {"ar": """
      <p>
        مرحباً بك في نسب، تطبيق شجرة العائلة من <strong>الكفافي</strong> («نحن»).
        باستخدامك نسب فإنك توافق على هذه الشروط. إن لم توافق عليها فلا تستخدم التطبيق.
      </p>

      <h2>الخدمة</h2>
      <p>
        نسب تطبيق <strong>خاص</strong> لبناء شجرة عائلتك وإدارتها ومشاركتها وفق إعداداتك.
        ليس شبكة اجتماعية: لا نشر عام، ولا اكتشاف، ولا دليل مشترك.
      </p>

      <h2>حسابك</h2>
      <p>
        لإنشاء حساب تزوّدنا ببريد إلكتروني وكلمة مرور. <strong>لا يتحقّق التطبيق من ملكيتك
        للبريد</strong>، فاستخدم بريداً تملكه. أنت مسؤول عن سرّية بيانات دخولك وعن كل نشاط
        يجري عبر حسابك.
      </p>

      <h2>محتواك ومسؤوليتك</h2>
      <p>
        أنت تملك ما تُدخله وتتحمّل مسؤوليته. وعند تسجيل بيانات عن أشخاص آخرين — ولا سيما
        الأحياء والقُصّر — يجب أن تملك الحق أو الإذن في ذلك. لا تُدخل محتوى مخالفاً للقانون
        أو منتهكاً لحقوق غيرك. أنت تمنحنا إذناً محدوداً بتخزين محتواك ومعالجته وعرضه لغرض
        تقديم الخدمة لك فقط — لا نبيعه ولا نستخدمه لغير ذلك.
      </p>

      <h2>الاستخدام المقبول</h2>
      <ul>
        <li>لا تستخدم نسب لأي غرض غير قانوني.</li>
        <li>لا تحاول اختراق خصوصية الآخرين أو أمن الخدمة أو الوصول غير المصرّح به.</li>
        <li>لا تُسئ استخدام الخدمة أو تعطّلها.</li>
      </ul>

      <h2>المشاركة</h2>
      <p>المشاركة بيدك وعلى مستوى كل شجرة (مُطّلِع أو محرِّر)، وقابلة للسحب في أي وقت. أنت مسؤول عمّن تمنحه الوصول.</p>

      <h2>الخصوصية</h2>
      <p>تحكم معالجتَنا لبياناتك <a href="%%B%%/nasab/privacy/">سياسة الخصوصية</a>، وهي جزء من هذه الشروط.</p>

      <h2>الخدمة «كما هي»</h2>
      <p>
        تُقدَّم الخدمة «كما هي» دون ضمانات. قد نعدّلها أو نوقفها أو نوقف ميزات منها. احتفظ
        بنسخك الخاصة عبر <strong>تصدير GEDCOM</strong> من داخل التطبيق.
      </p>

      <h2>حدود المسؤولية</h2>
      <p>
        إلى الحد الذي يسمح به النظام، لا نتحمّل مسؤولية أي أضرار غير مباشرة أو تبعية ناشئة
        عن استخدامك للخدمة، ولا عن فقدان بيانات لم تحتفظ بنسخة منها.
      </p>

      <h2>الإنهاء</h2>
      <p>
        يمكنك حذف حسابك في أي وقت (انظر <a href="%%B%%/nasab/support/#delete">حذف الحساب</a>).
        ولنا أن نوقف الوصول أو نُنهيه عند مخالفة هذه الشروط.
      </p>

      <h2>التغييرات على الشروط</h2>
      <p>قد نحدّث هذه الشروط؛ سننشر النسخة الجديدة على العنوان نفسه ونحدّث التاريخ أعلاه.</p>

      <h2>القانون الحاكم</h2>
      <p>تخضع هذه الشروط لأنظمة <strong>المملكة العربية السعودية</strong>.</p>

      <h2>للتواصل</h2>
      <p><strong>الكفافي</strong> &mdash; <a href="mailto:support@kefafi.dev">support@kefafi.dev</a></p>
""", "en": """
      <p>
        Welcome to Nasab, the family-tree app by <strong>Kefafi</strong>
        (&ldquo;we&rdquo;, &ldquo;us&rdquo;). By using Nasab you agree to these Terms.
        If you do not agree, do not use the app.
      </p>

      <h2>The service</h2>
      <p>
        Nasab is a <strong>private</strong> app for building, managing, and sharing your
        family tree according to your settings. It is not a social network: no public
        posting, no discovery, no shared directory.
      </p>

      <h2>Your account</h2>
      <p>
        To create an account you provide an email and password. The app
        <strong>does not verify that you own the email</strong>, so use an email you
        control. You are responsible for keeping your credentials safe and for activity
        under your account.
      </p>

      <h2>Your content and responsibility</h2>
      <p>
        You own and are responsible for what you enter. When you record information about
        other people &mdash; especially living people and minors &mdash; you must have
        the right or consent to do so. Do not enter content that is unlawful or infringes
        others' rights. You grant us a limited permission to store, process, and display
        your content solely to provide the service to you &mdash; we do not sell it or
        use it for anything else.
      </p>

      <h2>Acceptable use</h2>
      <ul>
        <li>Do not use Nasab for any unlawful purpose.</li>
        <li>Do not attempt to breach others' privacy, the security of the service, or gain unauthorized access.</li>
        <li>Do not misuse or disrupt the service.</li>
      </ul>

      <h2>Sharing</h2>
      <p>Sharing is yours to control, per tree (viewer or editor), and revocable at any time. You are responsible for whom you grant access.</p>

      <h2>Privacy</h2>
      <p>Our handling of your data is governed by the <a href="%%B%%/nasab/privacy/">Privacy Policy</a>, which is part of these Terms.</p>

      <h2>Service provided &ldquo;as is&rdquo;</h2>
      <p>
        The service is provided &ldquo;as is,&rdquo; without warranties. We may change,
        suspend, or discontinue features. Keep your own copies by using
        <strong>GEDCOM export</strong> in the app.
      </p>

      <h2>Limitation of liability</h2>
      <p>To the extent permitted by law, we are not liable for indirect or consequential damages arising from your use of the service, nor for loss of data you did not back up.</p>

      <h2>Termination</h2>
      <p>You may delete your account at any time (see <a href="%%B%%/nasab/support/#delete">Account deletion</a>). We may suspend or terminate access for violations of these Terms.</p>

      <h2>Changes to these Terms</h2>
      <p>We may update these Terms; we will post the new version at the same address and update the date above.</p>

      <h2>Governing law</h2>
      <p>These Terms are governed by the laws of the <strong>Kingdom of Saudi Arabia</strong>.</p>

      <h2>Contact</h2>
      <p><strong>Kefafi</strong> &mdash; <a href="mailto:support@kefafi.dev">support@kefafi.dev</a></p>
"""}},

 "support": {
  "eyebrow": {"ar": "الدعم", "en": "Support"},
  "h1": {"ar": "دعم نسب", "en": "Nasab Support"},
  "title": {"ar": "الدعم — نسب", "en": "Support — Nasab"},
  "desc": {"ar": "دعم نسب: أسئلة شائعة وكيفية حذف الحساب والبيانات.",
           "en": "Nasab support: FAQ and how to delete your account and data."},
  "meta": {"ar": "للمساعدة: support@kefafi.dev", "en": "Help: support@kefafi.dev"},
  "body": {"ar": """
      <p>نحن هنا للمساعدة. لأي سؤال أو مشكلة، راسلنا على <a href="mailto:support@kefafi.dev">support@kefafi.dev</a>.</p>

      <h2>الأسئلة الشائعة</h2>

      <h3>ما هو نسب؟</h3>
      <p>تطبيق خاص لبناء شجرة عائلتك ومشاركتها مع من تختار. ليس شبكة اجتماعية: لا موجز عام ولا اكتشاف.</p>

      <h3>كيف أعيد تعيين كلمة المرور؟</h3>
      <p>من شاشة تسجيل الدخول اختر «نسيت كلمة المرور؟» وأدخل بريدك، فيصلك <strong>رمز</strong>؛ ثم أدخل الرمز وكلمة المرور الجديدة.</p>

      <h3>لم يصلني الرمز.</h3>
      <p>بما أن التطبيق لا يتحقّق من ملكية البريد، تأكّد أنك استخدمت <strong>بريداً تملكه</strong> وكتبته بشكل صحيح، وافحص مجلد البريد غير المرغوب. إن استمرّت المشكلة فراسل الدعم.</p>

      <h3>كيف تعمل المشاركة؟</h3>
      <p>على مستوى كل شجرة: تدعو شخصاً برابط وتمنحه دور «مُطّلِع» أو «محرِّر»، ويمكنك سحب الوصول في أي وقت.</p>

      <h3>من يرى شجرتي؟</h3>
      <p>شجرتك خاصة افتراضياً، و<strong>الأشخاص الأحياء خاصون افتراضياً</strong>. أنت تتحكّم بظهور كل سجل.</p>

      <h3>كيف أصدّر بياناتي؟</h3>
      <p>يمكنك تصدير شجرتك بصيغة <strong>GEDCOM</strong> من داخل التطبيق.</p>

      <h3>كيف أصحّح معلومة؟</h3>
      <p>تعدّل أي سجل مباشرةً داخل التطبيق.</p>

      <h3>ماذا عن الصور؟</h3>
      <p>تزوّد نسب برابط الصورة؛ ويخزّن التطبيق الرابط لا ملف الصورة.</p>

      <h2 id="delete">حذف الحساب والبيانات</h2>
      <p>لحذف حسابك من داخل التطبيق: <strong>القائمة ← «حذف الحساب» ← تأكيد</strong>.</p>
      <p><strong>ماذا يُحذف:</strong></p>
      <ul>
        <li>حسابك (تسجيل الدخول).</li>
        <li>كل شجرة تملكها، وكل الأشخاص والزيجات فيها.</li>
        <li>كل صلاحيات المشاركة من حسابك وإليه.</li>
      </ul>
      <p>الحذف <strong>فوري ودائم ولا يمكن التراجع عنه</strong>.</p>
      <p><strong>ما الذي يبقى:</strong> القبائل التي أنشأتها تبقى مرجعاً مشتركاً يستفيد منه غيرك.</p>
      <p>إن تعذّر عليك تسجيل الدخول، راسلنا على <a href="mailto:support@kefafi.dev">support@kefafi.dev</a> من بريدك المسجَّل وسنتولّى الحذف.</p>

      <h2>للتواصل</h2>
      <p><strong>الكفافي</strong> &mdash; <a href="mailto:support@kefafi.dev">support@kefafi.dev</a></p>
""", "en": """
      <p>We're here to help. For any question or problem, email <a href="mailto:support@kefafi.dev">support@kefafi.dev</a>.</p>

      <h2>Frequently asked questions</h2>

      <h3>What is Nasab?</h3>
      <p>A private app for building and sharing your family tree with people you choose. It is not a social network: no public feed, no discovery.</p>

      <h3>How do I reset my password?</h3>
      <p>On the sign-in screen, choose &ldquo;Forgot password?&rdquo; and enter your email. You'll receive a <strong>code</strong>; enter the code and your new password.</p>

      <h3>I didn't get the code.</h3>
      <p>Because the app does not verify email ownership, make sure you used an <strong>email you own</strong> and typed it correctly, and check your spam folder. If it still doesn't arrive, contact support.</p>

      <h3>How does sharing work?</h3>
      <p>Per tree: you invite someone with a link and grant a &ldquo;viewer&rdquo; or &ldquo;editor&rdquo; role, and you can revoke access at any time.</p>

      <h3>Who can see my tree?</h3>
      <p>Your tree is private by default, and <strong>living people are private by default</strong>. You control the visibility of each record.</p>

      <h3>Can I export my data?</h3>
      <p>Yes — export your tree as <strong>GEDCOM</strong> from inside the app.</p>

      <h3>How do I correct information?</h3>
      <p>Edit any record directly in the app.</p>

      <h3>What about photos?</h3>
      <p>You give Nasab a photo URL; the app stores the link, not the image file.</p>

      <h2 id="delete">Account and data deletion</h2>
      <p>To delete your account from inside the app: <strong>menu &rarr; &ldquo;Delete account&rdquo; &rarr; confirm</strong>.</p>
      <p><strong>What is deleted:</strong></p>
      <ul>
        <li>Your account (your login).</li>
        <li>Every tree you own, and all people and marriages in them.</li>
        <li>All sharing grants to and from your account.</li>
      </ul>
      <p>Deletion is <strong>immediate, permanent, and irreversible</strong>.</p>
      <p><strong>What remains:</strong> tribes you created remain as shared reference for others.</p>
      <p>If you cannot sign in, email <a href="mailto:support@kefafi.dev">support@kefafi.dev</a> from your registered email and we will delete it for you.</p>

      <h2>Contact</h2>
      <p><strong>Kefafi</strong> &mdash; <a href="mailto:support@kefafi.dev">support@kefafi.dev</a></p>
"""}},
}

def page_legal(lang, slug):
    pg = NASAB_PAGES[slug]
    b = base(lang)
    alt_url = {"ar": f"/nasab/{slug}/", "en": f"/en/nasab/{slug}/"}
    canonical = DOMAIN + b + f"/nasab/{slug}/"
    body = pg["body"][lang].replace("%%B%%", b)
    nasab_name = "نسب" if lang == "ar" else "Nasab"
    return head(lang, pg["title"][lang], pg["desc"][lang], canonical, alt_url, extra="/nasab/favicon.svg") + header(lang, None, alt_url) + f"""  <main class="wrap">
    <a class="back-link" href="{b}/nasab/"><span class="mono">{back_arrow(lang)}</span>{nasab_name}</a>
    <div class="prose text-col">
      <p class="eyebrow">{e(pg['eyebrow'][lang])}</p>
      <h1>{e(pg['h1'][lang])}</h1>
      <p class="meta">{e(pg['meta'][lang])}</p>
{body}
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
    for slug in ["privacy", "terms", "support"]:
        add(f"{DOMAIN}/nasab/{slug}/", "yearly", "0.5")
        add(f"{DOMAIN}/en/nasab/{slug}/", "yearly", "0.4")
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
    for slug in ("privacy", "terms", "support"):
        write(pref + "nasab/" + slug + "/index.html", page_legal(lang, slug))

write("nasab/favicon.svg", favicon("ن", "ink"))
write("lumen/favicon.svg", favicon("ل", "ink"))
write("sayla/favicon.svg", favicon("س", "clay"))
write("sitemap.xml", sitemap())
print("done")
