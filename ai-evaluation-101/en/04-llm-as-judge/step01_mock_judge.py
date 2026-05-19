"""Ai Evaluation 101 - Episode 1: Mock judge."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLMJudge


def run() -> dict[str, str]:
    """Run."""
    judge = MockLLMJudge()
    prompt = "Explain why RAG is useful"
    answer_a = "RAG reduces hallucination because it uses retrieved evidence."
    answer_b = "It is a good method!"
    winner = judge.score_pair(prompt, answer_a, answer_b)
    return {"winner": winner}


if __name__ == "__main__":
    print(run())
