"""Generated from book-content article."""

from sklearn.model_selection import GroupShuffleSplit

groups = df["user_id"].values
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_idx, test_idx in gss.split(df, groups=groups):
    train_df = df.iloc[train_idx]
    test_df = df.iloc[test_idx]

# 검증: no shared user_id
assert set(train_df["user_id"]) & set(test_df["user_id"]) == set()
