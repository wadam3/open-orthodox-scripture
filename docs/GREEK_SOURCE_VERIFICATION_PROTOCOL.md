# Greek source verification protocol — photographic first-edition workflow

**Operational procedure v1.0 — 2026-11-12.** Applies to the provisional Orthodox Septuagint translation. First implementation: **Genesis 1**. This is a reproducible **procedure**, not a claim that all its checks have passed. Its governing project rules remain the [translation protocol](TRANSLATION_PROTOCOL.md).

## Governing source and evidence

- **Chosen primary text for Genesis:** H. B. Swete (editor), *The Old Testament in Greek According to the Septuagint*, Volume I, **1887 first edition**, printed Genesis 1 pp. **1–3**. Original historical catalog: https://archive.org/details/oldtestamentingr01swet ; alternate catalog and rights trail: https://commons.ptsem.edu/id/oldtestamentingr01swet .
- **Exact historical photographic page images logged for Genesis 1:** [printed p. 1](https://ccel.org/ccel/swete/lxx1/lxx1/png/0029=1.png), [printed p. 2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png), [printed p. 3](https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png), from Christian Classics Ethereal Library (CCEL). The 1887 *printed* page number is not the image-leaf number.
- **Page boundaries:** 1:1–13 on p. 1, 1:14 **crosses pp. 1–2**, 1:15–28 on p. 2, 1:29 **crosses pp. 2–3**, 1:30–31 on p. 3. The exact positioning of verse numerals and apparatus must be logged from the photographs rather than assumed from an electronic text.
- **Manuscript provenance:** Surviving Codex Vaticanus lacks Genesis's opening. Swete uses supplementary witnesses, including Alexandrinus (A). His **1887 printed** notes identify bracketed supplements within **1:20–25** and **1:29–2:3** where parts of A are lost. These are not claims that the whole verses are absent or that the other witnesses supplying each word have already been identified.
- **Not governing sources:** Later Swete printings, OCR/search snippets, third-party Greek digital text dumps, modern proprietary critical editions, and Brenton's 1844 *English* translation. Any such item may be documented as a separate comparator but must never silently substitute for 1887 first-edition Greek. Brenton is checked **after** original Greek work.

### Image access fallback, verified on Genesis 1 printed pp. 2–3

The CCEL site can reject direct navigation to `.../png/0030=2.png` when the URL is percent-encoded or a tool cannot resolve the binary image. A **reproducible successful route** is to open [the scanned-page index](https://ccel.org/ccel/swete/lxx1/Page_Index.html), click the printed page number **2** or **3**, then click its **“Scanned image”** link to render the original photographic image. For page 2 that leads to [image 0030=2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png); for page 3, [image 0031=3](https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png). If original-image access remains blocked, document the exact failed access and **do not** replace the evidence with a later “Swete” digital transcription. [Genesis 1 live log](../notes/ot/GEN/001.verification-log.md) now records short visual bracket examples and retains all incomplete gates.

## A. Exact original-page transcription procedure (per verse)

1. **Pin the edition and the photograph.** Record source-register ID `SWETE-1887-V1`, actual full image URL, printed page, verse number, print/editorial witness label, access date, and repository commit. If the page cannot be opened or distinguished from another printing, mark the verse `blocked` rather than filling text from memory or an uncontrolled site.
2. **Inspect the print itself in reading order.** Locate the beginning/end of the verse; note line wraps, any split words, unusual capital letters and spelling. Where a verse crosses pages, inspect **both** pages. A first-pass paraphrase is not a transcription.
3. **Copy a *diplomatic* Greek working line** directly from the historical image, preserving every word, breath mark, accent, iota subscript, punctuation mark, capitalization, printed **square bracket `[` and `]`**, and genuine orthographic variation. Record any questionable mark as an unresolved item in the *research log*, not as a guessed character in an approved Greek source file. Keep the printed line/page mapping in separate metadata so that verse-level line joins do not lose provenance.
4. **Keep critical apparatus separate.** Transcribe any relevant note and source siglum in the apparatus log, linked to its exact verse/Greek span and printed page. Do not incorporate an apparatus annotation into Scripture text. `[` and `]` in Swete remain **part of the evidence** of the edited Greek: don't remove them merely to make text look cleaner.
5. **For damaged Alexandrinus text**, identify the precise start/end characters of each bracketed span even when brackets occur **inside a word**, span a line break, or start/end on different lines. Record `witness=A`, exactly what the *1887* apparatus says, and whether another witness providing the restored text has actually been confirmed. **Do not assert an unexamined manuscript source.** Flag unresolved spans `bracket-not-mapped`; never silently turn supplied wording into fully attested A text.
6. **Perform a separate character-by-character pass** against the original page (not merely the first transcription, memory, another model's output, or a later electronic edition). Compare letter, breathing, accent, case, punctuation, bracket, verse boundary, and page apparatus. Log checker/method/date and actual corrections; if both passes are AI-assisted, say **AI-assisted two-pass**, not independent human verification.
7. **Normalize only in a separate derivative** after the diplomatic source is checked. Document Unicode NFC, optional capitalization/punctuation normalization, and why a search/display copy differs from source print. Never silently “fix” rare Greek spelling to match a later standard edition.
8. **Record unresolved evidence before proceeding.** The chapter can be a provisional English draft with outstanding brackets, but it cannot be called source-verified until all verse-level issues are resolved or explicitly dispositioned under approved internal policy.

## B. Greek-to-English accuracy and narration check

For **every verse**, compare the source-checked Greek against our original English JSON with a fresh pass: full clauses, subjects and referents, negatives, tense/aspect, number, semantic categories, repeated phrases, verse boundaries, omissions, unwarranted additions, and intentional idioms. Log exact Greek and English spans for each discrepancy; classify as `source-error`, `translation-error`, `style-choice`, `variant`, `manuscript-supplement`, or `pending-verification`. Each decision has a stable ID, evidence URL/page, proposed fix, rationale, decision status, and English revision/commit. Verified substantive Greek or textual alternatives require accessible reader-facing notes; ordinary audiobook narration should not read apparatus or verse numbers by default.

For Genesis 1, the working issue IDs include **GEN-001-TRN-005** (“one day”), **GEN-001-ED-008** (second-day Greek goodness), **GEN-001-TRN-014** (governance clause restored from the 1887 printing), **GEN-001-SRC-002** (bracketed A losses in 1:20–25), and **GEN-001-SRC-003** (1:29–2:3). See the [chapter research](../notes/ot/GEN/001.md) and [historical-image first-pass report](../notes/ot/GEN/001.source-audit.md). No unrelated Hebrew comparison is required.

**Audio gate:** Generate the narration script **from the current English JSON**, compare its words mechanically to the verse strings, then listen for cadence, pronunciation, ambiguous referents and smooth day transitions. Record what was **actually listened to**, especially any revisions made after an earlier listening pass. “Good for audio” never overrides Greek fidelity.

## C. Log and source-file convention

- **Method:** this document.
- **Per-verse live verification ledger:** [`notes/ot/GEN/001.verification-log.md`](../notes/ot/GEN/001.verification-log.md); use the same schema for later chapters.
- **Existing first-pass semantic evidence:** [`notes/ot/GEN/001.source-audit.md`](../notes/ot/GEN/001.source-audit.md).
- **Unverified working Greek:** [1:1–19](../notes/ot/GEN/001.greek-working.md) and [1:20–31](../notes/ot/GEN/001.greek-working-20-31.md). **Important: 1:20–31 does not preserve Swete's exact square brackets, so it is not diplomatic source text.**
- **Chapter/reader annotations:** [`translation/ot/GEN/001.json`](../translation/ot/GEN/001.json); never silently overwrite previously committed translation decisions.
- **Rights and edition gate:** [`docs/SOURCE_REGISTER.csv`](SOURCE_REGISTER.csv). Maintain `approved_for_reuse=false` until the recorded rights/source intake is actually approved. “Published in 1887, plausibly U.S. public domain” does not itself attest completion of the project's provenance/sign-off checklist.
- **Future cleared files** (not yet created): a page-aligned Greek diplomatic text in `sources/ot/greek/GEN/`, associated edition/page/witness metadata, apparatus record, and SHA-256 manifest. Record relative file name, byte encoding, normalization if any, SHA-256 of the exact committed bytes, provenance image URLs, and git commit SHA. A file path or checksum must not be fabricated in advance.

### Mandatory verse-ledger fields

Stable ID; chosen printed-page image(s); original working-Greek file; `first-pass English meaning check`; `exact Greek diplomatic letter check`; `bracket/apparatus mapping`; `second Greek-English audit`; open issue ID(s); checker/date/evidence (or explicit `none`); outcome and git revision. **Statuses** are `not-started`, `working`, `blocked`, `checked-first-pass`, `checked-second-pass`, and `reviewed`. `checked-first-pass` does **not** mean certified. Only evidence-backed fields may advance. For future human work, record reviewer identity/qualification and consent only when actually supplied.

## D. Chapter completion / release barriers

An *internal* source-verified milestone requires (i) every verse faithfully transcribed against **1887 original** with edition-specific bracket spans and relevant apparatus, (ii) independently rechecked complete chapter, (iii) reconciled English, (iv) all source/translation discrepancies resolved or explicitly documented under project rules, (v) source provenance, legal intake and actual SHA-256 captured, (vi) machine structural validation, and (vii) a separate logged narration pass. If any gate fails, chapter stays provisional `draft` with the open items surfaced. **Machine checks and AI agreement are not a qualified human review.**

The later formal publication/approval gate is **separate**, to occur only after a provisional full-Bible draft under the project's sequence: qualified Greek-language, Orthodox, editorial and rights reviews; explicit sign-offs; versioned text, notes and audio metadata. No institutional Orthodox endorsement may be inferred from a research commit.

## E. Genesis 1 checkpoint — 2026-11-12

- **Done:** 31 original English draft verses; 1887 first-page semantic audit and Brenton historical-English check logged; working Greek candidates for **1:1–31**; English 1:14 corrected, 1:20 and 1:31 refined; accessible manuscript/translation annotations and pilot narration script.
- **Not done:** a full bracket-preserving **diplomatic** Greek source transcription, exact verse-level map of all 1887 editorial restorations, letter/diacritic independent second pass, independent second Greek-to-English check, source gate/byte checksum, and refreshed post-correction listening pass.
- **Current status:** `draft`. [Live verse status](../notes/ot/GEN/001.verification-log.md). No claim of independently verified Greek, manuscript-wide collation, Church approval, or publication readiness.
