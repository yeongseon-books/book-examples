"""Generated from book-content article."""

k = 2
A_k = U_svd[:, :k] @ np.diag(S_svd[:k]) @ Vt_svd[:k, :]
rel_err = np.linalg.norm(A - A_k) / np.linalg.norm(A)
print('rank-k relative error:', rel_err)
