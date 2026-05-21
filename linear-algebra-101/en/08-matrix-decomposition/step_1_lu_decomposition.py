"""Generated from book-content article."""

import numpy as np
from scipy.linalg import lu

A = np.array([[4.0, 3.0], [6.0, 3.0]])
P, L, U = lu(A)
print("L:", L)
print("U:", U)
