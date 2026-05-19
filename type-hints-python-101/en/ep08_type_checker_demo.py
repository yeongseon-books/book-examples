"""Type Hints Python 101 - Episode 8: Type checker demo."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

_INTENTIONAL_ERRORS = {
    "wrong_add": 'add("1", 2)',
    "wrong_assign": "name: str = 123",
}


def run_mypy_if_available() -> dict[str, str | int]:
    """Run mypy if available."""
    mypy_path = shutil.which("mypy")
    if not mypy_path:
        return {"status": "skipped", "reason": "mypy not installed"}
    snippet = "\n".join(
        [
            "def add(a: int, b: int) -> int:",
            "    return a + b",
            "x: str = 1",
            'add("1", 2)',
        ]
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        p = Path(tmpdir) / "sample.py"
        p.write_text(snippet, encoding="utf-8")
        proc = subprocess.run(
            [mypy_path, "--no-error-summary", str(p)],
            capture_output=True,
            text=True,
            check=False,
        )
    return {
        "status": "ran",
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }
