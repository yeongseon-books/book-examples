"""Multimodal Ai 101 - 10편: production multimodal app 예제."""

from common import MultimodalApp, synthetic_audio


def run(question: str = "what is in image?") -> dict[str, object]:
    """Run."""
    app = MultimodalApp()
    return app.query("grid-a", question, synthetic_audio())
