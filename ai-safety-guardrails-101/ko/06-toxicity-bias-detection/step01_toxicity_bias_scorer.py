"""Ai Safety Guardrails 101 - 6편: toxicity bias detection 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import toxicity_bias_score


def run(text: str) -> dict[str, int]:
    """Run."""
    return toxicity_bias_score(text)


if __name__ == "__main__":
    print(run("You are stupid and women can't code."))
