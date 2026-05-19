from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.judge import evaluate_generation
from ko.shared import GENERATION_CASE


def main() -> None:
    print("Groq 기반 LLM-as-judge 데모")
    result = evaluate_generation(
        question=GENERATION_CASE.question,
        context=GENERATION_CASE.context,
        answer=GENERATION_CASE.answer,
        language="ko",
    )
    print(json.dumps({name: score.__dict__ for name, score in result.items()}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
