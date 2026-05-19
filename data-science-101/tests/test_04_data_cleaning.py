from _loader import load_module

m = load_module("04-data-cleaning.py")


def test_episode_04_cleaning_removes_nulls_and_duplicates() -> None:
    df = m.clean_dataset(seed=42)
    assert int(df.isna().sum().sum()) == 0
    assert int(df.duplicated(subset=["user_id"]).sum()) == 0
