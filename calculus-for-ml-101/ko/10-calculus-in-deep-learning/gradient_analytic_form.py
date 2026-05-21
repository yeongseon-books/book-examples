"""Generated from book-content article."""

def grads(x, y, w, b):
    p = model(x, w, b)
    err = p - y
    return err * x, err
