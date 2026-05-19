from __future__ import annotations

from dataclasses import dataclass
from math import erf, sqrt
from statistics import mean, stdev


@dataclass(frozen=True)
class EvalExample:
    case_id: str
    prompt: str
    reference: str


class MockLLMJudge:
    def score_pair(self, prompt: str, answer_a: str, answer_b: str) -> str:
        a = self._score_text(prompt, answer_a)
        b = self._score_text(prompt, answer_b)
        if a == b:
            return "Tie"
        return "A" if a > b else "B"

    def rubric_score(self, prompt: str, answer: str) -> dict[str, int]:
        lowered = answer.lower()
        correctness = (
            5
            if any(word in lowered for word in ["because", "근거", "따라서", "source"])
            else 3
        )
        completeness = 5 if len(answer.split()) >= 8 else 2
        clarity = 5 if len(answer) <= 180 else 3
        tone = 5 if "!" not in answer else 3
        return {
            "correctness": correctness,
            "completeness": completeness,
            "clarity": clarity,
            "tone": tone,
        }

    def _score_text(self, prompt: str, answer: str) -> int:
        prompt_words = set(_tokens(prompt))
        overlap = len(prompt_words.intersection(_tokens(answer)))
        bonus = (
            1
            if any(
                marker in answer.lower()
                for marker in ["because", "근거", "therefore", "따라서"]
            )
            else 0
        )
        return overlap + bonus


def _tokens(text: str) -> list[str]:
    cleaned = "".join(ch.lower() if ch.isalnum() else " " for ch in text)
    return [t for t in cleaned.split() if t]


def exact_match(prediction: str, reference: str) -> int:
    return int(prediction.strip().lower() == reference.strip().lower())


def bleu1_like(prediction: str, reference: str) -> float:
    p = _tokens(prediction)
    r = _tokens(reference)
    if not p or not r:
        return 0.0
    matched = sum(1 for token in p if token in r)
    return matched / len(p)


def rouge_l_like(prediction: str, reference: str) -> float:
    p = _tokens(prediction)
    r = _tokens(reference)
    if not p or not r:
        return 0.0
    lcs = _lcs_length(p, r)
    return lcs / len(r)


def _lcs_length(a: list[str], b: list[str]) -> int:
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def precision_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    sliced = retrieved[:k]
    if not sliced:
        return 0.0
    return sum(1 for doc in sliced if doc in relevant) / len(sliced)


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    sliced = retrieved[:k]
    return sum(1 for doc in sliced if doc in relevant) / len(relevant)


def welch_t_test(sample_a: list[float], sample_b: list[float]) -> tuple[float, float]:
    if len(sample_a) < 2 or len(sample_b) < 2:
        raise ValueError("each sample must have at least two values")
    mean_a = mean(sample_a)
    mean_b = mean(sample_b)
    var_a = stdev(sample_a) ** 2
    var_b = stdev(sample_b) ** 2
    t_num = mean_a - mean_b
    t_den = sqrt(var_a / len(sample_a) + var_b / len(sample_b))
    if t_den == 0.0:
        return 0.0, 1.0
    t_value = t_num / t_den
    p_approx = 2 * (1 - _normal_cdf(abs(t_value)))
    return t_value, max(0.0, min(1.0, p_approx))


def _normal_cdf(x: float) -> float:
    return 0.5 * (1 + erf(x / sqrt(2)))
