"""Generated from book-content article."""

import numpy as np
from scipy.spatial.distance import cityblock, cosine, euclidean, mahalanobis

# 샘플 벡터
v = np.array([1.0, 2.0, 3.0])
w = np.array([4.0, 5.0, 6.0])

# 1. 유클리드 거리 (L2)
dist_l2 = euclidean(v, w)
print('Euclidean distance:', dist_l2)
print('NumPy 동등:', np.linalg.norm(v - w))

# 2. 맨해튼 거리 (L1)
dist_l1 = cityblock(v, w)
print('Manhattan distance:', dist_l1)
print('NumPy 동등:', np.sum(np.abs(v - w)))

# 3. 코사인 거리 (1 - 코사인 유사도)
dist_cos = cosine(v, w)
print('Cosine distance:', dist_cos)
cos_sim = np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))
print('Cosine similarity:', cos_sim)
print('1 - cos_sim:', 1 - cos_sim)

# 4. 마할라노비스 거리
# 공분산 행렬 필요
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [2, 3, 4],
              [5, 6, 7]])
cov = np.cov(X.T)
cov_inv = np.linalg.pinv(cov)  # pseudo-inverse for stability

dist_maha = mahalanobis(v, w, cov_inv)
print('Mahalanobis distance:', dist_maha)

# 5. 여러 쌍 간 거리 행렬 계산
from scipy.spatial.distance import pdist, squareform

points = np.array([[0, 0],
                   [1, 0],
                   [0, 1],
                   [1, 1]])

# 모든 쌍 간 유클리드 거리
distances = pdist(points, metric='euclidean')
dist_matrix = squareform(distances)
print('Distance matrix:\n', dist_matrix)
