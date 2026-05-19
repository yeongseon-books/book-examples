from sklearn.cluster import KMeans
from sklearn.datasets import load_iris, make_blobs
from sklearn.linear_model import LogisticRegression


def run() -> dict[str, float]:
    xi, yi = load_iris(return_X_y=True)
    clf = LogisticRegression(max_iter=1000, random_state=42).fit(xi, yi)
    xb, _ = make_blobs(n_samples=200, centers=3, cluster_std=1.2, random_state=42)
    km = KMeans(n_clusters=3, n_init=10, random_state=42).fit(xb)
    return {
        "clf_acc": float(clf.score(xi, yi)),
        "kmeans_clusters": float(len(set(km.labels_))),
    }


def run_ep03() -> dict[str, float]:
    from sklearn.model_selection import train_test_split

    x, y = load_iris(return_X_y=True)
    xtr, xte, ytr, yte = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=42
    )
    good = (
        LogisticRegression(max_iter=1000, random_state=42).fit(xtr, ytr).score(xte, yte)
    )
    leaked = (
        LogisticRegression(max_iter=1000, random_state=42).fit(x, y).score(xte, yte)
    )
    return {"good": float(good), "leaked": float(leaked)}
