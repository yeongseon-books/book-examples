"""Generated from book-content article."""

import numpy as np

# 회전과 스케일링 합성
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
S = np.array([[2.0, 0.0],
              [0.0, 0.5]])

v = np.array([1.0, 0.0])

# 두 가지 방법
result1 = R @ (S @ v)  # 먼저 스케일, 그 다음 회전
result2 = (R @ S) @ v  # 합성 행렬을 미리 만듦

print('R(Sv):', result1)
print('(RS)v:', result2)
print('same?', np.allclose(result1, result2))
