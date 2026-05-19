"""
Step 01 — Check the environment variable
======================================================
Run:
    python step01_check_env.py

Verify that GROQ_API_KEY is set.
The script prints only the first six characters of the key.
"""

import os


def main() -> None:
    """Main."""
    api_key = os.environ["GROQ_API_KEY"]
    print(f"API key loaded: {api_key[:6]}...")
    print("Environment variable check complete.")


if __name__ == "__main__":
    main()
