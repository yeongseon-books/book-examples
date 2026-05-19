"""Model Evaluation 101 - Episode 1: Calibration demo."""

from __future__ import annotations

from common import make_imbalanced, safe_split
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import brier_score_loss


def run(seed: int = 42) -> dict[str, float | int]:
    """Run."""
    X, y = make_imbalanced(
        n_samples=1200, weights=(0.75, 0.25), class_sep=0.7, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    base = RandomForestClassifier(n_estimators=120, random_state=seed).fit(
        X_train, y_train
    )
    base_prob = base.predict_proba(X_test)[:, 1]
    frac_pos, mean_pred = calibration_curve(y_test, base_prob, n_bins=10)
    platt = CalibratedClassifierCV(base, method="sigmoid", cv=3).fit(X_train, y_train)
    platt_prob = platt.predict_proba(X_test)[:, 1]
    return {
        "base_brier": float(brier_score_loss(y_test, base_prob)),
        "platt_brier": float(brier_score_loss(y_test, platt_prob)),
        "calibration_bins": int(min(len(frac_pos), len(mean_pred))),
    }
