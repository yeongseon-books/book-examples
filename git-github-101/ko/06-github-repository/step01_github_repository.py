"""Git Github 101 - 6편: github repository 예제."""

from __future__ import annotations

from common import MiniRepo


def run() -> dict[str, object]:
    """Run."""
    repo = MiniRepo()
    repo.commit("feat: init", {"README.md": "x"})
    remotes = {"origin": "https://example.invalid/demo.git"}
    upstream = "origin/main"
    return {
        "remote": remotes["origin"],
        "upstream": upstream,
        "history": repo.history("main"),
    }
