"""Azure Aca 101 - Episode 1: Dapr sidecar."""


def publish_url(component: str, topic: str) -> str:
    """Publish url."""
    return f"http://localhost:3500/v1.0/publish/{component}/{topic}"


def invoke_url(app_id: str, method: str) -> str:
    """Invoke url."""
    return f"http://localhost:3500/v1.0/invoke/{app_id}/method/{method}"


def component_manifest() -> dict[str, object]:
    """Component manifest."""
    return {
        "componentType": "pubsub.azure.servicebus.queues",
        "scopes": ["api-app", "worker-app"],
        "secretRef": "servicebus-connection-string",
    }


def run() -> dict[str, object]:
    """Run."""
    return {
        "publish": publish_url("orderpubsub", "orders"),
        "invoke": invoke_url("worker-app", "process"),
        "component": component_manifest(),
    }


if __name__ == "__main__":
    print(run())
