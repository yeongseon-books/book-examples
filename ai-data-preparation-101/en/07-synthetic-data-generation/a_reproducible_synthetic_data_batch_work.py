"""Generated from book-content article."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import uuid

from openai import OpenAI

client = OpenAI()

SEED_TASKS = [
    {
        "task_id": "seed-001",
        "instruction": "Summarize the refund policy for a customer.",
        "input": "A customer on an annual plan asks whether a refund is still possible 10 days after payment.",
        "output": "Annual-plan payments are still within the 14-day refund review window.",
        "source_type": "self_instruct",
        "difficulty": "baseline",
        "evidence": None,
    },
    {
        "task_id": "seed-002",
        "instruction": "Answer a customer question using only the outage notice.",
        "input": "Explain the cause of the API slowdown described in the 2026-05-01 outage notice.",
        "output": "The outage notice says the direct cause was database connection-pool saturation.",
        "source_type": "rag_eval",
        "difficulty": "baseline",
        "evidence": "Cause: database connection-pool saturation",
    },
]

FAQ_CHUNKS = {
    "faq-014": "Refund policy: annual plans remain eligible for refund review within 14 days of payment; after that, partial-refund review depends on usage.",
    "faq-021": "Outage notice: from 2026-05-01 10:42 UTC, API latency increased because the database connection pool was saturated.",
}

GENERATION_CONTRACT = {
    "type": "object",
    "required": ["items"],
    "item_required": [
        "task_id",
        "instruction",
        "input",
        "output",
        "source_type",
        "difficulty",
        "reasons",
    ],
    "allowed_source_type": ["self_instruct", "evol_instruct", "rag_eval", "distillation"],
}

BRANCH_GUIDE = {
    "self_instruct": "Make a new task in the same domain but with a different customer situation.",
    "evol_instruct": "Take a baseline task and add one realistic constraint that forces deeper reasoning.",
    "rag_eval": "Generate only when the answer can be quoted from the supplied FAQ chunk.",
    "distillation": "Only use if a policy reviewer has approved output reuse for this teacher.",
}

def build_prompt(batch_goal: str, branch: str) -> str:
    return f"""
You are generating training data for a SaaS support assistant.
Batch goal: {batch_goal}
Branch guide: {BRANCH_GUIDE[branch]}

Return JSON with the shape:
{{
  "items": [
    {{
      "task_id": "syn-...",
      "instruction": "...",
      "input": "...",
      "output": "...",
      "source_type": "{branch}",
      "difficulty": "baseline|hard",
      "evidence": "required when source_type is rag_eval, otherwise null",
      "reasons": ["why this sample adds coverage"]
    }}
  ]
}}

Seed tasks:
{json.dumps(SEED_TASKS, ensure_ascii=False, indent=2)}

FAQ chunks:
{json.dumps(FAQ_CHUNKS, ensure_ascii=False, indent=2)}
"""

def generate_batch(batch_goal: str, branch: str, model: str = "gpt-4o-mini") -> list[dict]:
    rsp = client.chat.completions.create(
        model=model,
        temperature=0.7 if branch != "rag_eval" else 0.2,
        response_format={"type": "json_object"},
        messages=[{"role": "user", "content": build_prompt(batch_goal, branch)}],
    )
    payload = json.loads(rsp.choices[0].message.content)
    return payload["items"]

def validate_item(item: dict) -> list[str]:
    reasons = []
    for key in GENERATION_CONTRACT["item_required"]:
        if key not in item:
            reasons.append(f"missing:{key}")
    if item.get("source_type") not in GENERATION_CONTRACT["allowed_source_type"]:
        reasons.append("invalid_source_type")
    if item.get("source_type") == "rag_eval":
        evidence = item.get("evidence")
        if not evidence:
            reasons.append("missing_evidence")
        elif not any(evidence in chunk for chunk in FAQ_CHUNKS.values()):
            reasons.append("evidence_not_found")
    if any(token in item.get("output", "").lower() for token in ["i cannot", "i'm sorry", "unable to help"]):
        reasons.append("refusal_like_output")
    if len(item.get("output", "")) < 30:
        reasons.append("too_short")
    return reasons

def validate_batch(items: list[dict]) -> tuple[list[dict], list[dict], dict]:
    accepted, rejected = [], []
    seen = Counter()

    for item in items:
        item_reasons = validate_item(item)
        dedup_key = (item.get("instruction"), item.get("input"))
        seen[dedup_key] += 1
        if seen[dedup_key] > 1:
            item_reasons.append("duplicate_instruction_input")

        if item_reasons:
            rejected.append({"item": item, "reasons": item_reasons})
        else:
            accepted.append(item)

    total = len(items) or 1
    metrics = {
        "n_total": len(items),
        "n_accepted": len(accepted),
        "n_rejected": len(rejected),
        "accept_ratio": len(accepted) / total,
        "unique_ratio": len(seen) / total,
        "refusal_ratio": sum("refusal_like_output" in r["reasons"] for r in rejected) / total,
    }
    return accepted, rejected, metrics

def write_dataset(accepted: list[dict], run_id: str) -> Path:
    out_dir = Path("datasets/ai-data-preparation-101/07-synthetic-data-generation") / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "accepted.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for row in accepted:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return out_path

run_id = f"support-batch-{uuid.uuid4().hex[:8]}"
items = generate_batch(batch_goal="Expand refund and outage support tasks", branch="self_instruct")
accepted, rejected, metrics = validate_batch(items)

if metrics["accept_ratio"] < 0.8 or metrics["unique_ratio"] < 0.85 or metrics["refusal_ratio"] > 0.05:
    raise RuntimeError({"run_id": run_id, "status": "reject_batch", "metrics": metrics, "rejected": rejected[:3]})

dataset_path = write_dataset(accepted, run_id)
print({"run_id": run_id, "status": "accepted", "dataset_path": str(dataset_path), "metrics": metrics})
