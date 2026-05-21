"""Generated from book-content article."""

class AgentBenchmark:
    """Benchmark runner."""

    def __init__(self, name: str):
        self.name = name
        self.test_cases: List[TestCase] = []
        self.cost_tracker = CostTracker()

    def add_case(self, case: TestCase):
        self.test_cases.append(case)

    def run(self, agent, repeat: int = 3) -> dict:
        """Run the benchmark, repeating to reduce noise."""
        all_results = []

        for run_idx in range(repeat):
            for case in self.test_cases:
                start = time.time()
                outcome = agent.run(case.user_input)
                duration = time.time() - start

                all_results.append({
                    "run": run_idx,
                    "case_id": case.task_id,
                    "success": case.success_criteria(outcome),
                    "duration_seconds": duration
                })

        # Aggregate
        cases = {c.task_id for c in self.test_cases}
        per_case = {}
        for case_id in cases:
            case_runs = [r for r in all_results if r["case_id"] == case_id]
            per_case[case_id] = {
                "success_rate": sum(1 for r in case_runs if r["success"]) / len(case_runs),
                "avg_duration": sum(r["duration_seconds"] for r in case_runs) / len(case_runs)
            }

        return {
            "benchmark": self.name,
            "agent": agent.__class__.__name__,
            "total_runs": len(all_results),
            "overall_success_rate": sum(1 for r in all_results if r["success"]) / len(all_results),
            "per_case": per_case,
            "cost": self.cost_tracker.report()
        }
