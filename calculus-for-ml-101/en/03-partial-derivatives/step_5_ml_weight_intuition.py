"""Generated from book-content article."""

def loss(w1, w2):
    return (w1 - 1) ** 2 + (w2 + 2) ** 2

g1, g2 = partials(loss, 0.0, 0.0)  # responsibility per weight
