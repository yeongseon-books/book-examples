"""Generated from book-content article."""

def to_nodeport(svc):
    subprocess.run([
        "kubectl", "patch", "svc", svc, "-p",
        '{"spec": {"type": "NodePort"}}',
    ], check=True)
