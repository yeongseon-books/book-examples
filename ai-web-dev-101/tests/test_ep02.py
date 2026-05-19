from conftest import load_module


module = load_module("ko/02-prompt-engineering/step01_prompt_builder.py", "ep02")
build_prompt = module.build_prompt
choose_temperature = module.choose_temperature


def test_ep02_prompt_sections_and_temperature() -> None:
    prompt = build_prompt("시니어 리뷰어", "코드 리뷰", ["한국어", "3줄"], "JSON")
    assert "[SYSTEM]" in prompt and "[FORMAT]" in prompt
    assert choose_temperature("code") == 0.2
