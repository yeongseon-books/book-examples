"""Data Science 101 - Episode 10: Data project end to end."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from common import ensure_dir, make_dirty_dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def run_pipeline(output_dir: str | Path, seed: int = 42) -> dict[str, object]:
    """Run pipeline."""
    out = ensure_dir(output_dir)

    raw = make_dirty_dataset(seed=seed, n=500)
    raw["age"] = pd.to_numeric(raw["age"], errors="coerce")
    raw["amount"] = pd.to_numeric(raw["amount"], errors="coerce")
    clean = raw.drop_duplicates(subset=["user_id"], keep="last").copy()
    clean["country"] = clean["country"].fillna("UNKNOWN")
    clean["age"] = clean["age"].fillna(clean["age"].median())
    clean["amount"] = clean["amount"].fillna(clean["amount"].median())

    clean["is_kr"] = (clean["country"] == "KR").astype(int)
    clean["target"] = (
        (clean["amount"] > clean["amount"].median()) & (clean["age"] < 45)
    ).astype(int)
    X = clean[["age", "amount", "is_kr"]]
    y = clean["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=y
    )
    model = RandomForestClassifier(n_estimators=120, random_state=seed).fit(
        X_train, y_train
    )
    acc = float(model.score(X_test, y_test))

    model_path = out / "data_science_101_model.joblib"
    joblib.dump(model, model_path)
    # WARNING: joblib.load deserializes pickle data and can execute arbitrary code.
    # Only load files from trusted sources.
    loaded = joblib.load(model_path)
    sample = X_test[:20]
    same_preds = bool((model.predict(sample) == loaded.predict(sample)).all())

    return {
        "accuracy": acc,
        "model_path": str(model_path),
        "same_predictions": same_preds,
        "rows": int(clean.shape[0]),
    }


if __name__ == "__main__":
    print(run_pipeline("tmp"))
