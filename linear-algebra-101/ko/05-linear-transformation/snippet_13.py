# 신경망 한 레이어 시뮬레이션
W = np.random.randn(3, 4)
b = np.random.randn(3)
x = np.random.randn(4)

# 선형 부분
z = W @ x + b
print('linear output z:', z)

# 비선형 활성화
a = relu(z)
print('activated output a:', a)

# 선형 부분만으로는 복잡한 경계를 표현할 수 없음
# 비선형성이 표현력을 더함
