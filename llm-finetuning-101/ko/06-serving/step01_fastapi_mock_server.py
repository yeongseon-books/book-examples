"""FastAPI mock 서버"""

# pyright: reportGeneralTypeIssues=false

from __future__ import annotations

try:
    from fastapi import FastAPI
    from pydantic import BaseModel
except ImportError as exc:
    FastAPI = None
    BaseModel = object
    IMPORT_ERROR = exc
else:
    IMPORT_ERROR = None

APP = None

if FastAPI is not None:

    class InferenceRequest(BaseModel):
        """Inference request."""

        prompt: str
        adapter_name: str = "support-lora-v1"

    APP = FastAPI(title="fine-tuning-serving-mock")

    @APP.get("/health")
    def health_check():
        """Health check."""
        return {"status": "ok", "mode": "mock"}

    @APP.post("/generate")
    def generate(payload: InferenceRequest):
        """Generate."""
        return {
            "adapter": payload.adapter_name,
            "input": payload.prompt,
            "output": "이 응답은 실제 모델 대신 서빙 구조를 설명하기 위한 mock 결과입니다.",
        }


def main() -> None:
    """Main."""
    if FastAPI is None:
        print("FastAPI 또는 pydantic 이 없어 서버를 실행하지 못합니다.")
        print("ImportError 상세", IMPORT_ERROR)
        print("예시: uvicorn step01_fastapi_mock_server:APP --reload")
        return
    print("APP 객체가 준비되었습니다. uvicorn으로 실행하세요.")


if __name__ == "__main__":
    main()
