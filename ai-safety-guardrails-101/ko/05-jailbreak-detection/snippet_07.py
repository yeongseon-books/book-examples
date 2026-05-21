"""Generated from book-content article."""

def evaluate(detector, attacks: list[str], benign: list[str]) -> dict:
    tp = sum(1 for x in attacks if detector(x)["blocked"])
    fp = sum(1 for x in benign if detector(x)["blocked"])
    return {
        "recall": tp / len(attacks),
        "false_positive_rate": fp / len(benign),
    }
