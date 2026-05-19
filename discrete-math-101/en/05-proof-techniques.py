"""Discrete Math 101 - Episode 5: Proof techniques."""

# English runnable example
import math


def verify_induction(formula, direct, n_max=1000):
    """Check finite cases only; this is not a full induction proof."""
    return all(formula(n) == direct(n) for n in range(1, n_max + 1))


def sqrt2_contradiction_structure():
    """Sqrt2 contradiction structure."""
    return [
        "assume sqrt(2)=p/q reduced",
        "2q^2=p^2 so p even",
        "p=2k -> q even",
        "p,q both even contradiction",
    ]


if __name__ == "__main__":
    print(verify_induction(lambda n: n * (n + 1) // 2, lambda n: sum(range(1, n + 1))))
    print(math.isclose(math.sqrt(2) ** 2, 2.0))
