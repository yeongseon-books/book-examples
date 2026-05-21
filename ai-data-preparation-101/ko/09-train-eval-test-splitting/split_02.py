"""Generated from book-content article."""

from sklearn.model_selection import StratifiedShuffleSplit

X, y = features, labels
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_idx, test_idx in sss.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

# 검증
import numpy as np
print("train:", np.bincount(y_train) / len(y_train))
print("test :", np.bincount(y_test) / len(y_test))
