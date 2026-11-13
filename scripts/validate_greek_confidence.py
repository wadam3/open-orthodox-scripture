#!/usr/bin/env python3
"""Validate the <80% recheck queue for Genesis 1-2; never certify source Greek.

This checks saved editorial confidence flags. Scores are provisional estimates,
NOT source accuracy probabilities or substitutes for image-to-character proofing.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTERS = (
    (ROOT / "notes/ot/GEN/p2-1887-bracket-candidates.json", 20),
    (ROOT / "notes/ot/GEN/p3-1887-bracket-candidates.json", 21),
)
LETTERS = ROOT / "notes/ot/GEN/001-002.letter-confidence.json"
METHOD = ROOT / "docs/GENESIS_LETTER_CONFIDENCE_METHOD.md"


def check_entry(e: dict, kind: str) -> list[str]:
    errors = []
    ident = e.get("id", "<no-id>")
    score = e.get("editorial_confidence_percent" if kind == "bracket" else "editorial_letter_confidence_percent")
    if type(score) is not int or not (0 <= score <= 100):
        return [f"{ident}: invalid confidence score {score!r}"]
    expected_flag = score < 80
    expected_queue = ("deferred_rigorous_verification" if expected_flag
                      else ("routine_source_proofing" if kind == "bracket" else "routine_1887_photo_proofing"))
    if e.get("requires_rigorous_verification_later") is not expected_flag:
        errors.append(f"{ident}: incorrect strict-below-80 flag")
    if e.get("verification_queue") != expected_queue:
        errors.append(f"{ident}: incorrect verification queue")
    if e.get("verification_status") != "pending":
        errors.append(f"{ident}: expected pending proofing state")
    certification = "original_square_brackets_certified" if kind == "bracket" else "independent_1887_character_certified"
    if e.get(certification) is not False:
        errors.append(f"{ident}: unwarranted certified flag")
    if not e.get("confidence_reasoning"):
        errors.append(f"{ident}: missing evidence/rationale")
    if kind == "letter":
        if e.get("diacritics_and_punctuation_proofread") is not False:
            errors.append(f"{ident}: diacritics/printed punctuation not certified")
        if e.get("diagnostic_comparator_available"):
            a, b, edit = (e.get("working_greek_base_letter_count"),
                          e.get("comparator_base_letter_count"),
                          e.get("base_letter_levenshtein_distance"))
            if not all(type(x) is int for x in (a, b, edit)) or min(a, b) < 1 or edit < 0:
                errors.append(f"{ident}: missing/invalid base-letter diagnostic data")
            else:
                agreement = round(100 * (1 - edit / max(a, b)), 2)
                if abs(agreement - e.get("base_letter_agreement_percent", -100)) > 0.011:
                    errors.append(f"{ident}: letter agreement inconsistent with edit distance")
                base = (85 if edit == 0 else 80 if agreement >= 99 else
                        75 if agreement >= 98 else 70 if agreement >= 95 else 60)
                expected_score = base - e.get("page_boundary_penalty_percent", 0)
                if score != expected_score:
                    errors.append(f"{ident}: score mismatch with published rubric ({score} vs {expected_score})")
        else:
            if score != 65 - e.get("page_boundary_penalty_percent", 0):
                errors.append(f"{ident}: unavailable-comparator score differs from rubric")
    return errors


def main() -> int:
    errors: list[str] = []
    total_brackets = 0
    brackets_flagged = 0
    for path, count in REGISTERS:
        data = json.loads(path.read_text(encoding="utf-8"))
        entries = data["entries"]
        if len(entries) != count:
            errors.append(f"{path.name}: expected {count} bracket candidates, found {len(entries)}")
        ids = [e["id"] for e in entries]
        if len(set(ids)) != len(ids):
            errors.append(f"{path.name}: duplicate bracket IDs")
        for e in entries:
            errors.extend(check_entry(e, "bracket"))
            total_brackets += 1
            brackets_flagged += e.get("requires_rigorous_verification_later") is True
    data = json.loads(LETTERS.read_text(encoding="utf-8"))
    entries = data["entries"]
    if len(entries) != 56:
        errors.append(f"Letter scores: expected 56 verses, found {len(entries)}")
    expected_ids = {f"GEN-{ch:03}-{v:03}" for ch, num in ((1, 31), (2, 25))
                    for v in range(1, num + 1)}
    got_ids = [e.get("id") for e in entries]
    if set(got_ids) != expected_ids or len(set(got_ids)) != len(got_ids):
        errors.append("Letter scores: missing, duplicate or unexpected verse IDs")
    flagged = sum(e.get("requires_rigorous_verification_later") is True for e in entries)
    for e in entries:
        errors.extend(check_entry(e, "letter"))
    if (data["counts"].get("flagged_below_80") != flagged or
            data["counts"].get("not_flagged_at_or_above_80") != len(entries) - flagged):
        errors.append("Letter score summary counts inconsistent")
    if not METHOD.is_file():
        errors.append("Missing published Greek letter-confidence method")
    print(f"Greek letters: {len(entries)} verse scores; {flagged} flagged below 80%; "
          f"{len(entries)-flagged} at or above 80%.")
    print(f"1887 bracket candidates: {total_brackets}; {brackets_flagged} flagged below 80%.")
    print("These flags verify rubric consistency only, NOT Greek source accuracy.")
    for error in errors:
        print("ERROR: " + error)
    print("Confidence queue validation " + ("PASS" if not errors else "FAIL"))
    return 1 if errors else 1 if total_brackets != 41 or brackets_flagged != 34 else 0


if __name__ == "__main__":
    raise SystemExit(main())
