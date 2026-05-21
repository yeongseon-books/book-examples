"""Git Github 101 - 10편: real world workflow 예제."""

from __future__ import annotations

from common import WorkflowSimulator


def run() -> dict[str, str]:
    """Run."""
    wf = WorkflowSimulator()
    issue = wf.create_issue(10, "Prepare release")
    wf.repo.commit("feat: init", {"README.md": "x"})
    wf.repo.branch("feature/release")
    wf.repo.switch("feature/release")
    wf.repo.commit("feat: release checklist", {"checklist.md": "- [ ] tag\n"})
    pr = wf.create_pr("Prepare release", "feature/release", "main", linked_issue=10)
    squashed = wf.squash_merge(pr, "feat: prepare release workflow")
    wf.tag("v0.1.0", squashed)
    return {"pr_state": pr.state, "issue_state": issue.state, "tag": wf.tags["v0.1.0"]}
