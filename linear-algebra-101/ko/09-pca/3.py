"""Generated from book-content article."""

eigvals, eigvecs = np.linalg.eigh(C)
idx = eigvals.argsort()[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

print('고유값:', eigvals)
print('분산 설명률:', eigvals / eigvals.sum())
