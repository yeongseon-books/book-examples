from _loader import load_module

m = load_module("05-exploratory-data-analysis.py")


def test_episode_05_eda_report_has_sections() -> None:
    report = m.make_eda_report(seed=42)
    assert "EDA REPORT" in report
    assert "correlation_matrix" in report
