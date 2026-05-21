# 카나리 탐지 (간단한 방식)
def canary_check(model_call, canary: str = "Th3_C@nary_X9z!") -> bool:
    rsp = model_call(f"Complete the string: {canary[:5]}")
    return canary in rsp  # True는 suspected contamination을 의미합니다
