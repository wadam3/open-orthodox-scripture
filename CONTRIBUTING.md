# Contributing — current project stage

Thank you for your interest in Open Orthodox Scripture, the Scripture workstream of the proposed **Open Orthodox Library** initiative.

## When outside contributions begin

**Not yet:** The project's chosen process is to complete a **full provisional AI-assisted translation of the entire intended Orthodox Bible** before recruiting external translators, technical collaborators, and qualified human language/Orthodox reviewers. The repository is public for transparent planning, but early publication does **not** mean the translation is ready for community edits or review.

After the full provisional draft has been assembled, contribution opportunities will be opened for language review, Orthodox theological review, technical maintenance, accessibility, corrections, audio, documentation, and publishing.

Contributors do **not** need to share every future publishing ambition; technical maintainers do not have to be Orthodox. Qualified Orthodox theological sign-off is a distinct editorial role, not granted by GitHub access or popularity.

## Flagged Greek verification — when contributor review opens

The [canonical Greek source-verification protocol](docs/GREEK_SOURCE_VERIFICATION_PROTOCOL.md) now includes **exact, repeatable scoring formulas** for Greek letters and editorial brackets, a **strict <80% deferred-rigorous-verification flag**, and evidence requirements for independent verification. The [contributor verification workflow](docs/CONTRIBUTOR_GREEK_VERIFICATION_WORKFLOW.md) tells future reviewers how to select item IDs, examine the original historical photographs, recalculate scores, submit corrections, and preserve review history. Use the [Greek verification issue template](.github/ISSUE_TEMPLATE/greek_verification.md) and [pull-request template](.github/PULL_REQUEST_TEMPLATE.md) once external contributions are opened.

Scores measure **editorial triage confidence, not statistical probabilities or approval**. A reviewer must not improve a score solely to remove a flag. An item may be individually verified only with two distinct documented direct-image readings and a defensible apparatus record. Historical flags and change history must remain auditable, even after a source reading is independently verified. An individually verified item does **not** make a chapter Church-approved.

**Current Genesis baseline:** 34 of 41 bracket candidates and 7 of 56 letter-level verse candidates are below 80%; the rest still require routine checking. The validator and fixed tests are in the repository, but the real outside review program is postponed until the provisional Bible draft as described above.

## Future contribution rules

1. Work on a documented issue in a topic branch and use the pull-request template.
2. Supply precise source edition, provenance, and rights for any text, audio, image, voice, or other material; avoid copying copyright-protected English translations.
3. Document substantive linguistic choices, textual variants, names, theological terminology, and any AI assistance.
4. Keep work attributed to consenting contributors; do not expose another person's identity without permission.
5. Do not promote an AI draft, merged PR, or unreviewed chapter to ecclesiastically approved Scripture.
6. Respect the independent project disclaimer and agree to documented licensing and contributor terms when formally adopted.

## License and credit (proposed)

Original eligible text and audio contributions are proposed to use **CC BY 4.0**, and original code **MIT**. Those licenses permit commercial reuse (with CC BY attribution obligations) but do not cover third-party copyright-protected sources. The precise contributor grant and attribution process will be ratified before substantive outside contributions.

See [Translation protocol](docs/TRANSLATION_PROTOCOL.md) and [Roadmap](docs/ROADMAP.md).
