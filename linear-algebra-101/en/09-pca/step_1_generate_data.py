"""Generated from book-content article."""

import numpy as np
rng = np.random.default_rng(0)
X = rng.normal(size=(100, 3)) @ np.array([[1, 0.8, 0],
                                          [0, 0.6, 0],
                                          [0, 0,   1]])
