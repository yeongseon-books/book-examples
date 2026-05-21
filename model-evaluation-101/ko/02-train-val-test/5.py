"""Generated from book-content article."""

from sklearn.linear_model import LogisticRegression

sc = StandardScaler().fit(Xtr)
m = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
print("valid:", m.score(sc.transform(Xva), yva))
