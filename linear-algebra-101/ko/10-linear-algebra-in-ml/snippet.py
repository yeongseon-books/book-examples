"""Generated from book-content article."""

import numpy as np

rng = np.random.default_rng(7)
X = rng.normal(size=(300, 6))
w_true = np.array([1.2, -0.8, 0.5, 0.0, 0.3, -0.2])
y = X @ w_true + 0.05 * rng.normal(size=300)

# 1) 회귀 가중치
w_hat, *_ = np.linalg.lstsq(X, y, rcond=None)

# 2) 임베딩 유사도 (샘플 10개)
E = X[:10]
E = E / np.linalg.norm(E, axis=1, keepdims=True)
S = E @ E.T

# 3) PCA 압축
Xc = X - X.mean(axis=0)
U, sv, Vt = np.linalg.svd(Xc, full_matrices=False)
X3 = Xc @ Vt[:3].T

print('w_hat:', w_hat)
print('similarity matrix shape:', S.shape)
print('compressed shape:', X3.shape)
