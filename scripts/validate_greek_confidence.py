#!/usr/bin/env python3
"""Validate reproducible Genesis Greek-confidence scores and evidence-backed reviews.

The validator checks declared inputs, formulas, numeric flags and review evidence.
It cannot establish that any reviewer really read the historical source image.
Scores are editorial triage estimates, NOT calibrated probabilities of correctness.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATHS = (
    ROOT / "notes/ot/GEN/p2-1887-bracket-candidates.json",
    ROOT / "notes/ot/GEN/p3-1887-bracket-candidates.json",
)
LETTERS_PATH = ROOT / "notes/ot/GEN/001-002.letter-confidence.json"
BRACKET_METHOD = ROOT / "docs/GENESIS_BRACKET_CONFIDENCE_METHOD.md"
LETTER_METHOD = ROOT / "docs/GENESIS_LETTER_CONFIDENCE_METHOD.md"
PROTOCOL = ROOT / "docs/GREEK_SOURCE_VERIFICATION_PROTOCOL.md"

THRESHOLD = 80
VISUAL_BASE = {"high": 80, "medium": 65, "low": 45, "unresolved": 25}
STATES = {"pending", "in_review", "blocked", "verified"}


def normalize_greek(s: str) -> str:
    """NFD -> lower -> remove marks/non-Greek -> ς becomes σ (matches protocol)."""
    decomposed = unicodedata.normalize("NFD", s).lower()
    return "".join(("σ" if ch == "ς" else ch) for ch in decomposed
                   if "α" <= ch <= "ω")


def round_half_up_to_5(value: int) -> int:
    return int((Decimal(value) / Decimal(5)).quantize(Decimal(1),
                                                    rounding=ROUND_HALF_UP)) * 5


def bracket_score(category: str, context_matches: bool,
                  crosses_verse_or_line: bool, earlier_conflict: bool) -> int:
    raw = (VISUAL_BASE[category] + (5 if context_matches else -10)
           - (5 if crosses_verse_or_line else 0)
           - (10 if earlier_conflict else 0))
    return max(20, min(90, round_half_up_to_5(raw)))


def agreement_percent(length_a: int, length_b: int, edit_distance: int) -> Decimal:
    if min(length_a, length_b) <= 0 or edit_distance < 0:
        raise ValueError("Positive letter counts and nonnegative edit distance required")
    return ((Decimal(100) * (Decimal(1) - Decimal(edit_distance) /
                             Decimal(max(length_a, length_b))))
            .quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def letter_score(comparator_available: bool, edit_distance: int | None,
                 agreement: Decimal | None, page_count: int) -> int:
    if page_count < 1:
        raise ValueError("No source page")
    if not comparator_available:
        base = 65
    elif edit_distance == 0:
        base = 85
    elif agreement is not None and agreement >= 99:
        base = 80
    elif agreement is not None and agreement >= 98:
        base = 75
    elif agreement is not None and agreement >= 95:
        base = 70
    else:
        base = 60
    return base - (5 if page_count > 1 else 0)


def working_greek_verses(root: Path = ROOT) -> tuple[dict[tuple[int, int], str],
                                                     list[str]]:
    files = (
        ("notes/ot/GEN/001.greek-working.md", 1, "plain"),
        ("notes/ot/GEN/001.greek-working-20-31.md", 1, "bold"),
        ("notes/ot/GEN/002.greek-working.md", 2, "bold"),
    )
    verses: dict[tuple[int, int], str] = {}
    errors = []
    patterns = {
        "plain": re.compile(r"^(\d{1,2})\.\s+([\u0370-\u03ff\u1f00-\u1fff].*)$", re.M),
        "bold": re.compile(r"^\*\*(\d{1,2})\.\*\*\s+([\u0370-\u03ff\u1f00-\u1fff].*)$", re.M),
    }
    for relpath, chapter, style in files:
        path = root / relpath
        if not path.is_file():
            errors.append(f"Missing Greek working file: {relpath}")
            continue
        for match in patterns[style].finditer(path.read_text(encoding="utf-8")):
            key = chapter, int(match.group(1))
            if key in verses:
                errors.append(f"Duplicate working Greek verse: {chapter}:{key[1]}")
            else:
                verses[key] = match.group(2)
    expected = {(chapter, v) for chapter, count in ((1, 31), (2, 25))
                for v in range(1, count + 1)}
    for chapter, verse in sorted(expected - verses.keys()):
        errors.append(f"Missing working Greek verse: {chapter}:{verse}")
    for chapter, verse in sorted(verses.keys() - expected):
        errors.append(f"Unexpected working Greek verse: {chapter}:{verse}")
    return verses, errors


def validate_review(entry: dict, kind: str) -> list[str]:
    """Allow later independent completion; never accept bare 'verified' claims."""
    errors = []
    ident = entry.get("id", "<missing ID>")
    state = entry.get("verification_status")
    if state not in STATES:
        return [f"{ident}: invalid verification_status {state!r}"]
    certified_key = ("original_square_brackets_certified" if kind == "bracket"
                     else "independent_1887_character_certified")
    certified = entry.get(certified_key)
    if state != "verified":
        if certified is not False:
            errors.append(f"{ident}: {certified_key} must be false unless verified")
        if kind == "letter" and entry.get("diacritics_and_punctuation_proofread") is not False:
            errors.append(f"{ident}: premature diacritic/punctuation certification")
        if state == "blocked" and not str(entry.get("blocker") or "").strip():
            errors.append(f"{ident}: blocked status needs a specific blocker")
        if state == "in_review" and not (
            str(entry.get("review_note") or "").strip() or
            isinstance(entry.get("review_evidence"), dict)
        ):
            errors.append(f"{ident}: in_review status needs a progress/evidence note")
        return errors

    if certified is not True:
        errors.append(f"{ident}: verified requires {certified_key}=true")
    if kind == "letter" and entry.get("diacritics_and_punctuation_proofread") is not True:
        errors.append(f"{ident}: verified requires complete diacritic/punctuation check")
    evidence = entry.get("review_evidence")
    if not isinstance(evidence, dict):
        return errors + [f"{ident}: verified needs a review_evidence object"]

    required_strings = ("primary_reviewer", "secondary_reviewer",
                        "primary_review_date", "secondary_review_date",
                        "printed_page_and_line", "evidence_url",
                        "exact_printed_reading", "apparatus_disposition", "finding")
    for key in required_strings:
        v = evidence.get(key)
        if not isinstance(v, str) or not v.strip():
            errors.append(f"{ident}: missing verified evidence {key}")
        elif "EXAMPLE" in v or "<placeholder>" in v:
            errors.append(f"{ident}: placeholder evidence {key}")
    first = evidence.get("primary_reviewer")
    second = evidence.get("secondary_reviewer")
    if isinstance(first, str) and isinstance(second, str) and first.strip() == second.strip():
        errors.append(f"{ident}: independent reviewers must be distinct")
    if evidence.get("independent_second_pass") is not True:
        errors.append(f"{ident}: independent_second_pass must be true")
    for key in ("primary_review_date", "secondary_review_date"):
        value = evidence.get(key)
        if isinstance(value, str):
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    raise ValueError("Invalid ISO date")
                date.fromisoformat(value)
            except ValueError:
                errors.append(f"{ident}: {key} must be a real YYYY-MM-DD date")
    urls = evidence.get("original_image_urls")
    if not isinstance(urls, list) or not urls or any(
        not isinstance(u, str) or not u.startswith("https://") for u in urls
    ):
        errors.append(f"{ident}: supply actual HTTPS original-image URLs")
    link = evidence.get("evidence_url")
    if not isinstance(link, str) or not link.startswith("https://github.com/"):
        errors.append(f"{ident}: evidence_url must refer to a real GitHub record")
    history = entry.get("review_history")
    if not isinstance(history, list) or not history:
        errors.append(f"{ident}: verified needs append-only review_history")
    else:
        event = history[-1]
        keys = ("date", "issue_or_pr", "previous_reading", "proposed_reading",
                "previous_confidence_percent", "new_confidence_percent",
                "reason", "reviewer")
        if not isinstance(event, dict):
            errors.append(f"{ident}: review_history entry must be an object")
        else:
            for key in keys:
                if key not in event or event[key] is None or event[key] == "":
                    errors.append(f"{ident}: review_history missing {key}")
            if event.get("new_confidence_percent") != entry.get(
                "editorial_confidence_percent" if kind == "bracket"
                else "editorial_letter_confidence_percent"
            ):
                errors.append(f"{ident}: review_history new score doesn't match entry")
    return errors


def check_flags(entry: dict, kind: str) -> list[str]:
    errors = []
    ident = entry.get("id", "<missing ID>")
    score_key = ("editorial_confidence_percent" if kind == "bracket"
                 else "editorial_letter_confidence_percent")
    score = entry.get(score_key)
    if type(score) is not int or not 0 <= score <= 100:
        return [f"{ident}: invalid integer {score_key}"]
    flagged = score < THRESHOLD
    queue = ("deferred_rigorous_verification" if flagged else
             "routine_source_proofing" if kind == "bracket" else
             "routine_1887_photo_proofing")
    if entry.get("requires_rigorous_verification_later") is not flagged:
        errors.append(f"{ident}: <80 flag inconsistent with calculated score")
    if entry.get("verification_queue") != queue:
        errors.append(f"{ident}: verification_queue inconsistent with score")
    if not str(entry.get("confidence_reasoning") or "").strip():
        errors.append(f"{ident}: missing human-readable score rationale")
    errors += validate_review(entry, kind)
    return errors


def check_bracket(entry: dict, greek: dict[tuple[int, int], str]) -> list[str]:
    errors = check_flags(entry, "bracket")
    ident = entry.get("id", "<missing ID>")
    category = entry.get("confidence")
    inp = entry.get("confidence_input")
    if category not in VISUAL_BASE or not isinstance(inp, dict):
        return errors + [f"{ident}: missing/invalid visual category or inputs"]
    try:
        first = int(entry["verse"].split(":")[0])
        number = int(re.search(r":(\d+)", entry["verse"]).group(1))
        crossing = "–" in entry["verse"]
        verse = greek[(first, number)]
        if crossing:
            verse += " " + greek[(first, number + 1)]
        snippet = normalize_greek(
            entry["before"] + entry["supplied_candidate"] + entry["after"]
        )
        context_match = bool(snippet) and snippet in normalize_greek(verse)
    except (KeyError, ValueError, TypeError, AttributeError) as exc:
        return errors + [f"{ident}: source context unavailable: {exc}"]

    wrap = inp.get("verse_or_print_line_wrap")
    conflict = inp.get("earlier_conflicting_candidate")
    if type(wrap) is not bool or type(conflict) is not bool:
        return errors + [f"{ident}: wrap/conflict flags must be booleans"]
    if crossing and not wrap:
        errors.append(f"{ident}: crossing verse boundary requires wrap penalty")
    formula = {
        "visual_category": category,
        "base_points": VISUAL_BASE[category],
        "local_working_greek_context_matches": context_match,
        "context_adjustment": 5 if context_match else -10,
        "verse_or_print_line_wrap": wrap,
        "wrap_adjustment": -5 if wrap else 0,
        "earlier_conflicting_candidate": conflict,
        "conflict_adjustment": -10 if conflict else 0,
        "score_cap_percent": 90,
    }
    for key, computed in formula.items():
        if inp.get(key) != computed:
            errors.append(f"{ident}: confidence_input.{key} expected {computed!r}, got {inp.get(key)!r}")
    computed = bracket_score(category, context_match, wrap, conflict)
    if computed != entry.get("editorial_confidence_percent"):
        errors.append(f"{ident}: bracket score expected {computed} (saved {entry.get('editorial_confidence_percent')})")
    return errors


def check_letter(entry: dict, greek: dict[tuple[int, int], str]) -> list[str]:
    errors = check_flags(entry, "letter")
    ident = entry.get("id", "<missing ID>")
    try:
        current = greek[(entry["chapter"], entry["verse"])]
        pages = entry["printed_pages"]
        if not isinstance(pages, list) or not pages or any(type(p) is not int or p < 1 for p in pages):
            return errors + [f"{ident}: invalid printed_pages"]
        page_penalty = 5 if len(pages) > 1 else 0
        if entry.get("page_boundary_penalty_percent") != page_penalty:
            errors.append(f"{ident}: incorrect printed-page penalty")
        working_count = len(normalize_greek(current))
        if working_count != entry.get("working_greek_base_letter_count"):
            errors.append(f"{ident}: working Greek text changed; expected {working_count} base letters")
        available = entry.get("diagnostic_comparator_available")
        if type(available) is not bool:
            return errors + [f"{ident}: comparator availability must be boolean"]
        if available:
            a = entry["working_greek_base_letter_count"]
            b = entry["comparator_base_letter_count"]
            d = entry["base_letter_levenshtein_distance"]
            if any(type(v) is not int for v in (a, b, d)):
                return errors + [f"{ident}: letter counts/distance must be integers"]
            agree = agreement_percent(a, b, d)
            if agree != Decimal(str(entry.get("base_letter_agreement_percent"))):
                errors.append(f"{ident}: percent agreement not reproducible")
        else:
            agree = None
            d = None
            if entry.get("comparator_base_letter_count") is not None or entry.get("base_letter_levenshtein_distance") is not None:
                errors.append(f"{ident}: unavailable comparator cannot have invented match data")
            if entry.get("base_letter_agreement_percent") is not None:
                errors.append(f"{ident}: unavailable comparator cannot have agreement percent")
        computed = letter_score(available, d, agree, len(pages))
        if entry.get("editorial_letter_confidence_percent") != computed:
            errors.append(f"{ident}: letter score should be {computed}")
    except (KeyError, ValueError, TypeError, ArithmeticError) as exc:
        errors.append(f"{ident}: unable to validate letter score: {exc}")
    return errors


def main() -> int:
    errors = []
    for path in (BRACKET_METHOD, LETTER_METHOD, PROTOCOL):
        if not path.is_file():
            errors.append(f"Missing scoring/protocol document: {path.name}")
    greek, extraction_errors = working_greek_verses()
    errors.extend(extraction_errors)

    all_ids: set[str] = set()
    brackets = []
    for path in REGISTER_PATHS:
        if not path.is_file():
            errors.append(f"Missing bracket register: {path.name}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("review_rule", {}).get("threshold_percent") != THRESHOLD:
            errors.append(f"{path.name}: incorrect threshold metadata")
        entries = data.get("entries", [])
        for e in entries:
            if e.get("id") in all_ids:
                errors.append(f"Duplicate bracket ID: {e.get('id')}")
            all_ids.add(e.get("id"))
            errors.extend(check_bracket(e, greek))
        recorded = data.get("review_counts", {})
        nflag = sum(e.get("editorial_confidence_percent", 100) < THRESHOLD for e in entries)
        if (recorded.get("flagged_below_80") != nflag or
                recorded.get("not_flagged_at_or_above_80") != len(entries) - nflag):
            errors.append(f"{path.name}: stale review_counts")
        brackets.extend(entries)
    if not LETTERS_PATH.is_file():
        errors.append("Missing letter register")
        letter_entries = []
    else:
        data = json.loads(LETTERS_PATH.read_text(encoding="utf-8"))
        letter_entries = data.get("entries", [])
        expected = {f"GEN-{ch:03}-{v:03}" for ch, count in ((1, 31), (2, 25))
                    for v in range(1, count + 1)}
        actual = [e.get("id") for e in letter_entries]
        if len(actual) != len(expected) or set(actual) != expected:
            errors.append("Letter register missing/duplicated/out-of-scope Genesis verses")
        for e in letter_entries:
            errors.extend(check_letter(e, greek))
        flagged = sum(e.get("editorial_letter_confidence_percent", 100) < THRESHOLD for e in letter_entries)
        counts = data.get("counts", {})
        expected_counts = {
            "total": len(letter_entries),
            "flagged_below_80": flagged,
            "not_flagged_at_or_above_80": len(letter_entries) - flagged,
            "exact_base_letter_matches": sum(e.get("base_letter_levenshtein_distance") == 0 for e in letter_entries),
            "comparator_unavailable": sum(not e.get("diagnostic_comparator_available") for e in letter_entries),
        }
        for key, value in expected_counts.items():
            if counts.get(key) != value:
                errors.append(f"Letter register counts.{key} should be {value}")
    flagged_brackets = sum(e.get("editorial_confidence_percent", 100) < THRESHOLD for e in brackets)
    flagged_letters = sum(e.get("editorial_letter_confidence_percent", 100) < THRESHOLD for e in letter_entries)
    active_brackets = sum(e.get("editorial_confidence_percent", 100) < THRESHOLD and e.get("verification_status") != "verified" for e in brackets)
    active_letters = sum(e.get("editorial_letter_confidence_percent", 100) < THRESHOLD and e.get("verification_status") != "verified" for e in letter_entries)
    print(f"Bracket scores: {len(brackets)}; below 80: {flagged_brackets}; active: {active_brackets}.")
    print(f"Greek verse scores: {len(letter_entries)}; below 80: {flagged_letters}; active: {active_letters}.")
    print("Confidence scoring and review consistency: " + ("PASS" if not errors else "FAIL"))
    for err in errors:
        print("ERROR: " + err, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
