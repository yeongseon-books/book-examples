"""Generated from book-content article."""

def demographic_parity(predictions: list[int], groups: list[str]) -> dict:
    rates = {}
    for g in set(groups):
        members = [p for p, gg in zip(predictions, groups) if gg == g]
        rates[g] = sum(members) / len(members) if members else 0
    return rates

rates = demographic_parity(preds, groups)
if max(rates.values()) - min(rates.values()) > 0.1:
    alert("disparate impact detected")
