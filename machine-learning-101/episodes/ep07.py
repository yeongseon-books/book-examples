"""Machine Learning 101 - Episode 7."""

import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score


def run() -> dict[str, float]:
    """Run."""
    x, _ = make_blobs(n_samples=200, centers=3, cluster_std=1.0, random_state=42)
    km = KMeans(n_clusters=3, n_init=10, random_state=42).fit(x)
    db = DBSCAN(eps=0.7, min_samples=5).fit(x)
    db_labels = db.labels_
    db_valid = db_labels[db_labels != -1]
    db_sil = -1.0
    if len(np.unique(db_valid)) > 1:
        db_sil = float(silhouette_score(x[db_labels != -1], db_valid))
    return {
        "kmeans_sil": float(silhouette_score(x, km.labels_)),
        "dbscan_sil": db_sil,
        "kmeans_k": float(len(set(km.labels_))),
    }
