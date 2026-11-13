# Greek Septuagint source text

Reserved for chapter-aligned, independently transcribed Greek text from precisely documented public-domain editions.

## Proposed book layout

```text
sources/ot/greek/
  GEN/
    README.md              # Genesis source candidate, status and next actions
    chapters/
      001.txt              # future: Greek Genesis 1, only after verification
```

Other book IDs should match `translation/ot/`. A future chapter file should include stable verse identifiers and only the transcribed ancient Greek content. Exact serialization and normalization rules remain **provisional** until the Genesis 1 pilot establishes a tested convention.

For each imported chapter, preserve a verifiable connection to the historical printed page(s): edition, volume, page numbers, chapter/verse mapping, independent verification, any uncertainty or transcription corrections, and a checksum. Use the existing [source register](../../../docs/SOURCE_REGISTER.csv) for source-level rights/provenance rather than keeping contradictory duplicate registers.

**Do not import:** protected modern critical apparatus, copyrighted translations or notes, unverified OCR, modern digital transcriptions of uncertain status, or third-party content requiring permission or negotiated licenses.

Readers' explanatory footnotes belong in translation outputs; detailed evidence belongs in `notes/ot/`. Both must follow the [translation protocol](../../../docs/TRANSLATION_PROTOCOL.md).

**Status:** No actual Greek text files committed.
