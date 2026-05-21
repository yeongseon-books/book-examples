"""Generated from book-content article."""

from datasets import load_dataset
from datetime import datetime, timezone

ds = load_dataset("ag_news", split="train")
ds.to_csv("./data/raw/ag_news_train.csv")

sha, size = fingerprint_file("./data/raw/ag_news_train.csv")
card = DatasetCard(
    name="ag_news",
    version="1.0.0",
    source_type="public",
    source_url="https://huggingface.co/datasets/ag_news",
    license="custom (academic only)",
    snapshot_date=datetime.now(timezone.utc).isoformat(),
    row_count=len(ds),
    size_bytes=size,
    sha256=sha,
    schema={"text": "string", "label": "int (0-3)"},
    description="AG News topic classification dataset (4 classes).",
    pii_fields=[],
    owner="ml-platform-team",
    tags=["nlp", "classification", "news"],
)
with open("./data/raw/ag_news_train.card.json", "w") as f:
    f.write(card.to_json())
