from pathlib import Path

from en.ep06_versioning import branch_state_machine, changelog_parser, semver_bump


def test_ep06_versioning_and_branch_machine():
    assert semver_bump("1.2.3", "minor") == "1.3.0"
    text = Path("fixtures/ep06_changelog.md").read_text(encoding="utf-8")
    assert changelog_parser(text) == {"feat": 1, "fix": 1}
    assert branch_state_machine(["feature_start", "open_pr", "merge"]) == "main"
