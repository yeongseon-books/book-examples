# Alembic 101 (9/10): Deploy ordering and blue/green: synchronizing schema and application code safely

Example code for Alembic 101 series, episode 9.

## Learning Goals

- Understand the core concepts of synchronizing schema and application code safely.

## Assets

| File | Description |
|------|-------------|
| `step01_deploy_ordering.py` | Example code |
| `step_1_schema_add.py` | Example code |
| `step_3_tighten_to_not_null.py` | Example code |
| `step_4_drop_the_old_column.py` | Example code |
| `step_5_align_the_deploy_pipeline.yaml` | Example code |

## How to Run

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/09-deploy-ordering-and-blue-green/step01_deploy_ordering.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/en/09-deploy-ordering-and-blue-green.md)
