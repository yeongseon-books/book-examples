"""Generated from book-content article."""

B = np.array([[1.0, -1.0],
              [2.0,  0.0]])
v = np.array([2.0, 1.0])

first = B @ v
second = A @ first
direct = (A @ B) @ v

print('Bv =', first)
print('A(Bv) =', second)
print('(AB)v =', direct)
print('same?', np.allclose(second, direct))
