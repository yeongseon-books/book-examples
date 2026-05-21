"""Generated from book-content article."""

import numpy as np

# 기저 벡터
e1 = np.array([1.0, 0.0])
e2 = np.array([0.0, 1.0])

# 선형 조합
v = 3 * e1 + 4 * e2
print('v =', v)
print('||v|| =', np.linalg.norm(v))

# 행렬 곱을 열벡터의 선형 조합으로 읽기
A = np.array([[1.0, 2.0],
              [3.0, 4.0]])
x = np.array([5.0, 6.0])
result = A @ x
# 이것은 A의 첫 번째 열에 5를 곱하고, 두 번째 열에 6을 곱해 더한 것과 같습니다
manual = 5 * A[:, 0] + 6 * A[:, 1]
print('A @ x =', result)
print('manual =', manual)
print('same?', np.allclose(result, manual))
