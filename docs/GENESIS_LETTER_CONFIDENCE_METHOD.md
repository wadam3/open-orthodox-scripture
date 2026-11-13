# Genesis 1–2 — verse-level Greek letter confidence and 80% recheck rule

**Adopted:** 2026-11-12 (America/New_York). **Source:** H. B. Swete, *The Old Testament in Greek According to the Septuagint*, vol. I, **first edition (1887)**; photographed printed [p. 1](https://ccel.org/ccel/swete/lxx1/lxx1/png/0029=1.png), [p. 2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png), [p. 3](https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png), and [p. 4](https://ccel.org/ccel/swete/lxx1/lxx1/png/0032=4.png). The scanned book's [1887 title page](SWETE_1887_TITLE_PAGE_EVIDENCE.md) controls edition identity.

## Standing threshold (same rule as editorial brackets)

**Any verse-level letter-confidence estimate strictly below 80% must be flagged for more rigorous verification at a later date.** At or above 80% the extra low-confidence queue is not triggered, but **routine source proofreading is still mandatory**. Scores are rounded editorial estimates, **not calibrated probabilities** and not evidence of independent human approval. The exact printed accents, breathing marks, iota subscripts, punctuation, brackets and printed apparatus cannot be certified merely from an electronic letter match.

## What was actually compared

- Every one of the **56 existing working Greek verses** was compared by its **base Greek-letter sequence** (accent/diacritic/punctuation stripped) to an **independent diagnostic transcription** of Swete's **1901** volume I, electronically encoded by Perseus/First1KGreek in **2015**: [text and source metadata](https://beta.perseus.tufts.edu/urn:cts:greekLit:tlg0527.tlg001.1st1K-grc1:1/) and [source XML](https://raw.githubusercontent.com/PerseusDLCode/First1KGreek/HEAD/data/tlg0527/tlg001/tlg0527.tlg001.1st1K-grc1.xml). **Neither that later printing nor its separately CC BY-SA-licensed digital transcription is imported into our Greek source**; only numeric agreement and concise discrepancy descriptions are recorded here.
- The **1887 photographed pages** were used as the authority in the original first-pass Greek drafting and in targeted visual rechecks. This round's electronic diagnostic is **not a substitute for independent line-by-line collation** of all those photographed 1887 characters.
- The Perseus electronic file has **documentable encoding errors** (for example an extra repeated “ἡμέρα” in 1:31, and it assigns **Genesis 2:25** under **3:1**). Consequently 1901 agreement can only be weak corroboration, and disagreement is a **review trigger**, not proof that the 1887 text or our working reading is wrong.
- Individual editorial square-bracket observations, including 41 existing restored spans, have **separate bracket scores** under [the bracket confidence method](GENESIS_BRACKET_CONFIDENCE_METHOD.md). The verse scores here assess the **running Greek base-letter sequences**, *not* confidence in the positions of `[` and `]`. The two cannot be substituted for each other.

## Reproducible letter-comparison score

For each verse, compare the Unicode Greek base-letter sequences after decomposing Unicode to NFD, removing all combining accents/marks, case-folding, mapping final sigma `ς` to `σ`, and excluding punctuation, spaces, printed verse numbers, manuscript apparatus, and electronic markup. Use ordinary Levenshtein character edit distance, computed as `1 - edits/max(number_of_letters_in_draft, number_in_comparator)`, multiplied by 100. That **letter-agreement percentage is an objective metric between two strings, not confidence that either string reproduces 1887 correctly**.

Assign the following *subjective, conservative editorial letter-confidence rating*, with an **85% cap** because neither the independent full 1887 character proof nor every diacritic has passed:

| Letter sequence agreement to 1901 diagnostic text | Editorial confidence score |
| --- | ---: |
| Exact normalized Greek letter match | 85% |
| 99% or higher, not exact | 80% |
| 98% to less than 99% | 75% |
| 95% to less than 98% | 70% |
| Below 95% | 60% |
| Electronic comparator absent/unusable or misassigned to the wrong verse | 65% |

**Adjustment:** deduct 5 percentage points when the verse is split across **1887 printed pages** (Genesis **1:14**, **1:29**, or **2:16**), because the word-joining boundary needs an additional image check. Scores are never increased based on a theological expectation. Bracket candidates receive **no extra letter-score penalty** because their uncertain bracket placement is already separately scored and flagged.

Each verse's entry must include: first-edition page URL(s); diagnostic comparator agreement and limitations; confidence score; the exact strict-below-80 flag; a brief explanation of its evidence; and **`independent_1887_character_certified: false`** until a separate original-page check is actually completed. Any future actual 1887 character-level correction requires updating the chapter's working Greek, its English audit if meaning changes, its narration if English changes, and the corresponding hash manifest.

## Findings to consider in the source-language recheck

- **1:10**: the 1901 digital line spells the “gatherings” term differently; inspect the 1887 word `συστήματα`, not a modernized/OCR alternative.
- **1:31**: the digital transcription repeats `ἡμέρα` at the close, unlike the photographed 1887 page. Do not add a second word.
- **2:9**: the later electronic text uses a different inflection in the knowledge-tree wording; the first-edition photograph, not the 1901 form, governs the original English draft.
- **2:11**: river/land spelling and a small linking phrase differ; read `Εὐιλάτ` and `ἐκεῖ οὗ` from the 1887 photo, and document any exact accent uncertainty.
- **2:17**: **Resolved targeted Greek word discrepancy**—the photographed 1887 page 4 reads `φάγησθε`; the working line previously had `φάγητε` and was corrected. Later electronic text now matches the 96 normalized base letters exactly. This targeted correction does not certify the whole verse's accents, punctuation or brackets.
- **2:19–20**: the 1901 digital line has several evident possible encoding errors and an inflection difference; the actual 1887 p. 4 photograph remains controlling.
- **2:25**: the digital chapter/verse segmentation is corrupted; direct comparison to its “2:25” cannot be used for confidence scoring, even though our original 1887 page visibly includes the verse.

## Efficient review and stop rule

Prioritize **material Greek transcription mistakes**: omitted/changed letters with strong 1887 photographic evidence, changes affecting an English clause, wrong verse boundaries, and source-word forms that matter. Fix those immediately; update the paired English/narration only when meaning changes. Record a focused rationale.

For other differences that remain reasonably translated, **do not spend repeated rounds resolving 1887-versus-1901 discrepancies at low photographic resolution**. Keep the estimated confidence, the original source-page reference, the specific uncertainty, and the **strict-below-80% deferred rigorous-review flag**. Even scores at or above 80% still await the eventual whole-text character/diacritic check and later human review; they are **not certified**. Revisit deferred cases when stronger 1887 primary evidence becomes available or a change materially affects translation meaning.

**Applied example:** Genesis 2:17's original-page check corrected Greek `φάγητε` to `φάγησθε`. Its base-letter comparison then became exact, moving its estimated score from 70% to 85%. The English “you eat” and narration did not need changing. The remaining lower-confidence verses stay queued rather than blocking ongoing drafting indefinitely.

## What the check does and does not close

This diagnostic can complete a **base-letter comparison of 56 draft verses to a separate machine-readable text**, provide a transparent 80% queue, and reveal possible transcription anomalies. It **cannot honestly certify the original 1887 printing character-for-character**, especially accents, breathings, bracket positions and apparatus. Those still require a separate exhaustive source-photo pass. Scores do not change the repository's `status=draft` or `source.transcription_verified=false`, and qualified Orthodox/human review remains a distinct later step.
