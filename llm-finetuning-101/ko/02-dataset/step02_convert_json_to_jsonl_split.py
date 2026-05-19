"""Convert JSON to JSONL and split into train/validation"""

from __future__ import annotations

import json
import random
from pathlib import Path

SAMPLE_DATA = [
    {
        "instruction": "Summarize the refund policy.",
        "response": "Refunds are available within 14 days when usage remains low.",
        "category": "refund",
    },
    {
        "instruction": "How do I reset my password?",
        "response": "Use the reset-password link on the sign-in page and complete email verification.",
        "category": "auth",
    },
    {
        "instruction": "What happens if usage exceeds the quota?",
        "response": "The workspace becomes read-only and an alert is sent to administrators.",
        "category": "quota",
    },
    {
        "instruction": "Show an example tone for an incident update.",
        "response": "Use calm customer-facing language with impact, status, and next update time.",
        "category": "incident",
    },
    {
        "instruction": "What are enterprise plan highlights?",
        "response": "It includes SLA, SSO, audit logs, and dedicated support.",
        "category": "pricing",
    },
]


def load_records(source: Path):
    """Load records."""
    if source.exists():
        return json.loads(source.read_text(encoding="utf-8"))
    return SAMPLE_DATA


def write_jsonl(path: Path, rows) -> None:
    """Write jsonl."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    """Main."""
    base_dir = Path(__file__).resolve().parent
    source = base_dir / "outputs" / "synthetic_pairs.json"
    rows = load_records(source)
    random.Random(7).shuffle(rows)
    split_index = max(1, int(len(rows) * 0.8))
    train_rows = rows[:split_index]
    val_rows = rows[split_index:]
    output_dir = base_dir / "outputs"
    write_jsonl(output_dir / "train.jsonl", train_rows)
    write_jsonl(output_dir / "val.jsonl", val_rows)
    print("Training rows", len(train_rows))
    print("Validation rows", len(val_rows))
    print(
        "Used built-in sample data because no source JSON file was found."
        if not source.exists()
        else "Used the source JSON file."
    )


if __name__ == "__main__":
    main()


# Expected output:
# Converted 100 examples to JSONL
# Train split: 80 examples → train.jsonl
# Validation split: 20 examples → val.jsonl
