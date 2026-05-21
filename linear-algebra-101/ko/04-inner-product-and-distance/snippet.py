"""Generated from book-content article."""

import numpy as np

q = np.array([0.2, 0.8, 0.0])
d1 = np.array([0.1, 0.9, 0.0])
d2 = np.array([0.9, 0.1, 0.0])

def cosine(a, b):
    return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

for name, d in [('d1', d1), ('d2', d2)]:
    print(name)
    print('  cosine =', cosine(q, d))
    print('  L2     =', np.linalg.norm(q - d))
    print('  L1     =', np.abs(q - d).sum())
