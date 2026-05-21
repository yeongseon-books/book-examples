"""Generated from book-content article."""

class E2ETestSuite:
    """End-to-end test suite."""

    def __init__(self, agent):
        self.agent = agent
        self.results = []

    def run_scenario(self, scenario: dict) -> dict:
        """Run a single scenario."""
        recorder = TrajectoryRecorder(scenario["id"])

        try:
            # Run multi-turn conversation
            for turn in scenario["turns"]:
                response = self.agent.chat(turn["user"])

            # Final assertions
            assertions_passed = all(
                self._check_assertion(response, a)
                for a in scenario["assertions"]
            )
            return {
                "scenario_id": scenario["id"],
                "passed": assertions_passed,
                "trajectory": recorder.finalize(response, assertions_passed)
            }
        except Exception as e:
            return {
                "scenario_id": scenario["id"],
                "passed": False,
                "error": str(e)
            }

    def _check_assertion(self, response: str, assertion: dict) -> bool:
        if assertion["type"] == "contains":
            return assertion["value"] in response
        if assertion["type"] == "not_contains":
            return assertion["value"] not in response
        if assertion["type"] == "regex":
            import re
            return bool(re.search(assertion["pattern"], response))
        return False

# Define a scenario
scenario = {
    "id": "booking_flow",
    "turns": [
        {"user": "Find me a KTX from Seoul to Busan tomorrow"},
        {"user": "Show me morning departures"},
        {"user": "Book the first one"}
    ],
    "assertions": [
        {"type": "contains", "value": "booking confirmed"},
        {"type": "contains", "value": "KTX"}
    ]
}
