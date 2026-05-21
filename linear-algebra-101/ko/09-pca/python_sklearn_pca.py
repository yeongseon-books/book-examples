"""Generated from book-content article."""

import numpy as np
from sklearn.decomposition import PCA

rng = np.random.default_rng(99)
X = rng.normal(size=(150, 5))
X[:, 3] = 0.9 * X[:, 0] + 0.1 * rng.normal(size=150)

pca = PCA()
pca.fit(X)

print('설명 분산 비율:', pca.explained_variance_ratio_)
print('누적 분산 비율:', pca.explained_variance_ratio_.cumsum())

# 95% 이상 설명하는 최소 성분 수
n_components_95 = (pca.explained_variance_ratio_.cumsum() >= 0.95).argmax() + 1
print('95% 설명하는 최소 성분 수:', n_components_95)

# 차원 축소
pca_reduced = PCA(n_components=n_components_95)
X_reduced = pca_reduced.fit_transform(X)
print('축소 후 형상:', X_reduced.shape)
