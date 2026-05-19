from common import MultimodalApp, synthetic_audio


def run(question: str = "what is in image?") -> dict[str, object]:
    app = MultimodalApp()
    return app.query("grid-a", question, synthetic_audio())
