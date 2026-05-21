"""Generated from book-content article."""

import numpy as np

a = np.array([3.0, 1.0, -2.0])
b = np.array([6.0, 2.0, -4.0])
c = np.array([1.0, -1.0, 0.0])

def cosine(u, v):
    return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))

print('||a||, ||b||, ||c|| =', np.linalg.norm(a), np.linalg.norm(b), np.linalg.norm(c))
print('cos(a,b) =', cosine(a, b))
print('cos(a,c) =', cosine(a, c))
print('L2(a,c) =', np.linalg.norm(a - c))
print('L1(a,c) =', np.abs(a - c).sum())
