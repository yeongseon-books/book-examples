"""Generated from book-content article."""

from dataclasses import dataclass
from collections.abc import Callable

@dataclass
class GuardrailResult:
    allowed: bool
    stage: str
    reason: str | None = None
    metadata: dict | None = None

class GuardrailPipeline:
    def __init__(self, audit_sink: Callable):
        self.audit = audit_sink

    def run(self, request: dict) -> dict:
        ctx = {"request_id": request["request_id"], "user_id": request["user_id"]}

        # Pre-input
        for check in [self.rate_limit, self.detect_jailbreak, self.sanitize_input]:
            res = check(request)
            self.audit({**ctx, "stage": res.stage, "allowed": res.allowed, "reason": res.reason})
            if not res.allowed:
                return self._block(res)

        # Pre-prompt
        masked_prompt, pii_meta = self.mask_pii(request["prompt"])
        retrieved = self.retrieve(masked_prompt)
        sanitized_chunks = self.sanitize_context(retrieved)

        # Model call
        response = self.call_model(masked_prompt, sanitized_chunks)

        # Post-output
        for check in [self.moderate_output, self.verify_grounding, self.recheck_pii]:
            res = check(response, sanitized_chunks)
            self.audit({**ctx, "stage": res.stage, "allowed": res.allowed, "reason": res.reason})
            if not res.allowed:
                return self._block(res)

        final = self.unmask_pii(response, pii_meta)
        self.audit({**ctx, "stage": "delivered", "allowed": True})
        return {"answer": final}

    def _block(self, res: GuardrailResult) -> dict:
        return {"answer": "We can't process that request.", "blocked": True, "stage": res.stage}
