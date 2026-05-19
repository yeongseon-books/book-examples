"""Portfolio Project 101 - Episode 10: Portfolio audit."""

from __future__ import annotations

from pathlib import Path

from common import read_text

from ko.ep01_portfolio_scorer import score_portfolio_project
from ko.ep03_readme_linter import lint_readme_sections
from ko.ep05_deployment_readiness import check_deployment_readiness
from ko.ep06_test_docs_coverage import generate_coverage_report


def run_portfolio_audit(project_root: str | Path) -> dict[str, object]:
    """Run portfolio audit."""
    root = Path(project_root)
    readme_ok, readme_missing = lint_readme_sections(read_text(root / "README.md"))
    deploy = check_deployment_readiness(root)
    coverage = generate_coverage_report(root)
    score = score_portfolio_project(
        {
            "has_demo": readme_ok,
            "has_tests": coverage["test_files"] > 0,
            "has_readme": (root / "README.md").exists(),
            "has_deploy": all(deploy.values()),
            "has_monitoring": False,
            "has_ci": (root / ".github").exists(),
        }
    )
    return {
        "score": score,
        "readme_ok": readme_ok,
        "readme_missing": readme_missing,
        "deployment": deploy,
        "coverage": coverage,
    }
