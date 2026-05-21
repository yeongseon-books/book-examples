"""Generated from book-content article."""

from datasketch import MinHash, MinHashLSH

def make_minhash(text: str, num_perm: int = 128) -> MinHash:
    m = MinHash(num_perm=num_perm)
    # 5-gram word shingles
    words = text.lower().split()
    for i in range(len(words) - 4):
        shingle = " ".join(words[i:i+5])
        m.update(shingle.encode("utf-8"))
    return m

def near_dedup(docs: list[str], threshold: float = 0.85) -> list[str]:
    lsh = MinHashLSH(threshold=threshold, num_perm=128)
    keep: list[int] = []
    for i, doc in enumerate(docs):
        mh = make_minhash(doc)
        if not lsh.query(mh):  # nothing similar yet, keep
            lsh.insert(str(i), mh)
            keep.append(i)
    return [docs[i] for i in keep]

# Example
docs = [
    "The quick brown fox jumps over the lazy dog repeatedly today.",
    "The quick brown fox jumps over the lazy dog repeatedly today!",  # near-dup
    "Completely different content about machine learning and data.",
]
print(len(near_dedup(docs)))  # -> 2
