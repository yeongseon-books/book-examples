"""Generated from book-content article."""

def deterministic_gate(task_type: str, pred: str, expected: str) -> str:
    if task_type in {"classification", "extractive_qa"}:
        return "PASS" if exact_match_normalized(pred, expected) else "FAIL"

    rouge = scorer.score(expected, pred)["rougeL"].fmeasure
    if rouge >= 0.7:
        return "LIKELY_OK"
    if rouge <= 0.3:
        return "REVIEW_WITH_LLM_JUDGE"
    return "HUMAN_SPOT_CHECK"
