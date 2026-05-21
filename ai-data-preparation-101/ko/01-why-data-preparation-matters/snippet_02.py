"""Generated from book-content article."""

from sklearn.model_selection import train_test_split

# 잘못된 방식: plain random split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 올바른 방식: stratify keeps class ratios stable
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
