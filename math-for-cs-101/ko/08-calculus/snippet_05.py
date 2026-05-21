"""Generated from book-content article."""

def descend(f, x, lr=0.1, steps=100):
    for _ in range(steps):
        x = step(x, grad(f, x), lr)
    return x
