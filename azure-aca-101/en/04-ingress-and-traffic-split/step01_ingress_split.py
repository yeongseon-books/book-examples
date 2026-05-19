from fastapi import FastAPI, Header
from fastapi.testclient import TestClient


def app_for_revision(name: str) -> FastAPI:
    app = FastAPI()

    @app.get("/")
    def read_root(x_revision: str | None = Header(default=None)) -> dict[str, str]:
        return {"served_by": x_revision or name}

    return app


def ingress_hostname(app_name: str, mode: str) -> str:
    if mode == "external":
        return f"https://{app_name}.demo.koreacentral.azurecontainerapps.io"
    if mode == "internal":
        return f"https://{app_name}.internal.demo.koreacentral.azurecontainerapps.io"
    if mode == "disabled":
        return "disabled"
    raise ValueError("invalid mode")


def run() -> dict[str, str]:
    client = TestClient(app_for_revision("myapi--v1"))
    response = client.get("/")
    return {
        "host": ingress_hostname("myapi", "external"),
        "served_by": response.json()["served_by"],
    }


if __name__ == "__main__":
    print(run())
