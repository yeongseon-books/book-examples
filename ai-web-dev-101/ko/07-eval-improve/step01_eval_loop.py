from __future__ import annotations


def keyword_score(response: str, expected_keywords: list[str]) -> float:
    if not expected_keywords:
        return 0.0
    hit = sum(1 for kw in expected_keywords if kw in response)
    return hit / len(expected_keywords)


def evaluate_cases(cases: list[dict[str, object]]) -> dict[str, float]:
    scores: list[float] = []
    for case in cases:
        raw_keywords = case.get("expected_keywords", [])
        keywords = (
            [str(item) for item in raw_keywords]
            if isinstance(raw_keywords, list)
            else []
        )
        scores.append(keyword_score(str(case.get("response", "")), keywords))
    avg = sum(scores) / len(scores) if scores else 0.0
    pass_rate = sum(1 for s in scores if s >= 0.5) / len(scores) if scores else 0.0
    return {"avg_score": round(avg, 3), "pass_rate": round(pass_rate, 3)}
