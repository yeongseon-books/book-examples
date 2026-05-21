"""Generated from book-content article."""

from sklearn.calibration import calibration_curve

prob_true, prob_pred = calibration_curve(y_true, y_score, n_bins=10)
for p_hat, p_real in zip(prob_pred, prob_true, strict=False):
    print(round(p_hat, 3), round(p_real, 3), round(p_real - p_hat, 3))
