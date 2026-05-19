from conftest import load_module

run = load_module(
    "ko/10-production-multimodal-app/step01_production_app.py", "ep10"
).run


def test_ep10_end_to_end_app() -> None:
    result = run("summarize")
    assert result["top_hit"] in {"doc-1", "doc-2", "doc-3"}
    assert abs(float(result["audio_norm"]) - 1.0) < 1e-6
