"""Tests for 04 data cleaning in Data Science 101."""

from _loader import load_module

m = load_module("04-data-cleaning.py")


def test_episode_04_cleaning_removes_nulls_and_duplicates() -> None:
    """Test episode 04 cleaning removes nulls and duplicates."""
    df = m.clean_dataset(seed=42)
    assert int(df.isna().sum().sum()) == 0
    assert int(df.duplicated(subset=["user_id"]).sum()) == 0
