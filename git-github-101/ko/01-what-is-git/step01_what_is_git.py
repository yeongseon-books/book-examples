"""Git Github 101 - 1편: what is git 예제."""

from __future__ import annotations

from common import cleanup_dir, make_temp_repo, run_git


def run() -> dict[str, str]:
    """Run."""
    repo = make_temp_repo()
    try:
        version = run_git(repo, "--version").stdout.strip()
        branch = run_git(repo, "branch", "--show-current").stdout.strip()
        return {"version": version, "default_branch": branch}
    finally:
        cleanup_dir(repo)
