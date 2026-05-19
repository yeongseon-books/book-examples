from __future__ import annotations


def score_rubric(
    scores: dict[str, float], weak_threshold: float = 2.5
) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, score in scores.items():
        if score >= 4.0:
            result[key] = "strong"
        elif score >= weak_threshold:
            result[key] = "developing"
        else:
            result[key] = "gap"
    return result


COMPETENCIES = [
    "technical_depth",
    "cross_functional",
    "mentorship",
    "strategy",
    "impact",
]


def assess_senior_readiness(scores: dict[str, float]) -> dict[str, object]:
    normalized = {key: float(scores.get(key, 0.0)) for key in COMPETENCIES}
    rubric = score_rubric(normalized)
    gaps = [key for key, label in rubric.items() if label == "gap"]
    overall = sum(normalized.values()) / len(COMPETENCIES)
    return {
        "overall": overall,
        "rubric": rubric,
        "gaps": gaps,
        "ready": overall >= 3.8 and not gaps,
    }
