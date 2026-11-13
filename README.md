# Open Orthodox Scripture

**Open Orthodox Library** is the proposed umbrella identity. **An experiment in open-source Orthodox publishing** describes our approach to production and distribution, not an experiment in doctrine.

## Mission

To make the Holy Scriptures and Orthodox Christian literature freely accessible to everyone through faithful translation, open collaboration, and unrestricted distribution.

## How This Project Started

As an Orthodox Christian, I wanted a simple way to choose an individual book of the Bible and listen to it during long drives.

I searched the Bible-reading and audiobook apps I used, checked my favorite podcast app, and looked for a well-organized channel on the streaming services I used. I couldn't find the listening experience I was looking for.

That personal need inspired **Open Orthodox Library**: an independent experiment to make Scripture easier for everyone to access, with free text and audio, and print editions as well.

The project was inspired by my personal experience. It is not affiliated with, endorsed by, or approved by any Orthodox Church.

## Independence and ecclesiastical-status disclaimer

> Open Orthodox Library is an independent publishing initiative. It is not affiliated with, sponsored by, endorsed by, or officially approved by the Eastern Orthodox Church, any Orthodox jurisdiction, diocese, or ecclesiastical authority.
>
> The term *Orthodox* describes the project's theological and editorial orientation and does not imply official Church recognition or approval.
>
> Translations are independently produced and should not be represented as officially authorized Orthodox biblical texts.

This disclaimer applies to this repository and should accompany future print, digital, and audio publications. Individual expert review does not itself confer institutional Church approval.

## What we are building

- An original, Greek-source-based English translation oriented toward Eastern Orthodox tradition, starting with **Genesis chapter 1 from the Septuagint**.
- A complete provisional Bible translation produced **before** recruiting outside collaborators; AI assistance and internal verification are documented, but are not theological approval.
- Subsequent language, Orthodox theological, and editorial human review before any claim of reviewed publication.
- Free text and ebook access, print editions, and audiobook releases: individual books, separate Testaments, and an entire Bible when format/platform limits permit.
- Free individual-book audio on YouTube; free Spotify distribution is being explored. Audible editions are intended to be paid. The same narration is used across platforms unless a premium version offers genuinely meaningful improvements.
- A public, traceable, openly reusable project after adoption of suitable licenses. Commercial reuse with attribution is part of the mission.

## First steps and sequence

1. Verify source editions and rights. The **Greek Septuagint** is the starting textual tradition; the exact Genesis edition and Orthodox book order remain to be selected.
2. Define and test the [translation protocol](docs/TRANSLATION_PROTOCOL.md) against Genesis 1.
3. Draft every chapter in a consistent, versioned format, logging AI use, textual uncertainties, and corrections. Drafts must be clearly marked *provisional*.
4. After the complete provisional translation exists, invite qualified outside Greek-language and Orthodox reviewers and other contributors.
5. Release only material that has passed the relevant rights, linguistic, editorial, and Orthodox review gates. Prepare print, ebook, and audio formats per the [publishing strategy](docs/PUBLISHING_DISTRIBUTION.md).

## Project documents

- [Translation protocol](docs/TRANSLATION_PROTOCOL.md)
- [Why Swete? Source origin and rationale](docs/SWETE_SOURCE_BACKGROUND.md)
- [Source-text workspace and intake plan](sources/README.md)
- [Publishing and distribution strategy](docs/PUBLISHING_DISTRIBUTION.md)
- [Roadmap](docs/ROADMAP.md)
- [Decision register](docs/DECISIONS.md)
- [Editorial policy](docs/EDITORIAL_POLICY.md)
- [Audio production plan](docs/AUDIO_PLAN.md)
- [Proposed licensing](LICENSE.md)
- [Contribution policy and timing](CONTRIBUTING.md)

## License and status

The working proposal is **CC BY 4.0** for original text, original notes, and original audio, and **MIT** for original software. Contributor and third-party rights still need final review before substantive reuse or public releases. Creative Commons BY permits third-party commercial editions with appropriate attribution; it does not grant rights to outside copyrighted works.

**Status: foundation and provisional translation planning.** No Greek source edition has yet been approved for import, no Scripture chapter is approved for publication, and no Church authorization is claimed. The former Mark 1 starter remains a deferred planning placeholder, not the active first pilot.

Structural consistency check: \`python3 scripts/validate_chapters.py\`.
