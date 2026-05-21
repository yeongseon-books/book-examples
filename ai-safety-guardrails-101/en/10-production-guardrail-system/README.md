# AI Safety & Guardrails 101 (10/10): Building a Production Guardrail System

Example code for Ai Safety Guardrails 101 series, episode 10.

## Learning Goals

- Understand the core concepts of Building a Production Guardrail System.

## Assets

| File | Description |
|------|-------------|
| `example_audit_event_emitted_by_the_pipel.json` | Example code |
| `fail_open_vs_fail_closed.py` | Example code |
| `parallel_execution_for_independent_check.py` | Example code |
| `pipeline_implementation.py` | Example code |
| `regression_set_in_ci.py` | Example code |
| `step01_guardrail_pipeline.py` | Example code |

## How to Run

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/10-production-guardrail-system/fail_open_vs_fail_closed.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/en/10-production-guardrail-system.md)
