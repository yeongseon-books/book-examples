# GitHub Actions 101 (2/10): Workflows and Jobs

Example code for Github Actions 101 series, episode 2.

## Learning Goals

- Understand the core concepts of Workflows and Jobs.

## Assets

| File | Description |
|------|-------------|
| `step01_demo.py` | Example code |
| `step_1_split_into_jobs.yaml` | Example code |
| `step_2_order_with_needs.yaml` | Example code |
| `step_3_multiple_environments_via_matrix.yaml` | Example code |
| `step_4_pass_values_via_outputs.yaml` | Example code |
| `step_5_failure_policy_continue_on_error.yaml` | Example code |

## How to Run

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/02-workflow-and-job/step01_demo.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/en/02-workflow-and-job.md)
