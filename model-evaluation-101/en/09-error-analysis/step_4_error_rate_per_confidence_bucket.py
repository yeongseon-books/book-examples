"""Generated from book-content article."""

bins = np.linspace(0, 1, 6)
for lo, hi in zip(bins[:-1], bins[1:], strict=False):
    m_ = (proba >= lo) & (proba < hi)
    if m_.sum():
        err = (pred[m_] != yte[m_]).mean()
        print(round(lo, 1), round(hi, 1), "err:", round(err, 3))
