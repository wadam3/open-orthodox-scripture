#!/usr/bin/env python3
"""Validate structured chapter consistency, not theological or language accuracy."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSLATION_DIR = ROOT / "translation"
STATUSES = {"planning", "draft", "editorial-review", "orthodox-review", "approved"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        chapter = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return [f"{path}: cannot read JSON: {exc}"]

    def err(message: str) -> None:
        errors.append(f"{path.relative_to(ROOT)}: {message}")

    for field in ("book_id", "book_title", "language"):
        if not isinstance(chapter.get(field), str) or not chapter[field].strip():
            err(f"missing nonempty {field}")
    if type(chapter.get("chapter")) is not int or chapter["chapter"] < 1:
        err("chapter must be a positive integer")

    status = chapter.get("status")
    if status not in STATUSES:
        err(f"invalid status {status!r}")
    source = chapter.get("source")
    if not isinstance(source, dict):
        err("source must be an object")
        source = {}
    review = chapter.get("review")
    if not isinstance(review, dict):
        err("review must be an object")
        review = {}

    verses = chapter.get("verses")
    if not isinstance(verses, list):
        err("verses must be an array")
        return errors

    if status != "planning" and not verses:
        err("non-planning chapters must include verses")

    for expected_number, verse in enumerate(verses, start=1):
        if not isinstance(verse, dict):
            err(f"verse {expected_number} must be an object")
            continue
        if type(verse.get("verse")) is not int or verse["verse"] != expected_number:
            err(f"verse #{expected_number} must have sequential verse number {expected_number}")
        if not isinstance(verse.get("text"), str) or not verse["text"].strip():
            err(f"verse #{expected_number} must have nonempty original text")

    if status == "approved":
        if source.get("rights_reviewed") is not True:
            err("approved chapter requires source.rights_reviewed=true")
        for field in ("edition", "reference"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                err(f"approved chapter requires source.{field}")
        for field in ("language_editor", "orthodox_reviewer"):
            if not isinstance(review.get(field), str) or not review[field].strip():
                err(f"approved chapter requires review.{field}")
    return errors


def main() -> int:
    files = sorted(TRANSLATION_DIR.rglob("*.json"))
    if not files:
        print("No translation chapters found")
        return 0
    errors = [error for path in files for error in validate(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} chapter file(s). Structural checks only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
