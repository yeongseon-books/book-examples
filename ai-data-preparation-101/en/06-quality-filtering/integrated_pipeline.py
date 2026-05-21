"""Generated from book-content article."""

def quality_filter_pipeline(docs: list[str], pf: PerplexityFilter, clf) -> list[str]:
    survivors = []
    stats = {"heuristic": 0, "lang": 0, "perplexity": 0, "classifier": 0, "kept": 0}
    for d in docs:
        ok, reason = passes_heuristic(d)
        if not ok:
            stats["heuristic"] += 1
            continue
        if not keep_languages(d, allowed={"ko", "en"}):
            stats["lang"] += 1
            continue
        if not pf.passes(d):
            stats["perplexity"] += 1
            continue
        if quality_score(d) < 0.5:
            stats["classifier"] += 1
            continue
        survivors.append(d)
        stats["kept"] += 1
    return survivors, stats
