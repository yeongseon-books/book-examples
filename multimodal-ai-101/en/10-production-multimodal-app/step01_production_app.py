"""Multimodal Ai 101 - Episode 10: production multimodal app example."""

from common import MultimodalApp, synthetic_audio


def run(question: str = "what is in image?") -> dict[str, object]:
    """Run."""
    app = MultimodalApp()
    return app.query("grid-a", question, synthetic_audio())
