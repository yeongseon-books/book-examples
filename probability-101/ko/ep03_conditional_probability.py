from __future__ import annotations

from common import make_rng


def run(n: int = 200_000) -> dict[str, float]:
    rng = make_rng()
    d1 = rng.integers(1, 7, size=n)
    d2 = rng.integers(1, 7, size=n)
    a = (d1 + d2) >= 9
    b = d1 % 2 == 0
    p_a_given_b_sim = float((a & b).sum() / b.sum())

    total = 36
    num_b = 18
    num_a_and_b = sum(
        1 for x in range(1, 7) for y in range(1, 7) if (x + y >= 9 and x % 2 == 0)
    )
    p_a_given_b_exact = num_a_and_b / num_b
    return {"sim": p_a_given_b_sim, "exact": p_a_given_b_exact, "p_b": num_b / total}


if __name__ == "__main__":
    print(run())
