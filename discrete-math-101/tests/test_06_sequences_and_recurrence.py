import importlib.util
from pathlib import Path

def load(p):
    s=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def test_fibonacci_three_ways_match():
    m=load(Path('ko/06-sequences-and-recurrence.py'))
    vals=(m.fib_naive(20),m.fib_memo(20),m.fib_matrix(20))
    assert vals[0]==vals[1]==vals[2]
    assert m.recurrence_iter(10)==m.recurrence_closed(10)
