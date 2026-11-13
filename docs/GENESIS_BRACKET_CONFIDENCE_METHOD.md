# Genesis 1–2 — confidence percentages for editorial bracket observations

**Version:** 1.0, 2026-11-12. **Edition controlled by original source:** H. B. Swete, *The Old Testament in Greek According to the Septuagint*, Vol. I, **1887 first printing**, scanned [printed page 2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png) and [page 3](https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png). The book identity is independently established from the [photographed 1887 title page](SWETE_1887_TITLE_PAGE_EVIDENCE.md).

## What a percentage means

Each percentage is a **subjective, conservative editorial confidence score** for **whether the proposed `[` and `]` bracket boundaries and their immediately enclosed letters have been read correctly from a small historical photograph**. It is **not** a statistically calibrated probability, not the confidence that the biblical event occurred, not the certainty of the English translation, and not permission to label the Greek diplomatically proofread or source-verified. A score of 90% does **not** mean a 10% measured error rate. Human readers and better scans may disagree.

The numeric values are deliberately rounded to **5 percentage-point steps**. They serve prioritization and traceable disclosure, **not** false precision. The unverified bracket intervals *must remain flagged even above 85%*; this rubric does not replace checking every accent or manuscript apparatus line.

## Explicit scoring procedure (0–90 points available)

1. Start from the saved **direct-photo visual-assessment category**: `high=80`, `medium=65`, `low=45`, or `unresolved=25`. High means both edges are comparatively conspicuous in the 1887 scan; medium has visible support but one or more accents, punctuation or edges are less distinct; low represents material ambiguity; unresolved means the interval could actually be multiple distinct brackets.
2. Add **5 points** only if the **full before + inside + after character sequence, ignoring diacritics and punctuation**, is contiguous in the project's 56-verse *working Greek* at the specified verse location. This is a **weak consistency test**—the working Greek is an AI-authored draft, **not** an independent manuscript witness. If no such match exists, **subtract 10 points** instead and flag the inconsistency.
3. Subtract **5 points** if a bracket **crosses a printed verse boundary or split line**, because the source's line-break hyphen or raised verse number may be misread as text; record this deduction explicitly.
4. Subtract **10 points** for a candidate whose **earlier map was contradicted or reinterpreted** (such as `1:30` vegetation versus the formerly assumed one long bracket, or the corrected `1:29` closure). Such candidates need extra independent proofing even when current evidence looks persuasive.
5. **Cap at 90** to make clear that neither the assistant's repeated visual look nor a 1901 digital comparator constitutes independent 1887 character verification. Minimum 20. Round to the nearest 5 percent.

**Important:** The later 1901-based Perseus transcription may suggest where to look, but gets **no numerical bonus**: it is a *different edition*, has electronic errors, and does not prove an 1887 bracket. The 1887 Alexandrinus lacuna footnotes support **that supplemented text exists within the stated range**, not where any individual `]` closes, and receive **no bonus** either.

## Standing rule: deferred rigorous verification below 80% (adopted 2026-11-12)

**Any editorial bracket candidate with a confidence estimate strictly below 80% must be flagged for a later, more rigorous check.** A score exactly equal to 80% is not flagged under this threshold. Each entry in the [printed-page-2 candidate register](../notes/ot/GEN/p2-1887-bracket-candidates.json) or [printed-page-3 candidate register](../notes/ot/GEN/p3-1887-bracket-candidates.json) must keep its numeric `editorial_confidence_percent` and method/reasoning, together with:

- `requires_rigorous_verification_later: true` and `verification_queue: "deferred_rigorous_verification"` when the score is **below 80%**.
- `requires_rigorous_verification_later: false` and `verification_queue: "routine_source_proofing"` when the score is **80% or higher**.

For **both categories**, `verification_status` stays `pending` until actually reviewed, and `original_square_brackets_certified` remains `false` until full photographic source verification. **A high score does not constitute approval.** Upon any future score change, recalculate the flag and queue classification; never silently erase the recorded history or evidence. The later rigorous check should inspect the original 1887 image at adequate magnification, each `[`/`]` boundary, underlying letters, diacritics, line/verse transitions and apparatus, with the findings recorded.

**Baseline at adoption:** 41 candidates; **34 flagged below 80%**, **7 at or above 80%**. The queue is a prioritization tool; the whole chapter still needs ordinary Greek character-level checking.

## Interpretation and required action

| Estimated bracket-boundary confidence | Editorial label | Required next step |
| --- | --- | --- |
| 85–90% | **Reasonably supported working reading** | Retain as a clearly provisional image-based observation; separately verify every letter/accent and both bracket marks before source sign-off. |
| 65–80% | **Plausible, needs enlargement** | Keep in working notes; inspect larger original scan and resolve exact boundary. |
| 40–60% | **Low-confidence candidate** | Do not put into a diplomatic source; obtain better evidence or qualified proofing. |
| 20–35% | **Unresolved** | Record plausible alternatives or a gap, not invented bracket characters. |

There is **no automatic source-approval threshold**. Even a 90% score is **not certified**, because original-source-level correctness must be demonstrated rather than inferred from a heuristic.

## Scope of the two chapter review

- **44 verses** have no currently logged Alexandrinus restoration brackets (Genesis 1:1–19 and 1:26–28 = 22 verses; Genesis 2:4–25 = 22 verses). These need the **ordinary character/diacritic/punctuation comparison** separately from the bracket register. The absence of a known A-lacuna does **not** itself prove that every source character was checked.
- **12 verses** are within the two documented reconstructed ranges (Genesis 1:20–25, 1:29–31, Genesis 2:1–3). Their ordinary, unbracketed letters **also** need character proofreading, in addition to the bracket maps.
- [Source-image page 2 candidates](../notes/ot/GEN/p2-1887-bracket-candidates.json) and [page 3 candidates](../notes/ot/GEN/p3-1887-bracket-candidates.json) store the **score, formula inputs, method reference, and per-entry reasoning**. The source photo remains decisive.
- The two existing English-to-narration checks and SHA-256 content integrity tests already pass; this confidence assessment does not alter translation text or any existing certified/approved flags.

**Separate later human review** is deferred until the provisional Bible draft under the project's policy. **AI character proofreading still must not be misrepresented as independent expert certification.**
