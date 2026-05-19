"""Git Github 101 - Episode 1: Issue project."""

from __future__ import annotations

from common import WorkflowSimulator


def run() -> dict[str, str]:
    """Run."""
    wf = WorkflowSimulator()
    issue = wf.create_issue(1, "Add packing list")
    issue.labels.append("enhancement")
    issue.assignee = "alice"
    wf.repo.commit("feat: init", {"README.md": "x"})
    wf.repo.branch("feature/packing-list")
    pr = wf.create_pr(
        "Add packing list", "feature/packing-list", "main", linked_issue=1
    )
    wf.squash_merge(pr, "feat: add packing list")
    return {"issue_state": issue.state, "assignee": issue.assignee or ""}
