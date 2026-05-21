# Split into 10 tiny steps
steps = [
    "Open URL",
    "Wait for page load",
    "Extract title",
    "Validate title",
    "Extract body",
    "Validate body",
    "Extract links",
    "Validate links",
    "Save data",
    "Confirm save"
]
# LLM call at each step → 10 calls, slow and expensive
