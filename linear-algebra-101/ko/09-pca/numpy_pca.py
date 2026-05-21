"""Generated from book-content article."""

import numpy as np

rng = np.random.default_rng(42)
X = rng.normal(size=(200, 5))
X[:, 2] = 0.7 * X[:, 0] + 0.2 * X[:, 1] + 0.1 * rng.normal(size=200)

Xc = X - X.mean(axis=0)
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
explained_ratio = (S ** 2) / np.sum(S ** 2)
cum_ratio = np.cumsum(explained_ratio)

k = int(np.searchsorted(cum_ratio, 0.95) + 1)
Z = Xc @ Vt[:k].T
X_rec = Z @ Vt[:k]

recon_err = np.linalg.norm(Xc - X_rec) / np.linalg.norm(Xc)

print('explained ratio:', explained_ratio)
print('cumulative ratio:', cum_ratio)
print('chosen k:', k)
print('relative reconstruction error:', recon_err)
