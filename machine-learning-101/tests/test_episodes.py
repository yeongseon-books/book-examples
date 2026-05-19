"""Tests for episodes in Machine Learning 101."""

from episodes import ep01, ep02, ep04, ep05, ep06, ep07, ep08, ep09, ep10


def test_ep01_pipeline_basics() -> None:
    """Test ep01 pipeline basics."""
    out = ep01.run()
    assert out["acc"] > 0.75


def test_ep02_supervised_vs_unsupervised() -> None:
    """Test ep02 supervised vs unsupervised."""
    out = ep02.run()
    assert out["clf_acc"] > 0.9
    assert out["kmeans_clusters"] == 3.0


def test_ep03_leakage_demo() -> None:
    """Test ep03 leakage demo."""
    out = ep02.run_ep03()
    assert out["leaked"] >= out["good"]


def test_ep04_linear_regression_metrics() -> None:
    """Test ep04 linear regression metrics."""
    out = ep04.run()
    assert out["r2"] > 0.95
    assert out["mse"] < 60


def test_ep05_logistic_regression_confusion_matrix() -> None:
    """Test ep05 logistic regression confusion matrix."""
    out = ep05.run()
    assert out["acc"] > 0.8
    assert out["tp"] > 50


def test_ep06_feature_importance_and_tree_vs_forest() -> None:
    """Test ep06 feature importance and tree vs forest."""
    out = ep06.run()
    assert abs(out["tree_imp_sum"] - 1.0) < 1e-6
    assert abs(out["rf_imp_sum"] - 1.0) < 1e-6


def test_ep07_kmeans_cluster_count_and_silhouette() -> None:
    """Test ep07 kmeans cluster count and silhouette."""
    out = ep07.run()
    assert out["kmeans_k"] == 3.0
    assert out["kmeans_sil"] > 0.45


def test_ep08_ridge_shrinks_weights() -> None:
    """Test ep08 ridge shrinks weights."""
    out = ep08.run()
    assert out["ridge_norm"] < out["ols_norm"]


def test_ep09_cross_val_and_roc_auc() -> None:
    """Test ep09 cross val and roc auc."""
    out = ep09.run()
    assert out["cv_count"] == 5.0
    assert out["roc_auc"] > 0.8


def test_ep10_pipeline_gridsearch_end_to_end() -> None:
    """Test ep10 pipeline gridsearch end to end."""
    out = ep10.run()
    assert out["best_score"] > 0.75
    assert out["test_acc"] > 0.75
