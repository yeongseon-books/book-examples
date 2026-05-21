"""Generated from book-content article."""

import numpy as np

A = np.array([
    [4.0, 1.0, 0.0],
    [1.0, 3.0, 0.0],
    [0.0, 0.0, 2.0],
])

vals, vecs = np.linalg.eigh(A)
print('eigenvalues:', vals)

for i in range(len(vals)):
    v = vecs[:, i]
    residual = np.linalg.norm(A @ v - vals[i] * v)
    print(f'i={i}, residual={residual:.3e}')
