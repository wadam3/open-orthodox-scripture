# Chapter production time log

**Purpose:** Keep comparable chapter-level production benchmarks for the provisional Septuagint translation. Distinguish **initial translation drafting** from later source research, Greek transcription, editorial rechecks, pronunciation work, audiobook production, and external reviews. Do not infer actual hands-on labor hours from GitHub commit timestamps alone.

**Time zone:** America/New_York (EST, UTC-05:00 on November 12, 2026).
**Source of timestamp evidence:** GitHub repository commits. Commit-to-commit elapsed time is a wall-clock interval, not a stopwatch of active work.

## Genesis 1 — 31 English verses

| Milestone | Local time (November 12, 2026) | Evidence |
| --- | --- | --- |
| First 1:1–5 provisional translation saved | 8:53:39 p.m. EST | [Commit `30575418`](https://github.com/wadam3/open-orthodox-scripture/commit/30575418ab934f2d23c52c78ba3575489ef7758d) |
| Initial complete 31-verse English translation saved | 9:11:19 p.m. EST | [Commit `b69f4880`](https://github.com/wadam3/open-orthodox-scripture/commit/b69f48807d041aeb320b7cac0f872841c0bd3e2f) |
| Initial manuscript/English audit committed | 9:23:47 p.m. EST | [Commit `299126b4`](https://github.com/wadam3/open-orthodox-scripture/commit/299126b46de3365c7a3202f1af59d77242814d82) |
| First governing-Greek translation correction in 1:14 committed | 9:33:28 p.m. EST | [Commit `9ee3ac49`](https://github.com/wadam3/open-orthodox-scripture/commit/9ee3ac492d7a750c2f28c0f3dfb4e3630109f5d3) |

- **Measured GitHub elapsed time, first partial-verse commit to complete 31-verse draft: 17 minutes 40 seconds.** This is **not the entire kickoff-to-draft time** because work occurred before the first partial commit.
- **Earlier conversational planning estimate:** approximately **36 minutes from actual kickoff to all 31 English verses drafted**, with about **22 minutes of focused verse writing**. The kickoff and focused-writing start were **not established with a verifiable stopwatch in the Git history**; preserve these as **retrospective estimates**, not measured durations.
- **Earlier conversational total estimate:** approximately **1 hour 23 minutes** from beginning work through provisional chapter plus some corrections/research notes. This is a **broader, unverified estimate** that includes more than the initial translation and must not be used as a pure drafting benchmark.
- Later exhaustive 1887 scan proofing and independent human/Orthodox review are **not included** as completed initial translation work.

## Genesis 2 — 25 English verses

| Milestone | Local time (November 12, 2026) | Evidence |
| --- | --- | --- |
| Last preceding Genesis 1 research-note commit (possible before chapter 2 kickoff; **not a chapter 2 start marker**) | 10:05:07 p.m. EST | [Commit `7028ec04`](https://github.com/wadam3/open-orthodox-scripture/commit/7028ec04) |
| First complete 25-verse English draft saved | 10:13:12 p.m. EST | [Commit `4b5e60fa`](https://github.com/wadam3/open-orthodox-scripture/commit/4b5e60fa2c491801abb1f2171a8482fb3a8450bb) |
| First English verse-1 correction saved | 10:14:11 p.m. EST | [Commit `c45116c0`](https://github.com/wadam3/open-orthodox-scripture/commit/c45116c0f5b8a0c11410c6e260f053638f5c96cb) |
| First full text-only narration script saved | 10:14:52 p.m. EST | [Commit `28a35cca`](https://github.com/wadam3/open-orthodox-scripture/commit/28a35cca8e02bb84a3ff0c38faec3a33e15a411b) |
| Later original-Greek-driven English corrections saved | 10:18:07 p.m. and 10:19:14 p.m. EST | [2:19 commit `4e58a08e`](https://github.com/wadam3/open-orthodox-scripture/commit/4e58a08e150bc66a5e90b140c1c08c274565f323), [2:9 commit `ab4d31f7`](https://github.com/wadam3/open-orthodox-scripture/commit/ab4d31f75d5992a54d1d530b8cf04346f4b0126f) |
| Text-only narration synchronized with those corrections | 10:19:26 p.m. EST | [Commit `1d958e90`](https://github.com/wadam3/open-orthodox-scripture/commit/1d958e90d0ce8f9d038a46d17bef43093d635901) |
| Complete 25-verse **working Greek**, a separate research stage | 10:25:06 p.m. EST | [Commit `e9a5c617`](https://github.com/wadam3/open-orthodox-scripture/commit/e9a5c617) |

- **Exact Genesis 2 start time: not established.** The first complete English draft was committed at 10:13:12 p.m. EST. No first-partial-draft commit provides an equivalent Genesis 2 start marker.
- **Observed interval between preceding Genesis 1 note and Genesis 2 full English draft: 8 minutes 5 seconds**. This is an **upper-bound reference window after the preceding commit, not a verified Chapter 2 drafting duration**. Work may have started before or after that note; do not classify this as actual labor time.
- **Elapsed time from Genesis 2's first complete English draft to all initial Greek-driven English corrections and synchronized narration: 6 minutes 14 seconds.** This is an **observable revision window after** the initial translation, not initial drafting time.
- **Broader observed interval from the previous chapter's final research note to corrected Genesis 2 narration: 14 minutes 19 seconds**, but it is a *mixed context/workflow interval*, **not a verified translation time**.
- **Time for strictly initial translation:** **unknown (not stopwatch-logged)**. Use the observed timestamps above only as a planning reference. The later source verification and editorial bracket work remain separate.

## Reusable tracking procedure for Genesis 3 onward

To get reliable future benchmarks, capture at least these event timestamps directly when they occur, using ISO 8601 with offset and an explicit task label: `start_initial_translation`, `first_complete_english_draft`, `initial_translation_review_finished`, `narration_script_synchronized`, `source_verification_started`, and `source_verification_finished`. Log **active time** separately from elapsed wall-clock time and pauses if measuring labor cost. Link the actual commits and record who supplied any manual timestamp.

Use **drafting duration = first_complete_english_draft - start_initial_translation** only when **both timestamps were actually captured**. Otherwise report `not measured`; do not backfill an exact start based on a later commit. Track corrections, Greek source proofing, human reviews and audio recording as separate time categories. The provisional chapter's completion is not publication certification.
