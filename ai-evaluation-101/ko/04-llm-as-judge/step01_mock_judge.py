"""Ai Evaluation 101 - Episode 1: Mock judge."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLMJudge


def run() -> dict[str, str]:
    """Run."""
    judge = MockLLMJudge()
    prompt = "RAG가 왜 필요한지 설명해 주세요"
    answer_a = "RAG는 검색 근거를 붙여 hallucination을 줄입니다."
    answer_b = "좋은 기술입니다!"
    winner = judge.score_pair(prompt, answer_a, answer_b)
    return {"winner": winner}


if __name__ == "__main__":
    print(run())
