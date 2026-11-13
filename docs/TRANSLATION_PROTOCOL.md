# Translation protocol — provisional v0.3

**Scope:** Establish a repeatable, documented process for drafting an English Bible translation informed by the Eastern Orthodox tradition. First source tradition: Greek Septuagint; first pilot: **Genesis chapter 1**. The New Testament follows the Orthodox Old Testament in the initial drafting sequence.

## Nonnegotiable boundaries

1. **Free and accessible.** Original translated text will remain freely available, and the intended open license permits commercial reuse with attribution, subject to final legal review.
2. **Independent and not Church-approved.** Do not describe translations as sponsored, authorized, or approved by an Orthodox Church or jurisdiction. Qualified individual reviews are not institutional endorsement.
3. **No outside collaborators during the initial full-Bible drafting phase.** The founder coordinates internal AI-assisted production through completion of a **provisional draft of the entire intended Orthodox canon**. Outside translators, technical maintainers, and language/Orthodox reviewers are invited afterward. Public repository visibility is not a solicitation for immediate contributions.
4. **AI is never an authority.** AI drafts and AI cross-checks are provisional evidence, not independent scholarly or pastoral approval.
5. **Rights and provenance first, with no permission-seeking.** The project will not seek or negotiate licenses or permissions from third parties for source texts. Use independently verified public-domain source material and original project-created content; reject third-party editions, digital transcriptions, notes, translations, or other materials whose copying or redistribution depends on permission, a restrictive license, or uncertain rights. Document provenance and the public-domain basis before import. Our eventual license for *our own original work* is a separate question.
6. **Do not claim approval until it exists.** No chapter is labeled approved until the human linguistic, Orthodox, editorial, and rights gates are complete.

7. **Mandatory explanation of substantive differences.** Whenever a material difference in Greek witnesses, source wording, Orthodox textual usage, book order, verse numbering, or rendering is identified, preserve a separate decision record and attach a clear footnote or explanatory note to the affected passage. Never silently harmonize or invent a difference.

## Phase A — Establish sources and book inventory

- Enumerate the planned Orthodox Old Testament books, additions, and order, and record unresolved jurisdictional variations as explicit editorial decisions.
- Identify a specific Greek Septuagint edition for Genesis, including editor, publication details, provenance, stable reference, textual conventions, and the legal basis for its use. Do not import copyrighted apparatus, introductions, annotations, or digital editions without rights.
- Document any base-text variants, orthography choices, verse numbering, book names, and how the New Testament edition will later be chosen.
- Register every imported source in \`docs/SOURCE_REGISTER.csv\`; do not mark rights reviewed until independently verified as public domain or original project-created material. Do not request third-party permission or accept source terms that require a special license.
- Establish terminology and proper-name glossaries; choose the traditional-versus-modern English register only after comparison samples, not by default.

## Mandatory discrepancy footnotes and neutral source language

**Trigger:** A substantive discrepancy is detected between independently usable ancient witnesses or between our working base and a documented Orthodox textual tradition. This includes meaningful wording differences, omitted or added passages, names, numbering, sequence, canon placement, and Greek version traditions (for example, alternative forms of a biblical book). Pure punctuation or spelling changes without interpretive impact may be logged without a published footnote.

**Workflow for every qualifying passage:**
1. Open a numbered entry in the book's separate notes workspace, with book/chapter/verse, kind of difference, exact independently verifiable public-domain witness references, and date.
2. Describe the readings in original, plain language. Identify what is known, what is uncertain, whether the difference affects meaning, and why a rendering was chosen or left provisional.
3. Attach a concise, neutral footnote or explanation to the relevant verse or book section, with a stable note ID linking to the detailed record. Do not claim that a Church has officially endorsed a particular reading.
4. Run an independent internal check that every flagged substantive discrepancy has its matching reader-facing note. Preserve unresolved entries for later qualified human review.
5. Export corresponding explanations in print footnotes, ebook-linked notes, and accessible notes accompanying audio (spoken selectively when necessary for comprehension).

## Mandatory documentation when discrepancy flags are resolved

**Rule:** Every flagged textual or source-history discrepancy must have a traceable outcome in the **relevant source document**—for example, `docs/SWETE_SOURCE_BACKGROUND.md` for flags about Swete's Greek text. A decision recorded only in a chapter's research log, a Git commit, or an English footnote **is not sufficient**. If no source document exists for the relevant edition or witness, create one within `docs/` and link it from the source workspace before closing the flag. Keep the detailed evidence in the affected book's separate `notes/` workspace; do not replace it with the high-level source record.

**For each flag, follow these steps:**

1. **Keep a stable flag ID** from discovery through resolution. Identify the source edition/witness, affected book and passage(s), what differs or is uncertain, and link the original flag and book-specific research entry.
2. **Investigate with independently verified, rights-safe evidence.** Record exact historical references (edition, volume, page, manuscript witness and verse where possible), relevant Greek readings, alternative interpretations, and any independently supported Orthodox textual-use considerations. Distinguish a demonstrated difference from an unverified report.
3. **Record the outcome in the relevant source document** under that flag ID: the adopted text or editorial treatment, reasons for the decision, alternatives considered, significance for the English translation, and any remaining uncertainty. If the evidence does not justify a choice, explicitly record **unresolved** and the research still needed; never manufacture a solution.
4. **Cross-link the records:** source document ↔ book research log ↔ affected chapter/verse and reader-facing explanatory footnote, where one is required. A source-wide decision must be linked from every affected book or passage. Do not let resolved decisions disappear into commit history.
5. **Record accountability:** decision date, person or team responsible, current state (**open**, **provisional decision**, **verified decision / pending qualified human review**, or **reviewed and approved** only after the applicable formal gates), and the version/commit establishing the decision. An internal or AI-assisted decision is not Orthodox Church approval.
6. **Revisit transparently:** when new evidence changes a decision, update the same flag in the source document with the superseding conclusion, rationale, date, and links; preserve the previous outcome in history rather than silently overwriting its implications.

**Closure gate:** A flag may be marked resolved for the **provisional draft** only after its source document and book log agree, its evidence and rationale are recorded, and any substantive reader-facing footnote/explainer is present or explicitly queued where the corresponding text has not yet been drafted. This does **not** make the passage publication-approved; later qualified human review and release gates still apply. Publication must not omit a required footnote.

**Rights and naming:** Do not copy a restricted edition's apparatus, modern translation, explanatory wording, proprietary content, or protected transcription. Do not mention proprietary publishing products or brands in ordinary reader-facing notes; use generic descriptions such as “another ancient Greek witness” when sufficient. Maintain precise bibliographic references **internally**, using verifiable public-domain manuscripts/editions, because omission of provenance would make a discrepancy impossible to audit. Historical source identification is factual documentation, not approval, sponsorship, or license dependence.

**Evidence gate:** If a supposed difference cannot be substantiated independently from rights-safe material, record it as unverified, do not state it as fact or publish a misleading comparison, and leave the verse flagged for later review. A lack of reusable evidence cannot be fixed by stripping attribution or paraphrasing protected analysis.

## Phase B — Genesis 1 pilot

1. **Fix the input**: exact source edition, Genesis 1 boundaries, chapter/verse identification, rights status, provenance, and a source-version identifier.
2. **Analyze the Greek**: segment units, identify morphology/syntax, flag possible textual variants, idioms, technical terms, and theological stakes; link notes to precise references.
3. **Draft original English**: produce a fresh English rendering of each verse. Avoid copying or lightly rewording protected published translations.
4. **Independent internal audit**: compare Greek and draft verse by verse for omissions, additions, changed referents, negation, tense/aspect, genre, and consistency. Use a separate pass or tool and keep an issue log. This remains an AI-assisted internal check, not qualified human review.
5. **Revise, footnote, and log**: preserve alternatives, reasons for decisions, confidence/uncertainty, terminology choices, and unresolved questions; insert reader-facing notes for each verified substantive discrepancy. Never silently resolve disputed readings.
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
- Use the same approved text/version in all channels. Preserve attribution, independence disclaimer, and all mandatory discrepancy explanations in the format appropriate to print, ebook, and accessible audio.
- Produce narrated versions from approved text; prototype audio internally if useful but never mislabel it as reviewed Scripture.
- Follow \`docs/PUBLISHING_DISTRIBUTION.md\` for paid Audible, free YouTube, possible Spotify, print formats, and publisher restrictions.

## Chapter record minimum

Each draft should include: book ID, book title, chapter number, language, status, precise source edition and reference, rights status, ordered verses, stable discrepancy-footnote IDs and separate evidence/log entries, translation notes/variants, terminology decisions, AI-assistance disclosure, version or revision, outstanding review questions, and eventual named human sign-offs.

## Decisions not yet made

- Exact independently usable public-domain Septuagint source and provenance; planned Orthodox canon and book order.
- English register (traditional/liturgical versus modern-readable).
- Precise versioning, citation, glossary, and manuscript-variant rules.
- Greek New Testament source edition for later phases.
- Qualified reviewers and formal text-release authorization, **after** the complete provisional draft.
