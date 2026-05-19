from common import (
    validate_pr_description,
)
from en.ep04_pr_validator import run_example as run_en
from ko.ep04_pr_validator import run_example as run_ko


def test_ep04_behavior():
    assert run_ko() == []
    bad = "## Summary\nNo issue ref\n- [x] one"
    assert "missing_closes" in validate_pr_description(bad)
    assert run_en() == []
