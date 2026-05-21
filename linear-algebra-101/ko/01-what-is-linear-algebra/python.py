"""Generated from book-content article."""

import numpy as np

# 벡터 생성
v = np.array([1.0, 2.0, 3.0])
print('vector v:', v)
print('shape:', v.shape)
print('norm:', np.linalg.norm(v))

# 행렬 생성
A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0],
              [7.0, 8.0, 9.0]])
print('matrix A:', A)
print('shape:', A.shape)

# 단위행렬
I = np.eye(3)
print('identity:', I)

# 영벡터와 영행렬
zero_v = np.zeros(3)
zero_A = np.zeros((3, 3))
print('zero vector:', zero_v)
print('zero matrix:', zero_A)
