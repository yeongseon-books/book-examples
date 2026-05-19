"""Data Science Career 101 - Episode 8: First job."""

from __future__ import annotations

ROLE_TASKS = {
    "analyst": ["핵심 대시보드 학습", "지표 정의 문서화", "SQL 성능 점검"],
    "scientist": ["데이터 품질 검증", "베이스라인 모델 작성", "실험 로그 검토"],
    "engineer": ["파이프라인 DAG 파악", "데이터 모델 점검", "모니터링 알림 점검"],
}


def generate_onboarding_tasks(role: str, week: int) -> list[str]:
    """Generate onboarding tasks."""
    base = ROLE_TASKS[role]
    if week <= 1:
        return ["1:1 미팅 5건", "데이터 지도 작성", *base[:1]]
    if week <= 2:
        return [*base, "작은 승리 1건"]
    return [*base, "30/60/90 문서 업데이트", "결정 기록 문서"]


def validate_first_month_checklist(items: list[str]) -> dict[str, object]:
    """Validate first month checklist."""
    required = ["1:1", "데이터 지도", "작은 승리", "결정 기록"]
    missing = [key for key in required if not any(key in item for item in items)]
    return {"is_valid": not missing, "missing": missing}
