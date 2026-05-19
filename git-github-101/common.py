"""Shared utilities and domain models for Git Github 101."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@test",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@test",
    "GIT_TERMINAL_PROMPT": "0",
}


def make_temp_repo() -> str:
    """Make temp repo."""
    repo = tempfile.mkdtemp(prefix="git-github-101-")
    run_git(repo, "init", "-q")
    run_git(repo, "branch", "-M", "main")
    return repo


def run_git(
    cwd: str, *args: str, check: bool = True
) -> subprocess.CompletedProcess[str]:
    """Run git."""
    env = os.environ.copy()
    env.update(GIT_ENV)
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        env=env,
        check=check,
        text=True,
        capture_output=True,
    )


def write_file(path: Path, content: str) -> None:
    """Write file."""
    path.write_text(content, encoding="utf-8")


def cleanup_dir(path: str) -> None:
    """Cleanup dir."""
    shutil.rmtree(path, ignore_errors=True)


@dataclass
class Commit:
    """Commit."""

    id: str
    message: str
    parent: str | None
    files: dict[str, str]


@dataclass
class MiniRepo:
    """Mini repo."""

    branches: dict[str, str | None] = field(default_factory=lambda: {"main": None})
    commits: dict[str, Commit] = field(default_factory=dict)
    head: str = "main"
    _seq: int = 0

    def commit(self, message: str, files: dict[str, str]) -> str:
        """Commit."""
        self._seq += 1
        cid = f"c{self._seq:03d}"
        parent = self.branches[self.head]
        self.commits[cid] = Commit(id=cid, message=message, parent=parent, files=files)
        self.branches[self.head] = cid
        return cid

    def branch(self, name: str) -> None:
        """Branch."""
        self.branches[name] = self.branches[self.head]

    def switch(self, name: str) -> None:
        """Switch."""
        if name not in self.branches:
            raise KeyError(name)
        self.head = name

    def branch_tip(self, name: str) -> str | None:
        """Branch tip."""
        return self.branches.get(name)

    def history(self, branch: str) -> list[str]:
        """History."""
        tip = self.branches[branch]
        result: list[str] = []
        while tip:
            result.append(tip)
            tip = self.commits[tip].parent
        return result

    def merge_preview(
        self, source: str, target: str, path: str, base: str, ours: str, theirs: str
    ) -> str:
        """Merge preview."""
        if ours != theirs and ours != base and theirs != base:
            return f"<<<<<<< {target}\n{ours}\n=======\n{theirs}\n>>>>>>> {source}\n"
        return theirs if ours == base else ours


@dataclass
class PullRequestModel:
    """Pull request model."""

    number: int
    title: str
    source: str
    target: str
    state: str = "open"
    reviews: list[str] = field(default_factory=list)
    linked_issues: list[int] = field(default_factory=list)

    def review(self, comment: str) -> None:
        """Review."""
        self.reviews.append(comment)

    def merge(self) -> None:
        """Merge."""
        self.state = "merged"


@dataclass
class IssueModel:
    """Issue model."""

    number: int
    title: str
    labels: list[str] = field(default_factory=list)
    assignee: str | None = None
    state: str = "open"

    def close(self) -> None:
        """Close."""
        self.state = "closed"


@dataclass
class WorkflowSimulator:
    """Workflow simulator."""

    repo: MiniRepo = field(default_factory=MiniRepo)
    prs: list[PullRequestModel] = field(default_factory=list)
    issues: dict[int, IssueModel] = field(default_factory=dict)
    tags: dict[str, str] = field(default_factory=dict)

    def create_issue(self, number: int, title: str) -> IssueModel:
        """Create issue."""
        issue = IssueModel(number=number, title=title)
        self.issues[number] = issue
        return issue

    def create_pr(
        self, title: str, source: str, target: str, linked_issue: int | None = None
    ) -> PullRequestModel:
        """Create pr."""
        pr = PullRequestModel(
            number=len(self.prs) + 1, title=title, source=source, target=target
        )
        if linked_issue is not None:
            pr.linked_issues.append(linked_issue)
        self.prs.append(pr)
        return pr

    def squash_merge(self, pr: PullRequestModel, message: str) -> str:
        """Squash merge."""
        self.repo.switch(pr.target)
        cid = self.repo.commit(message, {"squash": pr.title})
        pr.merge()
        for issue_num in pr.linked_issues:
            if issue_num in self.issues:
                self.issues[issue_num].close()
        return cid

    def tag(self, name: str, commit_id: str) -> None:
        """Tag."""
        self.tags[name] = commit_id


class CommitMessageLinter:
    """Commit message linter."""

    PATTERN = re.compile(
        r"^(feat|fix|docs|style|refactor|test|chore)(\([a-z0-9_-]+\))?: .{1,50}$"
    )

    def lint(self, message: str) -> dict[str, Any]:
        """Lint."""
        errors: list[str] = []
        if not self.PATTERN.match(message):
            errors.append("subject must follow conventional commits and <=50 chars")
        if message.strip().endswith("."):
            errors.append("subject should not end with period")
        return {"ok": len(errors) == 0, "errors": errors}
