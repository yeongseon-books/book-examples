"""Developer Career 101 - Episode 2: Understanding roles."""

from common import keyword_score

ROLE_KEYWORDS = {
    "frontend": ["react", "css", "ui", "web vitals", "lcp"],
    "backend": ["api", "python", "sql", "latency", "distributed"],
    "fullstack": ["frontend", "backend", "end-to-end", "product"],
    "devops": ["ci/cd", "terraform", "deployment", "pipeline"],
    "sre": ["slo", "mttr", "incident", "reliability", "on-call"],
    "mobile": ["android", "ios", "swift", "kotlin", "mobile"],
    "ml": ["model", "pytorch", "feature", "training", "auc"],
}


def classify_job_description(text: str) -> dict:
    """Classify job description."""
    scores = {role: keyword_score(text, kws) for role, kws in ROLE_KEYWORDS.items()}
    best_role = max(scores, key=lambda role: scores[role])
    return {"role": best_role, "scores": scores}
