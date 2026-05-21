"""Generated from book-content article."""

import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[2.0, 0.0], [1.0, 2.0]])
v = np.array([1.0, -1.0])

print("A+B", A + B)
print("A@B", A @ B)
print("A@v", A @ v)
