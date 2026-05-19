"""FastAPI mock server"""

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
        prompt: str
        adapter_name: str = "support-lora-v1"

    APP = FastAPI(title="fine-tuning-serving-mock")

    @APP.get("/health")
    def health_check():
        return {"status": "ok", "mode": "mock"}

    @APP.post("/generate")
    def generate(payload: InferenceRequest):
        return {
            "adapter": payload.adapter_name,
            "input": payload.prompt,
            "output": "This is a mock output that demonstrates the serving shape instead of running a real model.",
        }


def main() -> None:
    if FastAPI is None:
        print("FastAPI or pydantic is unavailable, so the mock server cannot start.")
        print("ImportError details", IMPORT_ERROR)
        print("Example: uvicorn step01_fastapi_mock_server:APP --reload")
        return
    print("The APP object is ready. Start it with uvicorn.")


if __name__ == "__main__":
    main()
