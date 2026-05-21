"""Linux Cli 101 - 5편: grep find xargs 예제."""

from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    """Run."""
    ws = make_temp_workspace("ep05-")
    (ws / "a.txt").write_text("TODO one\n", encoding="utf-8")
    (ws / "b.txt").write_text("done\n", encoding="utf-8")
    grep = run_cmd(ws, "grep", "-n", "TODO", "a.txt")
    return {"code": grep.returncode, "stdout": grep.stdout}
