# A needs B result, B needs C result, C needs A result
dependencies = {
    "Analyze": ["Collect data"],
    "Collect data": ["Write report"],
    "Write report": ["Analyze"]  # Circular!
}
# Cannot execute
