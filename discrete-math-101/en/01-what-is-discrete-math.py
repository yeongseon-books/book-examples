"""Discrete Math 101 - Episode 1: What is discrete math."""

# English runnable example
# Boolean, set, and graph tour


def discrete_tour():
    """Discrete tour."""
    boolean = (3 % 2 == 1) and (4 % 2 == 0)
    aset, bset = {1, 2, 3}, {3, 4}
    set_ops = {"union": aset | bset, "intersection": aset & bset}
    graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    return {"boolean": boolean, "set_ops": set_ops, "neighbors_A": graph["A"]}


if __name__ == "__main__":
    print(discrete_tour())
