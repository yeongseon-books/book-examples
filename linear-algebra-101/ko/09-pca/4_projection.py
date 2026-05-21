"""Generated from book-content article."""

k = 1
X_pca = X_std @ eigvecs[:, :k]
print('1차원 투영:', X_pca.shape)
