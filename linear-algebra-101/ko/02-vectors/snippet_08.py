"""Generated from book-content article."""

x = np.array([10.0, 0.0])
y = np.array([1.0, 0.0])

x_n = x / np.linalg.norm(x)
y_n = y / np.linalg.norm(y)

print('raw dot:', x @ y)
print('normalized dot:', x_n @ y_n)
