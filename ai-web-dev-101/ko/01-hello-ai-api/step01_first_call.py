"""Ai Web Dev 101 - Episode 1: First call."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import cast

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLM


def first_ai_call(user_prompt: str) -> dict[str, object]:
    """First ai call."""
    llm = MockLLM()
    response = llm.chat(
        system="너는 친절한 번역가입니다.", user=user_prompt, temperature=0.2
    )
    choices = cast("list[dict[str, object]]", response["choices"])
    message = cast("dict[str, object]", choices[0]["message"])
    usage = cast("dict[str, int]", response["usage"])
    answer = str(message["content"])
    return {
        "answer": answer,
        "total_tokens": usage["total_tokens"],
        "is_cost_trackable": usage["total_tokens"] > 0,
    }


if __name__ == "__main__":
    result = first_ai_call("AI API 개발을 시작하는 개발자에게 응원의 한마디")
    print(result)
