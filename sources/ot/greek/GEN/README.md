# Genesis — Greek source intake

**Status:** 1887 first-edition printed Genesis pp. 1–3 examined for a first-pass semantic English audit; **NO Greek diplomatic transcription imported or independently verified yet**.

Historical source URL index: [Swete 1887 volume I and supporting catalogs](../../../SOURCE_URLS.md). No source scan or transcription has been downloaded into this repository.

## Provisional source candidate

Henry Barclay Swete (editor), *The Old Testament in Greek According to the Septuagint*, volume I, first edition, Cambridge, 1887. This is a **historical public-domain printed edition**, not a modern digital dataset or an Orthodox ecclesiastical endorsement.

See the [source decision](../../../../docs/SEPTUAGINT_SOURCE_DECISION.md) and [historical background](../../../../docs/SWETE_SOURCE_BACKGROUND.md) for bibliographic details, the historical scan location, and why the absence of the opening of Genesis in the surviving Codex Vaticanus matters.

## Verified preparation step — catalog and rights metadata (2026-11-12)

- **Historical edition identified:** Henry Barclay Swete (ed.), *The Old Testament in Greek According to the Septuagint*, Vol. I, Cambridge University Press, 1887. Internet Archive lists publication year 1887, volume 1, collection from Wellesley College Library, and status **NOT_IN_COPYRIGHT**: https://archive.org/details/oldtestamentingr01swet
- **Independent catalog confirmation:** Princeton Theological Commons lists volume 1, 1887, Cambridge University Press, with rights metadata **No Known Copyright**: https://commons.ptsem.edu/id/oldtestamentingr01swet
- **United States reuse rationale:** the 1887 published historical text is in the public domain by age. The linked current scans/catalog records are identification evidence, not authorization to copy unrelated modern transcriptions/annotations or representations about other countries' laws.
- **Source register:** `SWETE-1887-V1` recorded as a historical Greek source **candidate**, `approved_for_reuse=false`. This status means no original Greek chapter file should be imported until the actual printed pages and our original transcription have been checked.
- **Not yet done:** identify Genesis 1 physical/scanned pages, directly inspect printed Greek and witness marks, establish verse mapping, produce and independently verify an original Greek transcription, and establish the English rendering style. This step **does not** mean Genesis 1 has been translated.

## Genesis 1 — first-page and draft provenance (2026-11-12)

- **Exact historical source URL:** https://archive.org/details/oldtestamentingr01swet ; first edition Swete 1887 Volume I, **printed Genesis page 1** contains the opening passage. The entire Genesis 1 chapter continues on **printed pages 1–3**. Identify the scan's exact leaf index in a later confirmed audit; **do not invent an image URL**.
- **Independent bibliographic/rights URL:** https://commons.ptsem.edu/id/oldtestamentingr01swet ; Cambridge historical method: https://www.cambridge.org/core/books/old-testament-in-greek-according-to-the-septuagint/58D0D0A49BA2F1D53DB004EA01A1C052.
- **Manuscript caveat:** Codex Vaticanus lacks its opening Genesis leaves; the first portion of Swete is supplemented especially using Codex Alexandrinus. The 1887 page images and the general Alexandrinus witness markings are now checked in a first pass; individual Greek letters, exact bracket spans, secondary witnesses and complete source transcription still require a separate detailed check. Reader note `GEN-001-SRC-001` lives in [translation chapter 1](../../../../translation/ot/GEN/001.json) and [chapter 1 notes](../../../../notes/ot/GEN/001.md).
- **Text status:** no Greek transcription imported, and no rights-validated page-aligned transcription checksum. The [provisional English working draft of all 31 verses of Genesis 1](../../../../translation/ot/GEN/001.json) is **not** a verified or approved chapter; no ancient Greek source text has been imported.

## Original 1887 page images checked — 2026-11-12

**Source provider actually consulted:** Christian Classics Ethereal Library (photographic images of Swete's **1887 first edition**, identified by its title page). The original printed Genesis chapter 1 appears on three pages:

1. Printed **p. 1** (Genesis 1:1–14 begins): https://ccel.org/ccel/swete/lxx1/lxx1/png/0029=1.png
2. Printed **p. 2** (Genesis 1:14 continues through 1:29 begins): https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png
3. Printed **p. 3** (Genesis 1:29 continues through 1:31): https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png

**First-pass findings:** The Greek at 1:8 contains the divine “good” statement. Swete's **original** apparatus says bracketed parts of Genesis **1:20–25** (printed p. 2) and **1:29–2:3** (printed p. 3) are missing from surviving Codex Alexandrinus; his edited Greek supplies the printed bracketed words. See [31-verse audit with exact links and remaining checks](../../../../notes/ot/GEN/001.source-audit.md).

**Limits:** This is the **first-pass photographic Greek-to-English semantic check**. It **does not** establish a complete original Greek transcription, complete word-level bracket map or independent second pass. Do not change `approved_for_reuse=false` merely because public-domain pages have been inspected. Do not import digital Greek sourced from later printings or unverified third parties.

## Whole-chapter research flags

- **GEN-001-ED-008 (Greek reading of the second day):** The provisional English at 1:8 includes “God saw that it was good,” and the **1887 original printed p. 1 visibly confirms this Greek phrase**. This is a Greek original-edition reading, not a Hebrew comparison. Its full diplomatic source transcription remains pending.
- **GEN-001-ED-BRK (later-edition bracket reports):** A modern electronic “Swete” may reflect a **later printing**, not the 1887 first edition. Its bracket locations should not be silently assumed to match 1887. **We now have direct first-edition evidence:** printed p. 2 confirms lost portions in A within 1:20–25, and printed p. 3 confirms lost portions within 1:29–2:3. Exact word-level brackets and supporting alternate witnesses still require checking. Details: [Genesis 1 chapter research](../../../../notes/ot/GEN/001.md).
- **English draft complete ≠ Greek source transcription complete.** The current 31-verse English chapter is provisional; no underlying Greek diplomatic file has passed intake.

## Genesis 1 — work not yet completed

- [x] Confirm first-edition volume identity, year, bibliographic metadata, and U.S. public-domain rationale; log catalog-level verification in the source register.
- [x] Confirm the original **1887 first-edition printed page images 1–3** and chapter boundaries from CCEL and catalog them in [verse-by-verse first-pass audit](../../../../notes/ot/GEN/001.source-audit.md).
- [ ] Record exact Greek verse/page mapping and which ancient manuscript evidence underlies the printed passage; do not overstate unresolved witness details.
- [ ] Create an original transcription of Genesis 1 and verify it against the page images, including accents and breathings.
- [ ] Record reuse verification and provenance in `docs/SOURCE_REGISTER.csv` before source-text import.
- [ ] Record uncertain readings and independently verified substantive variants in `notes/ot/GEN/` and add linked reader-facing footnotes where required.
- [ ] Add chapter-aligned Greek source file(s) with version and checksum after all source-intake checks pass.

The English [Genesis translation workspace](../../../../translation/ot/GEN/README.md) remains separate. Neither a source import nor an AI-assisted draft constitutes Church approval.

## Current first-pass transcription progress (not approved for import)

The directly inspected 1887 printed pages revealed a material **English omission in Genesis 1:14**. Swete's text on [p. 2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png) reads `καὶ ἄρχειν τῆς ἡμέρας καὶ τῆς νυκτὸς` within the verse begun on [p. 1](https://ccel.org/ccel/swete/lxx1/lxx1/png/0029=1.png). The English JSON has been corrected to “to govern the day and the night.” A research-level [manually transcribed Greek draft for **1:1–19**](../../../../notes/ot/GEN/001.greek-working.md) is kept in `notes/`, **not this source directory**, until it passes all word/diacritic/apparatus checks. Genesis 1:20–31, including the exact printed brackets and Alexandrinus lacunae, remains untranscribed. The `approved_for_reuse=false` source-register gate remains unchanged.

## 1:20–31 Greek reading stage, 2026-11-12

The [remaining twelve verses have an explicitly provisional **normalized running Greek draft**](../../../../notes/ot/GEN/001.greek-working-20-31.md), based on Swete's 1887 photographic pages [2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png) and [3](https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png). It is **not** a diplomatic transcription because the exact printed square-bracket spans at 1:20–25 and 1:29–2:3 are still **unrecorded**. The 1:26–28 verses have no special bracket notice in this passage, but also require a second proofread. **No Greek original-source files are imported or source-cleared**, and the `approved_for_reuse=false` register value stays unchanged.

## Reproducible verification procedure and evidence (2026-11-12)

The [written Greek source verification method](../../../../docs/GREEK_SOURCE_VERIFICATION_PROTOCOL.md) specifies original-image/edition pinning, verse-aligned diplomatic transcription, preservation of Swete's 1887 bracket and apparatus typography, separate independent proofing, normalization metadata, rights/source acceptance, and a future actual SHA-256 checksum. The [Genesis 1 all-verse status ledger](../../../../notes/ot/GEN/001.verification-log.md) tracks every verse's evidence and unresolved gates. **No diplomatic Greek source has passed import**; the first-pass running Greek for 1:20–31 lacks the printed bracket spans. Source-register `approved_for_reuse=false` remains unchanged.
