class Node:
    def __init__(self, val: float, parents=(), local=()):
        self.val = val
        self.parents = parents
        self.local = local
        self.grad = 0.0


def add(a: Node, b: Node) -> Node:
    return Node(a.val + b.val, (a, b), (1.0, 1.0))


def mul(a: Node, b: Node) -> Node:
    return Node(a.val * b.val, (a, b), (b.val, a.val))


def backward(n: Node) -> None:
    n.grad = 1.0
    stack = [n]
    while stack:
        x = stack.pop()
        for p, lg in zip(x.parents, x.local):
            p.grad += x.grad * lg
            stack.append(p)


def run_demo() -> dict[str, float]:
    a, b, c = Node(2.0), Node(3.0), Node(4.0)
    y = mul(add(a, b), c)
    backward(y)
    return {"a_grad": a.grad, "b_grad": b.grad, "c_grad": c.grad}
