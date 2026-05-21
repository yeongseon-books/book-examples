"""Generated from book-content article."""

import numpy as np

v = np.array([4.0, 1.0])

E = np.eye(2)
B = np.column_stack([
    np.array([1.0, 1.0]),
    np.array([-1.0, 1.0]),
])

coord_E = np.linalg.solve(E, v)
coord_B = np.linalg.solve(B, v)

print('coord in standard basis:', coord_E)
print('coord in B basis:', coord_B)
print('reconstruct from B:', B @ coord_B)
