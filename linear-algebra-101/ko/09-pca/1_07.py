"""Generated from book-content article."""

import numpy as np

X = np.array([[1.0, 2000.0], [2.0, 3000.0], [3.0, 4000.0], [4.0, 5000.0]])
X_std = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
print('표준화 후:\n', X_std)
