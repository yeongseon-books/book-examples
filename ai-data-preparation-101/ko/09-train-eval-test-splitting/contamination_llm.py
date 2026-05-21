"""Generated from book-content article."""

import hashlib

def make_ngrams(text: str, n: int = 13) -> set[str]:
    tokens = text.split()
    if len(tokens) < n:
        return set()
    return {" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)}

def contamination_overlap(eval_doc: str, pretrain_chunks: list[str], n: int = 13) -> float:
    eval_grams = make_ngrams(eval_doc, n)
    if not eval_grams:
        return 0.0
    matched = 0
    for chunk in pretrain_chunks:
        chunk_grams = make_ngrams(chunk, n)
        matched += len(eval_grams & chunk_grams)
        if matched >= len(eval_grams):
            break
    return matched / len(eval_grams)

# 13-gram match >= 80% suggests contamination
