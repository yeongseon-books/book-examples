# Alembic 101 (6/10): Data migrations: separating schema changes from data changes

Example code for Alembic 101 series, episode 6.

## Learning Goals

- Understand the core concepts of separating schema changes from data changes.

## Assets

| File | Description |
|------|-------------|
| `batched_processing.py` | Example code |
| `before_after.py` | Example code |
| `before_after_05.py` | Example code |
| `step01_data_backfill.py` | Example code |
| `step_1_add_the_schema.py` | Example code |
| `step_2_data_backfill_revision.py` | Example code |
| `step_3_tighten_the_schema.py` | Example code |
| `step_5_verification_query.py` | Example code |
| `two_styles_of_op_execute.py` | Example code |

## How to Run

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/06-data-migrations/batched_processing.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/en/06-data-migrations.md)
