"""Generated from book-content article."""

import numpy as np

# 샘플 데이터 생성
rng = np.random.default_rng(42)
X = rng.normal(size=(200, 3))
X[:, 1] = X[:, 0] * 0.8 + rng.normal(scale=0.3, size=200)

# 공분산 행렬
Xc = X - X.mean(axis=0)
C = (Xc.T @ Xc) / (len(Xc) - 1)

# 고유값 분해
eigvals, eigvecs = np.linalg.eigh(C)

# 내림차순 정렬
idx = eigvals.argsort()[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

print('고유값(분산):', eigvals)
print('분산 설명률:', eigvals / eigvals.sum())

# 주성분 방향으로 투영
X_pca = Xc @ eigvecs[:, :2]
print('투영 후 형상:', X_pca.shape)
