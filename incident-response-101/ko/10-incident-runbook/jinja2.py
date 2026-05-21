"""Generated from book-content article."""

from jinja2 import Template

RUNBOOK_TEMPLATE = """
# Runbook: {{ service_name }}

**Last reviewed**: {{ last_reviewed }}
**Owner**: {{ owner }}

## Trigger

{{ trigger }}

## Diagnosis

1. Check error rate:
   ```
   {{ diagnosis_command }}
   ```
2. Expected: {{ expected_state }}

## Action

{% for step in action_steps %}
{{ loop.index }}. {{ step.description }}
   ```
   {{ step.command }}
   ```
   Expected time: {{ step.time }}
{% endfor %}

## Verification

{{ verification }}

## Escalation

{{ escalation }}
"""


def generate_runbook(config):
    template = Template(RUNBOOK_TEMPLATE)
    return template.render(**config)


# 사용 예시
payment_runbook_config = {
    "service_name": "Payment API High Error Rate",
    "last_reviewed": "2026-05-15",
    "owner": "@payment-team",
    "trigger": "Payment API 5xx rate > 5% for 3 minutes",
    "diagnosis_command": "kubectl logs -n prod payment-api --tail=100 | grep ERROR",
    "expected_state": "No timeout errors, circuit breaker not open",
    "action_steps": [
        {
            "description": "Check current deployment version",
            "command": "kubectl get deploy payment-api -n prod -o jsonpath='{.spec.template.spec.containers[0].image}'",
            "time": "30s",
        },
        {
            "description": "Rollback to previous version if needed",
            "command": "kubectl rollout undo deployment/payment-api -n prod",
            "time": "2min",
        },
        {
            "description": "Verify error rate decreased",
            "command": "# Check Grafana dashboard",
            "time": "1min",
        },
    ],
    "verification": "Error rate < 1% maintained for 5 minutes",
    "escalation": "If not resolved in 30 minutes, page @platform-lead",
}

# Runbook 생성
runbook_md = generate_runbook(payment_runbook_config)
print(runbook_md)

# 파일로 저장
with open("runbook/payment-api-high-error.md", "w", encoding="utf-8") as f:
    f.write(runbook_md)
