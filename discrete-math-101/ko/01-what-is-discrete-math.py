# 불리언, 집합, 그래프의 간단한 투어


def discrete_tour():
    boolean = (3 % 2 == 1) and (4 % 2 == 0)
    aset, bset = {1, 2, 3}, {3, 4}
    set_ops = {'union': aset | bset, 'intersection': aset & bset}
    graph = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
    return {'boolean': boolean, 'set_ops': set_ops, 'neighbors_A': graph['A']}


if __name__ == '__main__':
    print(discrete_tour())
