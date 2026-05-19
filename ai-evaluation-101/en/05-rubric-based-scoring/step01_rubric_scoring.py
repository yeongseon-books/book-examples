"""Ai Evaluation 101 - Episode 1: Rubric scoring."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLMJudge


def run() -> dict[str, object]:
    """Run."""
    judge = MockLLMJudge()
    answer = "Because RAG grounds generation on retrieved evidence, hallucination risk is reduced for factual tasks."
    scores = judge.rubric_score("Explain RAG", answer)
    verdict = (
        "PASS" if scores["correctness"] >= 4 and min(scores.values()) >= 3 else "REVIEW"
    )
    return {"scores": scores, "verdict": verdict}


if __name__ == "__main__":
    print(run())
