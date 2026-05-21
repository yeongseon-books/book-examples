"""Generated from book-content article."""

import numpy as np

# 선형변환 예시: 회전
theta = np.pi / 3
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])

u = np.array([1.0, 2.0])
v = np.array([3.0, 4.0])
a, b = 2.5, -1.3

# 선형성 검증
lhs = R @ (a * u + b * v)
rhs = a * (R @ u) + b * (R @ v)

print('T(au + bv):', lhs)
print('aT(u) + bT(v):', rhs)
print('선형성 만족:', np.allclose(lhs, rhs))
