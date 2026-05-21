"""Generated from book-content article."""

@dataclass
class TransformRecord:
    input_card_path: str
    input_sha256: str
    output_card_path: str
    output_sha256: str
    code_commit: str  # git rev-parse HEAD
    started_at: str
    finished_at: str
    config: dict

# Example
record = TransformRecord(
    input_card_path="./data/raw/ag_news_train.card.json",
    input_sha256="abc123...",
    output_card_path="./data/clean/ag_news_train.card.json",
    output_sha256="def456...",
    code_commit="a1b2c3d",
    started_at="2026-05-03T10:00:00Z",
    finished_at="2026-05-03T10:02:34Z",
    config={"min_length": 20, "lowercase": False},
)
