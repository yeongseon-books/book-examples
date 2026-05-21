"""Generated from book-content article."""

def tpr_by_group(y_true: list[int], y_pred: list[int], groups: list[str]) -> dict[str, float]:
    out = {}
    uniq = sorted(set(groups))
    for g in uniq:
        idx = [i for i, gg in enumerate(groups) if gg == g]
        positives = [i for i in idx if y_true[i] == 1]
        if not positives:
            out[g] = 0.0
            continue
        tp = sum(1 for i in positives if y_pred[i] == 1)
        out[g] = tp / len(positives)
    return out


def equal_opportunity_gap(y_true, y_pred, groups) -> float:
    tprs = tpr_by_group(y_true, y_pred, groups)
    return max(tprs.values()) - min(tprs.values()) if tprs else 0.0
