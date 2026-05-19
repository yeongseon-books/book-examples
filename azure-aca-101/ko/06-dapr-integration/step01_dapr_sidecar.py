def publish_url(component: str, topic: str) -> str:
    return f"http://localhost:3500/v1.0/publish/{component}/{topic}"


def invoke_url(app_id: str, method: str) -> str:
    return f"http://localhost:3500/v1.0/invoke/{app_id}/method/{method}"


def component_manifest() -> dict[str, object]:
    return {
        "componentType": "pubsub.azure.servicebus.queues",
        "scopes": ["api-app", "worker-app"],
        "secretRef": "servicebus-connection-string",
    }


def run() -> dict[str, object]:
    return {
        "publish": publish_url("orderpubsub", "orders"),
        "invoke": invoke_url("worker-app", "process"),
        "component": component_manifest(),
    }


if __name__ == "__main__":
    print(run())
