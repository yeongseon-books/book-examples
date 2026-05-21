"""Generated from book-content article."""

def hit_at_k(predictions: list[list[str]],
             gold: list[str], k: int = 5) -> float:
    hits = sum(1 for pred, g in zip(predictions, gold) if g in pred[:k])
    return hits / len(gold)

def mrr(predictions: list[list[str]], gold: list[str]) -> float:
    total = 0.0
    for pred, g in zip(predictions, gold):
        if g in pred:
            total += 1.0 / (pred.index(g) + 1)
    return total / len(predictions)
