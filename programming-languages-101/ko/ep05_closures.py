def make_counter(start: int = 0):
    value = start

    def inc():
        nonlocal value
        value += 1
        return value

    return inc


def partial_add(x: int):
    return lambda y: x + y
