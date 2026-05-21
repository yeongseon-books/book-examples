"""Generated from book-content article."""

def relu(x):
    return np.maximum(0, x)

u = np.array([1.0, -1.0])
v = np.array([2.0, -2.0])
a, b = 0.5, 0.5

# ReLU는 비선형
lhs = relu(a * u + b * v)
rhs = a * relu(u) + b * relu(v)

print('ReLU(au + bv):', lhs)
print('a ReLU(u) + b ReLU(v):', rhs)
print('선형성 만족:', np.allclose(lhs, rhs))  # False
