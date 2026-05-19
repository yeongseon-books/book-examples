"""Episode 09: logging/trace/cost 추적 예제입니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import deterministic_score, now_iso


def run(request_id: str, prompt: str) -> dict[str, object]:
    """Run."""
    tokens = len(prompt.split()) * 10
    cost = round(tokens / 1000 * 0.002, 6)
    return {
        "timestamp": now_iso(),
        "request_id": request_id,
        "tokens": tokens,
        "cost_usd": cost,
        "quality_score": deterministic_score(prompt),
    }


if __name__ == "__main__":
    print(run("req-1", "monitor agent token usage"))
