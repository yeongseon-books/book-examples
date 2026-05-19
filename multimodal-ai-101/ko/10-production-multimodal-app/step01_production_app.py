"""Multimodal Ai 101 - Episode 1: Production app."""

from common import MultimodalApp, synthetic_audio


def run(question: str = "what is in image?") -> dict[str, object]:
    """Run."""
    app = MultimodalApp()
    return app.query("grid-a", question, synthetic_audio())
