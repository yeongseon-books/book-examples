"""Generated from book-content article."""

import numpy as np

v = np.array([2.0, -1.0])
A = np.array([[1.5, 0.5],
              [0.0, 2.0]])
R = np.array([[0.0, -1.0],
              [1.0,  0.0]])

Av = A @ v
RAv = R @ Av

print('v =', v)
print('||v|| =', np.linalg.norm(v))
print('A v =', Av)
print('R(A v) =', RAv)
print('det(A) =', np.linalg.det(A))
