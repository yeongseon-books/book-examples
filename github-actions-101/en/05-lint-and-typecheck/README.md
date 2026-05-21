# GitHub Actions 101 (5/10): Lint and Type Check

Example code for Github Actions 101 series, episode 5.

## Learning Goals

- Understand the core concepts of Lint and Type Check.

## Assets

| File | Description |
|------|-------------|
| `.pre-commit-config.yaml` | Example code |
| `step01_demo.py` | Example code |
| `step_1_ruff_workflow.yaml` | Example code |
| `step_3_centralize_config_pyproject_toml.toml` | Example code |
| `step_5_lint_diffs_only_optional.yaml` | Example code |

## How to Run

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/05-lint-and-typecheck/.pre-commit-config.yaml
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/en/05-lint-and-typecheck.md)
