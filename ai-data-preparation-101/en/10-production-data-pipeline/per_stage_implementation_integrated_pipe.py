"""Generated from book-content article."""

from datetime import datetime

import pandas as pd


# Stage 1: Ingest
def stage_ingest(sources: list[str]) -> pd.DataFrame:
    dfs = [pd.read_json(s, lines=True) for s in sources]
    df = pd.concat(dfs, ignore_index=True)
    df["ingested_at"] = datetime.utcnow()
    return df

# Stage 2: Clean + Dedup (Ep3)
def stage_clean(df: pd.DataFrame) -> pd.DataFrame:
    df["text"] = df["text"].str.strip().str.replace(r"\s+", " ", regex=True)
    df = df[df["text"].str.len() >= 50]
    df = df.drop_duplicates(subset=["text"])
    return df

# Stage 3: PII (Ep4)
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def stage_pii(df: pd.DataFrame) -> pd.DataFrame:
    def redact(t: str) -> str:
        results = analyzer.analyze(text=t, language="en")
        return anonymizer.anonymize(text=t, analyzer_results=results).text
    df["text"] = df["text"].map(redact)
    return df

# Stage 4: Quality (Ep6)
def stage_quality(df: pd.DataFrame) -> pd.DataFrame:
    def passes(t: str) -> bool:
        words = t.split()
        return 50 <= len(words) <= 100_000
    return df[df["text"].map(passes)]

# Stage 5: Tokenize/Chunk (Ep5)
def stage_chunk(df: pd.DataFrame, max_tokens: int = 500) -> pd.DataFrame:
    rows = []
    for _, r in df.iterrows():
        # recursive_chunk from Ep5
        chunks = [r["text"][i:i+2000] for i in range(0, len(r["text"]), 1800)]
        for i, c in enumerate(chunks):
            rows.append({**r.to_dict(), "chunk_id": i, "text": c})
    return pd.DataFrame(rows)

# Stage 6: Split + Version (Ep9)
def stage_split(df: pd.DataFrame, time_col: str = "ingested_at") -> dict:
    df = df.sort_values(time_col)
    n = len(df)
    return {
        "train": df.iloc[:int(n*0.8)],
        "val":   df.iloc[int(n*0.8):int(n*0.9)],
        "test":  df.iloc[int(n*0.9):],
    }
