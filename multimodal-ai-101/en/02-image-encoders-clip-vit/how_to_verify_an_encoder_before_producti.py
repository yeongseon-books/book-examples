"""Generated from book-content article."""

def verify_top1_margin(probs, min_margin: float = 0.15) -> bool:
    top2 = sorted(probs, reverse=True)[:2]
    return (top2[0] - top2[1]) >= min_margin
