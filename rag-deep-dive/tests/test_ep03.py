from ko.ep03_retriever_mmr import mmr_rerank, top_k_retrieve


def test_ep03_topk_and_mmr_lengths():
    chunks = ["overlap helps context", "cosine similarity search", "prompt budget"]
    topk = top_k_retrieve("cosine", chunks, top_k=2)
    mmr = mmr_rerank("cosine", chunks, top_k=2)
    assert len(topk) == 2
    assert len(mmr) == 2


def test_ep03_mmr_unique_indices():
    chunks = ["a", "b", "c", "d"]
    mmr = mmr_rerank("a", chunks, top_k=3)
    ids = [x[0] for x in mmr]
    assert len(ids) == len(set(ids))
