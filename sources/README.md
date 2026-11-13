# Source texts — workspace and intake plan

This directory is for **independently verified public-domain source material** and the information needed to reproduce its transcription. It is separate from the English translation, the translation research logs, and the project-wide rules.

**Current status (2026-11-12): Structure only. No Greek source text or manuscript scans have been imported or approved for reuse.**

## Historical edition links

- [Source URL index](SOURCE_URLS.md): historical Swete Greek volumes, Brenton's nineteenth-century English volumes, and related source-selection references. URLs only; no files downloaded or imported.

## Directory map

- [`ot/`](ot/README.md): Old Testament source planning.
- [`ot/greek/`](ot/greek/README.md): Proposed home for transcribed Greek Septuagint passages.
- [`nt/`](nt/README.md): Reserved for New Testament source planning; no edition chosen.
- [`patristic/`](patristic/README.md): Apostolic Fathers / early Church source evidence workspace (not biblical Scripture).

Related locations remain authoritative for their respective purposes:

- [`docs/TRANSLATION_PROTOCOL.md`](../docs/TRANSLATION_PROTOCOL.md) — rules and verification gates.
- [`docs/SOURCE_REGISTER.csv`](../docs/SOURCE_REGISTER.csv) — canonical register of exact editions, provenance, rights basis, and approval for reuse.
- [`docs/SEPTUAGINT_SOURCE_DECISION.md`](../docs/SEPTUAGINT_SOURCE_DECISION.md) — provisional Genesis base-text decision.
- [`notes/ot/`](../notes/ot/) — book-specific discrepancies, manuscript evidence, translation choices, and unresolved questions.
- [`translation/ot/`](../translation/ot/) — original English translation drafts.

## Required intake sequence

1. Identify the **specific historic source edition**: full bibliographic details, stable scan or repository identifier, volume, page range, book/chapter/verse boundaries, and manuscript basis where established.
2. Record the rights determination in `docs/SOURCE_REGISTER.csv`. Accept **independently verified public-domain material only**, with original project-made transcription or another demonstrably public-domain pathway. Do not request licenses or permissions, or import texts with uncertain reuse rights.
3. Transcribe and verify Greek against the actual historical pages; retain accents, breathings, meaningful punctuation, and book/verse conventions. Do not assume OCR or a modern electronic transcription is accurate or free to reuse.
4. Record file-to-page/verse mapping, transcription date/reviewer, edition/version identifier, and a reproducible checksum in the book's source metadata when the first text file is created. Flag uncertain characters instead of guessing.
5. Log independently substantiated substantive variations in `notes/` and link mandatory explanatory footnotes to affected passages as required by the translation protocol.
6. Only then import source text; never mark a source, translation, or theological interpretation as Church-approved based merely on a repository commit.

The titles and names of historical editions may be recorded **here for exact provenance**, without copying protected modern editorial content or introducing unnecessary publisher/brand names in reader-facing Scripture notes.

**This directory is a source library, not a distribution of modern third-party scholarly editions.**
