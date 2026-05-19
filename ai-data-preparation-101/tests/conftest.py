from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_dict(relative_path: str) -> dict[str, object]:
    output = subprocess.check_output(
        [sys.executable, str(ROOT / relative_path)], text=True
    ).strip()
    data = ast.literal_eval(output)
    if not isinstance(data, dict):
        raise RuntimeError(f"expected dict output: {relative_path}")
    return data
