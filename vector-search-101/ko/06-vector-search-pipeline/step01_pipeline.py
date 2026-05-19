import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DOCUMENTS = [
    "임베딩 모델은 텍스트를 고정 길이 벡터로 바꿉니다.",
    "코사인 유사도는 질문 벡터와 문서 벡터의 방향 유사성을 비교합니다.",
    "FAISS IndexFlatIP는 정규화된 벡터를 빠르게 검색하기 좋은 출발점입니다.",
    "고정 크기 청킹은 긴 문서를 일정한 단위로 나누는 가장 단순한 방법입니다.",
    "벡터 검색 파이프라인은 수집, 청킹, 임베딩, 인덱싱, 검색 단계로 구성됩니다.",
    "검색 결과는 가장 비슷한 청크를 보여주고 이후 답변 생성 단계로 연결될 수 있습니다.",
]


class VectorSearchPipeline:
    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self._model = SentenceTransformer(model_name)
        self._index: faiss.IndexFlatIP | None = None
        self._documents: list[str] = []

    def build(self, documents: list[str]) -> None:
        self._documents = documents
        vectors = self._model.encode(documents, normalize_embeddings=True, convert_to_numpy=True).astype("float32")
        self._index = faiss.IndexFlatIP(vectors.shape[1])
        self._index.add(vectors)  # pyright: ignore[reportCallIssue]
        print(f"인덱스 생성 완료: 문서 {len(documents)}개, 차원 {vectors.shape[1]}")

    def search(self, query: str, top_k: int = 3) -> list[dict[str, float | str]]:
        if self._index is None:
            raise RuntimeError("build()를 먼저 호출해야 합니다.")

        query_vector = self._model.encode([query], normalize_embeddings=True, convert_to_numpy=True).astype("float32")
        scores, indices = self._index.search(query_vector, top_k)  # pyright: ignore[reportCallIssue]

        results: list[dict[str, float | str]] = []
        for doc_index, score in zip(indices[0], scores[0], strict=False):
            results.append(
                {
                    "score": float(score),
                    "text": self._documents[int(doc_index)],
                }
            )
        return results


def main() -> None:
    pipeline = VectorSearchPipeline()
    pipeline.build(DOCUMENTS)

    for query in [
        "벡터 검색 파이프라인은 어떤 단계로 구성되나요?",
        "정규화된 벡터를 어디에서 검색하나요?",
        "긴 문서를 단순하게 나누는 방법은 무엇인가요?",
    ]:
        print()
        print(f"질문: {query}")
        for rank, result in enumerate(pipeline.search(query, top_k=2), start=1):
            print(f"  {rank}. score={result['score']:.4f} | {result['text']}")


if __name__ == "__main__":
    main()
