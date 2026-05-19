from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from common import make_reg_dataset


def run() -> dict[str, float]:
    x, y = make_reg_dataset()
    model = LinearRegression().fit(x, y)
    pred = model.predict(x)
    return {
        "r2": float(r2_score(y, pred)),
        "mse": float(mean_squared_error(y, pred)),
        "coef0": float(model.coef_[0]),
    }
