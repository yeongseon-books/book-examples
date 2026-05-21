"""Generated from book-content article."""

import numpy as np

rng = np.random.default_rng(123)
X = rng.normal(size=(6, 4))
v = rng.normal(size=4)
A = rng.normal(size=(4, 4))

print('X shape:', X.shape)
print('v shape:', v.shape)
print('A shape:', A.shape)

# 기본 연산
xv = X @ v
Av = A @ v
print('Xv shape:', xv.shape)
print('Av shape:', Av.shape)

# 대칭 행렬 구성 후 고유값 확인
S = A.T @ A
eigvals = np.linalg.eigvalsh(S)
print('eigvals(S):', eigvals)

# SVD와 랭크 근사
U, s, Vt = np.linalg.svd(X, full_matrices=False)
rank = np.linalg.matrix_rank(X)
X2 = U[:, :2] @ np.diag(s[:2]) @ Vt[:2, :]
rel_err = np.linalg.norm(X - X2) / np.linalg.norm(X)

print('rank(X):', rank)
print('singular values:', s)
print('relative error(rank-2):', rel_err)
