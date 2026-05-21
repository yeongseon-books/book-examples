# Bad
# Test only the few new cases right before v2 ships
new_cases = [test1, test2]
if all(agent_v2.run(c) for c in new_cases):
    deploy_v2()  # Existing cases may have broken

# Good
# Run the full benchmark for regression
v1_results = benchmark.run(agent_v1)
v2_results = benchmark.run(agent_v2)
regressions = [
    case_id for case_id in v1_results["per_case"]
    if v1_results["per_case"][case_id]["success_rate"] >
       v2_results["per_case"][case_id]["success_rate"]
]
if not regressions:
    deploy_v2()
else:
    print(f"Regressions found: {regressions}")
