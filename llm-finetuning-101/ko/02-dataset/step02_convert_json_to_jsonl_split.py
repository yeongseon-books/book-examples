"""JSON → JSONL 변환과 train/val 분할"""

from __future__ import annotations

import json
import random
from pathlib import Path

SAMPLE_DATA = [
    {
        "instruction": "환불 정책을 요약해 주세요.",
        "response": "구매 후 14일 이내이며 사용량이 적으면 환불 가능합니다.",
        "category": "refund",
    },
    {
        "instruction": "비밀번호 재설정 방법을 알려 주세요.",
        "response": "로그인 화면의 비밀번호 재설정 링크를 눌러 이메일 인증을 진행하세요.",
        "category": "auth",
    },
    {
        "instruction": "사용량 한도 초과 시 어떻게 되나요?",
        "response": "기본적으로 읽기 전용 상태로 전환되며 관리자에게 알림이 전송됩니다.",
        "category": "quota",
    },
    {
        "instruction": "장애 공지 톤을 예시로 보여 주세요.",
        "response": "영향 범위, 현재 상태, 다음 업데이트 시각을 포함해 차분하게 안내합니다.",
        "category": "incident",
    },
    {
        "instruction": "엔터프라이즈 요금제 특징은?",
        "response": "SLA, SSO, 감사 로그, 전담 지원을 제공합니다.",
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
    print("학습 샘플 수", len(train_rows))
    print("검증 샘플 수", len(val_rows))
    print(
        "원본 JSON이 없어서 내장 샘플 데이터를 사용했습니다."
        if not source.exists()
        else "원본 JSON 파일을 사용했습니다."
    )


if __name__ == "__main__":
    main()
