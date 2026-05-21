"""Git Github 101 - 7편: pull request 예제."""

from __future__ import annotations

from common import WorkflowSimulator


def run() -> dict[str, str]:
    """Run."""
    wf = WorkflowSimulator()
    wf.repo.commit("feat: init", {"README.md": "x"})
    wf.repo.branch("feature/release-notes")
    wf.repo.switch("feature/release-notes")
    wf.repo.commit("feat: add release notes", {"notes.md": "release"})
    pr = wf.create_pr("Add release notes", "feature/release-notes", "main")
    pr.review("please clarify title")
    wf.squash_merge(pr, "feat: merge release notes")
    return {"state": pr.state, "reviews": str(len(pr.reviews))}
