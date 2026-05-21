# Alembic 101 (8/10): Downgrade strategy: when to write it for real and when to forbid it

Example code for Alembic 101 series, episode 8.

## Learning Goals

- Understand the core concepts of when to write it for real and when to forbid it.

## Assets

| File | Description |
|------|-------------|
| `before_after.py` | Example code |
| `before_after_05.py` | Example code |
| `declaring_no_downgrade.py` | Example code |
| `step01_downgrade_policy.py` | Example code |
| `step_1_write_a_reversible_revision.py` | Example code |
| `step_2_block_an_irreversible_revision.py` | Example code |
| `step_3_handle_a_rename_via_expand_contra.py` | Example code |
| `step_3_handle_a_rename_via_expand_contra_09.py` | Example code |
| `step_3_handle_a_rename_via_expand_contra_10.py` | Example code |

## How to Run

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/08-downgrade-strategy/before_after.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/en/08-downgrade-strategy.md)
