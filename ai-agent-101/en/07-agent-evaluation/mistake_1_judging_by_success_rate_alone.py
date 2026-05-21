# Bad
if benchmark["success_rate"] > 0.9:
    deploy_to_production()  # Ignores cost and latency

# Good
if (benchmark["success_rate"] > 0.9 and
    benchmark["cost"]["estimated_usd"] / benchmark["total_runs"] < 0.10 and
    benchmark["avg_latency_seconds"] < 5.0):
    deploy_to_production()
