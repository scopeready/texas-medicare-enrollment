# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

Static marketing / lead-generation site for ECOS Medicare Solutions (agent: Darin Weidauer, NPN 18580338) serving **Texas**, at https://texasmedicareenrollment.com. One of the ECOS state sites (Arizona, Georgia, Minnesota, Nevada, Colorado, Tennessee, plus the MyMedigapRate research site and Darin's MyECOS360 author page); they cross-link in the footer "Our network" strip and in the Organization `sameAs`.

## The generator is the source of truth

`source/generate.py` is the **shared engine** used by the newer ECOS state sites (Minnesota was the first); it should stay identical across them. Everything Texas-specific lives in the `source/content_*.py` modules, `source/scenes.py` (SVG hero art) and `source/site.css` (palette). **Edit the source and re-run `python3 source/generate.py`; never hand-edit a generated page.**

- Identity, phone, Web3Forms key, plan-year figures, network list, TPMO wording, nav, footer columns, home page: `content_site.py`.
- Regions, cities, military-community pages: `content_places.py` (one dict each; the generator writes the page, the footer links, the sitemap and both llms files).
- Guide pages: `content_topics_a.py` / `content_topics_b.py`; each has `keyfacts` (answer-first summary), `faqs` (mirrored into FAQPage JSON-LD) and `sources`.
- Links are root-absolute clean URLs (`/houston`, not `houston.html`). Vercel `cleanUrls` and GitHub Pages both resolve them.
- CSS tokens keep the names from the first (Minnesota) build (`--lake`, `--spruce`, `--maple`) with Texas values; do not rename them, the engine's inline styles reference `--lake-dark`.

## Compliance — do not weaken

CMS/TPMO rules apply.

- Every page carries the TPMO disclaimer and the "not connected with or endorsed by the United States government or the federal Medicare program" wording, plus the licensing/compensation disclosure, in the footer. Keep them.
- 1-800-MEDICARE, Medicare.gov and **Texas HICAP (800-252-9240)** are named as the official, independent alternatives.
- The lead form carries the permission-to-contact checkbox and its wording; the hidden `consent_text` records exactly what was agreed. Do not remove either. The form asks no health questions.
- **Do not invent or "update" dollar figures.** The 2026 Medicare figures come from the CMS release of Nov 14, 2025 and live in `SITE["fig"]` plus the costs page. Texas-specific claims (under-65 Plan A, no birthday rule, the 2026 rural-county exits, STAR+PLUS) are cited in each page's "Sources" block. Change them only with a source in hand.
- Texas facts other states' pages get wrong: Texas uses the **federal plan letters** (no state-standardized plans), has **no birthday rule**, requires **Plan A for under-65**, and its Medicaid managed care for seniors is **STAR+PLUS**. Do not paste Minnesota/Colorado copy into this site.
- The phone number is the agency's main line as a deliberate placeholder (see README); the carrier list is not enumerated anywhere on purpose.

## Preview / checks

```bash
python3 source/generate.py && python3 -m http.server 8000   # open /index.html, /houston.html
```
After a build: every JSON-LD block must parse, every `/slug` link must have a file, no `[[TOKEN]]` may remain, and `sitemap.xml` must list exactly the indexable pages.
