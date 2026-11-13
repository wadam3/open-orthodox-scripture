# Genesis 1–2: pre-human technical and source-fidelity QA checkpoint

**Checkpoint:** 2026-11-12 (America/New_York); GitHub Actions run [43359844374](https://github.com/wadam3/open-orthodox-scripture/actions/runs/43359844374). **Controlling text:** H. B. Swete (editor), *The Old Testament in Greek According to the Septuagint*, **first edition, volume I (1887)**, [printed pp. 1–4](https://ccel.org/ccel/swete/lxx1/Page_Index.html). This is a **technical-accuracy checkpoint**, *not* publication approval, a claim of Orthodox Church authority, or a substitute for qualified human philological review.

## Confirmed results

| Check | Genesis 1 | Genesis 2 | What the passing result actually proves |
| --- | ---: | ---: | --- |
| English verse count and continuous numbering | **PASS: 31/31** | **PASS: 25/25** | No missing/duplicate numbered verse records in our original English JSON |
| Working Greek verse coverage/numbering | **PASS: 31/31** | **PASS: 25/25** | A Greek *working reading* exists for each verse; **not** that its individual characters are accurate |
| Pilot narration text matches English verses | **PASS: 31/31** | **PASS: 25/25** | Exact normalized text equality, with a single heading and paragraph pauses; no recorded audio was listened to |
| Reader-note IDs unique | **PASS** | **PASS** | No duplicate note identifiers |
| First-edition source identity and image links | **Documented** | **Documented** | Sources are pinned to Swete's **1887** first printing; no later revision silently substituted |
| Chapter JSON structure / manuscript note linkage | **PASS: automated** | **PASS: automated** | `scripts/validate_chapters.py` plus special Genesis QA ran successfully in [GitHub Actions](https://github.com/wadam3/open-orthodox-scripture/actions/runs/43359844374) |
| SHA-256 for 7 live project text files | **PASS: exact file bytes** | **PASS: exact file bytes** | [Machine-readable hash manifest](GENESIS_1_2_CONTENT_HASHES.json) detects alteration of the committed drafts, working Greek and scripts. **No raw Greek image file hash was obtained** |
| Source-level per-letter transcription including all 1887 editorial square brackets | **NOT YET VERIFIED** | **NOT YET VERIFIED** | The Greek working files are intentionally normalized and omit original bracket formatting |
| Independently qualified Greek-to-English accuracy certification | **NOT YET VERIFIED** | **NOT YET VERIFIED** | AI semantic checks and narration equality do not prove source-character accuracy or expert sign-off |
| Source reuse/release approval | **NOT YET APPROVED** | **NOT YET APPROVED** | U.S. public-domain bibliographic evidence exists; the separate rights and provenance sign-off gate is not recorded |

**Result:** Both chapters pass the automated, reproducible *file-integrity* gate. They have undergone AI-assisted original-Greek meaning comparisons, including identified and corrected omissions. **They have not passed the source-diplomatic or independent Greek-verification gate**, so `status: draft`, `transcription_verified: false`, and `rights_reviewed: false` remain correct.

## Primary-source image and edition checks

- [Original 1887 photographed printed p. 1](https://ccel.org/ccel/swete/lxx1/lxx1/png/0029=1.png): Genesis 1:1–14 (verse 14 starts on this page).
- [Original 1887 photographed printed p. 2](https://ccel.org/ccel/swete/lxx1/lxx1/png/0030=2.png): Genesis 1:14 continuation–1:29 beginning; brackets and printed apparatus for 1:20–25.
- [Original 1887 photographed printed p. 3](https://ccel.org/ccel/swete/lxx1/lxx1/png/0031=3.png): Genesis 1:29 continuation–1:31 and Genesis 2:1–2:16 beginning; brackets and apparatus extending through 2:3.
- [Original 1887 photographed printed p. 4](https://ccel.org/ccel/swete/lxx1/lxx1/png/0032=4.png): Genesis 2:16 continuation–2:25. **Genesis 2:16 crosses pp. 3–4.**
- [Cambridge University Press](https://www.cambridge.org/core/books/old-testament-in-greek-according-to-the-septuagint/58D0D0A49BA2F1D53DB004EA01A1C052) confirms first publication of volume I in **1887**. [Princeton Theological Commons](https://commons.ptsem.edu/id/oldtestamentingr01swet) catalogs the **1887** edition and lists **“No Known Copyright.”** This is **supporting evidence**, not a completed legal approval or guarantee for every territory or subsequent digitization.
- Swete's original apparatus says the **parts enclosed in brackets** are lost in surviving Codex Alexandrinus (A) for Genesis **1:20–25** and **1:29–2:3**. It does **not** mean all words in those verses are unattested in every Greek manuscript.

## Retained Greek-specific translation decisions

- **1:14** includes the first-edition printed clause `καὶ ἄρχειν τῆς ἡμέρας καὶ τῆς νυκτὸς` (“to govern day and night”), already restored in English.
- **1:20** describes *moving living creatures*, not a later-language or Hebrew-source paraphrase; English was corrected earlier.
- **1:31** restores the audible “behold” corresponding to `ἰδού`.
- **2:2** uses the **sixth day** for completion of God's works and the **seventh day** for rest, preserving the selected 1887 Greek.
- **2:6** retains Greek `πηγή` as a **spring**, rather than silently importing “mist” from a different base text.
- **2:9** and **2:19** each restore Greek `ἔτι` (“also”), omitted in the first English pilot; both narration scripts reflect these corrections.
- **2:17** Greek plural prohibitions remain an open translation annotation because English “you” does not distinguish singular and plural.
- **2:18** retains Greek `ποιήσωμεν`, “Let us make.”

These are **source-informed AI translation decisions** with original-page evidence and reader notes, not a character-by-character certified diplomatic collation.

## Precise blockers before saying “everything except human review is done”

1. **Genesis 1:20–25**, original printed p. 2: multiple bracketed restorations, sometimes **inside Greek words**, need exact original-page opening/closing bracket positions, all letters, accents, breathing and critical apparatus recorded together. [Current tentative map](../notes/ot/GEN/001.bracket-map.md).
2. **Genesis 1:29–31 and Genesis 2:1–3**, original p. 3: the Alexandrinus-loss note crosses chapter boundaries. The candidate combined bracket around `χόρ...` through `καὶ ἐγένετο` in **1:30 is withdrawn as unproved**; do not treat it as one verified segment. [Genesis 1 observations](../notes/ot/GEN/001.bracket-map.md), [Genesis 2 observations](../notes/ot/GEN/002.bracket-map.md).
3. **All 56 Greek verses:** complete a careful **source-letter/diacritic/typographic** read against original 1887 images, with a second separate pass, BEFORE importing a verified Greek source to `sources/ot/greek/GEN/`. Working Greek coverage alone is **not** a pass.
4. **Reconcile the diplomatically source-checked Greek** against every English clause, capture accepted variants and the final apparatus, then complete explicit source rights intake and log direct byte hashes for the approved Greek source. The present hashes establish **project file identity**, not historic image fidelity.
5. **Real narration audition:** only text scripts exist; there is no production recording or listening-review evidence. Script equality is already checked.

**Human review intentionally deferred by project policy:** qualified Greek, Orthodox, editorial and rights/publication sign-offs occur after the provisional full Bible draft. No one should manufacture their identities or imply an ecclesiastical endorsement. The technical blockers above are distinct from that future human stage; simply calling those blockers “human review” would misrepresent current source verification.

## Additional pre-human evidence checkpoint — 2026-11-12

A documented [confidence-rating procedure](GENESIS_BRACKET_CONFIDENCE_METHOD.md) has now been applied to **41 original-image bracket candidates** in the [1887 p. 2 register](../notes/ot/GEN/p2-1887-bracket-candidates.json) and [p. 3 register](../notes/ot/GEN/p3-1887-bracket-candidates.json). Each entry includes an **estimated percentage**, formula inputs, local Greek contextual check, and plain-language reason; all remain marked **not certified**. Scores range from **35% to 85%** under the scoring rubric, which deliberately caps possible results below 100%. They are **subjective editorial confidence estimates, not calibrated probabilities** or a basis for silently accepting an uncertain bracket.

A separate [ordinary-Greek Unicode-readiness report](../notes/ot/GEN/001-002.unicode-readiness.md) checked all **56 working Greek verse lines** for NFC normalization, Greek-script presence, replacement/control characters and Latin-character contamination, with **no such encoding problems found**. It enumerates **44 verses without the recorded Alexandrinus bracket restorations**, separately from the **12** verses in the affected ranges. **Crucial limitation:** that report did not directly compare all Greek letters, breathing marks, accents or punctuation against a magnified first-edition photograph. Source-level letter-by-letter proofing remains **0 of 56 completed**, and independent qualified source certification remains open.

**Result:** Broader technical validation and transparently scored bracket hypotheses are now documented; **neither chapter has yet satisfied the original-image letter proofing or independent Greek accuracy gate**.

## New verse-level letter-confidence diagnostic and strict 80% queue

An [explicit source-letter confidence rubric](GENESIS_LETTER_CONFIDENCE_METHOD.md) and [machine-readable report covering all 56 verses](../notes/ot/GEN/001-002.letter-confidence.json) are now recorded. Each verse has source printed-page references, working-letter count, a separate **1901-derived electronic comparison**'s edit distance and letter-agreement percentage, a **conservative editorial confidence rating**, an evidence explanation and the **strict-below-80 flag**. **7 of 56 verses** remain flagged for more rigorous verification: **Genesis 1:10 (75%), 1:31 (60%), 2:9 (75%), 2:11 (70%), 2:19 (75%), 2:20 (75%), and 2:25 (65%)**. The other **49** are at or above 80%; **47** of the 56 now match the later digital text exactly after stripping punctuation and diacritics, and **2:25** is wrongly placed outside Genesis 2 in the electronic comparator.

**Interpretation:** 80% is a **triage threshold**, not automatic Greek verification. A score of 85% chiefly means that a *later electronic edition* matches the working **base-letter sequence**; it **does not establish that the first-edition 1887 accents, breathings, diacritics, punctuation, or every character were visually collated**. The original 1887 photographic images always control the text. The previously logged **34 of 41 bracket candidates below 80%** remain a separate deferred-rigorous-verification queue. Do not equate internal diagnostic match with approved, diplomatic, or independently source-verified Greek. Both chapters remain drafts.

**Targeted follow-up:** Genesis **2:17** was corrected from `φάγητε` to the printed 1887 Greek `φάγησθε` without changing the English or narration. This removes one lower-confidence *diagnostic* flag, **not** the need for eventual full first-edition character proofing. Under the project's efficiency rule, remaining inconsequential edition differences are recorded and deferred rather than endlessly re-compared.

## Reproducible commands and artifacts

```bash
python scripts/validate_chapters.py
python scripts/verify_genesis_pilots.py --verify-manifest
python -m py_compile scripts/validate_chapters.py scripts/verify_genesis_pilots.py
```

The public GitHub Actions workflow [`genesis-pilot-qa.yml`](../.github/workflows/genesis-pilot-qa.yml) runs these automatically on relevant changes. [Successful run 43359844374](https://github.com/wadam3/open-orthodox-scripture/actions/runs/43359844374) confirmed all three steps passed after fixing a parser that previously counted numbered English research instructions as Greek verses. The earlier failing run remains in GitHub history; it was not concealed.

The [English chapter files](../translation/ot/GEN/README.md), [Greek working text for Genesis 2](../notes/ot/GEN/002.greek-working.md), [chapter 1 verification ledger](../notes/ot/GEN/001.verification-log.md), [chapter 2 verification ledger](../notes/ot/GEN/002.verification-log.md) and [SHA-256 manifest](GENESIS_1_2_CONTENT_HASHES.json) are the durable handoff. **Do not mark either chapter source-verified or publication-approved yet.**
