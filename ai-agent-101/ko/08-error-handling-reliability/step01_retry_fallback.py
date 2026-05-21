"""Ai Agent 101 - 8편: error handling reliability 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import retry


def unstable(counter: dict[str, int]) -> str:
    """Unstable."""
    counter["n"] += 1
    if counter["n"] < 2:
        raise TimeoutError("temporary timeout")
    return "primary-success"


def run() -> dict[str, str]:
    """Run."""
    c = {"n": 0}
    try:
        result = retry(lambda: unstable(c), max_attempts=3)
        return {"path": "retry", "result": str(result)}
    except Exception:
        return {"path": "fallback", "result": "cached-response"}


if __name__ == "__main__":
    print(run())
