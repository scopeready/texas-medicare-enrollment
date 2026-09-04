#!/usr/bin/env python3
"""ECOS Medicare Solutions — state-site static generator.

Run from the repo root:  python3 source/generate.py
Everything state-specific lives in source/content.py (SITE, HOME, NAV, CITIES,
REGIONS, BASES, TOPIC_PAGES, …) and source/scenes.py (hero art). This file is
the engine and is meant to be identical across the ECOS state sites.
"""
import json, re, html
from pathlib import Path

from scenes import SCENES
from content import (SITE, HOME, NAV, FOOTER_COLS, PLACE_CARDS, CITIES, REGIONS, BASES,
                     TOPIC_PAGES, ABOUT_BODY, FAQ_PAGE, PRIVACY_BODY, TERMS_BODY)

ROOT = Path(__file__).resolve().parent.parent
S = SITE
SITE_URL, ORG, PHONE, TEL, EMAIL, NPN = S["url"], S["org"], S["phone"], S["tel"], S["email"], S["npn"]
STATE, PLAN_YEAR, ISO, REVIEWED, FIG = S["state"], S["plan_year"], S["iso"], S["reviewed"], S["fig"]
NETWORK = S["network"]
SAMEAS_ORG = [u for _, u in NETWORK] + S.get("sameas_org_extra", [])
SAMEAS_DARIN = S["sameas_darin"]
# Optional state producer licence shown next to the NPN wherever Darin is named (California requires the
# licence number adjacent to the licensee's name, Cal. Ins. Code 1725.5). Absent on sites that do not need it.
LIC = S.get("state_license")          # e.g. "0M00978"
LIC_LABEL = S.get("state_license_label", "License")   # e.g. "CA License"
LIC_TXT = f", {LIC_LABEL} #{LIC}" if LIC else ""
REGION = {r["slug"]: r for r in REGIONS}
CITY = {c["slug"]: c for c in CITIES}
BASE = {b["slug"]: b for b in BASES}

def fill(s):
    for k, v in (("[[PHONE]]", PHONE), ("[[TEL]]", TEL), ("[[EMAIL]]", EMAIL), ("[[QUOTE]]", S["quote_url"]),
                 ("[[YEAR]]", str(PLAN_YEAR)), ("[[STATE]]", STATE), ("[[SHIP]]", S["ship_name"]), ("[[SHIPPHONE]]", S["ship_phone"])):
        s = s.replace(k, v)
    return s

def unesc(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

# ----------------------------------------------------------------------------
# Shared fragments
# ----------------------------------------------------------------------------
def header():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="/" aria-label="{ORG} home">
      {S["logo_svg"]}
      <span><span class="brand__name">{ORG}</span><br>
      <span class="brand__tag">{S["brand_tag"]}</span></span>
    </a>
    <nav class="nav" aria-label="Primary">
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="navLinks"><span class="visually-hidden">Menu</span><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
      <ul class="nav__links" id="navLinks">{links}</ul>
      <a class="header-call" href="tel:{TEL}">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3.1-8.7A2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg>
        {PHONE}
      </a>
    </nav>
  </div>
</header>
'''

def footer():
    cols = "".join(f'<div><h4>{h}</h4><ul>' + "".join(f'<li>{li}</li>' for li in items) + '</ul></div>' for h, items in FOOTER_COLS)
    cities = "".join(f'<li><a href="/{c["slug"]}">{c["name"]}</a></li>' for c in CITIES)
    regions = "".join(f'<li><a href="/{r["slug"]}">{r["name"]}</a></li>' for r in REGIONS)
    bases = ("<h4>Military communities</h4><ul>" + "".join(f'<li><a href="/{b["slug"]}">{b["name"]}</a></li>' for b in BASES) + "</ul>") if BASES else ""
    net = " &middot; ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in NETWORK)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <p class="footer-brand">{ORG}</p>
        <p style="margin-bottom:.6em">{S["footer_tagline"]}</p>
        <p><a href="tel:{TEL}"><strong>{PHONE}</strong></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="font-size:.85rem">Darin Weidauer, licensed insurance agent, NPN {NPN}{LIC_TXT}. Statewide by phone and video.</p>
      </div>
      {cols}
    </div>
    <nav class="footer-areas" aria-label="Areas we serve">
      <h4>Cities we serve</h4><ul>{cities}</ul>
      <h4>Regions</h4><ul>{regions}</ul>
      {bases}
    </nav>
    <div class="footer-net"><span>Our network of sites:</span> {net}</div>
    <div class="disclaimer">
      <p><strong>Medicare disclaimer.</strong> {S["tpmo"]}</p>
      <p>{ORG} is not connected with or endorsed by the U.S. government or the federal Medicare program, and is not affiliated with {S["not_affiliated"]}, the U.S. Department of Veterans Affairs, the Department of Defense, or the TRICARE program. This is a solicitation for insurance. A licensed insurance agent may contact you.</p>
      <p>Insurance products are offered through {ORG}. Darin Weidauer is a licensed insurance agent in {STATE} (NPN {NPN}{LIC_TXT}) and 16 other states. We may receive compensation from insurance carriers for policies we sell; you pay the same premium whether you enroll through us, another agent, or the carrier directly.</p>
      <p>&copy; <span id="yr">{ISO[:4]}</span> {ORG}. Not affiliated with any government agency.</p>
    </div>
  </div>
</footer>
<script src="/site.js" defer></script>
<script src="/analytics.js" defer></script>
'''

CONSENT_TEXT = ("By checking the consent box and submitting this form, I give ECOS Medicare Solutions and a licensed insurance agent "
                "permission to contact me at the phone number and email I provided — including by phone call, text message (SMS), and email, "
                "using automated technology such as an autodialer or prerecorded/artificial voice — about Medicare Advantage, Medicare Supplement, "
                "and Part D plan options. I understand consent is not a condition of purchase and that message and data rates may apply, "
                "and that I can opt out at any time.")

def lead_form(form_id, title="Request your free Medicare review", note=None, interest=True):
    note = note or f'Tell us a little about you and Darin will reach out. Prefer to talk now? Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a>.'
    sel = ""
    if interest:
        opts = "".join(f"<option>{o}</option>" for o in S["interest_options"])
        sel = f'''<div class="field"><label for="interest">What can we help with? (optional)</label>
          <select id="interest" name="interest"><option value="">Choose one…</option>{opts}</select></div>'''
    return f'''<div class="lead-card" id="get-help">
      <h2 class="lead-card__title">{title}</h2>
      <p class="lead-card__note">{note}</p>
      <form id="{form_id}" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="{S["web3forms_key"]}">
        <input type="hidden" name="subject" value="New Medicare review request — {S["domain"]}">
        <input type="hidden" name="from_name" value="{S["name"]}">
        <input type="hidden" name="redirect" value="{SITE_URL}/thank-you">
        <input type="hidden" name="consent_text" value="{html.escape(CONSENT_TEXT, quote=True)}">
        <input type="hidden" name="consent_timestamp" id="consent_timestamp" value="">
        <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="zip">ZIP code or city</label><input id="zip" name="zip_or_city" type="text" autocomplete="postal-code" required></div>
        {sel}
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="consent"><input id="consent" name="consent" type="checkbox" required>
          <label for="consent">By checking this box and submitting, I give ECOS Medicare Solutions and a licensed agent permission to contact me at the number and email above &mdash; by phone call, text (SMS), and email, including with automated technology &mdash; about Medicare plan options. Consent is not a condition of purchase. Message &amp; data rates may apply; I can opt out anytime.</label>
        </div>
        <button class="btn btn--primary btn--block btn--lg" type="submit">Get my free review</button>
        <p class="form-fineprint">We never ask about your health on this form. See our <a href="/privacy">Privacy Policy</a>. This is a solicitation for insurance. Not connected with or endorsed by the U.S. government or the federal Medicare program.</p>
      </form>
    </div>'''

def crumbs(items):
    parts = [f'<a href="{p}">{n}</a>' if p else f'<span>{n}</span>' for n, p in items]
    return ('<div class="wrap" style="padding-top:1.1rem"><nav class="eyebrow crumb" aria-label="Breadcrumb">'
            + ' <span aria-hidden="true">/</span> '.join(parts) + '</nav></div>')

def hero(scene, eyebrow, h1, sub, crumb_items, form_id, form_title="Talk it through with Darin"):
    return f'''<section class="hero">
  <div class="hero__scene" aria-hidden="true">{SCENES[scene]}</div>
  {crumbs(crumb_items)}
  <div class="wrap hero__inner" style="padding-top:.5rem">
    <div>
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="hero__sub">{sub}</p>
      <div class="hero__actions">
        <a class="btn btn--primary btn--lg" href="tel:{TEL}">Call {PHONE}</a>
        <a class="btn btn--ghost btn--lg" href="#get-help">Request a free review</a>
      </div>
      <p class="hero__nocost"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> No cost, no obligation, no pressure.</p>
    </div>
    {lead_form(form_id, form_title, f'No cost, no pressure. Prefer to call? <a href="tel:{TEL}"><strong>{PHONE}</strong></a>.')}
  </div>
</section>
'''

def faq_html(faqs, eyebrow="Good to know"):
    items = "".join(f'<details><summary>{q}</summary><div class="faq__a"><p>{a}</p></div></details>' for q, a in faqs)
    return f'''<section class="section section--paper2"><div class="wrap">
<p class="eyebrow center">{eyebrow}</p><h2 class="center">Frequently asked questions</h2>
<div class="faq" style="margin-top:1.6rem">{items}</div></div></section>
'''

def keyfacts(items):
    if not items:
        return ""
    return '<aside class="keyfacts" aria-label="Key facts"><p class="keyfacts__title">At a glance</p><ul>' + "".join(f"<li>{i}</li>" for i in items) + '</ul></aside>'

def sources(items):
    if not items:
        return ""
    lis = "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in items)
    return f'<section class="section" style="padding-top:0"><div class="wrap"><div class="sources"><h2>Sources we used on this page</h2><ul>{lis}</ul><p>Figures are checked against the source at the review date in the byline below. If a source has changed since, the source wins.</p></div></div></section>'

def cta(h2, lede="A short, friendly conversation &mdash; no pressure, no cost."):
    return f'''<section class="section section--lake cta-strip"><div class="wrap">
<p class="eyebrow center">Ready when you are</p><h2>{h2}</h2>
<p class="lede" style="color:#dfe8ee;margin-inline:auto">{lede}</p>
<div class="cta-actions">
<a class="btn btn--gold btn--lg" href="tel:{TEL}">Call {PHONE}</a>
<a class="btn btn--ghost btn--lg" href="#get-help" style="color:#fff;border-color:#fff">Request a free review</a>
<a class="btn btn--ghost btn--lg" href="{S["quote_url"]}" target="_blank" rel="noopener" style="color:#fff;border-color:#fff">Get a quote online</a>
</div></div></section>
'''

def byline():
    return f'''<section class="section" style="padding-top:0"><div class="wrap">
<div class="byline">
<img src="/darin.jpg" alt="Darin Weidauer" width="52" height="52" loading="lazy">
<p>Written and reviewed by <a href="/about"><strong>Darin Weidauer</strong></a> &mdash; licensed insurance agent (NPN {NPN}{LIC_TXT}), Gerontologist (USC Leonard Davis School of Gerontology), MBA, Registered Social Security Analyst, and 22-year U.S. Air Force veteran.<span class="rev">Last reviewed {REVIEWED}. Plan availability, benefits and costs change every plan year &mdash; verify current details at <a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>, 1-800-MEDICARE, or {S["ship_name"]} at {S["ship_phone"]}.</span></p>
</div></div></section>
'''

# ----------------------------------------------------------------------------
# Structured data
# ----------------------------------------------------------------------------
def org_graph(area=None):
    area = area or {"@type": "State", "name": STATE}
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "InsuranceAgency", "@id": f"{SITE_URL}/#org", "name": ORG, "alternateName": S["name"], "url": f"{SITE_URL}/",
         "telephone": TEL, "email": EMAIL, "description": S["org_description"], "areaServed": area, "knowsAbout": S["knows_about"],
         "founder": {"@id": f"{SITE_URL}/#darin"}, "sameAs": SAMEAS_ORG, "image": f"{SITE_URL}/og-image.png",
         "logo": f"{SITE_URL}/favicon.svg", "priceRange": "Free consultation"},
        {"@type": "WebSite", "@id": f"{SITE_URL}/#website", "url": f"{SITE_URL}/", "name": S["name"], "publisher": {"@id": f"{SITE_URL}/#org"}, "inLanguage": "en-US"},
        {"@type": "Person", "@id": f"{SITE_URL}/#darin", "name": "Darin Weidauer", "honorificSuffix": "MBA, RSSA",
         "image": f"{SITE_URL}/darin.jpg", "url": f"{SITE_URL}/about", "jobTitle": "Independent Medicare Insurance Agent & Gerontologist",
         "identifier": ([{"@type": "PropertyValue", "propertyID": "NPN", "value": NPN}, {"@type": "PropertyValue", "propertyID": f"{STATE} insurance license", "value": LIC}] if LIC else {"@type": "PropertyValue", "propertyID": "NPN", "value": NPN}), "worksFor": {"@id": f"{SITE_URL}/#org"},
         "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Pepperdine University"}, {"@type": "CollegeOrUniversity", "name": "University of Southern California"}],
         "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Registered Social Security Analyst (RSSA)"},
                           {"@type": "EducationalOccupationalCredential", "credentialCategory": "Credentialed Gerontologist"},
                           {"@type": "EducationalOccupationalCredential", "credentialCategory": f"Licensed insurance agent, {STATE} (NPN {NPN}{LIC_TXT})"}],
         "knowsAbout": ["Medicare", "Medigap", "Social Security claiming", "Gerontology", "Retirement planning"], "sameAs": SAMEAS_DARIN},
    ]}

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + '</script>'

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": unesc(fill(q)), "acceptedAnswer": {"@type": "Answer", "text": unesc(fill(a))}} for q, a in faqs],
            "datePublished": ISO, "dateModified": ISO, "author": {"@id": f"{SITE_URL}/#darin"}, "reviewedBy": {"@id": f"{SITE_URL}/#darin"}, "inLanguage": "en-US"}

def crumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": unesc(n), "item": SITE_URL + (p or "")} for i, (n, p) in enumerate(items)]}

# ----------------------------------------------------------------------------
# Page shell
# ----------------------------------------------------------------------------
PAGES = []
def page(path, title, desc, body, schemas, ogtype="website", noindex=False):
    canonical = SITE_URL + ("/" if path == "index" else f"/{path}")
    title, desc = fill(title), fill(desc)
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">'
    t, d = html.escape(unesc(title), quote=True), html.escape(unesc(desc), quote=True)
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{d}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="{S["theme_color"]}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="author" content="Darin Weidauer">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{S["name"]}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{S["name"]} — {ORG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE_URL}/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{S["fonts_url"]}" rel="stylesheet">
<link rel="stylesheet" href="/site.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
'''
    out = head + header() + '<main id="main">\n' + body + '</main>\n' + footer() + '</body>\n</html>\n'
    (ROOT / f"{path}.html").write_text(fill(out), encoding="utf-8")
    return canonical

def register(canonical, priority="0.6"):
    PAGES.append((canonical, ISO, priority))

# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------
def place_options_grid():
    cards = "".join(f'<article class="card"><h3>{h}</h3><p>{p}</p><a class="card__link" href="{href}">{label} <span aria-hidden="true">&rarr;</span></a></article>' for h, p, href, label in PLACE_CARDS)
    return f'<div class="grid grid--4" style="margin-top:1.6rem">{cards}</div>'

def build_topic(p):
    slug = p["slug"]
    items = [("Home", "/")] + p.get("crumb_parents", []) + [(p["crumb"], None)]
    body = hero(p["scene"], p["eyebrow"], p["h1"], p["sub"], items, slug, p.get("form_title", "Talk it through with Darin"))
    body += f'<section class="section"><div class="wrap prose">{keyfacts(p.get("keyfacts"))}{p["body"]}</div></section>\n'
    body += faq_html(p["faqs"]) + cta(p["cta"]) + sources(p.get("sources")) + byline()
    schemas = [org_graph(), crumb_ld(items),
               {"@context": "https://schema.org", "@type": p.get("schema_type", "Article"), "headline": unesc(fill(p["h1"])),
                "description": unesc(fill(p["desc"])), "url": f"{SITE_URL}/{slug}", "mainEntityOfPage": f"{SITE_URL}/{slug}",
                "author": {"@id": f"{SITE_URL}/#darin"}, "publisher": {"@id": f"{SITE_URL}/#org"}, "reviewedBy": {"@id": f"{SITE_URL}/#darin"},
                "datePublished": ISO, "dateModified": ISO, "inLanguage": "en-US", "isPartOf": {"@id": f"{SITE_URL}/#website"},
                "about": p.get("about", f"Medicare in {STATE}"), "image": f"{SITE_URL}/og-image.png"},
               faq_ld(p["faqs"])]
    register(page(slug, p["title"], p["desc"], body, schemas, ogtype="article"), p.get("priority", "0.8"))

def place_cards_html(systems, communities):
    sysl = "".join(f"<li>{s}</li>" for s in systems)
    return f'''<div class="grid grid--3" style="margin-top:1.8rem">
      <article class="card">
        <svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 21V8l9-5 9 5v13"/><path d="M9 21v-6h6v6"/><path d="M10 11h4"/></svg>
        <h3>Care close to home</h3><p>Major care in the area includes:</p>
        <ul class="creds" style="margin-top:.2rem">{sysl}</ul>
        <p style="font-size:.95rem;margin-top:.6rem">Plan networks differ &mdash; we check that your doctors and hospital are covered before you enroll.</p>
      </article>
      <article class="card">
        <svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21s-7-5.2-7-11a7 7 0 0114 0c0 5.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>
        <h3>Communities we serve</h3><p>{communities}.</p>
      </article>
      <article class="card">
        <svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
        <h3>When you can enroll</h3><p>{S["enroll_note"]}</p>
      </article>
    </div>'''

def build_city(c):
    r = REGION[c["region"]]
    items = [("Home", "/"), (r["short"], f"/{r['slug']}"), (c["name"], None)]
    nearby = "".join(f'<a class="loc" href="/{n}">{(CITY.get(n) or BASE.get(n))["name"]} <span aria-hidden="true">&rarr;</span></a>' for n in c["nearby"])
    body = hero(c["scene"], f"Medicare help · {r['name']}", f"Medicare help in {c['name']}, {STATE}", c["sub"], items, c["slug"], "Request your free Medicare review")
    body += f'''<section class="section"><div class="wrap">
    <p class="eyebrow">Medicare in {c['name']}</p>
    <h2>What to know before you compare plans in {c['county']}</h2>
    {"".join(f"<p>{para}</p>" for para in c["intro"])}
    {place_cards_html(c["systems"], c["communities"])}</div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Your options</p><h2>Which kind of plan fits you in {c['name']}?</h2>{place_options_grid()}</div></section>
'''
    body += faq_html(c["faqs"], f"Questions from {c['name']}")
    body += f'''<section class="section"><div class="wrap"><p class="eyebrow">Nearby</p><h2>Medicare help in neighboring areas</h2>
    <div class="loc-grid" style="margin-top:1.4rem">{nearby}<a class="loc" href="/{r['slug']}">All of {r['name']} <span aria-hidden="true">&rarr;</span></a></div></div></section>
'''
    body += cta(f"Let&rsquo;s find your {c['name']} Medicare plan together.") + byline()
    area = {"@type": "City", "name": c["name"], "containedInPlace": {"@type": "State", "name": STATE}}
    desc = c.get("desc") or f"Free Medicare help in {c['name']} and {c['county']}: compare Medicare Advantage, Medigap and Part D with a licensed independent agent. Call {PHONE}."
    local = {"@context": "https://schema.org", "@type": "InsuranceAgency", "name": f"{ORG} — {c['name']}", "url": f"{SITE_URL}/{c['slug']}",
             "telephone": TEL, "description": unesc(fill(desc)),
             "areaServed": [{"@type": "City", "name": f"{c['name']}, {STATE}"}, {"@type": "AdministrativeArea", "name": f"{c['county']}, {STATE}"}],
             "parentOrganization": {"@id": f"{SITE_URL}/#org"}, "image": f"{SITE_URL}/og-image.png", "priceRange": "Free consultation"}
    title = c.get("title") or f"Medicare Plans in {c['name']}, {S['abbr']} {PLAN_YEAR} | {ORG}"
    register(page(c["slug"], title, desc, body, [org_graph(area), local, crumb_ld(items), faq_ld(c["faqs"])]), "0.6")

def build_base(b):
    r = REGION[b["region"]]
    items = [("Home", "/"), ("Veterans", "/veterans"), (b["name"], None)]
    nearby = "".join(f'<a class="loc" href="/{n}">{(CITY.get(n) or BASE.get(n))["name"]} <span aria-hidden="true">&rarr;</span></a>' for n in b["nearby"])
    body = hero(b["scene"], f"Medicare for military communities · {r['name']}", b["h1"], b["sub"], items, b["slug"], "Request your free Medicare review")
    body += f'''<section class="section"><div class="wrap">
    <p class="eyebrow">Medicare near {b['name']}</p>
    <h2>{b['h2']}</h2>
    {"".join(f"<p>{para}</p>" for para in b["intro"])}
    {place_cards_html(b["systems"], b["communities"])}</div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Your options</p><h2>Which kind of plan fits a military retiree here?</h2>{place_options_grid()}</div></section>
'''
    body += faq_html(b["faqs"], f"Questions from {b['name']} families")
    body += f'''<section class="section"><div class="wrap"><p class="eyebrow">Nearby</p><h2>Medicare help in neighboring areas</h2>
    <div class="loc-grid" style="margin-top:1.4rem">{nearby}<a class="loc" href="/veterans">Veterans &amp; Medicare guide <span aria-hidden="true">&rarr;</span></a></div></div></section>
'''
    body += cta(b["cta"]) + byline()
    area = {"@type": "Place", "name": f"{b['name']}, {STATE}", "containedInPlace": {"@type": "State", "name": STATE}}
    register(page(b["slug"], b["title"], b["desc"], body, [org_graph(area), crumb_ld(items), faq_ld(b["faqs"])]), "0.6")

def build_region(r):
    items = [("Home", "/"), (r["name"], None)]
    sysl = "".join(f"<li>{s}</li>" for s in r["systems"])
    cities = "".join(f'<a class="loc" href="/{s}">{(CITY.get(s) or BASE.get(s))["name"]} <span aria-hidden="true">&rarr;</span></a>' for s in r["cities"])
    body = hero(r["scene"], r["eyebrow"], r["h1"], r["sub"], items, r["slug"], "Request your free Medicare review")
    body += f'''<section class="section"><div class="wrap">
    <p class="eyebrow">Medicare in the region</p><h2>{r['name']}: what shapes the choice here</h2>
    {"".join(f"<p>{para}</p>" for para in r["intro"])}
    {r.get("note", "")}
    <p><strong>Counties:</strong> {r['counties']}.</p>
    <div class="grid grid--3" style="margin-top:1.8rem">
      <article class="card"><h3>Health systems</h3><ul class="creds" style="margin-top:.2rem">{sysl}</ul><p style="font-size:.95rem;margin-top:.6rem">Each contracts differently with each plan; we check your doctors first.</p></article>
      <article class="card"><h3>Cities in this region</h3><div class="loc-grid" style="margin-top:.6rem">{cities or '<p>We serve every town in the region by phone and video.</p>'}</div></article>
      <article class="card"><h3>When you can enroll</h3><p>{S["enroll_note"]}</p></article>
    </div></div></section>
<section class="section section--paper2"><div class="wrap"><p class="eyebrow">Your options</p><h2>Which kind of plan fits you?</h2>{place_options_grid()}</div></section>
'''
    body += faq_html(r["faqs"], f"Questions from {r['short']}") + cta(r.get("cta", f"Let&rsquo;s find the right plan for life in {r['short']}.")) + byline()
    area = {"@type": "AdministrativeArea", "name": f"{unesc(r['name'])}, {STATE}", "containedInPlace": {"@type": "State", "name": STATE}}
    title = r.get("title") or f"Medicare Help in {unesc(r['name']).split(' &')[0]}, {S['abbr']} {PLAN_YEAR} | {ORG}"
    desc = r.get("desc") or f"Free Medicare guidance across {unesc(r['name']).split(' &')[0]}: Medicare Advantage, Medigap and Part D compared by a licensed independent agent."
    register(page(r["slug"], title, desc, body, [org_graph(area), crumb_ld(items), faq_ld(r["faqs"])]), "0.6")

def build_home():
    H = HOME
    locs = "".join(f'<a class="loc" href="/{c["slug"]}">{c["name"]} <span aria-hidden="true">&rarr;</span></a>' for c in CITIES)
    regs = "".join(f'<a class="loc" href="/{r["slug"]}">{r["name"]} <span aria-hidden="true">&rarr;</span></a>' for r in REGIONS)
    bases = ""
    if BASES:
        bl = "".join(f'<a class="loc" href="/{b["slug"]}">{b["name"]} <span aria-hidden="true">&rarr;</span></a>' for b in BASES)
        bases = f'<p class="lede" style="margin-top:2.4rem">{H["bases_lede"]}</p><div class="loc-grid">{bl}</div>'
    diff = "".join(f'<article class="card help-card"><h3>{h}</h3><p>{p}</p><a class="card__link" href="{href}">{label} <span aria-hidden="true">&rarr;</span></a></article>' for h, p, href, label in H["different_cards"])
    sit = "".join(f'<article class="card help-card"><h3>{h}</h3><p>{p}</p><a class="card__link" href="{href}">{label} <span aria-hidden="true">&rarr;</span></a></article>' for h, p, href, label in H["situations"])
    trust = "".join(f'<span class="trust__item">{icon} {label}</span>' for icon, label in H["trust"])
    body = f'''<section class="hero">
  <div class="hero__scene" aria-hidden="true">{SCENES[H["scene"]]}</div>
  <div class="wrap hero__inner">
    <div>
      <p class="eyebrow">{H["eyebrow"]}</p>
      <h1>{H["h1"]}</h1>
      <p class="hero__sub">{H["sub"]}</p>
      <div class="hero__actions">
        <a class="btn btn--primary btn--lg" href="tel:{TEL}">Call {PHONE}</a>
        <a class="btn btn--ghost btn--lg" href="#get-help">Request a free review</a>
      </div>
      <p class="hero__nocost"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> No cost, no obligation, no pressure.</p>
    </div>
    {lead_form("home")}
  </div>
</section>
<div class="trust"><div class="wrap trust__inner">{trust}</div></div>
<section class="section"><div class="wrap">
    <p class="eyebrow">{H["different_eyebrow"]}</p>
    <h2>{H["different_h2"]}</h2>
    <p class="lede">{H["different_lede"]}</p>
    <div class="grid grid--3" style="margin-top:2rem">{diff}</div>
</div></section>
<section class="section section--paper2"><div class="wrap center">
    <p class="eyebrow">Medicare in {PLAN_YEAR}, at a glance</p>
    <h2>The numbers that matter this year</h2>
    <p class="lede">Premiums and deductibles change every year. Here are the current {PLAN_YEAR} Original Medicare figures &mdash; we refresh them annually so you are never reading last year&rsquo;s numbers.</p>
  </div>
  <div class="wrap">
    <div class="stats">
      <div class="stat"><div class="stat__num">{FIG['partb']}</div><div class="stat__label">Part B premium</div><div class="stat__sub">Standard monthly, {PLAN_YEAR}</div></div>
      <div class="stat"><div class="stat__num">{FIG['partb_ded']}</div><div class="stat__label">Part B deductible</div><div class="stat__sub">Annual, {PLAN_YEAR}</div></div>
      <div class="stat"><div class="stat__num">{FIG['parta_ded']}</div><div class="stat__label">Part A deductible</div><div class="stat__sub">Per hospital benefit period, {PLAN_YEAR}</div></div>
      <div class="stat"><div class="stat__num">{FIG['partd_cap']}</div><div class="stat__label">Part D drug cap</div><div class="stat__sub">Yearly out-of-pocket max, {PLAN_YEAR}</div></div>
    </div>
    <p class="source-note">Source: Centers for Medicare &amp; Medicaid Services, {PLAN_YEAR} Medicare Parts A &amp; B Premiums and Deductibles (released November 14, 2025) and {PLAN_YEAR} Part D parameters. Higher earners may pay an income-related surcharge (IRMAA) &mdash; see our <a href="/medicare-costs">{PLAN_YEAR} costs &amp; IRMAA page</a>.</p>
</div></section>
<section class="section"><div class="wrap">
    <p class="eyebrow">Where to start</p>
    <h2>{H["options_h2"]}</h2>
    <p class="lede">{H["options_lede"]}</p>
    {place_options_grid()}
</div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Your situation matters</p>
    <h2>Help for specific circumstances</h2>
    <p class="lede">{H["situations_lede"]}</p>
    <div class="grid grid--4" style="margin-top:2rem">{sit}</div>
</div></section>
<section class="section"><div class="wrap">
    <div class="callout"><div>
        <p class="eyebrow">Free guide</p>
        <h2 style="margin-bottom:.3em">New to Medicare? Start with Turning 65 in {STATE}.</h2>
        <p>{H["guide_p"]}</p>
        <a class="btn btn--primary" href="/turning-65">Read the Turning 65 guide</a> <a class="btn btn--ghost" href="/retirement-guide">Get the free 295-page book</a>
      </div>
      <svg width="150" height="150" viewBox="0 0 24 24" fill="none" stroke="{S["theme_color"]}" stroke-width="1.4" aria-hidden="true"><path d="M4 5a2 2 0 012-2h6v18H6a2 2 0 00-2 2z"/><path d="M20 5a2 2 0 00-2-2h-6v18h6a2 2 0 012 2z"/><path d="M8 7h2M8 10h2M14 7h2M14 10h2"/></svg>
    </div>
</div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Who you&rsquo;ll be working with</p>
    <div class="author">
      <img class="author__photo" src="/darin.jpg" width="600" height="600" alt="Darin Weidauer, independent Medicare insurance agent and credentialed gerontologist" loading="lazy" decoding="async">
      <div>
        <h2 style="margin-bottom:.15em">Darin Weidauer, MBA, RSSA&reg;</h2>
        <p style="font-weight:700;color:var(--lake-dark);margin-bottom:.6em">Gerontologist · Registered Social Security Analyst&reg; · U.S. Air Force Veteran</p>
        <ul class="creds"><li>NPN {NPN} · licensed in {STATE}{LIC_TXT}</li><li>Credentialed gerontologist (2014)</li><li>RSSA&reg;</li><li>22-yr USAF veteran (retired officer)</li><li>Author, <em>Retire With Confidence</em></li></ul>
        {H["author_html"]}
      </div>
    </div>
</div></section>
<section class="section" id="areas"><div class="wrap">
    <p class="eyebrow">Serving communities across {STATE}</p>
    <h2>Local Medicare help, statewide</h2>
    <p class="lede">{H["areas_lede"]}</p>
    <div class="loc-grid">{locs}</div>
    <p class="lede" style="margin-top:2.4rem">Or explore Medicare by region &mdash; the parts of the state we all know by name:</p>
    <div class="loc-grid">{regs}</div>
    {bases}
</div></section>
'''
    body += faq_html(H["faqs"], f"Questions {S['demonym']} ask") + cta(H["cta_h2"], H["cta_lede"]) + byline()
    register(page("index", H["title"], H["desc"], body, [org_graph(), faq_ld(H["faqs"])]), "1.0")

def build_about():
    items = [("Home", "/"), ("About Darin", None)]
    body = hero(HOME["scene"], "About · Who is behind this site", "Darin Weidauer, MBA, RSSA&reg;",
                f"Independent Medicare agent licensed in {STATE}, credentialed gerontologist, Registered Social Security Analyst, and 22-year U.S. Air Force veteran. Here is who you are talking to, what he is paid, and what he is not.", items, "about")
    body += f'<section class="section"><div class="wrap prose">{ABOUT_BODY}</div></section>\n' + cta("Have a Medicare question? Ask the person who wrote the page.") + byline()
    profile = {"@context": "https://schema.org", "@type": "ProfilePage", "@id": f"{SITE_URL}/about#profilepage", "url": f"{SITE_URL}/about",
               "name": f"About Darin Weidauer — {S['name']}", "mainEntity": {"@id": f"{SITE_URL}/#darin"}, "isPartOf": {"@id": f"{SITE_URL}/#website"}, "dateModified": ISO, "inLanguage": "en-US"}
    register(page("about", f"About Darin Weidauer | {ORG}",
                  f"Darin Weidauer: independent Medicare agent licensed in {STATE} (NPN {NPN}), gerontologist, Registered Social Security Analyst and retired Air Force officer. How he is paid.",
                  body, [org_graph(), profile, crumb_ld(items)], ogtype="profile"), "0.7")

def build_faq_page():
    items = [("Home", "/"), ("FAQ", None)]
    F = S["faq_page"]
    body = hero(F["scene"], f"Questions {S['demonym']} ask", F["h1"], F["sub"], items, "faq")
    body += faq_html(FAQ_PAGE, "Straight answers") + cta("Didn&rsquo;t see your question? Call and ask it.") + byline()
    register(page("faq", F["title"], F["desc"], body, [org_graph(), crumb_ld(items), faq_ld(FAQ_PAGE)]), "0.7")

def build_legal(slug, name, body_html, desc):
    items = [("Home", "/"), (name, None)]
    body = f'''<section class="hero hero--short"><div class="hero__scene" aria-hidden="true">{SCENES[HOME["scene"]]}</div>{crumbs(items)}
<div class="wrap" style="padding:1rem 0 2.4rem"><p class="eyebrow">{name}</p><h1>{name}</h1></div></section>
<section class="section"><div class="wrap prose">{body_html}</div></section>
'''
    register(page(slug, f"{name} | {ORG}", desc, body, [org_graph(), crumb_ld(items)]), "0.3")

def build_thankyou():
    items = [("Home", "/"), ("Thank you", None)]
    body = f'''<section class="hero hero--short"><div class="hero__scene" aria-hidden="true">{SCENES[HOME["scene"]]}</div>{crumbs(items)}
<div class="wrap" style="padding:1rem 0 2.4rem"><p class="eyebrow">Request received</p><h1>Thank you &mdash; your request is on its way.</h1></div></section>
<section class="section"><div class="wrap prose">
<p>Thanks for reaching out. Your request has been received, and Darin or a licensed agent on our team will get back to you shortly to set up your free, no-pressure Medicare review.</p>
<h2>What happens next</h2>
<ul><li>We&rsquo;ll reach out using the contact details you provided.</li><li>We&rsquo;ll listen first &mdash; your doctors, your prescriptions, your county, your budget.</li><li>Then we&rsquo;ll compare the options that actually fit, with no obligation.</li></ul>
<p>Need to talk sooner? Call us anytime at <a href="tel:{TEL}"><strong>{PHONE}</strong></a>.</p>
<p><a class="btn btn--ghost" href="/">&larr; Back to home</a></p>
</div></section>
'''
    page("thank-you", f"Thank you | {ORG}", "Your request has been received. Darin or a licensed agent will be in touch shortly.", body, [org_graph()], noindex=True)

def build_404():
    lis = "".join(f"<li>{li}</li>" for li in S["notfound_links"])
    body = f'''<section class="section"><div class="wrap prose">
<h1>We couldn&rsquo;t find that page</h1>
<p>The link may be out of date, or the address may have a typo. Here is where most people were heading.</p>
<h2>Popular guides</h2><ul>{lis}</ul>
<div class="note-box"><p>Still stuck? Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a> and we will point you to the right place &mdash; or just answer the question directly.</p></div>
</div></section>
'''
    page("404", f"Page not found | {ORG}", f"That page could not be found. Here are the {STATE} Medicare guides most people were looking for.", body, [org_graph()], noindex=True)

# ----------------------------------------------------------------------------
# Discovery files
# ----------------------------------------------------------------------------
def write_discovery():
    urls = "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{m}</lastmod>\n    <priority>{p}</priority>\n  </url>\n" for u, m, p in PAGES)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai", "Google-Extended",
            "PerplexityBot", "Perplexity-User", "Applebot", "Applebot-Extended", "CCBot", "Amazonbot", "meta-externalagent", "cohere-ai", "DuckAssistBot", "YouBot", "Bingbot"]
    (ROOT / "robots.txt").write_text(
        f"# Structured summaries for language models: /llms.txt and /llms-full.txt\n# {S['name']}\n# Standard search engines and AI / answer-engine crawlers are welcome.\n"
        "User-agent: *\nAllow: /\nDisallow: /thank-you\nDisallow: /source/\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n\n# --- AI and answer-engine crawlers: explicitly welcome ---\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots))
    topic_lines = "".join(f"- [{unesc(fill(p['nav_title']))}]({SITE_URL}/{p['slug']}): {unesc(fill(p['llm']))}\n" for p in TOPIC_PAGES)
    city_lines = "".join(f"- [Medicare help in {c['name']} ({c['county']})]({SITE_URL}/{c['slug']})\n" for c in CITIES)
    base_lines = "".join(f"- [{unesc(b['h1'])}]({SITE_URL}/{b['slug']})\n" for b in BASES)
    region_lines = "".join(f"- [Medicare help across {unesc(r['name'])}]({SITE_URL}/{r['slug']}): counties {r['counties']}\n" for r in REGIONS)
    net_lines = "".join(f"- [{n}]({u})\n" for n, u in NETWORK)
    facts = "".join(f"- {f}\n" for f in S["llm_facts"])
    (ROOT / "llms.txt").write_text(fill(f"""# {ORG} — {STATE}

> {S["llm_summary"]}

Contact: {PHONE} · {EMAIL} · {SITE_URL}/

## About
{ORG} is an independent Medicare insurance agency serving the State of {STATE}. Agent: Darin Weidauer, MBA, RSSA — gerontologist, Registered Social Security Analyst, 22-year U.S. Air Force veteran, licensed in {STATE}, NPN {NPN}{LIC_TXT}. Help is free to the consumer; independent agents are paid by carriers at enrollment, and the premium is the same whichever way you buy. Author page: https://www.myecos360.com/darin-weidauer

## What to know about Medicare in {STATE}
{facts}
## Verified {PLAN_YEAR} figures (CMS)
- Medicare Part B standard premium: {FIG['partb']}/month; annual deductible: {FIG['partb_ded']}
- Part A hospital deductible: {FIG['parta_ded']} per benefit period
- Part D out-of-pocket cap: {FIG['partd_cap']}/year; maximum deductible: {FIG['partd_ded']}; national base premium: {FIG['partd_base']}
- IRMAA (income surcharge) begins above {FIG['irmaa_single']} (single) / {FIG['irmaa_joint']} (joint), based on 2024 MAGI

## Pages
- [Home]({SITE_URL}/): free, plain-English Medicare help across {STATE}
{topic_lines}- [About Darin Weidauer]({SITE_URL}/about): credentials, licensing, compensation disclosure
- [FAQ]({SITE_URL}/faq): the questions {S['demonym']} ask most
{city_lines}{base_lines}{region_lines}- [Privacy Policy]({SITE_URL}/privacy)
- [Terms of Use]({SITE_URL}/terms)

## Same agency, other sites
{net_lines}
## Compliance
{unesc(S["tpmo"])} Not affiliated with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.
"""))
    full = [fill(f"# {ORG} — {STATE} (full reference)\n\nWebsite: {SITE_URL}/\nPhone: {PHONE}\nEmail: {EMAIL}\nService area: State of {STATE} (statewide — by phone and video)\nLast reviewed: {ISO}\n\n## About\n{ORG} is an independent Medicare insurance agency helping {STATE} retirees and people approaching 65 compare their Medicare options clearly, patiently, and at no cost. Independent agents are paid by the insurance carriers when a client enrolls, so there is no charge to the consumer, and plan premiums are the same whether you enroll with our help or on your own.\n\n## Agent / author\nDarin Weidauer, MBA, RSSA — independent Medicare insurance agent licensed in {STATE} (NPN {NPN}) and 16 other states (AZ, CA, CO, FL, GA, MN, NC, NM, NV, OH, SC, TN, TX, UT, WA), credentialed gerontologist (since 2014), Registered Social Security Analyst, and 22-year U.S. Air Force veteran (retired officer). Author of \"Retire With Confidence: Medicare, Social Security, and the Money Decisions That Decide Your Retirement\" (2026 Edition, 295 pages). Former Professor of Aerospace Studies at Loyola Marymount University; has lectured at more than 50 colleges and universities. Canonical author profile: https://www.myecos360.com/darin-weidauer\n\n## What to know about Medicare in {STATE}\n{facts}")]
    for p in TOPIC_PAGES:
        full.append(fill(f"\n## {unesc(p['h1'])}\nURL: {SITE_URL}/{p['slug']}\n"))
        for k in p.get("keyfacts", []):
            full.append(fill(f"- {unesc(k)}\n"))
        for q, a in p["faqs"]:
            full.append(fill(f"- Q: {unesc(q)} A: {unesc(a)}\n"))
    full.append("\n## Areas served\nCities: " + ", ".join(c["name"] for c in CITIES) + ".\nRegions: " + ", ".join(unesc(r["name"]) for r in REGIONS) + ".\n"
                + ("Military communities: " + ", ".join(b["name"] for b in BASES) + ".\n" if BASES else ""))
    full.append(fill(f"\n## Compliance\n{unesc(S['tpmo'])} {ORG} is not connected with or endorsed by the U.S. government or the federal Medicare program, and is not affiliated with {unesc(S['not_affiliated'])}, the VA, the Department of Defense, or TRICARE. This is a solicitation for insurance; a licensed agent may contact you.\n"))
    (ROOT / "llms-full.txt").write_text("".join(full))

def write_static():
    src = Path(__file__).resolve().parent
    (ROOT / "favicon.svg").write_text(S["favicon_svg"] + "\n")
    (ROOT / "vercel.json").write_text(json.dumps({"cleanUrls": True, "trailingSlash": False,
        "headers": [{"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}, {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]}]}, indent=2) + "\n")
    (ROOT / "CNAME").write_text(S["domain"] + "\n")
    (ROOT / ".nojekyll").write_text("")
    (ROOT / "site.js").write_text((src / "site.js").read_text())
    (ROOT / "analytics.js").write_text((src / "analytics.js").read_text())
    (ROOT / "site.css").write_text((src / "site.css").read_text())

def main():
    write_static()
    build_home()
    for p in TOPIC_PAGES:
        build_topic(p)
    build_about()
    build_faq_page()
    for c in CITIES:
        build_city(c)
    for b in BASES:
        build_base(b)
    for r in REGIONS:
        build_region(r)
    build_legal("privacy", "Privacy Policy", PRIVACY_BODY, f"How {S['domain']} collects, uses and protects the information you share with {ORG}.")
    build_legal("terms", "Terms of Use", TERMS_BODY, f"Terms of use for {S['domain']}, operated by {ORG}.")
    build_thankyou()
    build_404()
    write_discovery()
    print(f"built {len(PAGES)} indexable pages + thank-you + 404")

if __name__ == "__main__":
    main()
