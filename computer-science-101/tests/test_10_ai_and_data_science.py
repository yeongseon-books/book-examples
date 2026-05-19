import importlib.util
from pathlib import Path


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent.parent / rel)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_gradient_descent_fits_slope():
    m = load("ep10", "ko/10-ai-and-data-science.py")
    xs = [0, 1, 2, 3, 4, 5]
    ys = [1, 3, 5, 7, 9, 11]
    w, b = m.train_linear_regression(xs, ys, lr=0.02, epochs=4000)
    assert abs(w - 2.0) < 0.05
    assert abs(b - 1.0) < 0.1
