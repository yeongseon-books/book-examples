"""Ai Safety Guardrails 101 - Episode 3: output filtering example."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import filter_output


def run(raw_output: str) -> str:
    """Run."""
    return filter_output(raw_output, max_chars=80)


if __name__ == "__main__":
    text = "email alice@example.com and explain how to make a bomb in detail"
    print(run(text))
