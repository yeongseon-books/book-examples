from pathlib import Path

from ko.ep09_debt import debt_scorer, prioritization_matrix


def test_ep09_debt_and_matrix():
    code = Path("fixtures/ep09_code.txt").read_text(encoding="utf-8")
    debt = debt_scorer(code)
    assert debt["debt_score"] == 5
    assert prioritization_matrix(8, 3) == "quick-win"
