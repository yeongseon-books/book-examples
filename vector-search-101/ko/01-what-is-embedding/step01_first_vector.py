"""Vector Search 101 - Episode 1: First vector."""

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
SENTENCES = [
    "벡터 검색은 문장의 의미를 숫자로 바꾸는 것에서 시작됩니다.",
    "임베딩 모델은 비슷한 뜻의 문장을 가까운 위치에 둡니다.",
    "파이썬으로 첫 벡터를 확인해 보겠습니다.",
]


def main() -> None:
    """Main."""
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode(SENTENCES, normalize_embeddings=True, convert_to_numpy=True)

    print(f"모델: {MODEL_NAME}")
    print(f"문장 수: {len(SENTENCES)}")
    print(f"벡터 차원: {vectors.shape[1]}")
    print()

    for index, (sentence, vector) in enumerate(
        zip(SENTENCES, vectors, strict=False), start=1
    ):
        print(f"[{index}] 문장: {sentence}")
        print(f"    벡터 norm: {np.linalg.norm(vector):.4f}")
        print(f"    앞 5개 값: {vector[:5].tolist()}")
        print()


if __name__ == "__main__":
    main()
