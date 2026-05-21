"""Generated from book-content article."""

import numpy as np

pts = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0],
]).T

S = np.array([[2.0, 0.0], [0.0, 1.0]])
R = np.array([[0.0, -1.0], [1.0, 0.0]])
H = np.array([[1.0, 0.5], [0.0, 1.0]])

M = H @ R @ S
out = M @ pts

print('transform matrix M:
', M)
print('transformed points:
', out.T)
print('det(M) =', np.linalg.det(M))
