"""Generated from book-content article."""

import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(100, 3))
y = X @ np.array([1.0, -2.0, 0.5]) + rng.normal(scale=0.1, size=100)
w_hat, *_ = np.linalg.lstsq(X, y, rcond=None)
print("w_hat:", w_hat)
