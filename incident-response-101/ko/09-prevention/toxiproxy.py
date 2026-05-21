"""Generated from book-content article."""

import json

import requests


def setup_toxiproxy(proxy_name, listen, upstream):
    """
    toxiproxy를 통해 프록시를 생성합니다.
    """
    toxiproxy_url = "http://localhost:8474"
    payload = {
        "name": proxy_name,
        "listen": listen,
        "upstream": upstream,
        "enabled": True,
    }
    response = requests.post(f"{toxiproxy_url}/proxies", json=payload)
    return response.json()


def inject_latency(proxy_name, latency_ms, jitter_ms=0):
    """
    특정 프록시에 레이턴시를 주입합니다.
    """
    toxiproxy_url = "http://localhost:8474"
    toxic_payload = {
        "type": "latency",
        "attributes": {
            "latency": latency_ms,
            "jitter": jitter_ms,
        },
    }
    response = requests.post(
        f"{toxiproxy_url}/proxies/{proxy_name}/toxics",
        json=toxic_payload,
    )
    return response.json()


def inject_timeout(proxy_name, timeout_ms):
    """
    특정 프록시에 timeout을 주입합니다.
    """
    toxiproxy_url = "http://localhost:8474"
    toxic_payload = {
        "type": "timeout",
        "attributes": {
            "timeout": timeout_ms,
        },
    }
    response = requests.post(
        f"{toxiproxy_url}/proxies/{proxy_name}/toxics",
        json=toxic_payload,
    )
    return response.json()


# 사용 예시
# 1. 결제 API에 대한 proxy 설정
setup_toxiproxy("payment-api", "0.0.0.0:8001", "payment-api.internal:8000")

# 2. 3초 레이턴시 주입
inject_latency("payment-api", latency_ms=3000, jitter_ms=500)
print("결제 API에 3초 레이턴시 주입 완료")

# 3. timeout 후 circuit breaker 동작 확인
# 애플리케이션이 5초 timeout으로 설정되어 있다면
# circuit breaker가 열리고 fallback이 동작해야 함
