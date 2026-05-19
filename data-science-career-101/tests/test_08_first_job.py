from __future__ import annotations

from .conftest import load_module

mod = load_module("ko/08-first-job.py")


def test_first_month_checklist_validation() -> None:
    checklist = ["1:1 미팅 10건", "데이터 지도 작성", "작은 승리 1건", "결정 기록 문서"]
    result = mod.validate_first_month_checklist(checklist)
    assert result["is_valid"] is True
