"""Tests for ep10 in Sre 101."""

from en.ep10_operable_checklist import checklist_score


def test_ep10_operable_score():
    """Test ep10 operable score."""
    passed, score = checklist_score(
        {
            "logs": True,
            "metrics": True,
            "traces": True,
            "runbook": True,
            "dashboards": False,
            "alerts": True,
        }
    )
    assert passed == 5
    assert round(score, 3) == 0.833
