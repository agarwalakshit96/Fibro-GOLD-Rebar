# Fibro Gold - Market, Demand, Pricing, Customers (Stream 04)

Research date: 2026-10-08. Method: WebSearch only (WebFetch not used, so pages were not read in full; claims rest on search-result extracts).
Tags: **Verified** = seen in a primary/official source extract. **Reported** = secondary source, paid-report teaser or vendor claim. **Unverified** = single weak source or my inference. **Calculated** = my arithmetic from stated assumptions.

Coverage warning: several items (named NHAI projects, dealer margins for GFRP, Africa/Gulf import data, search volumes) could not be found. They are listed as gaps, not filled with guesses.

---

## 1. India market size, growth, drivers

| Figure | Value | Source | Tag |
|---|---|---|---|
| India GFRP rebar market 2025 | USD 56.52M, to USD 110.26M by 2030, CAGR 14.3% | MarketsandMarkets teaser, https://www.marketsandmarkets.com/Market-Reports/geography/gfrp-rebar-market/India | Reported (paid-report teaser). The same page also shows a conflicting "26.32 MN" snapshot, so internally inconsistent |
| India FRP rebar (broader than GFRP) 2025 | USD 40.99M, to USD 77.01M by 2030, CAGR 13.4% | https://www.marketsandmarkets.com/Market-Reports/geography/frp-rebars-market/India | Reported. Note: the "FRP" figure is lower than the "GFRP" figure, so scopes are not consistent. Treat as order of magnitude only |
| India FRP rebar CAGR 2024-2030 | 17.3% | ResearchAndMarkets via BusinessWire, https://www.businesswire.com/news/home/20250227915979/en (27 Feb 2025) | Reported |
| Global GFRP rebar | USD 1.2B (2025) to 3.0B (2034), CAGR 11.8% | https://marketintelo.com/report/gfrp-rebar-market | Reported, low-authority; other global reports give CAGR as low as 3.1%, so wide disagreement |

Takeaway: India is a small base (about USD 40-57M, roughly INR 350-480 crore) growing around 13-17% a year per vendors. Do not quote these in marketing as fact; if used, attribute to "MarketsandMarkets estimate".

Demand drivers:
- Steel corrosion in coastal India. IIT Hyderabad press release says India has a 7,500 km coastline and cites corrosion loss of 5-7% of GDP a year (claim attributed to a cited report). Source: https://pr.iith.ac.in/pressrelease/GFRPR.pdf - Reported.
- BIS standards now exist: IS 18256:2023 (specification) and IS 18255:2023 (test methods), Concrete Reinforcement Sectional Committee CED 54, voluntary certification. Sources: https://services.bis.gov.in/tmp/1734081435.pdf, https://www.bis.gov.in/wp-content/uploads/2024/01/Standard-of-the-week-19122023.pdf - Verified (existence, scope).
- Large corporate entrants legitimising the category: Olectra Greentech (MEIL group) launched GFRP rebar in Hyderabad, April 2025 (UNI, https://test.uniindia.com/~/hyd-olectra-unveils-next-gen-concrete-reinforcement-gfrp-rebar-an-alternative-to-steel-reinforcement/Business%20Economy/news/3448203.html) - Reported. Jindal Advanced Materials "Vantage" FRP rebar (https://www.nbmcw.com/news/jindal-advanced-materials-vantage-frp-rebars-alternative-to-steel-rebars.html) - Reported.
- Metro tunnelling (TBM soft-eyes) and marine/coastal structures are the strongest functional use cases.

Important scope limit in IS 18256 (affects marketing claims): scope is non-prestressed concrete, and the extract states it is for elements where consequence of failure is low as judged by the engineer in charge (examples: pavements, drainage structures, fences, manhole covers). For roads, highways and bridges it defers to Indian Roads Congress guidelines. Source: BIS draft CED 54 (19165), https://services.bis.gov.in/tmp/PRDCED19165_14092023_1_2.docx - Reported from a draft; confirm the final published text on the BIS portal before any compliance claim. Exclusions per extract: hybrid FRP, plain bars without surface enhancement, non-round, couplers.

---

## 2. Pricing

### 2.1 Observed India listings (IndiaMART, via search extracts, retrieved 2026-10-08)
Source: https://m.indiamart.com/impcat/frp-bar.html and supplier pages. All are seller asking prices, likely ex-GST, ex-freight, with unknown MOQ. Tag: Reported.

| Dia | Listing | Price | Note |
|---|---|---|---|
| 12 mm | Om Enterprises, Pune (coil, 900 MPa) | INR 145/kg | |
| 12 mm | Maruti Composites (straight, 1100 MPa) | INR 144/kg | https://m.indiamart.com/maruti-composites |
| 12 mm | Growex Network, Rajkot (6 ft) | INR 135/kg | marketed for solar fence, not construction |
| 16 mm | RN Elements LLP | INR 140/kg | https://m.indiamart.com/rn-elements-llp, "bridges and tunnels" |
| 16 mm | Maruti Composites (1200 MPa) | INR 148/kg | |
| 16 mm | Vraj Enterprise, Rajkot (6 ft) | INR 125/kg | |
| any | Indian directory listing | INR 135 "per piece" | https://www.indianbusinessportal.in/products/12-mm-gfrp-rebar (unit ambiguous) |
| any | Several suppliers | "Price on Request" | |

Also: an Indian road-drainage study used INR 160/kg for GFRP vs INR 55/kg for steel (IJRASET, https://www.ijraset.com/best-journal/comparative-study-of-gfrp-and-conventional-steel-in-road-drainage-design) - Reported (academic, weights in it look inconsistent).

Observed price band: about INR 125-160/kg, centre of mass INR 135-148/kg. No reliable listings were found for 6, 8, 10, 20, 25 or 32 mm, and none from L&T-SuFin or TradeIndia in readable form (TradeIndia page https://www.tradeindia.com/products/gfrp-rebar-c12333751.html appeared but no price extracted). Bulk discounts/typical project discounts: **not found; Unverified / gap**. Tell the pricing team to obtain live quotes by phone ("mystery shopper") for 8-32 mm.

### 2.2 Per-metre conversion (Calculated)
Assumptions: GFRP density 2.0 g/cm3 (bars of about 70-80% fibre by weight are typically 1.9-2.2; confirm with real product), nominal area pi d^2/4. Steel: kg/m = d^2/162. Steel price assumed INR 55-65/kg: infralens city price pages show roughly INR 55-73/kg for steel rebar (Reported, estimates not dealer quotes; https://infralens.in/prices/steel/gurgaon). The author of this file did not verify current Fe500D/550D mill/dealer prices - refresh before use.

| Dia (mm) | GFRP kg/m | GFRP INR/m at 125-148/kg | Steel kg/m | Steel INR/m at 55-65/kg |
|---|---|---|---|---|
| 6 | 0.057 | 7-8 | 0.222 | 12-14 |
| 8 | 0.101 | 13-15 | 0.395 | 22-26 |
| 10 | 0.157 | 20-23 | 0.617 | 34-40 |
| 12 | 0.226 | 28-33 | 0.889 | 49-58 |
| 16 | 0.402 | 50-60 | 1.580 | 87-103 |
| 20 | 0.628 | 79-93 | 2.469 | 136-160 |
| 25 | 0.982 | 123-145 | 3.858 | 212-251 |
| 32 | 1.608 | 201-238 | 6.321 | 348-411 |

Reading: per kg GFRP is about 2-2.7x steel, but because it is about a quarter of the weight, price per metre of the same nominal diameter is similar or lower than steel (roughly 55-60% of steel at the inputs above). Cross-check: one source says GFRP is "about 20-25% of steel's density" (IJRASET study above) - consistent.

### 2.3 Per unit tensile capacity (Calculated, illustrative)
The fair comparison is cost per kN of usable strength, not per metre.
- Steel Fe500D: yield 500 MPa (design 0.87 fy = 435 MPa). 12 mm: about 56 kN at yield; cost INR 49-58/m, so about INR 0.9-1.0 per kN-m.
- GFRP 12 mm: seller-claimed ultimate 900-1100 MPa (Reported listings; IS 18256 minimum values not checked). Ultimate capacity about 100-124 kN; INR 28-33/m gives about INR 0.25-0.3 per kN-m at ULTIMATE.
- But design is governed by lower limits: GFRP has no yield, elastic modulus roughly 1/5 of steel (Korean lap-splice study, https://koreascience.kr/article/CFKO200411722756114.pub?lang=en - Reported), so serviceability (crack width, deflection) and creep-rupture limits (design stress typically a fraction of ultimate in FRP codes - Unverified here) govern. In flexural members, GFRP cost advantage per metre is often consumed by needing more bar area. Marketing should therefore claim "lower cost per metre / lifecycle cost" in corrosion zones and avoid "cheaper than steel" broadly.
- Vendor claim: JAM says up to 35% cost saving versus steel (company interview, Reported). IIT Hyderabad says cost-effective on life-cycle basis (Reported). A review concludes short-term cost is higher than steel (Reported).

---

## 3. Applications and named projects

Verified/Reported named projects (all vendor- or secondary-sourced; none confirmed from owner documents):
- **Delhi Metro Phase 3**: GFRP bars used for numerous TBM "soft-eyes" in diaphragm walls at several stations. Reported by a search extract; original source link not retained, treat as Reported. Supplier names not captured. Needs primary verification (DMRC / contractor papers).
- **Chennai Metro (CMRL)**: Dextra says it supplied 61 FRP Soft Eyes for station entry/exit and TBM shafts. Source: https://dextragroup.com/ground-engineering/tunneling/astec-soft-eyes (Dextra newsletter https://dextragroup.com/dextras-quarterly-newsletter-connection-26) - Reported (supplier claim).
- **Mumbai Coastal Road and Versova-Ghatkopar Metro tunnel linings**: from MarketsandMarkets page only (https://www.marketsandmarkets.com/Market-Reports/geography/gfrp-rebar-market/India) - **Unverified**; do not use in marketing.
- **NHAI "approved GFRP for 12,000 km"**: appears on a market-aggregator page; no NHAI/MoRTH document found - **Unverified; likely unreliable. Do not repeat.**
- Jindal Advanced Materials lists Burj Khalifa, Kanagawa Expressway and marina piers as past uses of its FRP bars (interview, nbmcw link above) - Reported, and likely refers to FRP in general, not necessarily JAM product in India.
- No verified Indian highway/bridge, railway, water/sewage or MRI-room project was found. Supplier pages list "tunnels and metro, marine structures" (e.g., Grandform Fiber, Mumbai) without projects - Reported.

Use cases by category (functional fit, general knowledge plus extracts): coastal/marine (sea walls, jetties, piers), TBM soft-eyes and temporary/permanent diaphragm-wall openings (strongest, verified need), water and sewage plants (chemical exposure), industrial floors and pavements (IS 18256 low-risk scope), precast (drains, manhole covers, fences, boundary walls), MRI rooms/data centres (non-magnetic; Reported by supplier site), railway sleepers/ballast-less track (IITH mentions "rail structures"). Bridges and highway structural use: awaiting IRC guidance - see section 4.

Gap/next step: confirm projects through DMRC/CMRL tender archives, contractor technical papers (e.g., L&T, Afcons, Tata Projects), and ICI / IIT papers.

---

## 4. Buyer psychology and specification route

Pain points and objections (technical ones from Reported academic sources; commercial ones are my inference and marked Unverified):
- **Ductility / brittle failure**: no yield plateau; Korean study noted "potential ductility problem" despite visible cracking. Indian research suggests fibre-reinforced concrete mitigates. Reported.
- **Bending**: cannot be bent on site; bent bars/stirrups must be factory-made and lose strength at the bend (Czech study). Reported. Implication: offer pre-bent stirrups and cut-and-bend service.
- **Lap/development length**: longer than steel (bond-to-tensile ratio lower); example 40 db lap for spiral deformed GFRP reached 440 MPa vs steel over 400 MPa at 20 db; plain bars ineffective. Reported (Korean study).
- **Low modulus (about 1/5 steel)**: deflection and crack-width governed design. Reported.
- **Fire / high temperature**: resin softens; not covered in my sources - Unverified here (general knowledge). Needs a Fibro Gold fire position from the technical stream.
- **Code acceptance**: BIS IS 18256 voluntary; scope restricted to low-risk elements; IRC guidance for bridges/highways not found; no CPWD approval found. Engineer in charge must certify serviceability/strength/durability (BIS draft). Reported. So acceptance is project-by-project at present.
- **Price**: upfront higher per kg and often higher per functional capacity; sold on life-cycle cost.
- **Availability / supplier credibility**: many small traders (Rajkot, Pune), inconsistent specs for same diameter in listings (e.g., 12 mm at 900 vs 1100 MPa) - observed. Test certificates and batch traceability are a differentiator.

How a product gets specified (Unverified in detail; general Indian practice plus the BIS extract):
1. Design consultant/PMC writes a project-specific specification or approves a "technical submittal" referencing IS 18256/18255, ASTM D7957/D8505 or ACI 440.
2. Contractor proposes material; consultant and client approve via material approval request (MAR) with third-party test reports.
3. Public clients (NHAI/PWD/CPWD/metro corps) usually want listing in approved make lists or an explicit specification clause; none confirmed for GFRP. Metro soft-eyes are approved per project by the tunnel/D-wall designer.
4. Private builders/architects: decision by structural consultant plus developer cost engineer.

Typical order sizes and payment terms: **not found in any source**. Unverified general norms (verify in interviews): trial orders by the tonne or a few thousand metres; project orders by container; payment terms advance/PI for small buyers, 30-60 days for large contractors (steel dealers run on credit at both ends - independent dealer guide, Reported).

---

## 5. Distribution

- No India "GFRP dealer wanted" listings found. Existing channels: small traders (e.g., Vardhaman Enterprises, Pune, est. 2023, "wholesaler, trader and distributor of FRP rebar" - https://m.indiamart.com/vardhamanenterprisespune - Reported), manufacturers selling direct on IndiaMART. Dextra (Durabar) works through country distributors (Australia, Pakistan, Qatar, Ecuador, Mexico seen) - https://dextragroup.com/concrete-reinforcement-solutions/glass-fibre-reinforcement/durabar-composite-fibergrlass-gfrp-rebar - Reported. Technofast is exclusive GFRP distributor for Australia; Armastek South Africa is sole distributor for Armastek GFRP in Southern Africa - Reported.
- Analog margins (not GFRP): TMT dealers 5-15% plus quarterly rebates (manufacturer SRMB claim, https://www.srmbsteel.com/why-tmt-steel-is-a-profitable-dealership-business-in-kolkata - Reported, self-interested); distributor investment INR 50 lakh-2 crore, dealer at least INR 20 lakh; exclusivity requirements (SRMB; Captain Steel https://captainsteel.com/pages/tmt-distributor) - Reported. Cement distribution margin about 2-3% (2021 trade interview, https://indiancementreview.com/2021/10/companies-should-leave-at-least-the-small-volumes-to-us/) - Reported. Steel/cement are thin-margin commodity businesses with working-capital strain.
- GST: a tax blog states cement and TMT at 18% from 22 Sep 2025 (https://taxgarden.in/blog/income-tax-gst-for-cement-steel-building-material-dealers-india-ay-2026-27) - Unverified, check CBIC notification. GST on GFRP rebar not confirmed.
- Implication: a specialty, project-led, spec-driven product probably needs a "technical dealer" model with higher margin than commodity (assumption, Unverified); decide after interviews. How competitors recruit dealers: no evidence found.

---

## 6. Export

- **HS code**: Not confirmed. Glass fibre goods fall under HS 7019 (glass fibres and articles thereof); India tariff lines under 7019 include e.g. 70191900 and 70199090 (https://eximpe.com/hsncode-finder/7019, https://ximpex.in/hs-codes/7019, https://www.seair.co.in/fibre-glass-export-data/hs-code-70191900.aspx). One page lists BCD 10% and GST 18% for a 7019 line (Reported, applies to that line). Pultruded glass-fibre/resin rebar may alternatively be classified as articles of plastics (3926.90 / 3925 area) or 7019.90 by supplier practice - **no authoritative source found; get a customs-broker or advance ruling**. Importers' exporter listings and shipping data sites (Volza, Seair) can show what Indian exporters declare.
- **Saudi Arabia**: Aramco asked a local manufacturer (Pultron link) to localise GFRP rebar; projected demand 20M linear metres/year; GFRP approved by Saudi Aramco and the Royal Commission for Jubail and Yanbu; Aramco analysis said 10% of its steel rebar need could be replaced (https://theenergyyear.com/articles/the-transition-to-glass-fibre-reinforced-polymer-in-saudi-construction/) - Reported. Implication: local production and local content rules may crowd out imports; approvals (Aramco, RCJY, SASO/SABER conformity) are gatekeepers. SASO/SABER specifics not verified.
- **UAE, Qatar, Oman, Kuwait**: no GFRP-specific import data found. Dextra has a Qatar distributor (Reported). Indian companies MRG Composites and Shivpriya Fiber Forge claim use in "East Africa, UAE and India" (IndiaMART self-descriptions, https://m.indiamart.com/mrgcomposites-india/profile.html, https://m.indiamart.com/shivpriyafiberforgetechnologies/) - Reported, self-claimed. JAM says exports to Australia and Kenya (Reported).
- **Africa**: South Africa has local producer GFRP Tech (Linbro Park, Gauteng; launched Nov 2024; EnviraBar; https://www.engineeringnews.co.za/article/gfrp-tech-launches-first-of-its-kind-manufacturing-facility-in-south-africa-2024-11-19) and Armastek distribution - Reported. Kenya KEBS standards cover steel reinforcement (KS EAS 412); no FRP standard found; imports need KEBS Import Standardization Mark/PVoC for regulated goods (Reported for steel; FRP applicability Unverified). Nigeria, Ghana, Egypt: nothing found.
- International standard references buyers ask for: ASTM D7957 / D8505, ACI 440.1R / 440.6, CSA S807, CE approval (Roechling example) - Reported.
- Indian exporters: unverified self-claimants above; no shipment data found. Next: pull Volza/Seair/Zauba for HS 70199090 and 70191900 destination breakdowns, UN Comtrade for Saudi/UAE import lines under 7019.

---

## 7. Search demand

No reliable India volumes were obtained (Google Keyword Planner/Semrush needed with India location).
- Only data point: iSpionage lists "gfrp rebar" at about 40 monthly searches and "fiberglass rebar price" at about 10, probably US-based, undated (https://ispionage.com/Competitive_Intelligence_directory/t/535/tuf_bar_com_7475662D6261722E636F6D) - Unverified, do not use.
- Likely high-intent query clusters (inferred from listing/directory patterns and the topics found; **volumes unknown**): "GFRP rebar price" / "price per kg / per meter", "GFRP rebar vs steel", "GFRP rebar IS 18256", "GFRP rebar manufacturer in [Rajkot / Pune / Hyderabad / Mumbai / Ahmedabad]", "GFRP rebar suppliers India", "FRP bar", "basalt rebar", "GFRP rebar lap length / bending / design", "GFRP soft eye TBM", "GFRP rebar for MRI room", "GFRP rebar export / dealer".
- IndiaMART and Indianbusinessportal category pages already rank for product-plus-price queries (observed in results), meaning own-site content must compete with marketplaces. Competitor content existing: Dextra, NBM&CW articles (https://www.nbmcw.com/product-technology/building-materials/gfrp-a-sustainable-alternative-to-steel-in-infrastructure-projects.html).
- Action: run Keyword Planner (India) for the cluster list above; Google Trends India for "GFRP rebar" vs "FRP rebar" vs "fibre rebar".

---

## Key gaps and recommended follow-ups
1. Primary confirmation of Delhi Metro Phase 3 and CMRL soft-eye use; no verified bridge/highway project.
2. Live quotes (6-32 mm) from 5-8 Indian makers; full-spec comparison and MOQ/discount/payment terms.
3. Current Fe500D/550D dealer prices for the steel comparison.
4. IS 18256 numeric minimums (tensile strength, modulus, bond) from the final standard for honest spec sheets; confirm "low-risk" scope text.
5. IRC/MoRTH/CPWD status for GFRP (none found).
6. HS code ruling; Gulf conformity (SABER, ESMA/ECAS, Aramco, RCJY) and Africa approvals (KEBS, SABS, SON, GSA, EOS).
7. Keyword volumes for India.
