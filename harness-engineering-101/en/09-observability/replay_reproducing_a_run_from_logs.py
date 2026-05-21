"""Generated from book-content article."""

def replay_trace(trace_id: str, store) -> list[dict]:
    spans = store.load_spans(trace_id)
    results = []
    for span in spans:
        if span.name.startswith("tool."):
            tool_name = span.attributes["tool.name"]
            tool_input = span.attributes["tool.input"]
            actual = invoke_tool(tool_name, tool_input)
            expected = span.attributes["tool.output"]
            results.append({
                "span": span.name,
                "matches": actual == expected,
                "expected": expected,
                "actual": actual,
            })
    return results
