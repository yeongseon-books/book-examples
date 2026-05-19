from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from common import make_clf_dataset


def run() -> dict[str, float]:
    x, y = make_clf_dataset(class_sep=1.0)
    tree = DecisionTreeClassifier(max_depth=5, random_state=42).fit(x, y)
    rf = RandomForestClassifier(n_estimators=200, random_state=42).fit(x, y)
    return {
        "tree_acc": float(tree.score(x, y)),
        "rf_acc": float(rf.score(x, y)),
        "tree_imp_sum": float(tree.feature_importances_.sum()),
        "rf_imp_sum": float(rf.feature_importances_.sum()),
    }
