from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(relative_path: str) -> str:
    out = subprocess.check_output(["python3", str(ROOT / relative_path)], text=True)
    return out.strip()
