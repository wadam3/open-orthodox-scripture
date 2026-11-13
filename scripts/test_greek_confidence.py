#!/usr/bin/env python3
"""Deterministic, source-free tests for the Genesis confidence rubric.

All review objects in these tests are synthetic fixtures, not real reviewer
attestations, manuscript judgments or completed reviews.
"""
from __future__ import annotations

import copy
import unittest
from decimal import Decimal

import validate_greek_confidence as qa


class ConfidenceFormulaTests(unittest.TestCase):
    def test_greek_normalization(self):
        self.assertEqual(qa.normalize_greek("Καὶ [ὁ] λόγος, ἐστί."), "καιολογοσεστι")
        self.assertEqual(qa.normalize_greek("Σ ς σ"), "σσσ")

    def test_rounding_and_bounds(self):
        self.assertEqual(qa.round_half_up_to_5(32), 30)
        self.assertEqual(qa.round_half_up_to_5(33), 35)
        self.assertEqual(qa.bracket_score("unresolved", False, True, True), 20)
        self.assertEqual(qa.bracket_score("high", True, False, False), 85)
        self.assertEqual(qa.bracket_score("high", True, False, True), 75)
        self.assertEqual(qa.bracket_score("low", True, True, True), 35)

    def test_agreement_is_round_half_up(self):
        self.assertEqual(qa.agreement_percent(95, 96, 2), Decimal("97.92"))
        self.assertEqual(qa.agreement_percent(96, 96, 0), Decimal("100.00"))
        with self.assertRaises(ValueError):
            qa.agreement_percent(0, 96, 0)

    def test_letter_score_exact_threshold(self):
        self.assertEqual(qa.letter_score(True, 0, Decimal("100.00"), 1), 85)
        self.assertEqual(qa.letter_score(True, 0, Decimal("100.00"), 2), 80)
        self.assertEqual(qa.letter_score(True, 1, Decimal("99.00"), 1), 80)
        self.assertEqual(qa.letter_score(True, 1, Decimal("98.99"), 1), 75)
        self.assertEqual(qa.letter_score(True, 2, Decimal("97.92"), 1), 70)
        self.assertEqual(qa.letter_score(False, None, None, 1), 65)
        self.assertEqual(qa.letter_score(False, None, None, 2), 60)

    def test_strict_below_80_flag_not_less_than_or_equal(self):
        for score, expected in ((79, True), (80, False), (85, False)):
            with self.subTest(score=score):
                obj = {
                    "id": "FIXTURE",
                    "editorial_confidence_percent": score,
                    "requires_rigorous_verification_later": expected,
                    "verification_queue": (
                        "deferred_rigorous_verification" if expected
                        else "routine_source_proofing"
                    ),
                    "confidence_reasoning": "Synthetic fixture",
                    "verification_status": "pending",
                    "original_square_brackets_certified": False,
                }
                self.assertEqual(qa.check_flags(obj, "bracket"), [])
                modified = copy.deepcopy(obj)
                modified["requires_rigorous_verification_later"] = not expected
                self.assertTrue(qa.check_flags(modified, "bracket"))

    def test_recompute_bracket_from_real_greek_context_not_saved_boolean(self):
        good = {
            "id": "FIXTURE-BRACKET",
            "verse": "1:1",
            "before": "καὶ ",
            "supplied_candidate": "ἔστι",
            "after": " ὁ θεός",
            "confidence": "high",
            "editorial_confidence_percent": 85,
            "requires_rigorous_verification_later": False,
            "verification_queue": "routine_source_proofing",
            "verification_status": "pending",
            "original_square_brackets_certified": False,
            "confidence_reasoning": "Synthetic fixture",
            "confidence_input": {
                "visual_category": "high",
                "base_points": 80,
                "local_working_greek_context_matches": True,
                "context_adjustment": 5,
                "verse_or_print_line_wrap": False,
                "wrap_adjustment": 0,
                "earlier_conflicting_candidate": False,
                "conflict_adjustment": 0,
                "score_cap_percent": 90,
            },
        }
        greek = {(1, 1): "καὶ ἔστι ὁ θεός."}
        self.assertEqual(qa.check_bracket(good, greek), [])
        changed = copy.deepcopy(good)
        changed["supplied_candidate"] = "λέγει"
        self.assertTrue(qa.check_bracket(changed, greek))

    def test_verified_without_independent_evidence_is_rejected(self):
        obj = {
            "id": "FIXTURE",
            "verification_status": "verified",
            "original_square_brackets_certified": True,
        }
        self.assertTrue(qa.validate_review(obj, "bracket"))

    def test_evidence_complete_synthetic_fixture_can_be_item_verified(self):
        obj = {
            "id": "FIXTURE",
            "editorial_confidence_percent": 75,
            "verification_status": "verified",
            "original_square_brackets_certified": True,
            "review_evidence": {
                "primary_reviewer": "fixture_reviewer_one",
                "secondary_reviewer": "fixture_reviewer_two",
                "primary_review_date": "2026-01-01",
                "secondary_review_date": "2026-01-02",
                "independent_second_pass": True,
                "original_image_urls": ["https://example.org/fixture-image"],
                "printed_page_and_line": "fixture p. 1 line 2",
                "evidence_url": "https://github.com/example/repo/pull/42",
                "exact_printed_reading": "αβγ",
                "apparatus_disposition": "Synthetic fixture",
                "finding": "Synthetic fixture only; not an actual review",
            },
            "review_history": [{
                "date": "2026-01-02",
                "issue_or_pr": "https://github.com/example/repo/pull/42",
                "previous_reading": "αβ",
                "proposed_reading": "αβγ",
                "previous_confidence_percent": 60,
                "new_confidence_percent": 75,
                "reason": "Synthetic fixture only",
                "reviewer": "fixture_reviewer_two",
            }],
        }
        self.assertEqual(qa.validate_review(obj, "bracket"), [])
        bad = copy.deepcopy(obj)
        bad["review_evidence"]["secondary_reviewer"] = "fixture_reviewer_one"
        self.assertTrue(qa.validate_review(bad, "bracket"))
        letter = copy.deepcopy(obj)
        del letter["original_square_brackets_certified"]
        letter["independent_1887_character_certified"] = True
        letter["diacritics_and_punctuation_proofread"] = False
        self.assertTrue(qa.validate_review(letter, "letter"))
        letter["diacritics_and_punctuation_proofread"] = True
        self.assertEqual(qa.validate_review(letter, "letter"), [])


if __name__ == "__main__":
    unittest.main()
