"""Git Github 101 - 2편: first commit 예제."""

from __future__ import annotations

from pathlib import Path

from common import cleanup_dir, make_temp_repo, run_git, write_file


def run() -> dict[str, str]:
    """Run."""
    repo = make_temp_repo()
    try:
        write_file(Path(repo) / "README.md", "# First commit\n")
        run_git(repo, "add", "README.md")
        run_git(repo, "commit", "-m", "feat: add readme")
        head = run_git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
        return {"head": head}
    finally:
        cleanup_dir(repo)
