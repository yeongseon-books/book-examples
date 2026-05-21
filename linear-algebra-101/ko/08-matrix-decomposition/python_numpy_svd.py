"""Generated from book-content article."""

import numpy as np

# 간단한 그레이스케일 이미지 시뮬레이션 (64x64)
rng = np.random.default_rng(77)
img = rng.normal(size=(64, 64))

# SVD
U, S, Vt = np.linalg.svd(img, full_matrices=False)

# 상위 k개 특이값만 사용
for k in [5, 10, 20]:
    img_k = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    rel_error = np.linalg.norm(img - img_k) / np.linalg.norm(img)
    compression_ratio = (64 * k + k + 64 * k) / (64 * 64)
    print(f'k={k:2d}: rel_err={rel_error:.4f}, compression={compression_ratio:.2%}')
