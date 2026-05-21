"""Generated from book-content article."""

import numpy as np

A = np.array([
    [1.0, 2.0, 3.0],
    [2.0, 4.0, 6.0],
    [0.0, 1.0, 2.0],
])

rank = np.linalg.matrix_rank(A)
print('rank(A):', rank)

# 영공간 계산: Ax=0의 해 공간
U, S, Vt = np.linalg.svd(A)
null_mask = S < 1e-10
null_space = Vt[null_mask, :]

print('null space dim:', null_space.shape[0])
print('null space basis:\n', null_space)

# 검증: A @ v = 0
if null_space.shape[0] > 0:
    v = null_space[0]
    result = A @ v
    print('A @ v:', result)
    print('close to zero:', np.allclose(result, 0))
