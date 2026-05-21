"""Generated from book-content article."""

def f(x):
    return (x - 3.0) ** 2 + 2.0

def grad_f(x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def gradient_descent(x0=0.0, lr=0.1, steps=50):
    x = x0
    trace = []
    for _ in range(steps):
        g = grad_f(x)
        x = x - lr * g
        trace.append((x, f(x), g))
    return trace

trace = gradient_descent()
print(trace[-1])
