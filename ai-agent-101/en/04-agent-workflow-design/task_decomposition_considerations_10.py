# Reusable step library
REUSABLE_STEPS = {
    "web_scraping": {
        "description": "Extract data from website",
        "inputs": ["url", "selector"],
        "outputs": ["raw_data"],
        "tool": "scrape_website"
    },
    "data_cleaning": {
        "description": "Clean and standardize data",
        "inputs": ["raw_data"],
        "outputs": ["clean_data"],
        "tool": "clean_data"
    }
}
