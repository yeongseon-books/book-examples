# 예시: 5차원 → 2차원 압축
X = np.random.randn(100, 5)
Xc = X - X.mean(axis=0)
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)

k = 2
X_compressed = Xc @ Vt[:k].T
X_reconstructed = X_compressed @ Vt[:k]

reconstruction_error = np.linalg.norm(Xc - X_reconstructed) / np.linalg.norm(Xc)
print('상대 재구성 오차:', reconstruction_error)
