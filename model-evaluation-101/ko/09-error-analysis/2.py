"""Generated from book-content article."""

from sklearn.metrics import f1_score
slice_mask = Xte[:, 0] > 0
print("slice + :", f1_score(yte[slice_mask], pred[slice_mask]))
print("slice - :", f1_score(yte[~slice_mask], pred[~slice_mask]))
