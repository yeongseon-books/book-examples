import importlib.util
from pathlib import Path

def load():
    p = Path(__file__).resolve().parents[1] / 'ko/09-avoiding-pattern-overuse.py'
    s = importlib.util.spec_from_file_location('ep09', p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_same_result_simpler_code():
    m = load()
    assert m.over_engineered('Kim') == m.simple('Kim')
