"""Generated from book-content article."""

def loss(w):
    return (w - 3) ** 2

g = deriv(loss, 0.0)   # negative -> increase w to reduce loss
