# Contributor workflow — Greek source confidence, flags, and independent verification

**Policy adopted 2026-11-12.** Use this with the [Greek source-verification protocol](GREEK_SOURCE_VERIFICATION_PROTOCOL.md), the [bracket scoring rubric](GENESIS_BRACKET_CONFIDENCE_METHOD.md), and the [verse-letter scoring rubric](GENESIS_LETTER_CONFIDENCE_METHOD.md). This workflow defines how future contributors can improve individual findings **without silently changing an edition, erasing uncertainty, or claiming Church approval**.

**Contribution timing:** The project's [contributing policy](../CONTRIBUTING.md) currently defers recruiting external reviewers until the provisional Bible draft is assembled. This guide prepares the queue and standards for that later stage; it does **not** announce that formal outside review is already open.

## 1. Find a specific item rather than rechecking whole chapters

The two independent queues are:

- **Editorial brackets / Alexandrinus gaps:** [1887 printed page 2 candidates](../notes/ot/GEN/p2-1887-bracket-candidates.json) and [printed page 3 candidates](../notes/ot/GEN/p3-1887-bracket-candidates.json), keyed by bracket IDs such as `GEN-001-023-F`. Their score is `editorial_confidence_percent` and the proof flag is `original_square_brackets_certified`.
- **Running Greek letters:** [verse-level confidence register](../notes/ot/GEN/001-002.letter-confidence.json), keyed by verse IDs such as `GEN-002-017`. Its score is `editorial_letter_confidence_percent` and the proof flag is `independent_1887_character_certified`.

A candidate with a **score strictly below 80%** must have `requires_rigorous_verification_later: true`; otherwise it must have `false`. **Exactly 80% is not below 80%.** Its `verification_queue` must be `deferred_rigorous_verification` when below 80; for higher-scored entries the current routine queue names are `routine_source_proofing` (brackets) or `routine_1887_photo_proofing` (letters). **Even an 85% or 90% draft reading still needs ordinary photo proofing.** All confidence scores are *editorial estimates*, never calibrated correctness probabilities.

**Current baseline, subject to later improvements:** 41 bracket candidates, **34 below 80%**; 56 Greek verse candidates, **7 below 80%**. An item is *actively outstanding* when it has `requires_rigorous_verification_later=true` **and** its `verification_status` is **not** `verified`. Keep the numerical risk flag even after proofing if the original scoring method still rates it below 80%; the verified status plus evidence closes the *active review task*. This keeps historical uncertainty visible instead of silently upgrading a subjective percentage.

## 2. Reproduce the existing score, then examine better primary evidence

1. Open the exact first-edition photographic page recorded on the item. For Genesis 1–2, the [photographed 1887 title page](SWETE_1887_TITLE_PAGE_EVIDENCE.md) establishes edition identity, and [printed pages 1–4](https://ccel.org/ccel/swete/lxx1/Page_Index.html) establish the text. Record the actual **printed page, line, and enclosing Greek**. Crop coordinates or a page-and-line description help the next reviewer find an ambiguous mark.
2. For **brackets**, record each `[` and `]` separately, including partial words, printed line endings and a bracket crossing a verse. Recompute using the [explicit visual-category, surrounding-text, line-wrap and previous-conflict formula](GENESIS_BRACKET_CONFIDENCE_METHOD.md). Preserve the `confidence_input`, `confidence_reasoning` and `editorial_confidence_percent` fields. Later-edition electronic transcriptions provide **no bonus**.
3. For **letters**, compare each Greek base-letter sequence with the clearly identified **1901-derived electronic comparator only as a diagnostic**, using the [NFD normalization, edit-distance and 85% cap rubric](GENESIS_LETTER_CONFIDENCE_METHOD.md). It cannot certify 1887 accents, punctuation or manuscript marks. Record how many letters were compared, edits, comparison availability and any page-break penalty.
4. If the **1887 image is sharper** or a legitimate alternate 1887 scan is found, document the exact reading and evidence. **Do not boost the computed percentage arbitrarily**: update the inputs and recompute the stated formula, or propose a versioned scoring-policy change in a separate PR. A proofed word may legitimately retain a below-80 *secondary-comparator* score, while its independent original-image verification status becomes `verified`.
5. If the mark remains illegible, keep it `blocked` or `pending` and document competing readings and the required image/evidence. **Do not infer Greek from theology, English, a later edition or a model's agreement with itself.**

## 3. One issue, one evidence-backed pull request

When external contribution is opened, start with the [Greek verification issue template](../.github/ISSUE_TEMPLATE/greek_verification.md) and refer to the exact **item ID(s)**. The PR must include:

- **Before and proposed after:** complete bracket interval or verse-level Greek characters; identify any changes to accents, breathings, capitalization, punctuation and printed word division.
- **Primary provenance:** confirmed **1887** first-edition photograph URL, printed page/line, and what the print actually shows; alternative sources clearly labeled *comparators* and their rights respected.
- **Score audit:** old percentage, new percentage, exact rubric inputs/math, whether the **strict below-80 flag** changed, and why. Do not remove a low-score item without either formula-based recalculation or explicit independent verification.
- **Impact:** whether English meaning, reader notes, narration script, scholarly apparatus, source claims, or rights change. When English changes, update the JSON and narration text together; recompute checksums. A Greek-only character correction may leave English/audio untouched.
- **Traceability:** include issue/PR link, reviewer role or GitHub handle (only with consent), review date, actual actions performed, and append a `review_history` entry. **Never overwrite or erase an earlier reading without a changelog.**
- **Checks:** `python scripts/validate_chapters.py`, `python scripts/verify_genesis_pilots.py --verify-manifest`, and `python scripts/validate_greek_confidence.py`, plus a passing GitHub Actions run. Passing code checks validates *data consistency*, **not manuscript correctness**.

## 4. Status and independent review: evidence, not vote count

Each candidate has a `verification_status`:

| Status | Meaning | Allowed to claim original-photo certification? |
| --- | --- | --- |
| `pending` | Not yet independently proofed | No |
| `in_review` | A new source-image comparison is documented but not independently confirmed | No |
| `blocked` | Image or witness evidence insufficient; specify the blocker | No |
| `verified` | Two **distinct reviewers** independently examined the original 1887 photograph, reconciled the exact characters and apparatus, and recorded the evidence | **Only for this item**, not the chapter |

A person or AI that repeats its own reading does **not** constitute an independent reviewer. The second reader must consult the actual source image independently, not simply approve the first transcriber's assertion. The future workflow may use an AI first pass and **qualified human independent verification**, but the review must accurately name who/what performed each stage; GitHub collaboration or code passing by itself establishes no independent Greek expertise.

For `verification_status: "verified"`, attach an actual `review_evidence` object containing:

```json
{
  "primary_reviewer": "contributor-handle",
  "primary_review_date": "YYYY-MM-DD",
  "secondary_reviewer": "distinct-reviewer-handle",
  "secondary_review_date": "YYYY-MM-DD",
  "independent_second_pass": true,
  "original_image_urls": ["https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png"],
  "printed_page_and_line": "p. 3, line / column or crop locator",
  "evidence_url": "https://github.com/wadam3/open-orthodox-scripture/pull/EXAMPLE",
  "exact_printed_reading": "Greek text including any brackets",
  "apparatus_disposition": "Apparatus and witness claim checked / none relevant",
  "finding": "Which characters were compared and how the discrepancy was resolved"
}
```

This is a **schema example, not a claim of any completed review**; replace placeholders only with real evidence and links. The matching boolean `original_square_brackets_certified` (for a bracket item) or `independent_1887_character_certified` plus `diacritics_and_punctuation_proofread` (for a letter item) may become `true` only with the completed item-level evidence. At `pending`, `in_review` or `blocked`, these booleans stay `false`.

When a correction is made or an item is reviewed, append to its `review_history` rather than deleting the old assertion:

```json
{
  "date": "YYYY-MM-DD",
  "issue_or_pr": "https://github.com/wadam3/open-orthodox-scripture/pull/EXAMPLE",
  "previous_reading": "earlier proposed Greek",
  "proposed_reading": "new Greek from the 1887 photo",
  "previous_confidence_percent": 60,
  "new_confidence_percent": 85,
  "reason": "Describe which printed characters justified the change",
  "reviewer": "contributor-handle"
}
```

Dates, identities and links above are **examples** and must not be fabricated. The CI validator checks **presence and consistency**, not whether reviewers actually examined a source image; that is the maintainer's and independent reviewer's responsibility.

## 5. Closing versus escalating an item

- A reviewer may resolve a single reading without clearing every issue in the verse or chapter. **Item-level `verified` does not imply chapter-level `transcription_verified=true`**, Orthodox doctrinal approval, or rights approval.
- Any material Greek error affecting English clauses, negatives, theological or lexical categories, person/number, or the audiobook should be **fixed promptly**, even if its confidence was previously high.
- Minor disagreements with a later electronic edition that **do not affect intelligible translation** may stay in the below-80 queue for later rigorous review; do not endlessly revisit unchanged evidence.
- If two credible reviewers disagree, mark `blocked`, document both readings and request a higher-resolution image or a third qualified adjudicator. Do **not** average votes into a confidence percentage.
- Preserve the old and new values in Git history, add the review event, update score and flags mechanically, and allow CI to verify consistency. Do not represent any individual reader's opinion as an endorsement from an Orthodox Church.

## 6. Extend the process to later biblical books

Keep the **same strict <80 threshold, separate bracket/letter registers, evidence fields, source-edition pinning, and independent review requirement** for later chapters. Create book-specific registers and CI coverage as books are drafted; the existing automated validator currently targets **Genesis 1–2 only**, and its success must not be claimed for other books. Later scoring methods may change only with a versioned, documented rationale and an explicit migration of earlier scores.
