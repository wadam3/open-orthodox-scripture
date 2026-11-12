# Translation protocol — provisional v0.1

**Scope:** Establish a repeatable, documented process for drafting an English Bible translation informed by the Eastern Orthodox tradition. First source tradition: Greek Septuagint; first pilot: **Genesis chapter 1**. The New Testament follows the Orthodox Old Testament in the initial drafting sequence.

## Nonnegotiable boundaries

1. **Free and accessible.** Original translated text will remain freely available, and the intended open license permits commercial reuse with attribution, subject to final legal review.
2. **Independent and not Church-approved.** Do not describe translations as sponsored, authorized, or approved by an Orthodox Church or jurisdiction. Qualified individual reviews are not institutional endorsement.
3. **No outside collaborators during the initial full-Bible drafting phase.** The founder coordinates internal AI-assisted production through completion of a **provisional draft of the entire intended Orthodox canon**. Outside translators, technical maintainers, and language/Orthodox reviewers are invited afterward. Public repository visibility is not a solicitation for immediate contributions.
4. **AI is never an authority.** AI drafts and AI cross-checks are provisional evidence, not independent scholarly or pastoral approval.
5. **Rights and provenance first.** Ancient texts are not automatically equivalent to modern editions, digitizations, apparatus, notes, or English translations. Document exact sources and permissions before importing or distributing them.
6. **Do not claim approval until it exists.** No chapter is labeled approved until the human linguistic, Orthodox, editorial, and rights gates are complete.

## Phase A — Establish sources and book inventory

- Enumerate the planned Orthodox Old Testament books, additions, and order, and record unresolved jurisdictional variations as explicit editorial decisions.
- Identify a specific Greek Septuagint edition for Genesis, including editor, publication details, provenance, stable reference, textual conventions, and the legal basis for its use. Do not import copyrighted apparatus, introductions, annotations, or digital editions without rights.
- Document any base-text variants, orthography choices, verse numbering, book names, and how the New Testament edition will later be chosen.
- Register every imported source in \`docs/SOURCE_REGISTER.csv\`; do not mark rights reviewed until verified.
- Establish terminology and proper-name glossaries; choose the traditional-versus-modern English register only after comparison samples, not by default.

## Phase B — Genesis 1 pilot

1. **Fix the input**: exact source edition, Genesis 1 boundaries, chapter/verse identification, rights status, provenance, and a source-version identifier.
2. **Analyze the Greek**: segment units, identify morphology/syntax, flag possible textual variants, idioms, technical terms, and theological stakes; link notes to precise references.
3. **Draft original English**: produce a fresh English rendering of each verse. Avoid copying or lightly rewording protected published translations.
4. **Independent internal audit**: compare Greek and draft verse by verse for omissions, additions, changed referents, negation, tense/aspect, genre, and consistency. Use a separate pass or tool and keep an issue log. This remains an AI-assisted internal check, not qualified human review.
5. **Revise and log**: preserve alternatives, reasons for decisions, confidence/uncertainty, terminology choices, and unresolved questions; never silently resolve disputed readings.
6. **Machine checks**: verify sequential verse IDs, chapter metadata, nonempty text for drafts, required fields, and consistency with glossaries. Run \`python3 scripts/validate_chapters.py\`.
7. **Mark the artifact provisional**: status stays \`draft\` or \`editorial-review\` pending later qualified review. No approved label, publication-ready claim, or Church endorsement.
8. **Retrospective**: refine the template, prompts, audit rubric, and style guide before scaling to Genesis 2.

## Phase C — Complete the provisional Bible before outside collaboration

- Process each Old Testament chapter using the same source, original draft, audit, revision, and provenance steps.
- Keep book boundaries, disputed Septuagint canon/book-order issues, and alternate readings explicitly documented. Resolve policy questions by documented decision rather than silent model output.
- After the defined Old Testament inventory is drafted, select and rights-check an appropriate Greek New Testament edition and repeat the process for each NT chapter.
- Track progress as **not started / draft / internally checked / unresolved / ready for human review**. These are project-progress labels, not theological approvals.
- Freeze and tag a reproducible **complete provisional draft** only when every planned chapter is accounted for; publish the manifest and the list of unresolved issues. The provisional milestone does **not** authorize a reviewed print or audio Bible.

## Phase D — Qualified outside review, after the complete provisional draft

- Invite independent Greek-language editors, Orthodox clergy/scholars where appropriate, English editors, and technical maintainers.
- Record reviewer qualifications and consent to public credit; do not disclose private identities without permission.
- Verify source fidelity, theology and liturgical terminology, disputed readings, readability, attribution, canon/order, and internal consistency.
- Require explicit rights sign-off, language-editor sign-off, a designated qualified Orthodox-reviewer sign-off, and release-editor confirmation **for each approved chapter**. A GitHub merge or AI consensus is not sign-off.
- Maintain open corrections, editorial decisions, revision history, and releases; do not imply reviewer participation is Church-wide approval.

## Phase E — Publications

- After the appropriate human review gates, export a fixed and reproducible text release into free ebooks/digital files, print-ready assets, and narrated audiobooks.
- Use the same approved text/version in all channels. Preserve attribution and independence disclaimer.
- Produce narrated versions from approved text; prototype audio internally if useful but never mislabel it as reviewed Scripture.
- Follow \`docs/PUBLISHING_DISTRIBUTION.md\` for paid Audible, free YouTube, possible Spotify, print formats, and publisher restrictions.

## Chapter record minimum

Each draft should include: book ID, book title, chapter number, language, status, precise source edition and reference, rights status, ordered verses, translation notes/variants, terminology decisions, AI-assistance disclosure, version or revision, outstanding review questions, and eventual named human sign-offs.

## Decisions not yet made

- Exact Septuagint edition and license/provenance; planned Orthodox canon and book order.
- English register (traditional/liturgical versus modern-readable).
- Precise versioning, citation, glossary, and manuscript-variant rules.
- Greek New Testament source edition for later phases.
- Qualified reviewers and formal text-release authorization, **after** the complete provisional draft.
