"""Generated from book-content article."""

import numpy as np

# 1. 기본 행렬 생성
A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0],
              [7.0, 8.0, 10.0]])  # 의도적으로 비특이행렬로

print('A:', A)
print('shape:', A.shape)
print('dtype:', A.dtype)

# 2. 전치
print('A^T:', A.T)
print('A^T shape:', A.T.shape)

# 3. 행렬 곱
B = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [1.0, 1.0]])
C = A @ B
print('A @ B:', C)
print('result shape:', C.shape)

# 4. 원소별 곱 (Hadamard product)
D = np.array([[1.0, 2.0, 3.0],
              [1.0, 2.0, 3.0],
              [1.0, 2.0, 3.0]])
E = A * D
print('A * D (element-wise):', E)

# 5. 역행렬
# 정방행렬이고 풍풀랜크일 때만 존재
try:
    A_inv = np.linalg.inv(A)
    print('A^-1:', A_inv)
    print('A @ A^-1:', A @ A_inv)
except np.linalg.LinAlgError:
    print('A는 역행렬이 없습니다 (singular matrix)')

# 6. 행렬식 (determinant)
det = np.linalg.det(A)
print('det(A):', det)

# 7. 대각행렬
diag_vals = np.array([2.0, 3.0, 4.0])
D_matrix = np.diag(diag_vals)
print('diagonal matrix:', D_matrix)

# 8. 특수 행렬 생성
I = np.eye(3)
zeros = np.zeros((3, 3))
ones = np.ones((3, 3))
print('identity:', I)
print('zeros:', zeros)
print('ones:', ones)
