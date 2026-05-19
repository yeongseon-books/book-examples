import faiss
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DOCUMENT = (
    "벡터 검색 시스템은 긴 문서를 여러 청크로 나눈 뒤 각 청크를 임베딩합니다. "
    "청크가 너무 크면 서로 다른 주제가 한 덩어리에 섞이고, 너무 작으면 문맥이 잘립니다. "
    "고정 크기 청킹은 구현이 단순해서 첫 번째 실습에 잘 어울립니다. "
    "오버랩을 두면 경계에서 끊긴 문맥을 일부 복구할 수 있습니다. "
    "검색 단계에서는 질문과 가장 비슷한 청크를 찾아 원문 일부를 보여줍니다."
)


def fixed_size_chunks(text: str, size: int, overlap: int) -> list[str]:
    words = text.split()
    step = size - overlap
    if step <= 0:
        raise ValueError("overlap은 size보다 작아야 합니다.")

    chunks: list[str] = []
    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + size])
        if chunk:
            chunks.append(chunk)
    return chunks


def main() -> None:
    model = SentenceTransformer(MODEL_NAME)
    query = "문맥이 끊기지 않게 청크를 나누는 방법이 궁금합니다."

    for size, overlap in [(12, 3), (20, 5)]:
        chunks = fixed_size_chunks(DOCUMENT, size=size, overlap=overlap)
        vectors = model.encode(
            chunks, normalize_embeddings=True, convert_to_numpy=True
        ).astype("float32")
        index = faiss.IndexFlatIP(vectors.shape[1])
        index.add(vectors)  # pyright: ignore[reportCallIssue]

        query_vector = model.encode(
            [query], normalize_embeddings=True, convert_to_numpy=True
        ).astype("float32")
        scores, indices = index.search(query_vector, 2)  # pyright: ignore[reportCallIssue]

        print(f"size={size}, overlap={overlap}, chunk_count={len(chunks)}")
        for rank, (chunk_index, score) in enumerate(
            zip(indices[0], scores[0], strict=False), start=1
        ):
            preview = chunks[int(chunk_index)]
            print(f"  {rank}. score={float(score):.4f} | {preview}")
        print()


if __name__ == "__main__":
    main()
