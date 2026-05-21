"""Generated from book-content article."""

def grad(f, x, h=1e-5):
    return [(f([xi + (h if i == j else 0) for i, xi in enumerate(x)])
             - f([xi - (h if i == j else 0) for i, xi in enumerate(x)])) / (2 * h)
            for j in range(len(x))]
