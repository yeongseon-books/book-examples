from conftest import load_module


def test_logistic_regression_separates_tiny_dataset() -> None:
    mod = load_module("ko/06-ai-and-data-science.py")
    xs = [[0.1], [0.2], [0.8], [0.9]]
    ys = [0, 0, 1, 1]
    weights, bias = mod.train_logistic_regression(xs, ys, lr=0.3, epochs=400)
    assert mod.predict_probability([0.15], weights, bias) < 0.5
    assert mod.predict_probability([0.85], weights, bias) > 0.5
