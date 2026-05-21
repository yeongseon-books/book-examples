"""Generated from book-content article."""

import subprocess
import tempfile
from pathlib import Path


def execute_python_safely(code: str, timeout: float = 5.0) -> dict:
    """Execute Python code in an isolated environment."""
    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = Path(tmpdir) / "script.py"
        script_path.write_text(code)
        try:
            result = subprocess.run(
                ["python3", str(script_path)],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=tmpdir,  # Isolated working directory
                env={"PATH": "/usr/bin:/bin"},  # Minimal env
            )
            return {
                "stdout": result.stdout[:10_000],  # Cap output size
                "stderr": result.stderr[:10_000],
                "exit_code": result.returncode,
            }
        except subprocess.TimeoutExpired:
            raise ToolError(
                code=ErrorCode.UPSTREAM_TIMEOUT,
                what="code execution exceeded timeout",
                why=f"Execution did not complete in {timeout}s.",
                how="Reduce the work done in code, or split into multiple calls.",
                retryable=False,
            )
