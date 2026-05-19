import importlib.util
from pathlib import Path

def load(p):
    s=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def test_induction_verifier():
    m=load(Path('ko/05-proof-techniques.py'))
    ok=m.verify_induction(lambda n:n*(n+1)//2, lambda n:sum(range(1,n+1)), 100)
    assert ok is True
    assert 'contradiction' in m.sqrt2_contradiction_structure()[-1]
