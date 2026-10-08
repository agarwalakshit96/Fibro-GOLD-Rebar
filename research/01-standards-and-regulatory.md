# Fibro Gold – Stream 01: Standards, Certification and Regulatory Requirements

Research date: 2026-10-08. Method: web search only (WebFetch to bis.gov.in, supabase-hosted BIS PDFs, etc. failed with DNS errors, so no primary PDF text could be read directly).
Tags: **[V]** Verified (primary source seen in search results, at least at abstract/listing level), **[R]** Reported (secondary/vendor), **[U]** Unverified / not found.
IMPORTANT: Every numeric limit below tagged [R] came from vendor blogs and MUST be checked against the purchased BIS documents before any use in marketing or datasheets.

---
## 1. Indian standards

### 1.1 IS 18256:2023 – Solid round GFRP bars for concrete reinforcement – Specification
- [V] BIS "Know Your Standards" listing: new standard, no amendments shown, Concrete Reinforcement Sectional Committee CED 54; certification scheme listed as **voluntary**. https://services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/Indian_standards/isdetails/Mjk4OTc= ; BIS "Standard of the week" https://www.bis.gov.in/wp-content/uploads/2024/01/Standard-of-the-week-19122023.pdf
- [V] Scope: solid round GFRP straight bars (cut lengths or coils), bent bars and stirrups, with external surface enhancement; minimum requirements for fibre, resin, physical, chemical, mechanical properties. Design is not covered.
- [V] The BIS page carries downloadable lists: Active Licences, Expired/Cancelled Licences, and Testing Laboratories for IS 18256 (rows not visible to me).
- [R] Dates: cover shows October 2023 (IS 18256) and December 2023 (IS 18255); confirm on BIS portal.
- [R] Vendor-quoted minima (Jivial table; garbled layout, treat as UNVERIFIED): tensile strength about 700-850 MPa for 6-12 mm and about 550-650 MPa for 16-25 mm; tensile modulus >= 45 GPa; ultimate strain >= 1.1 %; bond strength >= 7.6 MPa; transverse shear >= 130 MPa; alkali-resistance retention >= 80 % of pristine ultimate tensile force. Source: https://jivialcomposite.com/blog/gfrp-rebar-standards-comparison and https://blog.rnelements.in/posts/gfrp-rebar-testing-parameters-is-18256-explained.html . Note ASTM D7957 modulus floor is 44.8 GPa [R]; a 50 GPa figure seen in a vendor tender clause is a project spec choice, not the standard.
- [U] Exact designation table (diameters/areas), fibre mass content, Tg, degree of cure, void, water absorption limits, alkali test temperature/duration, creep rupture, marking clause numbers: not retrieved. Do not quote.

### 1.2 IS 18255:2023 – FRP bars for concrete reinforcement – Methods of test
- [V] New standard, no amendments, CED 54 (same BIS portal family; see https://services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/Indian_standards/isdetails/MzAyODg= ). Defines terms and test procedures.
- [R] Its normative references include ASTM D7205/D7205M-21 (tensile) and methods for bond, alkali resistance, bent-bar strength, ignition loss, water absorption.
- Draft history: [V] BIS drafts DOC CED 54 (19165) and CED22018904 on services.bis.gov.in (e.g. https://services.bis.gov.in/tmp/CED22019165_16102023_1.pdf).
- [U] Any amendment/revision after Dec 2023: none seen. Re-check BIS portal before launch.
- Purchase official copies from BIS (standardsbis.in); do not rely on watermarked third-party hosted copies.

---
## 2. BIS licensing (Standard Mark)

- [V] Scheme-I of BIS (Conformity Assessment) Regulations, 2018: product certification licence (CM/L number) per product, per IS, per factory location; online application on BIS portal. https://www.bis.gov.in/product-certification/product-certification-faq/?lang=en , https://www.bis.gov.in/apply-for-a-license/?lang=en
- [V] Fees (BIS FAQ): application fee Rs 1,000; inspection fee Rs 7,000 per man-day payable before preliminary inspection. Marking fee is product specific (Annexure I of Scheme-I) [R]; annual licence fee Rs 1,000 [R, unverified]. Testing charges borne by applicant. MSME fee concession circular of 2020 (https://services.bis.gov.in/tmp/CMD1_MSMEFeeRelaxationCircular_20200610.pdf) was for 2020-21; check current status [U].
- [V/R] Timeline: BIS FMCS FAQ quotes about 6 months average from complete application (https://www.bis.gov.in/fmcs/fmcs-faqs); a law-firm blog says 35-60 days (optimistic, [R]). Initial licence up to 2 years; renewals up to 5 years [R]. Test reports for grant generally not older than 90 days [R].
- Steps (generic, [V/R]): apply online with factory details, test facility and equipment list, process flow, raw-material sources, QC plan -> BIS preliminary inspection of factory and in-house lab -> samples drawn and tested at BIS-recognised/own lab -> licence grant after marking fee -> surveillance inspections and market sampling.
- Plant/lab requirements: [R] BIS expects an in-house lab with calibrated equipment for tests listed in the IS (tensile UTM with suitable grips/extensometer, ignition loss/fibre content furnace, water-absorption, Tg/DSC or DMA access, alkali-immersion chamber) or tie-up with recognised lab for tests not feasible in-house. The exact IS 18256 Testing & Inspection (Scheme of Testing and Inspection, STI) requirements were [U] not retrieved.
- Licensees: [R] MRG Composites advertises "India's first BIS licence for GFRP rebar", CM/L-7600217414 (https://www.mrg-composites.com/gfrp-rebar-installation-guide/). ARC Insulations claims "India's First BIS 18256 Certified GFRP Rebar Range" (https://www.arcinsulations.com/rebar/) – conflicting "first" claims. Duraneo, Vegnar, Jivial, GFRP India claim IS 18256 conformity with no CM/L number seen. **None verified against the BIS Active Licences list. Action: download the list from the IS 18256 page on services.bis.gov.in manually.**
- Note: the BIS scheme for IS 18256 is voluntary [V]; a tender may nonetheless demand it.

---
## 3. Government adoption

- [R, strong] **IRC:137-2022**, "Guidelines on Use of Fibre-Reinforced Polymer Bars in Road Projects (Part 1: Glass Fibre-Reinforced Polymer Bars)", first edition, published Oct 2022, produced at MoRTH request; listed in the IRC catalogue at Rs 400. Catalogue: https://irc.nic.in/WriteReadData/LINKS/Catalogue%20January%20202512a28b67-ecd2-4263-a2d7-11a5cbfa6c86.pdf ; new publications list: https://www.irc.nic.in/WriteReadData/LINKS/11%20Arirval%20pub388a6a6b-a7ea-4b30-90c3-de2e6628162f.pdf . The catalogue listing is primary-ish [V for existence/title]; design details come from vendor summaries (environmental reduction factor CE, lap/development lengths) [R]. Part 2 existence [U].
- [V] MoRTH circular compendium of 13 Dec 2024 (https://morth.gov.in/sites/default/files/comprehensive_compendium_circular/Implementation-of-MORTH-Issued-Policy-Circulars%20-13122024.pdf): materials not in MoRTH Specifications must conform to IRC/IS or international standards; proprietary products need proven use and manufacturer licensing arrangement. It is a general route, not a GFRP-specific circular.
- [U] No MoRTH/NHAI circular specifically mandating or approving GFRP rebar found. No CPWD, state PWD, metro, railway (RDSO), MES, or Jal Jeevan specification found. Do not claim "approved by NHAI/CPWD" etc.
- [U/R] Project use claims (Mumbai Coastal Road tunnel linings, Versova-Ghatkopar Metro) come from a market-research page only (https://www.marketsandmarkets.com/Market-Reports/geography/frp-rebars-market/India); no owner confirmation. IIT Hyderabad press release mentions supporting BIS standard development: https://pr.iith.ac.in/pressrelease/GFRPR.pdf
- Action: obtain IRC:137 officially; file RTI/emails to MoRTH, NHAI technical, CPWD, RDSO, metro corporations for status.

---
## 4. International standards (reference list)

| Standard | Role | Status/notes | Tag |
|---|---|---|---|
| ASTM D7957/D7957M | Material spec, solid round GFRP bars | -22 now historical; -25 active (store.astm.org, updated Jan 2026). GSO adopted ASTM D7957-25. https://store.astm.org/d7957_d7957m-25.html ; https://dgsm.gso.org.sa/store/standards/GSO:977149?lang=en | V |
| ACI CODE-440.11-22 | US building code for GFRP-RC design, requires bars to ASTM D7957-22 | https://www.concrete.org/publications/internationalconcreteabstractsportal/m/details/id/51737215 | V |
| ACI 440.1R (guide, 2015) | Older design guide, superseded in effect by 440.11 for buildings | not re-checked | U |
| CSA S807-19 / S806 | Canadian bar spec (S807, E-CR glass) / design (S806) | https://scc-ccn.ca/standardsdb/standards/4030027 | V (S807) |
| ISO 10406-1:2025 | Test methods for FRP bars | https://scc-ccn.ca/standardsdb/standards/8190396 | V |
| ICC-ES AC454 | Acceptance criteria for glass/basalt FRP bars (IBC/IRC); Oct 2022 edition cited, revision draft Feb 2025 staff letter. https://icc-es.org/wp-content/uploads/AC454-0225-R1-Staff-Letter-and-Draft.pdf ; example ESR-5548 https://icc-es.org/wp-content/uploads/report-directory/ESR-5548.pdf | V |
| fib Bulletin 40 (FRP reinforcement in RC) | Design guidance, Europe | not searched | U |
| GSO 2699:2022 | GCC standard seen in results; scope not read | https://dgsm.gso.org.sa/store/standards/GSO:809043?lang=en | U (scope) |

ICC-ES ESR reports are earned by the manufacturer's own product via audited plant; Fibro Gold cannot cite another firm's ESR.

**Gulf**
- [R] Saudi Aramco has reportedly mandated GFRP in corrosive-environment engineering standards; local plants (IKK Mateenbar, Dextra ICSC) are Aramco approved. https://Compositesworld.com/news/saudi-aramco-inaugurates-first-gfrp-rebar-production-facility ; https://www.dextragroup.com/saudi-aramco-approves-dextra-icsc-manufacturing-facility-in-saudi-arabia/ . Aramco vendor qualification for an Indian exporter: [U].
- [U] Saudi Building Code (SBC 304) provisions, SASO/SABER certificate requirement, Qatar QCS, Dubai Municipality / Abu Dhabi approvals for GFRP: nothing found. Existing UAE manufacturers (Pultron Dubai) and project examples only.
**Africa:** [U] nothing found; check national bureaus (KEBS, SABS, SONCAP etc.) and PVoC-type import conformity schemes for each target country.

---
## 5. Testing

- [U] No list of NABL labs for GFRP rebar found. Method: search nabl.qci.in by discipline "Mechanical/Chemical – composites/plastics" and require scope sheet to list IS 18255 methods or ASTM D7205 (tensile), D7913 (bond), D7957 annexes, D570 (water absorption), D3171/ASTM D2584 ignition loss, DSC/DMA for Tg and cure. Candidate institutes to approach (not verified): IIT Hyderabad, IIT Madras/Bombay structural labs, SERC-Chennai, NCCBM/CSIR labs, NTH Alipore – [U].
- BIS also publishes an IS 18256 lab list on its standard page [V existence].
- Typical buyer documents [R/experience-based]: batch test report on tensile strength/modulus/strain, fibre content (ignition loss), Tg and degree of cure, water absorption, bond, transverse shear, alkali resistance, bar dimensions/cross-section; resin/glass material certificates; ISO 9001 certificate; BIS licence copy; third-party inspection reports; creep-rupture and durability data for long-life structures.
- Buyer requests for NABL testing exist publicly (contractlaboratory.com listing) [R].

---
## 6. Manufacturing quality essentials

All [R] unless noted; check IS 18256 raw-material clauses [U].
- Glass: ECR (boron-free, alkali/acid-resistant) glass roving; CSA S807 explicitly names E-CR glass [V]. Plain E-glass is weaker in alkaline concrete; avoid claiming ECR unless supplier certificate supports it.
- Resin: vinyl ester (common) or epoxy; polyester only if the standard permits (not confirmed). Resin supplier datasheet and cure/Tg data needed.
- Process: pultrusion with surface enhancement (sand coating, helical wrap, or ribs); post-cure; cut to length; bent bars/stirrups need factory-formed process (strength drop at bends; D7957 sets minimum bend diameter [V at abstract]).
- QC regime: incoming glass/resin certs, per-lot fibre content, dimensional checks, per-batch tensile/modulus, periodic bond/water/alkali/Tg tests, calibrated equipment, traceable batch marking, retained samples, ISO 9001 system.
- Truthful-claims implications: tensile strength figures must be tied to test method (nominal vs guaranteed); GFRP is not suited as compression reinforcement and has low modulus (deflection governs); no yield, brittle failure; fire behaviour limited; long-term strength reduced by environment (design reduction factors).

---
## 7. Pre-claim checklist and claims to avoid

Before using each claim, hold:
1. "BIS certified / ISI-marked IS 18256": valid CM/L licence in Fibro Gold's (or its manufacturing entity's) name, covering the specific sizes; BIS licence list entry; marking on bars/packaging exactly as the licence prescribes. If bars are made by a third-party/job-work plant, the licensee and factory must match the claim.
2. "Tested to IS 18255/18256": batch test reports from a NABL lab with those methods in scope; test date and report number kept.
3. "ASTM D7957 compliant": full D7957 test report for the current edition (D7957-25 vs -22 noted), ideally third-party certified.
4. "ACI CODE-440.11 compliant": strictly this is a design code; the bar is "manufactured to ASTM D7957, suitable for design per ACI CODE-440.11-22". Never say the bar is ACI 440 certified.
5. "ICC-ES / AC454 evaluated": only with an ESR in own name.
6. "CSA S807 compliant": a CSA/third-party certification or test report.
7. "IRC:137-2022 compliant": say "designed for use under IRC:137-2022 guidelines" with lab data supporting required properties; do not claim approval.
8. "Approved by NHAI / MoRTH / CPWD / metro / Aramco / Dubai Municipality": only with a written approval letter naming Fibro Gold.
9. "Alkali/corrosion-proof, 100-year life": only with long-term durability data; use "corrosion-resistant" and cite test retention.
10. Trademark/brand: BIS mark cannot be used before grant; check "Fibro Gold" brand registration and consistency with fibrotechfrp.com entity.

Claims to avoid: "ISI mark/BIS approved" without licence; "India's first BIS GFRP" (disputed between MRG and ARC); "stronger than steel" without per-weight qualifier; "replaces steel one-for-one"; "fireproof"; "NHAI approved"; "meets ACI/ASTM" without reports; quoting vendor-sourced IS limits not checked against the standard; Jizan/Mumbai Coastal/metro project names as own references.

---
## Open gaps
BIS licensee list (manual download), IS 18256 clause-level limits and marking, BIS marking fee for this product, NABL lab shortlist, MoRTH/NHAI/CPWD/RDSO/metro approvals, Gulf (SBC, SABER, QCS, Dubai) and Africa requirements, fib Bulletin 40 and ACI 440.1R status, IRC:137 text from official source.
