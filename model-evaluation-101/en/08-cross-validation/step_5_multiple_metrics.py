"""Generated from book-content article."""

from sklearn.model_selection import cross_validate

out = cross_validate(m, X, y, cv=cv, scoring=["f1_macro", "roc_auc"])
print({k: v.mean() for k, v in out.items() if k.startswith("test_")})
