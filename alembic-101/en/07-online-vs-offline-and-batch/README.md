# Alembic 101 (7/10): Online and offline modes: previewing DDL with --sql and handling SQLite batch

Example code for Alembic 101 series, episode 7.

## Learning Goals

- Understand the core concepts of previewing DDL with --sql and handling SQLite batch.

## Assets

| File | Description |
|------|-------------|
| `automating_render_as_batch.py` | Example code |
| `sqlite_and_batch_mode.sql` | Example code |
| `step01_online_offline_batch.py` | Example code |
| `step_3_apply_sqlite_batch.py` | Example code |
| `step_4_identify_ops_that_do_not_work_off.py` | Example code |

## How to Run

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/07-online-vs-offline-and-batch/automating_render_as_batch.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/en/07-online-vs-offline-and-batch.md)
