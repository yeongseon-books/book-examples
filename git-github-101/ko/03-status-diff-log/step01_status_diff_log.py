"""Git Github 101 - Episode 1: Status diff log."""

from __future__ import annotations

from pathlib import Path

from common import cleanup_dir, make_temp_repo, run_git, write_file


def run() -> dict[str, str]:
    """Run."""
    repo = make_temp_repo()
    try:
        write_file(Path(repo) / "notes.md", "hello\n")
        run_git(repo, "add", "notes.md")
        run_git(repo, "commit", "-m", "feat: add notes")
        write_file(Path(repo) / "notes.md", "hello\nworld\n")
        status = run_git(repo, "status", "-s").stdout.strip()
        diff = run_git(repo, "diff").stdout
        log = run_git(repo, "log", "--oneline", "-1").stdout.strip()
        return {"status": status, "diff": diff, "log": log}
    finally:
        cleanup_dir(repo)
