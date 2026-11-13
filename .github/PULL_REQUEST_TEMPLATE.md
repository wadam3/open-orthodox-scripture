## Summary

## Kind of change
- [ ] Translation/editorial
- [ ] Source rights / provenance
- [ ] Audio
- [ ] Repository tooling or documentation

## Provenance and rights
- Source edition and specific citation:
- Reuse rights reviewed (or state not applicable):
- Is any third-party material included? If yes, explain:
- AI assistance used, if any:

## Review
- Language editor:
- Orthodox reviewer (required before marking Scripture approved):
- Audio second-listener QA (if relevant):

## Greek source verification, if applicable
- Candidate ID(s), present score(s), and below-80 flag(s):
- Selected first-edition source page URL, printed line/crop and exact Greek:
- Previous versus proposed Greek, accents, breathings and editorial brackets:
- Confidence score recomputed using [the mandatory formula](../docs/GREEK_SOURCE_VERIFICATION_PROTOCOL.md), with all input values:
- Explanation of changed or unchanged flag (strictly **below** 80, not equal):
- Independent first and second image-reading evidence (or state pending/blocked):
- Reviewer identifiers and review dates when actually known (do not invent):
- Append-only item review_history and PR/issue link:
- English/narration and source-hash impact, if any:
- Do not mark a candidate `verified` without required evidence; do not mark a chapter approved merely because one item was verified.

## Local checks
- [ ] `python3 scripts/validate_chapters.py`
- [ ] No credentials, copyrighted external translation passages, or unlicensed voices added
- [ ] `python3 scripts/validate_greek_confidence.py` (for Greek candidate changes)
- [ ] `python3 scripts/test_greek_confidence.py` (for score/validator changes)
- [ ] Chapter/draft status and review evidence accurately represented
