from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from common import ensure_dir, summarize_dataframe


def generate_collected_data(output_dir: str | Path, seed: int = 42, n_users: int = 200) -> dict[str, object]:
    out = ensure_dir(output_dir)
    rng = np.random.default_rng(seed)
    users = pd.DataFrame({
        "user_id": [f"U{i:05d}" for i in range(n_users)],
        "country": rng.choice(["KR", "US", "JP"], n_users, p=[0.5, 0.3, 0.2]),
        "signup_days_ago": rng.integers(1, 365, size=n_users),
    })
    events = pd.DataFrame({
        "user_id": rng.choice(users["user_id"], size=n_users * 5),
        "event_type": rng.choice(["login", "view", "purchase"], size=n_users * 5, p=[0.5, 0.4, 0.1]),
        "session_minutes": rng.integers(1, 120, size=n_users * 5),
    })
    tx = pd.DataFrame({
        "user_id": rng.choice(users["user_id"], size=n_users * 2),
        "amount": rng.normal(50.0, 20.0, size=n_users * 2).round(2),
    })
    path = out / "collected_data.csv"
    merged = users.merge(events.groupby("user_id").size().rename("event_count"), on="user_id", how="left").merge(
        tx.groupby("user_id")["amount"].sum().rename("total_amount"), on="user_id", how="left"
    )
    merged["event_count"] = merged["event_count"].fillna(0).astype(int)
    merged["total_amount"] = merged["total_amount"].fillna(0.0)
    merged.to_csv(path, index=False)
    loaded = pd.read_csv(path)
    report = summarize_dataframe(loaded)
    report["csv_path"] = str(path)
    return report


if __name__ == "__main__":
    print(generate_collected_data("tmp"))
