# Fibro Gold – Handover / Restart Summary (2026-10-09)

**Status: ON HOLD** until a new Supabase account is created. No Supabase project, table, function or key was ever created or used by this work; everything below is in git (branch `claude/serene-pasteur-cuppkl`) and restarts from files.

## Decisions made
- Brand: **Fibro Gold**, sub-line **By Fibrotech FRP** (parent domain fibrotechfrp.com).
- Product scope: straight GFRP rebar only. Audiences: infrastructure contractors, builders/architects/consultants, dealers/distributors, export (Gulf, Africa).
- Build everything now; update certification wording later. **No BIS/ISI/NHAI/compliance claims until earned** (plant not yet set up; BIS licence comes after plant). Claims ladder in `brand/brand-foundation.md`.
- Tagline recommendation: "Strength, without corrosion."; look: charcoal #14161A + gold #C8A24A.

## What exists in the repo
| Path | Contents |
|---|---|
| `frp-rebar-competitor-websites.md` | ~60 FRP/GFRP/BFRP companies with websites (India, global, basalt, China) |
| `research/00-brand-decisions.md` | Owner-confirmed decisions + certification claim ladder |
| `research/01..05-*.md` | Standards/regulatory; Indian competitors; global benchmarks; market/pricing; name/visual/digital |
| `brand/brand-foundation.md` | Positioning, pillars, voice, messaging, claims ladder, boilerplate |
| `brand/brand-kit.html` | Open in browser: logo, colour, type, rules, mock applications |
| `brand/logo/` (+`png/`) | 19 SVG + PNG logo files; regenerate with `brand/tools/make_logo.py`, `export_png.js` |

## Research caveats
Tools could only search (no site/BIS/IP India access). Everything is tagged Verified/Reported/Unverified. Standards numeric limits came from vendor blogs: verify against purchased IS 18255/18256 before quoting. Do not use unverified claims (NHAI "12,000 km", Mumbai Coastal Road, MRG/ARC "largest/first").

## Open items (owner)
1. Trademark: attorney to run IP India/WIPO search for FIBRO GOLD; classes suggested 19, 6, 17 (+1, 35, 37, 40, 42).
2. Facts needed: plant location/capacity, bar sizes/grades, lead times, Fibrotech FRP history/clients/projects, contact details, GSTIN.
3. Website route: standalone Fibro Gold site (recommended) vs section of fibrotechfrp.com.
4. Close research gaps with a normal browser: BIS licence list, buy IS 18255/18256, NABL labs, competitor site screenshots.

## Remaining build order
1. Website (product, technical/downloads, dealers, export, enquiry forms, certification block)
2. Brochure/catalogue + datasheet templates
3. Social media kit + content calendar/templates
4. Extra branding kit items (presentation, packaging/labels, vehicle/site signage, email signature)

## Where Supabase would come in (plan only, nothing created)
Website backend: enquiry/quote form submissions, dealer applications, gated downloads (email capture), admin view of leads. Suggested tables: `enquiries`, `dealer_applications`, `download_requests`, `products`/`documents`. Use row-level security: public insert-only for forms, no public read. Alternative: keep Fibro Gold static and send forms to email/CRM (Zoho) if a database is not needed.

## Restart prompt (paste into a new session once the new Supabase account/project exists)
"Continue Fibro Gold. Read HANDOVER.md, brand/brand-foundation.md and research/00-brand-decisions.md. Connect to the new Supabase project <name/ref>. Build the website next as a <standalone / section> site, following the brand kit and claims ladder (no certification claims yet)."
