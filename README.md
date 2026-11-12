# Orthodox Scripture Project

**Working title.** A community-led effort to create an openly licensed English Bible translation informed by the Eastern Orthodox tradition, together with accessible audiobook editions.

> **Independent project:** This project is not affiliated with, sponsored by, or officially approved by any Orthodox Church, jurisdiction, diocese, or publisher. The word *Orthodox* describes the editorial orientation, not institutional endorsement.

## Why this exists

We want Scripture to be readable, listenable, carefully sourced, and freely reusable. Translation decisions should be transparent and open to review, without pretending that machine checks or a large number of GitHub contributors establish theological authority.

## Scope and sequence

1. **Launch:** Settle editorial governance, source-text rights, and contributor policies.
2. **Pilot:** Produce and review an original translation of Mark chapter 1 from a vetted Greek source text.
3. **New Testament:** Expand book by book with documented language and Orthodox theological review.
4. **Audio:** Produce reproducible narrated editions of approved text with pronunciation, accessibility, and listening quality checks.
5. **Old Testament:** Plan a Septuagint-oriented edition after the source edition, book order/canon, and rights are reviewed with qualified Orthodox advisors.

The Old Testament is intentionally deferred, not excluded. The exact canon and source editions remain open editorial decisions.

## Ways to contribute

You do **not** need to share every long-term publishing or audio goal to help maintain the repository. Technical maintainers, translators, Greek-language experts, proofreaders, accessibility reviewers, and audio engineers can contribute independently. Scripture approval requires a distinct editorial and Orthodox-review process; it is not decided by popularity or merge rights alone.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and the [roadmap](docs/ROADMAP.md).

## Project layout

- `translation/` - human-readable structured chapter drafts and review metadata
- `docs/` - editorial policy, source register, decisions, roadmap, and audio plan
- `audio/` - audiobook conventions (generated audio is not yet part of the repository)
- `scripts/` - local, dependency-free consistency checks
- `.github/` - issue and pull-request templates

## Development check

Run `python3 scripts/validate_chapters.py` locally. It validates chapter structure, not the accuracy or Orthodox suitability of any translation.

## Licensing

The initial licensing proposal is **CC BY 4.0** for original translation, documentation, and original audio, and **MIT** for software. See [LICENSE.md](LICENSE.md) for the proposed application and third-party restrictions. The owner and future contributors should confirm the licensing policy before substantive text/audio contributions begin.

## Project status

**Bootstrap / planning.** No Scripture translation or audio recordings have been published in this repository. No source text has been approved for import.