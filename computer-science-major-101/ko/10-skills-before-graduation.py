"""Computer Science Major 101 - Episode 10: Skills before graduation."""


def score_skills(rubric: dict[str, int], threshold: int = 3) -> dict[str, object]:
    """Score skills."""
    if not rubric:
        return {"average": 0.0, "gaps": [], "levels": {}}
    average = sum(rubric.values()) / len(rubric)
    gaps = sorted(skill for skill, score in rubric.items() if score < threshold)
    levels = {
        skill: (
            "strong" if score >= 4 else "developing" if score >= threshold else "gap"
        )
        for skill, score in rubric.items()
    }
    return {"average": round(average, 2), "gaps": gaps, "levels": levels}


if __name__ == "__main__":
    report = score_skills({"algorithms": 4, "systems": 2, "sql": 3, "writing": 2})
    print(report)
