import importlib.util
from pathlib import Path

def load():
    p = Path(__file__).resolve().parents[1] / 'ko/08-factory-and-di.py'
    s = importlib.util.spec_from_file_location('ep08', p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_factory_and_di_with_mock_injection():
    m = load()
    class MockPlugin(m.Plugin):
        def run(self, text): return f'mock:{text}'
    c = m.Container(); c.register(m.Plugin, lambda: MockPlugin())
    svc = m.Service(c.resolve(m.Plugin))
    assert svc.process('abc') == 'mock:abc'
    assert m.plugin_factory('upper').run('ab') == 'AB'
