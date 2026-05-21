"""Generated from book-content article."""

def run_evaluation(eval_set: list[dict], system_under_test) -> dict:
    # 1. Generate — feed inputs to the system under test, collect responses
    predictions = [system_under_test(ex["input"]) for ex in eval_set]

    # 2. Score — score each response
    scores = [score_one(ex, pred) for ex, pred in zip(eval_set, predictions, strict=False)]

    # 3. Aggregate — roll up the scores
    summary = {
        "accuracy": sum(s["correct"] for s in scores) / len(scores),
        "avg_relevance": sum(s["relevance"] for s in scores) / len(scores),
    }

    # 4. Compare — compare against the previous version
    return summary
