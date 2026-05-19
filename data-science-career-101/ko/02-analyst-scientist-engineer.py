"""Data Science Career 101 - Episode 2: Analyst scientist engineer."""

from __future__ import annotations

ROLE_KEYWORDS = {
    "analyst": {"sql", "dashboard", "kpi", "report", "stakeholder", "insight"},
    "scientist": {"experiment", "hypothesis", "model", "ab test", "causal", "feature"},
    "engineer": {"pipeline", "etl", "airflow", "spark", "warehouse", "reliability"},
}


def classify_job_description(text: str) -> dict[str, object]:
    """Classify job description."""
    lowered = text.lower()
    score = {role: 0 for role in ROLE_KEYWORDS}
    for role, keywords in ROLE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in lowered:
                score[role] += 1
    top = sorted(score.items(), key=lambda item: (-item[1], item[0]))[0][0]
    return {"scores": score, "predicted_role": top}
