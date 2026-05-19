import numpy as np
from common import fit_linear_regression_normal_eq, fit_logistic_regression_gd


def run():
    np.random.seed(0)
    rng = np.random.default_rng(0)

    x = rng.normal(size=(200, 3))
    w_true = np.array([1.5, -2.0, 0.75])
    y = x @ w_true + rng.normal(scale=0.05, size=200)
    w_hat = fit_linear_regression_normal_eq(x, y)

    x2 = rng.normal(size=(240, 2))
    w2 = np.array([2.0, -1.0])
    logits = x2 @ w2
    y2 = (logits > 0).astype(float)
    w_clf = fit_logistic_regression_gd(x2, y2, lr=0.4, steps=2500, seed=0)
    preds = (1 / (1 + np.exp(-(x2 @ w_clf))) > 0.5).astype(float)
    acc = float((preds == y2).mean())

    print('linreg weights:', w_hat)
    print('logistic accuracy:', acc)
    return {'w_true': w_true, 'w_hat': w_hat, 'clf_w': w_clf, 'acc': acc}


if __name__ == '__main__':
    run()
