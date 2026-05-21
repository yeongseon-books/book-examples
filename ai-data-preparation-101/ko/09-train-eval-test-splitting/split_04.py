"""Generated from book-content article."""

import pandas as pd

df = df.sort_values("timestamp")
n = len(df)
train = df.iloc[: int(n * 0.7)]
val   = df.iloc[int(n * 0.7) : int(n * 0.85)]
test  = df.iloc[int(n * 0.85) :]

# 롤링 윈도우 backtest (optional)
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5, test_size=int(n * 0.1))
for fold, (tr, te) in enumerate(tscv.split(df)):
    print(f"fold {fold}: train={len(tr)}, test={len(te)}")
