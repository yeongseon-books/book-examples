"""Generated from book-content article."""

import numpy as np
from sklearn.model_selection import TimeSeriesSplit

ts = np.arange(20).reshape(-1, 1)
for tr, te in TimeSeriesSplit(n_splits=3).split(ts):
    print(tr[-1], te[0])
