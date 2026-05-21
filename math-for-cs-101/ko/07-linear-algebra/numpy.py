"""Generated from book-content article."""

import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[2.0, 0.0], [1.0, 2.0]])
v = np.array([5.0, 6.0])

mat_vec = A @ v
mat_mul = A @ B
transposed = A.T
