from __future__ import annotations

from common import make_rng


def run(n: int = 200_000) -> dict[str, float]:
    rng = make_rng()
    x = rng.integers(1, 7, size=n)
    mean_sim = float(x.mean())
    var_sim = float(x.var())

    mean_exact = 3.5
    var_exact = 35 / 12
    return {
        "mean_exact": mean_exact,
        "mean_sim": mean_sim,
        "var_exact": var_exact,
        "var_sim": var_sim,
    }


if __name__ == "__main__":
    print(run())
