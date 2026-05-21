"""Generated from book-content article."""

M = np.array([[0.95, 0.05],
              [0.10, 0.90]])
v = np.array([1.0, 0.0])

for _ in range(30):
    v = M @ v
    v = v / np.linalg.norm(v)

print('dominant direction:', v)
