# Bee Field Guide

A single-file, offline beekeeping **field manual & quick reference** for The Alleman Apiary,
built from the Cornell Master Beekeeping course materials.

Open it on your phone, add it to your home screen, and it works with **no signal** at the bee yard.

## What's inside
- **Glossary** — 286 searchable terms (A–Z + instant search)
- **Inspection Checklist** — tap-through routine inspection that remembers your checkmarks
- **Varroa Treatments** — compare 6 mite treatments (efficacy, cost, timing, temperature, supers on/off)
- **Disease & Pest ID** — field signs + what to do for 10 problems (AFB, EFB, Nosema, chalkbrood, etc.)
- **Quick Reference** — key numbers and rules of thumb
- **Course Library** — the full course, organized by module (file links can point to Google Drive)
- **Search** — one box searches across everything

## Files
- `index.html` — the whole app (data is baked in, so it runs offline from one file)
- `manifest.json`, `sw.js`, `icon-*.png` — make it installable as a phone app (PWA)

## How to update the content
The content lives in `build_data.py`. Edit it, then rebuild:

```bash
python build_data.py                 # rewrites data.json
python assemble.py                   # injects data.json into index.html
```

(Glossary source: `beekeeping_glossary master.txt` → `parse_glossary.py` → `glossary.json`.)

After changing `index.html`, bump the `CACHE` version in `sw.js` so phones pull the new copy.

## Deploy
Static site — host on GitHub Pages (same pattern as the other LPP apps) under `lawnsplantspests-ui`.
