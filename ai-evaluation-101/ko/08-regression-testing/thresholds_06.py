# regression/thresholds.py
THRESHOLDS_WITH_TOLERANCE = {
    "exact_match":  (0.80, 0.02),  # pass at >= 0.78 (0.02 tolerance)
    "judge_score":  (4.0,  0.1),
    "faithfulness": (0.85, 0.02),
}

def check_with_tolerance(metric: str, score: float) -> bool:
    threshold, tol = THRESHOLDS_WITH_TOLERANCE[metric]
    return score >= (threshold - tol)
