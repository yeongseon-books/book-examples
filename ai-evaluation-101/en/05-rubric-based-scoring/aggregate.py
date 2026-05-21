# rubric/aggregate.py
def aggregate_weighted(scores: dict) -> tuple[float, str]:
    weights = {"correctness": 0.5, "completeness": 0.2,
               "clarity": 0.15, "tone": 0.15}
    weighted = sum(scores[k] * weights[k] for k in weights)

    # Correctness < 3 is an automatic FAIL
    if scores["correctness"] < 3:
        return weighted, "FAIL"
    if weighted >= 4.0:
        return weighted, "PASS"
    return weighted, "REVIEW"
