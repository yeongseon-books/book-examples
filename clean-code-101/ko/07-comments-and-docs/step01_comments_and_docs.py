# 결제 파트너가 HTTP 200을 반환해도 본문에 실패 상태를 넣는 경우가 있어
# 응답 코드 대신 본문 상태를 확인합니다.
def is_paid(response: dict[str, object]) -> bool:
    return response.get("status") == "PAID"


def discount(price: int, rate: float) -> int:
    """할인 적용 후 가격을 반환합니다.

    Args:
        price: 정수 원 단위 가격.
        rate: 0~1 범위의 할인율.

    Returns:
        반올림된 정수 가격.

    Raises:
        ValueError: rate가 범위를 벗어난 경우.
    """
    if not 0 <= rate <= 1:
        raise ValueError("rate out of range")
    return int(price * (1 - rate))
