#!/usr/bin/env python3
"""Reproducible *mechanical* QA for Genesis 1 and 2, not Greek philological approval.

This checks files and drafts only. It deliberately does not certify the
photographic 1887 Greek, manuscript bracket locations, theological decisions,
rights clearance, or the existence/quality of a spoken audio recording.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS = (
    (1, 31, "one", ("001.greek-working.md", "001.greek-working-20-31.md")),
    (2, 25, "two", ("002.greek-working.md",)),
)
HASH_MANIFEST = ROOT / "docs" / "GENESIS_1_2_CONTENT_HASHES.json"


def normalized(text: str) -> str:
    return " ".join(text.split())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def greek_verse_numbers(text: str) -> list[int]:
    """Match both working-note styles without reading explanatory numbered lists."""
    # Match only a verse number followed directly by a Greek letter, so numbered
    # English research instructions ("1. Copy ...") are never miscounted as verses.
    greek = r"[\u0370-\u03ff\u1f00-\u1fff]"
    plain = re.findall(rf"(?m)^(\d{{1,2}})\.[ \t]+(?={greek})", text)
    bold = re.findall(rf"(?m)^\*\*(\d{{1,2}})\.\*\*[ \t]+(?={greek})", text)
    return [int(x) for x in plain + bold]


def verify() -> tuple[list[str], dict]:
    issues: list[str] = []
    checks: list[dict] = []
    sha: dict[str, str] = {}
    for chapter, expected, title, greek_files in SPECS:
        tag = f"{chapter:03}"
        path = ROOT / f"translation/ot/GEN/{tag}.json"
        audio = ROOT / f"audio/scripts/GEN/{tag}.narration.txt"
        filenames = (path, audio) + tuple(ROOT / f"notes/ot/GEN/{name}" for name in greek_files)
        for file in filenames:
            if not file.is_file():
                issues.append(f"Genesis {chapter}: missing {file.relative_to(ROOT)}")
        if not all(p.is_file() for p in filenames):
            continue
        for file in filenames:
            sha[str(file.relative_to(ROOT))] = sha256(file)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            issues.append(f"Genesis {chapter}: invalid JSON: {exc}")
            continue
        verses = data.get("verses", [])
        if data.get("book_id") != "GEN" or data.get("chapter") != chapter:
            issues.append(f"Genesis {chapter}: book/chapter metadata mismatch")
        if len(verses) != expected:
            issues.append(f"Genesis {chapter}: {len(verses)} English verses; expected {expected}")
        if any(not isinstance(v, dict) or v.get("verse") != n or not isinstance(v.get("text"), str) or not v["text"].strip()
               for n, v in enumerate(verses, start=1)):
            issues.append(f"Genesis {chapter}: English verse numbers/text invalid")
        else:
            expected_script = normalized(" ".join(v["text"] for v in verses))
            script = audio.read_text(encoding="utf-8")
            header = f"Genesis. Chapter {title}."
            if not script.startswith(header):
                issues.append(f"Genesis {chapter}: narration chapter heading mismatch")
            spoken = normalized(script.removeprefix(header))
            if spoken != expected_script:
                issues.append(f"Genesis {chapter}: narration differs from original verse text")
        source = data.get("source", {})
        if source.get("source_register_id") != "SWETE-1887-V1":
            issues.append(f"Genesis {chapter}: edition provenance not pinned to Swete 1887")
        if not source.get("printed_page_images"):
            issues.append(f"Genesis {chapter}: missing original-image references")
        if data.get("status") == "approved" and (source.get("transcription_verified") is not True
                                                   or source.get("rights_reviewed") is not True):
            issues.append(f"Genesis {chapter}: unauthorized approved status")
        if source.get("transcription_verified") is True and not (ROOT / f"sources/ot/greek/GEN/{tag}.txt").exists():
            issues.append(f"Genesis {chapter}: source flagged verified but no approved Greek source file exists")
        notes = data.get("reader_notes", [])
        ids = [item.get("id") for item in notes if isinstance(item, dict)]
        if len(ids) != len(set(ids)) or any(not isinstance(v, str) or not v for v in ids):
            issues.append(f"Genesis {chapter}: reader note IDs are not unique/nonempty")
        for item in notes:
            if not isinstance(item, dict):
                issues.append(f"Genesis {chapter}: malformed reader note")
                continue
            refs = ([item["verse"]] if "verse" in item else item.get("verses", []))
            if any(not isinstance(v, int) or v < 1 or v > expected for v in refs):
                issues.append(f"Genesis {chapter}: note {item.get('id')} has out-of-range verse")
        found = []
        for file in filenames[2:]:
            found.extend(greek_verse_numbers(file.read_text(encoding="utf-8")))
        if len(found) != expected or sorted(found) != list(range(1, expected + 1)):
            issues.append(f"Genesis {chapter}: Greek working-verse numbering missing/duplicated: {found}")
        if chapter == 2 and len(verses) == 25:
            if not all("also" in verses[v-1]["text"].lower() for v in (9, 19)):
                issues.append("Genesis 2: previously verified 'also' in verses 9 and 19 missing")
            if "sixth day" not in verses[1]["text"].lower():
                issues.append("Genesis 2: 1887 sixth-day completion reading missing from English")
        checks.append({
            "chapter": chapter,
            "english_verses": len(verses),
            "greek_working_verses": len(found),
            "narration_exact_text_match": normalized(
                audio.read_text(encoding="utf-8").removeprefix(f"Genesis. Chapter {title}.")
            ) == normalized(" ".join(v.get("text", "") for v in verses if isinstance(v, dict))),
            "note_count": len(notes),
            "edition": source.get("source_register_id"),
            "greek_diplomatic_verified": source.get("transcription_verified", False),
            "rights_reviewed": source.get("rights_reviewed", False),
            "status": data.get("status"),
        })
    return issues, {"scope": "mechanical QA only, NOT independent scholarly Greek check",
                    "chapters": checks, "sha256_of_exact_committed_content": dict(sorted(sha.items()))}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-manifest", action="store_true",
                        help="Check committed file hashes, detecting drift after corrections")
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    args = parser.parse_args()
    issues, report = verify()
    if args.verify_manifest:
        if not HASH_MANIFEST.is_file():
            issues.append("Missing docs/GENESIS_1_2_CONTENT_HASHES.json")
        else:
            manifest = json.loads(HASH_MANIFEST.read_text(encoding="utf-8"))
            expected = manifest.get("sha256_of_exact_committed_content", {})
            actual = report["sha256_of_exact_committed_content"]
            for path in sorted(set(expected) | set(actual)):
                if expected.get(path) != actual.get(path):
                    issues.append(f"SHA-256 drift: {path}")
    if args.json:
        print(json.dumps({"ok": not issues, "issues": issues, **report}, ensure_ascii=False, indent=2))
    else:
        for record in report["chapters"]:
            print(f"Genesis {record['chapter']}: {record['english_verses']} English,"
                  f" {record['greek_working_verses']} Greek working verses;"
                  f" narration exact={record['narration_exact_text_match']};"
                  f" diplomatic Greek verified={record['greek_diplomatic_verified']}")
        print("Mechanical QA " + ("PASS" if not issues else "FAIL"))
        for issue in issues:
            print("ERROR: " + issue, file=sys.stderr)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
