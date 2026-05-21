"""Generated from book-content article."""

import subprocess


def create(name):
    subprocess.run(["helm", "create", name], check=True)
