"""Linux Cli 101 - Episode 1: Files dirs."""

from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    """Run."""
    ws = make_temp_workspace("ep02-")
    run_cmd(ws, "mkdir", "-p", "src/utils")
    run_cmd(ws, "touch", "hello.txt")
    run_cmd(ws, "cp", "hello.txt", "src/copy.txt")
    ls = run_cmd(ws, "ls", "src")
    return {"code": ls.returncode, "stdout": ls.stdout}
