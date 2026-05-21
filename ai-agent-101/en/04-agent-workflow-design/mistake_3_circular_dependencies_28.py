# Clear directionality
dependencies = {
    "Collect data": [],
    "Clean data": ["Collect data"],
    "Analyze": ["Clean data"],
    "Write report": ["Analyze"]
}
# Execution order determinable via topological sort
