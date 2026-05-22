# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is **not a software product repo.** It is the back-of-house workshop for **Bloom Soft Co.**, a digital wall art and printables shop that sells on Etsy and Redbubble. The repo holds:

- **Brand source** — logo, brand guidelines PDF, color palette
- **Generated product PDFs** (LDS General Conference printables) and the Python scripts that build them
- **Listing copy** — Etsy/Redbubble titles, descriptions, tags as Markdown
- **Launch playbooks** — standalone HTML files (open locally, not deployed)
- **AI prompts** — Imagen 3 prompts for cover art and product imagery

Customers never see this repo. Nothing here is deployed; everything is a draft that Chloe (the principal creative) hand-publishes to storefronts.

## Hard rules

These are non-negotiable and come from `README.md`:

- **Never publish to Etsy, Redbubble, TikTok, Instagram, or any other external destination from this repo.** Produce drafts in-repo only. Chloe (or Caleb on her behalf) does every publish step manually.
- **AI image generation runs outside this repo.** Scripts and Markdown files here produce *prompts*; Imagen 3 runs on Chloe's side so she controls seed, variation, and output. Do not try to invoke image-generation APIs from this repo.
- **Brand voice belongs to Chloe.** Customer-facing copy (listings, social scripts, descriptions) does not ship without her sign-off. When editing copy files, treat changes as suggestions for her review, not finished work.

## Git LFS — read this before anything else

`*.png`, `*.pdf`, and `*.jpg` are tracked by Git LFS (see `.gitattributes`). On a fresh clone without LFS installed, these files appear as ~130-byte pointer stubs, **not real assets**. If you see PNGs or PDFs reporting tiny sizes (≈130 bytes), LFS is not hydrated — run `git lfs install && git lfs pull` before assuming an asset is corrupt or missing.

Do not commit large binaries without confirming the LFS filter is active for that extension.

## Generating product PDFs

The two Python scripts in `scripts/` build the April 2026 General Conference product line. They are self-contained — no shared module, no config file. Brand colors (`BLUSH_PINK`, `SAGE_GREEN`, `WARM_GOLD`, `SKY_BLUE`, `DEEP_NAVY`, `CREAM`, etc.) are hex constants duplicated at the top of each script. If you change a brand color, change it in **both** scripts.

```bash
# Deps (only reportlab + pillow are needed)
pip install reportlab pillow

# Kids — Conference Passport (~30 pages, letter size)
python scripts/generate-kids-passport.py
# → products/conference/kids/conference-passport-kids-april-2026.pdf

# Adult — Conference Revelation System (~32 pages, letter size)
python scripts/generate-revelation-system.py
# → products/conference/adult/conference-revelation-system-april-2026.pdf
```

Each script's `build_pdf()` function writes to `products/conference/{kids,adult}/` relative to the repo root — re-running overwrites the previous build. After regenerating, expect the LFS-tracked PDF at the repo root (`conference-passport-kids-april-2026.pdf`, `conference-revelation-system-april-2026.pdf`) to also be updated if you copy/replace it; check `README.md`'s product table before committing to confirm filename, page count, and price haven't drifted.

**PDFs are generated, not hand-edited.** To change product content, edit the script and re-run — do not edit the PDF directly.

## Repo layout (the parts that matter)

- **Root `*.md`** — long-form research and copy that Chloe references and copy-pastes from. `conference-v2-premium-listings.md` is the current Etsy copy; `conference-products-listings.md` is the v1 superseded version. `product-pipeline-batch.md` is the master pipeline (47 wildflower/cottagecore listings). `competitive-research.md` informs pricing strategy.
- **Root `*.html`** — launch playbooks (`LAUNCH-TONIGHT.html`, `chloes-launch-guide.html`, `chloes-week-1-playbook.html`, `chloes-tiktok-scripts.html`, `bloom-soft-gtm-sprint.html`). These are local-view only — no build step, no deploy.
- **Root `w*_*.png` / `wallpaper*_*.png`** — phone/desktop wallpaper designs. Naming convention: `w<N>_<theme>.png` for phone wallpapers, `wallpaper<N>_<theme>.png` for the luxe series.
- **`scripts/`** — PDF generators (see above).
- **`products/conference/{adult,kids}/`** — generated PDF output.
- **`listings/etsy/`** — listing-image plans and per-platform listing copy.
- **`prompts/imagen3/`** — Imagen 3 prompt library (cover art, mockups). Each prompt is paired with a target filename and notes on text-overlay clearance.
- **`prompts/mockups/`** — mockup scene prompts for Etsy gallery images.
- **`listing-images/`** — finished mockup/listing imagery used in storefront galleries.

## Conventions for editing copy

- Listing copy files use the structure: **TITLE / DESCRIPTION / PRICE / TAGS** (and sometimes REDBUBBLE blocks). Preserve this layout — Chloe copy-pastes section by section into Etsy/Redbubble, so headers and ordering matter.
- Etsy tag lines are comma-separated and capped at 13 tags. Each tag ≤ 20 characters. Don't exceed these limits.
- Imagen 3 prompts always include "no text in image" and reserve a clear center for Canva overlay. Keep that constraint when adding new cover prompts.
- Brand voice cues: soft, dreamy, cottagecore, wildflower, watercolor, ethereal. Tagline pattern: *"Bloom Soft Co. — <something>."*

## Brand palette (single source of truth)

Defined in both `scripts/generate-kids-passport.py` and `scripts/generate-revelation-system.py`:

| Name | Hex |
| --- | --- |
| Blush Pink | `#F5B9C8` |
| Sage Green | `#A5C6B2` |
| Warm Gold | `#C3A564` |
| Sky Blue | `#B9D7F2` |
| Deep Navy | `#323F5A` |
| Cream | `#FDF8F0` |
| Ice Blue | `#D7E8FA` |
| Soft Lavender | `#E8D5E8` |
| Periwinkle | `#A0C0E4` |

The authoritative document is `bloom_soft_co_brand_guidelines.pdf` (LFS) — if it disagrees with these constants, the guidelines win and the scripts need updating.

## What there is not

- No test suite, no linter, no CI, no package.json, no build system. Don't invent one.
- No deployment. HTML files render locally; nothing serves them.
- No database or API. The "data" is Markdown and PDFs.
