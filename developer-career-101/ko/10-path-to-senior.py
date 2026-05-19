def readiness_scorecard(scores: dict[str, int]) -> dict:
    required = ["technical_depth", "mentorship", "cross_functional", "scope", "impact"]
    gaps = [k for k in required if scores.get(k, 0) < 6]
    avg = sum(scores.get(k, 0) for k in required) / len(required)
    plan = [f"strengthen {k} via monthly goals" for k in gaps]
    return {"average": round(avg, 2), "gaps": gaps, "plan_6m": plan}
