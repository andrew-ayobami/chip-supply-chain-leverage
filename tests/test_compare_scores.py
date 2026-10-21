"""Tests for src/compare_scores.py, using the made-up sheets in tests/fixtures/ only."""
import math
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import compare_scores as cs

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_pairs():
    a = cs.load_sheet(FIXTURES / "cases_andrew.csv", "case_id")
    b = cs.load_sheet(FIXTURES / "cases_ayodele.csv", "case_id")
    return cs.pair_scores(a, b, ["case"])


def hand_linear_kappa(x, y, k=3):
    """Weighted kappa written out from the formula, to check the sklearn-based version."""
    observed = np.zeros((k, k))
    for i, j in zip(x, y):
        observed[i, j] += 1
    observed /= observed.sum()
    expected = np.outer(observed.sum(axis=1), observed.sum(axis=0))
    weights = np.abs(np.subtract.outer(np.arange(k), np.arange(k)))  # 0, 1 or 2 levels apart
    return 1 - (weights * observed).sum() / (weights * expected).sum()


def test_counts_on_made_up_sheets():
    pairs, unscored = load_pairs()
    s = cs.agreement_stats(pairs)
    assert unscored == 1  # T3 state_control left blank by Andrew
    assert (s["n"], s["exact"], s["one_apart"], s["two_apart"]) == (17, 14, 2, 1)


def test_kappa_matches_hand_formula():
    pairs, _ = load_pairs()
    s = cs.agreement_stats(pairs)
    expected = hand_linear_kappa(pairs["andrew"], pairs["ayodele"])
    assert s["kappa"] == pytest.approx(expected)
    assert 0 < s["kappa"] < 1


def test_perfect_agreement_gives_kappa_one():
    x = pd.Series([0, 1, 2, 2, 1, 0])
    assert cs.weighted_kappa(x, x) == pytest.approx(1.0)


def test_kappa_undefined_when_everyone_uses_one_level():
    x = pd.Series([1, 1, 1])
    k = cs.weighted_kappa(x, x)
    assert math.isnan(k)
    assert "can't be worked out" in cs.kappa_sentence(k)


def test_kappa_sentence_bands():
    assert '"moderate"' in cs.kappa_sentence(0.55)
    assert '"almost perfect"' in cs.kappa_sentence(1.0)
    assert "no better than chance" in cs.kappa_sentence(-0.1)


def test_disagreement_list_is_complete_and_ordered():
    pairs, _ = load_pairs()
    d = cs.disagreements(pairs)
    assert len(d) == 3
    first = d.iloc[0]
    assert (first["id"], first["variable"], first["andrew"], first["ayodele"], first["levels_apart"]) == \
           ("T2", "cohesion", "low", "high", 2)
    assert set(zip(d["id"], d["variable"])) == {("T2", "cohesion"), ("T2", "substitutability"),
                                                ("T3", "time_to_replace")}


def test_scores_are_case_and_space_insensitive(tmp_path):
    text = (FIXTURES / "cases_andrew.csv").read_text().replace("T1,Made-up case A,low", "T1,Made-up case A, LOW ")
    path = tmp_path / "cases_andrew.csv"
    path.write_text(text)
    assert cs.load_sheet(path, "case_id").at["T1", "concentration"] == "low"


def test_invalid_score_is_rejected(tmp_path):
    text = (FIXTURES / "cases_andrew.csv").read_text().replace("T1,Made-up case A,low", "T1,Made-up case A,hi")
    path = tmp_path / "cases_andrew.csv"
    path.write_text(text)
    with pytest.raises(ValueError, match="allowed: low, medium, high"):
        cs.load_sheet(path, "case_id")


def test_mismatched_rows_are_rejected(tmp_path):
    lines = (FIXTURES / "cases_ayodele.csv").read_text().splitlines()
    path = tmp_path / "cases_ayodele.csv"
    path.write_text("\n".join(lines[:-1]) + "\n")  # drop T3
    a = cs.load_sheet(FIXTURES / "cases_andrew.csv", "case_id")
    b = cs.load_sheet(path, "case_id")
    with pytest.raises(ValueError, match="different rows"):
        cs.pair_scores(a, b, ["case"])


def test_full_report(tmp_path):
    for name in ("cases_andrew.csv", "cases_ayodele.csv"):
        (tmp_path / name).write_text((FIXTURES / name).read_text())
    text, dis = cs.report("cases", tmp_path)
    assert "**Exact agreement:** 14 of 17 (82%)" in text
    assert "Disagreements to settle (3)" in text
    assert len(dis) == 3
