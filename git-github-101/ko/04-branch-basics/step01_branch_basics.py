"""Git Github 101 - 4편: branch basics 예제."""

from __future__ import annotations

from pathlib import Path

from common import cleanup_dir, make_temp_repo, run_git, write_file


def run() -> dict[str, str]:
    """Run."""
    repo = make_temp_repo()
    try:
        write_file(Path(repo) / "base.txt", "base\n")
        run_git(repo, "add", "base.txt")
        run_git(repo, "commit", "-m", "feat: base")
        run_git(repo, "switch", "-c", "feature/docs")
        write_file(Path(repo) / "feature.txt", "feature\n")
        run_git(repo, "add", "feature.txt")
        run_git(repo, "commit", "-m", "feat: feature branch")
        graph = run_git(
            repo, "log", "--oneline", "--graph", "--decorate", "--all"
        ).stdout
        return {"graph": graph}
    finally:
        cleanup_dir(repo)
