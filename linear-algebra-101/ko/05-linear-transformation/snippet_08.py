"""Generated from book-content article."""

T = M
u = np.array([1.0, 2.0])
v = np.array([-1.0, 3.0])
a, b = 2.5, -0.7

lhs = T @ (a * u + b * v)
rhs = a * (T @ u) + b * (T @ v)
print(np.allclose(lhs, rhs))
