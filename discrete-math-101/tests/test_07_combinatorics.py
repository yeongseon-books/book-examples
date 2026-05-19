import importlib.util
from pathlib import Path

def load(p):
    s=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def test_counts_and_generation():
    m=load(Path('ko/07-combinatorics.py'))
    assert m.ncr(5,2)==10
    perms=m.all_permutations([1,2,3],2)
    assert len(perms)==m.npr(3,2)
