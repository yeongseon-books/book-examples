def lexical_scope(x: int):
    def inner(y: int) -> int:
        return x + y

    return inner


def dynamic_scope(func, env: dict, y: int) -> int:
    return func(env, y)


def dyn_add(env: dict, y: int) -> int:
    return env["x"] + y
