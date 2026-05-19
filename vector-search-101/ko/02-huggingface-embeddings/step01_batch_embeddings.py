import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
PAIRS = [
    (
        "벡터 검색은 비슷한 의미의 문장을 찾는 기술입니다.",
        "의미가 비슷한 텍스트를 가까운 벡터로 검색할 수 있습니다.",
    ),
    (
        "벡터 검색은 비슷한 의미의 문장을 찾는 기술입니다.",
        "오늘은 야구 경기 결과를 확인했습니다.",
    ),
    (
        "청킹 전략은 검색 품질에 큰 영향을 줍니다.",
        "문서를 어떻게 나누느냐에 따라 검색 결과가 달라집니다.",
    ),
]


def cosine_similarity(left: NDArray[np.float32], right: NDArray[np.float32]) -> float:
    return float(np.dot(left, right))


def main() -> None:
    model = SentenceTransformer(MODEL_NAME)
    flat_sentences = [sentence for pair in PAIRS for sentence in pair]
    embeddings = model.encode(
        flat_sentences, normalize_embeddings=True, convert_to_numpy=True
    )

    print(f"모델: {MODEL_NAME}")
    print(f"한 번에 임베딩한 문장 수: {len(flat_sentences)}")
    print()

    for pair_index, (sentence_a, sentence_b) in enumerate(PAIRS, start=0):
        vector_a = embeddings[pair_index * 2]
        vector_b = embeddings[pair_index * 2 + 1]
        similarity = cosine_similarity(vector_a, vector_b)

        print(f"쌍 {pair_index + 1}")
        print(f"  A: {sentence_a}")
        print(f"  B: {sentence_b}")
        print(f"  코사인 유사도: {similarity:.4f}")
        print()


if __name__ == "__main__":
    main()
