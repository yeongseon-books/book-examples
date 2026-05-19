from pathlib import Path

from en.ep04_review import diff_stat_analyzer, review_checklist_score


def test_ep04_diff_stat_and_score():
    diff = Path("fixtures/ep04_diff.patch").read_text(encoding="utf-8")
    stat = diff_stat_analyzer(diff)
    assert stat["a.py"]["additions"] == 2
    assert stat["b.py"]["deletions"] == 1
    assert review_checklist_score({"tests": True, "docs": False}) == 50.0
