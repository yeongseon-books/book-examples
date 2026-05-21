"""Generated from book-content article."""

import numpy as np

y = np.array([0]*95 + [1]*5)
pred_dummy = np.zeros_like(y)
print("acc:", (pred_dummy == y).mean())
