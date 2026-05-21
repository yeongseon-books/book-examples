# 예시: 정규화 효과
high_dim = 100
v = np.random.randn(high_dim)
w = np.random.randn(high_dim)

# 원본 범위가 넓음
print('Before normalization:')
print('  L2 distance:', np.linalg.norm(v - w))
print('  ||v||:', np.linalg.norm(v))
print('  ||w||:', np.linalg.norm(w))

# 정규화 후
v_n = v / np.linalg.norm(v)
w_n = w / np.linalg.norm(w)
print('\nAfter normalization:')
print('  L2 distance:', np.linalg.norm(v_n - w_n))
print('  cosine similarity:', np.dot(v_n, w_n))
