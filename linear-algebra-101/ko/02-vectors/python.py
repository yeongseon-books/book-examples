"""Generated from book-content article."""

import numpy as np


def cosine_similarity(a, b):
    """
    코사인 유사도를 계산합니다.
    cos(a, b) = (a · b) / (||a|| ||b||)
    """
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # 영벡터 방지
    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)

# 예시: 두 문서 임베딩 비교
doc1 = np.array([0.5, 0.8, 0.2])
doc2 = np.array([0.6, 0.7, 0.3])
doc3 = np.array([0.1, 0.1, 0.9])

print('doc1 vs doc2:', cosine_similarity(doc1, doc2))
print('doc1 vs doc3:', cosine_similarity(doc1, doc3))
print('doc2 vs doc3:', cosine_similarity(doc2, doc3))

# 정규화된 벡터는 내적 = 코사인 유사도
doc1_n = doc1 / np.linalg.norm(doc1)
doc2_n = doc2 / np.linalg.norm(doc2)
print('normalized dot:', np.dot(doc1_n, doc2_n))
print('cosine:', cosine_similarity(doc1, doc2))
