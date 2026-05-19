"""Vector Search 101 - Episode 1: Indexflat search."""

import faiss
import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CORPUS = [
    "임베딩은 텍스트를 숫자 벡터로 변환합니다.",
    "FAISS는 대규모 벡터를 빠르게 검색하는 라이브러리입니다.",
    "FastAPI는 파이썬 API 서버를 만들 때 자주 사용됩니다.",
    "청킹은 긴 문서를 검색하기 좋은 조각으로 나누는 과정입니다.",
    "코사인 유사도는 두 벡터의 방향이 얼마나 비슷한지 측정합니다.",
    "벡터 데이터베이스는 임베딩 검색에 최적화된 저장소입니다.",
]


def build_index(
    model: SentenceTransformer, corpus: list[str]
) -> tuple[faiss.IndexFlatIP, NDArray[np.float32]]:
    """Build index."""
    vectors = model.encode(
        corpus, normalize_embeddings=True, convert_to_numpy=True
    ).astype("float32")
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)  # pyright: ignore[reportCallIssue]
    return index, vectors


def search(
    model: SentenceTransformer,
    index: faiss.IndexFlatIP,
    query: str,
    top_k: int = 3,
) -> list[tuple[int, float]]:
    """Search."""
    query_vector = model.encode(
        [query], normalize_embeddings=True, convert_to_numpy=True
    ).astype("float32")
    scores, indices = index.search(query_vector, top_k)  # pyright: ignore[reportCallIssue]
    return list(zip(indices[0].tolist(), scores[0].tolist(), strict=False))


def main() -> None:
    """Main."""
    model = SentenceTransformer(MODEL_NAME)
    index, vectors = build_index(model, CORPUS)

    print(f"문서 수: {len(CORPUS)}")
    print(f"벡터 차원: {vectors.shape[1]}")
    print()

    queries = [
        "벡터 검색 라이브러리를 찾고 싶습니다.",
        "파이썬으로 API 서버를 만들고 싶습니다.",
    ]

    for query in queries:
        print(f"질문: {query}")
        for rank, (doc_index, score) in enumerate(search(model, index, query), start=1):
            print(f"  {rank}. score={score:.4f} | {CORPUS[doc_index]}")
        print()


if __name__ == "__main__":
    main()
