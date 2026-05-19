from ko.ep10_best_practices import score_module_typing


def test_ep10_ast_checklist_scorer() -> None:
    source = 'from typing import Any\nNameAlias: str = "x"\ndef f(a: int) -> int:\n    return a\n'
    score = score_module_typing(source)
    assert score["annotated_functions"] >= 1
    assert score["has_any"] >= 1
    assert score["aliases"] >= 1
