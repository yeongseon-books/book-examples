from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from en.common import build_logger, call_groq

logger = build_logger("en.evaluation")


@dataclass(slots=True)
class EvaluationCase:
    question: str
    answer: str
    reference: str


class LLMJudge:
    def __init__(self, model: str = "llama-3.1-8b-instant") -> None:
        self.model = model

    def evaluate(self, case: EvaluationCase) -> dict[str, Any]:
        system_prompt = "You are an evaluator for LLM answers. Score factuality, faithfulness, and clarity from 1 to 5 and explain the score in one line."
        user_prompt = (
            f"Question: {case.question}\n"
            f"Model answer: {case.answer}\n"
            f"Reference answer: {case.reference}\n"
            "Return plain text in the form score=<number>, reason=<text>."
        )
        try:
            result = call_groq(
                system_prompt=system_prompt, user_prompt=user_prompt, model=self.model
            )
            score = _extract_score(result.text)
            payload = {
                "score": score,
                "reason": result.text.strip(),
                "latency_ms": round(result.latency_ms, 1),
            }
            logger.info("LLM judge evaluation completed.", extra={"payload": payload})
            return payload
        except Exception as exc:
            logger.exception(
                "LLM judge failed; falling back to a heuristic evaluator.",
                extra={"payload": {"error": str(exc)}},
            )
            return heuristic_evaluate(case)


def _extract_score(text: str) -> int:
    for token in text.replace(",", " ").split():
        digits = "".join(ch for ch in token if ch.isdigit())
        if digits:
            value = int(digits)
            if 1 <= value <= 5:
                return value
    return 3


def heuristic_evaluate(case: EvaluationCase) -> dict[str, Any]:
    answer_words = set(case.answer.split())
    reference_words = set(case.reference.split())
    overlap = len(answer_words & reference_words)
    score = 5 if overlap >= 6 else 4 if overlap >= 4 else 3 if overlap >= 2 else 2
    reason = f"Heuristic fallback: {overlap} reference words overlap with the answer."
    return {"score": score, "reason": reason, "latency_ms": 0.0}


class BatchEvaluator:
    def __init__(self, judge: LLMJudge) -> None:
        self.judge = judge

    def run(self, cases: list[EvaluationCase]) -> dict[str, Any]:
        results = [self.judge.evaluate(case) for case in cases]
        average = (
            round(sum(item["score"] for item in results) / len(results), 2)
            if results
            else 0.0
        )
        return {"count": len(results), "average_score": average, "results": results}


def demo() -> None:
    cases = [
        EvaluationCase(
            question="Explain the incident root cause.",
            answer="A cache key collision combined with slow SQL queries caused the incident.",
            reference="The outage escalated because cache key collisions and database latency happened together.",
        ),
        EvaluationCase(
            question="Describe the mitigation.",
            answer="Split cache keys and tune the slow query path.",
            reference="Fix cache key design and optimize the slow SQL statements.",
        ),
    ]
    report = BatchEvaluator(LLMJudge()).run(cases)
    print(report)


if __name__ == "__main__":
    demo()
