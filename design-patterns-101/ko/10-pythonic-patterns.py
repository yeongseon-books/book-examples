from contextlib import contextmanager
from dataclasses import dataclass

class FileLike:
    def __init__(self): self.opened=False
    def open(self): self.opened=True
    def close(self): self.opened=False

@contextmanager
def managed_file(res):
    res.open()
    try: yield res
    finally: res.close()

def classic_iterator(values):
    out=[]
    i=0
    while i < len(values): out.append(values[i]); i += 1
    return out

def pythonic_iterator(values):
    return [x for x in values]

def strategy_class(kind, value):
    class AddOne: 
        def apply(self, v): return v + 1
    class Double:
        def apply(self, v): return v * 2
    strategy = AddOne() if kind == 'add' else Double()
    return strategy.apply(value)

def strategy_function(kind, value):
    strategy = {'add': lambda v: v + 1, 'double': lambda v: v * 2}[kind]
    return strategy(value)

@dataclass
class User:
    name: str
    age: int
