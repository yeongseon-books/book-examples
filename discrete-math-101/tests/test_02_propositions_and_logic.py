import importlib.util
from pathlib import Path

def load(p):
    s=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def test_truth_table_and_tautology():
    m=load(Path('ko/02-propositions-and-logic.py'))
    rows=[m.evaluate(p,q) for p in [False,True] for q in [False,True]]
    assert rows==[False,False,True,False]
    assert m.tautology(lambda p: p or (not p), ['p']) is True
