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
        "instruction": "고객이 환불 가능 기간을 물으면 정책 기준을 요약해 답하세요.",
        "input": "연간 플랜을 결제한 고객이 10일 뒤 환불 가능 여부를 묻습니다.",
        "output": "연간 플랜은 결제 후 14일 이내라면 환불 검토가 가능합니다.",
        "source_type": "self_instruct",
        "difficulty": "baseline",
        "evidence": None,
    },
    {
        "task_id": "seed-002",
        "instruction": "장애 공지 문서를 바탕으로 고객 질문에 답하세요.",
        "input": "2026-05-01 장애 공지 기준으로 API 지연 원인을 설명하세요.",
        "output": "당시 API 지연은 데이터베이스 connection pool 포화가 직접 원인이었습니다.",
        "source_type": "rag_eval",
        "difficulty": "baseline",
        "evidence": "원인: 데이터베이스 connection pool 포화",
    },
]

FAQ_CHUNKS = {
    "faq-014": "환불 정책: 연간 플랜은 결제 후 14일 이내 환불 검토가 가능하며, 이후에는 사용량을 기준으로 부분 환불 여부를 검토한다.",
    "faq-021": "장애 공지: 2026-05-01 10:42 UTC부터 API 지연이 발생했고, 데이터베이스 connection pool 포화가 원인이었다.",
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
    if any(token in item.get("output", "").lower() for token in ["죄송하지만", "도와드릴 수 없습니다", "i cannot"]):
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
