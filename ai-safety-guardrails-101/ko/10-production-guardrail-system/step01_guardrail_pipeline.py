import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import (
    AuditLog,
    KB,
    MockLLM,
    detect_jailbreak,
    detect_prompt_injection,
    filter_output,
    redact_pii,
    verify_grounded_answer,
)


def run(user_input: str) -> dict[str, object]:
    audit = AuditLog()
    audit.append("input", user_input)

    p_inj = detect_prompt_injection(user_input)
    if not p_inj.allowed:
        audit.append("blocked", p_inj.reason)
        return {"blocked": True, "stage": "prompt_injection"}

    jail = detect_jailbreak(user_input)
    if not jail.allowed:
        audit.append("blocked", jail.reason)
        return {"blocked": True, "stage": "jailbreak"}

    masked = redact_pii(user_input)
    answer = MockLLM().complete(masked)
    grounded = verify_grounded_answer(answer, KB)
    if not grounded.allowed:
        audit.append("blocked", grounded.reason)
        return {"blocked": True, "stage": "grounding"}

    safe = filter_output(answer)
    audit.append("delivered", safe)
    return {"blocked": False, "answer": safe, "chain_ok": audit.verify_chain()}


if __name__ == "__main__":
    print(run("서울 수도 정보를 알려주세요."))
