from common import RubricScorer


SCORER = RubricScorer(
    {
        "skill_fit": 0.25,
        "scope": 0.2,
        "learning_value": 0.2,
        "portfolio_impact": 0.2,
        "completability": 0.15,
    }
)


def evaluate_idea(values: dict[str, float]) -> dict:
    total, breakdown = SCORER.score(values)
    if total >= 75:
        decision = "GO"
    elif total >= 55:
        decision = "REFINE"
    else:
        decision = "NOGO"
    return {"score": total, "breakdown": breakdown, "decision": decision}
