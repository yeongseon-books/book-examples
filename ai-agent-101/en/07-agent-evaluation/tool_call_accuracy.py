"""Generated from book-content article."""

@dataclass
class ToolCallExpectation:
    """Expected tool call."""
    tool_name: str
    required_args: dict
    optional_args: dict = None

def evaluate_tool_call(
    actual_tool: str,
    actual_args: dict,
    expected: ToolCallExpectation
) -> dict:
    """Evaluate a single tool call."""
    result = {
        "tool_correct": actual_tool == expected.tool_name,
        "args_correct": True,
        "missing_args": [],
        "wrong_args": []
    }

    for key, expected_val in expected.required_args.items():
        if key not in actual_args:
            result["missing_args"].append(key)
            result["args_correct"] = False
        elif actual_args[key] != expected_val:
            result["wrong_args"].append({
                "key": key,
                "expected": expected_val,
                "actual": actual_args[key]
            })
            result["args_correct"] = False

    return result

# Example usage
expected = ToolCallExpectation(
    tool_name="get_weather",
    required_args={"city": "Seoul"}
)
actual_tool = "get_weather"
actual_args = {"city": "Seoul", "unit": "celsius"}
print(evaluate_tool_call(actual_tool, actual_args, expected))
# {'tool_correct': True, 'args_correct': True, ...}
