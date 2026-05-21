"""Generated from book-content article."""

import pandas as pd
from collections import Counter

def quick_quality_report(df: pd.DataFrame, text_col: str) -> dict:
    texts = df[text_col].dropna().astype(str)
    lengths = texts.str.len()
    word_counts = texts.str.split().str.len()
    return {
        "total_rows": len(df),
        "null_ratio": df[text_col].isna().mean(),
        "duplicate_ratio": 1 - texts.nunique() / len(texts),
        "avg_length": float(lengths.mean()),
        "p99_length": float(lengths.quantile(0.99)),
        "avg_words": float(word_counts.mean()),
        "language_dist": Counter(
            "en" if t.isascii() else "non-en" for t in texts.head(1000)
        ),
    }

# Example
df = pd.DataFrame({"text": ["hello", "hello", "안녕", None, "world"]})
print(quick_quality_report(df, "text"))
