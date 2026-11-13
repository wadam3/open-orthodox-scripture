# Genesis — book rationale, source selection, chapter workflow

**Status (2026-11-12):** Genesis **chapters 1 and 2** now contain **56 provisional English verses and 56 corresponding Greek working readings** (31 + 25). Both text-only narration scripts exactly match their English verse files. Original 1887 photographic pages **1–4** and two AI-assisted meaning audits are documented. The repeatable structural, narration and SHA-256 checks **pass in GitHub Actions**. Precise first-edition bracket and Greek character verification, a separately independent Greek-English review, narrated audio listening and subsequent qualified human review are **not yet complete**. Neither chapter is publication-ready or Church-approved; see the [Genesis 1–2 pre-human QA report](../../../docs/GENESIS_1_2_PRE_HUMAN_QA.md).

## Why this Greek source

**Selected provisional source:** Henry Barclay Swete, *The Old Testament in Greek According to the Septuagint*, **Volume I, first edition, Cambridge University Press, 1887**. This historical, manuscript-oriented Septuagint edition is in the U.S. public domain by publication date and offers a traceable Greek source that can be independently checked. The precise original printing matters: no newer critical or digital editions may be silently substituted.

**Where found (exact URLs):**
- Internet Archive / Wellesley College Library historical scan: **https://archive.org/details/oldtestamentingr01swet**.
- Princeton Theological Commons catalog/rights record: **https://commons.ptsem.edu/id/oldtestamentingr01swet**.
- Cambridge University Press edition-history reference: **https://www.cambridge.org/core/books/old-testament-in-greek-according-to-the-septuagint/58D0D0A49BA2F1D53DB004EA01A1C052**.
- General source URL directory: [sources/SOURCE_URLS.md](../../../sources/SOURCE_URLS.md).

**Manuscript basis and reader explanation:** The surviving Codex Vaticanus is missing its opening Genesis text, so Swete's Genesis 1 comes from supplementary manuscript material, notably Codex Alexandrinus. This is **not** a missing chapter in Swete. A reader-facing source note with ID `GEN-001-SRC-001` is linked in [chapter 1 JSON](001.json) and [chapter 1 research](../../../notes/ot/GEN/001.md). The exact printed Greek, brackets, witness sigla, page-to-verse mapping and later variant decisions still require independent page-level auditing.

**Other editions considered:** Rahlfs–Hanhart, Göttingen and modern Church of Greece editions have no separately verified public-domain text-reuse pathway under our rules; compare them only as permitted historical/contextual research, never import their modern text. See [Greek source comparison](../../../docs/SEPTUAGINT_SOURCE_COMPARISON.md). Brenton is a **nineteenth-century English comparison consulted only after our independent Greek drafting and audit**; do not use it as the Greek text or copy its wording: [Brenton policy](../../../docs/HISTORICAL_ENGLISH_TRANSLATION_REFERENCES.md).

## Chapters and audio design

Translate **Genesis 1, then Genesis 2, and so on through Genesis 50**, finishing every chapter's Greek-based draft, independent internal audit, decision notes, and mandatory reader notes before the provisional book-complete gate. Only after completing the whole Genesis book do we proceed to Exodus. The first chapter is a style-and-narration pilot; do not silently finalize wording before comparing aloud.

- **Main chapter texts:** [Genesis 1, 31 verses](001.json) and [Genesis 2, 25 verses](002.json) — **56 provisional English verses**, neither source-certified or publication-approved.
- **Working Greek and notes for Genesis 2:** [25-verse research reading](../../../notes/ot/GEN/002.greek-working.md), [source-image audit](../../../notes/ot/GEN/002.source-audit.md), [tentative original brackets](../../../notes/ot/GEN/002.bracket-map.md), and [live verse verification log](../../../notes/ot/GEN/002.verification-log.md).
- **Mechanical QA and checksum evidence:** [pre-human QA report](../../../docs/GENESIS_1_2_PRE_HUMAN_QA.md), [hash manifest](../../../docs/GENESIS_1_2_CONTENT_HASHES.json), [successful GitHub Actions run](https://github.com/wadam3/open-orthodox-scripture/actions/runs/43359844374).
- **Chapter-level audit and source URLs:** [`notes/ot/GEN/001.md`](../../../notes/ot/GEN/001.md) — translation decisions and the **confirmed original 1887 bracket notices**, Genesis 1:8 Greek-only reading, and unresolved questions. [All 31 first-pass source checks](../../../notes/ot/GEN/001.source-audit.md).
- **Original Greek intake:** [`sources/ot/greek/GEN/`](../../../sources/ot/greek/GEN/README.md) — transcription pending, do not import OCR or third-party digital text.
- **Central project rules:** [Translation Protocol v0.8](../../../docs/TRANSLATION_PROTOCOL.md) and [audio plan](../../../docs/AUDIO_PLAN.md).

For a smooth audiobook, generate only the clean chosen English text with natural pauses and chapter transitions. Keep all verse numbering/addressability in metadata; provide source and important variant explanations in the ebook/print notes and optional accessible audio notes. **Do not replace the verse text with research notes or insert URL narration in the continuous audiobook.**

**Approval:** Provisional AI-assisted text only. Qualified Greek-language, Orthodox, English and rights/editorial review occurs only after the entire Bible provisional draft, and no Orthodox Church authorization is claimed.

## First-pass translation and audio QA — 2026-11-12

All 31 English verses have been checked for meaning and narrative structure against the actual 1887 printed Greek images; the original 1844 Brenton English was consulted **only afterward**. The detailed source, page, and Greek-audit evidence is in [Genesis 1 source audit](../../../notes/ot/GEN/001.source-audit.md). Two local Greek-driven wordings were refined at 1:20 and 1:31. Source notes `GEN-001-SRC-002` and `GEN-001-SRC-003` now explain 1887 first-edition **editorial supplements where Alexandrinus is damaged**. The optional, unapproved [clean narration script](../../../audio/scripts/GEN/001.narration.txt) is produced directly from current JSON and omits footnotes and verse labels for continuous playback. **Status remains draft** until the original Greek transcription and an independent second audit are complete.

## Working Greek transcription and first-edition correction

The [Genesis 1:1–19 Greek working transcription](../../../notes/ot/GEN/001.greek-working.md) has been entered directly from **the selected Swete 1887 printed images** but remains unverified; it has **not** been imported into the approved Greek-source folder. The source check confirmed that **Genesis 1:14 explicitly includes governing day and night**, a phrase accidentally omitted from our English pilot; that clause is now restored in [the provisional English chapter](001.json), with reader note `GEN-001-TRN-014`. The [narration script](../../../audio/scripts/GEN/001.narration.txt) has been kept in sync. Full Greek transcription (including exact bracketed reconstructions from 1:20–31), an independent second audit, and qualified review remain required.

## Remaining Greek text, still under verification

A [provisional running-Greek reading for verses 1:20–31](../../../notes/ot/GEN/001.greek-working-20-31.md) is now recorded alongside the [first 19 verses](../../../notes/ot/GEN/001.greek-working.md). These **are research drafts, not an approved or fully diplomatic transcription**: the exact 1887 square brackets around editorial supplements in Alexandrinus lacunae are not yet transcribed and independently checked. Genesis 1 is still `draft` and must not advance to `internally checked` until the original 1887 source has been reconstructed faithfully in our own source file and cross-audited against English.
