"""Tests for ep09 in Sql 101."""

from en.ep09_index_explain import run_demo


def test_ep09_index_explain_plan():
    """Test ep09 index explain plan."""
    out = run_demo()
    before_text = " ".join(str(t) for t in out["before"])
    after_text = " ".join(str(t) for t in out["after"])
    assert "USING INDEX" not in before_text.upper()
    assert "USING INDEX" in after_text.upper()
