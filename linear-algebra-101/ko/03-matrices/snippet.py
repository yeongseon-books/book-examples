"""Generated from book-content article."""

import numpy as np

A = np.array([[3.0, 1.0],
              [1.0, 2.0]])
b = np.array([9.0, 8.0])

x = np.linalg.solve(A, b)
A_inv = np.linalg.inv(A)

print('solution x =', x)
print('check A@x =', A @ x)
print('cond(A) =', np.linalg.cond(A))
print('inv-based x =', A_inv @ b)
