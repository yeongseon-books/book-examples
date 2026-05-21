"""Generated from book-content article."""

import subprocess

def apply(path):
    subprocess.run(["kubectl", "apply", "-f", path], check=True)
