from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from common import ensure_dir, make_synthetic_classification


def create_charts(output_dir: str | Path, seed: int = 42) -> dict[str, str]:
    out = ensure_dir(output_dir)
    df = make_synthetic_classification(seed=seed, n=500)
    files: dict[str, str] = {}

    plt.figure()
    df["feature_0"].hist(bins=30)
    p = out / "histogram.png"
    plt.savefig(p)
    plt.close()
    files["histogram"] = str(p)

    plt.figure()
    plt.scatter(df["feature_0"], df["feature_1"], c=df["target"], alpha=0.5)
    p = out / "scatter.png"
    plt.savefig(p)
    plt.close()
    files["scatter"] = str(p)

    plt.figure()
    df.groupby("target")["feature_2"].mean().plot.bar()
    p = out / "bar.png"
    plt.savefig(p)
    plt.close()
    files["bar"] = str(p)

    plt.figure()
    df.sort_index()["feature_3"].rolling(20).mean().plot()
    p = out / "line.png"
    plt.savefig(p)
    plt.close()
    files["line"] = str(p)

    return files


if __name__ == "__main__":
    print(create_charts("tmp"))
