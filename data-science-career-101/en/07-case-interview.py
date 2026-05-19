from __future__ import annotations


def build_case_framework(prompt: str) -> dict[str, object]:
    return {
        "prompt": prompt,
        "clarifying_questions": [
            "어느 사용자 세그먼트에서 문제가 발생했나요?",
            "하락이 시작된 정확한 시점은 언제인가요?",
            "제품/마케팅 변경 이력이 있었나요?",
        ],
        "north_star_metric": "DAU",
        "supporting_metrics": ["활성 사용자당 세션 수", "재방문율", "신규 가입 전환율"],
        "hypotheses": [
            "온보딩 퍼널 이탈 증가",
            "핵심 기능 성능 저하",
            "데이터 파이프라인 집계 오류",
        ],
        "analysis_plan": [
            "세그먼트별 시계열 비교",
            "배포 전후 차이 분석",
            "이벤트 로깅 품질 점검",
        ],
        "decision_template": {
            "action": "실험/롤백 후보 제안",
            "risk": "잘못된 원인 가정",
            "follow_up": "2주 추적 측정",
        },
    }


def is_complete_framework(framework: dict[str, object]) -> bool:
    required = [
        "clarifying_questions",
        "north_star_metric",
        "hypotheses",
        "analysis_plan",
        "decision_template",
    ]
    return all(key in framework and framework[key] for key in required)
