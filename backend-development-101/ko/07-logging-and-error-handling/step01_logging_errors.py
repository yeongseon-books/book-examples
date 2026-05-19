"""에피소드 07: request_id와 글로벌 예외 처리 예제입니다."""

import logging
import sys
from pathlib import Path

from fastapi import FastAPI

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import domain_error_handlers, request_id_middleware

log = logging.getLogger("backend101")


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    request_id_middleware(app)
    domain_error_handlers(app)

    @app.get("/orders/{amount}")
    def create_order(amount: int):
        """Create order."""
        if amount <= 0:
            raise app.state.DomainError("INVALID_AMOUNT", "amount must be positive")
        log.info("order accepted amount=%s", amount)
        return {"accepted": amount}

    return app
