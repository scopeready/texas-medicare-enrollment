# Texas Medicare Enrollment

Static lead-generation site for **ECOS Medicare Solutions** (Darin Weidauer, NPN 18580338) serving Texas — https://texasmedicareenrollment.com

## What's here

- `*.html` at the repo root — the site (indexable pages + thank-you + 404), served at clean URLs (`/houston`, `/winter-texans`).
- `site.css`, `site.js`, `analytics.js`, `favicon.svg`, `og-image.png`, `darin.jpg` — shared assets.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt` — crawl and AI-discovery files.
- `vercel.json` (clean URLs, security headers), `CNAME` + `.nojekyll` (GitHub Pages fallback).
- `source/` — **the generator.** `generate.py` is the shared ECOS state-site engine; everything Texas-specific is in `content_site.py` (identity, home), `content_places.py` (regions, cities, military communities), `content_topics_a.py` / `content_topics_b.py` (guide pages), `content_legal.py` (FAQ, about, privacy, terms), `scenes.py` (hero art) and `site.css` (palette). `og.py` renders the share image.

## Editing

```bash
python3 source/generate.py     # rebuild every page + sitemap + llms files
python3 source/og.py           # rebuild og-image.png (needs Pillow)
python3 -m http.server 8000    # preview: open /index.html, /houston.html etc.
```

Edit the `source/content_*.py` files, re-run, commit. Do not hand-edit the generated HTML — the next build overwrites it.

## Before launch (Darin's checklist)

1. **Phone number.** `phone`/`tel` in `source/content_site.py` are the agency's main line; swap in a Texas number and rebuild.
2. **GA4.** Set `MEASUREMENT_ID` in `analytics.js` (it stays silent until you do).
3. **Web3Forms.** The form uses the shared agency key, so leads already arrive; create a Texas-specific key if you want them routed separately.
4. **TPMO disclaimer.** The footer uses the count-free CMS wording. Add Texas carrier/product counts to `tpmo` in `content_site.py` if wanted.
5. The 2026 carrier-exit statements are cited to KFF and Healthcare Dive; re-check each October when the next year's landscape is published.
6. Vercel: import the repo, add the domain, set the production branch to `main`.
