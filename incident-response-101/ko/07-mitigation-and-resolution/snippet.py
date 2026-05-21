"""Generated from book-content article."""

def canary_rollback(service, old_version, canary_ratio=0.1):
    """
    일부 트래픽만 먼저 이전 버전으로 되돌립니다.
    """
    return {
        "service": service,
        "old_version": old_version,
        "canary_ratio": canary_ratio,
        "status": "rollback_started",
        "watch_metrics": ["error_rate", "latency_p99"],
    }


def expand_rollback(service, canary_ratio, target_ratio):
    """
    카나리 비율을 점진적으로 높입니다.
    """
    if canary_ratio >= target_ratio:
        return {"status": "complete", "ratio": canary_ratio}

    new_ratio = min(canary_ratio + 0.1, target_ratio)
    return {
        "service": service,
        "new_ratio": new_ratio,
        "status": "expanding",
    }


# 사용 예시
initial = canary_rollback("payment-api", "v2.4.1", canary_ratio=0.1)
print(f"10% 트래픽을 {initial['old_version']}으로 되돌림")

# 모니터링 확인 후 확대
step1 = expand_rollback("payment-api", 0.1, 0.5)
print(f"오류율 정상, 50%로 확대: {step1['new_ratio']}")

step2 = expand_rollback("payment-api", 0.5, 1.0)
print(f"최종 100% 롤백 완료: {step2['status']}")
