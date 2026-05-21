"""Generated from book-content article."""

fp = (pred == 1) & (yte == 0)
fn = (pred == 0) & (yte == 1)
print("FP:", fp.sum(), "FN:", fn.sum())
