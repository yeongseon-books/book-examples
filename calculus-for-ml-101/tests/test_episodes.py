import math
import importlib.util
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pair(ep: str, file_name: str):
    return (
        load_module(f"ko/{ep}/{file_name}"),
        load_module(f"en/{ep}/{file_name}"),
    )


def test_ep01_derivative():
    ko, en = pair("01-what-is-derivative", "step01_derivative.py")
    assert math.isclose(ko.run_demo()["slope_at_2"], 4.0, rel_tol=1e-4)
    assert math.isclose(en.run_demo()["slope_at_2"], 4.0, rel_tol=1e-4)


def test_ep02_functions_and_slope():
    ko, en = pair("02-functions-and-slope", "step01_functions_and_slope.py")
    assert ko.linear(3.0) == 7.0
    assert en.relu_grad(2.0) == 1.0
    assert math.isclose(ko.sigmoid(0.0), 0.5)


def test_ep03_partial_derivatives():
    ko, en = pair("03-partial-derivatives", "step01_partial_derivatives.py")
    gx, gy = ko.run_demo()["partials_at_2_1"]
    ex, ey = en.run_demo()["partials_at_2_1"]
    assert math.isclose(gx, 4.0, rel_tol=1e-4)
    assert math.isclose(gy, 3.0, rel_tol=1e-4)
    assert math.isclose(gx, ex, rel_tol=1e-9)
    assert math.isclose(gy, ey, rel_tol=1e-9)


def test_ep04_gradient():
    ko, en = pair("04-gradient", "step01_gradient.py")
    kg = ko.run_demo()["grad"]
    eg = en.run_demo()["grad"]
    assert np.allclose(kg, np.array([-2.0, 4.0]))
    assert np.allclose(kg, eg)
    assert ko.run_demo()["next_loss"] < ko.loss(np.array([0.0, 0.0]))


def test_ep05_chain_rule():
    ko, en = pair("05-chain-rule", "step01_chain_rule.py")
    assert math.isclose(ko.run_demo()["chain"], ko.run_demo()["numeric"], rel_tol=1e-4)
    assert math.isclose(en.run_demo()["chain"], en.run_demo()["numeric"], rel_tol=1e-4)


def test_ep06_loss_function():
    ko, en = pair("06-loss-function", "step01_loss_function.py")
    kres = ko.run_demo()
    eres = en.run_demo()
    assert math.isclose(kres["mse"], 0.04666666666666666, rel_tol=1e-9)
    assert all(isinstance(v, float) for v in kres["mse_grad"])
    assert math.isclose(kres["bce"], eres["bce"], rel_tol=1e-12)


def test_ep07_gradient_descent():
    ko, en = pair("07-gradient-descent", "step01_gradient_descent.py")
    kw = ko.run_demo()["w"]
    ew = en.run_demo()["w"]
    assert abs(kw - 3.0) < 1e-4
    assert abs(ew - 3.0) < 1e-4


def test_ep08_optimization():
    ko, en = pair("08-optimization", "step01_optimization.py")
    kw = ko.run_demo()["w"]
    ew = en.run_demo()["w"]
    assert abs(kw) < 0.1
    assert abs(kw - ew) < 1e-10


def test_ep09_backprop():
    ko, en = pair("09-backpropagation-intuition", "step01_backprop.py")
    k = ko.run_demo()
    e = en.run_demo()
    assert math.isclose(k["a_grad"], 4.0)
    assert math.isclose(k["b_grad"], 4.0)
    assert math.isclose(k["c_grad"], 5.0)
    assert k == e


def test_ep10_training_loop():
    ko, en = pair("10-calculus-in-deep-learning", "step01_training_loop.py")
    k = ko.run_demo()
    e = en.run_demo()
    assert k["p0"] < 0.3
    assert k["p1"] > 0.7
    assert math.isclose(k["p0"], e["p0"], rel_tol=1e-9)
    assert math.isclose(k["p1"], e["p1"], rel_tol=1e-9)
