"""Generated from book-content article."""

def mse_grad(y, p):
    n = len(y)
    return [-2 * (yi - pi) / n for yi, pi in zip(y, p, strict=False)]
