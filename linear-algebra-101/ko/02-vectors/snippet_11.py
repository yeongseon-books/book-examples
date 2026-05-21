"""Generated from book-content article."""

import numpy as np

# 고차원 벡터 예시
dim = 128
v = np.random.randn(dim)
w = np.random.randn(dim)

# 동일한 연산이 그대로 작동
v_plus_w = v + w
norm_v = np.linalg.norm(v)
unit_v = v / norm_v

print(f'{dim}차원 벡터')
print('v + w shape:', v_plus_w.shape)
print('||v|| =', norm_v)
print('||unit_v|| =', np.linalg.norm(unit_v))

# 코사인 유사도도 동일하게 작동
cos_sim = np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))
print('cosine similarity:', cos_sim)
