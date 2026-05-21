"""Generated from book-content article."""

def chain_rule_example(x, w, b):
    # y = (w*x + b)^2
    z = w * x + b
    y = z ** 2
    dy_dz = 2 * z
    dz_dw = x
    dy_dw = dy_dz * dz_dw
    return y, dy_dw

print(chain_rule_example(2.0, 0.5, 1.0))
