"""Generated from book-content article."""

def cross_dedup(train: list[str], eval_set: list[str],
                threshold: float = 0.85) -> tuple[list[str], int]:
    """Remove train rows that overlap eval_set. Returns also count removed."""
    lsh = MinHashLSH(threshold=threshold, num_perm=128)
    for i, doc in enumerate(eval_set):
        lsh.insert(f"eval_{i}", make_minhash(doc))
    clean_train: list[str] = []
    removed = 0
    for doc in train:
        if lsh.query(make_minhash(doc)):
            removed += 1
            continue
        clean_train.append(doc)
    return clean_train, removed
