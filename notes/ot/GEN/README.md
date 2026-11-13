# Genesis — research and translation notes

## Current cross-chapter checkpoint (2026-11-12)

Genesis **1 (31 verses)** and **2 (25 verses)** now have original-English drafts, verse-aligned Greek working readings based on Swete's **1887 first printing**, matching text-only narration scripts, documented source-image research and per-verse audit logs. [Automated pre-human QA has passed](../../../docs/GENESIS_1_2_PRE_HUMAN_QA.md), including text matching and SHA-256 drift checks. **Neither chapter is yet an exact bracket-preserving Greek diplomatic transcription, independently source-verified, human-approved or publication-ready.** The Greek bracket and character uncertainties are listed in the cross-chapter report; no approval flags were changed.

- [Genesis 1 bracket research](001.bracket-map.md) and [verse verification](001.verification-log.md)
- [Genesis 2 Greek working verses](002.greek-working.md), [verse-by-verse AI semantic audit](002.source-audit.md), [bracket research](002.bracket-map.md), and [verse verification](002.verification-log.md)
- [English Chapter 1](../../../translation/ot/GEN/001.json), [English Chapter 2](../../../translation/ot/GEN/002.json), and [GitHub Actions success](https://github.com/wadam3/open-orthodox-scripture/actions/runs/43359844374)

## New 80% source-letter confidence rule (2026-11-12)

The [verse-by-verse letter-confidence register](001-002.letter-confidence.json) covers **all 56 verses**, with a [documented scoring method](../../../docs/GENESIS_LETTER_CONFIDENCE_METHOD.md). **8 verses scored below 80%** and are marked for more rigorous later verification; **48 scored at or above 80%**. Separate earlier [bracket observations](../../../docs/GENESIS_BRACKET_CONFIDENCE_METHOD.md) flagged **34 of 41 bracket candidates below 80%**. All percentages are heuristic editorial triage ratings, and all 1887 first-edition character/diacritic approvals remain **pending**. File-integrity QA and exact narration matching still pass; no official or independent publication approval is claimed.

**Book ID:** GEN  
**Status:** Complete Genesis 1 **31-verse English draft** logged; first-pass original-image Greek meaning check and historical Brenton comparison now documented; full diplomatic transcription, independent second audit, and formal review remain unfinished.

Companion translation: [Genesis](../../../translation/ot/GEN/README.md).

## Translation decision log
- [Genesis 1 research and first English style samples](001.md), including all actual online source URLs, a full-chapter 1:6–31 working decision register, the day-two Greek wording flag, later-printing bracket cautions, and the manuscript source note `GEN-001-SRC-001`.
- Text style remains unselected; no human review. For each future entry, record date, chapter/verse, proposed rendering, alternatives considered, explanation, and unresolved concerns.

## Greek sources and textual variants
See [Genesis 1 source and notes](001.md). Printed page identification and manuscript provenance are documented; original Greek diplomatic transcription and variant audit are **not yet complete**. Document exact edition, page/verse mapping, reading, evidence, and any rights restrictions before use.

## Discrepancy footnotes and explanations
`GEN-001-SRC-001` describes missing Vaticanus leaves and Swete's replacement manuscript basis. It is a **source-context explanation**, not evidence of a substantive disputed verse. For every substantive difference, create an entry with a stable note ID, Genesis chapter/verse, type of variation, independently verifiable public-domain witness, neutral explanation, chosen handling, uncertainty, and link to the footnote placed with the verse. Do not copy protected modern notes or name proprietary products in reader-facing explanations.

## AI-assisted checks and corrections
All 31 verses have an original AI-assisted working English draft but **have received a first-pass Greek image/meaning review but not an independent audit against a complete diplomatic Greek transcription**. See chapter notes for passage-level pending checks. Record checker, version, what was tested, suspected errors, corrections, and outstanding questions. AI checks do not constitute scholarly or Church approval.

## Open questions
Complete first-edition Greek source transcription, bracket verification, and independent English verse-by-verse checks; perform the listening-style comparison. The **English draft** has 31 verses, but the source-verified chapter is **not** finished or approved.

Notes are working materials, separate from the Scripture text and never a claim of official Church authorization.

## First-pass all-verse audit and 1844 Brenton cross-check

[Genesis 1:1–31 source-image / Brenton review register](001.source-audit.md) — every verse accounted for; exact 1887 page images, 1844 historic printed English, manuscript bracket findings, draft changes at 1:20 and 1:31, and the remaining verification gates.

## 1887 original-image Greek transcription: first segment

[Genesis 1:1–19 first-pass Greek working text](001.greek-working.md) — independently prepared manually from Swete 1887 printed pp. 1–2; **not yet certified**. The direct Greek source revealed an omitted “govern day and night” clause in our English 1:14, now corrected and linked to reader note `GEN-001-TRN-014`. Greek 1:20–31, printed brackets and a full second image audit remain open.

## Genesis 1:20–31 working Greek and bracket-verification queue

[Greek running-text draft for verses 20–31](001.greek-working-20-31.md) — source is Swete's **1887 printed pp. 2–3**; editorially supplied portions in **1:20–25 and 1:29–31** are **not yet mapped with exact printed brackets**, so this is **not** a complete diplomatic transcription or an internally checked chapter. Combined with [verses 1–19](001.greek-working.md), first-pass Greek readings now exist for all 31 verses, with explicit verification limits.

## Method and live verification ledger

[Full Greek source-verification procedure](../../../docs/GREEK_SOURCE_VERIFICATION_PROTOCOL.md) — photographic source identity, per-letter/diacritic transcription, bracket and apparatus preservation, independent translation recheck, rights/checksum and audio gates. [Genesis 1 per-verse verification ledger](001.verification-log.md) — **31 distinct entries**, with verified-versus-working status and current blockers. These are procedures and a live log; **the chapter is not independently checked yet**.
