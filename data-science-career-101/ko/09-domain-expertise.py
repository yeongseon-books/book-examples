"""Data Science Career 101 - Episode 9: Domain expertise."""

from __future__ import annotations

DOMAIN_MAP = {
    "fintech": {
        "metrics": ["승인율", "연체율", "거래 성공률"],
        "data_sources": ["결제 로그", "신용 이벤트", "KYC 데이터"],
        "regulations": ["AML", "개인정보보호", "전자금융규정"],
    },
    "health": {
        "metrics": ["재입원율", "치료 순응도", "대기 시간"],
        "data_sources": ["EMR", "청구 데이터", "웨어러블 데이터"],
        "regulations": ["HIPAA", "의료정보보호", "IRB"],
    },
    "ecommerce": {
        "metrics": ["전환율", "객단가", "재구매율"],
        "data_sources": ["클릭스트림", "주문 데이터", "재고 데이터"],
        "regulations": ["전자상거래법", "소비자보호", "개인정보보호"],
    },
}


def build_domain_spec(industry: str) -> dict[str, object]:
    """Build domain spec."""
    key = industry.lower()
    if key not in DOMAIN_MAP:
        raise ValueError(f"unsupported industry: {industry}")
    return {"industry": key, **DOMAIN_MAP[key]}
