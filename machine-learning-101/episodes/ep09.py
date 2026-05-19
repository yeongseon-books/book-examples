from common import make_clf_dataset
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split


def run() -> dict[str, float]:
    x, y = make_clf_dataset(class_sep=1.3)
    xtr, xte, ytr, yte = train_test_split(
        x, y, test_size=0.3, stratify=y, random_state=42
    )
    model = LogisticRegression(max_iter=1000, random_state=42).fit(xtr, ytr)
    prob = model.predict_proba(xte)[:, 1]
    pred = model.predict(xte)
    folds = cross_val_score(
        LogisticRegression(max_iter=1000, random_state=42), x, y, cv=5
    )
    report = classification_report(yte, pred, output_dict=True)
    return {
        "roc_auc": float(roc_auc_score(yte, prob)),
        "cv_count": float(len(folds)),
        "f1": float(report["1"]["f1-score"]),
    }
