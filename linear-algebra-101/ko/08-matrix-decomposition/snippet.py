"""Generated from book-content article."""

import numpy as np
from scipy.linalg import lu

A = np.array([
    [3.0, 1.0, 1.0],
    [1.0, 3.0, 1.0],
    [1.0, 1.0, 3.0],
])

P, L, U = lu(A)
Q, R = np.linalg.qr(A)
U_svd, S_svd, Vt_svd = np.linalg.svd(A)

print('LU check:', np.allclose(P @ A, L @ U))
print('QR check:', np.allclose(A, Q @ R))
print('SVD check:', np.allclose(A, U_svd @ np.diag(S_svd) @ Vt_svd))
