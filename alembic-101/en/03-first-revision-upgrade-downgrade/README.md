# Alembic 101 (3/10): Your first revision: writing upgrade and downgrade by hand

Example code for Alembic 101 series, episode 3.

## Learning Goals

- Understand the core concepts of writing upgrade and downgrade by hand.

## Assets

| File | Description |
|------|-------------|
| `before_after.py` | Example code |
| `before_after_03.py` | Example code |
| `step01_upgrade_downgrade.py` | Example code |
| `step_2_write_upgrade.py` | Example code |
| `step_3_write_downgrade_reverse_order.py` | Example code |
| `step_5_changing_a_column_on_sqlite_batch.py` | Example code |
| `step_6_fixing_data_with_op_execute.py` | Example code |
| `the_auto_generated_revision_file.py` | Example code |

## How to Run

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/03-first-revision-upgrade-downgrade/before_after.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/en/03-first-revision-upgrade-downgrade.md)
