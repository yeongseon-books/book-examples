from __future__ import annotations

import os

from common import EnvScope, make_temp_workspace, run_cmd


def run() -> dict[str, str]:
    ws = make_temp_workspace("ep08-")
    original = os.environ.get("DEMO_VAR", "")
    with EnvScope({"DEMO_VAR": "linux-cli-101"}):
        child = run_cmd(
            ws, "python3", "-c", "import os;print(os.getenv('DEMO_VAR',''))"
        )
        inside = child.stdout.strip()
    restored = os.environ.get("DEMO_VAR", "")
    return {"inside": inside, "restored": restored, "original": original}
