from ko.ep02_embed_index import InMemoryVectorIndex


def test_ep02_index_search_returns_topk():
    idx = InMemoryVectorIndex(dim=128)
    idx.add_texts(["chunk about overlap", "chunk about cosine", "chunk about prompt"])
    out = idx.search("cosine similarity", top_k=2)
    assert len(out) == 2
    assert all(isinstance(score, float) for _, score in out)
