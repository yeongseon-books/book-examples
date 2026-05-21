"""Ai Safety Guardrails 101 - 1편: why ai safety matters 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


def run(user_input: str) -> dict[str, str | bool]:
    """Run."""
    if len(user_input) > 500:
        return {"allowed": False, "reason": "too_long"}
    return {"allowed": True, "reason": "baseline_pass"}


if __name__ == "__main__":
    print(run("안전한 질문입니다."))
