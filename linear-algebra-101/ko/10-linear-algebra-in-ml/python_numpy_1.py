"""Generated from book-content article."""

import numpy as np

# 데이터
rng = np.random.default_rng(123)
X = rng.normal(size=(4, 3))  # 4 샘플, 3 피처
y = np.array([0, 1, 0, 1])  # 이진 분류

# 파라미터 초기화
W1 = rng.normal(scale=0.1, size=(3, 2))  # 은닉층 2개 뉴런
b1 = np.zeros(2)
W2 = rng.normal(scale=0.1, size=(2, 1))  # 출력층 1개 뉴런
b2 = np.zeros(1)

# 순전파
z1 = X @ W1 + b1
a1 = np.maximum(0, z1)  # ReLU
z2 = a1 @ W2 + b2
a2 = 1 / (1 + np.exp(-z2))  # Sigmoid

# 손실 (binary cross-entropy)
loss = -np.mean(y.reshape(-1, 1) * np.log(a2 + 1e-8) + (1 - y.reshape(-1, 1)) * np.log(1 - a2 + 1e-8))

# 역전파
da2 = (a2 - y.reshape(-1, 1)) / len(y)  # (4, 1)
dz2 = da2  # sigmoid derivative 포함
dW2 = a1.T @ dz2  # (2, 1)
db2 = dz2.sum(axis=0)  # (1,)

da1 = dz2 @ W2.T  # (4, 2)
dz1 = da1 * (z1 > 0)  # ReLU derivative
dW1 = X.T @ dz1  # (3, 2)
db1 = dz1.sum(axis=0)  # (2,)

print('loss:', loss)
print('dW1 shape:', dW1.shape, 'dW2 shape:', dW2.shape)
print('dW1:\n', dW1)
