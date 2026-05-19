"""Linux Cli 101 - Episode 1: Script."""

from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    """Run."""
    ws = make_temp_workspace("ep09-")
    script = ws / "hello.sh"
    script.write_text("#!/usr/bin/env bash\necho 'hello script'\n", encoding="utf-8")
    run_cmd(ws, "chmod", "+x", "hello.sh")
    result = run_cmd(ws, "bash", "hello.sh")
    return {"code": result.returncode, "stdout": result.stdout}
