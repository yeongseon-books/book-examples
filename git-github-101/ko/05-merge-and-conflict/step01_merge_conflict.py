"""Git Github 101 - 5편: merge and conflict 예제."""

from __future__ import annotations

from common import MiniRepo


def run() -> dict[str, str]:
    """Run."""
    repo = MiniRepo()
    repo.commit("feat: base", {"notes.md": "line1\n"})
    repo.branch("feature/a")
    repo.switch("feature/a")
    repo.commit("feat: a", {"notes.md": "line1\nA\n"})
    repo.switch("main")
    repo.branch("feature/b")
    repo.switch("feature/b")
    repo.commit("feat: b", {"notes.md": "line1\nB\n"})
    conflict = repo.merge_preview(
        "feature/a", "feature/b", "notes.md", "line1\n", "line1\nB\n", "line1\nA\n"
    )
    return {"conflict": conflict}
