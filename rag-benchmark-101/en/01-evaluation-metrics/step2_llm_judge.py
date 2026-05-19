"""Rag Benchmark 101 - Episode 2: Llm judge."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.judge import evaluate_generation
from en.shared import GENERATION_CASE


def main() -> None:
    """Main."""
    print("Groq LLM-as-judge demo")
    result = evaluate_generation(
        question=GENERATION_CASE.question,
        context=GENERATION_CASE.context,
        answer=GENERATION_CASE.answer,
        language="en",
    )
    print(
        json.dumps({name: score.__dict__ for name, score in result.items()}, indent=2)
    )


if __name__ == "__main__":
    main()
