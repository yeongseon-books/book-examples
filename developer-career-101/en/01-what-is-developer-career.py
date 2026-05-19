from common import clamp


def classify_stage(
    years: int, technical_depth: int, ownership: int, influence: int
) -> dict:
    score = clamp(years * 6 + technical_depth * 2 + ownership * 1.6 + influence * 1.4)
    if score >= 90:
        stage = "staff"
    elif score >= 65:
        stage = "senior"
    elif score >= 40:
        stage = "mid"
    else:
        stage = "junior"
    return {"stage": stage, "score": round(score, 2)}
