# Bad
result = agent.run(test_input)
if result == expected:
    print("Pass")

# Good
results = [agent.run(test_input) for _ in range(10)]
pass_rate = sum(1 for r in results if r == expected) / 10
print(f"Pass rate: {pass_rate:.0%}")
