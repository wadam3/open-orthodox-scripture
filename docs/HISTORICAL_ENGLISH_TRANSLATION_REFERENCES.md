# Historical English translation references — Brenton's Septuagint

**Status:** Approved as a **public-domain historical English comparison reference**, effective 2026-11-12; **not a primary Greek source, not a drafting template, not imported into the repository, and not an Orthodox ecclesiastical authority**. Passage-by-passage use remains subject to edition/provenance checks.

## What this reference is, and what it is not

Sir Lancelot Charles Lee Brenton translated the Greek Septuagint into **English** in the nineteenth century. His work is relevant to the *English choices* made by earlier translators, but must **not** be placed alongside Swete, Göttingen, or Rahlfs–Hanhart as though it were a separately selected original Greek base text. Our project's primary draft remains an independently authored translation of the verified public-domain Greek, beginning with Swete's **1887** historical printed Greek edition for Genesis 1.

**Chosen use:** After our initial independent Greek-to-English draft and internal Greek fidelity audit, compare Brenton's historical English rendering to the corresponding verse as an **additional diagnostic**. Divergences may reveal a neglected Greek sense, stylistic decision, different underlying Greek printed reading, antiquated English idiom, or a possible error in either rendering. They are *questions to investigate*, not automatic corrections to our translation. The antiquity of the English rendering does not make it the earliest Greek manuscript or a uniquely authoritative Orthodox interpretation.

## Which historical Brenton edition?

The **International Organization for Septuagint and Cognate Studies (IOSCS)** provides a helpful historical edition inventory. **Identify the precise printing before quoting, comparing, or importing any text.** Historical editions should not be silently conflated:

| Printing | Historical identification | Scope caveat | Project use |
| --- | --- | --- | --- |
| **1844** | Brenton, *The Septuagint Version of the Old Testament, According to the Vatican Text, Translated into English*, London: Samuel Bagster and Sons | **English-only**; the published edition did **not include the Apocrypha**. Two volumes. | Candidate primary public-domain English print for Genesis and other covered books |
| **1851** | Bagster Septuagint publication connected with Brenton's translation and introductions | Includes **Septuagint Daniel and Apocrypha separately paginated**, with Fourth Maccabees identified in the historical bibliographic description. Check actual title pages, contents, and languages rather than assuming it is identical to 1844 or a later diglot. | Candidate expanded historical witness when 1844 lacks a book |
| **c. 1870** | Bagster edition associating Greek text and English translation in parallel (diglot), with readings and notes | IOSCS notes **uncertainty about the precise initial diglot date**; printings and added notes can differ. | Candidate where a verified historical page-by-page comparison is useful; do not substitute a 20th-/21st-century reprint without provenance |

**Primary bibliographic pointer:** IOSCS, *Brenton's Translation of the Septuagint*: https://septuaginta.uni-goettingen.de/ioscs/brenton/

**Digitized historical book catalog:** University of Michigan copy of Brenton's **1844** edition, Google Books: https://books.google.com/books?id=9GRYAAAAMAAJ

**Independent original-print scan identification:** Wikimedia/Wikisource record of **1844 Volume 1** derived from historical material: https://en.wikisource.org/wiki/File:The_Septuagint_Version_of_the_Old_Testament_-_Brenton_-_1844_-_Volume_1.djvu

Do not copy IOSCS's prose or any modern site's editorial additions into the open translation. These links establish *research leads and bibliographic facts*, not blanket permission for modern database or reproduction contents.

## Intellectual-property and independence safeguards

- The original **1844 / 1851 / nineteenth-century Brenton English publications are public domain in the United States by publication date**. This does **not** mean every modern revised edition, translation update, digital transcription, explanatory note, typesetting design, or reproduction has been separately cleared.
- For the user's project-specific restriction, use **the verified historical printed edition**, and if a text extract or machine-readable reference is ever needed, make an **independent transcription checked against original historical pages** and document its provenance. Do **not** request third-party licenses or permissions or ingest electronic material with unclear origin/rights.
- **We do not copy Brenton's English as our own** even where the historical original wording is legally public domain: the project promises an **original translation from Greek**, not a lightly modernized or derivative Brenton edition.
- The *old English* is a secondary cross-check for our translation workflow; a historical English rendering **cannot resolve a Greek manuscript dispute** without checking the relevant independently reusable Greek evidence.
- Modern reprint metadata and web availability do not by themselves verify a legally reusable original text; do not assume a book's coverage, numbering, or layout is the same in all printings. Other jurisdictions may require rights review before publication.

## Required comparison workflow

1. **Before looking at Brenton**, lock our verified Greek source edition/page and independently draft and audit our English chapter as required by [the Translation Protocol](TRANSLATION_PROTOCOL.md).
2. **Identify Brenton's exact historic edition, print page, book/chapter/verse, and book coverage**. Log the bibliographic citation and U.S. public-domain rationale. If the passage is absent or unverified in that printing, record “not available” rather than filling from a modern reprint.
3. **Compare meanings, not just word choices:** separately list our independently drafted English, Brenton's treatment (prefer an original summary over verbatim duplication in research notes), the corresponding verified Greek words, and whether the difference affects interpretation.
4. **Resolve through the Greek text:** identify possible grammar, manuscript variant, historical idiom, or translation error; document reasons for keeping or revising our independent wording. If Brenton's English seems to reflect another Greek witness, verify that source from independent admissible Greek evidence.
5. **Cross-link any meaningful case** to the relevant book's `notes/ot/<BOOK_ID>/` log and, if a theological/denominational interpretive question arises, the `GTC-###` entry in [the comparison register](ORTHODOX_PROTESTANT_TRANSLATION_COMPARISONS.md). Add a neutral footnote only for a *substantiated substantive difference* under the protocol; a stylistic mismatch alone is not evidence of a manuscript discrepancy.
6. **Record the result** with original edition, date, what was learned, whether any English wording changed, reason, unresolved uncertainty, and provisional/human-review status. Preserve the already established book-at-a-time drafting order and post-draft independent human review.

## Routine coverage, approval, and separate confidence accounting — amended 2026-11-12

The [Translation Protocol v0.11](TRANSLATION_PROTOCOL.md) requires an **automatic post-draft, post-Greek-semantic-audit Brenton comparison for every verse in a chapter where a verified historical Brenton printing covers that verse**. In this context, “automatic” means **run the diagnostic and document the evidence as part of an already authorized chapter drafting workflow**; it does **not** mean automatically revise or approve the English. A brief comparison of every verse is mandatory, while deeper research is triggered by potential material differences, not by stylistic variety alone. An absent or inaccessible source must be marked `not_available` or `blocked` rather than passed.

The **per-verse chapter audit ledger** must record: verse ID, inspected historical Brenton edition, actual printed-page/source-image URL, controlling Greek source edition/page, checked/not available/blocked state, concise semantic comparison, observed discrepancy classification, note/issue link if material, any proposed modification and its rationale, explicit user-decision status, and date. Chapter-level coverage completion must be supported by all verse records, not a general statement or one selected example.

**User approval is required before applying each Brenton-motivated change.** When Brenton suggests a possible translation, footnote or narration modification, present the exact proposed change and supporting **controlling Greek** evidence and ask the user. Hold the suggestion as `proposed_pending_user_approval` until the user specifically approves it. **Do not apply the proposed English or narration revision, even if the historical English happens to be clearer**, merely because the comparison was scheduled or because the user previously authorized drafting. Track declined suggestions without repeatedly proposing them absent new source evidence. An independently identified material source error that did not arise from the Brenton check follows the normal primary-Greek error-correction process.

**No Brenton-based confidence points or blended accuracy scores.** The existing Greek base-letter score and printed-bracket score are deliberately separate source-evidence diagnostics. Neither formula changes; Brenton adds **zero** to either and never clears a below-80 review flag. A Brenton comparison can open an **English semantic-quality issue**, but an English comparison does not independently certify a Greek character, apparatus boundary, or manuscript reading.

**Historical status:** Existing Genesis 1 research logs cite select 1844 original-page comparisons, but do not contain a newly required *individual completed entry for every verse*. Genesis 2 has **not** undergone this full Brenton step. This policy change **does not conduct, backdate, or certify Genesis 2's comparison**. Apply it to future drafted chapters and conduct historical catch-up only when the user later authorizes that chapter's work.

## Status and exclusions

- **Selected for historical comparison:** Brenton's original nineteenth-century English Septuagint, with 1844 prioritized where the passage appears; use a specifically verified later nineteenth-century printing for passages not in 1844.
- **Not selected as our primary Greek source:** Brenton's English is not the Greek text we are translating.
- **Not selected for text ingestion:** No digitized Brenton corpus has been imported, approved, or checked verse by verse.
- **No Scripture text or notes have been changed** by adding this reference.
- **Source register:** [`docs/SOURCE_REGISTER.csv`](SOURCE_REGISTER.csv) remains the intake record for actual imported sources; bibliographic candidate references here are not falsely marked imported or approved for ingestion.

## Source references

- International Organization for Septuagint and Cognate Studies, historical edition identification: https://septuaginta.uni-goettingen.de/ioscs/brenton/
- Google Books, 1844 title and bibliographic metadata (University of Michigan copy): https://books.google.com/books?id=9GRYAAAAMAAJ
- 1844 Volume 1 historic scan catalog: https://en.wikisource.org/wiki/File:The_Septuagint_Version_of_the_Old_Testament_-_Brenton_-_1844_-_Volume_1.djvu
